"""Optional local Ollama paraphrase client with deterministic on-disk caching."""
import hashlib, json, pathlib, requests

def paraphrase(text, cache_dir='cache/paraphrases', model='qwen2.5:7b-instruct', base_url='http://localhost:11434/api/generate'):
    cache=pathlib.Path(cache_dir); cache.mkdir(parents=True,exist_ok=True)
    key=hashlib.sha256((model+'\0'+text).encode()).hexdigest(); path=cache/(key+'.json')
    if path.exists(): return json.loads(path.read_text(encoding='utf-8'))
    prompt='Paraphrase the following sentence in 2 to 4 distinct ways. Preserve every amount, address, and goal exactly. Return a JSON array only. Text: '+text
    response=requests.post(base_url,json={'model':model,'prompt':prompt,'stream':False,'options':{'temperature':0.9}},timeout=120)
    response.raise_for_status(); raw=response.json().get('response','[]')
    try: result=json.loads(raw)
    except Exception: result=[]
    result=[x for x in result if isinstance(x,str) and len(x.split())<60]
    path.write_text(json.dumps(result,ensure_ascii=False),encoding='utf-8'); return result
