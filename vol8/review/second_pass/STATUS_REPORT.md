# Vol 8 second pass — status report
*Made by `python3 tools/rv/sp_report.py 8` from `findings.tsv`, `questions.tsv`, `batches.tsv`, `open.tsv`; updated 2026-11-27. Format: `docs/SECOND_PASS_REPORT.md`.*

## 1. State
- **Stage:** S2 reading in page batches
- **Pages read:** 694 (550–559, 2–31, 32–61, 62–91, 92–121, 122–151, 152–181, 182–211, 212–241, 242–312, 312–395, 395–448, 448–475, 476–510, 510–544, 544–582, 582–613, 613–645, 645–677, 677–695)
- **Findings:** 2340 — applied 1900, kept/not applied 440 (English kept: misprints and doubts settled by rule; see part 5); edits ok 1854, failed 0
- **Reader tokens (batches so far):** 3896k; per page 5.6k
- **Last commit:** e0215527

## 2. Batches
| Batch | Pages | Findings | Applied | Edits ok / failed | Kept / not applied | Tokens | Commit | Note |
|---|---|---|---|---|---|---|---|---|
| 1 | 550–559 | 87 | 62 | 50 / 0 | 25 | 139k | d7e7d422 | pilot; 81 [?] seen, 59 removed (36 corrected), 22 kept |
| 2 | 2–31 | 79 | 40 | 40 / 0 | 39 | 223k | eab0f49c | 79 [?] seen, 40 removed (26 corrected), 39 kept |
| 3 | 32–61 | 47 | 18 | 16 / 0 | 29 | 134k | 337547ac | 47 [?] seen, 18 removed (16 corrected), 29 kept |
| 4 | 62–91 | 59 | 22 | 22 / 0 | 37 | 145k | 2f3b1d92 | 59 [?] seen, 22 removed (11 corrected), 37 kept |
| 5 | 92–121 | 47 | 23 | 22 / 0 | 24 | 118k | c2bfa8ce | 46 [?] seen, 22 removed (10 corrected), 24 kept |
| 6 | 122–151 | 82 | 29 | 29 / 0 | 53 | 164k | 35a4c917 | 81 [?] seen, 28 removed (19 corrected), 53 kept |
| 7 | 152–181 | 151 | 90 | 86 / 0 | 61 | 221k | 98529247 | 151 [?] seen, 90 removed (59 corrected), 61 kept |
| 8 | 182–211 | 158 | 103 | 100 / 0 | 55 | 244k | 6140a9b6 | 158 [?] seen, 103 removed (67 corrected), 55 kept |
| 9 | 212–241 | 100 | 67 | 64 / 0 | 33 | 191k | c73d3d9c | 100 [?] seen, 67 removed (39 corrected), 33 kept |
| 10 | 242–312 | 150 | 139 | 135 / 0 | 11 | 211k | 6ea1f23d | marks q236-q385: 150 seen, 139 removed, 11 kept |
| 11 | 312–395 | 145 | 132 | 129 / 0 | 13 | 186k | 0ca158e9 | marks q386-q535: 150 seen, 137 removed, 13 kept |
| 12 | 395–448 | 144 | 129 | 127 / 0 | 15 | 243k | e48e6dc8 | marks q536-q685: 150 seen, 135 removed, 15 kept |
| 13 | 448–475 | 131 | 129 | 124 / 0 | 2 | 188k | b505bab8 | marks q275-q424: 150 seen, 148 removed, 2 kept |
| 14 | 476–510 | 137 | 130 | 130 / 0 | 7 | 207k | f90096fc | marks q284-q433: 150 seen, 143 removed, 7 kept |
| 15 | 510–544 | 133 | 126 | 123 / 0 | 7 | 189k | 64ed7bd8 | marks q291-q440: 150 seen, 143 removed, 7 kept |
| 16 | 544–582 | 219 | 193 | 130 / 0 | 26 | 205k | 9f0ab941 | marks q298-q455: 150 seen, 149 removed, 1 kept |
| 17 | 582–613 | 153 | 144 | 138 / 0 | 9 | 192k | 51cc7584 | marks q307-q456: 150 seen, 141 removed, 9 kept |
| 18 | 613–645 | 144 | 137 | 133 / 0 | 7 | 200k | dfb9c7bc | marks q316-q465: 150 seen, 143 removed, 7 kept |
| 19 | 645–677 | 154 | 149 | 131 / 0 | 5 | 244k | c1e9ca69 | marks q323-q472: 150 seen, 145 removed, 5 kept |
| 20 | 677–695 | 134 | 126 | 125 / 0 | 8 | 252k | e0215527 | marks q327-q476: 150 seen, 143 removed, 7 kept |

## 3. Findings by kind
| Kind | Applied | Kept / not applied | Total |
|---|---|---|---|
| Q2 | 1067 | 288 | 1355 |
| Q1 | 726 | 149 | 875 |
| S3 | 99 | 0 | 99 |
| S2 | 6 | 0 | 6 |
| S1 | 2 | 0 | 2 |
| S7 | 0 | 2 | 2 |
| S13 | 0 | 1 | 1 |

By reader: R1 2337, R3 2, R6 1

## 4. Open items (not findings)
- **other** (pages 118): Pā. Sū. 3-1-0 (Kannada p. 118 prints ೩-೧-೦, impossible sutra number); applied as printed
- **other** (pages 204): Ni. 28 (Kannada p. 204 prints (ನಿ. ೨೮) for the names of action; not in the usual form a-b); applied as printed
- **other** (pages 445): Ṛ. Saṃ. reference in Wilson quotation (Kannada p. 445 prints (ಸೂ. ೧೦೫.೫.೯), not the usual form a-b-c); applied as printed: 105.5.9
- **other** (pages 414): Pā. Sū. 6-2-196, 8-2-39, 7-1-39 and U. Sū. 4-256 (Kannada p. 414 prints these numbers for ata upadhāyāḥ, vraśca-…, supāṃ suluk, nahor bhaś ca); applied as printed
- **other** (pages 470): Uṇ. Sū. 4-547 (Kannada p. 470 prints ಉ. ಸೂ. ೪-೫೪೭, impossible sūtra number); applied as printed
- **other** (pages 485): Ṛ. 1-1073 (Kannada p. 485 prints (ಋ. ೧-೧೦೭೩), impossible number form); applied as printed
- **other** (pages 488): Pā. Sū. 6-12-139 (Kannada p. 488 prints ೬-೧೨-೧೩೯, impossible); applied as printed
- **other** (pages 491): 2.4-22 (Kannada p. 491 prints ೨.೪-೨೨ in the list of Ṛks for suparṇa); applied as printed
- **other** (pages 501): U. Sū. 4-578 (Kannada p. 501 prints (ಉ. ಸೂ. ೪-೫೭೮), impossible number form); applied as printed
- **other** (pages 547): Nigh. 55-1 (Kannada p. 547 prints (ನಿಘಂಟು. ೫೫-೧), impossible number form); applied as printed
- **other** (pages 571): Ni. 6-16 (Kannada p. 571 prints (ನಿ. ೬-೧೬) for the names of food); applied as printed
- **other** (pages 572): Uṇ. 4-639 (Kannada p. 572 prints (ಉ. ಸೂ. ೪-೬೩೯), impossible number form); applied as printed
- **other** (pages 682): Pā. Sū. 6-249 (Kannada p. 682 prints (ಪಾ. ಸೂ ೬-೨೪೯) for gatir anantaraḥ, not in the usual form a-b-c); applied as printed
- **other** (pages 694): Ṛ. Saṃ. 0-168-9 (Kannada p. 694 prints (ಋ. ಸಂ. ೦-೧೬೮.-೯), impossible mandala number); applied as printed
- **other** (pages 694): Ṛ. Saṃ. 3-69-2 (Kannada p. 694 prints (ಋ. ಸಂ. ೩-೬೯-೨), no such hymn in mandala 3); applied as printed

## 5. Questions for the editor
**0 open questions** in `questions.tsv` (the editor decides only what the rules cannot: nothing else is asked).

Settled by rule, no reading needed: 87 Kannada misprints where the English is kept (`kn_misprints.tsv`); 91 places where the English is kept unchanged and listed for the scholar sample (`decided_by_default.tsv`). Impossible or odd printed numbers applied as printed are in part 4.

## 6. Files
`vol8/review/second_pass/findings.tsv` · `questions.tsv` · `batches.tsv` · `open.tsv` · `edits/` (edit files and results) · `../repair_log.md` (every English repair, heading "second pass") · `../../data/source_fixes.tsv` (edits of the supplied Kannada)

## 7. Next
the next page batch; then S3 totals (re-run the S0 checks), S4 coverage, S5 pictures, S6 records
