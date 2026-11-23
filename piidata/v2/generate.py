"""Expand v2 templates into labelled single-segment rows."""
import random, re

from ..segmenter import split_segments
from ..slots import make_slots, fill_slots, AMOUNTS, ENS
from ..splits import unit_float
from . import templates as T

_ALT = re.compile(r'\[\[((?:(?!\[\[|\]\]).)*)\]\]')

# Synonym groups. One choice per example, applied identically to a clean sentence and its twin
# so contrast pairs differ only in addressee and goal.
SYNONYMS = [
    ('recovery phrase', 'seed phrase', 'Secret Recovery Phrase', 'recovery words', '12-word phrase', 'mnemonic phrase'),
    ('your wallet', 'the wallet app', 'your browser wallet', 'your mobile wallet'),
    ('Click', 'Tap', 'Press', 'Select'),
    ('Check', 'Verify', 'Confirm', 'Double-check'),
    ('the user', 'the user', 'the account holder', 'the wallet owner', 'the customer'),
    ('block explorer', 'block explorer', 'Etherscan', 'chain explorer'),
]
HELP_PREFIX = ['', '', '', 'Tip: ', 'Note: ', 'Important: ', 'Remember: ', 'Security tip: ', 'Good to know: ']
OWN_ENS = ['savings.eth', 'my-vault.eth', 'alice-cold.eth', 'rahul-savings.eth']


def expand(template, rng):
    prev = None
    while prev != template:
        prev = template
        template = _ALT.sub(lambda m: rng.choice(m.group(1).split('|')), template, count=1)
    return template


def v2_slots(rng):
    s = make_slots(rng)
    s['amount2'] = rng.choice([a for a in AMOUNTS + ['500.00', '1500', '75.00', '9.99'] if a != s['amount']])
    s['own_ens'] = rng.choice(OWN_ENS)
    s['code'] = f'{rng.randrange(100000, 999999)}'
    return s


def synonymise(texts, rng):
    """Apply the same synonym choice to every string in texts (a clean/twin pair)."""
    out = list(texts)
    for group in SYNONYMS:
        if len(set(group)) < 2: continue
        pick = rng.choice(group)
        pat = re.compile('|'.join(re.escape(g) for g in sorted(set(group), key=len, reverse=True)))
        if any(pat.search(t) for t in out):
            out = [pat.sub(pick, t) for t in out]
    return out


def sloppy(texts, rng):
    """User-typed surface noise: lowercase start, dropped period, trailing pls/thanks."""
    r = rng.random()
    out = []
    for t in texts:
        if r < 0.25 and t[:1].isupper() and not t[1:2].isupper() and not t.startswith(('I ', "I'")): t = t[0].lower() + t[1:]
        if 0.25 <= r < 0.45 and t.endswith('.'): t = t[:-1]
        if 0.45 <= r < 0.55: t = t.rstrip('.') + (' thanks' if rng.random() < .5 else ' pls')
        out.append(t)
    return out


def addr(split, rng):
    return rng.choice(T.ADDR_TEST if split == 'test' else T.ADDR_TRAIN)


_CUE = re.compile(r'0x[0-9a-fA-F]{40}|https?://|\b(AI|agent|agents|assistant|assistants|bot|bots|model|LLM|automated|'
                  r'system|recovery phrase|seed phrase|private key|user\'?s?|confirm\w*|approv\w*|sign|signature|permit\w*|'
                  r'balance|history|transfer|send|pay\w*|spend\w*)\b', re.I)


def segments_of(text):
    return [s.text for s in split_segments(text)]


def template_split(group, seed):
    x = unit_float(seed, 'v2:' + group)
    return 'train' if x < .70 else ('dev' if x < .85 else 'test')


def _row(text, label, split, source, group, idx, **meta):
    rid = f'v2-{split}-{group}-{idx}'
    base = dict(id=rid, doc_id=rid, split=split, text=text, context=f' [SEG] {text} [SEG] ', label=int(label),
                source=source, template_id=group, seed_id=group if label else None, goal=meta.pop('goal', None),
                style=meta.pop('style', None), carrier=meta.pop('carrier', None), position=None, hard_case=None,
                paraphrased=False, seg_index=0, n_segments=1)
    base.update(meta)
    return base


CLEAN_SETS = {
    'v2_wallet_help': (T.WALLET_HELP, 'help'),
    'v2_user_command': (T.USER_COMMANDS, 'cmd'),
    'v2_web_clutter': (T.WEB_CLUTTER, 'clutter'),
    'v2_email': (T.EMAILS, 'email'),
    'v2_trigger_words': (T.BENIGN_TRIGGER_WORDS, 'trig'),
    'v2_ai_mentions': (T.AI_MENTIONS, 'aim'),
    'v2_trigger_words_2': (T.TRIGGER_WORDS_2, 'trig2'),
    'v2_trigger_grammar': (T.TRIGGER_GRAMMAR, 'tgram'),
    'v2_agent_grammar': (T.AGENT_GRAMMAR, 'agram'),
}
# Variants generated per template (before dedup).
PER_TEMPLATE = {'v2_wallet_help': 16, 'v2_user_command': 16, 'v2_web_clutter': 6, 'v2_email': 12, 'v2_trigger_words': 7,
                'v2_ai_mentions': 12, 'v2_trigger_words_2': 8, 'v2_trigger_grammar': 45, 'v2_agent_grammar': 45}
ATTACKS_PER_TEMPLATE = 22


def clean_and_twin_rows(seed, group_split):
    rng = random.Random(seed + 11)
    rows = []
    for source, (entries, short) in CLEAN_SETS.items():
        for i, (clean_t, twin_t) in enumerate(entries):
            group = f'{short}-{i:03d}'
            split = group_split(group)
            seen = set()
            for k in range(PER_TEMPLATE[source] * 3):
                if len(seen) >= PER_TEMPLATE[source]: break
                slots = v2_slots(rng)
                # Expand alternations with one rng state so pair choices line up.
                state = rng.getstate()
                c = expand(clean_t, rng)
                if twin_t:
                    rng.setstate(state); tw = expand(twin_t, rng)
                else:
                    tw = None
                texts = [c] + ([tw] if tw else [])
                if source == 'v2_wallet_help':
                    texts = synonymise(texts, rng)
                    pre = '' if re.match(r'^(Tip|Note|Important|Warning|Step)', texts[0]) else rng.choice(HELP_PREFIX)
                    texts = [pre + texts[0]] + texts[1:]
                elif source == 'v2_user_command':
                    texts = sloppy(texts, rng)
                elif source in ('v2_email', 'v2_trigger_words', 'v2_ai_mentions', 'v2_trigger_words_2'):
                    texts = synonymise(texts, rng)
                texts = [fill_slots(t, slots) for t in texts]
                if texts[0] in seen: continue
                seen.add(texts[0])
                pair_id = f'{group}-{len(seen)}'
                for j, seg in enumerate(segments_of(texts[0])):
                    rows.append(_row(seg, 0, split, source, group, f'{len(seen)}c{j}', pair_id=pair_id,
                                     family=None, v2_set=source))
                if len(texts) > 1:
                    clean_segs = set(segments_of(texts[0]))
                    for j, seg in enumerate(segments_of(texts[1])):
                        if seg in clean_segs or not _CUE.search(seg):
                            continue  # shared/cue-less piece: not part of the attack
                        rows.append(_row(seg, 1, split, 'v2_contrast_twin', group, f'{len(seen)}t{j}', pair_id=pair_id,
                                         family='contrast_' + short, v2_set=source, style='contrast_pair'))
    return rows


def attack_rows(seed, group_split, test_only_to_test=True):
    rng = random.Random(seed + 23)
    rows = []
    for family, entries in T.ATTACKS.items():
        for i, tmpl in enumerate(entries):
            group = f'atk-{family}-{i:03d}'
            split = 'test' if (family in T.TEST_ONLY_FAMILIES and test_only_to_test) else group_split(group)
            parts = tmpl if isinstance(tmpl, list) else [tmpl]
            seen = set()
            for k in range(ATTACKS_PER_TEMPLATE * 3):
                if len(seen) >= ATTACKS_PER_TEMPLATE: break
                slots = v2_slots(rng)
                a = addr(split, rng)
                texts = [fill_slots(expand(p.replace('{ADDR}', a), rng), slots) for p in parts]
                texts = synonymise(texts, rng)
                texts = [t[0].upper() + t[1:] if t[:1].islower() else t for t in texts]
                key = ' '.join(texts)
                if key in seen: continue
                seen.add(key)
                n = len(seen)
                for pi, t in enumerate(texts):
                    segs = segments_of(t)
                    for j, seg in enumerate(segs):
                        if len(segs) > 1 and not _CUE.search(seg):
                            continue  # e.g. a bare "Invoice settled." lead-in is not labelled injected
                        rows.append(_row(seg, 1, split, 'v2_attack', group, f'{n}p{pi}s{j}', family=family,
                                         style=family, goal=None, pair_id=None, v2_set='v2_attack',
                                         carrier='email_quote' if family == 'quoted_email' else None))
            if family in T.TEST_ONLY_FAMILIES and i == 0:
                for ci, ct in enumerate(T.TEST_ONLY_CLEAN[family]):
                    for k in range(4):
                        t = fill_slots(ct, v2_slots(rng))
                        rows.append(_row(t, 0, 'test', 'v2_test_only_clean', f'clean-{family}-{ci:02d}', f'{k}',
                                         family=family, v2_set='v2_attack', pair_id=None))
    return rows


COMPOSE_PER_FRAME = {'train': 34, 'dev': 26, 'test': 26}


def composed_attack_rows(seed, group_split):
    """Frame x action x suffix x addressing. Frames are the split unit, so test frames are unseen."""
    rng = random.Random(seed + 37)
    goals = sorted(T.ACTIONS)
    rows = []
    for family, frames in T.FRAMES.items():
        for i, frame in enumerate(frames):
            group = f'cmp-{family}-{i:02d}'
            split = group_split(group)
            seen = set()
            for k in range(COMPOSE_PER_FRAME[split] * 4):
                if len(seen) >= COMPOSE_PER_FRAME[split]: break
                slots = v2_slots(rng)
                goal = rng.choice(T.IMPLICIT_GOALS if family == 'implicit_harm' else goals)
                act = rng.choice(T.SHORT_ACTIONS) if family == 'short_agent_line' else rng.choice(T.ACTIONS[goal])
                suffix = rng.choice(T.SUFFIXES)
                if goal == 'suppress_confirmation' and 'confirm' in suffix: suffix = ''
                text = expand(frame, rng)
                text = (text.replace('{ADDR}', addr(split, rng)).replace('{Act}', act[0].upper() + act[1:])
                        .replace('{act}', act).replace('{sact}', act).replace('{suffix}', suffix))
                text = fill_slots(text, slots)
                text = synonymise([text], rng)[0]
                text = text[0].upper() + text[1:]
                segs = segments_of(text)
                if len(segs) != 1 or text in seen: continue
                seen.add(text)
                rows.append(_row(text, 1, split, 'v2_attack', group, len(seen), family=family, style=family,
                                 goal=None if family == 'short_agent_line' else goal, pair_id=None, v2_set='v2_attack'))
    return rows


def prose_swap(sentence, rng, slots):
    """Agent-addressed (and sometimes harmful) twin of an imperative documentation sentence."""
    s = sentence.strip()
    s_noperiod = s.rstrip('.!:;')
    s_lc = s[0].lower() + s[1:]
    tmpl = rng.choice(T.SWAP_HARM if rng.random() < 0.55 else T.SWAP_PREFIX)
    out = expand(tmpl, rng).replace('{s_noperiod}', s_noperiod).replace('{s_lc}', s_lc).replace('{s}', s)
    out = fill_slots(out, slots)
    if not out.endswith(('.', '!', '?')): out += '.'
    return out


def is_imperative(sentence):
    w = re.findall(r"[A-Za-z']+", sentence[:40])
    if ':' in sentence[:25] or '|' in sentence or not sentence.rstrip().endswith('.'):
        return False
    return bool(w) and w[0].lower() in T.IMPERATIVE_VERBS and sentence[:1].isupper() and 6 <= len(sentence.split()) <= 40
