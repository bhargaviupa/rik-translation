# Vol 12 — continue prompt for a NEW dispatcher session (Sonnet)

Fresh Claude Code session, **Sonnet**; paste everything below the line.

---

Continue the translation of Volume 12 (repo bhargaviupa/rik-translation) as the dispatcher. Sonnet only: every translator you start must have `model: sonnet`; never Opus. I am away: never wait for an answer; if blocked, record it in vol12/parts/session_state.md, push, stop. `git fetch origin claude/vol12 && git checkout -B claude/vol12 origin/claude/vol12` (LFS trouble: `GIT_LFS_SKIP_SMUDGE=1 …`, then `git lfs pull -I <scan file>`); `pip install indic_transliteration openpyxl xlrd` if missing. Never force-push or reset; no PRs; do not merge into main. Read ONLY CLAUDE.md, vol12/vol12_runbook.md, vol12/vol12_state.md, vol12/parts/session_state.md and the last progress note of `Rigveda_Samhita_Vol12_English_Translation.md`. Then run the batch loop of vol12/START_PROMPT.md (3-page batches, one Sonnet translator at a time, record the position and the batch cost, commit and push after each batch) from the recorded position. One line per batch; when your context fills, push, update the state and end with "NEXT SESSION: paste vol12/CONTINUE_PROMPT.md".
