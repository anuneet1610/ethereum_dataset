# Dataset build statistics

## train
Segments: 2496; mean characters: 111.6

| Label | Source | Count |
|---:|---|---:|
| 0 | crypto_prose | 62 |
| 0 | hard_negative | 1186 |
| 1 | synthetic_injection | 1248 |

### goal counts
- change_amount: 68
- drain_balance: 79
- escalate_permission: 2
- exfiltrate_private_data: 143
- exfiltrate_secret: 210
- extra_transfer: 124
- fake_user_approval: 157
- goal_hijack_generic: 132
- null: 1244
- out_of_scope_action: 51
- redirect_recipient: 41
- suppress_confirmation: 31
- unauthorized_typed_data_sign: 214

### style counts
- authority_impersonation: 67
- combined: 228
- escape_chars: 73
- fake_completion: 34
- ignore_previous: 432
- multi_sentence_split: 8
- naive: 101
- null: 1280
- polite_subtle: 273

### carrier counts
- html_comment: 187
- html_hidden: 172
- img_alt: 206
- markdown_table_cell: 229
- null: 1280
- pdf_footer_header: 247
- visible_body: 175

### position counts
- head: 296
- middle: 621
- null: 1280
- tail: 299

### Joint label/source/goal/style/carrier/position counts
| Label | Source | Goal | Style | Carrier | Position | Count |
|---:|---|---|---|---|---|---:|
| 1 | synthetic_injection | change_amount | escape_chars | html_hidden | head | 1 |
| 1 | synthetic_injection | change_amount | escape_chars | html_hidden | middle | 2 |
| 1 | synthetic_injection | change_amount | escape_chars | pdf_footer_header | head | 2 |
| 1 | synthetic_injection | change_amount | escape_chars | pdf_footer_header | tail | 4 |
| 1 | synthetic_injection | change_amount | fake_completion | markdown_table_cell | middle | 1 |
| 1 | synthetic_injection | change_amount | fake_completion | markdown_table_cell | tail | 3 |
| 1 | synthetic_injection | change_amount | fake_completion | visible_body | middle | 2 |
| 1 | synthetic_injection | change_amount | ignore_previous | markdown_table_cell | head | 1 |
| 1 | synthetic_injection | change_amount | ignore_previous | markdown_table_cell | middle | 3 |
| 1 | synthetic_injection | change_amount | ignore_previous | markdown_table_cell | tail | 3 |
| 1 | synthetic_injection | change_amount | ignore_previous | visible_body | head | 2 |
| 1 | synthetic_injection | change_amount | ignore_previous | visible_body | middle | 3 |
| 1 | synthetic_injection | change_amount | ignore_previous | visible_body | tail | 1 |
| 1 | synthetic_injection | change_amount | naive | visible_body | head | 1 |
| 1 | synthetic_injection | change_amount | naive | visible_body | middle | 3 |
| 1 | synthetic_injection | change_amount | naive | visible_body | tail | 2 |
| 1 | synthetic_injection | change_amount | null | null | null | 5 |
| 1 | synthetic_injection | change_amount | polite_subtle | html_hidden | head | 6 |
| 1 | synthetic_injection | change_amount | polite_subtle | html_hidden | middle | 10 |
| 1 | synthetic_injection | change_amount | polite_subtle | html_hidden | tail | 2 |
| 1 | synthetic_injection | change_amount | polite_subtle | markdown_table_cell | head | 3 |
| 1 | synthetic_injection | change_amount | polite_subtle | markdown_table_cell | middle | 6 |
| 1 | synthetic_injection | change_amount | polite_subtle | markdown_table_cell | tail | 2 |
| 1 | synthetic_injection | drain_balance | authority_impersonation | html_comment | middle | 2 |
| 1 | synthetic_injection | drain_balance | authority_impersonation | img_alt | head | 1 |
| 1 | synthetic_injection | drain_balance | authority_impersonation | img_alt | middle | 1 |
| 1 | synthetic_injection | drain_balance | authority_impersonation | img_alt | tail | 3 |
| 1 | synthetic_injection | drain_balance | authority_impersonation | markdown_table_cell | head | 1 |
| 1 | synthetic_injection | drain_balance | authority_impersonation | markdown_table_cell | middle | 6 |
| 1 | synthetic_injection | drain_balance | authority_impersonation | pdf_footer_header | head | 3 |
| 1 | synthetic_injection | drain_balance | authority_impersonation | pdf_footer_header | middle | 1 |
| 1 | synthetic_injection | drain_balance | authority_impersonation | pdf_footer_header | tail | 1 |
| 1 | synthetic_injection | drain_balance | authority_impersonation | visible_body | head | 2 |
| 1 | synthetic_injection | drain_balance | authority_impersonation | visible_body | middle | 2 |
| 1 | synthetic_injection | drain_balance | authority_impersonation | visible_body | tail | 5 |
| 1 | synthetic_injection | drain_balance | combined | html_comment | head | 2 |
| 1 | synthetic_injection | drain_balance | combined | html_comment | middle | 5 |
| 1 | synthetic_injection | drain_balance | combined | markdown_table_cell | middle | 2 |
| 1 | synthetic_injection | drain_balance | combined | markdown_table_cell | tail | 1 |
| 1 | synthetic_injection | drain_balance | combined | pdf_footer_header | middle | 1 |
| 1 | synthetic_injection | drain_balance | combined | pdf_footer_header | tail | 1 |
| 1 | synthetic_injection | drain_balance | escape_chars | html_hidden | middle | 1 |
| 1 | synthetic_injection | drain_balance | fake_completion | markdown_table_cell | middle | 2 |
| 1 | synthetic_injection | drain_balance | fake_completion | pdf_footer_header | middle | 3 |
| 1 | synthetic_injection | drain_balance | fake_completion | pdf_footer_header | tail | 1 |
| 1 | synthetic_injection | drain_balance | multi_sentence_split | html_hidden | middle | 1 |
| 1 | synthetic_injection | drain_balance | multi_sentence_split | html_hidden | tail | 1 |
| 1 | synthetic_injection | drain_balance | naive | html_comment | middle | 1 |
| 1 | synthetic_injection | drain_balance | naive | html_comment | tail | 1 |
| 1 | synthetic_injection | drain_balance | naive | html_hidden | middle | 1 |
| 1 | synthetic_injection | drain_balance | naive | markdown_table_cell | head | 1 |
| 1 | synthetic_injection | drain_balance | naive | markdown_table_cell | middle | 4 |
| 1 | synthetic_injection | drain_balance | naive | markdown_table_cell | tail | 2 |
| 1 | synthetic_injection | drain_balance | naive | visible_body | head | 1 |
| 1 | synthetic_injection | drain_balance | naive | visible_body | middle | 4 |
| 1 | synthetic_injection | drain_balance | null | null | null | 3 |
| 1 | synthetic_injection | drain_balance | polite_subtle | html_comment | head | 1 |
| 1 | synthetic_injection | drain_balance | polite_subtle | html_comment | middle | 2 |
| 1 | synthetic_injection | drain_balance | polite_subtle | html_comment | tail | 1 |
| 1 | synthetic_injection | drain_balance | polite_subtle | html_hidden | head | 1 |
| 1 | synthetic_injection | drain_balance | polite_subtle | html_hidden | middle | 4 |
| 1 | synthetic_injection | drain_balance | polite_subtle | html_hidden | tail | 3 |
| 1 | synthetic_injection | escalate_permission | null | null | null | 2 |
| 1 | synthetic_injection | exfiltrate_private_data | authority_impersonation | img_alt | middle | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | authority_impersonation | markdown_table_cell | head | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | authority_impersonation | markdown_table_cell | middle | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | authority_impersonation | visible_body | middle | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | combined | pdf_footer_header | head | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | combined | pdf_footer_header | middle | 2 |
| 1 | synthetic_injection | exfiltrate_private_data | combined | pdf_footer_header | tail | 3 |
| 1 | synthetic_injection | exfiltrate_private_data | combined | visible_body | head | 4 |
| 1 | synthetic_injection | exfiltrate_private_data | combined | visible_body | middle | 9 |
| 1 | synthetic_injection | exfiltrate_private_data | combined | visible_body | tail | 3 |
| 1 | synthetic_injection | exfiltrate_private_data | ignore_previous | markdown_table_cell | head | 6 |
| 1 | synthetic_injection | exfiltrate_private_data | ignore_previous | markdown_table_cell | middle | 20 |
| 1 | synthetic_injection | exfiltrate_private_data | ignore_previous | markdown_table_cell | tail | 5 |
| 1 | synthetic_injection | exfiltrate_private_data | ignore_previous | visible_body | head | 8 |
| 1 | synthetic_injection | exfiltrate_private_data | ignore_previous | visible_body | middle | 10 |
| 1 | synthetic_injection | exfiltrate_private_data | ignore_previous | visible_body | tail | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | naive | img_alt | middle | 2 |
| 1 | synthetic_injection | exfiltrate_private_data | naive | img_alt | tail | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | naive | visible_body | middle | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | null | null | null | 3 |
| 1 | synthetic_injection | exfiltrate_private_data | polite_subtle | html_comment | head | 9 |
| 1 | synthetic_injection | exfiltrate_private_data | polite_subtle | html_comment | middle | 12 |
| 1 | synthetic_injection | exfiltrate_private_data | polite_subtle | html_comment | tail | 7 |
| 1 | synthetic_injection | exfiltrate_private_data | polite_subtle | html_hidden | head | 11 |
| 1 | synthetic_injection | exfiltrate_private_data | polite_subtle | html_hidden | middle | 15 |
| 1 | synthetic_injection | exfiltrate_private_data | polite_subtle | html_hidden | tail | 4 |
| 1 | synthetic_injection | exfiltrate_secret | authority_impersonation | html_hidden | head | 2 |
| 1 | synthetic_injection | exfiltrate_secret | authority_impersonation | html_hidden | middle | 2 |
| 1 | synthetic_injection | exfiltrate_secret | authority_impersonation | visible_body | head | 3 |
| 1 | synthetic_injection | exfiltrate_secret | combined | img_alt | middle | 3 |
| 1 | synthetic_injection | exfiltrate_secret | combined | img_alt | tail | 1 |
| 1 | synthetic_injection | exfiltrate_secret | combined | pdf_footer_header | head | 1 |
| 1 | synthetic_injection | exfiltrate_secret | combined | pdf_footer_header | middle | 1 |
| 1 | synthetic_injection | exfiltrate_secret | combined | pdf_footer_header | tail | 3 |
| 1 | synthetic_injection | exfiltrate_secret | escape_chars | html_comment | head | 1 |
| 1 | synthetic_injection | exfiltrate_secret | escape_chars | html_comment | middle | 5 |
| 1 | synthetic_injection | exfiltrate_secret | escape_chars | html_comment | tail | 5 |
| 1 | synthetic_injection | exfiltrate_secret | escape_chars | img_alt | head | 3 |
| 1 | synthetic_injection | exfiltrate_secret | escape_chars | img_alt | middle | 7 |
| 1 | synthetic_injection | exfiltrate_secret | escape_chars | img_alt | tail | 4 |
| 1 | synthetic_injection | exfiltrate_secret | escape_chars | pdf_footer_header | head | 7 |
| 1 | synthetic_injection | exfiltrate_secret | escape_chars | pdf_footer_header | middle | 19 |
| 1 | synthetic_injection | exfiltrate_secret | escape_chars | pdf_footer_header | tail | 7 |
| 1 | synthetic_injection | exfiltrate_secret | fake_completion | pdf_footer_header | head | 1 |
| 1 | synthetic_injection | exfiltrate_secret | ignore_previous | img_alt | head | 9 |
| 1 | synthetic_injection | exfiltrate_secret | ignore_previous | img_alt | middle | 12 |
| 1 | synthetic_injection | exfiltrate_secret | ignore_previous | img_alt | tail | 8 |
| 1 | synthetic_injection | exfiltrate_secret | ignore_previous | markdown_table_cell | head | 9 |
| 1 | synthetic_injection | exfiltrate_secret | ignore_previous | markdown_table_cell | middle | 16 |
| 1 | synthetic_injection | exfiltrate_secret | ignore_previous | markdown_table_cell | tail | 5 |
| 1 | synthetic_injection | exfiltrate_secret | naive | html_hidden | head | 8 |
| 1 | synthetic_injection | exfiltrate_secret | naive | html_hidden | middle | 14 |
| 1 | synthetic_injection | exfiltrate_secret | naive | html_hidden | tail | 3 |
| 1 | synthetic_injection | exfiltrate_secret | naive | visible_body | head | 4 |
| 1 | synthetic_injection | exfiltrate_secret | naive | visible_body | middle | 15 |
| 1 | synthetic_injection | exfiltrate_secret | naive | visible_body | tail | 8 |
| 1 | synthetic_injection | exfiltrate_secret | null | null | null | 2 |
| 1 | synthetic_injection | exfiltrate_secret | polite_subtle | html_comment | head | 2 |
| 1 | synthetic_injection | exfiltrate_secret | polite_subtle | html_comment | middle | 6 |
| 1 | synthetic_injection | exfiltrate_secret | polite_subtle | html_comment | tail | 3 |
| 1 | synthetic_injection | exfiltrate_secret | polite_subtle | html_hidden | head | 4 |
| 1 | synthetic_injection | exfiltrate_secret | polite_subtle | html_hidden | middle | 4 |
| 1 | synthetic_injection | exfiltrate_secret | polite_subtle | html_hidden | tail | 1 |
| 1 | synthetic_injection | extra_transfer | authority_impersonation | pdf_footer_header | middle | 2 |
| 1 | synthetic_injection | extra_transfer | authority_impersonation | pdf_footer_header | tail | 1 |
| 1 | synthetic_injection | extra_transfer | authority_impersonation | visible_body | head | 1 |
| 1 | synthetic_injection | extra_transfer | authority_impersonation | visible_body | middle | 1 |
| 1 | synthetic_injection | extra_transfer | authority_impersonation | visible_body | tail | 1 |
| 1 | synthetic_injection | extra_transfer | escape_chars | img_alt | middle | 1 |
| 1 | synthetic_injection | extra_transfer | escape_chars | markdown_table_cell | middle | 1 |
| 1 | synthetic_injection | extra_transfer | escape_chars | markdown_table_cell | tail | 1 |
| 1 | synthetic_injection | extra_transfer | fake_completion | html_comment | middle | 1 |
| 1 | synthetic_injection | extra_transfer | fake_completion | markdown_table_cell | middle | 1 |
| 1 | synthetic_injection | extra_transfer | fake_completion | pdf_footer_header | head | 1 |
| 1 | synthetic_injection | extra_transfer | ignore_previous | img_alt | head | 4 |
| 1 | synthetic_injection | extra_transfer | ignore_previous | img_alt | middle | 10 |
| 1 | synthetic_injection | extra_transfer | ignore_previous | img_alt | tail | 3 |
| 1 | synthetic_injection | extra_transfer | ignore_previous | pdf_footer_header | head | 5 |
| 1 | synthetic_injection | extra_transfer | ignore_previous | pdf_footer_header | middle | 12 |
| 1 | synthetic_injection | extra_transfer | ignore_previous | pdf_footer_header | tail | 9 |
| 1 | synthetic_injection | extra_transfer | null | null | null | 4 |
| 1 | synthetic_injection | extra_transfer | polite_subtle | html_comment | head | 8 |
| 1 | synthetic_injection | extra_transfer | polite_subtle | html_comment | middle | 17 |
| 1 | synthetic_injection | extra_transfer | polite_subtle | html_comment | tail | 13 |
| 1 | synthetic_injection | extra_transfer | polite_subtle | markdown_table_cell | head | 2 |
| 1 | synthetic_injection | extra_transfer | polite_subtle | markdown_table_cell | middle | 2 |
| 1 | synthetic_injection | extra_transfer | polite_subtle | markdown_table_cell | tail | 3 |
| 1 | synthetic_injection | extra_transfer | polite_subtle | visible_body | head | 8 |
| 1 | synthetic_injection | extra_transfer | polite_subtle | visible_body | middle | 12 |
| 1 | synthetic_injection | fake_user_approval | authority_impersonation | markdown_table_cell | head | 1 |
| 1 | synthetic_injection | fake_user_approval | authority_impersonation | visible_body | tail | 1 |
| 1 | synthetic_injection | fake_user_approval | combined | html_hidden | middle | 5 |
| 1 | synthetic_injection | fake_user_approval | combined | html_hidden | tail | 1 |
| 1 | synthetic_injection | fake_user_approval | combined | img_alt | head | 6 |
| 1 | synthetic_injection | fake_user_approval | combined | img_alt | middle | 18 |
| 1 | synthetic_injection | fake_user_approval | combined | img_alt | tail | 5 |
| 1 | synthetic_injection | fake_user_approval | combined | pdf_footer_header | head | 4 |
| 1 | synthetic_injection | fake_user_approval | combined | pdf_footer_header | middle | 9 |
| 1 | synthetic_injection | fake_user_approval | combined | pdf_footer_header | tail | 6 |
| 1 | synthetic_injection | fake_user_approval | ignore_previous | img_alt | head | 8 |
| 1 | synthetic_injection | fake_user_approval | ignore_previous | img_alt | middle | 20 |
| 1 | synthetic_injection | fake_user_approval | ignore_previous | img_alt | tail | 13 |
| 1 | synthetic_injection | fake_user_approval | ignore_previous | markdown_table_cell | head | 13 |
| 1 | synthetic_injection | fake_user_approval | ignore_previous | markdown_table_cell | middle | 25 |
| 1 | synthetic_injection | fake_user_approval | ignore_previous | markdown_table_cell | tail | 11 |
| 1 | synthetic_injection | fake_user_approval | multi_sentence_split | html_hidden | middle | 1 |
| 1 | synthetic_injection | fake_user_approval | multi_sentence_split | visible_body | tail | 1 |
| 1 | synthetic_injection | fake_user_approval | naive | visible_body | head | 1 |
| 1 | synthetic_injection | fake_user_approval | naive | visible_body | middle | 2 |
| 1 | synthetic_injection | fake_user_approval | naive | visible_body | tail | 3 |
| 1 | synthetic_injection | fake_user_approval | null | null | null | 3 |
| 1 | synthetic_injection | goal_hijack_generic | authority_impersonation | markdown_table_cell | middle | 2 |
| 1 | synthetic_injection | goal_hijack_generic | authority_impersonation | visible_body | head | 1 |
| 1 | synthetic_injection | goal_hijack_generic | authority_impersonation | visible_body | middle | 2 |
| 1 | synthetic_injection | goal_hijack_generic | authority_impersonation | visible_body | tail | 2 |
| 1 | synthetic_injection | goal_hijack_generic | combined | img_alt | head | 3 |
| 1 | synthetic_injection | goal_hijack_generic | combined | img_alt | middle | 4 |
| 1 | synthetic_injection | goal_hijack_generic | combined | img_alt | tail | 2 |
| 1 | synthetic_injection | goal_hijack_generic | combined | markdown_table_cell | head | 1 |
| 1 | synthetic_injection | goal_hijack_generic | combined | markdown_table_cell | middle | 5 |
| 1 | synthetic_injection | goal_hijack_generic | combined | markdown_table_cell | tail | 4 |
| 1 | synthetic_injection | goal_hijack_generic | combined | pdf_footer_header | head | 2 |
| 1 | synthetic_injection | goal_hijack_generic | combined | pdf_footer_header | middle | 3 |
| 1 | synthetic_injection | goal_hijack_generic | combined | pdf_footer_header | tail | 5 |
| 1 | synthetic_injection | goal_hijack_generic | combined | visible_body | head | 2 |
| 1 | synthetic_injection | goal_hijack_generic | combined | visible_body | middle | 6 |
| 1 | synthetic_injection | goal_hijack_generic | combined | visible_body | tail | 1 |
| 1 | synthetic_injection | goal_hijack_generic | ignore_previous | html_comment | head | 3 |
| 1 | synthetic_injection | goal_hijack_generic | ignore_previous | html_comment | middle | 6 |
| 1 | synthetic_injection | goal_hijack_generic | ignore_previous | html_comment | tail | 9 |
| 1 | synthetic_injection | goal_hijack_generic | ignore_previous | markdown_table_cell | head | 6 |
| 1 | synthetic_injection | goal_hijack_generic | ignore_previous | markdown_table_cell | middle | 14 |
| 1 | synthetic_injection | goal_hijack_generic | ignore_previous | markdown_table_cell | tail | 3 |
| 1 | synthetic_injection | goal_hijack_generic | ignore_previous | pdf_footer_header | head | 5 |
| 1 | synthetic_injection | goal_hijack_generic | ignore_previous | pdf_footer_header | middle | 7 |
| 1 | synthetic_injection | goal_hijack_generic | ignore_previous | pdf_footer_header | tail | 5 |
| 1 | synthetic_injection | goal_hijack_generic | ignore_previous | visible_body | head | 7 |
| 1 | synthetic_injection | goal_hijack_generic | ignore_previous | visible_body | middle | 9 |
| 1 | synthetic_injection | goal_hijack_generic | ignore_previous | visible_body | tail | 3 |
| 1 | synthetic_injection | goal_hijack_generic | naive | html_comment | head | 1 |
| 1 | synthetic_injection | goal_hijack_generic | naive | html_comment | middle | 4 |
| 1 | synthetic_injection | goal_hijack_generic | naive | html_comment | tail | 1 |
| 1 | synthetic_injection | goal_hijack_generic | naive | markdown_table_cell | tail | 2 |
| 1 | synthetic_injection | goal_hijack_generic | null | null | null | 2 |
| 1 | synthetic_injection | out_of_scope_action | combined | img_alt | middle | 1 |
| 1 | synthetic_injection | out_of_scope_action | combined | pdf_footer_header | head | 1 |
| 1 | synthetic_injection | out_of_scope_action | combined | pdf_footer_header | middle | 4 |
| 1 | synthetic_injection | out_of_scope_action | combined | pdf_footer_header | tail | 5 |
| 1 | synthetic_injection | out_of_scope_action | combined | visible_body | middle | 1 |
| 1 | synthetic_injection | out_of_scope_action | fake_completion | html_hidden | tail | 1 |
| 1 | synthetic_injection | out_of_scope_action | fake_completion | markdown_table_cell | head | 1 |
| 1 | synthetic_injection | out_of_scope_action | fake_completion | markdown_table_cell | middle | 3 |
| 1 | synthetic_injection | out_of_scope_action | fake_completion | markdown_table_cell | tail | 2 |
| 1 | synthetic_injection | out_of_scope_action | fake_completion | pdf_footer_header | head | 1 |
| 1 | synthetic_injection | out_of_scope_action | fake_completion | pdf_footer_header | middle | 1 |
| 1 | synthetic_injection | out_of_scope_action | fake_completion | pdf_footer_header | tail | 2 |
| 1 | synthetic_injection | out_of_scope_action | ignore_previous | img_alt | head | 1 |
| 1 | synthetic_injection | out_of_scope_action | ignore_previous | img_alt | middle | 3 |
| 1 | synthetic_injection | out_of_scope_action | ignore_previous | img_alt | tail | 2 |
| 1 | synthetic_injection | out_of_scope_action | ignore_previous | pdf_footer_header | head | 1 |
| 1 | synthetic_injection | out_of_scope_action | ignore_previous | pdf_footer_header | tail | 1 |
| 1 | synthetic_injection | out_of_scope_action | multi_sentence_split | html_comment | tail | 1 |
| 1 | synthetic_injection | out_of_scope_action | naive | visible_body | head | 1 |
| 1 | synthetic_injection | out_of_scope_action | naive | visible_body | middle | 3 |
| 1 | synthetic_injection | out_of_scope_action | naive | visible_body | tail | 2 |
| 1 | synthetic_injection | out_of_scope_action | null | null | null | 1 |
| 1 | synthetic_injection | out_of_scope_action | polite_subtle | html_comment | head | 1 |
| 1 | synthetic_injection | out_of_scope_action | polite_subtle | html_comment | middle | 4 |
| 1 | synthetic_injection | out_of_scope_action | polite_subtle | html_comment | tail | 3 |
| 1 | synthetic_injection | out_of_scope_action | polite_subtle | visible_body | head | 1 |
| 1 | synthetic_injection | out_of_scope_action | polite_subtle | visible_body | middle | 3 |
| 1 | synthetic_injection | redirect_recipient | authority_impersonation | visible_body | middle | 2 |
| 1 | synthetic_injection | redirect_recipient | combined | html_comment | tail | 1 |
| 1 | synthetic_injection | redirect_recipient | combined | img_alt | head | 2 |
| 1 | synthetic_injection | redirect_recipient | combined | markdown_table_cell | head | 1 |
| 1 | synthetic_injection | redirect_recipient | combined | markdown_table_cell | middle | 4 |
| 1 | synthetic_injection | redirect_recipient | combined | markdown_table_cell | tail | 2 |
| 1 | synthetic_injection | redirect_recipient | fake_completion | markdown_table_cell | middle | 3 |
| 1 | synthetic_injection | redirect_recipient | fake_completion | pdf_footer_header | middle | 1 |
| 1 | synthetic_injection | redirect_recipient | ignore_previous | html_comment | middle | 3 |
| 1 | synthetic_injection | redirect_recipient | ignore_previous | html_comment | tail | 2 |
| 1 | synthetic_injection | redirect_recipient | ignore_previous | img_alt | head | 1 |
| 1 | synthetic_injection | redirect_recipient | ignore_previous | img_alt | middle | 4 |
| 1 | synthetic_injection | redirect_recipient | multi_sentence_split | markdown_table_cell | head | 3 |
| 1 | synthetic_injection | redirect_recipient | null | null | null | 3 |
| 1 | synthetic_injection | redirect_recipient | polite_subtle | html_comment | head | 1 |
| 1 | synthetic_injection | redirect_recipient | polite_subtle | html_comment | middle | 4 |
| 1 | synthetic_injection | redirect_recipient | polite_subtle | pdf_footer_header | head | 1 |
| 1 | synthetic_injection | redirect_recipient | polite_subtle | pdf_footer_header | middle | 3 |
| 1 | synthetic_injection | suppress_confirmation | authority_impersonation | html_comment | tail | 1 |
| 1 | synthetic_injection | suppress_confirmation | authority_impersonation | pdf_footer_header | middle | 2 |
| 1 | synthetic_injection | suppress_confirmation | combined | img_alt | middle | 2 |
| 1 | synthetic_injection | suppress_confirmation | combined | pdf_footer_header | middle | 2 |
| 1 | synthetic_injection | suppress_confirmation | escape_chars | html_comment | tail | 1 |
| 1 | synthetic_injection | suppress_confirmation | fake_completion | html_comment | middle | 2 |
| 1 | synthetic_injection | suppress_confirmation | fake_completion | markdown_table_cell | head | 1 |
| 1 | synthetic_injection | suppress_confirmation | ignore_previous | html_comment | tail | 2 |
| 1 | synthetic_injection | suppress_confirmation | ignore_previous | pdf_footer_header | head | 1 |
| 1 | synthetic_injection | suppress_confirmation | ignore_previous | pdf_footer_header | middle | 5 |
| 1 | synthetic_injection | suppress_confirmation | naive | html_hidden | head | 1 |
| 1 | synthetic_injection | suppress_confirmation | naive | html_hidden | tail | 2 |
| 1 | synthetic_injection | suppress_confirmation | naive | img_alt | tail | 1 |
| 1 | synthetic_injection | suppress_confirmation | null | null | null | 2 |
| 1 | synthetic_injection | suppress_confirmation | polite_subtle | html_hidden | middle | 3 |
| 1 | synthetic_injection | suppress_confirmation | polite_subtle | markdown_table_cell | head | 1 |
| 1 | synthetic_injection | suppress_confirmation | polite_subtle | markdown_table_cell | middle | 2 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | authority_impersonation | html_hidden | head | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | authority_impersonation | img_alt | head | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | authority_impersonation | img_alt | middle | 2 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | authority_impersonation | markdown_table_cell | tail | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | authority_impersonation | visible_body | middle | 2 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | authority_impersonation | visible_body | tail | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | combined | html_comment | head | 7 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | combined | html_comment | middle | 20 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | combined | html_comment | tail | 6 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | combined | pdf_footer_header | head | 10 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | combined | pdf_footer_header | middle | 15 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | combined | pdf_footer_header | tail | 9 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | escape_chars | img_alt | head | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | ignore_previous | html_hidden | head | 10 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | ignore_previous | html_hidden | middle | 14 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | ignore_previous | html_hidden | tail | 6 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | ignore_previous | pdf_footer_header | head | 14 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | ignore_previous | pdf_footer_header | middle | 19 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | ignore_previous | pdf_footer_header | tail | 11 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | null | null | null | 2 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | polite_subtle | html_hidden | head | 6 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | polite_subtle | html_hidden | middle | 12 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | polite_subtle | html_hidden | tail | 8 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | polite_subtle | img_alt | head | 7 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | polite_subtle | img_alt | middle | 17 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | polite_subtle | img_alt | tail | 8 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | polite_subtle | markdown_table_cell | head | 2 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | polite_subtle | markdown_table_cell | middle | 2 |
| null | crypto_prose | null | null | null | null | 62 |
| null | hard_negative | exfiltrate_private_data | null | null | null | 2 |
| null | hard_negative | exfiltrate_secret | null | null | null | 2 |
| null | hard_negative | null | null | null | null | 1182 |

Whitespace token-length histogram: {"0-16": 1844, "129+": 0, "17-32": 634, "33-64": 18, "65-128": 0}

## val
Segments: 190; mean characters: 121.4

| Label | Source | Count |
|---:|---|---:|
| 0 | crypto_prose | 2 |
| 0 | hard_negative | 93 |
| 1 | synthetic_injection | 95 |

### goal counts
- change_amount: 4
- exfiltrate_private_data: 2
- exfiltrate_secret: 6
- extra_transfer: 11
- fake_user_approval: 57
- null: 94
- out_of_scope_action: 4
- unauthorized_typed_data_sign: 12

### style counts
- authority_impersonation: 4
- combined: 4
- ignore_previous: 10
- multi_sentence_split: 2
- naive: 11
- null: 98
- polite_subtle: 61

### carrier counts
- html_comment: 25
- html_hidden: 35
- img_alt: 21
- markdown_table_cell: 6
- null: 98
- visible_body: 5

### position counts
- head: 25
- middle: 39
- null: 98
- tail: 28

### Joint label/source/goal/style/carrier/position counts
| Label | Source | Goal | Style | Carrier | Position | Count |
|---:|---|---|---|---|---|---:|
| 1 | synthetic_injection | change_amount | combined | img_alt | head | 1 |
| 1 | synthetic_injection | change_amount | combined | img_alt | middle | 1 |
| 1 | synthetic_injection | change_amount | combined | img_alt | tail | 2 |
| 1 | synthetic_injection | exfiltrate_private_data | multi_sentence_split | img_alt | middle | 2 |
| 1 | synthetic_injection | exfiltrate_secret | authority_impersonation | img_alt | head | 1 |
| 1 | synthetic_injection | exfiltrate_secret | authority_impersonation | img_alt | middle | 1 |
| 1 | synthetic_injection | exfiltrate_secret | authority_impersonation | markdown_table_cell | head | 2 |
| 1 | synthetic_injection | exfiltrate_secret | null | null | null | 1 |
| 1 | synthetic_injection | extra_transfer | ignore_previous | img_alt | head | 1 |
| 1 | synthetic_injection | extra_transfer | ignore_previous | img_alt | middle | 4 |
| 1 | synthetic_injection | extra_transfer | ignore_previous | img_alt | tail | 1 |
| 1 | synthetic_injection | extra_transfer | ignore_previous | markdown_table_cell | middle | 2 |
| 1 | synthetic_injection | extra_transfer | ignore_previous | markdown_table_cell | tail | 2 |
| 1 | synthetic_injection | extra_transfer | null | null | null | 1 |
| 1 | synthetic_injection | fake_user_approval | polite_subtle | html_comment | head | 3 |
| 1 | synthetic_injection | fake_user_approval | polite_subtle | html_comment | middle | 13 |
| 1 | synthetic_injection | fake_user_approval | polite_subtle | html_comment | tail | 6 |
| 1 | synthetic_injection | fake_user_approval | polite_subtle | html_hidden | head | 13 |
| 1 | synthetic_injection | fake_user_approval | polite_subtle | html_hidden | middle | 9 |
| 1 | synthetic_injection | fake_user_approval | polite_subtle | html_hidden | tail | 13 |
| 1 | synthetic_injection | out_of_scope_action | polite_subtle | html_comment | head | 1 |
| 1 | synthetic_injection | out_of_scope_action | polite_subtle | html_comment | middle | 2 |
| 1 | synthetic_injection | out_of_scope_action | polite_subtle | img_alt | head | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | naive | img_alt | middle | 4 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | naive | img_alt | tail | 2 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | naive | visible_body | head | 2 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | naive | visible_body | middle | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | naive | visible_body | tail | 2 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | null | null | null | 1 |
| null | crypto_prose | null | null | null | null | 2 |
| null | hard_negative | exfiltrate_secret | null | null | null | 1 |
| null | hard_negative | null | null | null | null | 92 |

Whitespace token-length histogram: {"0-16": 106, "129+": 0, "17-32": 82, "33-64": 2, "65-128": 0}

## test_id
Segments: 426; mean characters: 112.1

| Label | Source | Count |
|---:|---|---:|
| 0 | crypto_prose | 5 |
| 0 | hard_negative | 208 |
| 1 | synthetic_injection | 213 |

### goal counts
- change_amount: 57
- drain_balance: 32
- escalate_permission: 1
- exfiltrate_private_data: 2
- exfiltrate_secret: 91
- goal_hijack_generic: 15
- null: 212
- out_of_scope_action: 5
- redirect_recipient: 6
- unauthorized_typed_data_sign: 5

### style counts
- authority_impersonation: 96
- combined: 31
- fake_completion: 5
- ignore_previous: 6
- null: 216
- polite_subtle: 72

### carrier counts
- html_comment: 41
- html_hidden: 24
- img_alt: 25
- markdown_table_cell: 7
- null: 216
- pdf_footer_header: 109
- visible_body: 4

### position counts
- head: 47
- middle: 111
- null: 216
- tail: 52

### Joint label/source/goal/style/carrier/position counts
| Label | Source | Goal | Style | Carrier | Position | Count |
|---:|---|---|---|---|---|---:|
| 1 | synthetic_injection | change_amount | polite_subtle | html_comment | head | 5 |
| 1 | synthetic_injection | change_amount | polite_subtle | html_comment | middle | 23 |
| 1 | synthetic_injection | change_amount | polite_subtle | html_comment | tail | 5 |
| 1 | synthetic_injection | change_amount | polite_subtle | html_hidden | head | 5 |
| 1 | synthetic_injection | change_amount | polite_subtle | html_hidden | middle | 12 |
| 1 | synthetic_injection | change_amount | polite_subtle | html_hidden | tail | 7 |
| 1 | synthetic_injection | drain_balance | combined | img_alt | head | 4 |
| 1 | synthetic_injection | drain_balance | combined | img_alt | middle | 9 |
| 1 | synthetic_injection | drain_balance | combined | img_alt | tail | 2 |
| 1 | synthetic_injection | drain_balance | combined | pdf_footer_header | head | 2 |
| 1 | synthetic_injection | drain_balance | combined | pdf_footer_header | middle | 5 |
| 1 | synthetic_injection | drain_balance | combined | pdf_footer_header | tail | 9 |
| 1 | synthetic_injection | drain_balance | null | null | null | 1 |
| 1 | synthetic_injection | escalate_permission | null | null | null | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | null | null | null | 1 |
| 1 | synthetic_injection | exfiltrate_secret | authority_impersonation | pdf_footer_header | head | 25 |
| 1 | synthetic_injection | exfiltrate_secret | authority_impersonation | pdf_footer_header | middle | 40 |
| 1 | synthetic_injection | exfiltrate_secret | authority_impersonation | pdf_footer_header | tail | 26 |
| 1 | synthetic_injection | goal_hijack_generic | polite_subtle | html_comment | middle | 7 |
| 1 | synthetic_injection | goal_hijack_generic | polite_subtle | html_comment | tail | 1 |
| 1 | synthetic_injection | goal_hijack_generic | polite_subtle | img_alt | head | 3 |
| 1 | synthetic_injection | goal_hijack_generic | polite_subtle | img_alt | middle | 3 |
| 1 | synthetic_injection | goal_hijack_generic | polite_subtle | img_alt | tail | 1 |
| 1 | synthetic_injection | out_of_scope_action | authority_impersonation | markdown_table_cell | middle | 4 |
| 1 | synthetic_injection | out_of_scope_action | authority_impersonation | pdf_footer_header | head | 1 |
| 1 | synthetic_injection | redirect_recipient | ignore_previous | img_alt | head | 1 |
| 1 | synthetic_injection | redirect_recipient | ignore_previous | img_alt | middle | 2 |
| 1 | synthetic_injection | redirect_recipient | ignore_previous | markdown_table_cell | middle | 2 |
| 1 | synthetic_injection | redirect_recipient | ignore_previous | markdown_table_cell | tail | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | fake_completion | pdf_footer_header | head | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | fake_completion | visible_body | middle | 4 |
| null | crypto_prose | null | null | null | null | 5 |
| null | hard_negative | exfiltrate_private_data | null | null | null | 1 |
| null | hard_negative | null | null | null | null | 207 |

Whitespace token-length histogram: {"0-16": 182, "129+": 0, "17-32": 242, "33-64": 2, "65-128": 0}

## test_heldout
Segments: 1243; mean characters: 116.7

| Label | Source | Count |
|---:|---|---:|
| 0 | crypto_prose | 66 |
| 0 | hard_negative | 499 |
| 1 | synthetic_injection | 678 |

### goal counts
- change_amount: 49
- drain_balance: 46
- escalate_permission: 105
- exfiltrate_private_data: 74
- exfiltrate_secret: 63
- extra_transfer: 57
- fake_user_approval: 47
- goal_hijack_generic: 58
- null: 565
- out_of_scope_action: 33
- redirect_recipient: 46
- suppress_confirmation: 40
- unauthorized_typed_data_sign: 60

### style counts
- authority_impersonation: 32
- combined: 70
- escape_chars: 46
- fake_completion: 40
- ignore_previous: 66
- multi_sentence_split: 76
- naive: 49
- null: 565
- obfuscated: 120
- polite_subtle: 64
- role_play: 115

### carrier counts
- email_quote: 263
- html_comment: 14
- html_hidden: 36
- img_alt: 20
- json_tool_response: 251
- markdown_table_cell: 40
- null: 565
- pdf_footer_header: 31
- visible_body: 23

### position counts
- head: 173
- middle: 332
- null: 565
- tail: 173

### Joint label/source/goal/style/carrier/position counts
| Label | Source | Goal | Style | Carrier | Position | Count |
|---:|---|---|---|---|---|---:|
| 1 | synthetic_injection | change_amount | combined | email_quote | head | 1 |
| 1 | synthetic_injection | change_amount | combined | email_quote | middle | 4 |
| 1 | synthetic_injection | change_amount | escape_chars | json_tool_response | head | 1 |
| 1 | synthetic_injection | change_amount | escape_chars | json_tool_response | middle | 1 |
| 1 | synthetic_injection | change_amount | escape_chars | json_tool_response | tail | 1 |
| 1 | synthetic_injection | change_amount | ignore_previous | email_quote | head | 1 |
| 1 | synthetic_injection | change_amount | ignore_previous | email_quote | middle | 2 |
| 1 | synthetic_injection | change_amount | ignore_previous | email_quote | tail | 1 |
| 1 | synthetic_injection | change_amount | multi_sentence_split | email_quote | tail | 5 |
| 1 | synthetic_injection | change_amount | naive | email_quote | head | 2 |
| 1 | synthetic_injection | change_amount | naive | email_quote | tail | 1 |
| 1 | synthetic_injection | change_amount | obfuscated | email_quote | head | 3 |
| 1 | synthetic_injection | change_amount | obfuscated | email_quote | middle | 2 |
| 1 | synthetic_injection | change_amount | obfuscated | img_alt | middle | 1 |
| 1 | synthetic_injection | change_amount | obfuscated | img_alt | tail | 1 |
| 1 | synthetic_injection | change_amount | obfuscated | json_tool_response | head | 1 |
| 1 | synthetic_injection | change_amount | obfuscated | json_tool_response | middle | 1 |
| 1 | synthetic_injection | change_amount | obfuscated | json_tool_response | tail | 1 |
| 1 | synthetic_injection | change_amount | obfuscated | visible_body | head | 1 |
| 1 | synthetic_injection | change_amount | obfuscated | visible_body | tail | 1 |
| 1 | synthetic_injection | change_amount | polite_subtle | email_quote | head | 1 |
| 1 | synthetic_injection | change_amount | polite_subtle | email_quote | middle | 2 |
| 1 | synthetic_injection | change_amount | polite_subtle | email_quote | tail | 1 |
| 1 | synthetic_injection | change_amount | role_play | json_tool_response | head | 2 |
| 1 | synthetic_injection | change_amount | role_play | json_tool_response | middle | 6 |
| 1 | synthetic_injection | change_amount | role_play | json_tool_response | tail | 1 |
| 1 | synthetic_injection | change_amount | role_play | pdf_footer_header | head | 1 |
| 1 | synthetic_injection | change_amount | role_play | pdf_footer_header | middle | 2 |
| 1 | synthetic_injection | change_amount | role_play | pdf_footer_header | tail | 1 |
| 1 | synthetic_injection | drain_balance | combined | email_quote | middle | 3 |
| 1 | synthetic_injection | drain_balance | escape_chars | json_tool_response | head | 2 |
| 1 | synthetic_injection | drain_balance | escape_chars | json_tool_response | middle | 1 |
| 1 | synthetic_injection | drain_balance | ignore_previous | email_quote | middle | 3 |
| 1 | synthetic_injection | drain_balance | ignore_previous | email_quote | tail | 1 |
| 1 | synthetic_injection | drain_balance | ignore_previous | json_tool_response | middle | 4 |
| 1 | synthetic_injection | drain_balance | ignore_previous | json_tool_response | tail | 1 |
| 1 | synthetic_injection | drain_balance | multi_sentence_split | email_quote | head | 1 |
| 1 | synthetic_injection | drain_balance | multi_sentence_split | email_quote | middle | 1 |
| 1 | synthetic_injection | drain_balance | multi_sentence_split | email_quote | tail | 3 |
| 1 | synthetic_injection | drain_balance | naive | json_tool_response | head | 1 |
| 1 | synthetic_injection | drain_balance | naive | json_tool_response | middle | 3 |
| 1 | synthetic_injection | drain_balance | obfuscated | email_quote | tail | 2 |
| 1 | synthetic_injection | drain_balance | obfuscated | html_hidden | middle | 1 |
| 1 | synthetic_injection | drain_balance | obfuscated | visible_body | head | 1 |
| 1 | synthetic_injection | drain_balance | obfuscated | visible_body | middle | 1 |
| 1 | synthetic_injection | drain_balance | polite_subtle | json_tool_response | head | 1 |
| 1 | synthetic_injection | drain_balance | polite_subtle | json_tool_response | middle | 2 |
| 1 | synthetic_injection | drain_balance | role_play | email_quote | head | 1 |
| 1 | synthetic_injection | drain_balance | role_play | email_quote | middle | 2 |
| 1 | synthetic_injection | drain_balance | role_play | email_quote | tail | 3 |
| 1 | synthetic_injection | drain_balance | role_play | json_tool_response | head | 1 |
| 1 | synthetic_injection | drain_balance | role_play | json_tool_response | middle | 5 |
| 1 | synthetic_injection | drain_balance | role_play | json_tool_response | tail | 2 |
| 1 | synthetic_injection | escalate_permission | authority_impersonation | html_comment | middle | 6 |
| 1 | synthetic_injection | escalate_permission | authority_impersonation | img_alt | head | 1 |
| 1 | synthetic_injection | escalate_permission | authority_impersonation | markdown_table_cell | middle | 1 |
| 1 | synthetic_injection | escalate_permission | authority_impersonation | pdf_footer_header | head | 1 |
| 1 | synthetic_injection | escalate_permission | authority_impersonation | pdf_footer_header | middle | 2 |
| 1 | synthetic_injection | escalate_permission | authority_impersonation | visible_body | middle | 2 |
| 1 | synthetic_injection | escalate_permission | combined | email_quote | head | 1 |
| 1 | synthetic_injection | escalate_permission | combined | email_quote | middle | 3 |
| 1 | synthetic_injection | escalate_permission | combined | email_quote | tail | 1 |
| 1 | synthetic_injection | escalate_permission | combined | html_hidden | head | 1 |
| 1 | synthetic_injection | escalate_permission | combined | html_hidden | middle | 3 |
| 1 | synthetic_injection | escalate_permission | combined | html_hidden | tail | 1 |
| 1 | synthetic_injection | escalate_permission | combined | pdf_footer_header | head | 1 |
| 1 | synthetic_injection | escalate_permission | escape_chars | json_tool_response | middle | 1 |
| 1 | synthetic_injection | escalate_permission | escape_chars | json_tool_response | tail | 2 |
| 1 | synthetic_injection | escalate_permission | escape_chars | visible_body | middle | 1 |
| 1 | synthetic_injection | escalate_permission | fake_completion | email_quote | head | 1 |
| 1 | synthetic_injection | escalate_permission | fake_completion | email_quote | middle | 1 |
| 1 | synthetic_injection | escalate_permission | fake_completion | email_quote | tail | 1 |
| 1 | synthetic_injection | escalate_permission | fake_completion | markdown_table_cell | head | 2 |
| 1 | synthetic_injection | escalate_permission | fake_completion | markdown_table_cell | middle | 3 |
| 1 | synthetic_injection | escalate_permission | fake_completion | markdown_table_cell | tail | 1 |
| 1 | synthetic_injection | escalate_permission | fake_completion | pdf_footer_header | middle | 2 |
| 1 | synthetic_injection | escalate_permission | ignore_previous | json_tool_response | head | 1 |
| 1 | synthetic_injection | escalate_permission | ignore_previous | json_tool_response | middle | 3 |
| 1 | synthetic_injection | escalate_permission | ignore_previous | json_tool_response | tail | 2 |
| 1 | synthetic_injection | escalate_permission | ignore_previous | markdown_table_cell | head | 2 |
| 1 | synthetic_injection | escalate_permission | ignore_previous | markdown_table_cell | middle | 2 |
| 1 | synthetic_injection | escalate_permission | ignore_previous | markdown_table_cell | tail | 1 |
| 1 | synthetic_injection | escalate_permission | ignore_previous | visible_body | middle | 1 |
| 1 | synthetic_injection | escalate_permission | ignore_previous | visible_body | tail | 1 |
| 1 | synthetic_injection | escalate_permission | multi_sentence_split | email_quote | head | 4 |
| 1 | synthetic_injection | escalate_permission | multi_sentence_split | email_quote | middle | 2 |
| 1 | synthetic_injection | escalate_permission | multi_sentence_split | email_quote | tail | 5 |
| 1 | synthetic_injection | escalate_permission | multi_sentence_split | html_comment | middle | 1 |
| 1 | synthetic_injection | escalate_permission | multi_sentence_split | visible_body | head | 1 |
| 1 | synthetic_injection | escalate_permission | naive | email_quote | middle | 3 |
| 1 | synthetic_injection | escalate_permission | naive | email_quote | tail | 1 |
| 1 | synthetic_injection | escalate_permission | obfuscated | img_alt | middle | 4 |
| 1 | synthetic_injection | escalate_permission | obfuscated | markdown_table_cell | head | 1 |
| 1 | synthetic_injection | escalate_permission | obfuscated | markdown_table_cell | middle | 2 |
| 1 | synthetic_injection | escalate_permission | obfuscated | markdown_table_cell | tail | 1 |
| 1 | synthetic_injection | escalate_permission | obfuscated | visible_body | head | 2 |
| 1 | synthetic_injection | escalate_permission | polite_subtle | html_hidden | middle | 3 |
| 1 | synthetic_injection | escalate_permission | polite_subtle | html_hidden | tail | 2 |
| 1 | synthetic_injection | escalate_permission | polite_subtle | img_alt | head | 1 |
| 1 | synthetic_injection | escalate_permission | polite_subtle | img_alt | middle | 3 |
| 1 | synthetic_injection | escalate_permission | polite_subtle | json_tool_response | middle | 3 |
| 1 | synthetic_injection | escalate_permission | polite_subtle | json_tool_response | tail | 2 |
| 1 | synthetic_injection | escalate_permission | polite_subtle | markdown_table_cell | middle | 5 |
| 1 | synthetic_injection | escalate_permission | role_play | json_tool_response | head | 1 |
| 1 | synthetic_injection | escalate_permission | role_play | json_tool_response | middle | 3 |
| 1 | synthetic_injection | escalate_permission | role_play | json_tool_response | tail | 3 |
| 1 | synthetic_injection | exfiltrate_private_data | authority_impersonation | json_tool_response | head | 2 |
| 1 | synthetic_injection | exfiltrate_private_data | authority_impersonation | json_tool_response | middle | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | combined | email_quote | head | 2 |
| 1 | synthetic_injection | exfiltrate_private_data | combined | email_quote | middle | 4 |
| 1 | synthetic_injection | exfiltrate_private_data | escape_chars | email_quote | head | 3 |
| 1 | synthetic_injection | exfiltrate_private_data | escape_chars | email_quote | middle | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | escape_chars | json_tool_response | head | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | escape_chars | json_tool_response | middle | 3 |
| 1 | synthetic_injection | exfiltrate_private_data | escape_chars | json_tool_response | tail | 2 |
| 1 | synthetic_injection | exfiltrate_private_data | fake_completion | json_tool_response | head | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | fake_completion | json_tool_response | middle | 2 |
| 1 | synthetic_injection | exfiltrate_private_data | fake_completion | json_tool_response | tail | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | ignore_previous | email_quote | middle | 2 |
| 1 | synthetic_injection | exfiltrate_private_data | ignore_previous | email_quote | tail | 3 |
| 1 | synthetic_injection | exfiltrate_private_data | multi_sentence_split | email_quote | head | 3 |
| 1 | synthetic_injection | exfiltrate_private_data | multi_sentence_split | email_quote | middle | 2 |
| 1 | synthetic_injection | exfiltrate_private_data | multi_sentence_split | email_quote | tail | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | naive | email_quote | middle | 2 |
| 1 | synthetic_injection | exfiltrate_private_data | naive | json_tool_response | head | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | naive | json_tool_response | middle | 5 |
| 1 | synthetic_injection | exfiltrate_private_data | naive | json_tool_response | tail | 2 |
| 1 | synthetic_injection | exfiltrate_private_data | obfuscated | html_hidden | head | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | obfuscated | html_hidden | middle | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | obfuscated | json_tool_response | middle | 2 |
| 1 | synthetic_injection | exfiltrate_private_data | obfuscated | json_tool_response | tail | 3 |
| 1 | synthetic_injection | exfiltrate_private_data | obfuscated | visible_body | middle | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | polite_subtle | email_quote | head | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | polite_subtle | email_quote | middle | 6 |
| 1 | synthetic_injection | exfiltrate_private_data | polite_subtle | email_quote | tail | 2 |
| 1 | synthetic_injection | exfiltrate_private_data | polite_subtle | json_tool_response | head | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | polite_subtle | json_tool_response | middle | 3 |
| 1 | synthetic_injection | exfiltrate_private_data | role_play | email_quote | head | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | role_play | email_quote | middle | 3 |
| 1 | synthetic_injection | exfiltrate_private_data | role_play | email_quote | tail | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | role_play | html_hidden | head | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | role_play | markdown_table_cell | head | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | role_play | markdown_table_cell | middle | 1 |
| 1 | synthetic_injection | exfiltrate_private_data | role_play | markdown_table_cell | tail | 1 |
| 1 | synthetic_injection | exfiltrate_secret | combined | json_tool_response | head | 3 |
| 1 | synthetic_injection | exfiltrate_secret | combined | json_tool_response | tail | 2 |
| 1 | synthetic_injection | exfiltrate_secret | escape_chars | json_tool_response | head | 1 |
| 1 | synthetic_injection | exfiltrate_secret | escape_chars | json_tool_response | middle | 2 |
| 1 | synthetic_injection | exfiltrate_secret | escape_chars | json_tool_response | tail | 2 |
| 1 | synthetic_injection | exfiltrate_secret | fake_completion | email_quote | head | 4 |
| 1 | synthetic_injection | exfiltrate_secret | fake_completion | email_quote | middle | 3 |
| 1 | synthetic_injection | exfiltrate_secret | ignore_previous | json_tool_response | head | 1 |
| 1 | synthetic_injection | exfiltrate_secret | ignore_previous | json_tool_response | middle | 3 |
| 1 | synthetic_injection | exfiltrate_secret | ignore_previous | json_tool_response | tail | 4 |
| 1 | synthetic_injection | exfiltrate_secret | multi_sentence_split | email_quote | head | 1 |
| 1 | synthetic_injection | exfiltrate_secret | multi_sentence_split | email_quote | middle | 4 |
| 1 | synthetic_injection | exfiltrate_secret | multi_sentence_split | email_quote | tail | 1 |
| 1 | synthetic_injection | exfiltrate_secret | naive | json_tool_response | head | 2 |
| 1 | synthetic_injection | exfiltrate_secret | naive | json_tool_response | middle | 4 |
| 1 | synthetic_injection | exfiltrate_secret | naive | json_tool_response | tail | 3 |
| 1 | synthetic_injection | exfiltrate_secret | obfuscated | email_quote | head | 2 |
| 1 | synthetic_injection | exfiltrate_secret | obfuscated | email_quote | middle | 3 |
| 1 | synthetic_injection | exfiltrate_secret | obfuscated | html_hidden | head | 1 |
| 1 | synthetic_injection | exfiltrate_secret | obfuscated | html_hidden | middle | 2 |
| 1 | synthetic_injection | exfiltrate_secret | obfuscated | visible_body | tail | 1 |
| 1 | synthetic_injection | exfiltrate_secret | polite_subtle | json_tool_response | head | 2 |
| 1 | synthetic_injection | exfiltrate_secret | polite_subtle | json_tool_response | middle | 1 |
| 1 | synthetic_injection | exfiltrate_secret | polite_subtle | json_tool_response | tail | 1 |
| 1 | synthetic_injection | exfiltrate_secret | role_play | email_quote | head | 1 |
| 1 | synthetic_injection | exfiltrate_secret | role_play | email_quote | middle | 1 |
| 1 | synthetic_injection | exfiltrate_secret | role_play | email_quote | tail | 3 |
| 1 | synthetic_injection | exfiltrate_secret | role_play | markdown_table_cell | middle | 1 |
| 1 | synthetic_injection | exfiltrate_secret | role_play | markdown_table_cell | tail | 2 |
| 1 | synthetic_injection | exfiltrate_secret | role_play | pdf_footer_header | middle | 1 |
| 1 | synthetic_injection | exfiltrate_secret | role_play | pdf_footer_header | tail | 1 |
| 1 | synthetic_injection | extra_transfer | authority_impersonation | email_quote | middle | 2 |
| 1 | synthetic_injection | extra_transfer | combined | email_quote | middle | 1 |
| 1 | synthetic_injection | extra_transfer | combined | email_quote | tail | 3 |
| 1 | synthetic_injection | extra_transfer | combined | json_tool_response | head | 2 |
| 1 | synthetic_injection | extra_transfer | combined | json_tool_response | middle | 1 |
| 1 | synthetic_injection | extra_transfer | escape_chars | email_quote | middle | 2 |
| 1 | synthetic_injection | extra_transfer | escape_chars | email_quote | tail | 1 |
| 1 | synthetic_injection | extra_transfer | fake_completion | json_tool_response | head | 3 |
| 1 | synthetic_injection | extra_transfer | fake_completion | json_tool_response | middle | 3 |
| 1 | synthetic_injection | extra_transfer | fake_completion | json_tool_response | tail | 1 |
| 1 | synthetic_injection | extra_transfer | multi_sentence_split | email_quote | head | 2 |
| 1 | synthetic_injection | extra_transfer | multi_sentence_split | email_quote | middle | 2 |
| 1 | synthetic_injection | extra_transfer | multi_sentence_split | email_quote | tail | 4 |
| 1 | synthetic_injection | extra_transfer | multi_sentence_split | json_tool_response | head | 3 |
| 1 | synthetic_injection | extra_transfer | multi_sentence_split | json_tool_response | middle | 3 |
| 1 | synthetic_injection | extra_transfer | naive | json_tool_response | middle | 1 |
| 1 | synthetic_injection | extra_transfer | naive | json_tool_response | tail | 1 |
| 1 | synthetic_injection | extra_transfer | obfuscated | html_comment | head | 1 |
| 1 | synthetic_injection | extra_transfer | obfuscated | html_comment | tail | 1 |
| 1 | synthetic_injection | extra_transfer | obfuscated | html_hidden | head | 1 |
| 1 | synthetic_injection | extra_transfer | obfuscated | html_hidden | middle | 2 |
| 1 | synthetic_injection | extra_transfer | obfuscated | html_hidden | tail | 2 |
| 1 | synthetic_injection | extra_transfer | obfuscated | pdf_footer_header | head | 1 |
| 1 | synthetic_injection | extra_transfer | obfuscated | pdf_footer_header | middle | 2 |
| 1 | synthetic_injection | extra_transfer | obfuscated | pdf_footer_header | tail | 1 |
| 1 | synthetic_injection | extra_transfer | obfuscated | visible_body | middle | 1 |
| 1 | synthetic_injection | extra_transfer | role_play | email_quote | head | 3 |
| 1 | synthetic_injection | extra_transfer | role_play | email_quote | middle | 1 |
| 1 | synthetic_injection | extra_transfer | role_play | email_quote | tail | 1 |
| 1 | synthetic_injection | extra_transfer | role_play | img_alt | middle | 1 |
| 1 | synthetic_injection | extra_transfer | role_play | img_alt | tail | 1 |
| 1 | synthetic_injection | extra_transfer | role_play | markdown_table_cell | middle | 3 |
| 1 | synthetic_injection | fake_user_approval | authority_impersonation | email_quote | middle | 1 |
| 1 | synthetic_injection | fake_user_approval | combined | email_quote | head | 1 |
| 1 | synthetic_injection | fake_user_approval | combined | email_quote | middle | 3 |
| 1 | synthetic_injection | fake_user_approval | escape_chars | json_tool_response | head | 1 |
| 1 | synthetic_injection | fake_user_approval | escape_chars | json_tool_response | middle | 1 |
| 1 | synthetic_injection | fake_user_approval | escape_chars | json_tool_response | tail | 2 |
| 1 | synthetic_injection | fake_user_approval | ignore_previous | json_tool_response | middle | 4 |
| 1 | synthetic_injection | fake_user_approval | ignore_previous | json_tool_response | tail | 1 |
| 1 | synthetic_injection | fake_user_approval | multi_sentence_split | email_quote | head | 1 |
| 1 | synthetic_injection | fake_user_approval | multi_sentence_split | email_quote | middle | 3 |
| 1 | synthetic_injection | fake_user_approval | multi_sentence_split | email_quote | tail | 1 |
| 1 | synthetic_injection | fake_user_approval | naive | email_quote | head | 1 |
| 1 | synthetic_injection | fake_user_approval | naive | json_tool_response | middle | 1 |
| 1 | synthetic_injection | fake_user_approval | obfuscated | html_hidden | middle | 2 |
| 1 | synthetic_injection | fake_user_approval | obfuscated | img_alt | head | 2 |
| 1 | synthetic_injection | fake_user_approval | obfuscated | img_alt | middle | 1 |
| 1 | synthetic_injection | fake_user_approval | obfuscated | markdown_table_cell | head | 1 |
| 1 | synthetic_injection | fake_user_approval | obfuscated | markdown_table_cell | middle | 1 |
| 1 | synthetic_injection | fake_user_approval | obfuscated | markdown_table_cell | tail | 2 |
| 1 | synthetic_injection | fake_user_approval | obfuscated | pdf_footer_header | head | 2 |
| 1 | synthetic_injection | fake_user_approval | obfuscated | visible_body | head | 2 |
| 1 | synthetic_injection | fake_user_approval | polite_subtle | json_tool_response | head | 3 |
| 1 | synthetic_injection | fake_user_approval | polite_subtle | json_tool_response | middle | 2 |
| 1 | synthetic_injection | fake_user_approval | role_play | email_quote | middle | 5 |
| 1 | synthetic_injection | fake_user_approval | role_play | email_quote | tail | 3 |
| 1 | synthetic_injection | goal_hijack_generic | authority_impersonation | json_tool_response | head | 2 |
| 1 | synthetic_injection | goal_hijack_generic | escape_chars | email_quote | head | 1 |
| 1 | synthetic_injection | goal_hijack_generic | escape_chars | email_quote | tail | 1 |
| 1 | synthetic_injection | goal_hijack_generic | escape_chars | json_tool_response | head | 1 |
| 1 | synthetic_injection | goal_hijack_generic | fake_completion | json_tool_response | head | 1 |
| 1 | synthetic_injection | goal_hijack_generic | fake_completion | json_tool_response | middle | 5 |
| 1 | synthetic_injection | goal_hijack_generic | fake_completion | json_tool_response | tail | 5 |
| 1 | synthetic_injection | goal_hijack_generic | ignore_previous | json_tool_response | head | 1 |
| 1 | synthetic_injection | goal_hijack_generic | ignore_previous | json_tool_response | middle | 1 |
| 1 | synthetic_injection | goal_hijack_generic | ignore_previous | json_tool_response | tail | 2 |
| 1 | synthetic_injection | goal_hijack_generic | multi_sentence_split | email_quote | head | 3 |
| 1 | synthetic_injection | goal_hijack_generic | multi_sentence_split | email_quote | middle | 3 |
| 1 | synthetic_injection | goal_hijack_generic | naive | json_tool_response | middle | 2 |
| 1 | synthetic_injection | goal_hijack_generic | obfuscated | html_hidden | middle | 5 |
| 1 | synthetic_injection | goal_hijack_generic | obfuscated | html_hidden | tail | 2 |
| 1 | synthetic_injection | goal_hijack_generic | obfuscated | json_tool_response | middle | 4 |
| 1 | synthetic_injection | goal_hijack_generic | obfuscated | json_tool_response | tail | 1 |
| 1 | synthetic_injection | goal_hijack_generic | obfuscated | markdown_table_cell | tail | 1 |
| 1 | synthetic_injection | goal_hijack_generic | obfuscated | visible_body | head | 1 |
| 1 | synthetic_injection | goal_hijack_generic | obfuscated | visible_body | middle | 1 |
| 1 | synthetic_injection | goal_hijack_generic | polite_subtle | json_tool_response | head | 1 |
| 1 | synthetic_injection | goal_hijack_generic | polite_subtle | json_tool_response | middle | 1 |
| 1 | synthetic_injection | goal_hijack_generic | polite_subtle | json_tool_response | tail | 1 |
| 1 | synthetic_injection | goal_hijack_generic | role_play | email_quote | head | 5 |
| 1 | synthetic_injection | goal_hijack_generic | role_play | email_quote | middle | 3 |
| 1 | synthetic_injection | goal_hijack_generic | role_play | email_quote | tail | 4 |
| 1 | synthetic_injection | out_of_scope_action | combined | email_quote | middle | 2 |
| 1 | synthetic_injection | out_of_scope_action | combined | email_quote | tail | 2 |
| 1 | synthetic_injection | out_of_scope_action | combined | json_tool_response | head | 2 |
| 1 | synthetic_injection | out_of_scope_action | combined | json_tool_response | tail | 1 |
| 1 | synthetic_injection | out_of_scope_action | escape_chars | email_quote | middle | 1 |
| 1 | synthetic_injection | out_of_scope_action | escape_chars | json_tool_response | head | 2 |
| 1 | synthetic_injection | out_of_scope_action | escape_chars | json_tool_response | middle | 1 |
| 1 | synthetic_injection | out_of_scope_action | escape_chars | json_tool_response | tail | 1 |
| 1 | synthetic_injection | out_of_scope_action | ignore_previous | json_tool_response | tail | 2 |
| 1 | synthetic_injection | out_of_scope_action | multi_sentence_split | email_quote | head | 4 |
| 1 | synthetic_injection | out_of_scope_action | multi_sentence_split | email_quote | tail | 1 |
| 1 | synthetic_injection | out_of_scope_action | multi_sentence_split | json_tool_response | head | 1 |
| 1 | synthetic_injection | out_of_scope_action | multi_sentence_split | json_tool_response | middle | 1 |
| 1 | synthetic_injection | out_of_scope_action | naive | json_tool_response | head | 1 |
| 1 | synthetic_injection | out_of_scope_action | naive | json_tool_response | middle | 1 |
| 1 | synthetic_injection | out_of_scope_action | naive | json_tool_response | tail | 2 |
| 1 | synthetic_injection | out_of_scope_action | obfuscated | html_hidden | middle | 2 |
| 1 | synthetic_injection | out_of_scope_action | role_play | email_quote | head | 2 |
| 1 | synthetic_injection | out_of_scope_action | role_play | email_quote | middle | 3 |
| 1 | synthetic_injection | out_of_scope_action | role_play | email_quote | tail | 1 |
| 1 | synthetic_injection | redirect_recipient | combined | email_quote | head | 3 |
| 1 | synthetic_injection | redirect_recipient | combined | email_quote | middle | 7 |
| 1 | synthetic_injection | redirect_recipient | escape_chars | json_tool_response | head | 1 |
| 1 | synthetic_injection | redirect_recipient | escape_chars | json_tool_response | middle | 3 |
| 1 | synthetic_injection | redirect_recipient | escape_chars | json_tool_response | tail | 1 |
| 1 | synthetic_injection | redirect_recipient | ignore_previous | email_quote | middle | 2 |
| 1 | synthetic_injection | redirect_recipient | ignore_previous | email_quote | tail | 2 |
| 1 | synthetic_injection | redirect_recipient | ignore_previous | json_tool_response | middle | 2 |
| 1 | synthetic_injection | redirect_recipient | obfuscated | email_quote | head | 1 |
| 1 | synthetic_injection | redirect_recipient | obfuscated | email_quote | tail | 1 |
| 1 | synthetic_injection | redirect_recipient | obfuscated | html_comment | head | 1 |
| 1 | synthetic_injection | redirect_recipient | obfuscated | html_comment | middle | 1 |
| 1 | synthetic_injection | redirect_recipient | obfuscated | html_comment | tail | 1 |
| 1 | synthetic_injection | redirect_recipient | obfuscated | img_alt | middle | 2 |
| 1 | synthetic_injection | redirect_recipient | obfuscated | img_alt | tail | 1 |
| 1 | synthetic_injection | redirect_recipient | obfuscated | json_tool_response | tail | 1 |
| 1 | synthetic_injection | redirect_recipient | obfuscated | pdf_footer_header | head | 1 |
| 1 | synthetic_injection | redirect_recipient | polite_subtle | email_quote | middle | 3 |
| 1 | synthetic_injection | redirect_recipient | polite_subtle | email_quote | tail | 2 |
| 1 | synthetic_injection | redirect_recipient | role_play | img_alt | head | 1 |
| 1 | synthetic_injection | redirect_recipient | role_play | markdown_table_cell | middle | 1 |
| 1 | synthetic_injection | redirect_recipient | role_play | markdown_table_cell | tail | 1 |
| 1 | synthetic_injection | redirect_recipient | role_play | pdf_footer_header | head | 3 |
| 1 | synthetic_injection | redirect_recipient | role_play | pdf_footer_header | middle | 3 |
| 1 | synthetic_injection | redirect_recipient | role_play | pdf_footer_header | tail | 1 |
| 1 | synthetic_injection | suppress_confirmation | authority_impersonation | json_tool_response | head | 2 |
| 1 | synthetic_injection | suppress_confirmation | authority_impersonation | json_tool_response | middle | 3 |
| 1 | synthetic_injection | suppress_confirmation | authority_impersonation | json_tool_response | tail | 2 |
| 1 | synthetic_injection | suppress_confirmation | combined | email_quote | middle | 2 |
| 1 | synthetic_injection | suppress_confirmation | combined | email_quote | tail | 2 |
| 1 | synthetic_injection | suppress_confirmation | ignore_previous | json_tool_response | head | 2 |
| 1 | synthetic_injection | suppress_confirmation | ignore_previous | json_tool_response | middle | 1 |
| 1 | synthetic_injection | suppress_confirmation | multi_sentence_split | json_tool_response | head | 3 |
| 1 | synthetic_injection | suppress_confirmation | naive | json_tool_response | head | 1 |
| 1 | synthetic_injection | suppress_confirmation | naive | json_tool_response | middle | 2 |
| 1 | synthetic_injection | suppress_confirmation | naive | json_tool_response | tail | 1 |
| 1 | synthetic_injection | suppress_confirmation | obfuscated | email_quote | head | 1 |
| 1 | synthetic_injection | suppress_confirmation | obfuscated | email_quote | middle | 3 |
| 1 | synthetic_injection | suppress_confirmation | obfuscated | html_hidden | middle | 1 |
| 1 | synthetic_injection | suppress_confirmation | obfuscated | pdf_footer_header | tail | 3 |
| 1 | synthetic_injection | suppress_confirmation | polite_subtle | email_quote | head | 1 |
| 1 | synthetic_injection | suppress_confirmation | polite_subtle | email_quote | middle | 1 |
| 1 | synthetic_injection | suppress_confirmation | polite_subtle | email_quote | tail | 1 |
| 1 | synthetic_injection | suppress_confirmation | role_play | email_quote | tail | 1 |
| 1 | synthetic_injection | suppress_confirmation | role_play | html_comment | middle | 1 |
| 1 | synthetic_injection | suppress_confirmation | role_play | html_comment | tail | 1 |
| 1 | synthetic_injection | suppress_confirmation | role_play | json_tool_response | middle | 3 |
| 1 | synthetic_injection | suppress_confirmation | role_play | json_tool_response | tail | 1 |
| 1 | synthetic_injection | suppress_confirmation | role_play | markdown_table_cell | tail | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | authority_impersonation | email_quote | head | 2 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | authority_impersonation | email_quote | middle | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | authority_impersonation | email_quote | tail | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | combined | email_quote | head | 3 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | combined | email_quote | middle | 3 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | combined | email_quote | tail | 2 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | escape_chars | json_tool_response | head | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | ignore_previous | email_quote | middle | 2 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | ignore_previous | json_tool_response | head | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | ignore_previous | json_tool_response | middle | 2 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | ignore_previous | json_tool_response | tail | 2 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | multi_sentence_split | email_quote | middle | 5 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | multi_sentence_split | email_quote | tail | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | naive | json_tool_response | head | 2 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | naive | json_tool_response | middle | 3 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | obfuscated | json_tool_response | head | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | obfuscated | json_tool_response | middle | 7 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | obfuscated | json_tool_response | tail | 2 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | obfuscated | pdf_footer_header | middle | 2 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | obfuscated | visible_body | head | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | obfuscated | visible_body | middle | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | obfuscated | visible_body | tail | 2 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | polite_subtle | json_tool_response | head | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | polite_subtle | json_tool_response | middle | 3 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | polite_subtle | json_tool_response | tail | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | role_play | email_quote | head | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | role_play | email_quote | middle | 3 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | role_play | html_hidden | middle | 2 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | role_play | markdown_table_cell | head | 1 |
| 1 | synthetic_injection | unauthorized_typed_data_sign | role_play | markdown_table_cell | middle | 1 |
| null | crypto_prose | null | null | null | null | 66 |
| null | hard_negative | null | null | null | null | 499 |

Whitespace token-length histogram: {"0-16": 915, "129+": 0, "17-32": 328, "33-64": 0, "65-128": 0}

## dev_ood_crai
Segments: 920; mean characters: 175.0

| Label | Source | Count |
|---:|---|---:|
| 0 | crai | 475 |
| 1 | crai | 445 |

### goal counts
- null: 920

### style counts
- null: 920

### carrier counts
- null: 920

### position counts
- null: 920

### Joint label/source/goal/style/carrier/position counts
| Label | Source | Goal | Style | Carrier | Position | Count |
|---:|---|---|---|---|---|---:|
| 1 | crai | null | null | null | null | 445 |
| null | crai | null | null | null | null | 475 |

Whitespace token-length histogram: {"0-16": 308, "129+": 0, "17-32": 322, "33-64": 289, "65-128": 1}

## test_ood_crai
Segments: 2233; mean characters: 173.3

| Label | Source | Count |
|---:|---|---:|
| 0 | crai | 1100 |
| 1 | crai | 1133 |

### goal counts
- null: 2233

### style counts
- null: 2233

### carrier counts
- null: 2233

### position counts
- null: 2233

### Joint label/source/goal/style/carrier/position counts
| Label | Source | Goal | Style | Carrier | Position | Count |
|---:|---|---|---|---|---|---:|
| 1 | crai | null | null | null | null | 1133 |
| null | crai | null | null | null | null | 1100 |

Whitespace token-length histogram: {"0-16": 789, "129+": 0, "17-32": 728, "33-64": 714, "65-128": 2}

## train_crai
Segments: 3259; mean characters: 173.4

| Label | Source | Count |
|---:|---|---:|
| 0 | crai | 1604 |
| 1 | crai | 1655 |

### goal counts
- null: 3259

### style counts
- null: 3259

### carrier counts
- null: 3259

### position counts
- null: 3259

### Joint label/source/goal/style/carrier/position counts
| Label | Source | Goal | Style | Carrier | Position | Count |
|---:|---|---|---|---|---|---:|
| 1 | crai | null | null | null | null | 1655 |
| null | crai | null | null | null | null | 1604 |

Whitespace token-length histogram: {"0-16": 1134, "129+": 0, "17-32": 1077, "33-64": 1042, "65-128": 6}

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
