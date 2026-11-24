# Vol 1 second pass — status report
*Made by `python3 tools/rv/sp_report.py 1` from `findings.tsv`, `questions.tsv`, `batches.tsv`, `open.tsv`; updated 2026-11-24. Format: `docs/SECOND_PASS_REPORT.md`.*

## 1. State
- **Stage:** S2 reading in page batches
- **Pages read:** 160 of 720 (360–369, 1–30, 31–60, 61–90, 91–120, 121–150)
- **Findings:** 715 — applied 603, questions 112; edits ok 607, failed 0
- **Reader tokens (batches so far):** 1479k; per page 9.2k
- **Last commit:** a98e5a2

## 2. Batches
| Batch | Pages | Findings | Applied | Edits ok / failed | Questions | Tokens | Commit | Note |
|---|---|---|---|---|---|---|---|---|
| pilot | 360–369 | 73 | 52 | 31 / 0 | 21 | 169k | f594e7e | pilot; 52 edits first applied, then 21 Devanagari edits (and 6 IAST partners) reverted by the new sp_sanskrit gate, 6 re-applied after the word-join refinement: net 31 English edits stand; 15 citation lines are questions; English not page-aligned to the Kannada on these pages (judged by content) |
| 2 | 1–30 | 134 | 110 | 110 / 0 | 24 | 349k | b195d7a | 110 edits (31 S7 via sp_sanskrit, 20 S13 names, ~30 numbers, ~25 sense); English not page-aligned (Page 4 carries Kannada 4–6, Page 10 carries 10–11, Page 15–16 combined, pp. 17–24 'gap filled' block); numbers taken as printed that look odd are in open.tsv; three longer rewrites on pp. 2, 9, 30 for re-reading |
| 3 | 31–60 | 134 | 118 | 118 / 0 | 16 | 344k | 938a30a | 118 edits (28 S7 via sp_sanskrit, 21 S13, 21 S14, 11 S15, 9 S16, 9 S17; many name/number repairs); English sections missing for Kannada pp. 35, 48, 52 (text under Page 34, 'Pages 46–47', Page 51); Kannada p. 54 text sits under the p. 53 mark; Paila vs Shaila: the Devanagari block 'शैलो होता' and the contents entry still say Shaila (open item) |
| 4 | 61–90 | 143 | 131 | 131 / 0 | 12 | 320k | 7fae0cb | 131 edits (45 S7 via sp_sanskrit, ~86 R1: names, senses, numbers, omissions); English sections not aligned (p. 73 text under Page 72; Māṇḍūkeya section starts at Page 79 vs Kannada 80–82); some longer rewrites where the English sentence was wrong (pp. 69, 74, 75, 83); 4 odd printed numbers in open.tsv |
| 5 | 91–120 | 138 | 121 | 121 / 0 | 17 | 297k | 96c32e1 | 121 edits (55 S7, 22 S1 + 7 S3 numbers incl. table digits on p. 113); pp. 91–94 in the main English file, 95–120 in the Gaps file; several Kannada numerals contradict the Kannada's own totals (p. 113, 114, 117; p. 100 Kāṇva list): applied as printed, 4 rows in open.tsv; the English italic remark on p. 113 that column sums agree is now untrue (legacy remark kept) |
| 6 | 121–150 | 93 | 71 | 96 / 0 | 22 | TOK5 | a98e5a2 | 96 edits (25 Devanagari/IAST pairs via sp_sanskrit, 25 number repairs); Kannada table numerals applied as printed even where they contradict the Kannada's own totals (pp. 121, 138, 139, 142, 150: 6 rows in open.tsv; English rows without a Kannada counterpart blanked/dashed on pp. 138–139); legacy remarks contradicted by the edits left (pp. 138, 150, 123–124) |

## 3. Findings by kind
| Kind | Applied | Questions | Total |
|---|---|---|---|
| S7 | 240 | 19 | 259 |
| S13 | 105 | 1 | 106 |
| S14 | 86 | 0 | 86 |
| H29 | 0 | 85 | 85 |
| S1 | 77 | 0 | 77 |
| S16 | 24 | 3 | 27 |
| S3 | 23 | 0 | 23 |
| S17 | 14 | 4 | 18 |
| S15 | 18 | 0 | 18 |
| S2 | 16 | 0 | 16 |

By reader: R1 313, R3 249, R6 153

## 4. Open items (not findings)
- **other** (pages 13): Kannada p.13 prints the total of mantras as ೧೦೦೫೨ (10052) while p.12 and the table print 10552; applied as printed (English now 10,052)
- **other** (pages 14): Kannada p.14 gives the Mandala as ಹದಿಮೂರನೆಯ (13th) in the sentence on Sarasvati, Ila, Bharati; the Rigveda has 10 Mandalas; applied as printed
- **other** (pages 14): Kannada p.14 gives 1017 suktas plus 11 Valakhilya = 1028 while the table on p.12 totals 1028 suktas without them; applied as printed (English now 1,017 and 1,028)
- **other** (pages 7): Kannada p.7 names Mahadeva as author of the Vaijayanti; applied as printed (English had Yadavaprakasha)
- **other** (pages 49-50): Kannada p.49 quotes the Divyavadana with viMshatidhaa in the first clause and paMchaviMshatidhaa in the last; p.50 says 20+5 = 25 divisions and that the ancient text must have had 21; applied as printed (English now 20 and 25)
- **other** (pages 47): Kannada p.47 names the Rigvedic Paila (Pailo hOtaa vasOH putraH) while English front matter/contents and later pages (e.g. Shailalaka) use Shaila; this reading changed pp.47-48 only; the rest of the volume needs the same check
- **other** (pages 66): Kannada p.66 says that of the 11 Valakhilya suktas the mention of ten is found in Macdonell Sarvanukramani; applied as printed (English now: ten of 11)
- **other** (pages 67): Kannada p.67 prints 99 suktas for the 8th mandala of the Bashkala shakha; added to the English as printed
- **other** (pages 77): Kannada p.77 prints Vanaparva adhyaya 134 for the Kahola/Ashtavakra verses (applied as printed; English had 132)
- **other** (pages 90): Kannada p.90 prints fifteen (ಪಂಚದಶಧಾ) for the Bhartrihari variant; applied as printed (English had seventeen)
- **other** (pages 100): Kannada p.100 numbers the Kāṇva-branch list ೧, ೩, ೩, ೪ ... (no ೨); applied as printed (English row for Kaṭhāḥ now 3)
- **other** (pages 113): Kannada p.113 prints anuvāka ೩ for adhyāyas 2, 9, 12, 13, 14, 16, 18 where the English had 7, and ೩೬ as the second-dashaka total (summary table prints ೭೬); the column sums then differ from the printed totals 111 and 76; applied as printed; the English italic remark under the tables (sums agree) is now untrue
- **other** (pages 114): Kannada p.114 prints ೧೧ anuvākas for adhyāya 25 and ೫೧ mantras for adhyāya 29; the third-dashaka sums (98 and 555) then differ from the printed totals ೯೭ and ೫೫೪; applied as printed
- **other** (pages 117): Kannada p.117 prints ೩೩ mantras for adhyāya 18 and ೧೨೨ yajus for adhyāya 30 (English had 77 and 177); the mantra column then no longer adds to the printed total 1975; applied as printed
- **other** (pages 121): Kannada p.121 prints ೬೯೦೦—೨೫೨೩=೪೦೭೭; the subtraction gives 4377; applied as printed (English now 6900 − 2523 = 4077)
- **other** (pages 121): Kannada p.121 stray line prints [ ೦೫ ] where the English had [15]; applied as printed ([05])
- **other** (pages 138): Kannada p.138 kanda 1 total ೩೨೪ (English had 342; the column of the rows sums to 342); kanda 3 shows only four rows against the total 5 / 55 / 206 (the English fifth row 5, 11, 36 is removed, dashes put in its place); kanda 7 row 2 prints ೨೦ ೫೧ and the total row prints — ೧೦೭ ೨೫೨ (English had 21 and 5 / 108); applied as printed. The English table note about 652 against 651 is now out of date
- **other** (pages 139): Kannada p.139 prints 44+6+4+25=82 (the sum is 79); first-kanda adhyāya 8 prints ೧೧ ೬೭ against the printed totals 78 and 499 (the rows then sum to 79 and 529); third-kanda last row has no adhyāya number and no anuvāka count (English had 12 and 9); applied as printed; the English note about the third kanda and the sum 784 is unchanged
- **other** (pages 142): Kannada p.142 prints ೩೨ for both the Vaimānika (Vaikhānasa) and the Bāṇḍikīya (Khāṇḍikīya) headings, then ೩೩-೩೭, ೩೮; the English had 31 for the first; applied as printed (32)
- **other** (pages 150): Kannada p.150 prints the Kauthuma total ಒಟ್ಟು ೨೨೨ and Caland's number ೧೮೯ (rows 1197+294+1026+205 sum to 2722; the English had 2722 and 1869); applied as printed

## 5. Questions for the editor
102 rows in `questions.tsv`; by kind: H29 85, S13 1, S16 3, S17 4, S7 19

## 6. Files
`vol1/review/second_pass/findings.tsv` · `questions.tsv` · `batches.tsv` · `open.tsv` · `edits/` (edit files and results) · `../repair_log.md` (every English repair, heading "second pass") · `../../data/source_fixes.tsv` (edits of the supplied Kannada)

## 7. Next
the next page batch; then S3 totals (re-run the S0 checks), S4 coverage, S5 pictures, S6 records
