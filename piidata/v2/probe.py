"""Cheap shortcut probe: TF-IDF + logistic regression trained on v1 vs v1+v2.

Not a substitute for the DeBERTa run. It shows whether the word-level shortcut
("instruction words mean injection") still pays off in the training data.

    python -m piidata.v2.probe
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D, V2 = ROOT / 'data', ROOT / 'data' / 'v2'
CUES = ['ignore', 'sign', 'transfer', 'approval', 'instructions', 'override', 'approve', 'confirm', 'send', 'agent',
        'assistant', 'ai', 'user']


def read(p):
    return [json.loads(l) for l in p.open(encoding='utf-8') if l.strip()]


def main():
    import numpy as np
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.linear_model import LogisticRegression

    drop = {i for v in json.loads((V2 / 'v1_drop_from_train.json').read_text())['ids'].values() for i in v}
    v1 = [r for r in read(D / 'train.jsonl') + read(D / 'train_crai.jsonl') if r['id'] not in drop]
    v2 = read(V2 / 'train.jsonl')
    evals = {
        'test_docs (FP)': read(V2 / 'test_docs.jsonl'),
        'test_wallet_help (FP)': read(V2 / 'test_wallet_help.jsonl'),
        'test_wallet_help_synth (FP)': read(V2 / 'test_wallet_help_synth.jsonl'),
        'test_synth_clean (FP)': read(V2 / 'test_synth_clean.jsonl'),
        'test_attacks_v2 (TPR)': read(V2 / 'test_attacks_v2.jsonl'),
        'test_unseen_styles': read(V2 / 'test_unseen_styles.jsonl'),
        'test_contrast': read(V2 / 'test_contrast.jsonl'),
        'v1 test_id': read(D / 'test_id.jsonl'),
        'v1 test_heldout': read(D / 'test_heldout.jsonl'),
        'v1 test_ood_crai': read(D / 'test_ood_crai.jsonl'),
    }
    lines = ['# v2 TF-IDF shortcut probe', '',
             'Bag-of-words logistic regression (1-2 grams, balanced classes, threshold 0.5). A weak model on purpose: '
             'it shows which words the training data rewards, not what DeBERTa will score.', '',
             '| Eval set | Metric | v1 train | v1 + v2 train |', '|---|---|---:|---:|']
    models = {}
    for name, rows in (('v1', v1), ('v1+v2', v1 + v2)):
        vec = TfidfVectorizer(ngram_range=(1, 2), min_df=2, max_features=60000, sublinear_tf=True)
        X = vec.fit_transform([r['text'] for r in rows])
        lr = LogisticRegression(max_iter=3000, class_weight='balanced', C=4.0).fit(X, [r['label'] for r in rows])
        models[name] = (vec, lr)
    for ev, rows in evals.items():
        res = []
        for name in ('v1', 'v1+v2'):
            vec, lr = models[name]
            p = lr.predict(vec.transform([r['text'] for r in rows]))
            y = np.array([r['label'] for r in rows])
            tpr = p[y == 1].mean() * 100 if (y == 1).any() else None
            fpr = p[y == 0].mean() * 100 if (y == 0).any() else None
            res.append((tpr, fpr))
        for k, label in ((1, 'false alarms %'), (0, 'detection %')):
            if res[0][k] is not None:
                lines.append(f'| {ev} | {label} | {res[0][k]:.1f} | {res[1][k]:.1f} |')
    for name in ('v1', 'v1+v2'):
        vec, lr = models[name]
        names = np.array(vec.get_feature_names_out()); w = lr.coef_[0]
        lines += ['', f'## Strongest injected cues, {name}', '', ', '.join(f'`{x}`' for x in names[np.argsort(w)[-30:]][::-1])]
        vocab = vec.vocabulary_
        lines += ['', f'Weights of instruction words ({name}): ' +
                  ', '.join(f'`{c}` {w[vocab[c]]:+.2f}' for c in CUES if c in vocab)]
    (ROOT / 'reports' / 'v2_probe.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
