"""Build the v2 data: python -m piidata.v2.build  (run piidata.v2.fetch_docs once first).

Adds to the v1 files in data/ (they are not modified). Writes data/v2/*.jsonl plus reports.
"""
import argparse, collections, hashlib, json, random, re
from pathlib import Path

from ..segmenter import split_segments
from ..qc import check_addresses
from . import templates as T
from .extract import doc_segments, needs_review
from .fetch_docs import CACHE, _slug
from .generate import (clean_and_twin_rows, attack_rows, composed_attack_rows, template_split, prose_swap, is_imperative, v2_slots,
                       expand, CLEAN_SETS, _row)
from .sources import ROLE_CAPS, PER_SOURCE_CAP

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'data' / 'v2'
REPORTS = ROOT / 'reports'
SEED = 1729
GIVEAWAYS = [x.strip().lower() for x in (ROOT / 'injections' / 'giveaway_tokens.txt').read_text(encoding='utf-8').splitlines() if x.strip()]
SUSPECT = re.compile(r'ignore (all |any )?(the )?(previous|prior|above) (instructions|prompts?)|disregard (all )?(previous|prior)|'
                     r'you are now|pretend (to be|you are)|act as (an?|the) |from now on,? you', re.I)
PROSE_SWAPS = {'train': 420, 'dev': 90}
ESCALATION = re.compile(r'unlimited|allowance|spending (limit|cap)|standing permission|trusted spender|persistent spender|'
                        r'never expires|transfer cap|\b(raise|remove|increase|override|change)\b[^.]{0,30}\b(limit|cap)\b', re.I)
K_VARIANTS = 3


def norm(t):
    t = t.lower()
    t = re.sub(r'0x[0-9a-f]{40}', ' <addr> ', t)
    t = re.sub(r'https?://\S+', ' <url> ', t)
    t = re.sub(r'\b\d+(?:[.,]\d+)*\b', ' <num> ', t)
    t = re.sub(r'\b(eth|usdc|usdt|dai|weth|link)\b', ' <tok> ', t)
    t = re.sub(r'[\w-]+\.eth\b', ' <ens> ', t)
    return re.sub(r'\W+', ' ', t).strip()


# ---------------------------------------------------------------- template grouping
def template_groups():
    """Merge near-duplicate templates (Jaccard >= .6 on words) so they share a split."""
    items = []
    for source, (entries, short) in CLEAN_SETS.items():
        for i, (c, tw) in enumerate(entries):
            items.append((f'{short}-{i:03d}', c + (' ' + tw if tw else '')))
    for fam, entries in T.ATTACKS.items():
        for i, t in enumerate(entries):
            items.append((f'atk-{fam}-{i:03d}', ' '.join(t) if isinstance(t, list) else t))
    for fam, frames in T.FRAMES.items():
        for i, t in enumerate(frames):
            items.append((f'cmp-{fam}-{i:02d}', re.sub(r'\{(act|Act|sact|suffix)\}', '', t)))
    rng = random.Random(0)
    words = {g: set(norm(expand(t, rng).replace('{ADDR}', '')).split()) for g, t in items}
    parent = {g: g for g, _ in items}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    gs = [g for g, _ in items]
    merged = []
    for a in range(len(gs)):
        for b in range(a + 1, len(gs)):
            wa, wb = words[gs[a]], words[gs[b]]
            if len(wa) >= 4 and len(wb) >= 4 and len(wa & wb) / len(wa | wb) >= .6:
                ra, rb = find(gs[a]), find(gs[b])
                if ra != rb:
                    parent[rb] = ra; merged.append((gs[a], gs[b]))
    return (lambda g: template_split(find(g) if g in parent else g, SEED)), merged


# ---------------------------------------------------------------- real documentation prose
REVIEWED = OUT / 'reviewed_prose.json'   # sentences from the review queue checked by hand as benign
AGENT_WORDS = re.compile(r'\b(agents?|assistants?|AI|bots?|LLMs?|automated|copilot)\b', re.I)
AGENT_FORCE = {'train': 220, 'dev': 60, 'test_docs': 60, 'test_wallet': 30}


def prose_rows():
    manifest = json.loads((CACHE / 'manifest.json').read_text(encoding='utf-8'))
    allow = set(json.loads(REVIEWED.read_text(encoding='utf-8'))['benign']) if REVIEWED.exists() else set()
    by_role = collections.defaultdict(lambda: collections.defaultdict(list))
    forced = collections.defaultdict(list)
    review, seen = [], set()
    for m in manifest:
        raw = (CACHE / 'files' / _slug(m['repo'], m['subtree']) / m['path']).read_text(encoding='utf-8', errors='replace')
        for s in doc_segments(raw):
            key = norm(s)
            if key in seen: continue
            seen.add(key)
            if (needs_review(s) or SUSPECT.search(s)) and s not in allow:
                review.append((m['role'], m['repo'], s)); continue
            if AGENT_WORDS.search(s) or s in allow:
                forced[m['role']].append((s, m)); continue   # benign agent/AI mentions: always kept
            by_role[m['role']][m['repo']].append((s, m))
    rows = []
    split_of = {'train': 'train', 'dev': 'dev', 'test_docs': 'test', 'test_wallet': 'test'}
    set_of = {'train': 'prose_train', 'dev': 'dev_prose', 'test_docs': 'test_docs', 'test_wallet': 'test_wallet_help'}
    for role, repos in by_role.items():
        rng = random.Random(f'{SEED}:{role}')
        picked = []
        for repo in sorted(repos):
            items = repos[repo]
            rng.shuffle(items)
            picked.extend(items[:PER_SOURCE_CAP[role]])
        rng.shuffle(picked)
        if role in ('train', 'dev'):
            used = {id(x) for x in picked[:ROLE_CAPS[role]]}
            rest = [x for items in repos.values() for x in items if id(x) not in used and is_imperative(x[0])]
            rng.shuffle(rest)
            picked = picked[:ROLE_CAPS[role]] + rest[:PROSE_SWAPS[role]]
            caps = len(picked)
        else:
            caps = ROLE_CAPS[role]
        extra = forced.get(role, [])
        rng.shuffle(extra)
        picked = picked[:caps] + extra[:AGENT_FORCE[role]]
        caps = len(picked)
        for k, (s, m) in enumerate(picked[:caps]):
            rows.append(_row(s, 0, split_of[role], 'v2_prose', f'prose-{role}', k, family=None, pair_id=None,
                             v2_set=set_of[role], origin_repo=m['repo'], origin_url=m['url'], licence=m['licence']))
    return rows, review


CLUTTER_REAL = {'train': 420, 'dev': 80}


def real_clutter_rows():
    """Short headings and nav-like lines (1-3 words) from the train/dev doc sources: real page clutter."""
    from .extract import to_plain_text
    manifest = json.loads((CACHE / 'manifest.json').read_text(encoding='utf-8'))
    pools = collections.defaultdict(dict)
    for m in manifest:
        if m['role'] not in CLUTTER_REAL: continue
        raw = (CACHE / 'files' / _slug(m['repo'], m['subtree']) / m['path']).read_text(encoding='utf-8', errors='replace')
        for seg in split_segments(to_plain_text(raw)):
            t = seg.text.strip()
            w = t.split()
            if 1 <= len(w) <= 3 and re.fullmatch(r"[A-Za-z][A-Za-z0-9 '&/-]*[A-Za-z0-9]", t) and not needs_review(t):
                pools[m['role']].setdefault(t.lower(), (t, m))
    rows = []
    for role, n in CLUTTER_REAL.items():
        items = sorted(pools[role].values(), key=lambda x: hashlib.sha256(x[0].encode()).hexdigest())[:n]
        for k, (t, m) in enumerate(items):
            rows.append(_row(t, 0, role, 'v2_web_clutter_real', f'clutter-real-{role}', k, family=None, pair_id=None,
                             v2_set='clutter', origin_repo=m['repo'], origin_url=m['url'], licence=m['licence']))
    return rows


def swap_rows(prose):
    rng = random.Random(SEED + 5)
    out = []
    for split, n in PROSE_SWAPS.items():
        cands = [r for r in prose if r['split'] == split and is_imperative(r['text'])]
        rng.shuffle(cands)
        for k, r in enumerate(cands[:n]):
            twin = prose_swap(r['text'], rng, v2_slots(rng))
            segs = [s.text for s in split_segments(twin)]
            if len(segs) != 1: continue
            r['pair_id'] = f'swap-{split}-{k}'
            out.append(_row(twin, 1, split, 'v2_prose_swap', f'swap-{split}', k, family='prose_swap',
                            style='contrast_pair', pair_id=r['pair_id'], v2_set=r['v2_set'], origin_repo=r['origin_repo'],
                            origin_url=r['origin_url'], licence=r['licence']))
    return out


# ---------------------------------------------------------------- v1 rework
def v1_preamble_ids():
    """v1 rows labelled injected that are only a lead-in to the attack ("Result: verification=passed.",
    "[END OF DOCUMENT]", "Q: Are the payment details final?"). They carry no attack on their own."""
    out = {}
    for sp in ('train', 'val', 'test_id', 'test_heldout'):
        docs = {d['doc_id']: d for d in map(json.loads, (ROOT / 'data' / f'docs_{sp}.jsonl').open(encoding='utf-8'))}
        ids = []
        for line in (ROOT / 'data' / f'{sp}.jsonl').open(encoding='utf-8'):
            r = json.loads(line)
            if r['label'] != 1 or r.get('style') == 'multi_sentence_split': continue
            d = docs.get(r['doc_id'])
            if not d or 'labels' not in d: continue
            idx = [i for i, l in enumerate(d['labels']) if l]
            if idx and r['seg_index'] < max(idx): ids.append({'id': r['id'], 'text': r['text']})
        out[sp] = ids
    return out


def v1_texts(*splits):
    s = set()
    for sp in splits:
        for line in (ROOT / 'data' / f'{sp}.jsonl').open(encoding='utf-8'):
            s.add(norm(json.loads(line)['text']))
    return s


# ---------------------------------------------------------------- eval-set naming
def eval_set(r):
    if r['split'] == 'train':
        return 'train'
    src, fam = r['source'], r.get('family')
    if r['split'] == 'dev':
        if src == 'v2_prose': return 'dev_prose'
        if src in ('v2_attack',): return 'dev_attacks'
        if src in ('v2_contrast_twin', 'v2_prose_swap') or r.get('pair_id_has_twin'): return 'dev_contrast'
        return 'dev_synth_clean'
    if src == 'v2_prose':
        return r['v2_set']  # test_docs | test_wallet_help
    if fam in T.TEST_ONLY_FAMILIES: return 'test_unseen_styles'
    if src == 'v2_attack': return 'test_attacks_v2'
    if src == 'v2_wallet_help' and not r.get('pair_id_has_twin'): return 'test_wallet_help_synth'
    if src == 'v2_contrast_twin' or r.get('pair_id_has_twin'): return 'test_contrast'
    return 'test_synth_clean'


def build(args):
    group_split, merged = template_groups()
    def gs(group):
        return group_split(group)
    synth = (clean_and_twin_rows(SEED, gs) + attack_rows(SEED, gs, test_only_to_test=not args.train_on_unseen_styles)
             + composed_attack_rows(SEED, gs))
    prose, review = prose_rows()
    swaps = swap_rows(prose)
    rows = synth + prose + swaps + real_clutter_rows()
    twin_pairs = {r['pair_id'] for r in rows if r['label'] == 1 and r.get('pair_id')}
    for r in rows:
        r['pair_id_has_twin'] = bool(r.get('pair_id') in twin_pairs)

    # ---- dedup within split, then remove dev/test rows that also appear in training data
    v1_train = v1_texts('train', 'train_crai')
    v1_eval = v1_texts('val', 'test_id', 'test_heldout', 'dev_ood_crai', 'test_ood_crai')
    # Within a split keep up to K slot-only variants of one normalised form (prose: 1).
    kept, seen, count = [], collections.defaultdict(set), collections.Counter()
    for r in rows:
        k = norm(r['text'])
        cap = 1 if r['source'] == 'v2_prose' else K_VARIANTS
        if count[(r['split'], k)] >= cap: continue
        count[(r['split'], k)] += 1; seen[r['split']].add(k); kept.append(r)
    kept = list({(r['split'], r['text']): r for r in kept}.values())
    train_keys = seen['train'] | v1_train
    dropped = collections.Counter()
    final = []
    for r in kept:
        k = norm(r['text'])
        if r['split'] == 'train' and k in v1_eval: dropped['train_in_v1_eval'] += 1; continue
        if r['split'] in ('dev', 'test') and k in train_keys: dropped[f'{r["split"]}_in_train'] += 1; continue
        if r['split'] == 'test' and k in seen['dev']: dropped['test_in_dev'] += 1; continue
        final.append(r)
    # v1's test_heldout holds out the escalate_permission goal; keep that family out of v2 train/dev
    # too (it stays in v2 test), so the held-out number remains a real held-out measure.
    held = []
    for r in final:
        if r['split'] in ('train', 'dev') and r['label'] == 1 and ESCALATION.search(r['text']):
            dropped[f'{r["split"]}_escalation_held_out'] += 1
        else:
            held.append(r)
    final = held
    for r in final:
        r['eval_set'] = eval_set(r)
        r.pop('pair_id_has_twin', None)

    # ---- QC
    for r in final:
        assert len(split_segments(r['text'])) == 1, ('not a single segment', r['text'])
    inj_text = '\n'.join(r['text'].lower() for r in final if r['label'] == 1)
    bad = [g for g in GIVEAWAYS if g in inj_text]
    assert not bad, f'giveaway tokens in injected rows: {bad}'
    check_addresses([r for r in final if r['source'] != 'v2_prose'])
    tr_groups = {r['template_id'] for r in final if r['split'] == 'train' and not r.get('origin_repo')}
    for r in final:
        if r['split'] != 'train' and not r.get('origin_repo') and r['source'] != 'v2_test_only_clean':
            assert r['template_id'] not in tr_groups, ('template leakage', r['template_id'])
    tr_repos = {r.get('origin_repo') for r in final if r['split'] == 'train' and r.get('origin_repo')}
    for r in final:
        if r['split'] != 'train' and r.get('origin_repo'):
            assert r['origin_repo'] not in tr_repos, ('prose source leakage', r['origin_repo'])

    # ---- write
    OUT.mkdir(parents=True, exist_ok=True)
    by_set = collections.defaultdict(list)
    for r in final:
        by_set['train' if r['split'] == 'train' else ('dev' if r['split'] == 'dev' else r['eval_set'])].append(r)
    for old in OUT.glob('*.jsonl'): old.unlink()
    for name, rs in by_set.items():
        with (OUT / f'{name}.jsonl').open('w', encoding='utf-8', newline='\n') as f:
            for r in rs: f.write(json.dumps(r, ensure_ascii=False, separators=(',', ':')) + '\n')
    pre = v1_preamble_ids()
    (OUT / 'v1_drop_from_train.json').write_text(json.dumps(
        {'reason': 'lead-in sentences of multi-sentence seeds labelled injected but carrying no attack on their own',
         'ids': {sp: [x['id'] for x in v] for sp, v in pre.items()}}, indent=1), encoding='utf-8')
    write_reports(final, by_set, review, dropped, merged, pre)
    return final, by_set


def write_reports(final, by_set, review, dropped, merged, pre):
    REPORTS.mkdir(exist_ok=True)
    L = ['# v2 data build statistics', '', '| File | Rows | Injected | Clean | Injected % |', '|---|---:|---:|---:|---:|']
    for name in sorted(by_set):
        rs = by_set[name]; n1 = sum(r['label'] for r in rs)
        L.append(f'| data/v2/{name}.jsonl | {len(rs)} | {n1} | {len(rs) - n1} | {100 * n1 / len(rs):.1f} |')
    for name in ('train', 'dev'):
        L += ['', f'## {name}: rows by source / eval subset and label', '', '| Source | Subset | Label | Rows |', '|---|---|---:|---:|']
        c = collections.Counter((r['source'], r['eval_set'] if name != 'train' else '-', r['label']) for r in by_set[name])
        L += [f'| {s} | {e} | {l} | {n} |' for (s, e, l), n in sorted(c.items())]
    L += ['', '## Attack families (all splits)', '', '| Family | Split | Rows |', '|---|---|---:|']
    c = collections.Counter((r.get('family') or '-', r['split']) for r in final if r['label'] == 1)
    L += [f'| {f} | {s} | {n} |' for (f, s), n in sorted(c.items())]
    L += ['', '## Real prose sources', '', '| Repo | Split | Rows |', '|---|---|---:|']
    c = collections.Counter((r.get('origin_repo'), r['split']) for r in final if r['source'] == 'v2_prose')
    L += [f'| {f} | {s} | {n} |' for (f, s), n in sorted(c.items())]
    L += ['', '## Removed during dedup', ''] + [f'- {k}: {v}' for k, v in dropped.items()]
    L += ['', f'## Near-duplicate templates merged into one split ({len(merged)})', ''] + [f'- {a} ~ {b}' for a, b in merged]
    L += ['', '## v1 rows to drop from training (lead-in sentences labelled injected)', '']
    for sp, v in pre.items():
        L.append(f'- {sp}: {len(v)}' + ''.join(f'\n  - `{x["text"][:100]}`' for x in v[:6]))
    (REPORTS / 'v2_stats.md').write_text('\n'.join(L) + '\n', encoding='utf-8')

    rng = random.Random(SEED)
    R = ['# v2 prose: review queue and manual-pass sample', '',
         'Sentences mentioning AI tools/prompting or matching injection phrasing were removed from the clean pool '
         '(listed first). Below that is a random sample of kept prose per split for a manual pass.', '',
         f'## Removed ({len(review)})', '']
    R += [f'- [{role}] {repo}: {s}' for role, repo, s in review]
    for sp in ('train', 'dev', 'test'):
        pool = [r for r in final if r['source'] == 'v2_prose' and r['split'] == sp]
        R += ['', f'## Kept sample: {sp} ({len(pool)} rows total)', '']
        R += [f'- {r["origin_repo"]}: {r["text"]}' for r in rng.sample(pool, min(60, len(pool)))]
    (REPORTS / 'v2_prose_review.md').write_text('\n'.join(R) + '\n', encoding='utf-8')

    S = ['# v2 documentation sources and licences', '',
         'Sentences extracted from these repositories are redistributed under their licences. '
         'CC BY / CC BY-SA content requires attribution: each row carries `origin_url` and `licence`.', '',
         '| Repo | Licence | Split | Rows |', '|---|---|---|---:|']
    c = collections.Counter((r.get('origin_repo'), r.get('licence'), r['split']) for r in final if r.get('origin_repo'))
    S += [f'| https://github.com/{a} | {b} | {s} | {n} |' for (a, b, s), n in sorted(c.items())]
    (OUT / 'SOURCES.md').write_text('\n'.join(S) + '\n', encoding='utf-8')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--train-on-unseen-styles', action='store_true',
                    help='put role_play / quoted_email templates into train/dev too (removes them as a held-out test)')
    args = ap.parse_args()
    final, by_set = build(args)
    for name in sorted(by_set):
        rs = by_set[name]
        print(f'{name:24s} {len(rs):6d} rows  injected={sum(r["label"] for r in rs) / len(rs):.1%}')


if __name__ == '__main__':
    main()
