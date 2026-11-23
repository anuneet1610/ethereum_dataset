# Prompt-Injection Segment Classifier: Dataset and Fine-Tuning Report

Nov 21, 2026 · @IIT\_2792

## Overview

The fine-tuned classifier detects 94.9% of injected segments on a held-out CrAI test set at a 3.4% false-positive rate, while the off-the-shelf model it started from caught 26.6% on an earlier version of that test set.

It sits in the wallet access layer, directly after the tool that extracts text from documents and webpages. It follows the segmentation-removal method of Chen et al. (ACL 2025):

1. Split the extracted text into sentence-level segments.
2. Classify each segment as clean or injected.
3. Drop injected segments and pass the rest to the LLM.

The same classifier also screens the user's own prompt as a whole. On that path it flags the prompt and asks the user to clarify instead of removing text. The classifier is one defence layer; access-layer checks (untrusted addresses, spending limits, explicit confirmation of every signature) apply whether or not it fires.

## Threat model and labels

A segment is labelled injected when it tries to steer the agent beyond what the user asked; legitimate payment instructions for a human reader stay clean.

The system supports four wallet functions: transfers, balance checks, transaction history and EIP-712 typed-data signing. Attacks arrive in documents, webpages and tool responses that the user asks the agent to act on.

A segment is **injected** if either condition holds:

- **Agent-directed:** it addresses or impersonates an assistant, agent, automated processor or system, and tries to change its behaviour.
- **Inherently malicious:** whoever it addresses, it asks for seed phrases or private keys, a balance sweep, new permissions or limits, an unrequested signature, skipped or faked confirmation, or private wallet data sent to a third party.

A segment is **clean** if it is ordinary content, including instructions meant for the human reader, such as an invoice line asking for payment. Two deliberate hard cases are labelled clean and tagged for analysis, because the access layer rather than the classifier handles them:

- `bare_address_claim`: a plain statement that a payee address has changed, with no agent-directed wording.
- `human_phishing`: phishing aimed at a human reader with no instruction to the agent.

## Dataset generation

The dataset pairs every clean document with an injected copy of itself, so the inserted attack is the only thing that separates the two labels.

It is built by a reproducible Python pipeline (one command, fixed seeds) from hand-written seeds, then combined with a slice of the public CrAI-SafeFuncCall dataset.

1. **Seed attacks.** Over 300 hand-written injection templates, each tagged with a goal, a style and the carriers it fits. Goals cover the wallet threats: recipient redirect, amount change, extra transfer, balance drain, unauthorized typed-data signature, secret and private-data exfiltration, suppressed or faked confirmation, permission escalation, out-of-scope actions and generic goal hijacking. Styles include naive, ignore-previous, fake completion, escape characters, authority impersonation, polite or subtle, multi-sentence split, obfuscated (per-sample base64) and role play.
2. **Hard negatives.** Legitimate documents that look action-oriented: invoices, receipts, rent splits, payroll notes, refunds, balance statements and legitimate signing requests. They include attack-sounding words used innocently, such as "Please ignore the earlier draft; this invoice supersedes it."
3. **Slot filling and paraphrase.** Each seed is filled with a fresh random EIP-55 address, ENS name, token and amount, then paraphrased by a local model for variety. Phrases that became generator tics are banned.
4. **Paired assembly.** A base document is rendered once clean and once with the injection inserted at the head, middle or tail. Both versions share the same carrier wrapper (hidden HTML text, comments, alt text, PDF footers, markdown tables, JSON tool responses, email quotes) and whitespace, and are flattened the way the text extractor would output them.
5. **Segmentation and labelling.** A shared sentence splitter, the same module used at inference, cuts each document into segments. Only the sentences of the inserted attack are labelled injected.
6. **Splits.** Pairs are grouped by base document, so both versions always land in the same split. `test_heldout` holds out whole attack families (obfuscated and role-play styles, JSON and email carriers, permission escalation) never seen in training.
7. **Real outside data.** CrAI-SafeFuncCall memory texts are split by `source_id` into train (50%), dev (15%) and test (35%) with no overlap and the natural label ratio. Payload sentences are labelled injected, and giveaway tool names are replaced with realistic ones.
8. **Quality checks.** Every build runs deduplication, address validation, a giveaway-word scan, a leakage check across splits, and a shortcut probe. The probe requires a length-only classifier to stay at chance (KS D ≤ 0.10, accuracy ≤ 0.60) and lists the words a TF-IDF classifier relies on, so template artifacts are caught before training.

The final synthetic set has 2,496 training segments (about half injected), plus 3,259 CrAI training segments.

## Fine-tuning

The model is DeBERTa-v3-base, fine-tuned for binary classification on single segments, with the checkpoint chosen on outside data (CrAI dev) and the threshold on the synthetic validation set.

- **Base model:** `protectai/deberta-v3-base-prompt-injection-v2` (Apache-2.0, ungated, runs on CPU). It already detects classic injection framing, so training adapts it to wallet-specific attacks.
- **Input:** the segment text alone, truncated to 256 tokens. Neighbouring sentences are not included, so an attack never spills into the classification of the clean sentences beside it.
- **Training data:** synthetic train plus CrAI train, shuffled together.
- **Settings:** learning rate 1e-5, 1 epoch (360 steps), batch size 16, 50 warmup steps, weight decay 0.01, fp16 on a single Colab T4 GPU (about 23 minutes including evaluation and checkpointing every 25 steps), seed 42.
- **Checkpoint selection:** the model is evaluated every 25 steps on CrAI dev (relevant attacks plus all clean rows), and the checkpoint with the best F1 is kept (F1 0.907 at step 275).
- **Decision threshold:** the threshold that maximises F1 on the synthetic validation set, subject to a false-positive rate of at most 2% on its hard negatives, so legitimate payments are not blocked: 0.96. The app currently runs at 0.98.

The saved model carries a `filter_config.json` with the threshold and settings. The access layer loads it through a `SegmentFilter` class that uses the same segmenter as the dataset build.

## Results

Adding real CrAI training data lifts CrAI-test detection from 44.0% to 94.9% and cuts its false positives from 31.5% to 3.4%, with synthetic-set performance unchanged.

| Model | Synthetic test detection (%) | Held-out families detection (%) | Held-out hard-negative FP (%) | CrAI test detection (%) | CrAI test FP (%) |
| --- | --- | --- | --- | --- | --- |
| **Synthetic + CrAI (deployed)** | 94.8 | 76.0 | 2.4 | 94.9 | 3.4 |
| Synthetic only | 92.5 | 75.7 | 1.2 | 44.0 | 31.5 |

Detection is the share of injected segments flagged; FP is the share of clean segments flagged. On an earlier, larger version of the CrAI test split, the off-the-shelf baselines scored: ProtectAI DeBERTa 26.6% detection at 27.9% FP, Llama Prompt Guard 2 86M 2.9% detection. Prompt Guard 2 targets explicit jailbreaks rather than indirect injection.

## Limitations and next steps

The CrAI-test figure measures attacks in a style the model has seen in training; the main open item is a test on attacks written independently of both data sources.

- **CrAI is now partly in-distribution.** Its train and test splits share a generator and an agent-memory style, so 94.9% overstates performance on unseen attack styles.
- **Held-out families are missed 24% of the time.** These are attack styles and carriers kept out of training, such as encoded payloads and JSON tool responses.
- **Clean text alone carries dates and invoice IDs.** An injection written to look like an invoice line may be missed.
- **Small synthetic train set** (2,496 segments) and no general-domain prose among the clean examples, so false positives on ordinary webpages may be higher than measured.

Next: evaluate on 100 hand-written red-team attacks against the four wallet functions, and measure the end-to-end attack success rate of the full agent with the filter on and off.
