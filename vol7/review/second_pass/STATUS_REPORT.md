# Vol 7 second pass — status report
*Made by `python3 tools/rv/sp_report.py 7` from `findings.tsv`, `questions.tsv`, `batches.tsv`, `open.tsv`; updated 2026-11-27. Format: `docs/SECOND_PASS_REPORT.md`.*

## 1. State
- **Stage:** S2 reading in page batches
- **Pages read:** 461 (1–75, 76–145, 145–213, 215–291, 292–342, 343–385, 387–430, 431–463)
- **Findings:** 1159 — applied 943, kept/not applied 216 (English kept: misprints and doubts settled by rule; see part 5); edits ok 953, failed 0
- **Reader tokens (batches so far):** 2211k; per page 4.8k
- **Last commit:** 36149988

## 2. Batches
| Batch | Pages | Findings | Applied | Edits ok / failed | Kept / not applied | Tokens | Commit | Note |
|---|---|---|---|---|---|---|---|---|
| 1 | 1–75 | 146 | 94 | 94 / 0 | 52 | 243k | 856b8f44 | marks q12-q161: 150 seen, 98 removed, 52 kept |
| 2 | 76–145 | 142 | 94 | 94 / 0 | 48 | 239k | e9bd4eef | marks q64-q213: 150 seen, 102 removed, 48 kept |
| 3 | 145–213 | 155 | 147 | 141 / 0 | 8 | 270k | bfbab262 | marks q112-q261: 150 seen, 139 removed, 11 kept |
| 4 | 215–291 | 193 | 157 | 157 / 0 | 36 | 357k | 0e9ccb44 | marks q123-q272: 150 seen, 114 removed, 36 kept |
| 5 | 292–342 | 164 | 145 | 145 / 0 | 19 | 325k | 92eaf008 | marks q159-q308: 150 seen, 132 removed, 18-21 kept |
| 6 | 343–385 | 123 | 107 | 107 / 0 | 16 | 262k | 330a41e3 | marks q180-q329: 150 seen, 134 removed, 16 kept |
| 7 | 387–430 | 129 | 105 | 116 / 0 | 24 | 265k | cc1e92c6 | marks q197-q346: 150 seen, 126 removed, 24 kept |
| 8 | 431–463 | 112 | 99 | 99 / 0 | 13 | 250k | 36149988 | marks q227-q376: 150 seen, 137 removed, 13 kept |

## 3. Findings by kind
| Kind | Applied | Kept / not applied | Total |
|---|---|---|---|
| Q2 | 329 | 216 | 545 |
| Q1 | 482 | 0 | 482 |
| S3 | 132 | 0 | 132 |

By reader: R1 1159

## 4. Open items (not findings)
- **other** (pages 232): Kannada p.232 prints Pā. 3-685 (īṣākṣādīnāṃ chandasi prakṛtibhāvo vaktavyaḥ); applied as printed in the English (was Pā. Sū. 6-1-[128] vārttika)
- **other** (pages 257): Kannada p.257 prints Pā. Sū. 6-1-49 for उस्यपदान्तात्; applied as printed in the English (was 6-1-[96])
- **other** (pages 447): Kannada p.447 prints Ṛ. Saṃ. 5-45-55 (no such Ṛk; sūkta 5-45 has 11 Ṛks); applied as printed in the English (was 5-[?]-[?])

## 5. Questions for the editor
**0 open questions** in `questions.tsv` (the editor decides only what the rules cannot: nothing else is asked).

Settled by rule, no reading needed: 62 Kannada misprints where the English is kept (`kn_misprints.tsv`); 155 places where the English is kept unchanged and listed for the scholar sample (`decided_by_default.tsv`). Impossible or odd printed numbers applied as printed are in part 4.

## 6. Files
`vol7/review/second_pass/findings.tsv` · `questions.tsv` · `batches.tsv` · `open.tsv` · `edits/` (edit files and results) · `../repair_log.md` (every English repair, heading "second pass") · `../../data/source_fixes.tsv` (edits of the supplied Kannada)

## 7. Next
the next page batch; then S3 totals (re-run the S0 checks), S4 coverage, S5 pictures, S6 records
