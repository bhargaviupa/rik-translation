# Volume 14

First translation of this volume (not a correction pass); English file only (a Kannada text file only if asked). Maṇḍala / Aṣṭaka / Sūkta range: from the scan's title page (record in `vol14_state.md`).

| Path | What it is |
|---|---|
| `vol14_state.md` | Facts and status. Read first. |
| `vol14_runbook.md` | The method: page strips at ~360 dpi, one translator agent fed page ranges. |
| `START_PROMPT.md`, `CONTINUE_PROMPT.md` | Prompts for an independent session. |
| `scans/` | The 9 scan parts `14 Rigveda Samhitha Volume 14 N.pdf` (979 pages, ~660 ppi). `Rig_Vol14(1/2).pdf` are an old scan: ignore. |
| `parts/` | `session_state.md`: where the work stands. |
| `review/` | `doubts_v14.json` and the review pages. |
| `tools/` | `page.py` (read a page), `numsheets.py` (header strips, for the offset), `append_en.py`, `doubt.py`, `doubts_v14.py`, `cfg.py`. |

Output: `vol14/Rigveda_Samhita_Vol14_English_Translation.md`.

## Remaining pages from the supplied machine-read text (user decision, Nov 5 2026)
From printed p. 767 the translation continues with the Vol 15 workflow (`tools/rv/`, rules in `CLAUDE.md` section "Vol 15 onwards"): the Kannada text is made by script from the user's HTML/markdown, a Sonnet agent writes only the English chunk, the build adds Devanagari, IAST and accents, and the Kannada file and the English file are appended together.
- Config: `vol14/volcfg.json` (`source` = the supplied file(s) in `vol14/html/` with `@FIRST-LAST` printed pages; the English file stays at the repository root). The Kannada file `vol14/Rigveda_Samhita_Vol14_Kannada_Text.md` starts at p. 767; the earlier pages get their Kannada text in a back-fill when the supplied text for them is available.
- Dispatcher prompt: `vol14/CONTINUE_PROMPT_HTML.md`. The older image-based tools (`vol14/tools/api_batch.py`, `page.py`) are no longer used for new pages; **only one process may write the English file at a time** (stop the Mac API batches before starting).
- Vol 14 ends in Maṇḍala 2 at Sūkta 23; Vol 15 starts at Sūkta 24.
