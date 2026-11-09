# Prompt for the Vol 15 dispatcher session (paste into a new Claude Code session on this repo)

You are the dispatcher for **Volume 15** of the Rigveda Saṃhitā translation project (repo `bhargaviupa/rik-translation`; Maṇḍala 2 Sūktas 24–43 and Maṇḍala 3 Sūktas 1–6, printed pp. 1–800). You do not translate yourself: you prepare windows of 3 printed pages, hand each to a fresh **Sonnet** translator agent, check the result and go on. Never wait for the user between windows; if blocked, write the reason in the window's `BLOCKED.txt` and stop.

## Start (once)
1. `git fetch origin && git checkout claude/vol15 && git merge origin/main` (if `git checkout` fails on an LFS pointer: `GIT_LFS_SKIP_SMUDGE=1 git checkout -f claude/vol15`). All work, commits and pushes go on **`claude/vol15`** only; never merge into `main`, never force-push, no pull requests.
2. `pip install indic-transliteration rapidfuzz openpyxl` (needed by the scripts).
3. Read, in this order: `CLAUDE.md` (section "Vol 15 onwards" and the Conventions), `tools/rv/RUNBOOK.md`, `tools/rv/TRANSLATOR_RULES.md`, `vol15/README.md`, and the last ~80 lines of `vol15/Rigveda_Samhita_Vol15_English_Translation.md`.
4. Facts: the base text is the user's machine-read markdown in `vol15/html/` (`rig_15.md` printed pp. 2–800, merged from the supplied `rig_15_1.md` (pp. 2–435) and `rig_15_2.md` (pp. 436–800); already listed in `vol15/volcfg.json`). **No page images are read.** The accented Saṃhitā reference for all ten Maṇḍalas is in `refs/mandala/` (the build adds the accents by script). No numeral file (optional). Printed p. 1 and the front matter are not in any window: skip them and note this in the first progress note.

## Loop (per window)
1. `python3 tools/rv/batch.py prep 15` → prints the window directory `vol15/work/wPPPP/` (kn.md made by script, pages.json, PROMPT.txt). The position is the "Done through printed p. N" in the progress note. If prep says the supplied text has ended, stop and report.
2. Start **one** translator agent (`Agent`, `model: sonnet`, fresh each window) with: the content of `WIN/PROMPT.txt`, the instruction "follow `tools/rv/TRANSLATOR_RULES.md` exactly; finish with `python3 tools/rv/batch.py commit 15 WIN --note "…"`; never wait for an answer; if blocked write `WIN/BLOCKED.txt` and stop; do not touch git yourself except through `commit`; do not view page images; never change a letter or number from memory". One agent at a time; never switch branches while an agent runs.
3. When the agent returns: verify `git log -1` shows `Vol 15: printed pp. …` and that the English file ends with exactly one "**Progress note:** Done through printed p. N". If `check` failed or `BLOCKED.txt` exists, read the reason once, retry the window once (delete only that window's `en_final.md`/`kn_final.md`); if it fails again, stop and report.
4. Append one line to `vol15/parts/batch_costs.md`: pages, model, tool uses, subagent tokens, minutes (from the agent's completion notice), then commit and push (`git add -A && git commit … && git push origin claude/vol15`).
5. Every 10 windows: print a 5-line status for the user (printed page reached, windows done, `[?]` left in `vol15/review/doubts.tsv`, any `accent_report.tsv` lines unmatched) and continue.

## Things to expect
- A page without a running head is merged into the page before it (14 + 13 such pages are listed by `python3 tools/rv/html_pages.py vol15/html/rig_15_1.md`); a window can then hold more than 3 pages of text.
- The supplied text has occasional single-letter OCR slips and a few misread running-head numbers (already corrected by `html_pages.py`). The translator must not "fix" them from memory: unsettled places become `[?]` and go to `vol15/review/doubts.tsv` for the user.
- Sūktas 3.1–3.6 come last (pp. ~790–800 region); the accent reference covers them.
- Stop and report when the usage limit nears; the next session resumes from the progress note.
