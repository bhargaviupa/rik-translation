# Vol 1 second pass — status report
*Made by `python3 tools/rv/sp_report.py 1` from `findings.tsv`, `questions.tsv`, `batches.tsv`, `open.tsv`; updated 2026-11-24. Format: `docs/SECOND_PASS_REPORT.md`.*

## 1. State
- **Stage:** S2 reading in page batches
- **Pages read:** 10 of 720 (360–369)
- **Findings:** 73 — applied 52, questions 21; edits ok 31, failed 0
- **Reader tokens (batches so far):** 169k; per page 16.9k
- **Last commit:** f594e7e

## 2. Batches
| Batch | Pages | Findings | Applied | Edits ok / failed | Questions | Tokens | Commit | Note |
|---|---|---|---|---|---|---|---|---|
| pilot | 360–369 | 73 | 52 | 31 / 0 | 21 | 169k | f594e7e | pilot; 52 edits first applied, then 21 Devanagari edits (and 6 IAST partners) reverted by the new sp_sanskrit gate, 6 re-applied after the word-join refinement: net 31 English edits stand; 15 citation lines are questions; English not page-aligned to the Kannada on these pages (judged by content) |

## 3. Findings by kind
| Kind | Applied | Questions | Total |
|---|---|---|---|
| S7 | 48 | 15 | 63 |
| H29 | 0 | 5 | 5 |
| S14 | 3 | 0 | 3 |
| S1 | 1 | 0 | 1 |
| S17 | 0 | 1 | 1 |

By reader: R1 6, R3 62, R6 5

## 4. Open items (not findings)
- none recorded

## 5. Questions for the editor
11 rows in `questions.tsv`; by kind: H29 5, S17 1, S7 15

## 6. Files
`vol1/review/second_pass/findings.tsv` · `questions.tsv` · `batches.tsv` · `open.tsv` · `edits/` (edit files and results) · `../repair_log.md` (every English repair, heading "second pass") · `../../data/source_fixes.tsv` (edits of the supplied Kannada)

## 7. Next
the next page batch; then S3 totals (re-run the S0 checks), S4 coverage, S5 pictures, S6 records
