# Vol 24 — status

*Update this file at the end of every working session. It is the only place for volume-specific state; the general rules live in `CLAUDE.md`.*

## Scope
Ṛgveda-saṃhitā Part 24: Maṇḍala 8, Sūktas 21–67 (the volume's preface) = Aṣṭaka 6, adhyāyas 2–4 (the text opens "ಆರನೆಯ ಅಷ್ಟಕದಲ್ಲಿ ಎರಡನೆಯ ಅಧ್ಯಾಯವು", closes "ಆರನೆಯ ಅಷ್ಟಕದಲ್ಲಿ ನಾಲ್ಕನೆಯ ಅಧ್ಯಾಯವು ಸಮಾಪ್ತವಾದುದು" and "|| ಶುಭಂ ಭೂಯಾತ್ ||"). Printed pp. 1–797. `volcfg.json`: `mandalas` [8], window 6. Sūktas 49–59 are the Vālakhilya sūktas (80 Ṛks; the preface says Sāyaṇa wrote no bhāṣya on them and that the bhāṣya printed is the one from the Poona Vaidika Saṃśodhana Maṇḍala edition). The volume starts at Maṇḍala 8 Sūkta 21, so Vol 21 (to 7.19) and Vol 24 are not consecutive: Vols 22–23 are the missing range. Scope read from the supplied text only.

## Source and inputs
Supplied by the user (Nov 24 2026) as two machine-read markdown files, `rig_24_1.md` (to p. 390/391) and `rig_24_2.md` (from p. 391); the files are not kept (the user has them). Changes to the supplied text, and nothing else: (1) 43 embedded pictures (22 + 21) moved to `vol24/html/figures/` by `extract_figures.py` and replaced by `[figure: …]` lines (**none of them is a title page or cover; the first is at line 2298**, so the PDF has no title-page pictures from this text); (2) the converter's footer lines `Pages: 395/395` and `Pages: 408/408` and the `Markdown source` first line of each file removed; (3) `merge_md.py` REFUSED (seam at p. 391/392: each file alone reads p. 391 differently from the merged file; the merged file is right: head "391" at the start of file 2, p. 392 has no head), so the files were joined by hand exactly as the tool does (`a.rstrip('\n') + '\n\n' + b`); (4) marker `<!-- page 1 -->` inserted before the body's opening "ॐ" (line 183).
`html_pages.py`: 758 pages, printed 1–797. Printed pages with no running head (first pages of a sūkta or section, or a head merged into the page before; not a fault, lesson 67): 55, 59, 61, 63, 64, 74, 75, 112, 128, 136, 178, 179, 180, 193, 204, 224, 225, 233, 246, 259, 260, 270, 276, 306, 338, 348, 359, 367, 392, 422, 447, 456, 489, 527, 654, 658, 698, 728, 763. Head numbers misread by OCR and corrected by the offset rule are listed by `html_pages.py` (lines 588, 1500, 2589, 2671, 2751, 3269, 7388, 7675, 9871, 14715, 19993, 20435, 20678, 21441, 22881, 31140; the head at line 14715 reads "ಸಾರಥಿಭಾಷ್ಯಸಹಿತಾ ಮಂ. ೮. ಆ. ೫. ಸಾ. ೩೯೭", i.e. Sūkta 39 or 397 misread). **Page markers (QA finding F4, fixed Nov 25 2026):** the 39 page numbers listed above are pages whose running head the splitter did not read or read wrongly. Agents had inserted markers for 26 of them in the windows; 13 had none (59, 61, 63, 64, 75, 224, 225, 233, 259, 260, 447, 489, 763) and five markers carried the wrong number (59 labelled 60, 61 → 62, 63 → 65, 75 → 76, 233 → 234). Corrected by the dispatcher in the English and Kannada files (`review/repair_log.md`): the page chunks of the supplied text (separated by `---`; the chunk number is the printed page up to the seam at p. 391, where the hand-joined files lack one separator) were used as the reference. Now both files have exactly 797 markers, pp. 1–797 in order.
Front matter (lines 1–182; see `html/_layout.json`): preface "ಪಿಳಿಕೆ" (l. 1), contents (l. 39–141), abbreviations (l. 145). No scans, no numeral file. The text ends with the closing verses and a picture on the last page.

## Outputs
`vol24/Rigveda_Samhita_Vol24_English_Translation.md`, `…_Kannada_Text.md` (empty; "Done through printed p. 0"). Cost log `vol24/parts/batch_costs.md`.

## How it was made
By Sonnet agents, one per batch of three windows, no Batch API (`docs/prompts/VOL24_AGENT_PROMPT.md`). Conventions in `volcfg.json` as Vol 21.

## Status
**Translation complete: printed pp. 1–797** (Nov 24 2026; 127 windows, 42 agent batches; the last window ends with the colophon of the sixth aṣṭaka's fourth adhyāya and "May there be auspiciousness", nothing added). `batch.py next 24` prints "no further window"; `audit 24` passes at "done through printed p. 797"; `check_labels.py 24`: 2298 English blocks = 2298 Kannada blocks, 0 under another section's label. Maṇḍala 8 Sūktas 21–67 all present in order; every sūkta's Ṛk headings run 1…n without a gap (script check). 473 `**NOTE**` marks (521 rows in `review/notes.tsv`), 40 `**GLOSS**` marks. About 7.2M agent tokens in the 42 logged batches (`parts/batch_costs.md`; batch 21 counts only the resumed part after the usage limit).
Hand repairs: by `batch.py fix` inside the windows (garbled Pada/bhāṣya/Pratipadārtha labels, stray "XXIV nn" lines, missed running heads at pp. 55, 179–181, 193, 306, 338, 359, 367, 728 and others); dispatcher repairs in `review/repair_log.md`: missing `## Sūkta 32` heading (w0220), a translator remark removed (w0344), a kn.md edit by script logged after the fact (w0533). Sūkta head lines were OCR-damaged in many places (ಸೂಕ್ತ-೨೨ for 32, ೨೫ for 35 …): the agents wrote the number from the particulars line and the announcement, with a NOTE. No Maṇḍala heading precedes Sūkta 21 (the volume starts inside Maṇḍala 8).

## Open items
Finishing checklist (HANDBOOK §11) done on Nov 24 2026 as far as it can be done without scans: 1 colophon (yes); 2 tools: `refs_fix` 0 changes, `repair_inline` 0 left, `check_inline` over all 127 windows 0 mismatches, `check_labels` 0 under another label, all 47 `## Sūkta` headings present; 3 accent report (`review/accent_report.tsv`, `accent_report_pages.tsv`; 108 NOMATCH, 8 DIFF, 1 ABORT, nothing written); 4 Kannada headings written by `kn_headings.py --write` (47 sūktas, 730 Ṛks); 5 QA sample doubled (above); 6 front matter and PDFs: **not done** (no scan PDF of the front matter was supplied, PDFs are not built in this session); the preface is translated and installed (logged); `review/contents_check.md` compares the printed contents with the body; 7 review lists: `notes.tsv` (524 rows), `inline_mismatch.tsv` (empty), `accent_report_pages.tsv`, `contents_check.md`, `qa_sample*.md`; 8 metrics above; 9 lessons added to `docs/LESSONS.md`.
1. (user) 524 NOTE questions in `review/notes.tsv` (3 of them on the preface); 52 GLOSS markers (quotations without a Kannada meaning: to be filled from our own edition).
2. (user) 9 MINOR wording points of the two QA rounds (listed in the qa files) not repaired; the contents entries that differ from the heading page in `contents_check.md`.
3. (user) The text has many machine-read damages in the Sāyaṇa-bhāṣya, Pada and Pratipadārtha; the English follows the supplied text and marks them with NOTE. The Vālakhilya sūktas (49–59) use the bhāṣya from the Poona edition, as the preface says.
4. (user) Accent gaps listed, none written (no `--api` key); unaccented lines are never accented by hand.
5. (user) Print PDF: needs the front-matter scan or the user's decision to build from the supplied text (title pictures are not in the supplied text); contents and abbreviations lines 39–181 of `html/rig_24.md` are for the front matter job.
6. Judgement call for the second reading: Sūkta 37 particulars read "Śyāvāśva" where the print has ಶ್ವಾನಾಶ್ವಃ (NOTE kept); w0533 kn.md edit by script (logged); `check_labels` counts one Kannada block more than the English after `kn_headings --write` (a heading line).
7. Script candidates seen again and again: see `docs/LESSONS.md` (Vol 24 section).

## Publication (print PDF)
Not built.

## Metrics
| windows | pages | hand-fixes by kind | gate failures (first `done` refused) | `[?]` | inline mismatches | accent lines unmatched | QA sample (pages, errors, minors) | agent tokens / cost |
|---|---|---|---|---|---|---|---|---|
| 127 (42 agent batches) | 797 (+ preface) | about 80 `batch.py fix` calls: merged Saṃhitā/Pada or bhāṣya/Pratipadārtha blocks and garbled labels (most), stray lines (`XXIV nn` and the like), missed running heads (10), plain-text introductions made blocks (8), 1 missing heading, 1 translator remark, 1 unlogged script edit; dispatcher repairs: 3 + the Ṛk 1 split | about 1 per window (inline ⟦ ⟧ not in kn.md, Latin-letter Sanskrit, Kannada in Gist) | 0 | 0 (`review/inline_mismatch.tsv` empty) | 108 NOMATCH, 8 DIFF, 1 ABORT in `review/accent_report.tsv` (no `--api`) | round 1: 24 pages, 4 ERRORs (printed English of Ṛk 29 missing p. 520; two quotation overruns pp. 230, 422; 13 missing page markers), 5 MINOR; round 2 (doubled, 24 other pages): 1 ERROR (quotation cut short p. 566), 8 MINOR; all ERRORs but the page markers repaired (`review/qa_sample.md`, `qa_sample_2.md`, `repair_log.md`) | 7.17M tokens in the 42 logged batches (about 9k a page; Vol 12 route: about 10k a page); no API money |

## Lessons from this volume

## Pointers
`docs/prompts/VOL24_AGENT_PROMPT.md`, `vol24/html/_layout.json`.
