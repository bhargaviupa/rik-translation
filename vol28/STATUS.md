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
Batch API route (HANDBOOK §6a); budget given by the user: $100.

## Status
Done through printed p. 0 (set-up finished; nothing translated yet).

## Open items
1. Pages 162, 604, 605 missing from the supplied text (user: supply if available).

## Metrics
(to be filled at the end)
