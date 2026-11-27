# Vol 9 second pass — status report
*Made by `python3 tools/rv/sp_report.py 9` from `findings.tsv`, `questions.tsv`, `batches.tsv`, `open.tsv`; updated 2026-11-27. Format: `docs/SECOND_PASS_REPORT.md`.*

## 1. State
- **Stage:** S2 reading in page batches
- **Pages read:** 173 (1–150, 24–173)
- **Findings:** 295 — applied 267, kept/not applied 28 (English kept: misprints and doubts settled by rule; see part 5); edits ok 289, failed 0
- **Reader tokens (batches so far):** 228k; per page 1.3k
- **Last commit:** 89e3bf43

## 2. Batches
| Batch | Pages | Findings | Applied | Edits ok / failed | Kept / not applied | Tokens | Commit | Note |
|---|---|---|---|---|---|---|---|---|
| 1 | 1–150 | 130 | 122 | 122 / 0 | 8 | 228k | ce374228 |  |
| 2 | 24–173 | 173 | 167 | 167 / 0 | 6 | n/a | 89e3bf43 |  |

## 3. Findings by kind
| Kind | Applied | Kept / not applied | Total |
|---|---|---|---|
| Q1 | 162 | 0 | 162 |
| Q2 | 59 | 28 | 87 |
| S3 | 46 | 0 | 46 |

By reader: R1 295

## 4. Open items (not findings)
- **other** (pages 7): Kannada p.7 gives "prakṛtyaikāc" as Pā. Sū. 6-4-163, the English (p.7 grammar remark) says 6-1-197 "as printed"; unmarked, left (found while settling q21)
- **other** (pages 59): English p.59 (sumnāvarī): sixteen names of Uṣas cited "(Ni. 3-9)"; Kannada p.59 prints (ನಿ. 2-19); unmarked, left (found while settling q79)
- **other** (pages 60): English p.60 (sūnṛtā): names of Uṣas cited "(Ni. 3-9)"; Kannada p.60 prints (ನಿ. 2-19) for the Uṣas names and (ನಿ. 3-9) for the food names; unmarked, left (found while settling q81)
- **other** (pages 148): Kannada p.148 prints ತಸೌ ಮತ್ವರ್ಥೇ (ಪಾ. ಸೂ. 1-4-19); the English p.147/148 cites "tasau matvarthe" without a number; unmarked, left (found while settling q55)
- **other** (pages 181): English p.181 (Vimada): "Ṛ. Saṃ. 10-20-10 [as read], 10-2?-?" vs Kannada 10-20-10; 10-27-7, and "Atharvaveda 6-26-1-? / Aitareya Brāhmaṇa 5-5-1-?" vs Kannada Atharvaveda 4-29-4, Aitareya Brāhmaṇa 5-5-1; unmarked, left (found while settling q84)
- **other** (pages 181): Kannada p.181 prints the impossible references 11-25-10 and 1-211-13 (no maṇḍala 11, no sūkta 1-211); applied as printed in q83
- **other** (pages 182): English p.182 (barhiḥ): water names cited "(Ni. 1-112-19)"; Kannada p.182 prints (ನಿ. 2-24); unmarked, left (found while settling q86)
- **other** (pages 194): English p.194 (Tugra): "Ṛ. Saṃ. 6-20-8 [as read], 6-5-22-? and 10-49-4 [as read]"; Kannada p.194 prints 6-20-8; 6-26-4; 10-49-4; unmarked, left (found while settling q105)
- **other** (pages 198): English p.197/198: "nalopaḥ prātipadikāntasya, Pā. Sū. 8-2-16" unmarked; Kannada p.198 attaches (ಪಾ. ಸೂ. 8-2-16) to ಅನೋ ನುಟ್ (applied in q112); left
- **other** (pages 246): English p.246: "nine-hundred-and-ninety [as read — ombhattu sala tombhattu]"; Kannada p.246 prints ಒಂಬತ್ತು ಸಲ ತೊಂಬತ್ತು 9X90=810; unmarked, left (found while settling q173)

## 5. Questions for the editor
**0 open questions** in `questions.tsv` (the editor decides only what the rules cannot: nothing else is asked).

Settled by rule, no reading needed: 7 Kannada misprints where the English is kept (`kn_misprints.tsv`); 21 places where the English is kept unchanged and listed for the scholar sample (`decided_by_default.tsv`). Impossible or odd printed numbers applied as printed are in part 4.

## 6. Files
`vol9/review/second_pass/findings.tsv` · `questions.tsv` · `batches.tsv` · `open.tsv` · `edits/` (edit files and results) · `../repair_log.md` (every English repair, heading "second pass") · `../../data/source_fixes.tsv` (edits of the supplied Kannada)

## 7. Next
the next page batch; then S3 totals (re-run the S0 checks), S4 coverage, S5 pictures, S6 records
