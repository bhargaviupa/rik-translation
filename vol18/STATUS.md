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
Nov 11 2026. **Preface translated and installed** (api_front.py, $0.224; 12 NOTE rows; one Kannada word inside Wilson's English quotation transliterated by hand, logged). **Stage 1 done: printed pp. 1–246 (windows w0001–w0241, Maṇḍala 4 Sūktas 19–30 so far), batch cost $2.50 (first pass only, no retries; `parts/batch_costs.md`)**; `audit 18` passes at "done through printed p. 246". 84 rows in `review/notes.tsv` (12 of them from the preface). Ṛk counts per sūkta 19–30 run 1…n without gap (11, 11, 11, 11, 11, 11, 8, 7, 5, 5, 5, 21 so far; Sūkta 30 continues in the next stage). `## Maṇḍala 5` not reached yet.
Windows that needed a hand repair (all in `review/repair_log.md`): w0076 and w0101 (a Ṛk continued across the window boundary: heading marked "(continued)"), w0083 (a gate rejected "has supplied": tool fixed), w0156 (3 picture lines that only repeat verses removed; Ṛk 2 had no heading/labels), w0235 (Ṛk 17 had plain-text labels, no heading).

## Open items
1. Next stage: `python3 tools/rv/api_batch.py plan 18 --windows 40` (continues after p. 246), user's yes, `submit`, `collect`.
2. User: front-matter scan PDF for the print build; confirm the heading "English translation (H. H. Wilson)".

## Publication (print PDF)
Not built.

## Pointers
`CLAUDE.md`, `vol17/STATUS.md` (what happened on the first batch-API volume), `tools/rv/BRIEF.md`, `tools/rv/api_batch.py`, `docs/LESSONS.md` 41–50.
