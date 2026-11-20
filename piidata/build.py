"""Build deterministic segment datasets: python -m piidata.build --config configs/default.yaml."""
import argparse, json, random, re, sys
from pathlib import Path

from .assemble import assemble, contexts
from .clean_general import load_general
from .clean_crypto import generate as crypto_generate, TEMPLATES as CRYPTO_TEMPLATES
from .hard_negatives import generate as hard_generate, TEMPLATES as HARD_TEMPLATES
from .injections.generate import read_json_yaml, render_seed
from .slots import fill_slots, make_slots
from .segmenter import split_segments
from .splits import assign_group, assert_no_leakage, unit_float
from .qc import check_giveaways, check_addresses, write_stats, deduplicate_rows, check_hard_negative_docs, assert_crai_nonempty
from .crai import load_crai, build_crai_split

ROOT=Path(__file__).resolve().parents[1]
SPLITS=('train','val','test_id','test_heldout')
SCHEMA=('id doc_id split text context label source template_id seed_id goal style carrier position hard_case paraphrased seg_index n_segments').split()

def clean_group_split(group, seed):
    x=unit_float(seed,'clean:'+group)
    if x<.10: return 'test_heldout'
    y=(x-.10)/.90
    return 'train' if y<.8 else ('val' if y<.9 else 'test_id')

def read_config(path):
    raw=Path(path).read_text(encoding='utf-8-sig')
    try: return json.loads(raw)
    except json.JSONDecodeError:
        try:
            import yaml
            return yaml.safe_load(raw)
        except ImportError as exc: raise RuntimeError('Config must be JSON-compatible YAML unless pyyaml is installed') from exc

def write_jsonl(path,rows):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('w',encoding='utf-8',newline='\n') as f:
        for row in rows: f.write(json.dumps(row,ensure_ascii=False,separators=(',',':'))+'\n')

def _clean_row(text,split,source,template_id,doc_id,idx,n,ctx,hard_case=None):
    return dict(id=f'{split}-{doc_id}-{idx}',doc_id=doc_id,split=split,text=text,context=ctx,label=0,source=source,
      template_id=template_id,seed_id=None,goal=None,style=None,carrier=None,position=None,hard_case=hard_case,
      paraphrased=False,seg_index=idx,n_segments=n)

def _inj_row(text,split,doc_id,idx,n,ctx,seed,position,paraphrased=False):
    return dict(id=f'{split}-{doc_id}-{idx}',doc_id=doc_id,split=split,text=text,context=ctx,label=1,source='synthetic_injection',
      template_id=seed['id'],seed_id=seed['id'],goal=seed['goal'],style=seed['style'],carrier=seed['_carrier'],position=position,
      hard_case=None,paraphrased=paraphrased,seg_index=idx,n_segments=n)

def _vary_carrier_context(text, indices, slots, rng):
    """Add varied harmless document metadata to embedded attack sentences."""
    segments=split_segments(text); chosen=set(indices) if indices else set(range(len(segments)))
    pieces=[]; cursor=0
    for i,seg in enumerate(segments):
        pieces.append(text[cursor:seg.start])
        body=seg.text
        if i in chosen:
            punctuation=body[-1] if body and body[-1] in '.!?' else ''
            core=body[:-1] if punctuation else body
            extra=(f"; receipt {slots['invoice_id']} issued by {slots['merchant']}, batch {rng.randrange(100000,999999)}, "
              f"reference {slots['reference']}, dated {slots['date']}, stated amount {slots['amount']} {slots['token']}, "
              f"account label {slots['name']}, destination record {slots['recipient']}, ledger entry {rng.randrange(100000,999999)}")
            body=core+extra+punctuation
        pieces.append(body); cursor=seg.end
    pieces.append(text[cursor:])
    return ''.join(pieces)

def _validated_paraphrases(text, variants, seed):
    goals={
      'redirect_recipient':('address','recipient','transfer','pay'), 'change_amount':('amount','transfer','send','payment'),
      'extra_transfer':('transfer','payment','send','additional','second'), 'drain_balance':('balance','remaining','sweep','every'),
      'unauthorized_typed_data_sign':('sign','permit','typed'), 'exfiltrate_secret':('recovery','private key','secret','words'),
      'exfiltrate_private_data':('history','balance','address book','wallet'), 'suppress_confirmation':('confirmation','approval','without','silently'),
      'fake_user_approval':('approved','approval','consent'), 'escalate_permission':('limit','permission','spender','allowance'),
      'out_of_scope_action':('bridge','swap','stake','deploy','agent'), 'goal_hijack_generic':('ignore','instruction','link','output')}
    protected=re.findall(r'0x[0-9a-fA-F]{40}|[0-9]+\.[0-9]+|[\w.-]+\.eth\b',text)
    keys=goals.get(seed['goal'],())
    out=[]
    for value in variants:
        if not isinstance(value,str) or len(value.split())>=60: continue
        lower=value.lower()
        if any(x.lower() not in lower for x in protected): continue
        if keys and not any(k in lower for k in keys): continue
        out.append(value)
    return out[:4]

def build(config,paraphrase=False,skip_crai=False):
    rng=random.Random(config.get('seed',1729)); seeds=read_json_yaml(ROOT/'injections'/'seeds.yaml')
    boundaries=read_json_yaml(ROOT/'injections'/'boundary_pairs.yaml'); hard_cases=read_json_yaml(ROOT/'injections'/'hard_case_examples.yaml')
    goal_style=set(config.get('heldout_styles',['obfuscated','role_play']))
    held_carriers=set(config.get('heldout_carriers',['json_tool_response','email_quote']))
    held_goals=set(config.get('heldout_goals',['escalate_permission']))
    groups={s['id']:assign_group(s['id'],config.get('seed',1729), s['style'] in goal_style or s['goal'] in held_goals or bool(set(s['carriers'])&held_carriers)) for s in seeds}
    carriers=list(config.get('carriers',['visible_body','html_hidden','html_comment','img_alt','pdf_footer_header','markdown_table_cell','json_tool_response','email_quote']))
    eligible={sp:[s for s in seeds if groups[s['id']]==sp and set(s['carriers'])&set(carriers)] for sp in (*SPLITS,'test_heldout')}
    gen=load_general(config.get('general_paragraph_limit',4000))
    if not gen: print('Optional SQuAD/TriviaQA data unavailable; using synthetic prose pools.',file=sys.stderr)
    targets=config.get('targets',{'train':15000,'val':1500,'test_id':1500,'test_heldout':1000})
    pool_weights=config.get('clean_pool_weights',{'general':0.31,'crypto':0.23,'hard_negative':0.46})
    outputs={}; docs={}; all_rows=[]; paraphrase_cache={}
    for split in (*SPLITS,'test_heldout'):
        total=int(targets.get(split,0)); n_inj=int(total*config.get('injected_fraction',.35)); n_clean=total-n_inj
        n_inj=int(n_inj*config.get('oversample_injected',1.45))
        n_clean=int(n_clean*config.get('oversample_clean',2.2))
        rows=[]; documents=[]; inj_count=clean_count=docno=0
        hard_fraction=float(config.get('hard_negative_clean_fraction',pool_weights.get('hard_negative',.40)))
        hard_quota=int(n_clean*hard_fraction)
        nonhard_target=n_clean-hard_quota
        seq=eligible.get(split,[])
        general_items=[(i,item) for i,item in enumerate(gen) if clean_group_split(f'general-{i:05d}',config.get('seed',1729))==split]
        crypto_items=[i for i in range(len(CRYPTO_TEMPLATES)) if clean_group_split(f'crypto-{i:03d}',config.get('seed',1729))==split]
        def nonhard_document(seed_number):
            has_general=bool(general_items); has_crypto=bool(crypto_items)
            wg=float(pool_weights.get('general',.31)) if has_general else 0.0
            wc=float(pool_weights.get('crypto',.23)) if has_crypto else 0.0
            if has_general and (not has_crypto or rng.random()<wg/max(1e-9,wg+wc)):
                gi,(raw_source,raw_text)=general_items[seed_number%len(general_items)]
                source='squad' if raw_source=='squad' else 'triviaqa'; tid=f'general-{gi:05d}'
                pieces=split_segments(raw_text)[:2]
                body=' '.join(x.text for x in pieces)
                slots=make_slots(rng)
                return source,tid,body+' '+fill_slots('Reference {invoice_id} dated {date}; amount {amount} {token}.',slots)
            if crypto_items:
                ix=crypto_items[seed_number%len(crypto_items)]
                tid,body=crypto_generate(rng,ix); return 'crypto_prose',tid,body
            return 'crypto_prose','crypto-fallback',crypto_generate(rng,seed_number)[1]
        if n_inj and not seq: raise RuntimeError(f'No injection seeds assigned to {split}')
        # Injected documents contribute nearby clean context; remaining clean rows
        # are drawn from the three clean pools, with at least 40% hard negatives.
        while inj_count<n_inj:
            seed=dict(seq[docno%len(seq)])
            carrier_choices=[x for x in seed['carriers'] if x in carriers]
            if split=='test_heldout' and set(carrier_choices)&held_carriers:
                carrier_choices=[x for x in carrier_choices if x in held_carriers]
            seed['_carrier']=rng.choice(carrier_choices)
            paraphrased=False
            if paraphrase and seed['style']!='multi_sentence_split':
                if seed['id'] not in paraphrase_cache:
                    original,orig_indices=render_seed(seed,rng)
                    from .paraphrase_ollama import paraphrase as ollama_paraphrase
                    paraphrase_cache[seed['id']]=(original,orig_indices,_validated_paraphrases(original,ollama_paraphrase(original),seed))
                original,orig_indices,variants=paraphrase_cache[seed['id']]
                inj=variants[docno%len(variants)] if variants else original
                indices=orig_indices; paraphrased=bool(variants)
            else:
                inj,indices=render_seed(seed,rng)
            metadata=make_slots(rng)
            inj=_vary_carrier_context(inj,indices,metadata,rng)
            base_source,base_template,base=nonhard_document(docno)
            document,segs,labels,pos,span=assemble(base,inj,seed['_carrier'],rng,indices if seed['style']=='multi_sentence_split' else None)
            docid=f'{split}-doc-{docno:07d}'; contexts_for=contexts(segs)
            injection_locs=[]
            for i,(seg,label) in enumerate(zip(segs,labels)):
                if label and inj_count<n_inj:
                    rows.append(_inj_row(seg.text,split,docid,i,len(segs),contexts_for[i],seed,pos,paraphrased)); inj_count+=1; injection_locs.append([seg.start,seg.end])
                elif not label and clean_count<nonhard_target:
                    rows.append(_clean_row(seg.text,split,base_source,base_template,docid,i,len(segs),contexts_for[i])); clean_count+=1
            documents.append({'doc_id':docid,'split':split,'text':document,'injection_spans':[list(span)],'labels':labels,'template_id':seed['id'],'seed_id':seed['id'],'goal':seed['goal'],'style':seed['style'],'carrier':seed['_carrier'],'position':pos})
            docno+=1
        while clean_count<n_clean:
            # Reserve a fixed share of clean rows for explicit hard-negative documents.
            if clean_count>=nonhard_target:
                choices=[i for i in range(len(HARD_TEMPLATES)) if clean_group_split(f'hardneg-{i:03d}',config.get('seed',1729))==split]
                ix=choices[clean_count%len(choices)]; tid,text=hard_generate(rng,ix)
                source='hard_negative'; hard_case=None
            else:
                source,tid,text=nonhard_document(clean_count); hard_case=None
            segs=split_segments(text); docid=f'{split}-doc-{docno:07d}'; docno+=1; ctxs=contexts(segs)
            for i,s in enumerate(segs):
                if clean_count>=n_clean: break
                rows.append(_clean_row(s.text,split,source,tid,docid,i,len(segs),ctxs[i],hard_case)); clean_count+=1
            documents.append({'doc_id':docid,'split':split,'text':text,'injection_spans':[],'template_id':tid,'seed_id':None})
        # Include the supplied boundary pairs in their fixed group split.
        for pair in boundaries:
            dest=assign_group(pair['id'],config.get('seed',1729))
            if dest!=split: continue
            for label,key in ((0,'clean'),(1,'injected')):
                txt=fill_slots(pair[key],make_slots(rng)); docid=f'{split}-{pair["id"]}-{label}'
                rows.append(dict(id=f'{docid}-0',doc_id=docid,split=split,text=txt,context=f' [SEG] {txt} [SEG] ',label=label,source='hard_negative' if label==0 else 'synthetic_injection',template_id=pair['id'],seed_id=pair['id'] if label else None,goal=pair['goal'],style=None,carrier=None,position=None,hard_case=None,paraphrased=False,seg_index=0,n_segments=1))
                documents.append({'doc_id':docid,'split':split,'text':txt,'injection_spans':[] if not label else [[0,len(txt)]],'template_id':pair['id'],'seed_id':pair['id'] if label else None})
        # Supplied clean hard-case examples remain clean and are explicitly tagged.
        for item in hard_cases:
            dest=assign_group(item['id'],config.get('seed',1729))
            if dest!=split: continue
            txt=fill_slots(item['text'],make_slots(rng)); docid=f'{split}-{item["id"]}'
            rows.append(dict(id=docid+'-0',doc_id=docid,split=split,text=txt,context=f' [SEG] {txt} [SEG] ',label=0,source='hard_negative',template_id=item['id'],seed_id=None,goal=None,style=None,carrier=None,position=None,hard_case=item['hard_case'],paraphrased=False,seg_index=0,n_segments=1))
            documents.append({'doc_id':docid,'split':split,'text':txt,'injection_spans':[],'template_id':item['id'],'seed_id':None})
        outputs[split]=rows; docs[split]=documents; all_rows.extend(rows)

    # CrAI is mandatory unless the caller explicitly chooses --skip-crai.
    crai_source=load_crai(skip=skip_crai)
    crai_rows,crai_docs,audit=build_crai_split(crai_source)
    assert_crai_nonempty(crai_rows,enabled=not skip_crai)
    outputs['test_ood_crai']=crai_rows; docs['test_ood_crai']=crai_docs
    outputs['redteam_manual']=[]; docs['redteam_manual']=[]

    # Remove exact and 5-gram near duplicates across all in-distribution splits.
    flat=[r for sp in (*SPLITS,'test_heldout','test_ood_crai') for r in outputs[sp]]
    deduped=deduplicate_rows(flat)
    keep_ids={r['id'] for r in deduped}
    for sp in outputs: outputs[sp]=[r for r in outputs[sp] if r['id'] in keep_ids]
    for sp in docs:
        live={r['doc_id'] for r in outputs.get(sp,[])}
        docs[sp]=[d for d in docs[sp] if d['doc_id'] in live]
    all_rows=[r for sp in outputs for r in outputs[sp]]
    # Group safety assertion excludes boundary pair members, which intentionally
    # share one pair id and therefore remain together within their assigned split.
    assert_no_leakage(all_rows)
    tokens=[x.strip() for x in (ROOT/'injections'/'giveaway_tokens.txt').read_text(encoding='utf-8').splitlines() if x.strip()]
    # Validate the actual JSONL-export schema (free-form source metadata is included).
    check_giveaways(all_rows,tokens); check_addresses(all_rows)
    for sp in outputs: check_hard_negative_docs(outputs[sp],docs[sp])
    assert_crai_nonempty(outputs['test_ood_crai'],enabled=not skip_crai)
    out=ROOT/'data'; out.mkdir(exist_ok=True); (ROOT/'reports').mkdir(exist_ok=True)
    for split,rows in outputs.items():
        write_jsonl(out/f'{split}.jsonl',rows); write_jsonl(out/f'docs_{split}.jsonl',docs[split])
    import csv
    audit_sample=rng.sample(audit,min(100,len(audit))) if audit else []
    audit_columns=['row_id','attack','memory','segments (numbered)','predicted_injected_idx','predicted_payload_text','rewritten_payload_text','heuristic_rule_fired']
    with (ROOT/'reports'/'crai_label_audit.csv').open('w',encoding='utf-8',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=audit_columns); writer.writeheader()
        for row in audit_sample:
            row=dict(row); row['predicted_injected_idx']=json.dumps(row['predicted_injected_idx'],ensure_ascii=False)
            writer.writerow(row)
    write_stats(ROOT,outputs)
    samples=['# Review samples','']; sample_rng=random.Random(config.get('seed',1729))
    for goal in sorted({r.get('goal') for r in all_rows if r.get('goal')}):
        pool=[r for r in all_rows if r.get('goal')==goal]
        choices=sample_rng.sample(pool,min(10,len(pool)))
        samples += [f'## {goal}']+[f'- [{r["split"]}] {r["text"]}' for r in choices]+['']
    hard_pool=[r for r in all_rows if r['source']=='hard_negative']
    samples += ['## Hard negatives']+[f'- [{r["split"]}] {r["text"]}' for r in sample_rng.sample(hard_pool,min(20,len(hard_pool)))]
    (ROOT/'reports'/'samples.md').write_text('\n'.join(samples)+'\n',encoding='utf-8')
    write_jsonl(out/'redteam_manual.jsonl',[])
    (out/'redteam_manual_README.md').write_text('# Manual red-team set\n\nThis empty JSONL uses the dataset segment schema. Add approximately 100 hand-written attacks for a separately reviewed challenge set. Keep these examples out of model training until reviewed.\n',encoding='utf-8')
    return outputs

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--config',default='configs/default.yaml'); ap.add_argument('--paraphrase',action='store_true'); ap.add_argument('--skip-crai',action='store_true',help='Explicitly omit the CrAI OOD source')
    args=ap.parse_args(); build(read_config(args.config),args.paraphrase,args.skip_crai)

if __name__=='__main__': main()
