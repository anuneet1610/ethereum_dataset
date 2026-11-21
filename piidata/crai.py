"""CrAI-SafeFuncCall OOD import, trailing-payload heuristic, and audit helpers."""
import re
import hashlib
from collections.abc import Mapping

from .segmenter import split_segments

_CUES=(
    ('agent_or_system', re.compile(r'\b(?:assistant|agent|automated|processor|system|bot)\b',re.I)),
    ('tool_or_function', re.compile(r'\b(?:tools?|functions?|tool calls?|function calls?)\b|\bcall(?:ing)?\s+[\'"`]?\w+',re.I)),
    ('instruction', re.compile(r'\b(?:ignore|instruct\w*|always|must|should|invoke|use)\b|\bbefore\s+fetching\b',re.I)),
    ('wallet_action', re.compile(r'\b(?:transfer\w*|redirect\w*|send\w*|leak\w*)\b',re.I)),
)
_GIVEAWAY=re.compile(r'stealth_transfer|malicious_wallet_[a-z0-9_]*|0xdeadbeef|malicious|attacker|evil|hacker',re.I)
_FULL_ADDRESS=re.compile(r'0x[0-9a-fA-F]{40}')


def normalize_key(value):
    """Case and separator insensitive key normalization."""
    return re.sub(r'[^a-z0-9]+','',str(value).casefold())


def is_memory_injection(value):
    return normalize_key(value)=='memoryinjection'


def _rule_for(sentence):
    for name,pattern in _CUES:
        if pattern.search(sentence): return name
    return None


def label_memory_with_audit(memory):
    """Label the payload sentence and every sentence after its first heuristic cue."""
    segs=split_segments(memory); first=None; rule=None
    for i,seg in enumerate(segs):
        rule=_rule_for(seg.text)
        if rule:
            first=i; break
    labels=[(seg.text,int(first is not None and i>=first)) for i,seg in enumerate(segs)]
    return labels,first,rule or 'none'


def label_memory(memory):
    """Compatibility helper returning ``(sentence, label)`` pairs."""
    return label_memory_with_audit(memory)[0]


def sanitize(text):
    """Rewrite giveaway names and addresses to plausible wallet-domain terms."""
    text=_FULL_ADDRESS.sub('wallet-service.eth',text)
    text=re.sub(r'0xdeadbeef','wallet-service.eth',text,flags=re.I)
    text=re.sub(r'stealth_transfer','transfer',text,flags=re.I)
    text=re.sub(r'malicious_wallet_[a-z0-9_]*','collection.eth',text,flags=re.I)
    return _GIVEAWAY.sub('wallet-service',text)


def _find_columns(table, rows):
    columns=list(getattr(table,'column_names',[]) or [])
    if not columns and rows: columns=list(rows[0].keys())
    by_key={normalize_key(name):name for name in columns}
    memory_col=by_key.get('memory')
    attack_col=by_key.get('attack')
    if memory_col is None or attack_col is None:
        raise ValueError(f"CrAI split is missing required memory/attack columns; found {columns!r}")
    row_id_col=by_key.get('id') or by_key.get('rowid')
    return memory_col,attack_col,row_id_col


def normalize_dataset(dataset):
    """Read every available split and normalize its memory/attack columns."""
    if isinstance(dataset,Mapping):
        split_items=list(dataset.items())
    else:
        split_items=[('default',dataset)]
    normalized=[]
    for split_name,table in split_items:
        rows=list(table)
        if not rows: continue
        mem_col,attack_col,id_col=_find_columns(table,rows)
        for i,row in enumerate(rows):
            source_id=row.get(id_col) if id_col else None
            normalized.append({'row_id':str(source_id if source_id is not None else f'{split_name}-{i}'),
               'source_id':str(source_id if source_id is not None else f'{split_name}-{i}'),
               'attack':row.get(attack_col),'memory':str(row.get(mem_col) or ''),
               'source_split':str(split_name),'source_row':row})
    if not normalized:
        raise ValueError('CrAI dataset loaded but contained zero rows across all splits')
    matched=sum(is_memory_injection(row['attack']) for row in normalized)
    if matched==0:
        values=sorted({str(row['attack']) for row in normalized})
        raise ValueError(f'CrAI dataset has zero memory-injection rows; observed attack values: {values!r}')
    return normalized


def load_crai(skip=False, dataset_loader=None):
    """Load and normalize CrAI; raise a diagnostic unless explicitly skipped."""
    if skip: return []
    try:
        if dataset_loader is None:
            from datasets import load_dataset
            dataset_loader=load_dataset
        dataset=dataset_loader('SentientAGI/crypto-agent-safe-function-calling')
        return normalize_dataset(dataset)
    except Exception as exc:
        raise RuntimeError(f'Could not load usable CrAI-SafeFuncCall data: {exc}. Pass --skip-crai to omit this source.') from exc


def build_crai_split(rows):
    """Create OOD segment rows, docs, and per-document manual-review records."""
    from .assemble import contexts
    output=[]; documents=[]; audit=[]
    for row in rows:
        original=str(row.get('memory') or '')
        rewritten=sanitize(original)
        attack=row.get('attack')
        is_attack=is_memory_injection(attack)
        if is_attack:
            pairs,first,rule=label_memory_with_audit(rewritten)
        else:
            pairs=[(seg.text,0) for seg in split_segments(rewritten)]
            first=None; rule='benign_attack_value'
        segs=split_segments(rewritten); ctx=contexts(segs)
        seg_by_index=[]; payload=[]; payload_indices=[]; spans=[]
        offset=0
        for i,(text,label) in enumerate(pairs):
            # Splitter segments correspond one-to-one with the heuristic sentence list.
            seg=segs[i] if i<len(segs) else None
            if label:
                payload.append(text); payload_indices.append(i)
                if seg: spans.append([seg.start,seg.end])
            seg_by_index.append(f'{i}: {"injected" if label else "clean"} | {text}')
            source_id=str(row.get('source_id') or row['row_id'])
            split='dev_ood_crai' if int.from_bytes(hashlib.sha256(source_id.encode()).digest()[:4],'big')%5==0 else 'test_ood_crai'
            tag='crai_relevant' if is_attack else 'crai_other'
            output.append({'id':f"crai-{row['row_id']}-{i}",'doc_id':f"crai-{row['row_id']}",'split':split,
              'text':text,'context':ctx[i] if i<len(ctx) else text,'label':int(label),'source':'crai',
              'source_id':source_id,'crai_tag':tag,
              'template_id':f"crai-{row['row_id']}",'seed_id':None,'goal':None,'style':None,'carrier':None,'position':None,
              'hard_case':None,'paraphrased':False,'seg_index':i,'n_segments':len(pairs)})
        doc_id=f"crai-{row['row_id']}"
        source_id=str(row.get('source_id') or row['row_id'])
        split='dev_ood_crai' if int.from_bytes(hashlib.sha256(source_id.encode()).digest()[:4],'big')%5==0 else 'test_ood_crai'
        documents.append({'doc_id':doc_id,'split':split,'text':rewritten,'injection_spans':spans,
          'original_text':original,'template_id':f"crai-{row['row_id']}",'source_split':row.get('source_split'),'source_id':source_id,
          'crai_tag':'crai_relevant' if is_attack else 'crai_other'})
        audit.append({'row_id':row['row_id'],'attack':attack,'memory':original,
          'segments (numbered)':'\n'.join(seg_by_index),'predicted_injected_idx':payload_indices,
          'predicted_payload_text':' '.join(payload),'rewritten_payload_text':' '.join(payload),
          'heuristic_rule_fired':(f'{rule}@segment_{first}' if first is not None else rule)})
    return output,documents,audit
