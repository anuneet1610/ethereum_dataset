# v2 TF-IDF shortcut probe

Bag-of-words logistic regression (1-2 grams, balanced classes, threshold 0.5). A weak model on purpose: it shows which words the training data rewards, not what DeBERTa will score.

| Eval set | Metric | v1 train | v1 + v2 train |
|---|---|---:|---:|
| test_docs (FP) | false alarms % | 71.9 | 1.3 |
| test_wallet_help (FP) | false alarms % | 68.2 | 2.4 |
| test_wallet_help_synth (FP) | false alarms % | 69.6 | 1.3 |
| test_synth_clean (FP) | false alarms % | 52.9 | 15.4 |
| test_attacks_v2 (TPR) | detection % | 93.3 | 96.6 |
| test_unseen_styles | false alarms % | 75.0 | 16.7 |
| test_unseen_styles | detection % | 97.7 | 94.7 |
| test_contrast | false alarms % | 66.7 | 22.2 |
| test_contrast | detection % | 89.1 | 100.0 |
| v1 test_id | false alarms % | 1.4 | 0.9 |
| v1 test_id | detection % | 98.6 | 97.2 |
| v1 test_heldout | false alarms % | 7.8 | 1.4 |
| v1 test_heldout | detection % | 85.5 | 70.1 |
| v1 test_ood_crai | false alarms % | 4.4 | 4.2 |
| v1 test_ood_crai | detection % | 99.5 | 97.0 |

## Strongest injected cues, v1

`function`, `always`, `tool`, `use`, `redirect`, `transfer`, `to`, `to https`, `this`, `if`, `ignore`, `any`, `ignore the`, `use the`, `tools`, `directions`, `sign`, `and sign`, `to always`, `should`, `processing`, `to use`, `this page`, `signature`, `backup`, `function to`, `automated`, `call`, `always verify`, `transfer of`

Weights of instruction words (v1): `ignore` +3.30, `sign` +2.44, `transfer` +4.30, `approval` +1.55, `instructions` +1.60, `override` +0.69, `approve` +1.01, `confirm` -0.17, `send` +0.92, `assistant` +0.31, `ai` -0.11, `user` -3.68

## Strongest injected cues, v1+v2

`assistant`, `tool`, `transfer`, `agent`, `ai`, `redirect`, `function`, `always`, `any`, `ensure`, `note for`, `to`, `for`, `agents must`, `automated`, `to https`, `permit`, `this`, `use`, `verify`, `agents`, `automated agents`, `processing`, `sign the`, `data`, `bot`, `reading this`, `wallet`, `the user`, `after that`

Weights of instruction words (v1+v2): `ignore` +3.03, `sign` +2.67, `transfer` +8.86, `approval` +0.03, `instructions` +0.76, `override` +0.33, `approve` +1.57, `confirm` -0.55, `send` +2.72, `agent` +8.72, `assistant` +11.34, `ai` +8.59, `user` +4.41
