"""Load JSONL splits into a Hugging Face DatasetDict."""
import json
from pathlib import Path

def load_dataset_dict(data_dir='data',use_context=True):
    try: from datasets import Dataset, DatasetDict
    except ImportError as exc: raise RuntimeError('Install the listed dependency `datasets` to use loader.py') from exc
    root=Path(data_dir); result={}
    for split in ('train','val','test_id','test_heldout','test_ood_crai','redteam_manual'):
        path=root/f'{split}.jsonl'
        rows=[json.loads(x) for x in path.read_text(encoding='utf-8').splitlines() if x.strip()] if path.exists() else []
        if not use_context:
            for row in rows: row.pop('context',None)
        result[split]=Dataset.from_list(rows)
    return DatasetDict(result)
