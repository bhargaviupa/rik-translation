# Vol 29 — status

*Update this file at the end of every working session. It is the only place for volume-specific state; the general rules live in `CLAUDE.md`.*

## Scope
Ṛgveda-saṃhitā Part 29 (Jayachamarajendra Vedaratnamala no. 29, printed Mysore 1954; preface dated 22-12-1954): Aṣṭaka 8 adhyāyas 3–4 = Maṇḍala 10 Sūktas 72–94 (title page: "ಹತ್ತನೆಯ ಮಂಡಲದ ಸೂಕ್ತಗಳು ೭೨-೯೪"; the body opens "ಹತ್ತನೆಯ ಮಂಡಲದಲ್ಲಿ ಎಪ್ಪತ್ತೆರಡನೆಯ ಸೂಕ್ತವು"; the contents list reads 21 of the 23 entries with numbers, from 72 at p. 1 to 94 at p. 1003; the colophon of the fourth adhyāya and "ಮಂಗಳಂ" close the text). `volcfg.json`: `mandalas` [10], window 6. Printed pp. 1–1024 (preface, contents and abbreviations before p. 1). The preface says the part holds the Viśvakarma and Puruṣa sūktas among others. Scope read from the supplied text only.

## Source and inputs
Supplied by the user (Nov 25 2026) as three machine-read markdown files, `rig_29_1.md` (front matter and pp. 1–386), `rig_29_2.md` (pp. 387–786) and `rig_29_3.md` (pp. 787–1024); the files are not kept (the user has them). Changes to the supplied text, and nothing else: (1) 53 embedded pictures (19 + 17 + 17) moved to `vol29/html/figures/` by `extract_figures.py` and replaced by `[figure: …]` lines; the first two pictures (lines 3 and 22: printed title page and inner title) are kept for the PDF; (2) the converter's footer lines `Pages: 400/400`, `Pages: 400/400`, `Pages: 238/238` and the `Markdown source` first line of files 2 and 3 removed; (3) `merge_md.py` REFUSED (seams at pp. 386/387 and 786/787: the merged file reads the pages differently from each file alone), so the files were joined by hand (`rstrip('\n')`, then a blank line, a `---` page separator and a blank line, then the next file): **each seam keeps its `---`**; (4) marker `<!-- page 1 -->` inserted before the body's opening "## ॥ ಶ್ರೀ ॥" (line 417).
Check: the supplied text has a `---` line after every printed page; from the marker on there are 1024 chunks = 1024 printed pages (`check_page_markers.py 29`). `html_pages.py`: 912 pages read, printed 1–1024. Page numbers whose running head the splitter did not read (first pages of a sūkta, heads with OCR slips, the heads of the unnumbered pages; 112 of 1024; chunk k = printed page k; not a fault, lesson 67 and Vol 24 lessons): 15, 19, 35, 71, 80, 95, 103, 120, 135, 140, 167, 181, 182, 196, 232, 242, 255, 260, 268, 269, 280, 311, 318, 319, 349, 360, 386, 390, 447, 455, 456, 464, 472, 475, 494, 500, 518, 533, 534, 556, 560, 576, 579, 580, 581, 582, 587, 588, 600, 601, 616, 617, 619, 630, 634, 642, 643, 644, 656, 662, 670, 673, 674, 680, 700, 713, 714, 720, 736, 737, 743, 756, 757, 759, 764, 768, 772, 773, 776, 784, 785, 800, 805, 811, 814, 822, 830, 834, 835, 845, 860, 864, 869, 870, 871, 893, 897, 906, 922, 932, 941, 946, 963, 964, 970, 986, 987, 1002, 1005, 1014, 1019, 1020. Front matter (lines 1–416; see `html/_layout.json`): title pages (two pictures), board of scholars, preface (ಪೀಠಿಕೆ, l. 104–133), contents (l. 135–371, in two sections by adhyāya), abbreviations (l. 376–414). No scans, no numeral file.

## Outputs
`vol29/Rigveda_Samhita_Vol29_English_Translation.md`, `…_Kannada_Text.md` (empty; "Done through printed p. 0"). Cost log `vol29/parts/batch_costs.md`.

## How it was made
By Sonnet agents, one per batch of three windows, no Batch API (`docs/prompts/VOL29_AGENT_PROMPT.md`, as Vol 24). Conventions in `volcfg.json` as Vol 24.

## Status
Done through printed p. 193 after 10 agent batches (Nov 25 2026; Sūktas 72–81 present in order, Ṛk headings run without gap; `audit 29` passes; `check_labels.py 29`: 249 English blocks = 249 Kannada blocks, 0 under another section's label). 142 NOTE marks, 48 GLOSS marks. About 2.0M agent tokens (`parts/batch_costs.md`), 180–225k per batch. Known open: the marker of printed p. 167 is missing (its running head is garbled and was not marked; its text stands under p. 166), to be repaired with the other marker repairs at the end (`check_page_markers.py 29`). Heads whose numbers disagree with the marker (9, 58, 86, 98, 126) look like OCR slips of the head, to be checked against the `---` chunks at the end.

## Open items
1. (dispatcher) Preface to be translated separately into `work/preface/en.md` (finishing job; installing it is a logged repair with the user's yes).

## Publication (print PDF)
Not built.

## Metrics
| windows | pages | hand-fixes | gate failures | `[?]` | inline mismatches | accent lines unmatched | QA sample | agent tokens / cost |
|---|---|---|---|---|---|---|---|---|

## Lessons from this volume

## Pointers
`docs/prompts/VOL29_AGENT_PROMPT.md`, `vol29/html/_layout.json`.
