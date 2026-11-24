# Vol 6 second pass — status report
*Made by `python3 tools/rv/sp_report.py 6` from `findings.tsv`, `questions.tsv`, `batches.tsv`, `open.tsv`; updated 2026-11-24. Format: `docs/SECOND_PASS_REPORT.md`.*

## 1. State
- **Stage:** S2 reading in page batches
- **Pages read:** 160 of 618 (300–309, 2–31, 32–61, 62–91, 92–121, 122–151)
- **Findings:** 347 — applied 229, questions 118; edits ok 239, failed 0
- **Reader tokens (batches so far):** 1547k; per page 9.7k
- **Last commit:** 823a12c

## 2. Batches
| Batch | Pages | Findings | Applied | Edits ok / failed | Questions | Tokens | Commit | Note |
|---|---|---|---|---|---|---|---|---|
| pilot | 300–309 | 24 | 15 | 17 / 0 | 9 | 248k | b7ae9b6 | read 139k + apply 109k; the English reading notes on pp. 304 and 309 translate the bhāṣya and were not read |
| 1 | 2–31 | 86 | 35 | 43 / 0 | 51 | 304k | 2a611eb | most questions are Kannada misprints the English had silently put right (H29); pp. 7–8 are one English section (p. 7 edits filed under page 6) |
| 2 | 32–61 | 44 | 37 | 37 / 0 | 7 | 208k | fed3619 | 24 S2: sūtra numbers the English had and the Kannada does not print were removed |
| 3 | 62–91 | 76 | 55 | 55 / 0 | 21 | 311k | 96960c4 | 30 S2 removals; English pp. 72/73 boundary shifted by about a paragraph |
| 4 | 92–121 | 50 | 35 | 35 / 0 | 15 | 204k | 26ecee4 | 22 S2 removals; one edit (p. 95) needed a rerun after sp_apply.py learned two headings for one page |
| 5 | 122–151 | 67 | 52 | 52 / 0 | 15 | 272k | 823a12c | 20 S2 removals, 7 S7 quotation repairs; English p. 141 carries the first lines of Kannada p. 142 |

## 3. Findings by kind
| Kind | Applied | Questions | Total |
|---|---|---|---|
| H29 | 1 | 102 | 103 |
| S2 | 91 | 0 | 91 |
| S1 | 41 | 3 | 44 |
| S14 | 37 | 5 | 42 |
| S7 | 29 | 2 | 31 |
| S16 | 15 | 1 | 16 |
| S13 | 5 | 3 | 8 |
| S3 | 4 | 0 | 4 |
| S17 | 4 | 0 | 4 |
| R3 | 0 | 2 | 2 |
| S15 | 1 | 0 | 1 |
| S18 | 1 | 0 | 1 |

By reader: R1 214, R3 85, R6 48

## 4. Open items (not findings)
- **marker** (pages 65-66): The text of p. 66 stands inside the p. 65 block of the Kannada book (head missing): the page marker needs a fix; the English p. 66 matches that text
- **boundary-shifted** (pages 72-73): English p. 72 already carries about a paragraph of Kannada p. 73
- **boundary-shifted** (pages 141-142): English p. 141 carries the first lines of Kannada p. 142
- **page-absent** (pages 8, 559, 571): Not in the supplied text (no head); p. 66 is found inside p. 65, p. 8 inside p. 7 per the batch 1 reader (to be confirmed)
- **block-not-read** (pages 148): bhāṣya block: Devanagari paribhāṣā digit ९३-२ disagrees with IAST 93-7 and the Kannada ೯೩-೭ (blocks are not read in this pass)
- **findings-row-stale** (pages 95): The p. 95 row for Ā. 7-7 says question; the edit was applied afterwards (7-3)

## 5. Questions for the editor
117 rows in `questions.tsv`; by kind: H29 102, R3 2, S1 3, S13 3, S14 5, S16 1, S7 2

## 6. Files
`vol6/review/second_pass/findings.tsv` · `questions.tsv` · `batches.tsv` · `open.tsv` · `edits/` (edit files and results) · `../repair_log.md` (every English repair, heading "second pass") · `../../data/source_fixes.tsv` (edits of the supplied Kannada)

## 7. Next
the next page batch; then S3 totals (re-run the S0 checks), S4 coverage, S5 pictures, S6 records
