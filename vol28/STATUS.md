# Vol 28 — status

## Scope
Ṛgveda-saṃhitā, Maṇḍala 10, Sūktas 41–71 (Seventh Aṣṭaka, Adhyāya 8 from Sūkta 41, and the Eighth Aṣṭaka, Adhyāyas 1 and 2); printed pp. 1–674. "Bhāga 28" of the 1949–52 Kannada edition.

## Source and inputs
Three machine-read files supplied by the user (Nov 26 2026), merged losslessly into `vol28/html/rig_28.md` (`merge_md.py`: 661 pages in the inputs, 661 merged, no difference). Pictures extracted to `vol28/html/figures/` (60). `Pages: N/N` footers and `Markdown source` lines removed. Printed p. 1 has no head: `<!-- page 1 -->` inserted; `<!-- page N -->` for the headless pages 89, 93, 445. `html_pages.py` now also reads a full stop after the head number and the OCR variants `ಋದಸಂಹಿತಾ`, `ಸಾಯಣಭಾಷ್ಯಸೂಚಾ` (Vol 28).
**Pages missing in the supplied text: 162, 604, 605** (the text jumps from p. 161 to 163 and from 603 to 606; the sentence breaks). Listed in `review/page_flags.md`; not invented.
After p. 674 the file has the introduction (Pīṭhike) of the Bṛhaddevatā appendix; moved to `vol28/html/appendix_brhaddevata_intro.md`, not part of this volume's pages.
Word-meaning check against the Wikisource Pada (`pratipada_check.py 28 --source`): 56 fix-certain rows, 36 applied (one-letter filter), logged in `data/source_fixes.tsv`.

## Outputs
`vol28/Rigveda_Samhita_Vol28_English_Translation.md`, `…_Kannada_Text.md` (append-only).

## How it was made
Batch API route (HANDBOOK §6a); budget given by the user: $100, spent about $7.2 (batch of 112 windows $6.91 as collected; preface $0.07; two windows re-sent directly $0.09 and $0.15). One batch (`msgbatch_01WdC3BXLFE5UDpT62cssRhm`), then `collect` with a dispatcher loop that repaired, window by window, the faults listed in `review/repair_log.md` (Pratipadārtha lines quoted as a block, one-off block numbers, cut-off and empty answers, remarks, Cyrillic letters, a figure line, doubled Ṛk headings, stray labels).

## Status
Done through printed p. 674 (final). Audit PASS; Kannada headings written (31 sūktas, 343 Saṃhitā/Ṛk headings); preface installed; `check_labels` 1185/1185 blocks. Sūkta 41–71 present; Ṛk counts agree with the Wikisource index except Sūkta 48 (12 headings: the supplied text prints Ṛk 1 twice, NOTE).

## Open items
1. Pages 162, 604, 605 missing from the supplied text (user: supply if available).
2. NOTE questions: 174 rows in `review/notes.tsv` (plan: resolve by the default rule once the user agrees).
3. Kannada prose quoted as Sanskrit blocks in the supplied text (Eighth-Aṣṭaka title page and Pīṭhike pp. 89–99; a few lines on pp. 41, 271, 320, 629) appear as Kannada-in-Devanagari blocks in the English file.
4. Accent report: 173 Saṃhitā lines not matched without `--api` (`review/accent_report_pages.tsv`).
5. English review PDF built 2026-11-28 on `claude/vol28-pdf` (`review/vol28_full_Eng.pdf`, 1162 pages, pdf_check passes); press, year and imprint print as "[… to be supplied]"; no contents page from the original (the shared step set a table of Sūktas from the headings); Kannada print PDF not part of that build.
6. English contents page added 2026-11-28 on `claude/vol28-contents` from the user's scan (`contents_src/`; 31 sūktas, 126 rows; English PDF 1168 pages, pdf_check passes, all contents links resolve; no override needed; doubtful readings listed in `contents_src/NOTES.md`); page marks glued to the line before were separated (repair_log).
7. Not done: merge to `main`.

## Metrics
(to be filled at the end)
