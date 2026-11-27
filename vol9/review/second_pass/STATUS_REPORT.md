# Vol 9 second pass — status report
*Made by `python3 tools/rv/sp_report.py 9` from `findings.tsv`, `questions.tsv`, `batches.tsv`, `open.tsv`; updated 2026-11-27. Format: `docs/SECOND_PASS_REPORT.md`.*

## 1. State
- **Stage:** S2 reading in page batches
- **Pages read:** 150 (1–150)
- **Findings:** 145 — applied 122, kept/not applied 23 (English kept: misprints and doubts settled by rule; see part 5); edits ok 122, failed 0
- **Reader tokens (batches so far):** 228k; per page 1.5k
- **Last commit:** ce374228

## 2. Batches
| Batch | Pages | Findings | Applied | Edits ok / failed | Kept / not applied | Tokens | Commit | Note |
|---|---|---|---|---|---|---|---|---|
| 1 | 1–150 | 130 | 122 | 122 / 0 | 8 | 228k | ce374228 |  |

## 3. Findings by kind
| Kind | Applied | Kept / not applied | Total |
|---|---|---|---|
| Q2 | 53 | 23 | 76 |
| Q1 | 68 | 0 | 68 |
| S3 | 1 | 0 | 1 |

By reader: R1 145

## 4. Open items (not findings)
- **other** (pages 7): Kannada p.7 gives "prakṛtyaikāc" as Pā. Sū. 6-4-163, the English (p.7 grammar remark) says 6-1-197 "as printed"; unmarked, left (found while settling q21)
- **other** (pages 59): English p.59 (sumnāvarī): sixteen names of Uṣas cited "(Ni. 3-9)"; Kannada p.59 prints (ನಿ. 2-19); unmarked, left (found while settling q79)
- **other** (pages 60): English p.60 (sūnṛtā): names of Uṣas cited "(Ni. 3-9)"; Kannada p.60 prints (ನಿ. 2-19) for the Uṣas names and (ನಿ. 3-9) for the food names; unmarked, left (found while settling q81)

## 5. Questions for the editor
**0 open questions** in `questions.tsv` (the editor decides only what the rules cannot: nothing else is asked).

Settled by rule, no reading needed: 4 Kannada misprints where the English is kept (`kn_misprints.tsv`); 19 places where the English is kept unchanged and listed for the scholar sample (`decided_by_default.tsv`). Impossible or odd printed numbers applied as printed are in part 4.

## 6. Files
`vol9/review/second_pass/findings.tsv` · `questions.tsv` · `batches.tsv` · `open.tsv` · `edits/` (edit files and results) · `../repair_log.md` (every English repair, heading "second pass") · `../../data/source_fixes.tsv` (edits of the supplied Kannada)

## 7. Next
the next page batch; then S3 totals (re-run the S0 checks), S4 coverage, S5 pictures, S6 records
