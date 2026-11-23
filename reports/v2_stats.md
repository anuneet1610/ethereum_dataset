# v2 data build statistics

| File | Rows | Injected | Clean | Injected % |
|---|---:|---:|---:|---:|
| data/v2/dev.jsonl | 2194 | 522 | 1672 | 23.8 |
| data/v2/test_attacks_v2.jsonl | 522 | 522 | 0 | 100.0 |
| data/v2/test_contrast.jsonl | 127 | 55 | 72 | 43.3 |
| data/v2/test_docs.jsonl | 826 | 0 | 826 | 0.0 |
| data/v2/test_synth_clean.jsonl | 312 | 0 | 312 | 0.0 |
| data/v2/test_unseen_styles.jsonl | 145 | 133 | 12 | 91.7 |
| data/v2/test_wallet_help.jsonl | 708 | 0 | 708 | 0.0 |
| data/v2/test_wallet_help_synth.jsonl | 79 | 0 | 79 | 0.0 |
| data/v2/train.jsonl | 10485 | 2573 | 7912 | 24.5 |

## train: rows by source / eval subset and label

| Source | Subset | Label | Rows |
|---|---|---:|---:|
| v2_agent_grammar | - | 0 | 350 |
| v2_ai_mentions | - | 0 | 39 |
| v2_attack | - | 1 | 1939 |
| v2_contrast_twin | - | 1 | 214 |
| v2_email | - | 0 | 151 |
| v2_prose | - | 0 | 5055 |
| v2_prose_swap | - | 1 | 420 |
| v2_trigger_grammar | - | 0 | 495 |
| v2_trigger_words | - | 0 | 54 |
| v2_trigger_words_2 | - | 0 | 30 |
| v2_user_command | - | 0 | 380 |
| v2_wallet_help | - | 0 | 877 |
| v2_web_clutter | - | 0 | 61 |
| v2_web_clutter_real | - | 0 | 420 |

## dev: rows by source / eval subset and label

| Source | Subset | Label | Rows |
|---|---|---:|---:|
| v2_agent_grammar | dev_synth_clean | 0 | 36 |
| v2_ai_mentions | dev_contrast | 0 | 13 |
| v2_ai_mentions | dev_synth_clean | 0 | 4 |
| v2_attack | dev_attacks | 1 | 384 |
| v2_contrast_twin | dev_contrast | 1 | 48 |
| v2_email | dev_synth_clean | 0 | 16 |
| v2_prose | dev_prose | 0 | 1033 |
| v2_prose_swap | dev_contrast | 1 | 90 |
| v2_trigger_grammar | dev_synth_clean | 0 | 224 |
| v2_trigger_words | dev_contrast | 0 | 8 |
| v2_trigger_words | dev_synth_clean | 0 | 4 |
| v2_trigger_words_2 | dev_synth_clean | 0 | 8 |
| v2_user_command | dev_contrast | 0 | 8 |
| v2_user_command | dev_synth_clean | 0 | 51 |
| v2_wallet_help | dev_contrast | 0 | 30 |
| v2_wallet_help | dev_synth_clean | 0 | 153 |
| v2_web_clutter | dev_synth_clean | 0 | 13 |
| v2_web_clutter_real | dev_synth_clean | 0 | 71 |

## Attack families (all splits)

| Family | Split | Rows |
|---|---|---:|
| agent_directed_general | dev | 72 |
| agent_directed_general | test | 127 |
| agent_directed_general | train | 527 |
| authority_impersonation | dev | 70 |
| authority_impersonation | test | 56 |
| authority_impersonation | train | 276 |
| change_amount_agent | dev | 52 |
| change_amount_agent | test | 40 |
| change_amount_agent | train | 123 |
| contrast_aim | dev | 10 |
| contrast_aim | train | 9 |
| contrast_cmd | dev | 5 |
| contrast_cmd | test | 4 |
| contrast_cmd | train | 48 |
| contrast_email | train | 26 |
| contrast_help | dev | 29 |
| contrast_help | test | 45 |
| contrast_help | train | 106 |
| contrast_trig | dev | 4 |
| contrast_trig | test | 6 |
| contrast_trig | train | 25 |
| fake_completion | dev | 53 |
| fake_completion | test | 78 |
| fake_completion | train | 230 |
| fake_memory | dev | 57 |
| fake_memory | test | 122 |
| fake_memory | train | 300 |
| implicit_harm | dev | 37 |
| implicit_harm | test | 78 |
| implicit_harm | train | 173 |
| multi_sentence_split | test | 8 |
| multi_sentence_split | train | 85 |
| prose_swap | dev | 90 |
| prose_swap | train | 420 |
| quoted_email | test | 65 |
| role_play | test | 68 |
| short_agent_line | dev | 43 |
| short_agent_line | test | 13 |
| short_agent_line | train | 225 |

## Real prose sources

| Repo | Split | Rows |
|---|---|---:|
| astral-sh/uv | train | 422 |
| encode/httpx | train | 412 |
| ethereum/ethereum-org-website | test | 708 |
| fastapi/fastapi | train | 482 |
| github/docs | train | 624 |
| jestjs/jest | train | 499 |
| kubernetes/website | test | 404 |
| mdn/content | test | 422 |
| microsoft/vscode-docs | dev | 420 |
| prettier/prettier | train | 441 |
| pydantic/pydantic | train | 414 |
| python-poetry/poetry | train | 435 |
| rust-lang/book | train | 435 |
| squidfunk/mkdocs-material | train | 491 |
| vitejs/vite | dev | 321 |
| wevm/viem | train | 400 |
| wevm/wagmi | dev | 292 |

## Removed during dedup

- dev_in_train: 13
- train_escalation_held_out: 264
- dev_escalation_held_out: 45

## Near-duplicate templates merged into one split (2)

- cmd-003 ~ cmd-070
- cmp-agent_directed_general-08 ~ cmp-implicit_harm-05

## v1 rows to drop from training (lead-in sentences labelled injected)

- train: 4
  - `Wallet Security settlement notice: the supplier wallet has been rotated.`
  - `Q: Are the payment details final?`
  - `A: Yes.`
  - `User: Has the payment been approved?`
- val: 0
- test_id: 2
  - `An archived message asserts that consent was granted.`
  - `The transcript says permission was recorded earlier.`
- test_heldout: 48
  - `From: operations@example.test`
  - `Subject: revised handling`
  - `The status field reports success.`
  - `[END OF DOCUMENT]`
  - `Review status is marked complete.`
  - `### SYSTEM`
