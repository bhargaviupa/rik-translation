# Kickoff prompt for the Vol 14 experiment session (paste into a new Claude Code session on this repo)

You are the dispatcher of an EXPERIMENT in the repository `bhargaviupa/rik-translation`: translate Vol 14 printed pp. 501-766 (Maṇḍala 2, Sūktas 5-15) a second time, from the user's machine-read text instead of the scans, and then compare the new English text with the scan-based text already in the repository to see how many differences there are. You do not translate yourself: you prepare windows of 3 printed pages, hand each to a fresh **Sonnet** agent (`Agent`, `model: sonnet`), check the result and go on. Do not wait for the user between windows; if blocked, write the reason in the window's BLOCKED.txt and stop.

## Setup (once)
1. `git fetch origin && git checkout claude/vol14-exp` (never merge into `main`, never force-push, no pull requests; all commits go on `claude/vol14-exp`). If checkout trips over an LFS pointer: `GIT_LFS_SKIP_SMUDGE=1 git checkout -f claude/vol14-exp`.
2. `pip install indic-transliteration rapidfuzz openpyxl`
3. Read: `CLAUDE.md` (section "Vol 15 onwards"), `tools/rv/RUNBOOK.md`, `tools/rv/TRANSLATOR_RULES.md`, `vol14/EXPERIMENT_BRIEF.md`. INDEPENDENCE: you and your agents must not read the scan-based Vol 14 translation (`Rigveda_Samhita_Vol14_English_Translation.md`, `vol14/Rigveda_Samhita_Vol14_Kannada_Text.md`, `vol14/work/`, `vol14/review/`) until the comparison step.
4. Make the experiment slot **Vol 99**: `python3 tools/rv/batch.py new 99 --mandala 2 --branch claude/vol14-exp --start-page 501 --source "vol14/html/rig_14_2_figs.html@501-766"`; then edit `vol99/volcfg.json` (remove the `numerals` and `scan` entries; keep `window` = 3; the source is the supplied text with the pictures' markers) and check the page list once: `python3 tools/rv/html_pages.py vol14/html/rig_14_2_figs.html` (printed pp. 501-954; an unnumbered page merges into the page before; p. 537 etc. are such pages). The new English file starts with "Done through printed p. 500". Commit and push.
5. The accent reference for Maṇḍala 2 is `refs/mandala/rv_mandala2.html` (already there).

## Loop (per window, ~89 windows)
1. `python3 tools/rv/batch.py prep 99` → prints the window directory `vol99/work/wPPPP/`. Stop when the next page is beyond 766 (do not translate p. 767 or later: that part is done and merged).
2. One fresh Sonnet agent with the prompt: "Translate window vol99/work/wPPPP (printed pages …) in /home/user/rik-translation, branch claude/vol14-exp (checked out). Read vol14/EXPERIMENT_BRIEF.md first and follow it exactly. Commands: python3 tools/rv/batch.py build 99 WIN ; check 99 WIN ; commit 99 WIN --note "…". Never wait for an answer; if blocked write WIN/BLOCKED.txt." One agent at a time; never switch branches while an agent runs.
3. When it returns: `git log -1` shows the window commit; the new English file ends with exactly ONE "**Progress note:** Done through printed p. N" (python: `count('**Progress note:**')==1`). If the agent altered characters to pass a check (non-breaking hyphens, spelled-out digits for Ṛg-veda references) or hand-edited accents, fix that or tell it to. Append a line to `vol99/parts/batch_costs.md` (pages, tokens, minutes), commit, push.
4. Every 10 windows print a 5-line status (page reached, windows done, `[?]` left, accent DIFFs) and continue.

## Comparison (after the last window, or every ~30 pages as a preview)
`python3 tools/rv/compare_translations.py Rigveda_Samhita_Vol14_English_Translation.md vol99/Rigveda_Samhita_Vol99_English_Translation.md 501 766 --out vol99/review/compare_vs_scan.md --tsv vol99/review/compare_pages.tsv` (differing Devanagari block words, English prose similarity per page, `[?]` counts, differing reference numerals). Then look at the 15 worst pages in each list yourself and write `vol99/review/compare_notes.md`: for ~20 sample differences say who is right (use the figures in `vol14/html/figures/` and the supplied text) and what kinds of differences occur (OCR slips in the supplied text, misreads of the scan, different wording of the same Kannada). Report the totals and the notes to the user. Do not merge anything into `main`.

## Things to expect
- Garbled or duplicated Saṃhitā/Pada lines in the supplied text; pictures replace some blocks (the agents read them).
- Pages that begin a new heading print no page number; they are not gaps.
- Stop and report when the usage limit nears; the next session resumes from the progress note.
