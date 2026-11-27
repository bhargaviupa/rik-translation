# Vol 7 second pass — status report
*Made by `python3 tools/rv/sp_report.py 7` from `findings.tsv`, `questions.tsv`, `batches.tsv`, `open.tsv`; updated 2026-11-27. Format: `docs/SECOND_PASS_REPORT.md`.*

## 1. State
- **Stage:** S2 reading in page batches
- **Pages read:** 75 (1–75)
- **Findings:** 146 — applied 94, kept/not applied 52 (English kept: misprints and doubts settled by rule; see part 5); edits ok 94, failed 0
- **Reader tokens (batches so far):** 243k; per page 3.2k
- **Last commit:** 856b8f44

## 2. Batches
| Batch | Pages | Findings | Applied | Edits ok / failed | Kept / not applied | Tokens | Commit | Note |
|---|---|---|---|---|---|---|---|---|
| 1 | 1–75 | 146 | 94 | 94 / 0 | 52 | 243k | 856b8f44 | marks q12-q161: 150 seen, 98 removed, 52 kept |

## 3. Findings by kind
| Kind | Applied | Kept / not applied | Total |
|---|---|---|---|
| Q2 | 19 | 52 | 71 |
| Q1 | 70 | 0 | 70 |
| S3 | 5 | 0 | 5 |

By reader: R1 146

## 4. Open items (not findings)
- none recorded

## 5. Questions for the editor
**0 open questions** in `questions.tsv` (the editor decides only what the rules cannot: nothing else is asked).

Settled by rule, no reading needed: 7 Kannada misprints where the English is kept (`kn_misprints.tsv`); 45 places where the English is kept unchanged and listed for the scholar sample (`decided_by_default.tsv`). Impossible or odd printed numbers applied as printed are in part 4.

## 6. Files
`vol7/review/second_pass/findings.tsv` · `questions.tsv` · `batches.tsv` · `open.tsv` · `edits/` (edit files and results) · `../repair_log.md` (every English repair, heading "second pass") · `../../data/source_fixes.tsv` (edits of the supplied Kannada)

## 7. Next
the next page batch; then S3 totals (re-run the S0 checks), S4 coverage, S5 pictures, S6 records
