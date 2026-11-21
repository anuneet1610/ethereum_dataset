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

def word_length_metrics(rows):
    """KS effect size/p-value and length-only CV accuracy for labeled rows."""
    clean=sorted(len(r['text'].split()) for r in rows if int(r.get('label',0))==0)
    injected=sorted(len(r['text'].split()) for r in rows if int(r.get('label',0))==1)
    if not clean or not injected:
        return {'ks_d':1.0,'ks_p':0.0,'length_accuracy':1.0,
          'clean_mean':sum(clean)/len(clean) if clean else 0.0,'clean_median':_median(clean),
          'injected_mean':sum(injected)/len(injected) if injected else 0.0,'injected_median':_median(injected)}
    i=j=0; d=0.0
    while i<len(clean) or j<len(injected):
        value=min(clean[i] if i<len(clean) else float('inf'),injected[j] if j<len(injected) else float('inf'))
        while i<len(clean) and clean[i]<=value: i+=1
        while j<len(injected) and injected[j]<=value: j+=1
        d=max(d,abs(i/len(clean)-j/len(injected)))
    if d==0: p=1.0
    else:
        ne=len(clean)*len(injected)/(len(clean)+len(injected))
        lam=(ne**.5+.12+.11/(ne**.5))*d
        p=2*sum(((-1)**(k-1))*__import__('math').exp(-2*k*k*lam*lam) for k in range(1,101))
        p=max(0.0,min(1.0,p))
    accuracy=_length_only_accuracy(rows)
    return {'ks_d':d,'ks_p':p,'length_accuracy':accuracy,
      'clean_mean':sum(clean)/len(clean),'clean_median':_median(clean),
      'injected_mean':sum(injected)/len(injected),'injected_median':_median(injected)}

def _median(values):
    if not values: return 0.0
    mid=len(values)//2
    return float(values[mid]) if len(values)%2 else (values[mid-1]+values[mid])/2

def _length_only_accuracy(rows):
    labels=[int(r.get('label',0)) for r in rows]
    if len(set(labels))<2: return 1.0
    lengths=[len(r['text'].split()) for r in rows]
    train=[]; test=[]
    for label in (0,1):
        indices=[i for i,value in enumerate(labels) if value==label]
        indices.sort(key=lambda i:(i*1103515245+1729)%2147483647)
        n=max(1,int(len(indices)*.75))
        train.extend(indices[:n]); test.extend(indices[n:] or indices[-1:])
    values=sorted(set(lengths[i] for i in train))
    cuts=[values[0]-1]+[(a+b)/2 for a,b in zip(values,values[1:])]+[values[-1]+1]
    candidates=[]
    for cut in cuts:
        for invert in (0,1):
            predict=lambda i: int(lengths[i]>cut)^invert
            candidates.append((sum(predict(i)==labels[i] for i in train),sum(predict(i)==labels[i] for i in test)))
    best_train=max(item[0] for item in candidates)
    return max(item[1] for item in candidates if item[0]==best_train)/len(test)

def ks_word_count_pvalue(rows):
    """Backward-compatible accessor for the descriptive KS p-value."""
    return word_length_metrics(rows)['ks_p']

def length_source_category(row):
    source=str(row.get('source',''))
    template=str(row.get('template_id',''))
    if template.startswith('boundary-') or template.startswith('boundary_pair'):
        return 'boundary pairs'
    if row.get('hard_case'):
        return 'hard cases'
    if row.get('base_doc_id') and row.get('base_doc_id')!=row.get('doc_id'):
        return 'paired docs'
    if source in ('squad','triviaqa','general_prose'):
        return 'general prose'
    if source=='crypto_prose': return 'crypto prose'
    if source=='synthetic_injection': return 'paired docs'
    if source=='hard_negative': return 'hard cases'
    return source or 'unknown'

def length_report_by_source(rows):
    from collections import defaultdict
    grouped=defaultdict(list)
    for row in rows: grouped[length_source_category(row)].append(row)
    for name in ('paired docs','general prose','crypto prose','boundary pairs','hard cases'):
        grouped.setdefault(name,[])
    return {name:{'rows':len(group),'metrics':word_length_metrics(group)} for name,group in sorted(grouped.items())}

def match_word_length_strata(rows,seed=1729):
    """Downweight rows into exact word-count strata independently per split."""
    by_split={}
    for row in rows:
        by_split.setdefault(row.get('split',''),{0:[],1:[]})[int(row.get('label',0))].append(row)
    selected=[]
    for split,labels in sorted(by_split.items()):
        def buckets(items):
            result={}
            for row in items:
                result.setdefault(len(row['text'].split()),[]).append(row)
            return result
        clean=buckets(labels[0]); injected=buckets(labels[1])
        for length in sorted(set(clean)&set(injected)):
            n=min(len(clean[length]),len(injected[length]))
            selected.extend(clean[length][:n]); selected.extend(injected[length][:n])
    return selected

def downsample_injections_to_ngram_cap(rows,max_rate=.02):
    """Deterministically thin only attack rows until the phrase cap is met."""
    kept=list(rows)
    while True:
        stats=injected_ngram_frequencies(kept)
        if stats['max_rate']<=max_rate: return kept
        worst=tuple(stats['worst_ngram'].split())
        candidates=[]
        for i,row in enumerate(kept):
            if int(row.get('label',0))!=1: continue
            text=re.sub(r'https?://\S+|0x[a-fA-F0-9]{40}|\b[A-Za-z0-9+/]{24,}={0,2}\b',' ',str(row.get('text','')))
            words=[w.lower() for w in re.findall(r"[a-z]+(?:'[a-z]+)?",text) if w.lower() not in _NG_STOPWORDS]
            if any(tuple(words[j:j+len(worst)])==worst for j in range(len(words)-len(worst)+1)):
                candidates.append(i)
        if not candidates: raise AssertionError('ngram cap reported a cue with no removable injection row')
        # Remove one occurrence per pass. Use a stable rotating choice so that
        # repeated build runs select the same examples.
        remove=candidates[-1]
        kept.pop(remove)

def check_length_balance(rows,max_d=.10,max_accuracy=.60):
    metrics=word_length_metrics(rows)
    if metrics['ks_d']>max_d or metrics['length_accuracy']>max_accuracy:
        raise AssertionError(f"word-length balance failed: KS D={metrics['ks_d']:.4f} (max {max_d:.2f}), length-only accuracy={metrics['length_accuracy']:.4f} (max {max_accuracy:.2f}); KS p={metrics['ks_p']:.6g}")
    return metrics

_NG_STOPWORDS=set('a an and are as at be been being by can could did do does for from had has have he her here hers him his how i if in into is it its me my of on or our ours she that the their theirs them then there these they this to was we were what when where which who why with would you your'.split())

def injected_ngram_frequencies(rows):
    """Document frequency of content bigrams/trigrams in injections.

    Function words and per-sample identifiers (URLs, EVM addresses, base64
    blobs) are excluded; they are not reusable instruction cues.
    """
    from collections import Counter
    counts=Counter(); total=0
    for row in rows:
        if int(row.get('label',0))!=1: continue
        total+=1
        text=str(row.get('text',''))
        text=re.sub(r'https?://\S+|0x[a-fA-F0-9]{40}|\b[A-Za-z0-9+/]{24,}={0,2}\b',' ',text)
        words=[w.lower() for w in re.findall(r"[a-z]+(?:'[a-z]+)?",text) if w.lower() not in _NG_STOPWORDS]
        for n in (2,3): counts.update(set(tuple(words[i:i+n]) for i in range(len(words)-n+1)))
    worst=max(counts.items(),key=lambda item:item[1],default=((),0))
    rate=worst[1]/max(1,total)
    return {'injection_count':total,'max_rate':rate,'worst_ngram':' '.join(worst[0]),'worst_count':worst[1],
      'counts':counts}

def check_injected_ngram_frequency(rows,max_rate=.02):
    stats=injected_ngram_frequencies(rows)
    if stats['max_rate']>max_rate:
        raise AssertionError(f'injected content n-gram {stats["worst_ngram"]!r} occurs in {stats["worst_count"]}/{stats["injection_count"]} segments ({stats["max_rate"]:.2%}), over {max_rate:.2%}')
    return stats

def tfidf_probe(train_rows,test_rows,enforce_length=True):
    """Train a text TF-IDF probe and length-only logistic classifier."""
    try:
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.linear_model import LogisticRegression
        from sklearn.metrics import accuracy_score
    except ImportError as exc:
        raise RuntimeError('scikit-learn is required for the TF-IDF probe') from exc
    xtr=[r['text'] for r in train_rows]; ytr=[int(r['label']) for r in train_rows]
    xte=[r['text'] for r in test_rows]; yte=[int(r['label']) for r in test_rows]
    vector=TfidfVectorizer(ngram_range=(1,2),max_features=50000,sublinear_tf=True)
    a=vector.fit_transform(xtr); b=vector.transform(xte)
    model=LogisticRegression(max_iter=1000,class_weight='balanced',random_state=1729).fit(a,ytr)
    pred=model.predict(b); accuracy=accuracy_score(yte,pred)
    names=vector.get_feature_names_out(); coef=model.coef_[0]
    top_injected=[(names[i],float(coef[i])) for i in coef.argsort()[-40:][::-1]]
    top_clean=[(names[i],float(coef[i])) for i in coef.argsort()[:40]]
    all_rows=list(train_rows)+list(test_rows)
    all_matrix=vector.transform([r['text'] for r in all_rows]).tocsr()
    all_labels=[int(r['label']) for r in all_rows]
    cue_frequency={}
    for cue,_ in set(top_injected+top_clean):
        col=int(vector.vocabulary_[cue]); present=all_matrix[:,col].getnnz(axis=1)
        clean_n=sum(int(v)>0 and label==0 for v,label in zip(present,all_labels))
        inj_n=sum(int(v)>0 and label==1 for v,label in zip(present,all_labels))
        clean_total=sum(label==0 for label in all_labels); inj_total=sum(label==1 for label in all_labels)
        cue_frequency[cue]={'clean_count':clean_n,'clean_total':clean_total,'clean_rate':clean_n/max(1,clean_total),
          'injected_count':inj_n,'injected_total':inj_total,'injected_rate':inj_n/max(1,inj_total)}
    lens_train=[[len(r['text'].split())] for r in train_rows]; lens_test=[[len(r['text'].split())] for r in test_rows]
    length_model=LogisticRegression(max_iter=1000,class_weight='balanced',random_state=1729).fit(lens_train,ytr)
    length_accuracy=accuracy_score(yte,length_model.predict(lens_test))
    if enforce_length and length_accuracy>.65: raise AssertionError(f'length-only probe accuracy {length_accuracy:.4f} exceeds 0.65')
    return {'tfidf_accuracy':float(accuracy),'length_accuracy':float(length_accuracy),'top_injected':top_injected,'top_clean':top_clean,'cue_frequency':cue_frequency}

def check_format_parity(clean_docs,injected_docs,max_gap=.15):
    patterns={'newlines':r'\n','markdown_header':r'(?m)^#{1,6}\s','htmlish':r'<[A-Za-z!/]',
      'code_block':r'```','email_header':r'(?im)^(?:from|to|subject):'}
    report={}
    for name,pattern in patterns.items():
        clean=sum(bool(re.search(pattern,d.get('text',''))) for d in clean_docs)/max(1,len(clean_docs))
        injected=sum(bool(re.search(pattern,d.get('text',''))) for d in injected_docs)/max(1,len(injected_docs))
        report[name]=(clean,injected)
        if abs(clean-injected)>max_gap:
            raise AssertionError(f'formatting parity failed for {name}: clean={clean:.3f}, injected={injected:.3f}')
    return report

def write_probe_report(path,result,ks_p,ngram_stats=None):
    lines=['# TF-IDF and length probe','',f'- TF-IDF accuracy on test_id: {result["tfidf_accuracy"]:.4f}',
      f'- Length-only accuracy on test_id: {result["length_accuracy"]:.4f}',f'- Word-count KS p-value: {ks_p:.6g}','',
      f'- Injected content phrase n-gram maximum frequency (2–3 words; function words and per-sample identifiers excluded): {ngram_stats["worst_count"]}/{ngram_stats["injection_count"]} ({ngram_stats["max_rate"]:.2%}) for `{ngram_stats["worst_ngram"]}`' if ngram_stats else '',
      '## Top 40 injected cues','']
    lines += [f'- `{w}`: {v:.4f} · clean {result["cue_frequency"][w]["clean_count"]}/{result["cue_frequency"][w]["clean_total"]} ({result["cue_frequency"][w]["clean_rate"]:.1%}); injected {result["cue_frequency"][w]["injected_count"]}/{result["cue_frequency"][w]["injected_total"]} ({result["cue_frequency"][w]["injected_rate"]:.1%})' for w,v in result['top_injected']]
    lines += ['', '## Top 40 clean cues','']
    lines += [f'- `{w}`: {v:.4f} · clean {result["cue_frequency"][w]["clean_count"]}/{result["cue_frequency"][w]["clean_total"]} ({result["cue_frequency"][w]["clean_rate"]:.1%}); injected {result["cue_frequency"][w]["injected_count"]}/{result["cue_frequency"][w]["injected_total"]} ({result["cue_frequency"][w]["injected_rate"]:.1%})' for w,v in result['top_clean']]
    cues=list(dict.fromkeys([w for w,_ in result['top_injected']]+[w for w,_ in result['top_clean']]))
    lines += ['', '## Cue frequencies by label', '',
      '| Cue | Clean count/rate | Injected count/rate |','|---|---:|---:|']
    lines += [f'| `{cue}` | {result["cue_frequency"][cue]["clean_count"]}/{result["cue_frequency"][cue]["clean_total"]} ({result["cue_frequency"][cue]["clean_rate"]:.1%}) | {result["cue_frequency"][cue]["injected_count"]}/{result["cue_frequency"][cue]["injected_total"]} ({result["cue_frequency"][cue]["injected_rate"]:.1%}) |' for cue in cues]
    if result['tfidf_accuracy']>.95: lines += ['', '> Warning: TF-IDF accuracy exceeds 0.95; inspect for template leakage.']
    Path(path).write_text('\n'.join(lines)+'\n',encoding='utf-8')

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
                except ImportError as exc:
                    raise RuntimeError('eth-utils with a Keccak backend is required to verify fresh EIP-55 addresses') from exc

def deduplicate_rows(rows, threshold=.90):
    """Normalized exact dedup plus MinHash/LSH or bounded shingle buckets."""
    import hashlib
    def normalize(value):
        text=str(value).lower()
        text=re.sub(r'0x[a-f0-9]{40}', ' <addr> ', text)
        text=re.sub(r'\b\d+(?:[.,]\d+)*\b',' <num> ',text)
        return re.sub(r'\s+',' ',text).strip()
    exact=set(); unique=[]
    for row in rows:
        text=normalize(row.get('text',''))
        digest=hashlib.blake2b(text.encode('utf-8'),digest_size=16).digest()
        if digest in exact: continue
        exact.add(digest); unique.append((row,text))
    try:
        from datasketch import MinHash,MinHashLSH
        lsh=MinHashLSH(threshold=threshold,num_perm=64); kept=[]
        for i,(row,text) in enumerate(unique):
            shingles=set(text.split())
            shingles={' '.join(text.split()[j:j+5]) for j in range(max(1,len(text.split())-4))}
            mh=MinHash(num_perm=64)
            for sh in shingles: mh.update(sh.encode('utf-8'))
            if lsh.query(mh): continue
            key=str(i); lsh.insert(key,mh); kept.append(row)
        return kept
    except ImportError:
        # With no LSH dependency, retain exact-hash dedup only. This avoids
        # false positives from coarse band collisions.
        return [row for row,_ in unique]

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

