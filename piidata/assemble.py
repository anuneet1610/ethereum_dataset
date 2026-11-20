"""Document insertion, extraction flattening, and segment labeling."""
import random
from .carriers import render, flatten
from .segmenter import split_segments

def assemble(base, injected, carrier, rng, injected_indices=None):
    base_parts=split_segments(base)
    pos=rng.choices(['head','middle','tail'],[.25,.5,.25])[0]
    at=0 if pos=='head' else (len(base_parts)//2 if pos=='middle' else len(base_parts))
    before=' '.join(x.text for x in base_parts[:at]); after=' '.join(x.text for x in base_parts[at:])
    rendered=render(injected,carrier); extracted=flatten(rendered,carrier)
    doc=' '.join(x for x in [before,extracted,after] if x)
    start=doc.find(extracted)
    marked=set(injected_indices or [])
    segs=split_segments(doc); labels=[]
    if marked:
        injsegs=split_segments(extracted)
        ranges=[]; p=start
        for s in injsegs: ranges.append((p+s.start,p+s.end))
        for i,s in enumerate(segs): labels.append(int(any(i2 in marked and min(s.end,b)-max(s.start,a)>0 for i2,(a,b) in enumerate(ranges))))
    else:
        end=start+len(extracted)
        for s in segs:
            overlap=max(0,min(s.end,end)-max(s.start,start))
            labels.append(int(s.end>s.start and overlap/(s.end-s.start)>=.30))
    return doc,segs,labels,pos,(start,start+len(extracted))

def contexts(segs,max_chars=1700):
    out=[]
    for i,s in enumerate(segs):
        prev=segs[i-1].text if i else ''; nxt=segs[i+1].text if i+1<len(segs) else ''
        value=f'{prev} [SEG] {s.text} [SEG] {nxt}'
        out.append(value[:max_chars])
    return out
