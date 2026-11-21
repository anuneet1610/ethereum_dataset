"""Build a small sample from current construction code and probe it."""
import argparse, base64, json, random, re
from pathlib import Path

from .assemble import assemble_pair
from .clean_crypto import generate as crypto_generate,TEMPLATES as CRYPTO_TEMPLATES
from .hard_negatives import TEMPLATES as HARD_TEMPLATES
from .injections.generate import read_json_yaml,render_seed
from .qc import (tfidf_probe,write_probe_report,ks_word_count_pvalue,
                 check_injected_ngram_frequency)
from .slots import make_slots,fill_slots
from .splits import unit_float
from .build import write_jsonl
from .segmenter import split_segments
from .contacts import make_contact_line

ROOT=Path(__file__).resolve().parents[1]
SAMPLE_CARRIERS=['visible_body','img_alt','markdown_table_cell','html_comment','json_tool_response','email_quote','html_hidden','pdf_footer_header']
SHORT_CLEAN=[
 'Receipt archived.','The receipt is ready.','Payment remains pending.','Invoice received today.','Terms are listed below.',
 'Review the wallet details.','Recipient details appear above.','Transaction status: confirmed.','Network fee appears separately.',
 'The requested amount is due.','Check the token balance.','View recent transaction history.','Use the listed invoice reference.',
 'Payment is due by Friday.','The merchant confirmed receipt.','An order remains open.','Read the service terms carefully.',
 'The monthly rent split is ready.','Settlement is due this month.','Your payment record was updated.',
 'The invoice lists {amount} {token}.','The merchant is {merchant}.','The transfer is pending review.',
 'A receipt is available for {name}.','The payment terms remain in effect.','The network fee is shown separately.',
 'This order closes on {date}.','The token amount appears on the invoice.','The transaction has a confirmed status.',
 'Please keep the receipt with your records.','The posted date is {date}.','The merchant recorded a payment.',
 'The wallet screen displays the transfer details.','The invoice includes ordinary payment terms.',
 'The displayed balance excludes pending transactions.','The transaction history lists completed wallet activity.',
 'Review the network, token, amount, and recipient before confirming.'
]

def matched_base_goal(seed,slots,rng,index):
    base_slots=dict(slots)
    context=seed.get('context','').lower()
    terms={
      'payroll':('payroll','salary'), 'refund':('refund','return'), 'invoice':('invoice','bill'),
      'checkout':('checkout','order','permit'), 'rent_split':('rent','household'),
      'api_response':('transaction','history','explorer','response'), 'webpage':('page','site','campaign'),
      'email':('email','sign-in','message'), 'donation':('donation','gift','campaign'),
    }.get(context,())
    pool=[]
    for ix,title_body in enumerate(CRYPTO_TEMPLATES):
        title,body=title_body
        if terms and not any(term in (title+' '+body).lower() for term in terms): continue
        pool.append(('crypto_prose',title,crypto_generate(rng,ix,base_slots)[1]))
    for ix,template in enumerate(HARD_TEMPLATES):
        title,body=template.split(': ',1)
        if terms and not any(term in (title+' '+body).lower() for term in terms): continue
        pool.append(('hard_negative',title,fill_slots(body,base_slots)))
    if not pool:
        pool=[('crypto_prose',tid,text) for ix in range(len(CRYPTO_TEMPLATES))
              for tid,text in [crypto_generate(rng,ix,base_slots)]]
    source,title,text=rng.choice(pool)
    # Shared benign account metadata gives clean and injected documents the
    # same realistic ENS/URL exposure and keeps the slots drawn from one pool.
    if seed['goal']=='change_amount':
        text += f' The invoiced total is {base_slots["amount"]} {base_slots["token"]}.'
    return source,title,text

def make_sample(count=2000,seed=1729):
    rng=random.Random(seed); seeds=read_json_yaml(ROOT/'injections'/'seeds.yaml')
    seeds=[s for s in seeds if s['style']!='multi_sentence_split']
    rng.shuffle(seeds)
    carriers=set(SAMPLE_CARRIERS); rows=[]; pairs=[]; group=0
    while len(rows)<int(count*4.0):
        item=dict(seeds[group%len(seeds)]); slots=make_slots(rng)
        inj,_=render_seed(item,rng,slots)
        encoded_payload=''
        for candidate in re.findall(r'(?<![A-Za-z0-9+/])[A-Za-z0-9+/]{20,}={0,2}(?![A-Za-z0-9+/])',inj):
            try:
                decoded=base64.b64decode(candidate,validate=True).decode('utf-8')
                if 'Reference this sample as CASE-' in decoded:
                    encoded_payload=candidate; break
            except (ValueError,UnicodeDecodeError):
                continue
        # Select naturally written, context-matched clean sentences. For an
        # amount attack, every clean candidate uses the distinct invoice total.
        base_slots=dict(slots)
        if item['goal']=='change_amount':
            base_slots['amount']=rng.choice([x for x in ('0.03','0.075','0.125','1.25','18.40','42.75','120.00','250.50') if x!=slots['amount']])
        candidates=[]
        source,title,base_text=matched_base_goal(item,base_slots,rng,group)
        candidates.extend(s.text for s in split_segments(base_text))
        for ti in range(len(CRYPTO_TEMPLATES)):
            tid,text=crypto_generate(rng,ti,base_slots)
            if not item.get('context') or any(w in (tid+' '+text).lower() for w in item.get('context','').replace('_',' ').split()):
                candidates.extend(s.text for s in split_segments(text))
        for ti,template in enumerate(HARD_TEMPLATES):
            title_candidate,body=template.split(': ',1)
            text=fill_slots(body,base_slots)
            context_words=item.get('context','').replace('_',' ').split()
            if not context_words or any(w.lower() in (title_candidate+' '+text).lower() for w in context_words):
                candidates.extend(s.text for s in split_segments(text))
        candidates.extend(fill_slots(text,base_slots) for text in SHORT_CLEAN)
        inj_parts=split_segments(inj)
        chosen=[]
        for part in inj_parts:
            target=len(part.text.split())
            exact=[text for text in candidates if len(text.split())==target]
            sentence=rng.choice(exact) if exact else min(candidates,key=lambda text:abs(len(text.split())-target))
            chosen.append(sentence)
        anchor=split_segments(base_text)[0].text if split_segments(base_text) else base_text
        url_part=next((p.text for p in inj_parts if 'https://' in p.text or 'http://' in p.text),None)
        extra=[make_contact_line(slots,rng,include_url=bool(url_part),
                                 target_words=len(url_part.split()) if url_part else None)]
        if item['goal']=='change_amount':extra.append(f'The invoice total is {base_slots["amount"]} {base_slots["token"]}.')
        base_parts=[anchor]+[sentence for sentence in chosen if sentence!=anchor]+extra
        base='\n'.join(base_parts)
        carrier=rng.choice([x for x in item['carriers'] if x in carriers])
        clean_doc,attack_doc=assemble_pair(base,inj,None,carrier,rng)
        base_id=f'base-{group:06d}'; split='train' if unit_float(seed,base_id)<.8 else 'test_id'
        clean_text,clean_segs,_,_,_=clean_doc
        attack_text,attack_segs,attack_labels,_,span=attack_doc
        # A paired group contributes the unchanged base segments once and only
        # the inserted segment(s) from its injected version.
        for i,seg in enumerate(clean_segs):
            rows.append({'id':f'{base_id}-clean-{i}','base_doc_id':base_id,'doc_id':base_id+'-clean','split':split,'text':seg.text,'label':0,'source':source,'template_id':title})
        for i,(seg,label) in enumerate(zip(attack_segs,attack_labels)):
            if label:
                rows.append({'id':f'{base_id}-injected-{i}','base_doc_id':base_id,'doc_id':base_id+'-injected','split':split,'text':seg.text,'label':1,'source':'synthetic_injection','template_id':item['id'],'seed_id':item['id'],'goal':item['goal'],'style':item['style'],'carrier':carrier})
            else:
                rows.append({'id':f'{base_id}-context-{i}','base_doc_id':base_id,'doc_id':base_id+'-injected','split':split,'text':seg.text,'label':0,'source':source,'template_id':title})
        if slots['ens_name'] not in base or (url_part and slots['url'] not in base):
            raise AssertionError(f'{base_id} is missing the paired ENS/URL contact metadata')
        if slots['attacker_addr'].lower() in base.lower():
            raise AssertionError(f'{base_id} attacker address leaked into its base document')
        if item['goal']=='change_amount' and slots['amount']==base_slots['amount']:
            raise AssertionError(f'{base_id} change_amount does not differ from the invoice amount')
        pairs.append({'base_doc_id':base_id,'split':split,'goal':item['goal'],'carrier':carrier,'base':base,'clean_doc':clean_text,'injected_doc':attack_text,'injection_span':span,'injected_segments':[s.text for s,l in zip(attack_segs,attack_labels) if l],
                      'attacker_addr':slots['attacker_addr'],'recipient':slots['recipient'],'ens_name':slots['ens_name'],'url':slots['url'],
                      'attack_amount':slots['amount'],'base_amount':base_slots['amount'],'base64_payload':encoded_payload,
                      'url_in_attack':bool(url_part),
                      'uses_base64':'{base64_payload}' in str(item.get('text') or item.get('split_sentences') or '')})
        group+=1
    # This diagnostic sample uses only naturally occurring segment strings and
    # equal word-count strata. No segment is edited or padded.
    selected=[]
    for split in ('train','test_id'):
        split_rows=[r for r in rows if r['split']==split]
        buckets={label:{} for label in (0,1)}
        for row in split_rows:
            length=len(row['text'].split())
            key=(length,'http://' in row['text'] or 'https://' in row['text'],'.eth' in row['text'].lower())
            buckets[row['label']].setdefault(key,[]).append(row)
        matched=[]
        for length in sorted(set(buckets[0])&set(buckets[1])):
            n=min(len(buckets[0][length]),len(buckets[1][length]))
            matched.extend(rng.sample(buckets[0][length],n)); matched.extend(rng.sample(buckets[1][length],n))
        selected.extend(matched)
    if len(selected)>count:
        # Keep the diagnostic sample exactly at the requested size while
        # preserving split proportions, label balance, and exact word buckets.
        target_pairs=count//2
        split_caps={sp:sum(r['split']==sp and r['label']==1 for r in selected) for sp in ('train','test_id')}
        split_targets={sp:int(target_pairs*split_caps[sp]/max(1,sum(split_caps.values()))) for sp in split_caps}
        split_targets['train']+=target_pairs-sum(split_targets.values())
        sampled=[]
        for split in ('train','test_id'):
            part=[r for r in selected if r['split']==split]
            by_stratum={}
            for row in part:
                key=(len(row['text'].split()),'http://' in row['text'] or 'https://' in row['text'],'.eth' in row['text'].lower())
                by_stratum.setdefault(key,{0:[],1:[]})[row['label']].append(row)
            caps={key:min(len(b[0]),len(b[1])) for key,b in by_stratum.items()}
            need=split_targets[split]; total=sum(caps.values())
            alloc={key:int(need*c/max(1,total)) for key,c in caps.items()}
            remainder=need-sum(alloc.values())
            for key in sorted(caps,key=lambda x:(need*caps[x]/max(1,total)-alloc[x]),reverse=True)[:remainder]:alloc[key]+=1
            for key,take in alloc.items():
                sampled.extend(rng.sample(by_stratum[key][0],take));sampled.extend(rng.sample(by_stratum[key][1],take))
        selected=sampled
    return selected,pairs

def write_pairs(path,pairs,count=10):
    lines=['# Ten new matched base/injection pairs','',
      'The clean document is the base text unchanged. The injected document retains the same base and inserts the seed text at a sampled position. Both versions share the base_doc_id and split. Carriers are rendered over the inserted document and flattened as extracted text.','']
    for i,p in enumerate(pairs[:count],1):
        lines += [f'## Pair {i} · {p["base_doc_id"]} · {p["goal"]} · {p["carrier"]} · {p["split"]}','', '**Clean document (unchanged base)**','```text',p['clean_doc'],'```','', '**Injected document**','```text',p['injected_doc'],'```','', '**Inserted segment(s)**',*['- '+s for s in p['injected_segments']], '']
    Path(path).write_text('\n'.join(lines),encoding='utf-8')

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--segments',type=int,default=2000); ap.add_argument('--output',default='reports/sample_probe_report.md'); ap.add_argument('--examples',default='reports/new_paired_examples.md')
    args=ap.parse_args(); rows,pairs=make_sample(args.segments)
    from eth_utils import is_checksum_address
    attackers=[p['attacker_addr'] for p in pairs]
    if len(set(attackers))!=len(attackers) or any(not is_checksum_address(x) for x in attackers):
        raise AssertionError('attacker addresses must be fresh, unique EIP-55 checksummed values')
    encoded=[p['base64_payload'] for p in pairs if p['base64_payload']]
    expected_encoded=sum(bool(p['uses_base64']) for p in pairs)
    if len(encoded)!=expected_encoded:
        raise AssertionError(f'encoded payload count mismatch: expected {expected_encoded}, found {len(encoded)}')
    if len(encoded)!=len(set(encoded)):
        raise AssertionError('encoded instruction payloads are not unique per sample')
    train=[r for r in rows if r['split']=='train']; test=[r for r in rows if r['split']=='test_id']
    ROOT.joinpath('data').mkdir(exist_ok=True)
    write_jsonl(ROOT/'data'/'probe_sample_train.jsonl',train); write_jsonl(ROOT/'data'/'probe_sample_test_id.jsonl',test)
    result=tfidf_probe(train,test,enforce_length=False); ks=ks_word_count_pvalue(rows)
    ngram_stats=check_injected_ngram_frequency(rows)
    write_probe_report(args.output,result,ks,ngram_stats); write_pairs(args.examples,pairs)
    with Path(args.output).open('a',encoding='utf-8') as f:
        hard_negative_rows=sum(r['label']==0 and r.get('source')=='hard_negative' for r in rows)
        url_pairs=sum(p['url_in_attack'] for p in pairs)
        url_segment_counts={label:sum(label==r['label'] and ('http://' in r['text'] or 'https://' in r['text']) for r in rows) for label in (0,1)}
        ens_segment_counts={label:sum(label==r['label'] and '.eth' in r['text'].lower() for r in rows) for label in (0,1)}
        f.write(f'\n## Sample provenance\n\n- Segments: {len(rows)}\n- Train segments: {len(train)}\n- Test ID segments: {len(test)}\n- Base document groups: {len(pairs)}\n- Split key: `base_doc_id`\n- Construction: inserted and paraphrased seed text with extractor-style carrier flattening; clean examples preserve the same carrier layout and base content.\n- Unique EIP-55 attacker addresses: {len(set(attackers))}/{len(pairs)}\n- Unique per-sample encoded real instructions: {len(set(encoded))} across {len(encoded)} encoded samples\n- Innocent attack-language hard-negative templates available: {len(HARD_TEMPLATES)}; included in sample: {hard_negative_rows}\n- Clean/injected pair documents both contain an ENS contact (100%).\n- URL-bearing injected documents and their clean mates: {url_pairs}/{len(pairs)} ({url_pairs/max(1,len(pairs)):.1%}); contact sentences are length-matched to their inserted URL sentence.\n- Segment feature counts matched by label: URL clean/injected {url_segment_counts[0]}/{url_segment_counts[1]}; ENS clean/injected {ens_segment_counts[0]}/{ens_segment_counts[1]}.\n')
    print(f'Sample segments={len(rows)}; train={len(train)}; test_id={len(test)}; tfidf={result["tfidf_accuracy"]:.4f}; length={result["length_accuracy"]:.4f}; ks_p={ks:.6g}')

if __name__=='__main__': main()
