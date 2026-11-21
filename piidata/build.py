"""Build deterministic segment datasets: python -m piidata.build --config configs/default.yaml."""
import argparse, json, random, re, sys
from pathlib import Path

from .assemble import assemble, assemble_pair, contexts, format_clean_document
from .clean_general import load_general
from .clean_crypto import generate as crypto_generate, TEMPLATES as CRYPTO_TEMPLATES
from .hard_negatives import generate as hard_generate, TEMPLATES as HARD_TEMPLATES
from .injections.generate import read_json_yaml, render_seed
from .slots import fill_slots, make_slots
from .segmenter import split_segments
from .contacts import make_contact_line
from .splits import assign_group, assert_no_leakage, unit_float,assign_stratified_seed_groups
from .qc import (check_giveaways,check_addresses,write_stats,deduplicate_rows,
                 check_hard_negative_docs,assert_crai_nonempty,check_length_balance,
                 tfidf_probe,write_probe_report,check_format_parity,check_injected_ngram_frequency,
                 length_report_by_source,word_length_metrics,match_word_length_strata)
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

def _clean_row(text,split,source,template_id,doc_id,idx,n,ctx,hard_case=None,base_doc_id=None):
    return dict(id=f'{split}-{doc_id}-{idx}',doc_id=doc_id,split=split,text=text,context=ctx,label=0,source=source,
      base_doc_id=base_doc_id or doc_id,
      template_id=template_id,seed_id=None,goal=None,style=None,carrier=None,position=None,hard_case=hard_case,
      paraphrased=False,seg_index=idx,n_segments=n)

def _inj_row(text,split,doc_id,idx,n,ctx,seed,position,paraphrased=False,base_doc_id=None):
    return dict(id=f'{split}-{doc_id}-{idx}',doc_id=doc_id,split=split,text=text,context=ctx,label=1,source='synthetic_injection',
      base_doc_id=base_doc_id or doc_id,
      template_id=seed['id'],seed_id=seed['id'],goal=seed['goal'],style=seed['style'],carrier=seed['_carrier'],position=position,
      hard_case=None,paraphrased=paraphrased,seg_index=idx,n_segments=n)

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
    import time
    stage_started=time.perf_counter()
    rng=random.Random(config.get('seed',1729)); seeds=read_json_yaml(ROOT/'injections'/'seeds.yaml')
    boundaries=read_json_yaml(ROOT/'injections'/'boundary_pairs.yaml'); hard_cases=read_json_yaml(ROOT/'injections'/'hard_case_examples.yaml')
    goal_style=set(config.get('heldout_styles',['obfuscated','role_play']))
    held_carriers=set(config.get('heldout_carriers',['json_tool_response','email_quote']))
    held_goals=set(config.get('heldout_goals',['escalate_permission']))
    groups=assign_stratified_seed_groups(seeds,config.get('seed',1729),goal_style,held_goals,held_carriers)
    carriers=list(config.get('carriers',['visible_body','html_hidden','html_comment','img_alt','pdf_footer_header','markdown_table_cell','json_tool_response','email_quote']))
    eligible={sp:[s for s in seeds if groups[s['id']]==sp and set(s['carriers'])&set(carriers)] for sp in (*SPLITS,'test_heldout')}
    gen=load_general(config.get('general_paragraph_limit',4000))
    if not gen: print('Optional SQuAD/TriviaQA data unavailable; using synthetic prose pools.',file=sys.stderr)
    targets=config.get('targets',{'train':15000,'val':1500,'test_id':1500,'test_heldout':1000})
    pool_weights=config.get('clean_pool_weights',{'general':0.31,'crypto':0.23,'hard_negative':0.46})
    outputs={}; docs={}; all_rows=[]; paraphrase_cache={}; used_attacker_addresses=set()
    for split in (*SPLITS,'test_heldout'):
        total=int(targets.get(split,0)); n_inj=int(total*config.get('injected_fraction',.35)); n_clean=total-n_inj
        n_inj=int(n_inj*config.get('oversample_injected',1.45)*6)
        n_clean=int(n_clean*config.get('oversample_clean',2.2))
        # Production uses the same paired construction as the sample: each
        # injected document has a clean mate. Avoid a much larger unpaired
        # clean quota, which was the source of the production length skew.
        n_clean=n_inj
        rows=[]; documents=[]; inj_count=clean_count=docno=0
        hard_fraction=0.0
        hard_quota=int(n_clean*hard_fraction)
        nonhard_target=n_clean-hard_quota
        seq=eligible.get(split,[])
        general_items=[(i,item) for i,item in enumerate(gen) if clean_group_split(f'general-{i:05d}',config.get('seed',1729))==split]
        crypto_items=[i for i in range(len(CRYPTO_TEMPLATES)) if clean_group_split(f'crypto-{i:03d}',config.get('seed',1729))==split]
        def nonhard_document(seed_number,slots=None,context=None,include_url=None,url_words=None):
            if include_url is None: include_url=rng.random()<.16
            if context:
                key=context.lower().replace('_',' ')
                terms={'payroll':('payroll','salary'),'refund':('refund','return'),'invoice':('invoice','bill'),
                  'checkout':('checkout','order','permit'),'rent split':('rent','household'),
                  'api response':('transaction','history','explorer','response'),'webpage':('page','site','campaign'),
                  'email':('email','sign-in','message'),'donation':('donation','gift','campaign')}.get(key,())
                contextual=[]
                for ix,template in enumerate(HARD_TEMPLATES):
                    title,body=template.split(': ',1)
                    if terms and any(term in (title+' '+body).lower() for term in terms):
                        contextual.append(('hard_negative',title,fill_slots(body,slots or make_slots(rng))))
                for ix,(title,body) in enumerate(CRYPTO_TEMPLATES):
                    if terms and any(term in (title+' '+body).lower() for term in terms):
                        tid,text=crypto_generate(rng,ix,slots); contextual.append(('crypto_prose',tid,text))
                if contextual:
                    source,tid,body=rng.choice(contextual)
                    values=slots or make_slots(rng)
                    body += ' '+make_contact_line(values,rng,include_url,url_words)
                    return source,tid,body
            has_general=bool(general_items); has_crypto=bool(crypto_items)
            wg=float(pool_weights.get('general',.31)) if has_general else 0.0
            wc=float(pool_weights.get('crypto',.23)) if has_crypto else 0.0
            if has_general and (not has_crypto or rng.random()<wg/max(1e-9,wg+wc)):
                gi,(raw_source,raw_text)=general_items[seed_number%len(general_items)]
                source='squad' if raw_source=='squad' else 'triviaqa'; tid=f'general-{gi:05d}'
                pieces=split_segments(raw_text)[:2]
                body=' '.join(x.text for x in pieces)
                values=slots or make_slots(rng)
                body += ' '+fill_slots('The due date is {date}; total {amount} {token}.',values)
                return source,tid,body+' '+make_contact_line(values,rng,include_url,url_words)
            if crypto_items:
                ix=crypto_items[seed_number%len(crypto_items)]
                tid,body=crypto_generate(rng,ix,slots); values=slots or make_slots(rng)
                return 'crypto_prose',tid,body+' '+make_contact_line(values,rng,include_url,url_words)
            body=crypto_generate(rng,seed_number,slots)[1]; values=slots or make_slots(rng)
            return 'crypto_prose','crypto-fallback',body+' '+make_contact_line(values,rng,include_url,url_words)
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
            slot_values=make_slots(rng)
            if paraphrase and seed['style']!='multi_sentence_split':
                if seed['id'] not in paraphrase_cache:
                    cached_original,cached_indices=render_seed(seed,rng,slot_values)
                    from .paraphrase_ollama import paraphrase as ollama_paraphrase
                    paraphrase_cache[seed['id']]=(cached_original,cached_indices,_validated_paraphrases(cached_original,ollama_paraphrase(cached_original),seed),dict(slot_values))
                cached_original,orig_indices,variants,cached_slots=paraphrase_cache[seed['id']]
                original,_=render_seed(seed,rng,slot_values)
                inj=variants[docno%len(variants)] if variants else original
                if variants:
                    for key,old_value in sorted(cached_slots.items(),key=lambda item:-len(item[1])):
                        new_value=slot_values.get(key)
                        if old_value and new_value and old_value!=new_value: inj=inj.replace(old_value,new_value)
                    old_payload=re.search(r'(?<![A-Za-z0-9+/])[A-Za-z0-9+/]{20,}={0,2}(?![A-Za-z0-9+/])',cached_original)
                    new_payload=re.search(r'(?<![A-Za-z0-9+/])[A-Za-z0-9+/]{20,}={0,2}(?![A-Za-z0-9+/])',original)
                    if old_payload and new_payload: inj=inj.replace(old_payload.group(0),new_payload.group(0))
                indices=orig_indices; paraphrased=bool(variants)
            else:
                inj,indices=render_seed(seed,rng,slot_values)
            attacker=slot_values['attacker_addr']
            if attacker in used_attacker_addresses:
                raise AssertionError(f'attacker address was reused: {attacker}')
            used_attacker_addresses.add(attacker)
            base_slots=dict(slot_values)
            if seed['goal']=='change_amount':
                options=[v for v in ('0.03','0.075','0.125','1.25','18.40','42.75','120.00','250.50') if v!=slot_values['amount']]
                base_slots['amount']=rng.choice(options)
            url_segment=next((part.text for part in split_segments(inj) if 'https://' in part.text or 'http://' in part.text),None)
            # Mirror the sample's natural-sentence matching: keep clean
            # sentences intact and choose from contextual prose with the
            # closest word count for every inserted sentence.
            from .probe import matched_base_goal,SHORT_CLEAN
            base_source,base_template,base_anchor=matched_base_goal(seed,base_slots,rng,docno)
            candidates=[part.text for part in split_segments(base_anchor)]
            candidates.extend(fill_slots(text,base_slots) for text in SHORT_CLEAN)
            inj_parts=split_segments(inj); chosen=[]
            contact=make_contact_line(base_slots,rng,include_url=bool(url_segment),target_words=len(url_segment.split()) if url_segment else None)
            contact_parts=[part.text for part in split_segments(contact)]
            candidates.extend(contact_parts)
            for part in inj_parts:
                exact=[candidate for candidate in candidates if len(candidate.split())==len(part.text.split())]
                chosen.append(rng.choice(exact) if exact else min(candidates,key=lambda candidate:abs(len(candidate.split())-len(part.text.split()))))
            base_parts=[part.text for part in split_segments(base_anchor)[:1]]+chosen
            # Keep shared ENS and support URL metadata, when present, in their
            # own natural contact sentences and let per-split sampling downweight
            # any unmatched clean length buckets.
            base_parts.extend(part for part in contact_parts if part not in base_parts)
            base='\n'.join(dict.fromkeys(base_parts))
            if seed['goal']=='change_amount':
                base += ' '+fill_slots('The invoice total is {amount} {token}.',base_slots)
                if slot_values['amount']==base_slots['amount'] or slot_values['amount'] not in inj or base_slots['amount'] not in base:
                    raise AssertionError('change_amount must differ from and match the base invoice total')
            if attacker.lower() in base.lower(): raise AssertionError('attacker address leaked into the paired base document')
            if slot_values['ens_name'] not in base or (url_segment and slot_values['url'] not in base):
                raise AssertionError('paired clean and injected documents must share their ENS/URL contact metadata')
            clean_pair,attack_pair=assemble_pair(base,inj,None,seed['_carrier'],rng,indices if seed['style']=='multi_sentence_split' else None)
            _,_,_,pos,span=attack_pair
            document,segs,labels,_,_=attack_pair
            docid=f'{split}-doc-{docno:07d}'; contexts_for=contexts(segs)
            base_id=f'{split}-base-{docno:07d}'
            injection_locs=[]
            for i,(seg,label) in enumerate(zip(segs,labels)):
                if label and inj_count<n_inj:
                    rows.append(_inj_row(seg.text,split,docid,i,len(segs),contexts_for[i],seed,pos,paraphrased,base_id)); inj_count+=1; injection_locs.append([seg.start,seg.end])
                elif not label:
                    # Keep the paired base context available for exact
                    # length-stratum sampling after deduplication.
                    rows.append(_clean_row(seg.text,split,base_source,base_template,docid,i,len(segs),contexts_for[i],base_doc_id=base_id)); clean_count+=1
            labeled_spans=[[seg.start,seg.end] for seg,label in zip(segs,labels) if label]
            documents.append({'doc_id':docid,'base_doc_id':base_id,'split':split,'text':document,'injection_spans':labeled_spans,'labels':labels,'template_id':seed['id'],'seed_id':seed['id'],'goal':seed['goal'],'style':seed['style'],'carrier':seed['_carrier'],'position':pos})
            clean_doc,clean_segs,clean_labels,_,clean_span=clean_pair
            clean_docid=f'{split}-paired-clean-{docno:07d}'
            clean_contexts=contexts(clean_segs)
            for i,seg in enumerate(clean_segs):
                rows.append(_clean_row(seg.text,split,base_source,base_template,clean_docid,i,len(clean_segs),clean_contexts[i],base_doc_id=base_id)); clean_count+=1
            documents.append({'doc_id':clean_docid,'base_doc_id':base_id,'split':split,'text':clean_doc,'injection_spans':[],'template_id':seed['id'],'seed_id':None,'paired_doc_id':docid})
            docno+=1
        while clean_count<n_clean:
            # Reserve a fixed share of clean rows for explicit hard-negative documents.
            if clean_count>=nonhard_target:
                choices=[i for i in range(len(HARD_TEMPLATES)) if clean_group_split(f'hardneg-{i:03d}',config.get('seed',1729))==split]
                ix=choices[clean_count%len(choices)]; clean_slots=make_slots(rng); tid,text=hard_generate(rng,ix,clean_slots)
                text += ' '+make_contact_line(clean_slots,rng,rng.random()<.16)
                source='hard_negative'; hard_case=None
            else:
                source,tid,text=nonhard_document(clean_count); hard_case=None
            text=format_clean_document(text,rng); segs=split_segments(text); docid=f'{split}-doc-{docno:07d}'; docno+=1; ctxs=contexts(segs)
            for i,s in enumerate(segs):
                if clean_count>=n_clean: break
                rows.append(_clean_row(s.text,split,source,tid,docid,i,len(segs),ctxs[i],hard_case)); clean_count+=1
            documents.append({'doc_id':docid,'split':split,'text':text,'injection_spans':[],'template_id':tid,'seed_id':None})
        # Add individual clean prose sentences at the requested clean share;
        # length-stratum sampling later retains only lengths represented by
        # the injection distribution.
        prose_target=int(n_inj*.18); prose=[]
        for gi,(raw_source,raw_text) in general_items:
            prose.extend(('general_prose',f'general-{gi:05d}',s.text) for s in split_segments(raw_text))
        for ix in crypto_items:
            tid,body=crypto_generate(rng,ix,make_slots(rng))
            prose.extend(('crypto_prose',tid,s.text) for s in split_segments(body))
        rng.shuffle(prose)
        for source,tid,text in prose[:prose_target]:
            docid=f'{split}-prose-{docno:07d}'; docno+=1
            rows.append(_clean_row(text,split,source,tid,docid,0,1,f' [SEG] {text} [SEG] '))
        # Include the supplied boundary pairs in their fixed group split.
        for pair in boundaries:
            dest=assign_group(pair['id'],config.get('seed',1729))
            if dest!=split: continue
            pair_slots=make_slots(rng)
            pair_inj=fill_slots(pair['injected'],pair_slots)
            contact=' '+make_contact_line(pair_slots,rng,'https://' in pair_inj or 'http://' in pair_inj)
            for label,key in ((0,'clean'),(1,'injected')):
                txt=format_clean_document(fill_slots(pair[key],pair_slots)+contact,rng); docid=f'{split}-{pair["id"]}-{label}'
                rows.append(dict(id=f'{docid}-0',doc_id=docid,split=split,text=txt,context=f' [SEG] {txt} [SEG] ',label=label,source='hard_negative' if label==0 else 'synthetic_injection',template_id=pair['id'],seed_id=pair['id'] if label else None,goal=pair['goal'],style=None,carrier=None,position=None,hard_case=None,paraphrased=False,seg_index=0,n_segments=1))
                documents.append({'doc_id':docid,'split':split,'text':txt,'injection_spans':[] if not label else [[0,len(txt)]],'template_id':pair['id'],'seed_id':pair['id'] if label else None})
        # Supplied clean hard-case examples remain clean and are explicitly tagged.
        for item in hard_cases:
            dest=assign_group(item['id'],config.get('seed',1729))
            if dest!=split: continue
            clean_slots=make_slots(rng)
            txt=format_clean_document(fill_slots(item['text'],clean_slots)+' '+make_contact_line(clean_slots,rng,rng.random()<.16),rng); docid=f'{split}-{item["id"]}'
            rows.append(dict(id=docid+'-0',doc_id=docid,split=split,text=txt,context=f' [SEG] {txt} [SEG] ',label=0,source='hard_negative',template_id=item['id'],seed_id=None,goal=None,style=None,carrier=None,position=None,hard_case=item['hard_case'],paraphrased=False,seg_index=0,n_segments=1))
            documents.append({'doc_id':docid,'split':split,'text':txt,'injection_spans':[],'template_id':item['id'],'seed_id':None})
        outputs[split]=rows; docs[split]=documents; all_rows.extend(rows)

    # CrAI is mandatory unless the caller explicitly chooses --skip-crai.
    crai_source=load_crai(skip=skip_crai)
    crai_rows,crai_docs,audit=build_crai_split(crai_source)
    outputs['dev_ood_crai']=[r for r in crai_rows if r['split']=='dev_ood_crai']
    outputs['test_ood_crai']=[r for r in crai_rows if r['split']=='test_ood_crai']
    docs['dev_ood_crai']=[d for d in crai_docs if d['split']=='dev_ood_crai']
    docs['test_ood_crai']=[d for d in crai_docs if d['split']=='test_ood_crai']
    assert_crai_nonempty(outputs['test_ood_crai'],enabled=not skip_crai)
    outputs['redteam_manual']=[]; docs['redteam_manual']=[]

    print(f"generation: {sum(map(len,outputs.values()))} rows ({time.perf_counter()-stage_started:.1f}s)",flush=True)
    # Remove exact and near duplicates; CrAI is carried through untouched.
    crai_all=outputs['dev_ood_crai']+outputs['test_ood_crai']
    flat=[r for sp in (*SPLITS,'test_heldout') for r in outputs[sp]]
    # Balance the oversampled candidates before the quadratic near-duplicate
    # pass, keeping that pass bounded to the rows that can enter the corpus.
    print(f"split: {len(flat)} in-distribution rows; CrAI {len(crai_all)} rows",flush=True)
    flat=match_word_length_strata(flat,config.get('seed',1729))
    print(f"length matching candidates: {len(flat)} rows",flush=True)
    deduped=deduplicate_rows(flat)
    print(f"dedup: {len(deduped)} rows ({time.perf_counter()-stage_started:.1f}s elapsed)",flush=True)
    # Add individual prose sentences after dedup so they remain available as
    # a separate 18% clean pool.
    for sp in (*SPLITS,'test_heldout'):
        target=int(int(targets.get(sp,0))*.65*.18); prose=[]
        for ix,(title,body) in enumerate(CRYPTO_TEMPLATES):
            prose.extend(('crypto_prose',f'crypto-{ix:03d}',part.text) for part in split_segments(body))
        for gi,(source,text) in enumerate(gen):
            if clean_group_split(f'general-{gi:05d}',config.get('seed',1729))==sp:
                prose.extend(('general_prose',f'general-{gi:05d}',part.text) for part in split_segments(text))
        for i,(source,tid,text) in enumerate(prose[:target]):
            docid=f'{sp}-prose-pool-{i}'; deduped.append(_clean_row(text,sp,source,tid,docid,0,1,f' [SEG] {text} [SEG] '))
    raw_train_source_stats=length_report_by_source([r for r in deduped if r.get('split')=='train'])
    deduped=match_word_length_strata([r for r in deduped if not r.get('split','').endswith('_crai')],config.get('seed',1729))+crai_all
    print(f"length matching final: {len(deduped)} rows; CrAI unchanged {len(crai_all)}",flush=True)
    keep_ids={r['id'] for r in deduped}
    for sp in outputs: outputs[sp]=[r for r in outputs[sp] if r['id'] in keep_ids]
    for sp in docs:
        live={r['doc_id'] for r in outputs.get(sp,[])}
        # Row dedup can discard a clean mate's duplicate segment rows while
        # leaving the attacked doc. Retain that base mate for paired document
        # parity and audit reporting.
        paired_clean_ids={d['doc_id'] for d in docs[sp] if d.get('paired_doc_id') in live}
        docs[sp]=[d for d in docs[sp] if d['doc_id'] in live or d['doc_id'] in paired_clean_ids]
    # Reapply the same exact-word-count matcher to each assigned in-distribution
    # split after dedup; the two CrAI splits pass through verbatim.
    indist=[r for sp in (*SPLITS,'test_heldout') for r in outputs[sp]]
    matched_ids={r['id'] for r in match_word_length_strata(indist,config.get('seed',1729))}
    for sp in (*SPLITS,'test_heldout'):
        outputs[sp]=[r for r in outputs[sp] if r['id'] in matched_ids]
    all_rows=[r for sp in outputs for r in outputs[sp]]
    print(f"length matching: {len(all_rows)} in-distribution rows; CrAI {len(crai_all)} unchanged ({time.perf_counter()-stage_started:.1f}s)",flush=True)
    # Group safety assertion excludes boundary pair members, which intentionally
    # share one pair id and therefore remain together within their assigned split.
    assert_no_leakage(all_rows)
    tokens=[x.strip() for x in (ROOT/'injections'/'giveaway_tokens.txt').read_text(encoding='utf-8').splitlines() if x.strip()]
    # Validate the actual JSONL-export schema (free-form source metadata is included).
    check_giveaways(all_rows,tokens); check_addresses(all_rows)
    for sp in outputs: check_hard_negative_docs(outputs[sp],docs[sp])
    assert_crai_nonempty(outputs['test_ood_crai'],enabled=not skip_crai)
    length_stats={sp:word_length_metrics(rows) for sp,rows in outputs.items() if rows and not sp.endswith('_crai')}
    source_stats=length_report_by_source(outputs['train'])
    length_lines=['# Word-length diagnostics','', 'Word counts are whitespace token counts. Length-only accuracy is measured with stratified 75/25 holdout within each group.','', '- Deduplication: normalized exact-hash only (datasketch MinHash LSH is unavailable; exact fallback used).','', '## Full train before length matching: source diagnosis','', '| Source | Rows | Clean mean | Clean median | Injected mean | Injected median | KS D | KS p | Length-only accuracy |','|---|---:|---:|---:|---:|---:|---:|---:|---:|']
    for source,entry in raw_train_source_stats.items():
        m=entry['metrics']; length_lines.append(f"| {source} | {entry['rows']} | {m['clean_mean']:.2f} | {m['clean_median']:.1f} | {m['injected_mean']:.2f} | {m['injected_median']:.1f} | {m['ks_d']:.4f} | {m['ks_p']:.6g} | {m['length_accuracy']:.4f} |")
    length_lines += ['', '## Final full train by source','', '| Source | Rows | Clean mean | Clean median | Injected mean | Injected median | KS D | KS p | Length-only accuracy |','|---|---:|---:|---:|---:|---:|---:|---:|---:|']
    for source,entry in source_stats.items():
        m=entry['metrics']; length_lines.append(f"| {source} | {entry['rows']} | {m['clean_mean']:.2f} | {m['clean_median']:.1f} | {m['injected_mean']:.2f} | {m['injected_median']:.1f} | {m['ks_d']:.4f} | {m['ks_p']:.6g} | {m['length_accuracy']:.4f} |")
    length_lines += ['', '## Effect-size gates by split','', '| Split | Rows | KS D | KS p (informational) | Length-only accuracy |','|---|---:|---:|---:|---:|']
    for sp,rows in outputs.items():
        if not rows or sp.endswith('_crai'): continue
        m=length_stats[sp]; length_lines.append(f"| {sp} | {len(rows)} | {m['ks_d']:.4f} | {m['ks_p']:.6g} | {m['length_accuracy']:.4f} |")
    (ROOT/'reports').mkdir(exist_ok=True)
    (ROOT/'reports'/'length_source_report.md').write_text('\n'.join(length_lines)+'\n',encoding='utf-8')
    for sp,rows in outputs.items():
        if rows and not sp.endswith('_crai'): check_length_balance(rows)
    print('QC: passed',flush=True)
    ks_p=length_stats['train']['ks_p']
    probe=tfidf_probe(outputs['train'],outputs['test_id'],enforce_length=False)
    write_probe_report(ROOT/'reports'/'probe_report.md',probe,ks_p)
    clean_docs=[d for d in docs['train'] if not d.get('injection_spans')]
    injected_docs=[d for d in docs['train'] if d.get('injection_spans')]
    check_format_parity(clean_docs,injected_docs)
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
