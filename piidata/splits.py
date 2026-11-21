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
        group=r.get('base_doc_id') or r.get('seed_id') or r.get('template_id')
        split=r.get('split')
        if group in seen and seen[group]!=split:
            raise AssertionError(f'group leakage: {group}: {seen[group]} vs {split}')
        seen[group]=split
    return True

def assign_stratified_seed_groups(seeds,seed=1729,heldout_styles=(),heldout_goals=(),heldout_carriers=()):
    """Assign whole seed IDs to 80/10/10 splits while balancing goal and style."""
    held_style=set(heldout_styles); held_goal=set(heldout_goals); held_carrier=set(heldout_carriers)
    result={}; buckets={'train':[],'val':[],'test_id':[]}; rates={'train':.8,'val':.1,'test_id':.1}
    ordinary=[]
    for item in seeds:
        if item['style'] in held_style or item['goal'] in held_goal or set(item.get('carriers',()))&held_carrier:
            result[item['id']]='test_heldout'
        else: ordinary.append(item)
    ordinary.sort(key=lambda s:unit_float(seed,s['id']))
    by_goal={}; by_style={}
    for split in buckets: by_goal[split]={}; by_style[split]={}
    goal_totals={}; style_totals={}
    for item in ordinary:
        goal_totals[item['goal']]=goal_totals.get(item['goal'],0)+1
        style_totals[item['style']]=style_totals.get(item['style'],0)+1
    for item in ordinary:
        options=[]
        for split in buckets:
            g=(by_goal[split].get(item['goal'],0)+1)/(rates[split]*goal_totals[item['goal']])
            s=(by_style[split].get(item['style'],0)+1)/(rates[split]*style_totals[item['style']])
            global_load=(len(buckets[split])+1)/(rates[split]*max(1,len(ordinary)))
            options.append((g+s+0.25*global_load+unit_float(seed,item['id']+split)*1e-6,split))
        dest=min(options)[1]; result[item['id']]=dest; buckets[dest].append(item)
        by_goal[dest][item['goal']]=by_goal[dest].get(item['goal'],0)+1
        by_style[dest][item['style']]=by_style[dest].get(item['style'],0)+1
    return result
