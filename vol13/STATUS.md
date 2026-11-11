# Vol 13 — status

*Update this file at the end of every working session. It is the only place for volume-specific state; the general rules live in `CLAUDE.md`.*

## Decision (user, Nov 11 2026)
**Vol 13 is re-translated from the user's machine-read text**, by the Batch API route with the Vol 17 conventions. Reason: the old translation, read from page scans, has 1,482 `[?]` marks on 517 of its 653 pages (about 390 after a number or reference, 425 after Sanskrit, 650 after English words), its Sanskrit was typed from the scans, and there is no Kannada file.

## Scope
Expected from the old edition: Maṇḍala 1 Sūktas 166–183 (Fourth Adhyāya of the Second Aṣṭaka), printed pp. 1–657. To be confirmed from the supplied text.

## Source and inputs
**Not yet supplied**: the user's files go to `vol13/html/`. No scans (removed Nov 7 2026).

## Outputs
New, empty: `vol13/Rigveda_Samhita_Vol13_English_Translation.md` and `…_Kannada_Text.md` (progress note "Done through printed p. 0"). `volcfg.json`: window 6, `note_style` NOTE, sub-heading layout, bhāṣya block Devanagari only, grammar in Sanskrit, Wilson label (to confirm), `source` page range to be set from the text.
**Old translation, kept untouched: `vol13/legacy/`** (`Rigveda_Samhita_Vol13_English_Translation_scan.md`, `.docx`, `.pdf`). `publish/out/vol13_full.pdf` and the docx/pdf pair there are builds of the old text. `publish/build_vol45.py 13` no longer finds its input at the old path.

## Status
Scaffold only. Nothing translated, nothing sent to the API. Next: `vol13/CONTINUE_PROMPT_HTML.md` in a new session, after the user uploads the text.

## Open items
1. User: upload the Vol 13 text; say how much of the API budget is left (Vol 17 cost $20.14; Vol 18 is running on the same budget; Vol 13 is estimated at $7–8 at the send-once rate).
2. `review/user_readings_part1.tsv` (38 readings the user gave for the old file) and the numbers of the old translation are compared with the new text at the end (prompt, "After the last page").
3. Old review material in `vol13/review/` and the scripts in `vol13/tools/` belong to the scan workflow; kept, not used.

## Pointers
`vol13/CONTINUE_PROMPT_HTML.md`, `vol17/STATUS.md`, `vol18/STATUS.md`, `tools/rv/api_batch.py`, `docs/LESSONS.md` 41–54. Old workflow: `vol13/vol13_state.md`, `vol13/vol13_runbook.md`.
