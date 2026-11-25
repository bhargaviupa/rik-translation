# Vol 1 second pass — status report
*Made by `python3 tools/rv/sp_report.py 1` from `findings.tsv`, `questions.tsv`, `batches.tsv`, `open.tsv`; updated 2026-11-25. Format: `docs/SECOND_PASS_REPORT.md`.*

## 1. State
- **Stage:** S2 reading in page batches
- **Pages read:** 310 of 720 (360–369, 1–30, 31–60, 61–90, 91–120, 121–150, 151–180, 181–210, 211–240, 241–270, 271–300)
- **Findings:** 1172 — applied 1001, questions 171; edits ok 1005, failed 0
- **Reader tokens (batches so far):** 3040k; per page 9.8k
- **Last commit:** 3514965

## 2. Batches
| Batch | Pages | Findings | Applied | Edits ok / failed | Questions | Tokens | Commit | Note |
|---|---|---|---|---|---|---|---|---|
| pilot | 360–369 | 73 | 52 | 31 / 0 | 21 | 169k | f594e7e | pilot; 52 edits first applied, then 21 Devanagari edits (and 6 IAST partners) reverted by the new sp_sanskrit gate, 6 re-applied after the word-join refinement: net 31 English edits stand; 15 citation lines are questions; English not page-aligned to the Kannada on these pages (judged by content) |
| 2 | 1–30 | 134 | 110 | 110 / 0 | 24 | 349k | b195d7a | 110 edits (31 S7 via sp_sanskrit, 20 S13 names, ~30 numbers, ~25 sense); English not page-aligned (Page 4 carries Kannada 4–6, Page 10 carries 10–11, Page 15–16 combined, pp. 17–24 'gap filled' block); numbers taken as printed that look odd are in open.tsv; three longer rewrites on pp. 2, 9, 30 for re-reading |
| 3 | 31–60 | 134 | 118 | 118 / 0 | 16 | 344k | 938a30a | 118 edits (28 S7 via sp_sanskrit, 21 S13, 21 S14, 11 S15, 9 S16, 9 S17; many name/number repairs); English sections missing for Kannada pp. 35, 48, 52 (text under Page 34, 'Pages 46–47', Page 51); Kannada p. 54 text sits under the p. 53 mark; Paila vs Shaila: the Devanagari block 'शैलो होता' and the contents entry still say Shaila (open item) |
| 4 | 61–90 | 143 | 131 | 131 / 0 | 12 | 320k | 7fae0cb | 131 edits (45 S7 via sp_sanskrit, ~86 R1: names, senses, numbers, omissions); English sections not aligned (p. 73 text under Page 72; Māṇḍūkeya section starts at Page 79 vs Kannada 80–82); some longer rewrites where the English sentence was wrong (pp. 69, 74, 75, 83); 4 odd printed numbers in open.tsv |
| 5 | 91–120 | 138 | 121 | 121 / 0 | 17 | 297k | 96c32e1 | 121 edits (55 S7, 22 S1 + 7 S3 numbers incl. table digits on p. 113); pp. 91–94 in the main English file, 95–120 in the Gaps file; several Kannada numerals contradict the Kannada's own totals (p. 113, 114, 117; p. 100 Kāṇva list): applied as printed, 4 rows in open.tsv; the English italic remark on p. 113 that column sums agree is now untrue (legacy remark kept) |
| 6 | 121–150 | 93 | 71 | 96 / 0 | 22 | 353k | a98e5a2 | 96 edits (25 Devanagari/IAST pairs via sp_sanskrit, 25 number repairs); Kannada table numerals applied as printed even where they contradict the Kannada's own totals (pp. 121, 138, 139, 142, 150: 6 rows in open.tsv; English rows without a Kannada counterpart blanked/dashed on pp. 138–139); legacy remarks contradicted by the edits left (pp. 138, 150, 123–124) |
| 7 | 151–180 | 178 | 162 | 162 / 0 | 16 | 344k | 0d0d282 | 162 edits (96 Devanagari/IAST repairs via sp_sanskrit, 22 S1 + 1 S3, 28 S13 names); where the Kannada word is a plausible misprint and the English had another reading the Kannada was followed as printed and flagged as a question (pp. 166, 178); pp. 151–167 in the Gaps file, 168–180 in the main file; 7 open.tsv rows (Kannada totals/branch numbers that do not fit) |
| 8 | 181–210 | 79 | 71 | 71 / 0 | 8 | 317k | d2c93de | 71 edits (28 S14 sense, 12 S13 names, 9 S16, 8 S2, 5 S3, 4 S15, 4 S1, 1 S7), 8 Gaps index count rows corrected; first batch under the Nov 25 method (no questions: 15 kn_misprints, 7 decided_by_default rows; no Devanagari/IAST lines edited); Kannada p. 198 block holds printed 198+199; an older '## Page 191' summary in the main file (two-level heading) is out of sp_apply's reach (listed in decided_by_default) |
| 9 | 211–240 | 87 | 74 | 74 / 0 | 13 | 279k | 0a76ccd | 74 edits (24 S14 sense, 16 S13 names, 12 S3 + 11 S1 numbers, 5 S16, 4 S15); the supplied Kannada p. 215 is a copy of p. 216 (true p. 215 absent: English p. 215 unchecked); several paragraphs on pp. 214, 217, 232 replaced as wrong as a whole; Kannada table references applied as printed even where odd (7-1-0 p. 224, p. 239 numbering, 1237 vs 80 years: open.tsv) |
| 10 | 241–270 | 55 | 46 | 46 / 0 | 9 | 268k | 3a47bde | 46 edits (33 R6 names/terms, 13 R1 incl. whole-paragraph replacements on pp. 247, 248, 253, 254, 257, 258, 260 where the English was wrong as a whole); no page shifts; p. 241 Kannada 101 sūktas vs quoted Sanskrit 1001 applied as printed (open.tsv); p. 258 Chaturvedasvāmin account has no English (not added) |
| 11 | 271–300 | 58 | 45 | 45 / 0 | 13 | TOK10 | 3514965 | 45 edits (18 S14 sense, 10 S1 chapter/heading numbers, 6 S13, 6 S16, 4 S2 removals, 3 S15); chapter numbers now follow the Kannada (p. 284 ch. 16, p. 285 ch. 17, p. 296 ch. 18); heading numbers 7→3/2 on pp. 271, 277, 283, 291 and Kṣura's date 1290→190 on p. 276 applied as printed (open.tsv); English p. 270 already holds the first lines of Kannada p. 271 |

## 3. Findings by kind
| Kind | Applied | Questions | Total |
|---|---|---|---|
| S7 | 352 | 21 | 373 |
| S14 | 189 | 2 | 191 |
| S13 | 178 | 13 | 191 |
| S1 | 120 | 1 | 121 |
| H29 | 0 | 119 | 119 |
| S16 | 50 | 3 | 53 |
| S3 | 38 | 0 | 38 |
| S2 | 29 | 0 | 29 |
| S15 | 29 | 0 | 29 |
| S17 | 16 | 12 | 28 |

By reader: R1 560, R3 367, R6 245

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
- **other** (pages 151): Kannada p.151 prints 959 more mantras for the Jaiminīya branch and 3681 in all, 182 fewer for Caland's 1687; the Kauthuma figures do not fit both (3681-959=2722, the p.150 total); English had 95; applied as printed (959)
- **other** (pages 153-154): Kannada pp.153-154 print the branch numbers ೧೨ (Kālabavinaḥ, after ೯), ೧೧ (Śāṭkāyaninaḥ), ೨ (Rauriki, before ೧೩), ೧೫, ೧೬; the English had 10 and 12; applied as printed (12 and 2)
- **other** (pages 156): Kannada p.156 prints the Brahmāṇḍa Purāṇa reference as (೨-೩೫-೭೧ ಮತ್ತು ೨), the English had 71 and 72; applied as printed (71 and 2)
- **other** (pages 164): English p.164 note 'The figures are not reproduced because their digits are unreadable' stands beside the figures 4627 and 4432, which agree with Kannada ೪೬೨೭ and ೪೪೩೨; remark left, the digits can now be read
- **other** (pages 165): Kannada p.165 numbers the branch heading ೨. ಬ್ರಹ್ಮವದಾಃ after ೬. ಜಲದಾಶಿ and before ೮; English had 7; applied as printed (2)
- **other** (pages 166): Kannada p.166 prints ೬೦೨೦ ಋಕ್ಕುಗಳು for the Cāraṇavaidya saṃhitā while its quoted verse says six thousand and twenty-six (ṣaṭsahasram … ṣaḍviṃśatiḥ); the English prose 6020 stands as printed
- **other** (pages 173): Kannada p.173 says the Kauṣītakī-brāhmaṇa follows the Bāṣkala branch although p.172 equates the Kauṣītakī brāhmaṇa with the Śāṅkhāyana branch; English changed to Bashkala as printed
- **other** (pages 181, 182): Kannada p.181 heading prints ವಾಸಿಷ್ಠರು—೮ while its seven names and the p.182 table give 7; the English heading carries 8 as printed
- **other** (pages 202): Kannada p.202 prints [0] for ವಿಹವ್ಯಃ ಆಂಗಿರಸಃ 10-128 (no mantras); English keeps [0] as printed
- **other** (pages 224): Kannada p.224 table prints ೭ ೧ ೦ (7-1-0) for agnim naro....; impossible reference, applied as printed (English was 7-1-1)
- **other** (pages 239): Kannada p.239 numbers the points (೪) then (೬), skipping 5, and prints the (೬) line twice (second line has Yaska correctly); applied as printed ((6))
- **other** (pages 240): Kannada p.240 prints Anandatirtha 1197-1237 while the Kannada text says he lived 80 years; applied as printed (English was 1197-1277)
- **page-absent** (pages 215): The supplied Kannada p. 215 is a copy of p. 216 (running head 216); the true p. 215 text is not in the file, so English p. 215 could not be checked (the supplied file needs a new p. 215)
- **other** (pages 241): Kannada p.241 prints 101 suktas of the Rigveda while the quoted Sanskrit says thousand-and-one (ekottarasahasra); applied as printed (English had 1,001)
- **other** (pages 271): Kannada p.271 numbers the Adityadarshana section ೩ although the list had reached ೬ (Halayudha) on p.270 and ೮ (Devapala) follows on p.272; applied as printed (English was 7)
- **other** (pages 276): Kannada p.276 prints Kshura as about C.E. ೧೯೦ (190), although Sayana (14th c.) quotes him; applied as printed (English was 1290)
- **other** (pages 277): Kannada p.277 numbers the Venkatesha section 2 (Arabic numeral) after ೬ Sayana; applied as printed (English was 7)
- **other** (pages 283): Kannada p.283 numbers the Gunavishnu section ೨ after ೬ Shobhakara; applied as printed (English was 7)
- **other** (pages 291): Kannada p.291 numbers the Atharvaveda Pada-patha section ೨ after ೬ Samaveda; applied as printed (English was 7)
- **other** (pages 300): Kannada p.300 gives the Hiranyagarbha hymn as Mandala 10, hymn 124; applied as printed (English had Mandala 1, ninth section)

## 5. Questions for the editor
**0 open questions** in `questions.tsv` (the editor decides only what the rules cannot: nothing else is asked).

Settled by rule, no reading needed: 147 Kannada misprints where the English is kept (`kn_misprints.tsv`); 41 places where the English is kept unchanged and listed for the scholar sample (`decided_by_default.tsv`). Impossible or odd printed numbers applied as printed are in part 4.

## 6. Files
`vol1/review/second_pass/findings.tsv` · `questions.tsv` · `batches.tsv` · `open.tsv` · `edits/` (edit files and results) · `../repair_log.md` (every English repair, heading "second pass") · `../../data/source_fixes.tsv` (edits of the supplied Kannada)

## 7. Next
the next page batch; then S3 totals (re-run the S0 checks), S4 coverage, S5 pictures, S6 records
