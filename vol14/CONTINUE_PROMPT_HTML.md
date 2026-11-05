# Prompt for the Vol 14 (supplied-text) dispatcher session — paste into a new Claude Code session on this repo

You are the dispatcher for the **remaining pages of Volume 14** of the Rigveda Saṃhitā translation project (repo `bhargaviupa/rik-translation`): from printed p. 767 to the end of the volume (Maṇḍala 2, up to Sūkta 23). You do not translate yourself: you prepare windows of 3 printed pages, hand each to a fresh **Sonnet** translator agent, check the result and go on. Never wait for the user between windows; if blocked, write the reason in the window's `BLOCKED.txt` and stop.

## Start (once)
1. **Only one process may write the English file.** Make sure no Mac API batch (`vol14/tools/api_batch.py`) is running or will run.
2. `git fetch origin && git checkout claude/vol14-html && git merge origin/main` (if checkout fails on an LFS pointer: `GIT_LFS_SKIP_SMUDGE=1 git checkout -f claude/vol14-html`). All work, commits and pushes go on **`claude/vol14-html`** only; never merge into `main`, never force-push, no pull requests.
3. `pip install indic-transliteration rapidfuzz openpyxl`
4. Read, in order: `CLAUDE.md` (section "Vol 15 onwards" and the Conventions), `tools/rv/RUNBOOK.md`, `tools/rv/TRANSLATOR_RULES.md`, `vol14/README.md` (last section), and the last ~120 lines of `Rigveda_Samhita_Vol14_English_Translation.md` (repository root: the format of the existing text and the single trailing progress note).
5. Facts: the base text is the user's machine-read text in `vol14/html/` (listed under `source` in `vol14/volcfg.json`, `file@FIRST-LAST` printed pages). If `vol14/html/` has no file yet, stop and ask the user to supply it. **No page images are read.** The English file stays at the repository root (`out.en` in the config); the new Kannada file `vol14/Rigveda_Samhita_Vol14_Kannada_Text.md` starts at p. 767. The accented Saṃhitā reference for all ten Maṇḍalas is in `refs/mandala/`. No numeral file (optional). Check once: `python3 tools/rv/html_pages.py <file>` (page numbers, pages without a running head).
6. Keep the **format of the existing Vol 14 text** (per-Ṛk headings `#### Ṛk N`, label lines, Devanagari + IAST + English layers); the build normalises labels. The progress note currently reads "Done through printed p. 766 (PDF 790)"; the new note will read "Done through printed p. N".

## Loop (per window)
1. `python3 tools/rv/batch.py prep 14` → prints the window directory `vol14/work/wPPPP/` (kn.md made by script, pages.json, PROMPT.txt). If prep says the supplied text has ended, stop and report.
2. Start **one** translator agent (`Agent`, `model: sonnet`, fresh each window) with the content of `WIN/PROMPT.txt` plus: "follow `tools/rv/TRANSLATOR_RULES.md` exactly; match the style of the existing Vol 14 text; finish with `python3 tools/rv/batch.py commit 14 WIN --note "…"`; never wait for an answer; if blocked write `WIN/BLOCKED.txt` and stop; do not touch git except through `commit`; do not view page images; never change a letter or number from memory". One agent at a time; never switch branches while an agent runs.
3. When the agent returns: verify `git log -1` shows `Vol 14: printed pp. …` and that the English file ends with exactly one "**Progress note:** Done through printed p. N". If `check` failed or `BLOCKED.txt` exists, read the reason once and retry the window once; if it fails again, stop and report.
4. Append one line to `vol14/parts/batch_costs.md` (pages, model, tool uses, subagent tokens, minutes), then `git add -A && git commit && git push origin claude/vol14-html`.
5. Every 10 windows print a 5-line status for the user (printed page reached, windows done, `[?]` left in `vol14/review/doubts.tsv`, unmatched lines in `accent_report.tsv`) and continue.

## Things to expect
- A page without a running head is merged into the page before it; a window can then hold more than 3 pages of text.
- Occasional single-letter OCR slips in the supplied text: never "fix" them from memory; unsettled places become `[?]` and go to `vol14/review/doubts.tsv` for the user.
- Stop and report when the usage limit nears; the next session resumes from the progress note.

## Note on the supplied text (user, Nov 5 2026)
The supplied text ends at printed p. 954, which is the end of Vol 14. Printed numbers 790, 791, 870 and 876 are absent from the text because those pages begin a new heading and the original prints no page number; their content is present (merged into the page before). Do not flag them as gaps and do not stop for them.
