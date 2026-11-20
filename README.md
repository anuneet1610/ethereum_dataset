# Ethereum wallet prompt-injection segment dataset

This repository builds a deterministic dataset for segment-level screening of text extracted from webpages and documents before it reaches a natural-language Ethereum wallet agent. The wallet scope is transfer, balance lookup, transaction-history lookup, and EIP-712 typed-data signing.

## Build

Use Python 3.10 or newer. Install the allowed dependencies with `python -m pip install -r requirements.txt` for the CrAI, SQuAD, and TriviaQA sources, HF loader, checksum validation, or Ollama paraphrase client.

From the repository root, run:

```console
python -m piidata.build --config configs/default.yaml
```

CrAI-SafeFuncCall is required by default. If it cannot be loaded or has no rows marked as memory injection, the build fails with a diagnostic instead of silently creating an empty OOD set. Pass `--skip-crai` only when intentionally omitting this source. That mode supports an offline synthetic build. SQuAD and TriviaQA paragraphs are included when the listed `datasets` dependency can access its cache or the Hub. Install `pyyaml` only if you replace the JSON-compatible default config with other YAML syntax. `eth-utils` enables checksum validation for hex addresses in external content. The Ollama paraphrase option additionally requires `requests` and a local Ollama endpoint:

```console
python -m piidata.build --config configs/default.yaml --paraphrase
```

The `--paraphrase` option uses `qwen2.5:7b-instruct` by default and caches responses under `cache/paraphrases/`. Run the shared segmenter using `piidata.segmenter.split_segments(text)`. Load outputs as a Hugging Face `DatasetDict` using `piidata.loader.load_dataset_dict(data_dir='data', use_context=True)`; this requires `datasets`.

## Outputs

- `data/<split>.jsonl`: one labeled segment per line.
- `data/docs_<split>.jsonl`: assembled document text and injection spans.
- `data/redteam_manual.jsonl`: empty manual challenge set with `redteam_manual_README.md`.
- `reports/stats.md`, `reports/samples.md`, `reports/crai_label_audit.csv`: QC summaries and review aids.

Default target sizes and held-out families are in `configs/default.yaml`. All random generators use the configured seed. Dataset access uses the local Hugging Face cache when available and otherwise follows the datasets library's Hub behavior.
