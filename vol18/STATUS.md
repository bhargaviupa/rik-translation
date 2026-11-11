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
Text prepared and windows planned (Nov 11 2026); **nothing sent to the API, nothing translated: waiting for the user's go-ahead.** Free plan of the first 5 windows (pp. 1–30): 115,533 input tokens, about 3,850 per page.

## Open items
1. User: go-ahead for the first stage; later the front-matter scan PDF for the print build; confirm the heading "English translation (H. H. Wilson)".
2. Dispatcher: translate the preface first (`python3 tools/rv/api_front.py 18 113 677 preface`, then `--install` when no window job runs), then the windows in stages (`api_batch.py plan|submit|collect 18`), reporting cost after each stage.

## Publication (print PDF)
Not built.

## Pointers
`CLAUDE.md`, `vol17/STATUS.md` (what happened on the first batch-API volume), `tools/rv/BRIEF.md`, `tools/rv/api_batch.py`, `docs/LESSONS.md` 41–50.
