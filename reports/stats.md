# Dataset build statistics

## train
Segments: 15723; mean characters: 235.2

| Label | Source | Count |
|---:|---|---:|
| 0 | crypto_prose | 4073 |
| 0 | hard_negative | 6351 |
| 1 | synthetic_injection | 5299 |

### goal counts
- change_amount: 556
- drain_balance: 626
- escalate_permission: 8
- exfiltrate_private_data: 255
- exfiltrate_secret: 543
- extra_transfer: 379
- fake_user_approval: 546
- goal_hijack_generic: 380
- null: 10372
- out_of_scope_action: 502
- redirect_recipient: 469
- suppress_confirmation: 503
- unauthorized_typed_data_sign: 584

### style counts
- authority_impersonation: 702
- combined: 951
- escape_chars: 742
- fake_completion: 909
- ignore_previous: 537
- multi_sentence_split: 454
- naive: 415
- null: 10476
- polite_subtle: 537

### carrier counts
- html_comment: 911
- html_hidden: 776
- img_alt: 707
- markdown_table_cell: 1006
- null: 10476
- pdf_footer_header: 1051
- visible_body: 796

### position counts
- head: 1292
- middle: 2636
- null: 10476
- tail: 1319

### Joint label/source/goal/style/carrier/position counts
| Label | Source | Goal | Style | Carrier | Position | Count |
|---:|---|---|---|---|---|---:|
| 1 | synthetic_injection | change_amount | combined | html_comment | head | 10 |
| 1 | synthetic_injection | change_amount | combined | html_comment | middle | 26 |
| 1 | synthetic_injection | change_amount | combined | html_comment | tail | 8 |
| 1 | synthetic_injection | change_amount | combined | img_alt | head | 6 |
| 1 | synthetic_injection | change_amount | combined | img_alt | middle | 20 |
| 1 | synthetic_injection | change_amount | combined | img_alt | tail | 14 |
| 1 | synthetic_injection | change_amount | escape_chars | html_hidden | head | 18 |
| 1 | synthetic_injection | change_amount | escape_chars | html_hidden | middle | 42 |
| 1 | synthetic_injection | change_amount | escape_chars | html_hidden | tail | 14 |
| 1 | synthetic_injection | change_amount | escape_chars | pdf_footer_header | head | 32 |
| 1 | synthetic_injection | change_amount | escape_chars | pdf_footer_header | middle | 38 |
| 1 | synthetic_injection | change_amount | escape_chars | pdf_footer_header | tail | 24 |
| 1 | synthetic_injection | change_amount | fake_completion | img_alt | head | 4 |
| 1 | synthetic_injection | change_amount | fake_completion | img_alt | middle | 8 |
| 1 | synthetic_injection | change_amount | fake_completion | img_alt | tail | 6 |
| 1 | synthetic_injection | change_amount | fake_completion | markdown_table_cell | head | 7 |
| 1 | synthetic_injection | change_amount | fake_completion | markdown_table_cell | middle | 7 |
| 1 | synthetic_injection | change_amount | fake_completion | markdown_table_cell | tail | 7 |
| 1 | synthetic_injection | change_amount | fake_completion | pdf_footer_header | head | 5 |
| 1 | synthetic_injection | change_amount | fake_completion | pdf_footer_header | middle | 12 |
| 1 | synthetic_injection | change_amount | fake_completion | pdf_footer_header | tail | 4 |
| 1 | synthetic_injection | change_amount | fake_completion | visible_body | head | 5 |
| 1 | synthetic_injection | change_amount | fake_completion | visible_body | middle | 11 |
| 1 | synthetic_injection | change_amount | fake_completion | visible_body | tail | 8 |
| 1 | synthetic_injection | change_amount | ignore_previous | markdown_table_cell | head | 5 |
| 1 | synthetic_injection | change_amount | ignore_previous | markdown_table_cell | middle | 13 |
| 1 | synthetic_injection | change_amount | ignore_previous | markdown_table_cell | tail | 7 |
| 1 | synthetic_injection | change_amount | ignore_previous | visible_body | head | 5 |
| 1 | synthetic_injection | change_amount | ignore_previous | visible_body | middle | 9 |
| 1 | synthetic_injection | change_amount | ignore_previous | visible_body | tail | 3 |
| 1 | synthetic_injection | change_amount | multi_sentence_split | html_comment | head | 5 |
| 1 | synthetic_injection | change_amount | multi_sentence_split | html_comment | middle | 14 |
| 1 | synthetic_injection | change_amount | multi_sentence_split | pdf_footer_header | head | 4 |
| 1 | synthetic_injection | change_amount | multi_sentence_split | pdf_footer_header | middle | 13 |
| 1 | synthetic_injection | change_amount | multi_sentence_split | pdf_footer_header | tail | 6 |
| 1 | synthetic_injection | change_amount | naive | visible_body | head | 12 |
| 1 | synthetic_injection | change_amount | naive | visible_body | middle | 18 |
| 1 | synthetic_injection | change_amount | naive | visible_body | tail | 12 |
| 1 | synthetic_injection | change_amount | null | null | null | 5 |
| 1 | synthetic_injection | change_amount | polite_subtle | html_comment | head | 3 |
| 1 | synthetic_injection | change_amount | polite_subtle | html_comment | middle | 9 |
| 1 | synthetic_injection | change_amount | polite_subtle | html_comment | tail | 6 |
| 1 | synthetic_injection | change_amount | polite_subtle | html_hidden | head | 11 |
| 1 | synthetic_injection | change_amount | polite_subtle | html_hidden | middle | 22 |
| 1 | synthetic_injection | change_amount | polite_subtle | html_hidden | tail | 15 |
| 1 | synthetic_injection | change_amount | polite_subtle | markdown_table_cell | head | 3 |
| 1 | synthetic_injection | change_amount | polite_subtle | markdown_table_cell | middle | 11 |
| 1 | synthetic_injection | change_amount | polite_subtle | markdown_table_cell | tail | 4 |
| 1 | synthetic_injection | drain_balance | authority_impersonation | html_comment | head | 5 |
| 1 | synthetic_injection | drain_balance | authority_impersonation | html_comment | middle | 11 |
| 1 | synthetic_injection | drain_balance | authority_impersonation | html_comment | tail | 5 |
| 1 | synthetic_injection | drain_balance | authority_impersonation | markdown_table_cell | head | 6 |
| 1 | synthetic_injection | drain_balance | authority_impersonation | markdown_table_cell | middle | 13 |
| 1 | synthetic_injection | drain_balance | authority_impersonation | markdown_table_cell | tail | 5 |
| 1 | synthetic_injection | drain_balance | authority_impersonation | visible_body | head | 11 |
| 1 | synthetic_injection | drain_balance | authority_impersonation | visible_body | middle | 17 |
| 1 | synthetic_injection | drain_balance | authority_impersonation | visible_body | tail | 9 |
| 1 | synthetic_injection | drain_balance | combined | html_comment | head | 20 |
| 1 | synthetic_injection | drain_balance | combined | html_comment | middle | 40 |
| 1 | synthetic_injection | drain_balance | combined | html_comment | tail | 22 |
| 1 | synthetic_injection | drain_balance | combined | img_alt | head | 4 |
| 1 | synthetic_injection | drain_balance | combined | img_alt | middle | 28 |
| 1 | synthetic_injection | drain_balance | combined | img_alt | tail | 8 |
| 1 | synthetic_injection | drain_balance | combined | markdown_table_cell | head | 18 |
| 1 | synthetic_injection | drain_balance | combined | markdown_table_cell | middle | 16 |
| 1 | synthetic_injection | drain_balance | combined | markdown_table_cell | tail | 6 |
| 1 | synthetic_injection | drain_balance | combined | pdf_footer_header | head | 24 |
| 1 | synthetic_injection | drain_balance | combined | pdf_footer_header | middle | 46 |
| 1 | synthetic_injection | drain_balance | combined | pdf_footer_header | tail | 16 |
| 1 | synthetic_injection | drain_balance | escape_chars | html_hidden | head | 16 |
| 1 | synthetic_injection | drain_balance | escape_chars | html_hidden | middle | 20 |
| 1 | synthetic_injection | drain_balance | escape_chars | html_hidden | tail | 8 |
| 1 | synthetic_injection | drain_balance | escape_chars | img_alt | head | 10 |
| 1 | synthetic_injection | drain_balance | escape_chars | img_alt | middle | 18 |
| 1 | synthetic_injection | drain_balance | escape_chars | img_alt | tail | 10 |
| 1 | synthetic_injection | drain_balance | fake_completion | markdown_table_cell | head | 3 |
| 1 | synthetic_injection | drain_balance | fake_completion | markdown_table_cell | middle | 13 |
| 1 | synthetic_injection | drain_balance | fake_completion | markdown_table_cell | tail | 5 |
| 1 | synthetic_injection | drain_balance | fake_completion | pdf_footer_header | head | 6 |
| 1 | synthetic_injection | drain_balance | fake_completion | pdf_footer_header | middle | 19 |
| 1 | synthetic_injection | drain_balance | fake_completion | pdf_footer_header | tail | 12 |
| 1 | synthetic_injection | drain_balance | fake_completion | visible_body | head | 2 |
| 1 | synthetic_injection | drain_balance | fake_completion | visible_body | middle | 13 |
| 1 | synthetic_injection | drain_balance | fake_completion | visible_body | tail | 9 |
| 1 | synthetic_injection | drain_balance | multi_sentence_split | html_hidden | head | 7 |
| 1 | synthetic_injection | drain_balance | multi_sentence_split | html_hidden | middle | 17 |
| 1 | synthetic_injection | drain_balance | multi_sentence_split | html_hidden | tail | 3 |
| 1 | synthetic_injection | drain_balance | multi_sentence_split | visible_body | head | 4 |
| 1 | synthetic_injection | drain_balance | multi_sentence_split | visible_body | middle | 8 |
| 1 | synthetic_injection | drain_balance | multi_sentence_split | visible_body | tail | 2 |
| 1 | synthetic_injection | drain_balance | naive | html_comment | head | 4 |
| 1 | synthetic_injection | drain_balance | naive | html_comment | middle | 17 |
| 1 | synthetic_injection | drain_balance | naive | html_comment | tail | 2 |
| 1 | synthetic_injection | drain_balance | naive | html_hidden | head | 6 |
| 1 | synthetic_injection | drain_balance | naive | html_hidden | middle | 10 |
| 1 | synthetic_injection | drain_balance | naive | html_hidden | tail | 2 |
| 1 | synthetic_injection | drain_balance | naive | markdown_table_cell | head | 7 |
| 1 | synthetic_injection | drain_balance | naive | markdown_table_cell | middle | 7 |
| 1 | synthetic_injection | drain_balance | naive | markdown_table_cell | tail | 4 |
| 1 | synthetic_injection | drain_balance | naive | visible_body | head | 10 |
| 1 | synthetic_injection | drain_balance | naive | visible_body | middle | 11 |
| 1 | synthetic_injection | drain_balance | naive | visible_body | tail | 3 |
| 1 | synthetic_injection | drain_balance | null | null | null | 4 |
| 1 | synthetic_injection | escalate_permission | null | null | null | 4 |
| 1 | synthetic_injection | exfiltrate_private_data | authority_impersonation | img_alt | head | 8 |
| 1 | synthetic_injection | exfiltrate_private_data | authority_impersonation | img_alt | middle | 7 |
| 1 | synthetic_injection | exfiltrate_private_data | authority_impersonation | img_alt | tail | 7 |
| 1 | synthetic_injection | exfiltrate_private_data | authority_impersonation | visible_body | head | 6 |
| 1 | synthetic_injection | exfiltrate_private_data | authority_impersonation | visible_body | middle | 8 |
| 1 | synthetic_injection | exfiltrate_private_data | authority_impersonation | visible_body | tail | 5 |
| 1 | synthetic_injection | exfiltrate_private_data | fake_completion | markdown_table_cell | head | 6 |
| 1 | synthetic_injection | exfiltrate_private_data | fake_completion | markdown_table_cell | middle | 8 |
| 1 | synthetic_injection | exfiltrate_private_data | fake_completion | markdown_table_cell | tail | 7 |
| 1 | synthetic_injection | exfiltrate_private_data | fake_completion | pdf_footer_header | head | 2 |
| 1 | synthetic_injection | exfiltrate_private_data | fake_completion | pdf_footer_header | middle | 8 |
| 1 | synthetic_injection | exfiltrate_private_data | fake_completion | pdf_footer_header | tail | 10 |
| 1 | synthetic_injection | exfiltrate_private_data | ignore_previous | markdown_table_cell | head | 3 |
| 1 | synthetic_injection | exfiltrate_private_data | ignore_previous | markdown_table_cell | middle | 11 |
| 1 | synthetic_injection | exfiltrate_private_data | ignore_previous | markdown_table_cell | tail | 6 |
| 1 | synthetic_injection | exfiltrate_private_data | ignore_previous | visible_body | head | 6 |
| 1 | synthetic_injection | exfiltrate_private_data | ignore_previous | visible_body | middle | 12 |
| 1 | synthetic_injection | exfiltrate_private_data | ignore_previous | visible_body | tail | 3 |
| 1 | synthetic_injection | exfiltrate_private_data | multi_sentence_split | html_hidden | head | 3 |
| 1 | synthetic_injection | exfiltrate_private_data | multi_sentence_split | html_hidden | middle | 12 |
| 1 | synthetic_injection | exfiltrate_private_data | multi_sentence_split | html_hidden | tail | 10 |
| 1 | synthetic_injection | exfiltrate_private_data | multi_sentence_split | visible_body | middle | 12 |
| 1 | synthetic_injection | exfiltrate_private_data | multi_sentence_split | visible_body | tail | 4 |
| 1 | synthetic_injection | exfiltrate_private_data | naive | img_alt | head | 3 |
| 1 | synthetic_injection | exfiltrate_private_data | naive | img_alt | middle | 10 |
| 1 | synthetic_injection | exfiltrate_private_data | naive | img_alt | tail | 7 |
| 1 | synthetic_injection | exfiltrate_private_data | naive | visible_body | head | 6 |
| 1 | synthetic_injection | exfiltrate_private_data | naive | visible_body | middle | 13 |
| 1 | synthetic_injection | exfiltrate_private_data | naive | visible_body | tail | 3 |
| 1 | synthetic_injection | exfiltrate_private_data | null | null | null | 4 |
| 1 | synthetic_injection | exfiltrate_private_data | polite_subtle | html_comment | head | 9 |
| 1 | synthetic_injection | exfiltrate_private_data | polite_subtle | html_comment | middle | 9 |
| 1 | synthetic_injection | exfiltrate_private_data | polite_subtle | html_comment | tail | 4 |
| 1 | synthetic_injection | exfiltrate_private_data | polite_subtle | html_hidden | head | 5 |
| 1 | synthetic_injection | exfiltrate_private_data | polite_subtle | html_hidden | middle | 12 |
| 1 | synthetic_injection | exfiltrate_private_data | polite_subtle | html_hidden | tail | 2 |
| 1 | synthetic_injection | exfiltrate_secret | authority_impersonation | html_hidden | head | 6 |
| 1 | synthetic_injection | exfiltrate_secret | authority_impersonation | html_hidden | middle | 7 |
| 1 | synthetic_injection | exfiltrate_secret | authority_impersonation | html_hidden | tail | 4 |
| 1 | synthetic_injection | exfiltrate_secret | authority_impersonation | img_alt | head | 4 |
| 1 | synthetic_injection | exfiltrate_secret | authority_impersonation | img_alt | middle | 10 |
| 1 | synthetic_injection | exfiltrate_secret | authority_impersonation | img_alt | tail | 1 |
| 1 | synthetic_injection | exfiltrate_secret | authority_impersonation | markdown_table_cell | head | 10 |
| 1 | synthetic_injection | exfiltrate_secret | authority_impersonation | markdown_table_cell | middle | 11 |
| 1 | synthetic_injection | exfiltrate_secret | authority_impersonation | markdown_table_cell | tail | 5 |
| 1 | synthetic_injection | exfiltrate_secret | authority_impersonation | pdf_footer_header | head | 12 |
| 1 | synthetic_injection | exfiltrate_secret | authority_impersonation | pdf_footer_header | middle | 19 |
| 1 | synthetic_injection | exfiltrate_secret | authority_impersonation | pdf_footer_header | tail | 11 |
| 1 | synthetic_injection | exfiltrate_secret | authority_impersonation | visible_body | head | 5 |
| 1 | synthetic_injection | exfiltrate_secret | authority_impersonation | visible_body | middle | 10 |
| 1 | synthetic_injection | exfiltrate_secret | authority_impersonation | visible_body | tail | 9 |
| 1 | synthetic_injection | exfiltrate_secret | escape_chars | html_comment | head | 10 |
| 1 | synthetic_injection | exfiltrate_secret | escape_chars | html_comment | middle | 18 |
| 1 | synthetic_injection | exfiltrate_secret | escape_chars | html_comment | tail | 8 |
| 1 | synthetic_injection | exfiltrate_secret | escape_chars | img_alt | head | 4 |
| 1 | synthetic_injection | exfiltrate_secret | escape_chars | img_alt | middle | 20 |
| 1 | synthetic_injection | exfiltrate_secret | escape_chars | img_alt | tail | 6 |
| 1 | synthetic_injection | exfiltrate_secret | escape_chars | pdf_footer_header | head | 22 |
| 1 | synthetic_injection | exfiltrate_secret | escape_chars | pdf_footer_header | middle | 52 |
| 1 | synthetic_injection | exfiltrate_secret | escape_chars | pdf_footer_header | tail | 24 |
| 1 | synthetic_injection | exfiltrate_secret | fake_completion | html_hidden | head | 5 |
| 1 | synthetic_injection | exfiltrate_secret | fake_completion | html_hidden | middle | 14 |
| 1 | synthetic_injection | exfiltrate_secret | fake_completion | html_hidden | tail | 2 |
| 1 | synthetic_injection | exfiltrate_secret | fake_completion | markdown_table_cell | head | 9 |
| 1 | synthetic_injection | exfiltrate_secret | fake_completion | markdown_table_cell | middle | 28 |
| 1 | synthetic_injection | exfiltrate_secret | fake_completion | markdown_table_cell | tail | 7 |
| 1 | synthetic_injection | exfiltrate_secret | fake_completion | pdf_footer_header | head | 2 |
| 1 | synthetic_injection | exfiltrate_secret | fake_completion | pdf_footer_header | middle | 9 |
| 1 | synthetic_injection | exfiltrate_secret | fake_completion | pdf_footer_header | tail | 6 |
| 1 | synthetic_injection | exfiltrate_secret | ignore_previous | img_alt | head | 2 |
| 1 | synthetic_injection | exfiltrate_secret | ignore_previous | img_alt | middle | 12 |
| 1 | synthetic_injection | exfiltrate_secret | ignore_previous | img_alt | tail | 4 |
| 1 | synthetic_injection | exfiltrate_secret | ignore_previous | markdown_table_cell | head | 7 |
| 1 | synthetic_injection | exfiltrate_secret | ignore_previous | markdown_table_cell | middle | 13 |
| 1 | synthetic_injection | exfiltrate_secret | ignore_previous | markdown_table_cell | tail | 3 |
| 1 | synthetic_injection | exfiltrate_secret | multi_sentence_split | html_comment | head | 4 |
| 1 | synthetic_injection | exfiltrate_secret | multi_sentence_split | html_comment | middle | 13 |
| 1 | synthetic_injection | exfiltrate_secret | multi_sentence_split | html_comment | tail | 5 |
| 1 | synthetic_injection | exfiltrate_secret | multi_sentence_split | visible_body | head | 2 |
| 1 | synthetic_injection | exfiltrate_secret | multi_sentence_split | visible_body | middle | 11 |
| 1 | synthetic_injection | exfiltrate_secret | multi_sentence_split | visible_body | tail | 6 |
| 1 | synthetic_injection | exfiltrate_secret | naive | html_hidden | head | 7 |
| 1 | synthetic_injection | exfiltrate_secret | naive | html_hidden | middle | 8 |
| 1 | synthetic_injection | exfiltrate_secret | naive | html_hidden | tail | 5 |
| 1 | synthetic_injection | exfiltrate_secret | naive | visible_body | head | 6 |
| 1 | synthetic_injection | exfiltrate_secret | naive | visible_body | middle | 9 |
| 1 | synthetic_injection | exfiltrate_secret | naive | visible_body | tail | 7 |
| 1 | synthetic_injection | exfiltrate_secret | null | null | null | 4 |
| 1 | synthetic_injection | exfiltrate_secret | polite_subtle | html_comment | head | 5 |
| 1 | synthetic_injection | exfiltrate_secret | polite_subtle | html_comment | middle | 12 |
| 1 | synthetic_injection | exfiltrate_secret | polite_subtle | html_comment | tail | 5 |
| 1 | synthetic_injection | exfiltrate_secret | polite_subtle | html_hidden | head | 5 |
| 1 | synthetic_injection | exfiltrate_secret | polite_subtle | html_hidden | middle | 7 |
| 1 | synthetic_injection | exfiltrate_secret | polite_subtle | html_hidden | tail | 7 |
| 1 | synthetic_injection | extra_transfer | authority_impersonation | pdf_footer_header | head | 9 |
| 1 | synthetic_injection | extra_transfer | authority_impersonation | pdf_footer_header | middle | 11 |
| 1 | synthetic_injection | extra_transfer | authority_impersonation | pdf_footer_header | tail | 9 |
| 1 | synthetic_injection | extra_transfer | authority_impersonation | visible_body | head | 2 |
| 1 | synthetic_injection | extra_transfer | authority_impersonation | visible_body | middle | 7 |
| 1 | synthetic_injection | extra_transfer | authority_impersonation | visible_body | tail | 4 |
| 1 | synthetic_injection | extra_transfer | fake_completion | html_comment | head | 6 |
| 1 | synthetic_injection | extra_transfer | fake_completion | html_comment | middle | 14 |
| 1 | synthetic_injection | extra_transfer | fake_completion | html_comment | tail | 2 |
| 1 | synthetic_injection | extra_transfer | fake_completion | markdown_table_cell | head | 8 |
| 1 | synthetic_injection | extra_transfer | fake_completion | markdown_table_cell | middle | 23 |
| 1 | synthetic_injection | extra_transfer | fake_completion | markdown_table_cell | tail | 10 |
| 1 | synthetic_injection | extra_transfer | fake_completion | pdf_footer_header | head | 6 |
| 1 | synthetic_injection | extra_transfer | fake_completion | pdf_footer_header | middle | 7 |
| 1 | synthetic_injection | extra_transfer | fake_completion | pdf_footer_header | tail | 7 |
| 1 | synthetic_injection | extra_transfer | ignore_previous | img_alt | head | 13 |
| 1 | synthetic_injection | extra_transfer | ignore_previous | img_alt | middle | 23 |
| 1 | synthetic_injection | extra_transfer | ignore_previous | img_alt | tail | 7 |
| 1 | synthetic_injection | extra_transfer | ignore_previous | markdown_table_cell | head | 6 |
| 1 | synthetic_injection | extra_transfer | ignore_previous | markdown_table_cell | middle | 12 |
| 1 | synthetic_injection | extra_transfer | ignore_previous | markdown_table_cell | tail | 3 |
| 1 | synthetic_injection | extra_transfer | ignore_previous | pdf_footer_header | head | 5 |
| 1 | synthetic_injection | extra_transfer | ignore_previous | pdf_footer_header | middle | 10 |
| 1 | synthetic_injection | extra_transfer | ignore_previous | pdf_footer_header | tail | 3 |
| 1 | synthetic_injection | extra_transfer | naive | html_hidden | head | 7 |
| 1 | synthetic_injection | extra_transfer | naive | html_hidden | middle | 14 |
| 1 | synthetic_injection | extra_transfer | naive | html_hidden | tail | 5 |
| 1 | synthetic_injection | extra_transfer | naive | pdf_footer_header | head | 4 |
| 1 | synthetic_injection | extra_transfer | naive | pdf_footer_header | middle | 8 |
| 1 | synthetic_injection | extra_transfer | naive | pdf_footer_header | tail | 3 |
| 1 | synthetic_injection | extra_transfer | null | null | null | 4 |
| 1 | synthetic_injection | extra_transfer | polite_subtle | html_comment | head | 15 |
| 1 | synthetic_injection | extra_transfer | polite_subtle | html_comment | middle | 25 |
| 1 | synthetic_injection | extra_transfer | polite_subtle | html_comment | tail | 19 |
| 1 | synthetic_injection | extra_transfer | polite_subtle | markdown_table_cell | head | 4 |
| 1 | synthetic_injection | extra_transfer | polite_subtle | markdown_table_cell | middle | 9 |
| 1 | synthetic_injection | extra_transfer | polite_subtle | markdown_table_cell | tail | 10 |
| 1 | synthetic_injection | extra_transfer | polite_subtle | visible_body | head | 7 |
| 1 | synthetic_injection | extra_transfer | polite_subtle | visible_body | middle | 21 |
| 1 | synthetic_injection | extra_transfer | polite_subtle | visible_body | tail | 13 |
| 1 | synthetic_injection | fake_user_approval | authority_impersonation | html_comment | head | 6 |
| 1 | synthetic_injection | fake_user_approval | authority_impersonation | html_comment | middle | 8 |
| 1 | synthetic_injection | fake_user_approval | authority_impersonation | html_comment | tail | 3 |
| 1 | synthetic_injection | fake_user_approval | authority_impersonation | img_alt | head | 5 |
| 1 | synthetic_injection | fake_user_approval | authority_impersonation | img_alt | middle | 15 |
| 1 | synthetic_injection | fake_user_approval | authority_impersonation | img_alt | tail | 5 |
| 1 | synthetic_injection | fake_user_approval | authority_impersonation | markdown_table_cell | head | 4 |
| 1 | synthetic_injection | fake_user_approval | authority_impersonation | markdown_table_cell | middle | 7 |
| 1 | synthetic_injection | fake_user_approval | authority_impersonation | markdown_table_cell | tail | 5 |
| 1 | synthetic_injection | fake_user_approval | authority_impersonation | visible_body | head | 6 |
| 1 | synthetic_injection | fake_user_approval | authority_impersonation | visible_body | middle | 10 |
| 1 | synthetic_injection | fake_user_approval | authority_impersonation | visible_body | tail | 8 |
| 1 | synthetic_injection | fake_user_approval | combined | html_hidden | head | 16 |
| 1 | synthetic_injection | fake_user_approval | combined | html_hidden | middle | 46 |
| 1 | synthetic_injection | fake_user_approval | combined | html_hidden | tail | 22 |
| 1 | synthetic_injection | fake_user_approval | combined | img_alt | head | 16 |
| 1 | synthetic_injection | fake_user_approval | combined | img_alt | middle | 12 |
| 1 | synthetic_injection | fake_user_approval | combined | img_alt | tail | 12 |
| 1 | synthetic_injection | fake_user_approval | combined | pdf_footer_header | head | 6 |
| 1 | synthetic_injection | fake_user_approval | combined | pdf_footer_header | middle | 22 |
| 1 | synthetic_injection | fake_user_approval | combined | pdf_footer_header | tail | 14 |
| 1 | synthetic_injection | fake_user_approval | escape_chars | html_comment | head | 8 |
| 1 | synthetic_injection | fake_user_approval | escape_chars | html_comment | middle | 18 |
| 1 | synthetic_injection | fake_user_approval | escape_chars | html_comment | tail | 14 |
| 1 | synthetic_injection | fake_user_approval | escape_chars | markdown_table_cell | head | 4 |
| 1 | synthetic_injection | fake_user_approval | escape_chars | markdown_table_cell | middle | 16 |
| 1 | synthetic_injection | fake_user_approval | escape_chars | markdown_table_cell | tail | 22 |
| 1 | synthetic_injection | fake_user_approval | fake_completion | html_hidden | head | 5 |
| 1 | synthetic_injection | fake_user_approval | fake_completion | html_hidden | middle | 14 |
| 1 | synthetic_injection | fake_user_approval | fake_completion | html_hidden | tail | 2 |
| 1 | synthetic_injection | fake_user_approval | fake_completion | markdown_table_cell | head | 5 |
| 1 | synthetic_injection | fake_user_approval | fake_completion | markdown_table_cell | middle | 9 |
| 1 | synthetic_injection | fake_user_approval | fake_completion | markdown_table_cell | tail | 4 |
| 1 | synthetic_injection | fake_user_approval | fake_completion | pdf_footer_header | head | 6 |
| 1 | synthetic_injection | fake_user_approval | fake_completion | pdf_footer_header | middle | 28 |
| 1 | synthetic_injection | fake_user_approval | fake_completion | pdf_footer_header | tail | 9 |
| 1 | synthetic_injection | fake_user_approval | multi_sentence_split | html_comment | head | 6 |
| 1 | synthetic_injection | fake_user_approval | multi_sentence_split | html_comment | middle | 14 |
| 1 | synthetic_injection | fake_user_approval | multi_sentence_split | html_comment | tail | 4 |
| 1 | synthetic_injection | fake_user_approval | multi_sentence_split | html_hidden | head | 3 |
| 1 | synthetic_injection | fake_user_approval | multi_sentence_split | html_hidden | middle | 12 |
| 1 | synthetic_injection | fake_user_approval | multi_sentence_split | html_hidden | tail | 3 |
| 1 | synthetic_injection | fake_user_approval | multi_sentence_split | pdf_footer_header | head | 3 |
| 1 | synthetic_injection | fake_user_approval | multi_sentence_split | pdf_footer_header | middle | 8 |
| 1 | synthetic_injection | fake_user_approval | multi_sentence_split | pdf_footer_header | tail | 6 |
| 1 | synthetic_injection | fake_user_approval | multi_sentence_split | visible_body | head | 5 |
| 1 | synthetic_injection | fake_user_approval | multi_sentence_split | visible_body | middle | 10 |
| 1 | synthetic_injection | fake_user_approval | multi_sentence_split | visible_body | tail | 8 |
| 1 | synthetic_injection | fake_user_approval | naive | visible_body | head | 10 |
| 1 | synthetic_injection | fake_user_approval | naive | visible_body | middle | 19 |
| 1 | synthetic_injection | fake_user_approval | naive | visible_body | tail | 13 |
| 1 | synthetic_injection | fake_user_approval | null | null | null | 5 |
| 1 | synthetic_injection | goal_hijack_generic | authority_impersonation | markdown_table_cell | head | 8 |
| 1 | synthetic_injection | goal_hijack_generic | authority_impersonation | markdown_table_cell | middle | 6 |
| 1 | synthetic_injection | goal_hijack_generic | authority_impersonation | markdown_table_cell | tail | 4 |
| 1 | synthetic_injection | goal_hijack_generic | authority_impersonation | visible_body | head | 9 |
| 1 | synthetic_injection | goal_hijack_generic | authority_impersonation | visible_body | middle | 8 |
| 1 | synthetic_injection | goal_hijack_generic | authority_impersonation | visible_body | tail | 6 |
| 1 | synthetic_injection | goal_hijack_generic | combined | markdown_table_cell | head | 12 |
| 1 | synthetic_injection | goal_hijack_generic | combined | markdown_table_cell | middle | 20 |
| 1 | synthetic_injection | goal_hijack_generic | combined | markdown_table_cell | tail | 8 |
| 1 | synthetic_injection | goal_hijack_generic | combined | visible_body | head | 14 |
| 1 | synthetic_injection | goal_hijack_generic | combined | visible_body | middle | 18 |
| 1 | synthetic_injection | goal_hijack_generic | combined | visible_body | tail | 10 |
| 1 | synthetic_injection | goal_hijack_generic | fake_completion | html_hidden | head | 5 |
| 1 | synthetic_injection | goal_hijack_generic | fake_completion | html_hidden | middle | 8 |
| 1 | synthetic_injection | goal_hijack_generic | fake_completion | html_hidden | tail | 7 |
| 1 | synthetic_injection | goal_hijack_generic | fake_completion | markdown_table_cell | head | 1 |
| 1 | synthetic_injection | goal_hijack_generic | fake_completion | markdown_table_cell | middle | 14 |
| 1 | synthetic_injection | goal_hijack_generic | fake_completion | markdown_table_cell | tail | 6 |
| 1 | synthetic_injection | goal_hijack_generic | ignore_previous | html_comment | head | 12 |
| 1 | synthetic_injection | goal_hijack_generic | ignore_previous | html_comment | middle | 12 |
| 1 | synthetic_injection | goal_hijack_generic | ignore_previous | html_comment | tail | 17 |
| 1 | synthetic_injection | goal_hijack_generic | ignore_previous | markdown_table_cell | head | 5 |
| 1 | synthetic_injection | goal_hijack_generic | ignore_previous | markdown_table_cell | middle | 9 |
| 1 | synthetic_injection | goal_hijack_generic | ignore_previous | markdown_table_cell | tail | 5 |
| 1 | synthetic_injection | goal_hijack_generic | ignore_previous | pdf_footer_header | head | 6 |
| 1 | synthetic_injection | goal_hijack_generic | ignore_previous | pdf_footer_header | middle | 9 |
| 1 | synthetic_injection | goal_hijack_generic | ignore_previous | pdf_footer_header | tail | 4 |
| 1 | synthetic_injection | goal_hijack_generic | ignore_previous | visible_body | head | 12 |
| 1 | synthetic_injection | goal_hijack_generic | ignore_previous | visible_body | middle | 23 |
| 1 | synthetic_injection | goal_hijack_generic | ignore_previous | visible_body | tail | 10 |
| 1 | synthetic_injection | goal_hijack_generic | multi_sentence_split | pdf_footer_header | head | 2 |
| 1 | synthetic_injection | goal_hijack_generic | multi_sentence_split | pdf_footer_header | middle | 11 |
| 1 | synthetic_injection | goal_hijack_generic | multi_sentence_split | pdf_footer_header | tail | 6 |
| 1 | synthetic_injection | goal_hijack_generic | multi_sentence_split | visible_body | head | 5 |
| 1 | synthetic_injection | goal_hijack_generic | multi_sentence_split | visible_body | middle | 11 |
| 1 | synthetic_injection | goal_hijack_generic | multi_sentence_split | visible_body | tail | 6 |
| 1 | synthetic_injection | goal_hijack_generic | naive | html_comment | head | 4 |
| 1 | synthetic_injection | goal_hijack_generic | naive | html_comment | middle | 11 |
| 1 | synthetic_injection | goal_hijack_generic | naive | html_comment | tail | 3 |
| 1 | synthetic_injection | goal_hijack_generic | naive | markdown_table_cell | head | 5 |
| 1 | synthetic_injection | goal_hijack_generic | naive | markdown_table_cell | middle | 11 |
| 1 | synthetic_injection | goal_hijack_generic | naive | markdown_table_cell | tail | 7 |
| 1 | synthetic_injection | goal_hijack_generic | null | null | null | 5 |
| 1 | synthetic_injection | out_of_scope_action | authority_impersonation | html_hidden | head | 6 |
| 1 | synthetic_injection | out_of_scope_action | authority_impersonation | html_hidden | middle | 12 |
| 1 | synthetic_injection | out_of_scope_action | authority_impersonation | html_hidden | tail | 4 |
| 1 | synthetic_injection | out_of_scope_action | authority_impersonation | img_alt | head | 5 |
| 1 | synthetic_injection | out_of_scope_action | authority_impersonation | img_alt | middle | 10 |
| 1 | synthetic_injection | out_of_scope_action | authority_impersonation | img_alt | tail | 4 |
| 1 | synthetic_injection | out_of_scope_action | authority_impersonation | markdown_table_cell | head | 3 |
| 1 | synthetic_injection | out_of_scope_action | authority_impersonation | markdown_table_cell | middle | 10 |
| 1 | synthetic_injection | out_of_scope_action | authority_impersonation | markdown_table_cell | tail | 4 |
| 1 | synthetic_injection | out_of_scope_action | authority_impersonation | pdf_footer_header | head | 7 |
| 1 | synthetic_injection | out_of_scope_action | authority_impersonation | pdf_footer_header | middle | 9 |
| 1 | synthetic_injection | out_of_scope_action | authority_impersonation | pdf_footer_header | tail | 8 |
| 1 | synthetic_injection | out_of_scope_action | combined | pdf_footer_header | head | 16 |
| 1 | synthetic_injection | out_of_scope_action | combined | pdf_footer_header | middle | 20 |
| 1 | synthetic_injection | out_of_scope_action | combined | pdf_footer_header | tail | 12 |
| 1 | synthetic_injection | out_of_scope_action | combined | visible_body | head | 2 |
| 1 | synthetic_injection | out_of_scope_action | combined | visible_body | middle | 22 |
| 1 | synthetic_injection | out_of_scope_action | combined | visible_body | tail | 10 |
| 1 | synthetic_injection | out_of_scope_action | escape_chars | html_hidden | head | 8 |
| 1 | synthetic_injection | out_of_scope_action | escape_chars | html_hidden | middle | 20 |
| 1 | synthetic_injection | out_of_scope_action | escape_chars | html_hidden | tail | 8 |
| 1 | synthetic_injection | out_of_scope_action | escape_chars | markdown_table_cell | head | 14 |
| 1 | synthetic_injection | out_of_scope_action | escape_chars | markdown_table_cell | middle | 18 |
| 1 | synthetic_injection | out_of_scope_action | escape_chars | markdown_table_cell | tail | 14 |
| 1 | synthetic_injection | out_of_scope_action | fake_completion | html_hidden | head | 7 |
| 1 | synthetic_injection | out_of_scope_action | fake_completion | html_hidden | middle | 8 |
| 1 | synthetic_injection | out_of_scope_action | fake_completion | html_hidden | tail | 6 |
| 1 | synthetic_injection | out_of_scope_action | fake_completion | markdown_table_cell | head | 13 |
| 1 | synthetic_injection | out_of_scope_action | fake_completion | markdown_table_cell | middle | 24 |
| 1 | synthetic_injection | out_of_scope_action | fake_completion | markdown_table_cell | tail | 7 |
| 1 | synthetic_injection | out_of_scope_action | fake_completion | pdf_footer_header | head | 5 |
| 1 | synthetic_injection | out_of_scope_action | fake_completion | pdf_footer_header | middle | 10 |
| 1 | synthetic_injection | out_of_scope_action | fake_completion | pdf_footer_header | tail | 2 |
| 1 | synthetic_injection | out_of_scope_action | ignore_previous | img_alt | head | 3 |
| 1 | synthetic_injection | out_of_scope_action | ignore_previous | img_alt | middle | 6 |
| 1 | synthetic_injection | out_of_scope_action | ignore_previous | img_alt | tail | 8 |
| 1 | synthetic_injection | out_of_scope_action | ignore_previous | pdf_footer_header | head | 5 |
| 1 | synthetic_injection | out_of_scope_action | ignore_previous | pdf_footer_header | middle | 13 |
| 1 | synthetic_injection | out_of_scope_action | ignore_previous | pdf_footer_header | tail | 6 |
| 1 | synthetic_injection | out_of_scope_action | multi_sentence_split | html_comment | head | 7 |
| 1 | synthetic_injection | out_of_scope_action | multi_sentence_split | html_comment | middle | 7 |
| 1 | synthetic_injection | out_of_scope_action | multi_sentence_split | html_comment | tail | 5 |
| 1 | synthetic_injection | out_of_scope_action | multi_sentence_split | pdf_footer_header | head | 5 |
| 1 | synthetic_injection | out_of_scope_action | multi_sentence_split | pdf_footer_header | middle | 15 |
| 1 | synthetic_injection | out_of_scope_action | multi_sentence_split | pdf_footer_header | tail | 2 |
| 1 | synthetic_injection | out_of_scope_action | null | null | null | 5 |
| 1 | synthetic_injection | out_of_scope_action | polite_subtle | html_comment | head | 15 |
| 1 | synthetic_injection | out_of_scope_action | polite_subtle | html_comment | middle | 22 |
| 1 | synthetic_injection | out_of_scope_action | polite_subtle | html_comment | tail | 8 |
| 1 | synthetic_injection | out_of_scope_action | polite_subtle | img_alt | head | 4 |
| 1 | synthetic_injection | out_of_scope_action | polite_subtle | img_alt | middle | 6 |
| 1 | synthetic_injection | out_of_scope_action | polite_subtle | img_alt | tail | 6 |
| 1 | synthetic_injection | out_of_scope_action | polite_subtle | visible_body | head | 5 |
| 1 | synthetic_injection | out_of_scope_action | polite_subtle | visible_body | middle | 9 |
| 1 | synthetic_injection | out_of_scope_action | polite_subtle | visible_body | tail | 7 |
| 1 | synthetic_injection | redirect_recipient | authority_impersonation | pdf_footer_header | head | 5 |
| 1 | synthetic_injection | redirect_recipient | authority_impersonation | pdf_footer_header | middle | 13 |
| 1 | synthetic_injection | redirect_recipient | authority_impersonation | pdf_footer_header | tail | 3 |
| 1 | synthetic_injection | redirect_recipient | authority_impersonation | visible_body | head | 7 |
| 1 | synthetic_injection | redirect_recipient | authority_impersonation | visible_body | middle | 8 |
| 1 | synthetic_injection | redirect_recipient | authority_impersonation | visible_body | tail | 6 |
| 1 | synthetic_injection | redirect_recipient | combined | html_comment | head | 8 |
| 1 | synthetic_injection | redirect_recipient | combined | html_comment | middle | 20 |
| 1 | synthetic_injection | redirect_recipient | combined | html_comment | tail | 24 |
| 1 | synthetic_injection | redirect_recipient | combined | img_alt | head | 8 |
| 1 | synthetic_injection | redirect_recipient | combined | img_alt | middle | 16 |
| 1 | synthetic_injection | redirect_recipient | combined | img_alt | tail | 16 |
| 1 | synthetic_injection | redirect_recipient | combined | markdown_table_cell | head | 8 |
| 1 | synthetic_injection | redirect_recipient | combined | markdown_table_cell | middle | 16 |
| 1 | synthetic_injection | redirect_recipient | combined | markdown_table_cell | tail | 9 |
| 1 | synthetic_injection | redirect_recipient | fake_completion | html_comment | head | 4 |
| 1 | synthetic_injection | redirect_recipient | fake_completion | html_comment | middle | 11 |
| 1 | synthetic_injection | redirect_recipient | fake_completion | html_comment | tail | 7 |
| 1 | synthetic_injection | redirect_recipient | fake_completion | img_alt | head | 5 |
| 1 | synthetic_injection | redirect_recipient | fake_completion | img_alt | middle | 12 |
| 1 | synthetic_injection | redirect_recipient | fake_completion | img_alt | tail | 3 |
| 1 | synthetic_injection | redirect_recipient | fake_completion | markdown_table_cell | head | 10 |
| 1 | synthetic_injection | redirect_recipient | fake_completion | markdown_table_cell | middle | 8 |
| 1 | synthetic_injection | redirect_recipient | fake_completion | markdown_table_cell | tail | 3 |
| 1 | synthetic_injection | redirect_recipient | fake_completion | pdf_footer_header | head | 3 |
| 1 | synthetic_injection | redirect_recipient | fake_completion | pdf_footer_header | middle | 15 |
| 1 | synthetic_injection | redirect_recipient | fake_completion | pdf_footer_header | tail | 3 |
| 1 | synthetic_injection | redirect_recipient | ignore_previous | html_comment | head | 5 |
| 1 | synthetic_injection | redirect_recipient | ignore_previous | html_comment | middle | 19 |
| 1 | synthetic_injection | redirect_recipient | ignore_previous | html_comment | tail | 2 |
| 1 | synthetic_injection | redirect_recipient | ignore_previous | img_alt | head | 14 |
| 1 | synthetic_injection | redirect_recipient | ignore_previous | img_alt | middle | 12 |
| 1 | synthetic_injection | redirect_recipient | ignore_previous | img_alt | tail | 10 |
| 1 | synthetic_injection | redirect_recipient | ignore_previous | markdown_table_cell | head | 8 |
| 1 | synthetic_injection | redirect_recipient | ignore_previous | markdown_table_cell | middle | 5 |
| 1 | synthetic_injection | redirect_recipient | ignore_previous | markdown_table_cell | tail | 9 |
| 1 | synthetic_injection | redirect_recipient | multi_sentence_split | html_comment | head | 9 |
| 1 | synthetic_injection | redirect_recipient | multi_sentence_split | html_comment | middle | 5 |
| 1 | synthetic_injection | redirect_recipient | multi_sentence_split | html_comment | tail | 4 |
| 1 | synthetic_injection | redirect_recipient | multi_sentence_split | html_hidden | head | 3 |
| 1 | synthetic_injection | redirect_recipient | multi_sentence_split | html_hidden | middle | 14 |
| 1 | synthetic_injection | redirect_recipient | multi_sentence_split | html_hidden | tail | 1 |
| 1 | synthetic_injection | redirect_recipient | multi_sentence_split | markdown_table_cell | head | 13 |
| 1 | synthetic_injection | redirect_recipient | multi_sentence_split | markdown_table_cell | middle | 23 |
| 1 | synthetic_injection | redirect_recipient | multi_sentence_split | markdown_table_cell | tail | 12 |
| 1 | synthetic_injection | redirect_recipient | null | null | null | 4 |
| 1 | synthetic_injection | redirect_recipient | polite_subtle | html_comment | head | 3 |
| 1 | synthetic_injection | redirect_recipient | polite_subtle | html_comment | middle | 14 |
| 1 | synthetic_injection | redirect_recipient | polite_subtle | html_comment | tail | 4 |
| 1 | synthetic_injection | redirect_recipient | polite_subtle | pdf_footer_header | head | 8 |
| 1 | synthetic_injection | redirect_recipient | polite_subtle | pdf_footer_header | middle | 7 |
| 1 | synthetic_injection | redirect_recipient | polite_subtle | pdf_footer_header | tail | 6 |
| 1 | synthetic_injection | suppress_confirmation | authority_impersonation | html_comment | head | 4 |
| 1 | synthetic_injection | suppress_confirmation | authority_impersonation | html_comment | middle | 11 |
| 1 | synthetic_injection | suppress_confirmation | authority_impersonation | html_comment | tail | 2 |
| 1 | synthetic_injection | suppress_confirmation | authority_impersonation | pdf_footer_header | head | 12 |
| 1 | synthetic_injection | suppress_confirmation | authority_impersonation | pdf_footer_header | middle | 22 |
| 1 | synthetic_injection | suppress_confirmation | authority_impersonation | pdf_footer_header | tail | 11 |
| 1 | synthetic_injection | suppress_confirmation | authority_impersonation | visible_body | head | 2 |
| 1 | synthetic_injection | suppress_confirmation | authority_impersonation | visible_body | middle | 12 |
| 1 | synthetic_injection | suppress_confirmation | authority_impersonation | visible_body | tail | 7 |
| 1 | synthetic_injection | suppress_confirmation | combined | img_alt | head | 12 |
| 1 | synthetic_injection | suppress_confirmation | combined | img_alt | middle | 22 |
| 1 | synthetic_injection | suppress_confirmation | combined | img_alt | tail | 6 |
| 1 | synthetic_injection | suppress_confirmation | combined | pdf_footer_header | head | 10 |
| 1 | synthetic_injection | suppress_confirmation | combined | pdf_footer_header | middle | 28 |
| 1 | synthetic_injection | suppress_confirmation | combined | pdf_footer_header | tail | 4 |
| 1 | synthetic_injection | suppress_confirmation | fake_completion | html_comment | head | 20 |
| 1 | synthetic_injection | suppress_confirmation | fake_completion | html_comment | middle | 34 |
| 1 | synthetic_injection | suppress_confirmation | fake_completion | html_comment | tail | 30 |
| 1 | synthetic_injection | suppress_confirmation | fake_completion | html_hidden | head | 8 |
| 1 | synthetic_injection | suppress_confirmation | fake_completion | html_hidden | middle | 10 |
| 1 | synthetic_injection | suppress_confirmation | fake_completion | html_hidden | tail | 4 |
| 1 | synthetic_injection | suppress_confirmation | fake_completion | img_alt | head | 5 |
| 1 | synthetic_injection | suppress_confirmation | fake_completion | img_alt | middle | 12 |
| 1 | synthetic_injection | suppress_confirmation | fake_completion | img_alt | tail | 4 |
| 1 | synthetic_injection | suppress_confirmation | fake_completion | markdown_table_cell | head | 10 |
| 1 | synthetic_injection | suppress_confirmation | fake_completion | markdown_table_cell | middle | 20 |
| 1 | synthetic_injection | suppress_confirmation | fake_completion | markdown_table_cell | tail | 9 |
| 1 | synthetic_injection | suppress_confirmation | ignore_previous | html_comment | head | 6 |
| 1 | synthetic_injection | suppress_confirmation | ignore_previous | html_comment | middle | 8 |
| 1 | synthetic_injection | suppress_confirmation | ignore_previous | html_comment | tail | 5 |
| 1 | synthetic_injection | suppress_confirmation | ignore_previous | pdf_footer_header | head | 3 |
| 1 | synthetic_injection | suppress_confirmation | ignore_previous | pdf_footer_header | middle | 14 |
| 1 | synthetic_injection | suppress_confirmation | ignore_previous | pdf_footer_header | tail | 5 |
| 1 | synthetic_injection | suppress_confirmation | multi_sentence_split | img_alt | head | 8 |
| 1 | synthetic_injection | suppress_confirmation | multi_sentence_split | img_alt | middle | 9 |
| 1 | synthetic_injection | suppress_confirmation | multi_sentence_split | img_alt | tail | 7 |
| 1 | synthetic_injection | suppress_confirmation | multi_sentence_split | visible_body | head | 2 |
| 1 | synthetic_injection | suppress_confirmation | multi_sentence_split | visible_body | middle | 8 |
| 1 | synthetic_injection | suppress_confirmation | multi_sentence_split | visible_body | tail | 7 |
| 1 | synthetic_injection | suppress_confirmation | naive | html_hidden | head | 4 |
| 1 | synthetic_injection | suppress_confirmation | naive | html_hidden | middle | 9 |
| 1 | synthetic_injection | suppress_confirmation | naive | html_hidden | tail | 6 |
| 1 | synthetic_injection | suppress_confirmation | naive | img_alt | head | 9 |
| 1 | synthetic_injection | suppress_confirmation | naive | img_alt | middle | 7 |
| 1 | synthetic_injection | suppress_confirmation | naive | img_alt | tail | 6 |
| 1 | synthetic_injection | suppress_confirmation | null | null | null | 4 |
| 1 | synthetic_injection | suppress_confirmation | polite_subtle | html_hidden | head | 7 |
| 1 | synthetic_injection | suppress_confirmation | polite_subtle | html_hidden | middle | 8 |
| 1 | synthetic_injection | suppress_confirmation | polite_subtle | html_hidden | tail | 4 |
| 1 | synthetic_injection | suppress_confirmation | polite_subtle | markdown_table_cell | head | 5 |
| 1 | synthetic_injection | suppress_confirmation | polite_subtle | markdown_table_cell | middle | 10 |
| 1 | synthetic_injection | suppress_confirmation | polite_subtle | markdown_table_cell | tail | 7 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | authority_impersonation | img_alt | head | 6 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | authority_impersonation | img_alt | middle | 12 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | authority_impersonation | img_alt | tail | 4 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | authority_impersonation | markdown_table_cell | head | 3 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | authority_impersonation | markdown_table_cell | middle | 12 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | authority_impersonation | markdown_table_cell | tail | 11 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | authority_impersonation | visible_body | head | 10 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | authority_impersonation | visible_body | middle | 20 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | authority_impersonation | visible_body | tail | 5 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | combined | html_comment | head | 8 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | combined | html_comment | middle | 24 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | combined | html_comment | tail | 4 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | combined | pdf_footer_header | head | 8 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | combined | pdf_footer_header | middle | 38 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | escape_chars | html_hidden | head | 12 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | escape_chars | html_hidden | middle | 42 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | escape_chars | html_hidden | tail | 22 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | escape_chars | img_alt | head | 8 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | escape_chars | img_alt | middle | 18 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | escape_chars | img_alt | tail | 18 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | escape_chars | markdown_table_cell | head | 4 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | escape_chars | markdown_table_cell | middle | 22 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | escape_chars | markdown_table_cell | tail | 18 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | fake_completion | html_comment | head | 7 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | fake_completion | html_comment | middle | 11 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | fake_completion | html_comment | tail | 4 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | fake_completion | markdown_table_cell | head | 3 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | fake_completion | markdown_table_cell | middle | 15 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | fake_completion | markdown_table_cell | tail | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | fake_completion | pdf_footer_header | head | 3 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | fake_completion | pdf_footer_header | middle | 10 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | fake_completion | pdf_footer_header | tail | 3 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | fake_completion | visible_body | head | 7 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | fake_completion | visible_body | middle | 13 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | fake_completion | visible_body | tail | 5 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | ignore_previous | html_hidden | head | 5 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | ignore_previous | html_hidden | middle | 8 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | ignore_previous | html_hidden | tail | 6 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | ignore_previous | pdf_footer_header | head | 6 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | ignore_previous | pdf_footer_header | middle | 7 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | ignore_previous | pdf_footer_header | tail | 9 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | naive | img_alt | head | 8 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | naive | img_alt | middle | 8 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | naive | img_alt | tail | 3 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | naive | visible_body | head | 6 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | naive | visible_body | middle | 11 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | naive | visible_body | tail | 5 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | null | null | null | 4 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | polite_subtle | html_hidden | head | 7 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | polite_subtle | html_hidden | middle | 12 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | polite_subtle | html_hidden | tail | 4 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | polite_subtle | img_alt | head | 5 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | polite_subtle | img_alt | middle | 5 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | polite_subtle | img_alt | tail | 8 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | polite_subtle | markdown_table_cell | head | 10 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | polite_subtle | markdown_table_cell | middle | 20 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | polite_subtle | markdown_table_cell | tail | 12 |
| null | crypto_prose | null | null | null | null | 4073 |
| null | hard_negative | change_amount | null | null | null | 5 |
| null | hard_negative | drain_balance | null | null | null | 4 |
| null | hard_negative | escalate_permission | null | null | null | 4 |
| null | hard_negative | exfiltrate_private_data | null | null | null | 4 |
| null | hard_negative | exfiltrate_secret | null | null | null | 4 |
| null | hard_negative | extra_transfer | null | null | null | 4 |
| null | hard_negative | fake_user_approval | null | null | null | 5 |
| null | hard_negative | goal_hijack_generic | null | null | null | 5 |
| null | hard_negative | null | null | null | null | 6299 |
| null | hard_negative | out_of_scope_action | null | null | null | 5 |
| null | hard_negative | redirect_recipient | null | null | null | 4 |
| null | hard_negative | suppress_confirmation | null | null | null | 4 |
| null | hard_negative | unauthorized_typed_data_sign | null | null | null | 4 |

Whitespace token-length histogram: {"0-16": 1396, "129+": 0, "17-32": 9641, "33-64": 2876, "65-128": 1810}

## val
Segments: 1623; mean characters: 216.2

| Label | Source | Count |
|---:|---|---:|
| 0 | crypto_prose | 370 |
| 0 | hard_negative | 723 |
| 1 | synthetic_injection | 530 |

### goal counts
- drain_balance: 116
- exfiltrate_private_data: 116
- exfiltrate_secret: 2
- extra_transfer: 2
- null: 1088
- out_of_scope_action: 59
- redirect_recipient: 120
- suppress_confirmation: 118
- unauthorized_typed_data_sign: 2

### style counts
- authority_impersonation: 58
- combined: 116
- escape_chars: 116
- fake_completion: 118
- naive: 59
- null: 1098
- polite_subtle: 58

### carrier counts
- html_comment: 167
- html_hidden: 27
- img_alt: 35
- markdown_table_cell: 44
- null: 1098
- pdf_footer_header: 135
- visible_body: 117

### position counts
- head: 135
- middle: 260
- null: 1098
- tail: 130

### Joint label/source/goal/style/carrier/position counts
| Label | Source | Goal | Style | Carrier | Position | Count |
|---:|---|---|---|---|---|---:|
| 1 | synthetic_injection | drain_balance | authority_impersonation | img_alt | head | 9 |
| 1 | synthetic_injection | drain_balance | authority_impersonation | img_alt | middle | 17 |
| 1 | synthetic_injection | drain_balance | authority_impersonation | img_alt | tail | 9 |
| 1 | synthetic_injection | drain_balance | authority_impersonation | pdf_footer_header | head | 7 |
| 1 | synthetic_injection | drain_balance | authority_impersonation | pdf_footer_header | middle | 7 |
| 1 | synthetic_injection | drain_balance | authority_impersonation | pdf_footer_header | tail | 9 |
| 1 | synthetic_injection | drain_balance | polite_subtle | html_comment | head | 6 |
| 1 | synthetic_injection | drain_balance | polite_subtle | html_comment | middle | 14 |
| 1 | synthetic_injection | drain_balance | polite_subtle | html_comment | tail | 11 |
| 1 | synthetic_injection | drain_balance | polite_subtle | html_hidden | head | 12 |
| 1 | synthetic_injection | drain_balance | polite_subtle | html_hidden | middle | 11 |
| 1 | synthetic_injection | drain_balance | polite_subtle | html_hidden | tail | 4 |
| 1 | synthetic_injection | exfiltrate_private_data | combined | pdf_footer_header | head | 14 |
| 1 | synthetic_injection | exfiltrate_private_data | combined | pdf_footer_header | middle | 38 |
| 1 | synthetic_injection | exfiltrate_private_data | combined | pdf_footer_header | tail | 6 |
| 1 | synthetic_injection | exfiltrate_private_data | combined | visible_body | head | 18 |
| 1 | synthetic_injection | exfiltrate_private_data | combined | visible_body | middle | 26 |
| 1 | synthetic_injection | exfiltrate_private_data | combined | visible_body | tail | 14 |
| 1 | synthetic_injection | exfiltrate_secret | null | null | null | 1 |
| 1 | synthetic_injection | extra_transfer | null | null | null | 1 |
| 1 | synthetic_injection | out_of_scope_action | naive | visible_body | head | 9 |
| 1 | synthetic_injection | out_of_scope_action | naive | visible_body | middle | 33 |
| 1 | synthetic_injection | out_of_scope_action | naive | visible_body | tail | 17 |
| 1 | synthetic_injection | redirect_recipient | fake_completion | html_comment | head | 22 |
| 1 | synthetic_injection | redirect_recipient | fake_completion | html_comment | middle | 36 |
| 1 | synthetic_injection | redirect_recipient | fake_completion | html_comment | tail | 16 |
| 1 | synthetic_injection | redirect_recipient | fake_completion | markdown_table_cell | head | 14 |
| 1 | synthetic_injection | redirect_recipient | fake_completion | markdown_table_cell | middle | 16 |
| 1 | synthetic_injection | redirect_recipient | fake_completion | markdown_table_cell | tail | 14 |
| 1 | synthetic_injection | redirect_recipient | null | null | null | 1 |
| 1 | synthetic_injection | suppress_confirmation | escape_chars | html_comment | head | 14 |
| 1 | synthetic_injection | suppress_confirmation | escape_chars | html_comment | middle | 32 |
| 1 | synthetic_injection | suppress_confirmation | escape_chars | html_comment | tail | 16 |
| 1 | synthetic_injection | suppress_confirmation | escape_chars | pdf_footer_header | head | 10 |
| 1 | synthetic_injection | suppress_confirmation | escape_chars | pdf_footer_header | middle | 30 |
| 1 | synthetic_injection | suppress_confirmation | escape_chars | pdf_footer_header | tail | 14 |
| 1 | synthetic_injection | suppress_confirmation | null | null | null | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | null | null | null | 1 |
| null | crypto_prose | null | null | null | null | 370 |
| null | hard_negative | exfiltrate_secret | null | null | null | 1 |
| null | hard_negative | extra_transfer | null | null | null | 1 |
| null | hard_negative | null | null | null | null | 718 |
| null | hard_negative | redirect_recipient | null | null | null | 1 |
| null | hard_negative | suppress_confirmation | null | null | null | 1 |
| null | hard_negative | unauthorized_typed_data_sign | null | null | null | 1 |

Whitespace token-length histogram: {"0-16": 10, "129+": 0, "17-32": 1116, "33-64": 380, "65-128": 117}

## test_id
Segments: 1420; mean characters: 235.4

| Label | Source | Count |
|---:|---|---:|
| 0 | crypto_prose | 356 |
| 0 | hard_negative | 536 |
| 1 | synthetic_injection | 528 |

### goal counts
- change_amount: 25
- drain_balance: 2
- escalate_permission: 2
- exfiltrate_private_data: 52
- exfiltrate_secret: 50
- extra_transfer: 50
- fake_user_approval: 50
- goal_hijack_generic: 75
- null: 889
- out_of_scope_action: 125
- redirect_recipient: 25
- suppress_confirmation: 50
- unauthorized_typed_data_sign: 25

### style counts
- authority_impersonation: 50
- combined: 150
- escape_chars: 150
- fake_completion: 25
- ignore_previous: 50
- multi_sentence_split: 50
- null: 895
- polite_subtle: 50

### carrier counts
- html_comment: 80
- html_hidden: 52
- img_alt: 201
- markdown_table_cell: 66
- null: 895
- pdf_footer_header: 126

### position counts
- head: 134
- middle: 260
- null: 895
- tail: 131

### Joint label/source/goal/style/carrier/position counts
| Label | Source | Goal | Style | Carrier | Position | Count |
|---:|---|---|---|---|---|---:|
| 1 | synthetic_injection | change_amount | multi_sentence_split | html_hidden | head | 2 |
| 1 | synthetic_injection | change_amount | multi_sentence_split | html_hidden | middle | 9 |
| 1 | synthetic_injection | change_amount | multi_sentence_split | html_hidden | tail | 4 |
| 1 | synthetic_injection | change_amount | multi_sentence_split | pdf_footer_header | head | 4 |
| 1 | synthetic_injection | change_amount | multi_sentence_split | pdf_footer_header | middle | 5 |
| 1 | synthetic_injection | change_amount | multi_sentence_split | pdf_footer_header | tail | 1 |
| 1 | synthetic_injection | drain_balance | null | null | null | 1 |
| 1 | synthetic_injection | escalate_permission | null | null | null | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | authority_impersonation | markdown_table_cell | head | 5 |
| 1 | synthetic_injection | exfiltrate_private_data | authority_impersonation | markdown_table_cell | middle | 5 |
| 1 | synthetic_injection | exfiltrate_private_data | authority_impersonation | markdown_table_cell | tail | 2 |
| 1 | synthetic_injection | exfiltrate_private_data | authority_impersonation | pdf_footer_header | head | 4 |
| 1 | synthetic_injection | exfiltrate_private_data | authority_impersonation | pdf_footer_header | middle | 7 |
| 1 | synthetic_injection | exfiltrate_private_data | authority_impersonation | pdf_footer_header | tail | 2 |
| 1 | synthetic_injection | exfiltrate_private_data | multi_sentence_split | html_hidden | head | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | multi_sentence_split | html_hidden | middle | 6 |
| 1 | synthetic_injection | exfiltrate_private_data | multi_sentence_split | html_hidden | tail | 7 |
| 1 | synthetic_injection | exfiltrate_private_data | multi_sentence_split | img_alt | head | 3 |
| 1 | synthetic_injection | exfiltrate_private_data | multi_sentence_split | img_alt | middle | 3 |
| 1 | synthetic_injection | exfiltrate_private_data | multi_sentence_split | img_alt | tail | 5 |
| 1 | synthetic_injection | exfiltrate_private_data | null | null | null | 1 |
| 1 | synthetic_injection | exfiltrate_secret | combined | img_alt | head | 8 |
| 1 | synthetic_injection | exfiltrate_secret | combined | img_alt | middle | 10 |
| 1 | synthetic_injection | exfiltrate_secret | combined | img_alt | tail | 10 |
| 1 | synthetic_injection | exfiltrate_secret | combined | pdf_footer_header | head | 8 |
| 1 | synthetic_injection | exfiltrate_secret | combined | pdf_footer_header | middle | 12 |
| 1 | synthetic_injection | exfiltrate_secret | combined | pdf_footer_header | tail | 2 |
| 1 | synthetic_injection | extra_transfer | escape_chars | img_alt | middle | 26 |
| 1 | synthetic_injection | extra_transfer | escape_chars | img_alt | tail | 6 |
| 1 | synthetic_injection | extra_transfer | escape_chars | markdown_table_cell | head | 2 |
| 1 | synthetic_injection | extra_transfer | escape_chars | markdown_table_cell | middle | 6 |
| 1 | synthetic_injection | extra_transfer | escape_chars | markdown_table_cell | tail | 10 |
| 1 | synthetic_injection | fake_user_approval | ignore_previous | img_alt | head | 3 |
| 1 | synthetic_injection | fake_user_approval | ignore_previous | img_alt | middle | 4 |
| 1 | synthetic_injection | fake_user_approval | ignore_previous | img_alt | tail | 1 |
| 1 | synthetic_injection | fake_user_approval | ignore_previous | markdown_table_cell | head | 5 |
| 1 | synthetic_injection | fake_user_approval | ignore_previous | markdown_table_cell | middle | 8 |
| 1 | synthetic_injection | fake_user_approval | ignore_previous | markdown_table_cell | tail | 4 |
| 1 | synthetic_injection | fake_user_approval | polite_subtle | html_comment | head | 2 |
| 1 | synthetic_injection | fake_user_approval | polite_subtle | html_comment | middle | 9 |
| 1 | synthetic_injection | fake_user_approval | polite_subtle | html_comment | tail | 3 |
| 1 | synthetic_injection | fake_user_approval | polite_subtle | html_hidden | head | 1 |
| 1 | synthetic_injection | fake_user_approval | polite_subtle | html_hidden | middle | 4 |
| 1 | synthetic_injection | fake_user_approval | polite_subtle | html_hidden | tail | 6 |
| 1 | synthetic_injection | goal_hijack_generic | combined | img_alt | head | 6 |
| 1 | synthetic_injection | goal_hijack_generic | combined | img_alt | middle | 12 |
| 1 | synthetic_injection | goal_hijack_generic | combined | pdf_footer_header | head | 6 |
| 1 | synthetic_injection | goal_hijack_generic | combined | pdf_footer_header | middle | 16 |
| 1 | synthetic_injection | goal_hijack_generic | combined | pdf_footer_header | tail | 10 |
| 1 | synthetic_injection | goal_hijack_generic | polite_subtle | html_comment | head | 5 |
| 1 | synthetic_injection | goal_hijack_generic | polite_subtle | html_comment | middle | 7 |
| 1 | synthetic_injection | goal_hijack_generic | polite_subtle | html_comment | tail | 2 |
| 1 | synthetic_injection | goal_hijack_generic | polite_subtle | img_alt | head | 3 |
| 1 | synthetic_injection | goal_hijack_generic | polite_subtle | img_alt | middle | 7 |
| 1 | synthetic_injection | goal_hijack_generic | polite_subtle | img_alt | tail | 1 |
| 1 | synthetic_injection | out_of_scope_action | combined | img_alt | head | 4 |
| 1 | synthetic_injection | out_of_scope_action | combined | img_alt | middle | 8 |
| 1 | synthetic_injection | out_of_scope_action | combined | img_alt | tail | 6 |
| 1 | synthetic_injection | out_of_scope_action | combined | pdf_footer_header | head | 12 |
| 1 | synthetic_injection | out_of_scope_action | combined | pdf_footer_header | middle | 14 |
| 1 | synthetic_injection | out_of_scope_action | combined | pdf_footer_header | tail | 6 |
| 1 | synthetic_injection | out_of_scope_action | escape_chars | html_comment | head | 10 |
| 1 | synthetic_injection | out_of_scope_action | escape_chars | html_comment | middle | 12 |
| 1 | synthetic_injection | out_of_scope_action | escape_chars | html_comment | tail | 4 |
| 1 | synthetic_injection | out_of_scope_action | escape_chars | img_alt | head | 6 |
| 1 | synthetic_injection | out_of_scope_action | escape_chars | img_alt | middle | 14 |
| 1 | synthetic_injection | out_of_scope_action | escape_chars | img_alt | tail | 4 |
| 1 | synthetic_injection | out_of_scope_action | fake_completion | markdown_table_cell | head | 1 |
| 1 | synthetic_injection | out_of_scope_action | fake_completion | markdown_table_cell | middle | 4 |
| 1 | synthetic_injection | out_of_scope_action | fake_completion | markdown_table_cell | tail | 3 |
| 1 | synthetic_injection | out_of_scope_action | fake_completion | pdf_footer_header | head | 2 |
| 1 | synthetic_injection | out_of_scope_action | fake_completion | pdf_footer_header | middle | 10 |
| 1 | synthetic_injection | out_of_scope_action | fake_completion | pdf_footer_header | tail | 5 |
| 1 | synthetic_injection | redirect_recipient | ignore_previous | img_alt | head | 5 |
| 1 | synthetic_injection | redirect_recipient | ignore_previous | img_alt | middle | 7 |
| 1 | synthetic_injection | redirect_recipient | ignore_previous | img_alt | tail | 2 |
| 1 | synthetic_injection | redirect_recipient | ignore_previous | markdown_table_cell | head | 3 |
| 1 | synthetic_injection | redirect_recipient | ignore_previous | markdown_table_cell | middle | 4 |
| 1 | synthetic_injection | redirect_recipient | ignore_previous | markdown_table_cell | tail | 4 |
| 1 | synthetic_injection | suppress_confirmation | escape_chars | html_comment | head | 8 |
| 1 | synthetic_injection | suppress_confirmation | escape_chars | html_comment | middle | 10 |
| 1 | synthetic_injection | suppress_confirmation | escape_chars | html_comment | tail | 8 |
| 1 | synthetic_injection | suppress_confirmation | escape_chars | img_alt | head | 8 |
| 1 | synthetic_injection | suppress_confirmation | escape_chars | img_alt | middle | 8 |
| 1 | synthetic_injection | suppress_confirmation | escape_chars | img_alt | tail | 8 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | authority_impersonation | html_hidden | head | 3 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | authority_impersonation | html_hidden | middle | 4 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | authority_impersonation | html_hidden | tail | 5 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | authority_impersonation | img_alt | head | 4 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | authority_impersonation | img_alt | middle | 9 |
| null | crypto_prose | null | null | null | null | 356 |
| null | hard_negative | drain_balance | null | null | null | 1 |
| null | hard_negative | escalate_permission | null | null | null | 1 |
| null | hard_negative | exfiltrate_private_data | null | null | null | 1 |
| null | hard_negative | null | null | null | null | 533 |

Whitespace token-length histogram: {"0-16": 278, "129+": 0, "17-32": 746, "33-64": 246, "65-128": 150}

## test_heldout
Segments: 1094; mean characters: 225.6

| Label | Source | Count |
|---:|---|---:|
| 0 | crypto_prose | 253 |
| 0 | hard_negative | 491 |
| 1 | synthetic_injection | 350 |

### goal counts
- change_amount: 32
- drain_balance: 28
- escalate_permission: 32
- exfiltrate_private_data: 38
- exfiltrate_secret: 30
- extra_transfer: 36
- fake_user_approval: 25
- goal_hijack_generic: 19
- null: 744
- out_of_scope_action: 14
- redirect_recipient: 38
- suppress_confirmation: 28
- unauthorized_typed_data_sign: 30

### style counts
- authority_impersonation: 16
- combined: 50
- escape_chars: 58
- fake_completion: 10
- ignore_previous: 25
- multi_sentence_split: 30
- naive: 32
- null: 744
- obfuscated: 53
- polite_subtle: 23
- role_play: 53

### carrier counts
- email_quote: 143
- html_comment: 6
- html_hidden: 14
- img_alt: 10
- json_tool_response: 144
- markdown_table_cell: 11
- null: 744
- pdf_footer_header: 10
- visible_body: 12

### position counts
- head: 77
- middle: 199
- null: 744
- tail: 74

### Joint label/source/goal/style/carrier/position counts
| Label | Source | Goal | Style | Carrier | Position | Count |
|---:|---|---|---|---|---|---:|
| 1 | synthetic_injection | change_amount | combined | email_quote | middle | 4 |
| 1 | synthetic_injection | change_amount | escape_chars | json_tool_response | head | 2 |
| 1 | synthetic_injection | change_amount | escape_chars | json_tool_response | tail | 2 |
| 1 | synthetic_injection | change_amount | ignore_previous | email_quote | head | 1 |
| 1 | synthetic_injection | change_amount | ignore_previous | email_quote | middle | 1 |
| 1 | synthetic_injection | change_amount | multi_sentence_split | email_quote | middle | 2 |
| 1 | synthetic_injection | change_amount | naive | email_quote | middle | 1 |
| 1 | synthetic_injection | change_amount | naive | email_quote | tail | 1 |
| 1 | synthetic_injection | change_amount | obfuscated | email_quote | middle | 2 |
| 1 | synthetic_injection | change_amount | obfuscated | email_quote | tail | 1 |
| 1 | synthetic_injection | change_amount | obfuscated | img_alt | middle | 1 |
| 1 | synthetic_injection | change_amount | obfuscated | img_alt | tail | 1 |
| 1 | synthetic_injection | change_amount | obfuscated | json_tool_response | head | 1 |
| 1 | synthetic_injection | change_amount | obfuscated | json_tool_response | middle | 1 |
| 1 | synthetic_injection | change_amount | obfuscated | json_tool_response | tail | 1 |
| 1 | synthetic_injection | change_amount | polite_subtle | email_quote | middle | 2 |
| 1 | synthetic_injection | change_amount | role_play | json_tool_response | head | 1 |
| 1 | synthetic_injection | change_amount | role_play | json_tool_response | middle | 3 |
| 1 | synthetic_injection | change_amount | role_play | json_tool_response | tail | 2 |
| 1 | synthetic_injection | change_amount | role_play | visible_body | head | 1 |
| 1 | synthetic_injection | change_amount | role_play | visible_body | tail | 1 |
| 1 | synthetic_injection | drain_balance | combined | email_quote | tail | 4 |
| 1 | synthetic_injection | drain_balance | escape_chars | json_tool_response | middle | 2 |
| 1 | synthetic_injection | drain_balance | escape_chars | json_tool_response | tail | 2 |
| 1 | synthetic_injection | drain_balance | ignore_previous | email_quote | middle | 1 |
| 1 | synthetic_injection | drain_balance | ignore_previous | email_quote | tail | 1 |
| 1 | synthetic_injection | drain_balance | ignore_previous | json_tool_response | head | 1 |
| 1 | synthetic_injection | drain_balance | ignore_previous | json_tool_response | tail | 1 |
| 1 | synthetic_injection | drain_balance | multi_sentence_split | email_quote | head | 1 |
| 1 | synthetic_injection | drain_balance | multi_sentence_split | email_quote | tail | 1 |
| 1 | synthetic_injection | drain_balance | naive | json_tool_response | middle | 2 |
| 1 | synthetic_injection | drain_balance | obfuscated | email_quote | head | 1 |
| 1 | synthetic_injection | drain_balance | obfuscated | email_quote | tail | 1 |
| 1 | synthetic_injection | drain_balance | obfuscated | html_hidden | middle | 1 |
| 1 | synthetic_injection | drain_balance | obfuscated | visible_body | tail | 1 |
| 1 | synthetic_injection | drain_balance | polite_subtle | json_tool_response | tail | 2 |
| 1 | synthetic_injection | drain_balance | role_play | email_quote | head | 2 |
| 1 | synthetic_injection | drain_balance | role_play | json_tool_response | middle | 4 |
| 1 | synthetic_injection | escalate_permission | authority_impersonation | html_comment | tail | 1 |
| 1 | synthetic_injection | escalate_permission | authority_impersonation | img_alt | tail | 1 |
| 1 | synthetic_injection | escalate_permission | authority_impersonation | markdown_table_cell | middle | 1 |
| 1 | synthetic_injection | escalate_permission | authority_impersonation | visible_body | head | 2 |
| 1 | synthetic_injection | escalate_permission | combined | email_quote | middle | 2 |
| 1 | synthetic_injection | escalate_permission | combined | html_hidden | middle | 2 |
| 1 | synthetic_injection | escalate_permission | escape_chars | img_alt | tail | 2 |
| 1 | synthetic_injection | escalate_permission | escape_chars | json_tool_response | middle | 2 |
| 1 | synthetic_injection | escalate_permission | fake_completion | email_quote | middle | 1 |
| 1 | synthetic_injection | escalate_permission | fake_completion | markdown_table_cell | middle | 1 |
| 1 | synthetic_injection | escalate_permission | ignore_previous | json_tool_response | tail | 1 |
| 1 | synthetic_injection | escalate_permission | ignore_previous | visible_body | middle | 1 |
| 1 | synthetic_injection | escalate_permission | multi_sentence_split | email_quote | middle | 3 |
| 1 | synthetic_injection | escalate_permission | multi_sentence_split | html_comment | middle | 1 |
| 1 | synthetic_injection | escalate_permission | naive | email_quote | head | 1 |
| 1 | synthetic_injection | escalate_permission | naive | email_quote | middle | 1 |
| 1 | synthetic_injection | escalate_permission | obfuscated | img_alt | head | 1 |
| 1 | synthetic_injection | escalate_permission | obfuscated | img_alt | middle | 1 |
| 1 | synthetic_injection | escalate_permission | polite_subtle | html_hidden | middle | 1 |
| 1 | synthetic_injection | escalate_permission | polite_subtle | img_alt | head | 1 |
| 1 | synthetic_injection | escalate_permission | polite_subtle | json_tool_response | middle | 1 |
| 1 | synthetic_injection | escalate_permission | polite_subtle | markdown_table_cell | head | 2 |
| 1 | synthetic_injection | escalate_permission | role_play | json_tool_response | middle | 1 |
| 1 | synthetic_injection | escalate_permission | role_play | json_tool_response | tail | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | authority_impersonation | json_tool_response | middle | 2 |
| 1 | synthetic_injection | exfiltrate_private_data | combined | email_quote | head | 2 |
| 1 | synthetic_injection | exfiltrate_private_data | combined | email_quote | middle | 2 |
| 1 | synthetic_injection | exfiltrate_private_data | escape_chars | email_quote | middle | 4 |
| 1 | synthetic_injection | exfiltrate_private_data | escape_chars | json_tool_response | head | 2 |
| 1 | synthetic_injection | exfiltrate_private_data | escape_chars | json_tool_response | middle | 2 |
| 1 | synthetic_injection | exfiltrate_private_data | fake_completion | json_tool_response | middle | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | fake_completion | json_tool_response | tail | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | ignore_previous | email_quote | middle | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | ignore_previous | email_quote | tail | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | multi_sentence_split | email_quote | head | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | multi_sentence_split | email_quote | middle | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | naive | email_quote | head | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | naive | email_quote | middle | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | naive | json_tool_response | head | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | naive | json_tool_response | middle | 3 |
| 1 | synthetic_injection | exfiltrate_private_data | obfuscated | html_hidden | middle | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | obfuscated | json_tool_response | middle | 2 |
| 1 | synthetic_injection | exfiltrate_private_data | obfuscated | visible_body | middle | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | polite_subtle | email_quote | head | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | polite_subtle | email_quote | middle | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | polite_subtle | json_tool_response | middle | 2 |
| 1 | synthetic_injection | exfiltrate_private_data | role_play | email_quote | middle | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | role_play | email_quote | tail | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | role_play | html_hidden | middle | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | role_play | markdown_table_cell | middle | 1 |
| 1 | synthetic_injection | exfiltrate_secret | combined | email_quote | middle | 2 |
| 1 | synthetic_injection | exfiltrate_secret | combined | json_tool_response | head | 2 |
| 1 | synthetic_injection | exfiltrate_secret | escape_chars | json_tool_response | middle | 4 |
| 1 | synthetic_injection | exfiltrate_secret | fake_completion | email_quote | middle | 1 |
| 1 | synthetic_injection | exfiltrate_secret | fake_completion | email_quote | tail | 1 |
| 1 | synthetic_injection | exfiltrate_secret | ignore_previous | json_tool_response | middle | 3 |
| 1 | synthetic_injection | exfiltrate_secret | ignore_previous | json_tool_response | tail | 1 |
| 1 | synthetic_injection | exfiltrate_secret | multi_sentence_split | email_quote | head | 1 |
| 1 | synthetic_injection | exfiltrate_secret | multi_sentence_split | email_quote | middle | 1 |
| 1 | synthetic_injection | exfiltrate_secret | naive | json_tool_response | head | 2 |
| 1 | synthetic_injection | exfiltrate_secret | naive | json_tool_response | middle | 1 |
| 1 | synthetic_injection | exfiltrate_secret | naive | json_tool_response | tail | 1 |
| 1 | synthetic_injection | exfiltrate_secret | obfuscated | email_quote | tail | 2 |
| 1 | synthetic_injection | exfiltrate_secret | obfuscated | html_hidden | head | 1 |
| 1 | synthetic_injection | exfiltrate_secret | obfuscated | html_hidden | middle | 1 |
| 1 | synthetic_injection | exfiltrate_secret | polite_subtle | json_tool_response | middle | 1 |
| 1 | synthetic_injection | exfiltrate_secret | polite_subtle | json_tool_response | tail | 1 |
| 1 | synthetic_injection | exfiltrate_secret | role_play | email_quote | head | 1 |
| 1 | synthetic_injection | exfiltrate_secret | role_play | email_quote | middle | 1 |
| 1 | synthetic_injection | exfiltrate_secret | role_play | markdown_table_cell | middle | 1 |
| 1 | synthetic_injection | exfiltrate_secret | role_play | pdf_footer_header | middle | 1 |
| 1 | synthetic_injection | extra_transfer | authority_impersonation | email_quote | middle | 1 |
| 1 | synthetic_injection | extra_transfer | authority_impersonation | email_quote | tail | 1 |
| 1 | synthetic_injection | extra_transfer | combined | email_quote | middle | 2 |
| 1 | synthetic_injection | extra_transfer | combined | email_quote | tail | 2 |
| 1 | synthetic_injection | extra_transfer | combined | json_tool_response | head | 2 |
| 1 | synthetic_injection | extra_transfer | combined | json_tool_response | middle | 2 |
| 1 | synthetic_injection | extra_transfer | escape_chars | email_quote | head | 2 |
| 1 | synthetic_injection | extra_transfer | escape_chars | email_quote | tail | 2 |
| 1 | synthetic_injection | extra_transfer | fake_completion | json_tool_response | head | 1 |
| 1 | synthetic_injection | extra_transfer | fake_completion | json_tool_response | middle | 1 |
| 1 | synthetic_injection | extra_transfer | multi_sentence_split | email_quote | head | 1 |
| 1 | synthetic_injection | extra_transfer | multi_sentence_split | email_quote | middle | 3 |
| 1 | synthetic_injection | extra_transfer | multi_sentence_split | email_quote | tail | 1 |
| 1 | synthetic_injection | extra_transfer | multi_sentence_split | json_tool_response | middle | 2 |
| 1 | synthetic_injection | extra_transfer | multi_sentence_split | json_tool_response | tail | 1 |
| 1 | synthetic_injection | extra_transfer | naive | json_tool_response | head | 2 |
| 1 | synthetic_injection | extra_transfer | naive | json_tool_response | middle | 1 |
| 1 | synthetic_injection | extra_transfer | naive | json_tool_response | tail | 1 |
| 1 | synthetic_injection | extra_transfer | obfuscated | html_comment | head | 1 |
| 1 | synthetic_injection | extra_transfer | obfuscated | html_hidden | head | 1 |
| 1 | synthetic_injection | extra_transfer | obfuscated | pdf_footer_header | middle | 1 |
| 1 | synthetic_injection | extra_transfer | obfuscated | visible_body | middle | 1 |
| 1 | synthetic_injection | extra_transfer | role_play | email_quote | head | 1 |
| 1 | synthetic_injection | extra_transfer | role_play | email_quote | middle | 1 |
| 1 | synthetic_injection | extra_transfer | role_play | img_alt | middle | 1 |
| 1 | synthetic_injection | extra_transfer | role_play | markdown_table_cell | tail | 1 |
| 1 | synthetic_injection | fake_user_approval | authority_impersonation | email_quote | middle | 1 |
| 1 | synthetic_injection | fake_user_approval | authority_impersonation | email_quote | tail | 1 |
| 1 | synthetic_injection | fake_user_approval | combined | email_quote | head | 2 |
| 1 | synthetic_injection | fake_user_approval | combined | email_quote | middle | 2 |
| 1 | synthetic_injection | fake_user_approval | escape_chars | json_tool_response | middle | 2 |
| 1 | synthetic_injection | fake_user_approval | escape_chars | json_tool_response | tail | 2 |
| 1 | synthetic_injection | fake_user_approval | ignore_previous | json_tool_response | middle | 1 |
| 1 | synthetic_injection | fake_user_approval | multi_sentence_split | email_quote | middle | 2 |
| 1 | synthetic_injection | fake_user_approval | naive | email_quote | head | 1 |
| 1 | synthetic_injection | fake_user_approval | naive | json_tool_response | middle | 1 |
| 1 | synthetic_injection | fake_user_approval | naive | json_tool_response | tail | 1 |
| 1 | synthetic_injection | fake_user_approval | obfuscated | html_hidden | middle | 2 |
| 1 | synthetic_injection | fake_user_approval | obfuscated | img_alt | middle | 1 |
| 1 | synthetic_injection | fake_user_approval | obfuscated | pdf_footer_header | head | 1 |
| 1 | synthetic_injection | fake_user_approval | obfuscated | visible_body | middle | 1 |
| 1 | synthetic_injection | fake_user_approval | polite_subtle | json_tool_response | head | 1 |
| 1 | synthetic_injection | fake_user_approval | role_play | email_quote | head | 1 |
| 1 | synthetic_injection | fake_user_approval | role_play | email_quote | middle | 2 |
| 1 | synthetic_injection | goal_hijack_generic | authority_impersonation | json_tool_response | middle | 1 |
| 1 | synthetic_injection | goal_hijack_generic | escape_chars | email_quote | tail | 2 |
| 1 | synthetic_injection | goal_hijack_generic | escape_chars | json_tool_response | tail | 2 |
| 1 | synthetic_injection | goal_hijack_generic | fake_completion | json_tool_response | head | 1 |
| 1 | synthetic_injection | goal_hijack_generic | fake_completion | json_tool_response | middle | 1 |
| 1 | synthetic_injection | goal_hijack_generic | ignore_previous | json_tool_response | middle | 1 |
| 1 | synthetic_injection | goal_hijack_generic | multi_sentence_split | email_quote | middle | 1 |
| 1 | synthetic_injection | goal_hijack_generic | naive | json_tool_response | middle | 1 |
| 1 | synthetic_injection | goal_hijack_generic | obfuscated | html_hidden | middle | 1 |
| 1 | synthetic_injection | goal_hijack_generic | obfuscated | json_tool_response | head | 1 |
| 1 | synthetic_injection | goal_hijack_generic | obfuscated | json_tool_response | middle | 1 |
| 1 | synthetic_injection | goal_hijack_generic | obfuscated | markdown_table_cell | middle | 1 |
| 1 | synthetic_injection | goal_hijack_generic | polite_subtle | json_tool_response | head | 1 |
| 1 | synthetic_injection | goal_hijack_generic | role_play | email_quote | head | 2 |
| 1 | synthetic_injection | goal_hijack_generic | role_play | email_quote | middle | 1 |
| 1 | synthetic_injection | goal_hijack_generic | role_play | email_quote | tail | 1 |
| 1 | synthetic_injection | out_of_scope_action | combined | json_tool_response | middle | 2 |
| 1 | synthetic_injection | out_of_scope_action | escape_chars | email_quote | middle | 2 |
| 1 | synthetic_injection | out_of_scope_action | escape_chars | json_tool_response | middle | 1 |
| 1 | synthetic_injection | out_of_scope_action | escape_chars | json_tool_response | tail | 1 |
| 1 | synthetic_injection | out_of_scope_action | ignore_previous | json_tool_response | tail | 1 |
| 1 | synthetic_injection | out_of_scope_action | multi_sentence_split | email_quote | middle | 1 |
| 1 | synthetic_injection | out_of_scope_action | naive | json_tool_response | middle | 2 |
| 1 | synthetic_injection | out_of_scope_action | obfuscated | visible_body | head | 1 |
| 1 | synthetic_injection | out_of_scope_action | obfuscated | visible_body | middle | 1 |
| 1 | synthetic_injection | out_of_scope_action | role_play | email_quote | middle | 2 |
| 1 | synthetic_injection | redirect_recipient | combined | email_quote | head | 2 |
| 1 | synthetic_injection | redirect_recipient | combined | email_quote | middle | 6 |
| 1 | synthetic_injection | redirect_recipient | escape_chars | json_tool_response | head | 4 |
| 1 | synthetic_injection | redirect_recipient | escape_chars | json_tool_response | middle | 8 |
| 1 | synthetic_injection | redirect_recipient | escape_chars | json_tool_response | tail | 2 |
| 1 | synthetic_injection | redirect_recipient | ignore_previous | email_quote | middle | 3 |
| 1 | synthetic_injection | redirect_recipient | ignore_previous | email_quote | tail | 1 |
| 1 | synthetic_injection | redirect_recipient | obfuscated | email_quote | middle | 2 |
| 1 | synthetic_injection | redirect_recipient | obfuscated | html_comment | middle | 2 |
| 1 | synthetic_injection | redirect_recipient | obfuscated | pdf_footer_header | middle | 2 |
| 1 | synthetic_injection | redirect_recipient | polite_subtle | email_quote | head | 2 |
| 1 | synthetic_injection | redirect_recipient | role_play | pdf_footer_header | head | 1 |
| 1 | synthetic_injection | redirect_recipient | role_play | pdf_footer_header | middle | 1 |
| 1 | synthetic_injection | redirect_recipient | role_play | pdf_footer_header | tail | 2 |
| 1 | synthetic_injection | suppress_confirmation | authority_impersonation | json_tool_response | head | 1 |
| 1 | synthetic_injection | suppress_confirmation | authority_impersonation | json_tool_response | middle | 1 |
| 1 | synthetic_injection | suppress_confirmation | combined | email_quote | middle | 4 |
| 1 | synthetic_injection | suppress_confirmation | ignore_previous | json_tool_response | middle | 2 |
| 1 | synthetic_injection | suppress_confirmation | multi_sentence_split | email_quote | head | 1 |
| 1 | synthetic_injection | suppress_confirmation | multi_sentence_split | json_tool_response | middle | 1 |
| 1 | synthetic_injection | suppress_confirmation | naive | json_tool_response | middle | 3 |
| 1 | synthetic_injection | suppress_confirmation | naive | json_tool_response | tail | 1 |
| 1 | synthetic_injection | suppress_confirmation | obfuscated | email_quote | middle | 1 |
| 1 | synthetic_injection | suppress_confirmation | obfuscated | email_quote | tail | 1 |
| 1 | synthetic_injection | suppress_confirmation | obfuscated | html_hidden | head | 1 |
| 1 | synthetic_injection | suppress_confirmation | obfuscated | html_hidden | middle | 1 |
| 1 | synthetic_injection | suppress_confirmation | polite_subtle | email_quote | middle | 2 |
| 1 | synthetic_injection | suppress_confirmation | role_play | email_quote | middle | 2 |
| 1 | synthetic_injection | suppress_confirmation | role_play | html_comment | middle | 1 |
| 1 | synthetic_injection | suppress_confirmation | role_play | json_tool_response | head | 1 |
| 1 | synthetic_injection | suppress_confirmation | role_play | json_tool_response | middle | 3 |
| 1 | synthetic_injection | suppress_confirmation | role_play | markdown_table_cell | head | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | authority_impersonation | email_quote | head | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | authority_impersonation | email_quote | middle | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | combined | email_quote | middle | 4 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | escape_chars | json_tool_response | middle | 2 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | escape_chars | json_tool_response | tail | 2 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | ignore_previous | json_tool_response | head | 2 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | multi_sentence_split | email_quote | middle | 2 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | multi_sentence_split | email_quote | tail | 2 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | naive | json_tool_response | head | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | naive | json_tool_response | tail | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | obfuscated | json_tool_response | head | 2 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | obfuscated | json_tool_response | tail | 2 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | obfuscated | pdf_footer_header | tail | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | obfuscated | visible_body | middle | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | polite_subtle | json_tool_response | head | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | polite_subtle | json_tool_response | middle | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | role_play | email_quote | middle | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | role_play | email_quote | tail | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | role_play | markdown_table_cell | middle | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | role_play | markdown_table_cell | tail | 1 |
| null | crypto_prose | null | null | null | null | 253 |
| null | hard_negative | null | null | null | null | 491 |

Whitespace token-length histogram: {"0-16": 89, "129+": 1, "17-32": 690, "33-64": 246, "65-128": 68}

## test_ood_crai
Segments: 6156; mean characters: 173.0

| Label | Source | Count |
|---:|---|---:|
| 0 | crai | 2924 |
| 1 | crai | 3232 |

### goal counts
- null: 6156

### style counts
- null: 6156

### carrier counts
- null: 6156

### position counts
- null: 6156

### Joint label/source/goal/style/carrier/position counts
| Label | Source | Goal | Style | Carrier | Position | Count |
|---:|---|---|---|---|---|---:|
| 1 | crai | null | null | null | null | 3232 |
| null | crai | null | null | null | null | 2924 |

Whitespace token-length histogram: {"0-16": 2230, "129+": 0, "17-32": 1929, "33-64": 1988, "65-128": 9}

## redteam_manual
Segments: 0; mean characters: 0.0

| Label | Source | Count |
|---:|---|---:|

### goal counts

### style counts

### carrier counts

### position counts

### Joint label/source/goal/style/carrier/position counts
| Label | Source | Goal | Style | Carrier | Position | Count |
|---:|---|---|---|---|---|---:|

Whitespace token-length histogram: {"0-16": 0, "129+": 0, "17-32": 0, "33-64": 0, "65-128": 0}
