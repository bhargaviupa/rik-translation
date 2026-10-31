# Vol 14 — continue prompt for a NEW independent session

Paste everything below the line (Opus).

---

Continue translating Vol 14 (repo bhargaviupa/rik-translation). Independent session; I am away: never wait for an answer; if blocked record it in vol14/parts/session_state.md, push, stop. `git fetch origin claude/vol14 && git checkout -B claude/vol14 origin/claude/vol14` (never reset a pushed branch or force-push; no PRs; merge to main only when I say). Read ONLY CLAUDE.md, vol14/vol14_runbook.md, vol14/vol14_state.md, vol14/parts/session_state.md, and the last ~40 lines of `Rigveda_Samhita_Vol14_English_Translation.md`. Continue from the recorded point with the runbook's "Work": for each batch of 6 consecutive pages start a NEW translator agent, discarded afterwards (it reads with `python3 vol14/tools/page.py PDFPAGE /tmp/pg`, writes, appends with vol14/tools/append_en.py, IAST by script, replies with one line); you record progress in vol14/parts/session_state.md and push every sūkta or ~15 pages. When your context fills: finish the current Ṛk, push, update the state, and end with "NEXT SESSION: paste vol14/CONTINUE_PROMPT.md". One or two lines per reply.
