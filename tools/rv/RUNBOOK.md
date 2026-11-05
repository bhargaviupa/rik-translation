# Vol 15+ runbook for the dispatcher (the main Claude Code session)

One window = 3 consecutive PDF pages. The dispatcher only dispatches; a **fresh Sonnet translator agent per window** does the reading (an agent cannot drop old images from its context; the output files carry the continuity).

## Set-up (once per volume)
1. `python3 tools/rv/batch.py new N --mandala M --start-pdf K` -> `volN/volcfg.json`, folders, empty `Rigveda_Samhita_VolN_English_Translation.md` and `..._Kannada_Text.md` (progress note: Done through PDF K-1).
2. Put the scan parts in `volN/scans/` (named `N <name> 1.pdf`, `… 2.pdf`, …) and the user's numeral file(s) in `volN/numerals/` (columns: Page | Line | Kannada digits | English digits | context; a Kannada-numerals column is picked up by header name).
3. Fix the page map in `volcfg.json` **before any translation**: sample ~8 header strips (`python3 tools/rv/page.py N PDF /tmp/h --strips 6`, look at the page-number corner) and set `printed` = [[from_pdf, k], …] (a pair at every change), `skip_pdf` (PDFs that duplicate the previous page), `numerals.file_page` ([[from_pdf, delta]], file page = PDF - delta; confirm on a page with known numerals). Re-check at every part boundary.
4. Accented reference: `refs/mandala/rv_mandalaM.html` must exist for the volume's Maṇḍala (the user adds Maṇḍala 3+).
5. Branch: create `claude/volN` from main; `volcfg.json` "branch" guards commits.

## Per window
1. `python3 tools/rv/batch.py prep N` -> prints the window directory and page list (warns if no numeral rows).
2. Start a translator agent (`model: sonnet`) with: the content of `WIN/PROMPT.txt` and "follow tools/rv/TRANSLATOR_RULES.md; finish with `commit`; never wait for an answer: if blocked, write the reason to WIN/BLOCKED.txt and stop". One window per agent; never two agents writing the same volume files; never switch branches while an agent runs.
3. When the agent returns: confirm `git log -1` shows the window's commit and `tail -3` of the English file shows the new progress note. If BLOCKED.txt exists, handle it and re-run the window (delete the partly built `en_final.md`/`kn_final.md` only).
4. Record the agent's tokens/minutes in `volN/parts/batch_costs.md` (one line) so cost per window can be compared.
5. Every ~10 windows: spot-check the last window by eye on the strips (IAST layer present, one progress note, no repeated text, `[?]` density, numerals vs file), and update the offset map if a header disagrees with `printed`.

## Gates (batch.py check; commit refuses to append if any fails)
page markers in both files; `[?]` within the allowance; numerals vs the user's file (NEAR / missing rows); English references have Kannada twins; no unplaced Sanskrit block; no Devanagari in the Kannada file; Ṛk headings in order; no hand-typed IAST.

## Files
`tools/rv/rvlib.py` (config, page map, rendering, zoom) · `page.py` · `numerals.py` · `convert.py` (Kannada -> Devanagari expansion) · `labels.py` · `batch.py` (new, prep, build, check, zoomlist, fix, commit). Shared with older volumes: `publish/tools/translit/add_iast.py`, `kannada_to_deva.py`, `publish/tools/accents/accent_volume.py`.

## Not built yet / to decide
- The `[?]` re-check pass over Vols 1–14's existing files (separate tool).
- Real-scan test of the whole loop with an agent (only the scripts were tested, on a synthetic window).
- The numeral file's new Kannada-numerals column: only header-name matching is implemented; send a sample when ready.
