# Vol 29 — status

*Update this file at the end of every working session. It is the only place for volume-specific state; the general rules live in `CLAUDE.md`.*

## Scope
Ṛgveda-saṃhitā Part 29 (Jayachamarajendra Vedaratnamala no. 29, printed Mysore 1954; preface dated 22-12-1954): Aṣṭaka 8 adhyāyas 3–4 = Maṇḍala 10 Sūktas 72–94 (title page: "ಹತ್ತನೆಯ ಮಂಡಲದ ಸೂಕ್ತಗಳು ೭೨-೯೪"; the body opens "ಹತ್ತನೆಯ ಮಂಡಲದಲ್ಲಿ ಎಪ್ಪತ್ತೆರಡನೆಯ ಸೂಕ್ತವು"; the contents list reads 21 of the 23 entries with numbers, from 72 at p. 1 to 94 at p. 1003; the colophon of the fourth adhyāya and "ಮಂಗಳಂ" close the text). `volcfg.json`: `mandalas` [10], window 6. Printed pp. 1–1024 (preface, contents and abbreviations before p. 1). The preface says the part holds the Viśvakarma and Puruṣa sūktas among others. Scope read from the supplied text only.

## Source and inputs
Supplied by the user (Nov 25 2026) as three machine-read markdown files, `rig_29_1.md` (front matter and pp. 1–386), `rig_29_2.md` (pp. 387–786) and `rig_29_3.md` (pp. 787–1024); the files are not kept (the user has them). Changes to the supplied text, and nothing else: (1) 53 embedded pictures (19 + 17 + 17) moved to `vol29/html/figures/` by `extract_figures.py` and replaced by `[figure: …]` lines; the first two pictures (lines 3 and 22: printed title page and inner title) are kept for the PDF; (2) the converter's footer lines `Pages: 400/400`, `Pages: 400/400`, `Pages: 238/238` and the `Markdown source` first line of files 2 and 3 removed; (3) `merge_md.py` REFUSED (seams at pp. 386/387 and 786/787: the merged file reads the pages differently from each file alone), so the files were joined by hand (`rstrip('\n')`, then a blank line, a `---` page separator and a blank line, then the next file): **each seam keeps its `---`**; (4) marker `<!-- page 1 -->` inserted before the body's opening "## ॥ ಶ್ರೀ ॥" (line 417).
Check: the supplied text has a `---` line after every printed page; from the marker on there are 1024 chunks = 1024 printed pages (`check_page_markers.py 29`). `html_pages.py`: 912 pages read, printed 1–1024. Page numbers whose running head the splitter did not read (first pages of a sūkta, heads with OCR slips, the heads of the unnumbered pages; 112 of 1024; chunk k = printed page k; not a fault, lesson 67 and Vol 24 lessons): 15, 19, 35, 71, 80, 95, 103, 120, 135, 140, 167, 181, 182, 196, 232, 242, 255, 260, 268, 269, 280, 311, 318, 319, 349, 360, 386, 390, 447, 455, 456, 464, 472, 475, 494, 500, 518, 533, 534, 556, 560, 576, 579, 580, 581, 582, 587, 588, 600, 601, 616, 617, 619, 630, 634, 642, 643, 644, 656, 662, 670, 673, 674, 680, 700, 713, 714, 720, 736, 737, 743, 756, 757, 759, 764, 768, 772, 773, 776, 784, 785, 800, 805, 811, 814, 822, 830, 834, 835, 845, 860, 864, 869, 870, 871, 893, 897, 906, 922, 932, 941, 946, 963, 964, 970, 986, 987, 1002, 1005, 1014, 1019, 1020. Front matter (lines 1–416; see `html/_layout.json`): title pages (two pictures), board of scholars, preface (ಪೀಠಿಕೆ, l. 104–133), contents (l. 135–371, in two sections by adhyāya), abbreviations (l. 376–414). No scans, no numeral file.

## Outputs
`vol29/Rigveda_Samhita_Vol29_English_Translation.md`, `…_Kannada_Text.md` (both complete, 1024 page markers, Kannada Sūkta/Ṛk headings written), `review/` lists (notes.tsv, repair_log.md, contents_check.md, accent_report*.tsv, inline_mismatch.tsv, qa_sample.md, qa_sample_2.md). Cost log `vol29/parts/batch_costs.md`.

## How it was made
By Sonnet agents, one per batch of three windows, no Batch API (`docs/prompts/VOL29_AGENT_PROMPT.md`, as Vol 24). Conventions in `volcfg.json` as Vol 24.

## Status
**Translation complete: printed pp. 1–1024** (Nov 25 2026; 52 agent batches; the last window ends with the colophon, the closing verse and "ಮಂಗಳಂ", nothing added). `batch.py next 29` prints "no further window"; `audit 29` passes at "done through printed p. 1024"; `check_labels.py 29`: 1018 English blocks = 1018 Kannada blocks, 0 under another section's label. Maṇḍala 10 Sūktas 72–94 all present in order; every sūkta's Ṛk headings run 1…n without a gap (script check; two displaced verses are bold `**Verse N**` lines). 930 `**NOTE**` marks, 144 `**GLOSS**` marks. About 10.4M agent tokens in the 50 batches with a figure (`parts/batch_costs.md`; batches 24 and 41 lost their figures to a container restart and to the usage limit).
Dispatcher repairs (`review/repair_log.md`): displaced page p. 321 (user decision: bold `**Verse 35**`, `batch.py` made not to add a Ṛk heading under it), a stray heading, a sentence that had lost words (p. 417), a Pratipadārtha entry split by a page break (pp. 520/521), the Ṛk 9 marker/heading order (p. 553). Shared-tool changes made in this job, to be brought to main: `tools/rv/batch.py` (no Ṛk heading under a `**Verse N**` line; `fix` adds a marked page to `pages.json`), `tools/rv/check_page_markers.py` (new).

## Open items
1. (user) **Source defects for the better copy**: printed p. 321 (displaced page; Sūkta 83 Ṛk 1 has no Pratipadārtha/Bhāvārtha/English), p. 588 (repeats p. 586), the Sūkta 78 Ṛk 3 Bhāvārtha and English (cut off in the print, pp. 144–146), a Tamil stray line on many pages, garbled references and Saṃhitā/Pada/bhāṣya text in many places (all as NOTEs).
2. (user) 895 NOTE questions in `review/notes.tsv` (39 reference NOTEs were settled by the list, `review/notes_resolved.tsv`); 144 GLOSS markers (quotations without a Kannada meaning, to be filled from our own edition); the reference abbreviations missing from the BRIEF list (Upaniṣad, Śatapatha, Gītā …) cause many NOTEs: add them to the list before the second reading.
3. (user) Front matter and PDFs need the front-matter scan; contents and abbreviations (supplied lines 135–414) are for that job. Accent report: 147 lines unmatched, not applied (`--api` not run).
4. (tool) Cause of the broken `( (*…‖ (*)` brackets (12 lines, repaired) not found in `tools/rv/` (docs/LESSONS.md).
5. Judgement calls for the second reading: where the print gives no Ṛk number the agents headed the Ṛk by order with a NOTE (as in Vol 24); inline Sanskrit that could not be copied from kn.md was written in Latin letters or given in English in some windows (w1010, w1017 and others); the printed-English slips ("hrᱥband") were written as the word plainly reads with a NOTE; two QA notes left to the editor (p. 188 misprint ಅಶಿಥಿಲ, p. 95 ಇರುಚಿ "rim of the wheel").

## Publication (print PDF)
Not built.

## Metrics
| windows | pages | batches | agent tokens | hand repairs (logged) | gate failures | `[?]` | inline mismatches | accent lines unmatched | QA sample |
|---|---|---|---|---|---|---|---|---|---|
| 152 window dirs | 1024 | 52 (agent per 3 windows) | 10,284,913 for the 50 batches with a figure (batches 24, 41: none; about 10k per page); preface agent 76k | see `review/repair_log.md` (markers, preface, QA edits, one reference) | not tallied | 0 | 0 | 147 | 2 rounds × 24 pages (Opus): 2 ERROR, 11 MINOR, all repaired |

## Lessons from this volume
See `docs/LESSONS.md` (Vol 24 and Vol 29 sections).

## Pointers
`docs/prompts/VOL29_AGENT_PROMPT.md`, `vol29/html/_layout.json`.
