"""Stable group assignment helpers."""
import hashlib

def unit_float(seed, value):
    h=hashlib.sha256(f'{seed}:{value}'.encode()).digest()
    return int.from_bytes(h[:8],'big')/2**64

def assign_group(group, seed=1729, heldout=False):
    if heldout: return 'test_heldout'
    x=unit_float(seed,group)
    return 'train' if x<.8 else ('val' if x<.9 else 'test_id')

def assert_no_leakage(rows):
    seen={}
    for r in rows:
        group=r.get('seed_id') or r.get('template_id')
        split=r.get('split')
        if group in seen and seen[group]!=split:
            raise AssertionError(f'group leakage: {group}: {seen[group]} vs {split}')
        seen[group]=split
    return True
