# Vol 10 second pass — status report
*Made by `python3 tools/rv/sp_report.py 10` from `findings.tsv`, `questions.tsv`, `batches.tsv`, `open.tsv`; updated 2026-11-27. Format: `docs/SECOND_PASS_REPORT.md`.*

## 1. State
- **Stage:** S2 reading in page batches
- **Pages read:** 618 (300–309, 2–31, 32–61, 62–91, 92–121, 122–151, 152–181, 182–211, 300–368, 350–499, 500–579, 580–619, 620–659, 660–707)
- **Findings:** 1041 — applied 944, kept/not applied 97 (English kept: misprints and doubts settled by rule; see part 5); edits ok 965, failed 0
- **Reader tokens (batches so far):** 3549k; per page 5.7k
- **Last commit:** (this commit)

## 2. Batches
| Batch | Pages | Findings | Applied | Edits ok / failed | Kept / not applied | Tokens | Commit | Note |
|---|---|---|---|---|---|---|---|---|
| 1 | 300–309 | 35 | 30 | 38 / 0 | 5 | 180k | e889856a | pilot; 27 [?] seen, 22 resolved from the Kannada, 5 kept (inside our remarks) |
| 2 | 2–31 | 24 | 14 | 17 / 0 | 10 | 157k | 1119c0fb | pp. 2-3 read in full; pp. 4-31 script-assisted (numbers, refs, all 19 [?]) not read as prose: re-read later; 19 [?] seen, 6 removed, 13 kept |
| 3 | 32–61 | 96 | 87 | 87 / 0 | 9 | 251k | c53f4019 | all pages read; 68 of 87 edits add sutra numbers the Kannada prints; 17 [?] seen, 0 removed (Kannada non-words), 17 kept |
| 4 | 62–91 | 77 | 72 | 72 / 0 | 5 | 224k | 9d18ba97 | all pages read; 41 edits add sutra numbers; 8 [?] seen, 5 removed, 3 kept (in remarks) |
| 5 | 92–121 | 43 | 30 | 34 / 0 | 13 | 268k | 3ef7390f | all pages read; 15 [?] seen, 8 removed, 7 kept |
| 6 | 122–151 | 29 | 20 | 24 / 0 | 9 | 237k | 47f213ba | all pages read; 15 [?] seen, 8 removed, 7 kept |
| 7 | 152–181 | 46 | 37 | 37 / 0 | 9 | 255k | 750bb9d6 | all pages read; 21 [?] seen, 7 removed, 14 kept |
| 8 | 182–211 | 33 | 28 | 28 / 0 | 5 | 213k | 649ae3f4 | all pages read; 7 [?] seen, 2 removed, 5 kept |
| 9 | 300–368 | 112 | 102 | 111 / 0 | 10 | 301k | (this commit) | mark-only batch q1-q150 (marks of pp. 2-368 left after qmark_strip): 134 settled, 16 kept; marks 1041 -> 907 |
| 10 | 350–499 | 160 | 156 | 137 / 0 | 4 | 287k | (this commit) | mark-only batch pp. 350-499: 150 of 154 settled, 4 kept; marks 907 -> 757 |
| 11 | 500–579 | 110 | 106 | 106 / 0 | 4 | 340k | (this commit) | mark-only batch pp. 500-579: 151 of 155 settled, 4 kept; marks 757 -> 606 |
| 12 | 580–619 | 90 | 88 | 88 / 0 | 2 | 292k | (this commit) | mark-only batch pp. 580-619: 172 marks removed, 2 kept; marks 606 -> 434 |
| 13 | 620–659 | 100 | 97 | 97 / 0 | 3 | 284k | (this commit) | mark-only batch pp. 620-659: 191 marks removed, 3 kept; marks 434 -> 243 |
| 14 | 660–707 | 92 | 89 | 89 / 0 | 3 | 260k | (this commit) | mark-only batch pp. 660-707: 208 marks removed, 6 kept; marks 243 -> 35 |

## 3. Findings by kind
| Kind | Applied | Kept / not applied | Total |
|---|---|---|---|
| Q1 | 412 | 0 | 412 |
| Q2 | 239 | 80 | 319 |
| S3 | 134 | 1 | 135 |
| S1 | 68 | 0 | 68 |
| S2 | 31 | 3 | 34 |
| S13 | 29 | 4 | 33 |
| S14 | 19 | 2 | 21 |
| H29 | 0 | 5 | 5 |
| S16 | 5 | 0 | 5 |
| S7 | 5 | 0 | 5 |
| S15 | 2 | 0 | 2 |
| S18 | 0 | 2 | 2 |

By reader: R1 1015, R3 18, R6 8

## 4. Open items (not findings)
- **other** (pages 307): running head Varga printed ವ. ೧೭ (neighbouring heads ವ. ೧೩); applied as printed (Varga 17)
- **other** (pages 29): Ghoṣā sūktas printed ೨೯-೪೦ ಮತ್ತು ೪೧ನೇ; applied as printed
- **other** (pages 37): grammar sūtra number printed ೨-೪-೨೨೬ (juhotyādibhyaḥ śluḥ; Aṣṭādhyāyī 2-4 has fewer sūtras); applied as printed
- **other** (pages 78): Pā. Sū. printed ೩-೧-೫-೩ (four figures); applied as printed
- **other** (pages 158): Kannada p.158 prints the Pāṇini sūtra number of śatur anumo nadyajādī as ೬-೧-೧-೩; applied as printed
- **other** (pages 160, 168): Kannada running head prints Sū. ೧೨೩ (not ೧೨೪) on pp. 160 and 168; applied as printed
- **other** (pages 159): Kannada running head of p.159 prints Varga ೬ (pp. 153-157 print 6, p.161 prints 8); applied as printed
- **other** (pages 460): Ṛ. Saṃ. 11-86-22 printed (ಋ. ಸಂ. ೧೧-೮೬-೨೨), an impossible Maṇḍala; applied as printed in the English
- **other** (pages 434-435): Neighbouring Nirukta numbers not marked: p.434 arm Ni. 2-15 (Kannada 3-8), p.435 food Ni. 2-24 (Kannada 3-9); not touched
- **other** (pages 531): English says the commentator explains Ṛ. Saṃ. 1-132-6, Kannada p.531 says ೧-೧೨೨-೩ (unmarked, not edited); Ni. 11-37 given in English as read "೧೧-೧೭" while Kannada has ೧೧-೩೭
- **other** (pages 527): English Okya (Ni. 3-13); Kannada p.527 prints (ನಿ. ೩-೩) (unmarked, not edited)
- **other** (pages 543): Kannada p.543 gives Pā. Sū. 8-3-9 for matuvasoḥ sambuddhau, English (unmarked) has 8-3-1; Uṇ. Sū. 4-530 applied as printed (impossible number? Sāyaṇa block p.541 prints Uṇ. 4-90)
- **other** (pages 561): English (unmarked) Pā. Sū. 8-5-70 [as read] for amnarūdharavar…; Kannada p.561 prints ೮-೨-೭೦
- **other** (pages 607): Kannada p.607 head block lists Indra for Ṛks 4-8, the anuvāda on p.606 says "(೫-೯)" for the five Ṛks beginning ಆ ವಾಂ ರಥ; English bracket "[Ṛks 4–8]" unmarked, left
- **other** (pages 590): Kannada p.590 prints ಋ. ಸಂ. ೭-೨೫-೨೯ for the Ṛk vājinīvatī sūryasya yoṣā citrāmaghā (no such verse); applied as printed (the English first read 1-48-3)
- **other** (pages 583): unmarked neighbour: English "(the one cited by the author of the Nirukta, 2-31-4)" but Kannada p.583 gives ೭-೩೯-೪ for that Ṛk; left
- **other** (pages 598): unmarked neighbour: English "yo te bhīmāny āyudhā" but Kannada p.598 reads ಯಾ ತೇ ಭೀಮಾನ್ಯಾಯುಧಾ (yā te); left
- **other** (pages 600): unmarked neighbour: English "khujendragra… [as read: śukrendraśuci…]" but Kannada p.600 reads ಋಜೇಂದ್ರಾಗ್ರ; left
- **other** (pages 608): unmarked neighbour: English "jayi ca (Pā. Sū. 6-1-203 [as read])" but Kannada p.608 prints ಪಾ ೬-೧-೨೧೨ (p.612 ೬-೧-೨೧೩); left
- **other** (pages 623): unmarked: Sense remark cites the pūrvapeyam quotation as (Ṛ. Saṃ. 8-1-1 [as read]); Kannada p.623/625 prints ಋ. ೭-೯೨-೧; not edited (no mark)
- **other** (pages 650): unmarked: "of the first Ṛk" (adribhiḥ sutānām, Ṛ. Saṃ. 1-135); Kannada p.650 says ೫ ನೇ ಋಕ್ಕು (fifth Ṛk); not edited (no mark)
- **other** (pages 663): Kannada prints Ṛ. Saṃ. ೧೦-೯೧೭-೨ for yaḥ parasyāḥ parāvataḥ (impossible sūkta number); applied as printed (q55)
- **other** (pages 668): Ṛ. Saṃ. printed 4-57-2 in the English after kṣetrasya patinā vayam; the Kannada p.668 prints ೪-೫೭-೧ (unmarked, not edited)
- **other** (pages 678): Kannada prints Tai. Saṃ. ೬-೨೯೭-೨ ರಿಂದ ೮ for the Uttaravedi passage (impossible number, probably 6-2-9-2 to 8); applied as printed (q101)

## 5. Questions for the editor
**0 open questions** in `questions.tsv` (the editor decides only what the rules cannot: nothing else is asked).

Settled by rule, no reading needed: 94 Kannada misprints where the English is kept (`kn_misprints.tsv`); 38 places where the English is kept unchanged and listed for the scholar sample (`decided_by_default.tsv`). Impossible or odd printed numbers applied as printed are in part 4.

## 6. Files
`vol10/review/second_pass/findings.tsv` · `questions.tsv` · `batches.tsv` · `open.tsv` · `edits/` (edit files and results) · `../repair_log.md` (every English repair, heading "second pass") · `../../data/source_fixes.tsv` (edits of the supplied Kannada)

## 7. Next
the next page batch; then S3 totals (re-run the S0 checks), S4 coverage, S5 pictures, S6 records
