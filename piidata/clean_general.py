"""Optional adapters for clean paragraph datasets from Hugging Face."""
def load_general(limit=5000):
    try:
        from datasets import load_dataset
    except ImportError:
        return []
    out=[]
    for name, config, split, fields in [('squad',None,'train',['context']),('trivia_qa','rc','train',['search_results'])]:
        try:
            ds=load_dataset(name,config,split=split,streaming=True)
            for row in ds:
                vals=[]
                for f in fields:
                    v=row.get(f,'')
                    if isinstance(v,dict): v=' '.join(v.get('search_context',[]) or [])
                    if isinstance(v,list): v=' '.join(map(str,v))
                    if isinstance(v,str): vals.append(v)
                text=' '.join(vals).strip()
                if text and len(text.split())<=350: out.append((name,text))
                if len(out)>=limit: return out
        except Exception:
            continue
    return out
