# Vol 8 second pass — status report
*Made by `python3 tools/rv/sp_report.py 8` from `findings.tsv`, `questions.tsv`, `batches.tsv`, `open.tsv`; updated 2026-11-27. Format: `docs/SECOND_PASS_REPORT.md`.*

## 1. State
- **Stage:** S2 reading in page batches
- **Pages read:** 40 (550–559, 2–31)
- **Findings:** 166 — applied 102, kept/not applied 64 (English kept: misprints and doubts settled by rule; see part 5); edits ok 90, failed 0
- **Reader tokens (batches so far):** 362k; per page 9.1k
- **Last commit:** eab0f49c

## 2. Batches
| Batch | Pages | Findings | Applied | Edits ok / failed | Kept / not applied | Tokens | Commit | Note |
|---|---|---|---|---|---|---|---|---|
| 1 | 550–559 | 87 | 62 | 50 / 0 | 25 | 139k | d7e7d422 | pilot; 81 [?] seen, 59 removed (36 corrected), 22 kept |
| 2 | 2–31 | 79 | 40 | 40 / 0 | 39 | 223k | eab0f49c | 79 [?] seen, 40 removed (26 corrected), 39 kept |

## 3. Findings by kind
| Kind | Applied | Kept / not applied | Total |
|---|---|---|---|
| Q2 | 37 | 61 | 98 |
| Q1 | 58 | 0 | 58 |
| S2 | 5 | 0 | 5 |
| S1 | 2 | 0 | 2 |
| S7 | 0 | 2 | 2 |
| S13 | 0 | 1 | 1 |

By reader: R1 163, R3 2, R6 1

## 4. Open items (not findings)
- none recorded

## 5. Questions for the editor
**0 open questions** in `questions.tsv` (the editor decides only what the rules cannot: nothing else is asked).

Settled by rule, no reading needed: 11 Kannada misprints where the English is kept (`kn_misprints.tsv`); 6 places where the English is kept unchanged and listed for the scholar sample (`decided_by_default.tsv`). Impossible or odd printed numbers applied as printed are in part 4.

## 6. Files
`vol8/review/second_pass/findings.tsv` · `questions.tsv` · `batches.tsv` · `open.tsv` · `edits/` (edit files and results) · `../repair_log.md` (every English repair, heading "second pass") · `../../data/source_fixes.tsv` (edits of the supplied Kannada)

## 7. Next
the next page batch; then S3 totals (re-run the S0 checks), S4 coverage, S5 pictures, S6 records
