# Vol 8 second pass — status report
*Made by `python3 tools/rv/sp_report.py 8` from `findings.tsv`, `questions.tsv`, `batches.tsv`, `open.tsv`; updated 2026-11-27. Format: `docs/SECOND_PASS_REPORT.md`.*

## 1. State
- **Stage:** S2 reading in page batches
- **Pages read:** 130 (550–559, 2–31, 32–61, 62–91, 92–121)
- **Findings:** 319 — applied 165, kept/not applied 154 (English kept: misprints and doubts settled by rule; see part 5); edits ok 150, failed 0
- **Reader tokens (batches so far):** 759k; per page 5.8k
- **Last commit:** c2bfa8ce

## 2. Batches
| Batch | Pages | Findings | Applied | Edits ok / failed | Kept / not applied | Tokens | Commit | Note |
|---|---|---|---|---|---|---|---|---|
| 1 | 550–559 | 87 | 62 | 50 / 0 | 25 | 139k | d7e7d422 | pilot; 81 [?] seen, 59 removed (36 corrected), 22 kept |
| 2 | 2–31 | 79 | 40 | 40 / 0 | 39 | 223k | eab0f49c | 79 [?] seen, 40 removed (26 corrected), 39 kept |
| 3 | 32–61 | 47 | 18 | 16 / 0 | 29 | 134k | 337547ac | 47 [?] seen, 18 removed (16 corrected), 29 kept |
| 4 | 62–91 | 59 | 22 | 22 / 0 | 37 | 145k | 2f3b1d92 | 59 [?] seen, 22 removed (11 corrected), 37 kept |
| 5 | 92–121 | 47 | 23 | 22 / 0 | 24 | 118k | c2bfa8ce | 46 [?] seen, 22 removed (10 corrected), 24 kept |

## 3. Findings by kind
| Kind | Applied | Kept / not applied | Total |
|---|---|---|---|
| Q2 | 62 | 151 | 213 |
| Q1 | 95 | 0 | 95 |
| S2 | 6 | 0 | 6 |
| S1 | 2 | 0 | 2 |
| S7 | 0 | 2 | 2 |
| S13 | 0 | 1 | 1 |

By reader: R1 316, R3 2, R6 1

## 4. Open items (not findings)
- **other** (pages 118): Pā. Sū. 3-1-0 (Kannada p. 118 prints ೩-೧-೦, impossible sutra number); applied as printed

## 5. Questions for the editor
**0 open questions** in `questions.tsv` (the editor decides only what the rules cannot: nothing else is asked).

Settled by rule, no reading needed: 16 Kannada misprints where the English is kept (`kn_misprints.tsv`); 13 places where the English is kept unchanged and listed for the scholar sample (`decided_by_default.tsv`). Impossible or odd printed numbers applied as printed are in part 4.

## 6. Files
`vol8/review/second_pass/findings.tsv` · `questions.tsv` · `batches.tsv` · `open.tsv` · `edits/` (edit files and results) · `../repair_log.md` (every English repair, heading "second pass") · `../../data/source_fixes.tsv` (edits of the supplied Kannada)

## 7. Next
the next page batch; then S3 totals (re-run the S0 checks), S4 coverage, S5 pictures, S6 records
