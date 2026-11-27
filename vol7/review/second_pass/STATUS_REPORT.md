# Vol 7 second pass — status report
*Made by `python3 tools/rv/sp_report.py 7` from `findings.tsv`, `questions.tsv`, `batches.tsv`, `open.tsv`; updated 2026-11-27. Format: `docs/SECOND_PASS_REPORT.md`.*

## 1. State
- **Stage:** S2 reading in page batches
- **Pages read:** 213 (1–75, 76–145, 145–213)
- **Findings:** 438 — applied 330, kept/not applied 108 (English kept: misprints and doubts settled by rule; see part 5); edits ok 329, failed 0
- **Reader tokens (batches so far):** 752k; per page 3.5k
- **Last commit:** bfbab262

## 2. Batches
| Batch | Pages | Findings | Applied | Edits ok / failed | Kept / not applied | Tokens | Commit | Note |
|---|---|---|---|---|---|---|---|---|
| 1 | 1–75 | 146 | 94 | 94 / 0 | 52 | 243k | 856b8f44 | marks q12-q161: 150 seen, 98 removed, 52 kept |
| 2 | 76–145 | 142 | 94 | 94 / 0 | 48 | 239k | e9bd4eef | marks q64-q213: 150 seen, 102 removed, 48 kept |
| 3 | 145–213 | 155 | 147 | 141 / 0 | 8 | 270k | bfbab262 | marks q112-q261: 150 seen, 139 removed, 11 kept |

## 3. Findings by kind
| Kind | Applied | Kept / not applied | Total |
|---|---|---|---|
| Q2 | 102 | 108 | 210 |
| Q1 | 201 | 0 | 201 |
| S3 | 27 | 0 | 27 |

By reader: R1 438

## 4. Open items (not findings)
- none recorded

## 5. Questions for the editor
**0 open questions** in `questions.tsv` (the editor decides only what the rules cannot: nothing else is asked).

Settled by rule, no reading needed: 21 Kannada misprints where the English is kept (`kn_misprints.tsv`); 88 places where the English is kept unchanged and listed for the scholar sample (`decided_by_default.tsv`). Impossible or odd printed numbers applied as printed are in part 4.

## 6. Files
`vol7/review/second_pass/findings.tsv` · `questions.tsv` · `batches.tsv` · `open.tsv` · `edits/` (edit files and results) · `../repair_log.md` (every English repair, heading "second pass") · `../../data/source_fixes.tsv` (edits of the supplied Kannada)

## 7. Next
the next page batch; then S3 totals (re-run the S0 checks), S4 coverage, S5 pictures, S6 records
