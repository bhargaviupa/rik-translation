# Vol 9 second pass — status report
*Made by `python3 tools/rv/sp_report.py 9` from `findings.tsv`, `questions.tsv`, `batches.tsv`, `open.tsv`; updated 2026-11-27. Format: `docs/SECOND_PASS_REPORT.md`.*

## 1. State
- **Stage:** S2 reading in page batches
- **Pages read:** 178 (1–150, 24–173, 29–178)
- **Findings:** 442 — applied 414, kept/not applied 28 (English kept: misprints and doubts settled by rule; see part 5); edits ok 454, failed 0
- **Reader tokens (batches so far):** 591k; per page 3.3k
- **Last commit:** 45b1fd40

## 2. Batches
| Batch | Pages | Findings | Applied | Edits ok / failed | Kept / not applied | Tokens | Commit | Note |
|---|---|---|---|---|---|---|---|---|
| 1 | 1–150 | 130 | 122 | 122 / 0 | 8 | 228k | ce374228 |  |
| 2 | 24–173 | 173 | 167 | 167 / 0 | 6 | 363k | 89e3bf43 |  |
| 3 | 29–178 | 170 | 165 | 165 / 0 | 5 | n/a | 45b1fd40 |  |

## 3. Findings by kind
| Kind | Applied | Kept / not applied | Total |
|---|---|---|---|
| Q1 | 252 | 0 | 252 |
| Q2 | 71 | 28 | 99 |
| S3 | 91 | 0 | 91 |

By reader: R1 442

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
- **other** (pages 263): Kannada p.263 prints supāṃ sulug (ājā) as Pā. Sū. 3-1-39 and jñityādir nityam as 7-1-39/7-1-197 (elsewhere in the volume 7-1-39 and 6-1-197); applied as printed in q57, q59, unmarked others left (found while settling q57/q59)
- **other** (pages 256, 257): English p.256 gives the saṅgrāma names as twenty-four and quarter-names as sixteen with (Ni. 3-9); Kannada p.255 prints 46 and 26 with (ನಿ. 3-20); English p.257 stena (Ni. 3-9) where Kannada p.257 prints (ನಿ. 3-19); unmarked, left (found while settling q45/q47)
- **other** (pages 269): Kannada p.269 prints citaḥ as Pā. Sū. 6-1-193 and supāṃ sulug (dasrā) as 3-1-39; applied as printed in q65, q68 (elsewhere 6-1-163, 7-1-39) (found while settling q65/q68)
- **other** (pages 277): English p.277 gives the Pārāvata/Paṇi passage as 'Ṛk 6-47-22 [as read]'; Kannada p.277 prints Ṛ. Saṃ. 6-61-1; unmarked, left (found while settling q74-q78)
- **other** (pages 278): Kannada p.278 prints citaḥ as Pā. Sū. 6-1-193 and supāṃ sulug (yuktā) as 3-1-85 (elsewhere 6-1-163 and 7-1-39); q85 applied as printed, unmarked others left (found while settling q85)
- **other** (pages 286): Kannada p.286 prints Pā. Sū. 9-1-15, 9-2-13, 9-4-48 (no ninth adhyāya; elsewhere 6-1-15, 6-2-139, 6-4-48); applied as printed in q93, q94, q96
- **other** (pages 290): English p.290 says the Vaśa sūkta Ṛ. Saṃ. 8-46 has 'three Ṛks'; Kannada p.290 prints 8-46 ರಲ್ಲಿ 33 ಋಕ್ಕುಗಳು (33 Ṛks); unmarked, left (found while settling q99)
- **other** (pages 307): Kannada p.307 prints vyatyayo bahulam as Pā. Sū. 3 1-86 (elsewhere 3-1-85); applied as printed in q120
- **other** (pages 312): Kannada p.312 prints for pratne the sūtra 'nas ca purāṇe prāt' (Pā. Sū. 5-4-2-51) and ಸಾ. ಸೂ. 3-1-39 for supāṃ sulug; English p.312 names the sūtra pratnapūrvaviśveṣvimātāl; numbers applied as printed in q129, q130, sūtra name unmarked, left
- **other** (pages 327): Kannada p.327 prints supāṃ sulug as Pā. Sū. 3-1-39 (elsewhere 7-1-39); q150 applied as printed
- **other** (pages 333): English p.333 keeps 'Printed yajñanāyopekṣamāṇāya — kept as printed [sic?]'; Kannada p.333 prints ಯಜ್ಜನಾಯಾಪೇಕ್ಷಮಾಣಾಯ (yajjanāyāpekṣamāṇāya); unmarked, left (found while settling q156)
- **other** (pages 335, 344): Kannada p.335 prints acoyat as Pā. Sū. 3-1-99 and yatonāvaḥ as 6-1-213; Kannada p.344 prints 3-1-92 and 6-1-13; each applied as printed in q162, q170, q171 (found while settling q162/q170/q171)

## 5. Questions for the editor
**0 open questions** in `questions.tsv` (the editor decides only what the rules cannot: nothing else is asked).

Settled by rule, no reading needed: 7 Kannada misprints where the English is kept (`kn_misprints.tsv`); 21 places where the English is kept unchanged and listed for the scholar sample (`decided_by_default.tsv`). Impossible or odd printed numbers applied as printed are in part 4.

## 6. Files
`vol9/review/second_pass/findings.tsv` · `questions.tsv` · `batches.tsv` · `open.tsv` · `edits/` (edit files and results) · `../repair_log.md` (every English repair, heading "second pass") · `../../data/source_fixes.tsv` (edits of the supplied Kannada)

## 7. Next
the next page batch; then S3 totals (re-run the S0 checks), S4 coverage, S5 pictures, S6 records
