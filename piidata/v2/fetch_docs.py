"""Download the documentation listed in sources.py into cache/v2_docs/ (network, run once).

Uses one GitHub API call per (repo, subtree) to list files and raw.githubusercontent.com
for file contents. Everything is cached, so re-running costs nothing. Set GITHUB_TOKEN to
lift the 60-calls-per-hour anonymous API limit.

    python -m piidata.v2.fetch_docs
"""
import hashlib, json, os, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from .sources import SOURCES, DOC_EXTENSIONS

ROOT = Path(__file__).resolve().parents[2]
CACHE = ROOT / 'cache' / 'v2_docs'
UA = {'User-Agent': 'piidata-docs-fetch'}


def _get(url, accept=None, retries=3):
    headers = dict(UA)
    if accept: headers['Accept'] = accept
    token = os.environ.get('GITHUB_TOKEN')
    if token and 'api.github.com' in url: headers['Authorization'] = f'Bearer {token}'
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as r:
                return r.read()
        except Exception as exc:
            if attempt == retries - 1: raise
            time.sleep(1.5 * (attempt + 1))


def _slug(repo, subtree):
    return repo.replace('/', '__') + '__' + subtree.replace('/', '_')


def list_files(repo, subtree):
    path = CACHE / 'trees' / (_slug(repo, subtree) + '.json')
    if path.exists():
        return json.loads(path.read_text(encoding='utf-8'))
    raw = _get(f'https://api.github.com/repos/{repo}/git/trees/HEAD:{subtree}?recursive=1')
    data = json.loads(raw)
    if 'tree' not in data:
        raise RuntimeError(f'cannot list {repo}/{subtree}: {data}')
    files = sorted(x['path'] for x in data['tree'] if x['type'] == 'blob' and x['path'].lower().endswith(DOC_EXTENSIONS))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(files), encoding='utf-8')
    return files


def pick(files, n, key):
    """Deterministic, spread-out sample of n files (stable across runs)."""
    files = [f for f in files if '/translations/' not in f and not f.startswith('translations/')
             and 'changelog' not in f.lower() and 'release-notes' not in f.lower()
             and 'contributing' not in f.lower()]
    ranked = sorted(files, key=lambda f: hashlib.sha256(f'{key}:{f}'.encode()).hexdigest())
    return sorted(ranked[:n])


def fetch_one(repo, subtree, rel):
    out = CACHE / 'files' / _slug(repo, subtree) / rel
    if out.exists():
        return out
    data = _get(f'https://raw.githubusercontent.com/{repo}/HEAD/{subtree}/{rel}')
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(data)
    return out


def main():
    CACHE.mkdir(parents=True, exist_ok=True)
    manifest = []
    jobs = []
    for repo, subtree, licence, role, max_files in SOURCES:
        try:
            files = list_files(repo, subtree)
        except Exception as exc:
            print(f'!! skip {repo}/{subtree}: {exc}', file=sys.stderr)
            continue
        chosen = pick(files, max_files, repo + subtree)
        print(f'{role:12s} {repo}/{subtree}: {len(files)} doc files, using {len(chosen)}')
        for rel in chosen:
            jobs.append((repo, subtree, rel))
            manifest.append({'repo': repo, 'subtree': subtree, 'path': rel, 'licence': licence, 'role': role,
                             'url': f'https://github.com/{repo}/blob/HEAD/{subtree}/{rel}'})
    with ThreadPoolExecutor(8) as pool:
        results = list(pool.map(lambda j: _safe_fetch(*j), jobs))
    ok = {(r, s, p) for (r, s, p), good in zip(jobs, results) if good}
    manifest = [m for m in manifest if (m['repo'], m['subtree'], m['path']) in ok]
    (CACHE / 'manifest.json').write_text(json.dumps(manifest, indent=1), encoding='utf-8')
    print(f'fetched {len(manifest)}/{len(jobs)} files into {CACHE}')


def _safe_fetch(repo, subtree, rel):
    try:
        fetch_one(repo, subtree, rel); return True
    except Exception as exc:
        print(f'!! {repo}/{subtree}/{rel}: {exc}', file=sys.stderr); return False


if __name__ == '__main__':
    main()
