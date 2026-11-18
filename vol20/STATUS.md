# Vol 20 — status

*Update this file at the end of every working session. It is the only place for volume-specific state; the general rules live in `CLAUDE.md`.*

## Scope
Read from the supplied text (title lines, sūkta heading lines, closing lines); not checked against a scan. Maṇḍala 5 Sūktas 63–87 (to the end of Maṇḍala 5, Fourth Aṣṭaka) and Maṇḍala 6 Sūktas 1–28 (Fourth Aṣṭaka, Adhyāyas 5–6; the text's last sūkta heading is Sūkta 28, closing lines "ಶುಭಂ ಭೂಯಾತ್ | ಮಂಗಳಂ" and the colophon of the sixth adhyāya). Printed pp. 1–844. `volcfg.json`: `mandalas` [5, 6], window 6. The sūkta numbers printed in a few heading lines are OCR-damaged (e.g. "೬೦" for 70, "೨" for 22, "ಅನುವಾಕ—೨೫"): the translator writes the number the text prints and marks a NOTE; to be confirmed when the sequence is checked at the end of each stage.

## Source and inputs
`vol20/html/rig_20.md`: the user's two files (`rig_20_1.md`, `rig_20_2.md`, supplied Nov 18 2026) merged. Changes made to the supplied text, all mechanical: (1) the 68 embedded pictures (23 + 45) were extracted to `vol20/html/figures/` and replaced by `[figure: …]` lines; (2) the converter's `Pages: 400/400` and `Pages: 465/465` footer lines and the second file's `Markdown source` line (and the blank line before it) were removed; (3) **one line `<!-- page 1 -->` inserted before "ॐ || ಶ್ರೀಃ ||" (line 744)**. `merge_md.py` REFUSED (the seam at pp. 378–381: each file alone splits pp. 378 and 381 as heads, the merged file reads 379/380 as pages and 378/381 as merged into the page before: the splitter's neighbour rule), so the two files were concatenated by hand with the same single blank-line join the tool uses; the merged file splits into 814 pages, printed 1–844.
Page numbers without a running head (first pages of a sūkta/section; not a fault, lesson 67): 30, 38, 140, 162, 188, 214, 223, 314, 324, 339, 340, 366, 378, 381, 384, 385, 416, 442, 446, 458, 468, 504, 590, 608, 612, 636, 647, 732, 764, 806 (30 of 844). Splitter anomalies to watch at `next` (head misread, number used): p. 385→386 line 16280, p. 3→394, p. 5→455, p. 665→666.
Front matter (lines 1–743, no window covers it): title lines and board of scholars (l. 100), the volume's preface (ಪೀಠಿಕೆ, from l. 129), contents (from l. 463), abbreviations (l. 705). `vol20/html/_layout.json` records approximate line numbers. No scans, no numeral file.

## Outputs
`vol20/Rigveda_Samhita_Vol20_English_Translation.md` and `…_Kannada_Text.md` (empty; progress note "Done through printed p. 0"). Cost log `vol20/parts/batch_costs.md`.

## How it is made
By Sonnet agents, one per batch of three windows, no Batch API (`CONTINUE_PROMPT_HTML.md`). Conventions in `volcfg.json` as Vol 18, plus `printed_english_label` "English translation".

## Status
Nov 18 2026. **Done through printed p. 532** (30 batches; about 63% of the volume). Maṇḍala 5 Sūktas 63–87 and its Pariśiṣṭa/Śrī-sūkta appendix are complete (Sūkta 86's heading was inserted by a logged repair); Maṇḍala 6 is under way: `## Maṇḍala 6` and Sūktas 1–15 present, each sūkta's Ṛk headings run 1…n without a gap (checked by script at p. 532). 250 NOTE marks, 84 GLOSS marks. `check_labels.py 20`: 880 English blocks, 0 under the wrong label. `rv structure` not usable on this volume. Page 339 has no text in the supplied md. Tokens per batch 107k–228k, about 160–225k lately (`parts/batch_costs.md`).
Hand repairs (all in `review/repair_log.md`, or by `batch.py fix` logs): `##` headings → bold (pp. 1–6, 266–271); stray Saṃhitā label (pp. 278–283); Sūkta 86 heading (p. 241/242); page heading between label and block (pp. 432–437); two translator remarks removed (pp. 459–477); w0521 repaired in kn.md by script instead of `batch.py fix` (logged after the fact). Recurring tool gap, not changed: the bhāṣya `>` block swallows the Pratipadārtha/Bhāvārtha lines under a garbled label (about a dozen windows; agents repair with `batch.py fix`); candidate script change in `html_to_kn.py` (lessons).

## Open items
1. Preface (if translated): `work/preface/en.md`, installation is a logged repair after the user's yes.
2. Tool TODO: `merge_md.py` should accept a seam where each input's last/first page is merged or split differently (this volume).
