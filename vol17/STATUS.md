# Vol 17 — status

*Update this file at the end of every working session. It is the only place for volume-specific state; the general rules live in `CLAUDE.md`.*

## Scope
Not confirmed yet: to be read from the supplied text (title page, contents, first running heads). Vol 16 ended with Maṇḍala 3 Sūkta 39 (Third Aṣṭaka, Adhyāya 2), so Vol 17 is expected to continue Maṇḍala 3 from Sūkta 40; `volcfg.json` has `mandala` 3 and `mandalas` [3, 4] (the accent reference files used) as a starting assumption only.

## Source and inputs
**Waiting for the user's machine-read text.** Put the file(s) in `vol17/html/`. Several markdown files → merge with `python3 tools/rv/merge_md.py vol17/html/rig_17.md IN1.md IN2.md --write`; pictures of verse blocks → `vol17/html/figures/` with `[figure: vol17/html/figures/NAME.jpg]` lines in the text (as in Vols 12, 14, 16). Then: `python3 tools/rv/html_pages.py vol17/html/rig_17.md` (page split), and set `source` in `vol17/volcfg.json` to the real printed-page range (now a placeholder `rig_17.md@2-999`).

## Outputs
`vol17/Rigveda_Samhita_Vol17_English_Translation.md` and `…_Kannada_Text.md` (empty; progress note "Done through printed p. 1"). Cost log `vol17/parts/batch_costs.md`.

## How it was made
Planned as the **pilot of the Batch API flow** (user decision, Nov 11 2026; API key `RIK_API_KEY`, budget $66): `python3 tools/rv/api_batch.py plan 17 --windows 5` (free: prepares windows, counts tokens, prints the estimate) → `submit 17` (spends money) → `status 17` → `collect 17` (writes each window's `en.md`, logs real cost, runs the gates and commits in page order). Model `claude-sonnet-5-5`, 6-page windows. Nothing has been sent yet.

## Status
Set up only (Nov 11 2026). Nothing translated.

## Open items
1. User: supply the machine-read text (and pictures, if the text has them); later the front-matter scan PDF for the print build.
2. Dispatcher: confirm scope and Maṇḍala from the text; run the pilot (5 windows), report measured cost per page and gate results before sending more; QA sample of the pilot pages against the Kannada.

## Publication (print PDF)
Not built.

## Pointers
`CLAUDE.md`, `tools/rv/BRIEF.md`, `tools/rv/api_batch.py` (docstring), `docs/LESSONS.md` 31–40.
