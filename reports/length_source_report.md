# Word-length diagnostics

Word counts are whitespace token counts. Length-only accuracy is measured with stratified 75/25 holdout within each group.

- Deduplication: normalized exact-hash only (datasketch MinHash LSH is unavailable; exact fallback used).

## Full train before length matching: source diagnosis

| Source | Rows | Clean mean | Clean median | Injected mean | Injected median | KS D | KS p | Length-only accuracy |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| boundary pairs | 52 | 39.00 | 39.0 | 28.79 | 28.0 | 0.9167 | 0.00121925 | 0.9231 |
| crypto prose | 131 | 9.44 | 9.0 | 0.00 | 0.0 | 1.0000 | 0 | 1.0000 |
| general prose | 0 | 0.00 | 0.0 | 0.00 | 0.0 | 1.0000 | 0 | 1.0000 |
| hard cases | 0 | 0.00 | 0.0 | 0.00 | 0.0 | 1.0000 | 0 | 1.0000 |
| paired docs | 4591 | 14.96 | 16.0 | 12.85 | 13.0 | 0.3521 | 2.80879e-104 | 0.7308 |

## Final full train by source

| Source | Rows | Clean mean | Clean median | Injected mean | Injected median | KS D | KS p | Length-only accuracy |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| boundary pairs | 36 | 39.00 | 39.0 | 29.31 | 28.5 | 0.8750 | 0.00293856 | 0.8889 |
| crypto prose | 0 | 0.00 | 0.0 | 0.00 | 0.0 | 1.0000 | 0 | 1.0000 |
| general prose | 0 | 0.00 | 0.0 | 0.00 | 0.0 | 1.0000 | 0 | 1.0000 |
| hard cases | 0 | 0.00 | 0.0 | 0.00 | 0.0 | 1.0000 | 0 | 1.0000 |
| paired docs | 2460 | 14.73 | 15.0 | 14.43 | 15.0 | 0.0209 | 0.949001 | 0.4927 |

## Effect-size gates by split

| Split | Rows | KS D | KS p (informational) | Length-only accuracy |
|---|---:|---:|---:|---:|
| train | 2496 | 0.0000 | 1 | 0.4856 |
| val | 190 | 0.0000 | 1 | 0.4167 |
| test_id | 426 | 0.0000 | 1 | 0.4722 |
| test_heldout | 1243 | 0.0705 | 0.089387 | 0.5385 |
