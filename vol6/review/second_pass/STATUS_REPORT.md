# Vol 6 second pass — status report
*Made by `python3 tools/rv/sp_report.py 6` from `findings.tsv`, `questions.tsv`, `batches.tsv`, `open.tsv`; updated 2026-11-24. Format: `docs/SECOND_PASS_REPORT.md`.*

## 1. State
- **Stage:** S2 reading in page batches
- **Pages read:** 250 of 618 (300–309, 2–31, 32–61, 62–91, 92–121, 122–151, 152–181, 182–211, 212–241)
- **Findings:** 484 — applied 341, questions 143; edits ok 351, failed 0
- **Reader tokens (batches so far):** 2035k; per page 8.1k
- **Last commit:** 4a72102

## 2. Batches
| Batch | Pages | Findings | Applied | Edits ok / failed | Questions | Tokens | Commit | Note |
|---|---|---|---|---|---|---|---|---|
| pilot | 300–309 | 24 | 15 | 17 / 0 | 9 | 248k | b7ae9b6 | read 139k + apply 109k; the English reading notes on pp. 304 and 309 translate the bhāṣya and were not read |
| 1 | 2–31 | 86 | 35 | 43 / 0 | 51 | 304k | 2a611eb | most questions are Kannada misprints the English had silently put right (H29); pp. 7–8 are one English section (p. 7 edits filed under page 6) |
| 2 | 32–61 | 44 | 37 | 37 / 0 | 7 | 208k | fed3619 | 24 S2: sūtra numbers the English had and the Kannada does not print were removed |
| 3 | 62–91 | 76 | 55 | 55 / 0 | 21 | 311k | 96960c4 | 30 S2 removals; English pp. 72/73 boundary shifted by about a paragraph |
| 4 | 92–121 | 50 | 35 | 35 / 0 | 15 | 204k | 26ecee4 | 22 S2 removals; one edit (p. 95) needed a rerun after sp_apply.py learned two headings for one page |
| 5 | 122–151 | 67 | 52 | 52 / 0 | 15 | 272k | 823a12c | 20 S2 removals, 7 S7 quotation repairs; English p. 141 carries the first lines of Kannada p. 142 |
| 7 | 152–181 | 43 | 35 | 35 / 0 | 8 | 223k | 7998fe1 | 19 S1 + 8 S2 number repairs, 2 S7 quotation repairs; two English headings each for pp. 154 and 179 (handled) |
| 8 | 182–211 | 52 | 40 | 40 / 0 | 12 | 265k | 24b7437 | 18 S1 + 8 S2 number repairs, 6 S7 quotation repairs; p. 203 has two English headings (handled); p. 196 sense (apart from / in company of man) left as a question |
| 9 | 212–241 | 42 | 37 | 37 / 0 | 5 | TOK8 | 4a72102 | 22 S2, 4 S3 number repairs, R3 quotation repairs (Taittirīya, Skandasvāmin); English pp. 232–235 shifted against the Kannada (see open items); duplicate removed from English p. 213/214 |

## 3. Findings by kind
| Kind | Applied | Questions | Total |
|---|---|---|---|
| S2 | 126 | 1 | 127 |
| H29 | 1 | 116 | 117 |
| S1 | 70 | 3 | 73 |
| S14 | 46 | 6 | 52 |
| S7 | 41 | 7 | 48 |
| S16 | 23 | 3 | 26 |
| S3 | 12 | 0 | 12 |
| R3 | 8 | 2 | 10 |
| S13 | 5 | 4 | 9 |
| S17 | 6 | 1 | 7 |
| S15 | 2 | 0 | 2 |
| S18 | 1 | 0 | 1 |

By reader: R1 312, R3 114, R6 58

## 4. Open items (not findings)
- **marker** (pages 65-66): The text of p. 66 stands inside the p. 65 block of the Kannada book (head missing): the page marker needs a fix; the English p. 66 matches that text
- **boundary-shifted** (pages 72-73): English p. 72 already carries about a paragraph of Kannada p. 73
- **boundary-shifted** (pages 141-142): English p. 141 carries the first lines of Kannada p. 142
- **page-absent** (pages 8, 559, 571): Not in the supplied text (no head); p. 66 is found inside p. 65, p. 8 inside p. 7 per the batch 1 reader (to be confirmed)
- **block-not-read** (pages 148): bhāṣya block: Devanagari paribhāṣā digit ९३-२ disagrees with IAST 93-7 and the Kannada ೯೩-೭ (blocks are not read in this pass)
- **findings-row-stale** (pages 95): The p. 95 row for Ā. 7-7 says question; the edit was applied afterwards (7-3)
- **boundary-shifted** (pages 232-233): English p. 232 carries the pratipadārtha of Ṛk 68.4, which sits on Kannada p. 233
- **boundary-shifted** (pages 234-235): English p. 234 reaches into Kannada p. 235; English p. 235 repeats the Skandasvāmin passage as "Special Topics (concluded)"

## 5. Questions for the editor
142 rows in `questions.tsv`; by kind: H29 116, R3 2, S1 3, S13 4, S14 6, S16 3, S17 1, S2 1, S7 7

## 6. Files
`vol6/review/second_pass/findings.tsv` · `questions.tsv` · `batches.tsv` · `open.tsv` · `edits/` (edit files and results) · `../repair_log.md` (every English repair, heading "second pass") · `../../data/source_fixes.tsv` (edits of the supplied Kannada)

## 7. Next
the next page batch; then S3 totals (re-run the S0 checks), S4 coverage, S5 pictures, S6 records
