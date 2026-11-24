# Vol 24 — status

*Update this file at the end of every working session. It is the only place for volume-specific state; the general rules live in `CLAUDE.md`.*

## Scope
Ṛgveda-saṃhitā Part 24: Maṇḍala 8, Sūktas 21–67 (the volume's preface) = Aṣṭaka 6, adhyāyas 2–4 (the text opens "ಆರನೆಯ ಅಷ್ಟಕದಲ್ಲಿ ಎರಡನೆಯ ಅಧ್ಯಾಯವು", closes "ಆರನೆಯ ಅಷ್ಟಕದಲ್ಲಿ ನಾಲ್ಕನೆಯ ಅಧ್ಯಾಯವು ಸಮಾಪ್ತವಾದುದು" and "|| ಶುಭಂ ಭೂಯಾತ್ ||"). Printed pp. 1–797. `volcfg.json`: `mandalas` [8], window 6. Sūktas 49–59 are the Vālakhilya sūktas (80 Ṛks; the preface says Sāyaṇa wrote no bhāṣya on them and that the bhāṣya printed is the one from the Poona Vaidika Saṃśodhana Maṇḍala edition). The volume starts at Maṇḍala 8 Sūkta 21, so Vol 21 (to 7.19) and Vol 24 are not consecutive: Vols 22–23 are the missing range. Scope read from the supplied text only.

## Source and inputs
Supplied by the user (Nov 24 2026) as two machine-read markdown files, `rig_24_1.md` (to p. 390/391) and `rig_24_2.md` (from p. 391); the files are not kept (the user has them). Changes to the supplied text, and nothing else: (1) 43 embedded pictures (22 + 21) moved to `vol24/html/figures/` by `extract_figures.py` and replaced by `[figure: …]` lines (**none of them is a title page or cover; the first is at line 2298**, so the PDF has no title-page pictures from this text); (2) the converter's footer lines `Pages: 395/395` and `Pages: 408/408` and the `Markdown source` first line of each file removed; (3) `merge_md.py` REFUSED (seam at p. 391/392: each file alone reads p. 391 differently from the merged file; the merged file is right: head "391" at the start of file 2, p. 392 has no head), so the files were joined by hand exactly as the tool does (`a.rstrip('\n') + '\n\n' + b`); (4) marker `<!-- page 1 -->` inserted before the body's opening "ॐ" (line 183).
`html_pages.py`: 758 pages, printed 1–797. Printed pages with no running head (first pages of a sūkta or section, or a head merged into the page before; not a fault, lesson 67): 55, 59, 61, 63, 64, 74, 75, 112, 128, 136, 178, 179, 180, 193, 204, 224, 225, 233, 246, 259, 260, 270, 276, 306, 338, 348, 359, 367, 392, 422, 447, 456, 489, 527, 654, 658, 698, 728, 763. Head numbers misread by OCR and corrected by the offset rule are listed by `html_pages.py` (lines 588, 1500, 2589, 2671, 2751, 3269, 7388, 7675, 9871, 14715, 19993, 20435, 20678, 21441, 22881, 31140; the head at line 14715 reads "ಸಾರಥಿಭಾಷ್ಯಸಹಿತಾ ಮಂ. ೮. ಆ. ೫. ಸಾ. ೩೯೭", i.e. Sūkta 39 or 397 misread). Front matter (lines 1–182; see `html/_layout.json`): preface "ಪಿಳಿಕೆ" (l. 1), contents (l. 39–141), abbreviations (l. 145). No scans, no numeral file. The text ends with the closing verses and a picture on the last page.

## Outputs
`vol24/Rigveda_Samhita_Vol24_English_Translation.md`, `…_Kannada_Text.md` (empty; "Done through printed p. 0"). Cost log `vol24/parts/batch_costs.md`.

## How it was made
By Sonnet agents, one per batch of three windows, no Batch API (`docs/prompts/VOL24_AGENT_PROMPT.md`). Conventions in `volcfg.json` as Vol 21.

## Status
Done through printed p. 758 after 40 agent batches (Nov 24 2026; Sūktas 21–66 present in order, Ṛk headings run without gap; `audit 24` passes; `check_labels.py 24`: 2187 English blocks = 2187 Kannada blocks, 0 under another section's label). 451 NOTE marks, 40 GLOSS marks. About 7M agent tokens (`parts/batch_costs.md`). Dispatcher repairs in `review/repair_log.md`: missing `## Sūkta 32` heading (w0220), a translator remark removed (w0344), a kn.md edit by script logged after the fact (w0533). Batch 21 was interrupted by the usage limit and resumed with SendMessage without loss. Remaining: Sūkta 67 and the colophon (pp. 759–797).

## Open items
1. (dispatcher) Preface to be translated separately into `work/preface/en.md`; installing it is a logged repair after the user's yes.

## Publication (print PDF)
Not built.

## Metrics
| windows | pages | hand-fixes | gate failures | `[?]` | inline mismatches | accent lines unmatched | QA sample | agent tokens / cost |
|---|---|---|---|---|---|---|---|---|

## Lessons from this volume

## Pointers
`docs/prompts/VOL24_AGENT_PROMPT.md`, `vol24/html/_layout.json`.
