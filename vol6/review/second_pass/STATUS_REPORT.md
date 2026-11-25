# Vol 6 second pass — status report
*Made by `python3 tools/rv/sp_report.py 6` from `findings.tsv`, `questions.tsv`, `batches.tsv`, `open.tsv`; updated 2026-11-25. Format: `docs/SECOND_PASS_REPORT.md`.*

## 1. State
- **Stage:** S2 reading in page batches
- **Pages read:** 618 of 618 (300–309, 2–31, 32–61, 62–91, 92–121, 122–151, 152–181, 182–211, 212–241, 242–271, 272–299, 310–339, 340–369, 370–399, 400–429, 430–459, 460–489, 490–519, 520–549, 550–579, 580–599, 600–619)
- **Findings:** 1188 — applied 871, questions 317; edits ok 878, failed 0
- **Reader tokens (batches so far):** 5301k; per page 8.6k
- **Last commit:** f19b850

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
| 11 | 272–299 | 52 | 39 | 39 / 0 | 13 | 216k | 0acd82d | 11 S1 + 14 S3 (five running heads Varga [?] → 14) number repairs, 5 S7 quotation repairs; no page shifts |
| 12 | 310–339 | 35 | 29 | 29 / 0 | 6 | 250k | 06cf9df | 8 S1 + 5 S2 number repairs, 5 S7 quotation repairs, 7 S14 sense; English pp. 315/316 and 324/325 shifted (see open items) |
| 13 | 340–369 | 38 | 32 | 32 / 0 | 6 | 257k | bf12e26 | 6 S1 + 3 S2 number repairs, 6 S7 quotation repairs, 12 S18 grammar sūtra repairs; no page shifts; English grammar pages omit several numbers the Kannada prints (not added) |
| 14 | 370–399 | 45 | 35 | 35 / 0 | 10 | 259k | 93be96c | 15 S7 + 1 S7/R6 quotation repairs, 8 S2 removals; p. 370 reference changed to 18-18-8 as the Kannada prints (impossible maṇḍala, see open items); one edit needed a retry (asterisks); pp. 374 and 396 line up with the Kannada |
| 15 | 400–429 | 53 | 45 | 45 / 0 | 8 | 242k | abb8a1d | 13 S1/S2 number repairs (incl. Ṛk 10-98-5 → 10-92-5, sūkta 72 → 73), 14 S7 + 4 S13 quotation/term repairs; one retry; no page shifts; p. 425 Pā. Sū. 7-1-171 applied as printed (open item) |
| 16 | 430–459 | 38 | 18 | 18 / 0 | 20 | 232k | e2afdaa | 6 S2 + 4 S1 number repairs; p. 451 Pā. Sū. [6-2-2] → 9-2-2 as the Kannada prints (no adhyāya 9: see open items); p. 443 volume 2 → 1; p. 458 lines up; no page shifts |
| 17 | 460–489 | 42 | 30 | 30 / 0 | 12 | 244k | e0252e0 | 14 number fixes, 10 number removals, 6 R3 quotation repairs; English pp. 471/472 and 480/481 shifted (open items); one edit-file slip left an extra harmless p. 471 row in findings.tsv; reader hit the usage limit and was resumed |
| 18 | 490–519 | 66 | 47 | 47 / 0 | 19 | 253k | f10e549 | 31 S1 + 11 S2 number repairs, 2 S7; Pāṇini adhyāya 9 printed on p. 507, and 6-2-55 vs 5-3-55 on p. 515 (open items); English from p. 490 is a condensed rendering; no page shifts |
| 19 | 520–549 | 100 | 84 | 84 / 0 | 16 | 243k | 369af22 | 84 edits: 21 S1, about 40 S2 removals of sūtra numbers the Kannada does not print, 33 S7 quotation edits (IAST + Devanagari pairs); no page shifts; p. 540 prints 6-1-167 vs p. 521 6-1-197 (each page's own number applied); findings.tsv/questions.tsv p. 532 rows were trimmed by hand by the reader |
| 20 | 550–579 | 78 | 56 | 56 / 0 | 22 | 246k | 5fbbab4 | 46 number repairs (16 S1/S3, 13 sūtra numbers, 18 removals), 7 R3 quotation edits; pp. 559 and 571 have no head in the supplied text (inside 558 and 570); English pp. 570/571 shifted (open items) |
| 21 | 580–599 | 46 | 31 | 31 / 0 | 15 | 204k | 72888b7 | 4 S1 + 17 S2 + 2 S3 number repairs, 3 S13, 3 S14; no page shifts |
| 22 | 600–619 | 62 | 49 | 49 / 0 | 13 | 188k | f19b850 | 28 S2 + 8 S3 number repairs, incl. the Dadhyañc/Manu numerals of pp. 616–618 settled from the Kannada ([?] marks removed; Kannada prints ೬-೬--೬-೧ read as 6-6-6-1); 10 R3/S13; no page shifts |

## 3. Findings by kind
| Kind | Applied | Questions | Total |
|---|---|---|---|
| S2 | 304 | 1 | 305 |
| H29 | 3 | 277 | 280 |
| S1 | 177 | 3 | 180 |
| S7 | 145 | 13 | 158 |
| S14 | 86 | 7 | 93 |
| S3 | 48 | 0 | 48 |
| S16 | 44 | 3 | 47 |
| S13 | 24 | 8 | 32 |
| S17 | 14 | 1 | 15 |
| S18 | 13 | 0 | 13 |
| R3 | 8 | 4 | 12 |
| S15 | 4 | 0 | 4 |
| H21 | 1 | 0 | 1 |

By reader: R1 736, R3 274, R6 178

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
- **boundary-shifted** (pages 315-316): English p. 315 carries the whole Special Topics paragraph incl. the first lines of Kannada p. 316; English p. 316 repeats its end as "(Completion)"
- **boundary-shifted** (pages 324-325): English p. 324 carries the whole bhāṣya of 72.9 incl. the grammatical tail that is on Kannada p. 325
- **other** (pages 370): Applied by the rule "Kannada numerals are correct": "Ṛ. Saṃ. 10-108-8" → "18-18-8" (Kannada ೧೮-೧೮-೮). A maṇḍala 18 does not exist: the Kannada digits look machine-misread; the editor may want to look at this one place
- **other** (pages 425): Kannada prints Pā. Sū. 7-1-171 for ūḍidaṃ padādi (hṛde); the sūtra number looks odd (elsewhere 6-1-171); applied as printed
- **other** (pages 451): Kannada prints Pā. Sū. 9-2-2 (tatpuruṣe tulyārtha…); there is no adhyāya 9; applied as printed
- **other** (pages 443, 458): The English note on p. 458 says the Rik 74.5 cross-reference read 'volume 2'; after this pass p. 443 reads 'volume 1' as in the Kannada, so the note is stale
- **other** (pages 461): Kannada prints Pā. Sū. 6-1-189 (āmantritasya) here and 6-1-198 on p. 486; applied as printed
- **boundary-shifted** (pages 471-472): English p. 471 carries the whole grammar page of 76.1 that is on Kannada pp. 471-472; English p. 472 has only the Saṃhitā of 76.2
- **boundary-shifted** (pages 480-481): English p. 480 carries the bhāṣya tail and Pratipadārtha of 76.4 that are on Kannada p. 481
- **other** (pages 475-476): Kannada p. 476 has its own mark and head; English pp. 475/476 divide exactly as the Kannada (p. 476 starts at ಮಹೇ)
- **other** (pages 507): Kannada prints Pāṇini adhyāya 9 (ಶೇರನಿಟಿ ಪಾ. ಸೂ. ೯-೪-೫೧); applied as printed (English 6-4-51 replaced by 9-4-51)
- **other** (pages 515): Kannada prints ಅತಿಶಾಯನೇ ತಮಬಿಷ್ಠನೌ as ಪಾ. ಸೂ. ೬-೨-೫೫; pp. 502 and 518 print ೫-೩-೫೫; applied as printed on p. 515
- **boundary-shifted** (pages 570-571): English p. 570 (jaghantha entry) carries the first lines of the Kannada p. 571 text (inside the Kannada p. 570 block, head 571 missing); English p. 571 starts at arcan

## 5. Questions for the editor
**0 open questions** in `questions.tsv` (the editor decides only what the rules cannot: nothing else is asked).

Settled by rule, no reading needed: 260 Kannada misprints where the English is kept (`kn_misprints.tsv`); 54 places where the English is kept unchanged and listed for the scholar sample (`decided_by_default.tsv`). Impossible or odd printed numbers applied as printed are in part 4.

## 6. Files
`vol6/review/second_pass/findings.tsv` · `questions.tsv` · `batches.tsv` · `open.tsv` · `edits/` (edit files and results) · `../repair_log.md` (every English repair, heading "second pass") · `../../data/source_fixes.tsv` (edits of the supplied Kannada)

## 7. Next
the next page batch; then S3 totals (re-run the S0 checks), S4 coverage, S5 pictures, S6 records
