# Vol 6 second pass — status report
*Made by `python3 tools/rv/sp_report.py 6` from `findings.tsv`, `questions.tsv`, `batches.tsv`, `open.tsv`; updated 2026-11-24. Format: `docs/SECOND_PASS_REPORT.md`.*

## 1. State
- **Stage:** S2 reading in page batches
- **Pages read:** 308 of 618 (300–309, 2–31, 32–61, 62–91, 92–121, 122–151, 152–181, 182–211, 212–241, 242–271, 272–299)
- **Findings:** 582 — applied 412, questions 170; edits ok 422, failed 0
- **Reader tokens (batches so far):** 2467k; per page 8.0k
- **Last commit:** 0acd82d

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
| 9 | 212–241 | 42 | 37 | 37 / 0 | 5 | 212k | 4a72102 | 22 S2, 4 S3 number repairs, R3 quotation repairs (Taittirīya, Skandasvāmin); English pp. 232–235 shifted against the Kannada (see open items); duplicate removed from English p. 213/214 |
| 10 | 242–271 | 46 | 32 | 32 / 0 | 14 | 220k | e5f80e2 | 24 S2 number repairs, 5 S7 quotation repairs; no '### Page 259' heading in the English; English p. 256/257 shifted (see open items) |
| 11 | 272–299 | 52 | 39 | 39 / 0 | 13 | TOK10 | 0acd82d | 11 S1 + 14 S3 (five running heads Varga [?] → 14) number repairs, 5 S7 quotation repairs; no page shifts |

## 3. Findings by kind
| Kind | Applied | Questions | Total |
|---|---|---|---|
| S2 | 149 | 1 | 150 |
| H29 | 1 | 142 | 143 |
| S1 | 80 | 3 | 83 |
| S14 | 54 | 6 | 60 |
| S7 | 50 | 7 | 57 |
| S16 | 27 | 3 | 30 |
| S3 | 28 | 0 | 28 |
| S13 | 5 | 5 | 10 |
| R3 | 8 | 2 | 10 |
| S17 | 7 | 1 | 8 |
| S15 | 2 | 0 | 2 |
| S18 | 1 | 0 | 1 |

By reader: R1 374, R3 133, R6 75

## 4. Open items (not findings)
- **marker** (pages 65-66): The text of p. 66 stands inside the p. 65 block of the Kannada book (head missing): the page marker needs a fix; the English p. 66 matches that text
- **boundary-shifted** (pages 72-73): English p. 72 already carries about a paragraph of Kannada p. 73
- **boundary-shifted** (pages 141-142): English p. 141 carries the first lines of Kannada p. 142
- **page-absent** (pages 8, 559, 571): Not in the supplied text (no head); p. 66 is found inside p. 65, p. 8 inside p. 7 per the batch 1 reader (to be confirmed)
- **block-not-read** (pages 148): bhāṣya block: Devanagari paribhāṣā digit ९३-२ disagrees with IAST 93-7 and the Kannada ೯೩-೭ (blocks are not read in this pass)
- **findings-row-stale** (pages 95): The p. 95 row for Ā. 7-7 says question; the edit was applied afterwards (7-3)
- **boundary-shifted** (pages 232-233): English p. 232 carries the pratipadārtha of Ṛk 68.4, which sits on Kannada p. 233
- **boundary-shifted** (pages 234-235): English p. 234 reaches into Kannada p. 235; English p. 235 repeats the Skandasvāmin passage as "Special Topics (concluded)"
- **page-absent** (pages 259): No "### Page 259" in the English: English p. 258 covers Kannada pp. 258–259
- **boundary-shifted** (pages 256-257): English p. 256 holds the pratipadārtha of Ṛk 69.5 that is on Kannada p. 257
- **block-not-read** (pages 268): bhāṣya block (Devanagari and IAST) still has tai. brā. [1-1-9-2?], [1-1-9-10?], ni. [1-11?]; the Kannada prints 2-1-2-7, 2-1-2-10, 2-11 (corrected in the Meaning and Special Topics paragraphs only)
- **block-not-read** (pages 252, 255): Kannada grammar tails print ६-७ / ८-९ while its own Saṃhitā/Pada blocks print ५-६ / ७-८; English follows the blocks (a question row)
- **block-not-read** (pages 280, 284, 293): bhāṣya-tail characterisations still have [?] numerals (Uṇ. [2-28?] on p. 280; Uṇ. 2-97, 4-73, Phiṭ., Pā. 5-2-122 on pp. 284, 293); they come from the bhāṣya, not from the Kannada numerals; for the editor
- **other** (pages 283): The Kannada heading prints "ಸೂಕ್ತ-೨೧" where the English gives 71 (question row)

## 5. Questions for the editor
169 rows in `questions.tsv`; by kind: H29 142, R3 2, S1 3, S13 5, S14 6, S16 3, S17 1, S2 1, S7 7

## 6. Files
`vol6/review/second_pass/findings.tsv` · `questions.tsv` · `batches.tsv` · `open.tsv` · `edits/` (edit files and results) · `../repair_log.md` (every English repair, heading "second pass") · `../../data/source_fixes.tsv` (edits of the supplied Kannada)

## 7. Next
the next page batch; then S3 totals (re-run the S0 checks), S4 coverage, S5 pictures, S6 records
