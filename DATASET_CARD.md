# Dataset card: Ethereum wallet-agent prompt-injection segments

## Purpose and intended use

Train and evaluate segment classifiers that screen extracted webpage or document text before a natural-language agent can act through a wallet. The only supported wallet functions are ETH/ERC-20 transfers, balance lookup, transaction-history lookup, and EIP-712 typed-data signing. Intended for research on indirect prompt injection and defensive filtering, not as a substitute for wallet confirmation or transaction policy enforcement.

## Labels

`1` (injected) means a segment steers an AI, assistant, agent, automated processor, system, or tool, or requests an inherently unsafe action: secret disclosure, balance sweep, permission escalation, unrequested typed-data signing, confirmation bypass, fabricated approval, or private wallet-data exfiltration. `0` (clean) includes ordinary human-facing payment instructions, legitimate bounded signing contexts, and explanatory prose. Human-directed address-change claims (`bare_address_claim`) and human phishing (`human_phishing`) are clean hard cases. For split-sentence seed records, only listed sentence indices are injected.

## Sources and licenses

- SQuAD training contexts: CC BY-SA 4.0.
- TriviaQA `rc` Wikipedia contexts: Apache 2.0 (per the dataset card).
- Synthetic wallet/Ethereum prose, invoice-style hard negatives, and injection seeds: generated for this project; seed files were provided in the repository and are preserved unchanged.
- CrAI-SafeFuncCall (`SentientAGI/crypto-agent-safe-function-calling`): only used in `test_ood_crai`; consult the Hugging Face dataset card for its license and terms before redistribution.

## Generation

The pipeline fills the supplied 300 injection seeds, 60 boundary pairs, and 40 clean hard-case examples with deterministic synthetic slots; renders eight text carriers; flattens them as extracted text; and applies the shared regex sentence segmenter. Clean pools include 80 reviewed hard-negative templates, wallet-domain prose, and optional SQuAD/TriviaQA paragraphs. Seed and template groups stay within one split. Held-out styles, carriers, and one goal family are configurable. Optional Ollama paraphrases use a local endpoint and disk cache. CrAI-SafeFuncCall is required by default to populate the OOD split; `--skip-crai` explicitly omits it.

## Known limitations

Synthetic slots and carrier rendering cannot represent all real wallets, languages, PDF extraction failures, or adversarial obfuscations. SQuAD and TriviaQA are optional and may be unavailable; synthetic pools still run. If CrAI cannot load or contains no memory-injection rows, the default build stops with an error; use `--skip-crai` only when an empty external OOD split is intentional. The regex splitter is deliberately dependency-light and should be checked against production extractor output. A segment classifier can miss attacks or flag legitimate content; transaction confirmation, scoped permissions, and independent policy checks remain necessary.
