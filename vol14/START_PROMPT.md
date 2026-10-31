# Vol 14 — start prompt for a NEW, independent session (nothing monitors it)

Open a fresh Claude Code session on `bhargaviupa/rik-translation` (Opus) and paste everything below the line. Later sessions: `vol14/CONTINUE_PROMPT.md`.

---

Translate Volume 14 of the Rigveda Samhita (1949 Kannada commentary: Sāyaṇa's Sanskrit bhāṣya + H. P. Venkata Rao's Kannada explanation) into English. You work alone; I am away: never wait for an answer. If blocked, write it in vol14/parts/session_state.md, push, stop.

1. `git fetch origin main && git checkout -B claude/vol14 origin/main` (LFS trouble: see runbook "Hygiene"). Never force-push or reset; no PRs; do not merge into main. Push `git push -u origin claude/vol14` after every sūkta or ~15 pages.
2. Read ONLY CLAUDE.md, vol14/vol14_runbook.md, vol14/vol14_state.md. For the format look at ONE finished sūkta of Vol 13 (`git show origin/claude/vol13:Rigveda_Samhita_Vol13_English_Translation.md | head -c 30000`) and copy it. Read nothing else.
3. Set-up as in the runbook (page offset by sampling header strips, Sūkta range from the title page; set OFFSET in vol14/tools/cfg.py; note both in vol14/vol14_state.md). Then start translating.
4. Method: the runbook's "Work": for each batch of 6 consecutive pages start a NEW translator agent (it is discarded afterwards); it reads each page with `python3 vol14/tools/page.py PDFPAGE /tmp/pg` (full-width strips at ~360 dpi, no separate zoom step), writes it, appends with `vol14/tools/append_en.py`, IAST by script, and replies with one line; give it the position, the file's last ~40 lines and a format model, as the runbook says. You dispatch, record progress in vol14/parts/session_state.md, commit and push. Keep your own replies to one or two lines.
5. When your context is filling: finish the current Ṛk, push, update the state, last line "NEXT SESSION: paste vol14/CONTINUE_PROMPT.md".
