"""Document insertion, extraction flattening, and segment labeling."""
import random
from .carriers import render_document
from .segmenter import split_segments

def format_document(text, layout):
    """Apply extractor-visible formatting parity to clean and injected docs."""
    wrappers=[lambda s:'\n'+s,
      lambda s:'### Payment record\n'+s,
      lambda s:'From: billing@merchant.net\nSubject: Payment details\n'+s,
      lambda s:'<section class="receipt">\n'+s+'\n</section>',
      lambda s:'```text\n'+s+'\n```',
      lambda s:'### Terms and payment\nFrom: accounts@merchant.net\n'+s+'\n```text\nstatus: filed\n```']
    return wrappers[layout%len(wrappers)](text)

def format_clean_document(text, rng):
    return format_document(text,rng.randrange(6))

def assemble(base, injected, carrier, rng, injected_indices=None, position=None):
    pos=position or rng.choices(['head','middle','tail'],[.25,.5,.25])[0]
    _,doc,start,end=render_document(base,injected,carrier,pos)
    marked=set(injected_indices or [])
    if not injected:
        segs=split_segments(doc)
        return doc,segs,[0]*len(segs),pos,(start,end)
    # Segment the three regions independently so a neighboring base sentence
    # can never be absorbed into an injection (or vice versa).
    regions=((0,start,False),(start,end,True),(end,len(doc),False))
    segs=[]; labels=[]; local_index=0
    for left,right,is_injection in regions:
        for part in split_segments(doc[left:right]):
            from .segmenter import Segment
            segs.append(Segment(part.start+left,part.end+left,part.text))
            labels.append(int(is_injection and (not marked or local_index in marked)))
            if is_injection: local_index+=1
    return doc,segs,labels,pos,(start,end)


def assemble_pair(base, injected, clean_control, carrier, rng, injected_indices=None):
    """Clean is the unchanged base; injection is inserted into that same base."""
    injected_doc, injected_segs, injected_labels, pos, span = assemble(
        base,injected,carrier,rng,injected_indices)
    _,clean_doc,_,_=render_document(base,'',carrier,pos)
    clean_segs=split_segments(clean_doc); clean_labels=[0]*len(clean_segs)
    return ((clean_doc,clean_segs,clean_labels,pos,(0,0)),
            (injected_doc,injected_segs,injected_labels,pos,span))

def contexts(segs,max_chars=1700):
    out=[]
    for i,s in enumerate(segs):
        prev=segs[i-1].text if i else ''; nxt=segs[i+1].text if i+1<len(segs) else ''
        value=f'{prev} [SEG] {s.text} [SEG] {nxt}'
        out.append(value[:max_chars])
    return out
