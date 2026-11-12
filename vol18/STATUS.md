# Vol 18 — status

*Update this file at the end of every working session. It is the only place for volume-specific state; the general rules live in `CLAUDE.md`.*

## Scope
Maṇḍala 4 Sūktas 19–58 (to the end of Maṇḍala 4) and Maṇḍala 5 Sūktas 1–8, Third Aṣṭaka, Adhyāyas 6–8; printed pp. 1–851 (colophon of the eighth adhyāya and closing lines at the end). Read from the supplied text (title page, 48 sūkta heading lines, closing lines); not checked against a scan.

## Source and inputs
`vol18/html/rig_18.md`: the user's two files (`rig_18_1.md`, `rig_18_2.md`; supplied Nov 11 2026) merged losslessly with `tools/rv/merge_md.py` (815 page splits identical before and after). Changes made to the supplied text, all mechanical: the 76 embedded pictures were extracted to `vol18/html/figures/` and replaced by `[figure: …]` lines; the converter's two `Pages: N/N` footer lines and two `Indus by Sarvam` lines were removed; **one line `<!-- page 1 -->` was inserted before the opening "|| ಶ್ರೀಃ ||" of the body** (line 1122; printed p. 1 prints no running head). The page splitter finds 816 of the 851 printed pages (35 numbers have no head of their own; the translator marks them).
Front matter (lines 1–1120, no window covers it): title pages and board of scholars; **the volume's preface (ಪೀಠಿಕೆ), lines 113–677, roman pp. i–xiv, dated 12-11-52**; the contents (lines 679–1081, partly as HTML tables); the list of abbreviations. `vol18/html/_layout.json` records these line numbers. `volcfg.json`: `source` = `rig_18.md@1-851`, window 6, `mandalas` [4, 5]. No scans, no numeral file, no front-matter scan PDF yet.

## Outputs
`vol18/Rigveda_Samhita_Vol18_English_Translation.md` and `…_Kannada_Text.md` (empty; progress note "Done through printed p. 0"). Cost log `vol18/parts/batch_costs.md`.

## How it will be made
Batch API route as for Vol 17 (`RIK_API_KEY`): `python3 tools/rv/api_batch.py plan 18 --windows K` (free: prepares windows, counts tokens, prints the estimate) → `submit 18` (spends money: only after the user has seen the estimate) → `status 18` → `collect 18`. Conventions carried over from Vol 17 in `volcfg.json`: Sonnet, 6-page windows, `**NOTE**` marks instead of remarks, no Kannada script in the English text, sub-heading layout, bhāṣya block in Devanagari only with a Gist that covers most of it, Pratipadārtha one word per line, printed English headed "English translation (H. H. Wilson)" (still to be confirmed by the user), grammar sections (if the volume has any) rendered in Sanskrit.

## Status
Nov 11 2026. **Translation complete: printed pp. 1–851** (title lines, preface, Maṇḍala 4 Sūktas 19–58, Maṇḍala 5 Sūktas 1–8, colophon of the eighth adhyāya and closing lines at p. 851, nothing added). `audit 18` passes at "done through printed p. 851". Total API cost **$8.89** (preface $0.224; windows $8.66: stage 1 $2.50, stage 2 $2.33, stage 3 $2.85, stage 4 $0.98), first pass only, no retries (`parts/batch_costs.md`). Maṇḍala 4 Sūktas 19–58 and Maṇḍala 5 Sūktas 1–8 are all present; each sūkta's Ṛk headings run 1…n without gap. 329 rows (incl. header) in `review/notes.tsv`: 328 NOTE marks, 12 of them from the preface.
**Page numbers with no `### Printed p. N` heading** (the supplied text has no marker for them): after a local repair on Nov 11 2026 (`review/repair_log.md`: 138, 208, 293, 454, 514, 525, 644, 674, 738, 740 restored; markers 513 and 739 relabelled) **510, 534, 648, 668, 669** remain (5 of 851; no remnant of the page break in the text). **Decision (user, Nov 11 2026): page markers are kept; the five missing ones are not to be chased, the content being all there.**
Hand repairs (all in `review/repair_log.md`): stage 1: w0076, w0101, w0156, w0235 (gate bug at w0083); stage 2: figure lines in w0334, w0427, w0445; stage 3: figure line in w0579, missing page heading (w0560), spurious Saṃhitā label in the Kannada file (w0623), `## Maṇḍala 5` heading (w0667), gate bug at w0541; stage 4: Ṛk 4 headings (w0821). 12 figure lines removed in all (each compared by eye with kn.md).

## Finishing job (Nov 12 2026)
Done: `refs_fix`, `repair_inline` (0 changes); Kannada headings (48 sūktas, 455 Ṛks); accent report (`review/accent_report.tsv`, `accent_report_pages.tsv`: 183 lines without a match in the reference, left unaccented, listed for the user); review PDFs built with `publish/volbook.py 18` (`publish/out/vol18_full_Eng.pdf`, `vol18_full_Kan.pdf`, with `.html`; front matter = title page + credits only, no cover/portraits/board/contents yet); QA sample of 24 pages by Opus agents: **`review/qa_sample.md` (4 ERROR, 30 MINOR)**.
**Known defect, repaired by hand Nov 12 2026**: in 6 windows (pp. 162–167, 223–228, 316–321, 445–450, 729–734, and a garbled Pada label on p. 373) the Saṃhitā/Pada/bhāṣya blocks stood under the label of another section; blocks put back under their own labels (details in `review/repair_log.md`); `python3 tools/rv/check_labels.py 18` reports 0; a gate in `batch.py check` now stops such a window in future. Five `**NOTE**` rows of "block placed here by script" were removed and one NOTE (Sūkta 44 introduction) added; the review PDFs built before this repair are being rebuilt.
Not done: doubled QA sample (due because ERRORs were found); of the 4 reported ERRORs the label one (g318) is repaired, g177, s736, s783 and the minor items are not; front matter beyond title page/credits.

## Open items
1. The finishing job (docs/HANDBOOK.md §11: accent pass, Kannada headings, QA sample, PDFs): separate; not started, only with the user. Front matter for the print build comes from the supplied md (title pages, board, contents, abbreviations as text; cover and title pictures are in `html/figures/`; preface already translated): no scan PDF is needed, but `volbook.py` still expects a scan-PDF `pubcfg.json`, to be adapted then.
2. Heading of the printed English: **kept as the old `Printed English`** (user, Nov 11 2026); the "(H. H. Wilson)" label was removed from `volcfg.json` and from the Vol 18 text (461 headings). Vol 17 still has the label (ask before changing).
3. Release details (publisher, ISBN, rights, permissions): the user will give them later; they go into `publish/release.json`, not into the volumes.
4. Tool TODOs of this volume: all closed (lesson 60); to be proved on the next volume's first stage.

## Publication (print PDF)
Not built.

## Pointers
`CLAUDE.md`, `vol17/STATUS.md` (what happened on the first batch-API volume), `tools/rv/BRIEF.md`, `tools/rv/api_batch.py`, `docs/LESSONS.md` 41–50.
