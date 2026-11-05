# Vol 15+ runbook for the dispatcher (the main Claude Code session)

One window = 3 consecutive PDF pages. The dispatcher only dispatches; a **fresh Sonnet translator agent per window** does the reading (an agent cannot drop old images from its context; the output files carry the continuity).

## Set-up (once per volume)
1. `python3 tools/rv/batch.py new N --mandala M --start-page 1 --source "volN/html/FILE1.html@1-100" --source "volN/html/FILE2.md@101-200"` -> `volN/volcfg.json`, folders, empty `Rigveda_Samhita_VolN_English_Translation.md` and `..._Kannada_Text.md` (progress note: Done through printed p. START-1). Each `--source` is a file of the supplied machine-read text with the printed pages (`@FIRST-LAST`) taken from it; add one per file as the user supplies them. Strip embedded base64 images from a markdown file before committing it.
2. Numeral file: optional (the supplied text's numerals were found correct). If the user supplies one, put it in `volN/numerals/`; it is then used as a cross-check. Set `numerals.file_page` (file page = PDF - delta) and `printed` (printed = PDF - k) in `volcfg.json` only to the extent the numeral file needs PDF numbers (`prep` warns when no rows are found).
3. Accented reference: `refs/mandala/rv_mandalaM.html` must exist for the volume's Maṇḍala (the user adds Maṇḍala 3+).
4. Branch: create `claude/volN` from main; `volcfg.json` "branch" guards commits.
5. Check the supplied text once: `python3 tools/rv/html_pages.py FILE` (page numbers present? a page with no running head merges into the previous one: the splitter needs a running head with the page number on each page; markdown files lacking one need that head restored).

## Per window
1. `python3 tools/rv/batch.py prep N` -> window directory with `kn.md` (script-made from the supplied text), numerals, PROMPT.txt. The next 3 printed pages after the progress note are used; if the supplied text ends, prep stops and asks for the next file.
2. Start a translator agent (`model: sonnet`) with the content of `WIN/PROMPT.txt` and "follow tools/rv/TRANSLATOR_RULES.md; finish with `commit`; never wait for an answer: if blocked, write the reason to WIN/BLOCKED.txt and stop". One window per agent; never two agents writing the same volume files; never switch branches while an agent runs.
3. When the agent returns: confirm `git log -1` shows the window's commit and `tail -3` of the English file shows the new progress note. If BLOCKED.txt exists, handle it and re-run the window.
4. Record the agent's tokens/minutes in `volN/parts/batch_costs.md`.
5. Every ~10 windows: spot-check one window against the scan if the user has supplied it (IAST layer present, one progress note, no repeated text, `[?]` density, numerals vs file).

## Gates (batch.py check; commit refuses to append if any fails)
page markers in both files (`<!-- printed N -->` in kn.md, `### Printed p. N` in en.md); `[?]` within the allowance; numerals vs the user's file (NEAR / missing rows); English references have Kannada twins; no unplaced Sanskrit block; no Devanagari in the Kannada file; Ṛk headings in order; no hand-typed IAST.

## Files
`tools/rv/rvlib.py` (config, page map, source text) · `html_pages.py` (split the supplied text into printed pages) · `html_to_kn.py` (Kannada text by script) · `page.py` (scan strips/zoom, optional) · `numerals.py` · `convert.py` (Kannada -> Devanagari expansion) · `labels.py` · `batch.py` (new, prep, build, check, zoomlist, fix, commit). Shared with older volumes: `publish/tools/translit/add_iast.py`, `kannada_to_deva.py`, `publish/tools/accents/accent_volume.py`.

## Not built yet / to decide
- The `[?]` re-check pass over Vols 1–14's existing files (separate tool).
- Real-scan test of the whole loop with an agent (only the scripts were tested, on a synthetic window).
- The numeral file's new Kannada-numerals column: only header-name matching is implemented; send a sample when ready.
