"""Load and fill the reviewed static injection and boundary seed files."""
import json
from pathlib import Path
from ..slots import fill_slots, make_slots

def read_json_yaml(path):
    # Supplied YAML seed files are JSON-compatible YAML by design.
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def render_seed(seed, rng):
    values=make_slots(rng)
    if seed.get('text') is not None:
        return fill_slots(seed['text'],values), list(seed.get('injected_idx') or [])
    sent=[fill_slots(x,values) for x in seed['split_sentences']]
    return ' '.join(sent), list(seed['injected_idx'] or [])

