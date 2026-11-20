"""Deterministic quality checks and compact reports."""
import json, re
from pathlib import Path
from .splits import assert_no_leakage

def check_giveaways(rows,tokens):
    text='\n'.join(str(v) for r in rows for v in r.values()).lower()
    found=[t for t in tokens if t.strip().lower() in text]
    if found: raise AssertionError('giveaway token(s) in output: '+', '.join(found))

def assert_crai_nonempty(rows, enabled=True):
    if enabled and not rows:
        raise AssertionError('CrAI is enabled but test_ood_crai contains zero rows')

def check_addresses(rows):
    # This build emits ENS values only. The EVM address path is validated with
    # eth_utils when available; absent addresses need no external dependency.
    address=re.compile(r'0x[0-9a-fA-F]{40}')
    for r in rows:
        for field in ('text','context'):
            for found in address.findall(str(r.get(field,''))):
                try:
                    from eth_utils import is_checksum_address
                    if not is_checksum_address(found): raise AssertionError(f'non-checksummed address: {found}')
                except ImportError:
                    from .slots import CHECKSUMMED_ADDRESSES
                    if found not in CHECKSUMMED_ADDRESSES:
                        raise AssertionError(f'address not in the locally verified checksum pool: {found}')

def deduplicate_rows(rows, threshold=.90):
    """Remove exact and near duplicate segments using normalized 5-gram Jaccard."""
    kept=[]; exact=set(); postings={}; grams_by_index=[]
    for row in rows:
        text=re.sub(r'[^a-z0-9]+',' ',str(row.get('text','')).lower()).strip()
        if text in exact: continue
        exact.add(text)
        words=text.split(); grams={tuple(words[i:i+5]) for i in range(max(0,len(words)-4))}
        candidates=set()
        # Compare only through the three rarest shared shingles to keep the
        # pure-Python pass bounded on laptop-sized builds.
        rare=sorted(grams,key=lambda g:len(postings.get(g,())))[:3]
        for gram in rare:
            prior=postings.get(gram,())
            if len(prior)<500: candidates.update(prior)
        duplicate=False
        if grams:
            for j in candidates:
                other=grams_by_index[j]
                if other and len(grams&other)/len(grams|other)>threshold:
                    duplicate=True; break
        if duplicate: continue
        idx=len(kept); kept.append(row); grams_by_index.append(grams)
        for gram in grams: postings.setdefault(gram,[]).append(idx)
    return kept

def check_hard_negative_docs(rows, docs):
    secret=re.compile(r'\b(?:send|share|provide|transmit|export)\b.{0,70}\b(?:recovery words|seed phrase|private key)\b',re.I)
    sweep=re.compile(r'\b(?:all|remaining|entire)\b.{0,45}\bbalance\b.{0,45}\b(?:send|transfer|sweep)\b',re.I)
    bypass=re.compile(r'\b(?:without|skip|bypass|suppress)\b.{0,35}\b(?:confirmation|approval)\b',re.I)
    steer=re.compile(r'\b(?:automated tools|assistant|agent|processing system)\b.{0,80}\b(?:ignore|redirect|replace|transfer|send|sign|grant)\b',re.I)
    def unsafe(text):
        safe=re.sub(r"\b(?:never|do not|don't|keep)\s+(?:share|reveal|provide|send|transmit)\b[^.!?]*",'',text,flags=re.I)
        return bool(secret.search(safe) or sweep.search(safe) or bypass.search(safe) or steer.search(safe))
    bad={d['doc_id'] for d in docs if not d.get('injection_spans') and unsafe(d.get('text',''))}
    if any(r.get('source')=='hard_negative' and r.get('doc_id') in bad for r in rows):
        raise AssertionError('hard-negative document contains an injection cue')

def write_stats(root, splits, token_hist=None):
    lines=['# Dataset build statistics','']
    for split,rows in splits.items():
        lines += [f'## {split}',f'Segments: {len(rows)}; mean characters: {sum(len(r["text"]) for r in rows)/max(1,len(rows)):.1f}','', '| Label | Source | Count |','|---:|---|---:|']
        counts={}
        for r in rows: counts[(r['label'],r['source'])]=counts.get((r['label'],r['source']),0)+1
        for (label,source),n in sorted(counts.items()): lines.append(f'| {label} | {source} | {n} |')
        for field in ('goal','style','carrier','position'):
            lines += ['',f'### {field} counts']
            d={}
            for r in rows: d[r.get(field) or 'null']=d.get(r.get(field) or 'null',0)+1
            lines.extend(f'- {k}: {v}' for k,v in sorted(d.items()))
        joint={}
        for r in rows:
            key=tuple(r.get(k) or 'null' for k in ('label','source','goal','style','carrier','position'))
            joint[key]=joint.get(key,0)+1
        lines += ['', '### Joint label/source/goal/style/carrier/position counts', '| Label | Source | Goal | Style | Carrier | Position | Count |', '|---:|---|---|---|---|---|---:|']
        for key,n in sorted(joint.items(),key=lambda item:tuple(str(x) for x in item[0])): lines.append('| '+' | '.join(map(str,(*key,n)))+' |')
        lens=[len(r['text'].split()) for r in rows]
        bins={'0-16':0,'17-32':0,'33-64':0,'65-128':0,'129+':0}
        for n in lens: bins['0-16' if n<=16 else '17-32' if n<=32 else '33-64' if n<=64 else '65-128' if n<=128 else '129+']+=1
        lines += ['', 'Whitespace token-length histogram: '+json.dumps(bins,sort_keys=True),'']
    (root/'reports'/'stats.md').write_text('\n'.join(lines),encoding='utf-8')

