# Vol 1 second pass — status report
*Made by `python3 tools/rv/sp_report.py 1` from `findings.tsv`, `questions.tsv`, `batches.tsv`, `open.tsv`; updated 2026-11-24. Format: `docs/SECOND_PASS_REPORT.md`.*

## 1. State
- **Stage:** S2 reading in page batches
- **Pages read:** 70 of 720 (360–369, 1–30, 31–60)
- **Findings:** 341 — applied 280, questions 61; edits ok 259, failed 0
- **Reader tokens (batches so far):** 518k; per page 7.4k
- **Last commit:** @C@

## 2. Batches
| Batch | Pages | Findings | Applied | Edits ok / failed | Questions | Tokens | Commit | Note |
|---|---|---|---|---|---|---|---|---|
| pilot | 360–369 | 73 | 52 | 31 / 0 | 21 | 169k | f594e7e | pilot; 52 edits first applied, then 21 Devanagari edits (and 6 IAST partners) reverted by the new sp_sanskrit gate, 6 re-applied after the word-join refinement: net 31 English edits stand; 15 citation lines are questions; English not page-aligned to the Kannada on these pages (judged by content) |
| 2 | 1–30 | 134 | 110 | 110 / 0 | 24 | 349k | b195d7a | 110 edits (31 S7 via sp_sanskrit, 20 S13 names, ~30 numbers, ~25 sense); English not page-aligned (Page 4 carries Kannada 4–6, Page 10 carries 10–11, Page 15–16 combined, pp. 17–24 'gap filled' block); numbers taken as printed that look odd are in open.tsv; three longer rewrites on pp. 2, 9, 30 for re-reading |
| 3 | 31–60 | 134 | 118 | 118 / 0 | 16 | TOK2 | @C@ | 118 edits (28 S7 via sp_sanskrit, 21 S13, 21 S14, 11 S15, 9 S16, 9 S17; many name/number repairs); English sections missing for Kannada pp. 35, 48, 52 (text under Page 34, 'Pages 46–47', Page 51); Kannada p. 54 text sits under the p. 53 mark; Paila vs Shaila: the Devanagari block 'शैलो होता' and the contents entry still say Shaila (open item) |

## 3. Findings by kind
| Kind | Applied | Questions | Total |
|---|---|---|---|
| S7 | 105 | 18 | 123 |
| S14 | 44 | 0 | 44 |
| S13 | 44 | 0 | 44 |
| H29 | 0 | 37 | 37 |
| S1 | 19 | 0 | 19 |
| S2 | 16 | 0 | 16 |
| S15 | 16 | 0 | 16 |
| S3 | 15 | 0 | 15 |
| S17 | 10 | 4 | 14 |
| S16 | 11 | 2 | 13 |

By reader: R1 137, R3 125, R6 79

## 4. Open items (not findings)
- **other** (pages 13): Kannada p.13 prints the total of mantras as ೧೦೦೫೨ (10052) while p.12 and the table print 10552; applied as printed (English now 10,052)
- **other** (pages 14): Kannada p.14 gives the Mandala as ಹದಿಮೂರನೆಯ (13th) in the sentence on Sarasvati, Ila, Bharati; the Rigveda has 10 Mandalas; applied as printed
- **other** (pages 14): Kannada p.14 gives 1017 suktas plus 11 Valakhilya = 1028 while the table on p.12 totals 1028 suktas without them; applied as printed (English now 1,017 and 1,028)
- **other** (pages 7): Kannada p.7 names Mahadeva as author of the Vaijayanti; applied as printed (English had Yadavaprakasha)
- **other** (pages 49-50): Kannada p.49 quotes the Divyavadana with viMshatidhaa in the first clause and paMchaviMshatidhaa in the last; p.50 says 20+5 = 25 divisions and that the ancient text must have had 21; applied as printed (English now 20 and 25)
- **other** (pages 47): Kannada p.47 names the Rigvedic Paila (Pailo hOtaa vasOH putraH) while English front matter/contents and later pages (e.g. Shailalaka) use Shaila; this reading changed pp.47-48 only; the rest of the volume needs the same check

## 5. Questions for the editor
51 rows in `questions.tsv`; by kind: H29 37, S16 2, S17 4, S7 18

## 6. Files
`vol1/review/second_pass/findings.tsv` · `questions.tsv` · `batches.tsv` · `open.tsv` · `edits/` (edit files and results) · `../repair_log.md` (every English repair, heading "second pass") · `../../data/source_fixes.tsv` (edits of the supplied Kannada)

## 7. Next
the next page batch; then S3 totals (re-run the S0 checks), S4 coverage, S5 pictures, S6 records
