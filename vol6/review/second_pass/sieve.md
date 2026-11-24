# Vol 6 second pass — S0 sieve (Nov 24 2026)

All figures are from commands run in this session. Nothing was changed in the English or in the supplied text.

## a. Pages
- Supplied files: `rig_6_1.md` (2–81), `rig_6_1_0.md` (82), `rig_6_2.md` (83–382), `rig_6_3.md` (383–619). `html_pages.load_many` gives 609 pages, printed 2–619.
- **Pages without a running head** (merged into the page before; listed, not chased, LESSONS 67): 8, 66, 216, 374, 396, 458, 476, 559, 571 (9 pages). Head-number anomalies: rig_6_2 p. 38 head read for 88; rig_6_3 head read 501 for 561 (both corrected by the neighbour rule).
- English file: 617 `### Page` sections. English pages not in the supplied text: 1 (title page), 620 (after the printer's line) and the nine headless pages above. Supplied pages with no English page: 7 and 259 (**to look at in S2**).
- The Kannada book `vol6/Rigveda_Samhita_Vol6_Kannada_Text.md` was made now (S1 step, needed as input for the checks): `tools/rv/prose_kn.py … --rk-from 2 --vol 6` (new option `--vol`, the header said "ಸಂಪುಟ 1"). It has 624 `printed` marks (609 pages + 9 "NOT IN THE SUPPLIED TEXT" marks + others as the tool writes them; to be reviewed in S1).

## b. Audit
`python3 tools/rv/batch.py audit 6` does not run: "no config vol6/volcfg.json" (legacy volume, no config). Invariants checked instead: page sequence (above), one trailing progress note in the English file (present: "VOLUME 6 IS COMPLETE … pp. 1–620"), no Telugu letters or digits in the Kannada file.

## c. Script checks
| Check | Tool | Compared | Result |
|---|---|---|---|
| Quotations, `[?]`, references, numbers, page by page | `recheck.py 6` | 617 English pages vs. supplied pages ±1 | `[?]` 565 on 251 pages; Devanagari quotations that differ: 191 on 129 pages; reference only in the English: 1,102 on 527 pages; reference only in the supplied text: 374 on 225 pages; plain numbers only in the English: 223 on 132 pages; 56 pages with none of these |
| Unambiguous number corrections | `recheck_numbers.py 6` (list only) | all references | 32 proposed (all references), 1,070 left manual: `vol6/review/recheck/numbers_candidates.tsv` (e.g. p. 25 `4-51-4`→`4-51-3`, p. 102 `6-66-3`→`6-66-33`). **Not applied** (S3, and only after the S2 reading) |
| Abbreviations vs. `rv/references.tsv` | `refs_apply.py 6` (preview) | whole volume | 144 places in the English/check, 164 in the Kannada file where the Kannada file as made now differs; "the English already had the right form, or reads the number differently". **Not written** (the reference-corrector agent does that) |
| Letters of other scripts | inline script | whole English and Kannada files | English: no Arabic, Cyrillic, Greek or Telugu; **one Devanagari letter inside a Latin word: p. 342 `alloपaḥ`** (to repair in S3, the reading `alloपaḥ` = Latin letters + Devanagari प, the Kannada decides). English has 1,156 Kannada letters on 65 pages (77 lines): front-matter description lines and remarks (e.g. pp. 1, 2, 16, 19, 21, 24, 282, 426, 454), to be read in S2. Kannada file: 0 Devanagari letters (the danda only), 0 Telugu |
| Inventory of legacy marks | grep | English file | `[?]` 568, `[sic]` 49, `**GLOSS**` 115, "as read" 738, "as printed" 640, "as supplied" 1, italic bracket remarks `*[` 40; none removed |

**Caveats on the counts.** recheck.py aligns by letters and treats a reference printed in a different form (e.g. `64-1` for Sūkta 64 Ṛk 1, Pāṇini `6-4-111` that the Kannada prints as `೬-೪-೧೧೧`) as different, so the reference figures are an upper bound; each place still has to be read. The 191 quotation differences are in inline Sanskrit of the commentary (R3).

## d. Pages with the most flagged places (quotation differences + reference/number differences)

| page | `[?]` | quote diffs | ref only EN | ref only supplied | number only EN |
|---|---|---|---|---|---|
| 510 | 4 | 0 | 6 | 6 | 7 |
| 587 | 10 | 4 | 5 | 6 | 3 |
| 527 | 5 | 0 | 9 | 4 | 3 |
| 616 | 4 | 0 | 7 | 8 | 1 |
| 618 | 9 | 0 | 5 | 10 | 1 |
| 518 | 2 | 2 | 6 | 3 | 3 |
| 258 | 0 | 0 | 4 | 3 | 5 |
| 567 | 3 | 0 | 10 | 0 | 2 |
| 454 | 1 | 0 | 4 | 0 | 7 |
| 606 | 1 | 0 | 6 | 3 | 2 |
| 381 | 0 | 0 | 3 | 2 | 5 |
| 515 | 6 | 4 | 3 | 2 | 1 |
| 543 | 4 | 0 | 7 | 1 | 2 |
| 617 | 4 | 2 | 3 | 3 | 2 |
| 16 | 1 | 7 | 2 | 0 | 0 |
| 49 | 0 | 0 | 8 | 1 | 0 |
| 60 | 0 | 0 | 6 | 0 | 3 |
| 263 | 0 | 0 | 4 | 4 | 1 |
| 267 | 1 | 1 | 4 | 4 | 0 |
| 278 | 1 | 0 | 5 | 4 | 0 |
| 459 | 0 | 0 | 5 | 4 | 0 |
| 536 | 2 | 0 | 6 | 1 | 2 |
| 540 | 2 | 0 | 6 | 2 | 1 |
| 546 | 1 | 4 | 3 | 1 | 1 |
| 547 | 8 | 1 | 5 | 1 | 2 |
| 57 | 0 | 1 | 6 | 0 | 1 |
| 95 | 0 | 0 | 4 | 1 | 3 |
| 139 | 0 | 0 | 5 | 2 | 1 |
| 154 | 1 | 0 | 3 | 0 | 5 |
| 170 | 1 | 0 | 3 | 3 | 2 |
| 203 | 1 | 1 | 3 | 2 | 2 |
| 225 | 0 | 0 | 4 | 2 | 2 |
| 399 | 0 | 0 | 5 | 3 | 0 |
| 425 | 0 | 0 | 5 | 2 | 1 |
| 467 | 1 | 0 | 3 | 0 | 5 |
| 507 | 0 | 1 | 3 | 1 | 3 |
| 545 | 4 | 4 | 2 | 2 | 0 |
| 574 | 0 | 0 | 6 | 2 | 0 |
| 575 | 1 | 0 | 5 | 1 | 2 |
| 6 | 2 | 0 | 5 | 0 | 2 |

Full table: `vol6/review/recheck/summary.tsv` (per page); detail per page in `vol6/review/recheck/pNNNN.md`.

## e. Size of S2
About 560 of 609 pages carry at least one flagged place; the pilot (10 pages from the middle) and the 30-page batches are therefore a full read of the volume, not a read of flagged pages only.
