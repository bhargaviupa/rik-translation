# Vol 1 second pass — S0 sieve (Nov 24 2026)

All figures are from commands run in this session. Nothing in the English or in the supplied text was changed by S0.

## a. Pages
- Supplied files: `rig_1_1.md` (front matter and pp. 1–224), `rig_1_2.md` (pp. 225–572/574), `rig_1_3.md` (pp. 575–720). `prose_kn.py … --rk-from 606` gives **707 pages, printed 1–720**. Printed pp. 17–24, which the old scans lacked, **are present** in the supplied text.
- **Without text in the supplied files (13):** 54, 199, 345, 409, 422, 428, 473, 573, 574, 594, 595, 651, 716 (heads missing or pages absent; listed, not chased, LESSONS 67; 573–574 and 594–595 are two consecutive pages each and need a look in S2).
- English files: `Rigveda_Samhita_Vol1_English_Translation.md` (601 `### Page` sections) and `…_Gaps_English_Translation.md` (119); `recheck.py` reads both. English pages not in the supplied text: 54, 199, 409, 422, 428, 473, 573, 574, 651. Supplied pages with no English page: 5, 11, 15, 16, 35, 46, 47, 48, 52, 73, 372, 373, 447, 717, 718, 719, 720 (to look at in S2).
- Kannada book: the old file made from HTML was renamed `vol1/kannada/Rigveda_Samhita_Vol1_Kannada_Text_OLD_scan_html.md`; the new one is `vol1/Rigveda_Samhita_Vol1_Kannada_Text.md` (`tools/rv/prose_kn.py … --front vol1/html/rig_1_1.md --rk-from 606 --vol 1`): 720 page marks, in order, no duplicates, 13 marked "NOT IN THE SUPPLIED TEXT"; 0 Devanagari letters (danda excepted); 57 stray-line notes as the shared tool writes them.

## b. Audit
`python3 tools/rv/batch.py audit 1` is not available (legacy volume, no `volcfg.json`). Invariants checked by script: page marks in order; 720 marks; no duplicate; English page headings exist for 720 − 9 pages.

## c. Script checks
| Check | Tool | Result |
|---|---|---|
| Quotations, `[?]`, references, numbers per page | `recheck.py 1` (715 English pages vs. supplied pages ±1) | `[?]` 116 on 73 pages; Devanagari quotations that differ 421 on 230 pages; reference only in the English 521 on 171 pages; reference only in the supplied text 796 on 143 pages; plain numbers only in the English 613 on 186 pages; 245 pages with none of these |
| Anchored number corrections | `recheck_numbers.py 1` (list only) | 2 proposed, 488 left manual (`vol1/review/recheck/numbers_candidates.tsv`) |
| Reference names | `refs_apply.py 1` preview | 178 English places, 206 Kannada places (not written) |
| Letters of other scripts | inline | English: 1 Cyrillic letter (not yet located); Kannada letters in the English 237 + 43 (headings, remarks, quotations); Kannada book: 1 Telugu letter |
| Legacy marks, English main / Gaps | grep | `[?]` 104 / 14; `[sic]` 0 / 14; `GLOSS` 0 / 0; "as read" 77 / 16; "as printed" 44 / 92; italic bracket remarks 11 / 2 |

Pages with most flagged places: 198 (89), 191 (61), 201 (51), 197 (49), 203 (48), 196 (47), 190 (46), 204 (44), 715 (44), 200 (43). Caveat as for Vol 6: recheck.py counts a reference printed in another form as a difference, so reference figures are an upper bound; the 796 references only in the supplied text are many because the Gaps and skipped ranges (pp. 95–167, 191–205, 261–283, 288–295) have thin English.

## d. Size of S2
475 of 715 compared pages carry at least one flagged place. S2 is a full read of 720 pages (about 24 batches of 30; Vol 6 cost 8.6k tokens a page).

## S3 addendum — before and after (Nov 25 2026, after the last batch)
| Check (`recheck.py 1`, same tool) | S0 | After S2 repairs |
|---|---|---|
| `[?]` in the English | 116 on 73 pages | 106 on 66 pages (108 by a plain count) |
| Devanagari quotations that differ | 421 on 230 pages | 390 on 221 pages (Sanskrit lines were not edited by this pass: derived data) |
| References only in the English | 521 on 171 pages | 475 on 146 pages |
| References only in the supplied text | 796 on 143 pages | 783 on 129 pages |
| Plain numbers only in the English | 613 on 186 pages | 573 on 165 pages |
| Pages with none of these | 245 | 272 |
| `recheck_numbers.py` manual | 488 | 443 (1 anchored correction applied) |
| Reference names (`refs_apply.py 1 --write`) | 178 English + 206 Kannada places | written: Kannada 206, English 2; preview now empty |
| Other scripts in the English | 1 Cyrillic letter (p. 562) | 0 (replaced) |
| Legacy marks `[?]` / `[sic]` / "as read" / "as printed" | 118 / 14 / 93 / 136 | 108 / 14 / 91 / 127 |
