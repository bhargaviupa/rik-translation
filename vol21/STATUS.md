# Vol 21 — status

*Update this file at the end of every working session. It is the only place for volume-specific state; the general rules live in `CLAUDE.md`.*

## Scope
Ṛgveda-saṃhitā Part 21 (Jayachamarajendra Vedaratnamala no. 21): Aṣṭaka 4 adhyāyas 7–8 and Aṣṭaka 5 adhyāyas 1–2 = Maṇḍala 6, Sūktas 29–75 and Maṇḍala 7, Sūktas 1–19 (`"mandalas": [6, 7]`). Printed pp. 1–841 (preface and contents before p. 1). Editor-translator H. P. Venkata Rao, Sree Sharada Press, Mysore, 1953. Branch `claude/elegant-rubin-ivuybj`.

## Source and inputs
Supplied by the user (Nov 18 2026) as two machine-read markdown files, `rig_21_1.md` (pp. to 388) and `rig_21_2.md` (from 389); merged losslessly into `vol21/html/rig_21.md` by `tools/rv/merge_md.py` (776 pages in inputs = 776 in merged). Changes to the supplied text, and nothing else: (1) the converter's footer lines `Pages: 400/400`, `₹0` (end of part 1) and `Pages: 454/454` (end of part 2) removed; (2) the leading blank line and `Markdown source` marker of part 2 removed; (3) 94 embedded pictures moved to `vol21/html/figures/` by `tools/rv/extract_figures.py` (line replaced by `[figure: …]`); (4) the marker `<!-- page 1 -->` inserted before the body title page (line 366). The two input files are not kept in the repository (the user has them).

`html_pages.py`: 777 pages, printed 1–841. Printed pages with no running head (first pages of a sūkta or section; not a fault, lesson 67): 12, 26, 66, 92, 112, 113, 122, 123, 130, 140, 152, 153, 162, 192, 227, 232, 236, 270, 276, 284, 294, 308, 318, 334, 335, 346, 400, 418, 425, 429, 430, 431, 446, 460, 472, 486, 492, 496, 502, 512, 534, 564, 584, 585, 590, 594, 595, 602, 613, 624, 628, 634, 638, 644, 645, 646, 656, 670, 671, 676, 746, 805, 806, 832. Running-head numbers misread by OCR and corrected by the offset rule (listed by `html_pages.py`): lines 4876, 5276, 6535, 13946, 17952, 24174, 25929 (`828`→629), 26622, 27512 (`68`→668), 27634. Front matter (lines 1–365): title pages, publisher's dedication, Vedavimarśana-vidvanmaṇḍali list, preface (ಪಿಠಿಕೆ is the body's introduction at line 391; the editor's preface ends at line ~210), table of contents (ಮಂಡಲ 6 sūktas 29–75, then 7: 1–19). No abbreviations list. The text ends with `॥ ಮಂಗಳಂ ॥` on p. 841.

## Outputs
(English file, Kannada file, review files, PDFs; where the latest PDFs are.)

## How it was made
Prepared Nov 18 2026 from `vol20/CONTINUE_PROMPT_HTML.md` (no `vol21/CONTINUE_PROMPT_HTML.md` existed; the Vol 20 prompt was used as the template). Agent route, as Vol 20.

## Status
Done through printed p. 841 (the whole volume; 44 agent batches of three windows, Nov 18–19 2026; `batch.py audit 21` passes; last window w0839 ends with the colophon and benediction verses). Verified by `done` (VERIFIED for every window), `audit`, `check_labels.py 21` (0 blocks under another section's label; 2075 English blocks, 2076 Kannada blocks) and `rv import` (372 NOTE marks = 372 rows in `review/notes.tsv`).

## Open items
1. (user) 372 `**NOTE**` questions in `review/notes.tsv`; 164 `**GLOSS**` markers (quotations without a Kannada meaning: to be filled from our own edition).
2. (user) `rv import` reports 5 Sanskrit blocks differing from the source (`review/import_report.md`: 21.6.030.03.samhita, 21.6.065.03.samhita, 21.7.001.21.samhita, 21.7.018.14.pada, 21.7.019.11.samhita) and `rv structure` finds no reference verses for Maṇḍalas 6–7 (reference data missing or `--mandalas 6,7` not accepted: not investigated; `rv/` not changed).
3. (user) The accents gate left a few NOMATCH lines per window; they need `--api` with `RIK_API_KEY`.
4. (dispatcher) Hand-edits outside `batch.py fix`: see `review/repair_log.md` (w0121, w0592/w0607, spelling and remark repairs).
5. (dispatcher) The preface is translated separately into `vol21/work/preface/en.md`; installing it is a logged repair with the user's yes.
6. (user) Script candidates seen again and again (LESSONS): garbled label before Pada/bhāṣya, Pratipadārtha lines inside the bhāṣya block, unblocked Anuvāda/particulars, stray `XXI nn` lines, running heads inside blocks (pp. 123/124, 153, 336, 431, 585, 629, 656, 804–807 and others).
(Numbered; each says who must act: user / dispatcher. Counts: `[?]` in `review/doubts.tsv`, accent-report lines, inline mismatches, page flags.)

## Publication (print PDF)
(Built? date, page counts, front-matter roles, known layout issues, cover real/reconstructed.)

## Metrics (fill at the end of the volume; compare with the previous volume)
| windows | pages | hand-fixes by kind (merged heads / garbled labels / stray lines / hyphen joins / other-script letters) | gate failures | `[?]` | inline mismatches | accent lines unmatched | QA sample (pages, errors, minors) | agent tokens / cost |
|---|---|---|---|---|---|---|---|---|

## Lessons from this volume
(One line each → also added to `docs/LESSONS.md` with the rule/tool change.)

## Pointers
(Files worth reading first.)
