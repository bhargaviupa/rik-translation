# Vol 10 — start prompt for a NEW session (Phase 1: numerals from the user's files)

Open a fresh Claude Code session on `bhargaviupa/rik-translation` and **choose SONNET (not Opus)**; paste everything below the line. The xls/xlsx numeral files must be in `vol10/numerals/` (committed to main or to the branch) before you start.

---

You are the coordinator for the correction of Volume 10 of the Rigveda Samhita English translation (repo bhargaviupa/rik-translation; Maṇḍala 1, Sūktas 122–136, already fully translated, ~2,870 `[?]`). **Use Sonnet only: any worker you start (Agent tool, general-purpose) must have `model: sonnet`; never Opus.** Work on branch `claude/pass2-vol10` from `origin/main` (`git fetch origin main && git checkout -B claude/pass2-vol10 origin/main`; LFS trouble: `GIT_LFS_SKIP_SMUDGE=1 git checkout …`). Never force-push or reset; no PRs; do not merge into main. I am away: do not wait for answers, except at the one explicit stop below.

Read ONLY CLAUDE.md, vol10/README.md, vol10/vol10_state.md, vol10/vol10_runbook.md and docs/COORDINATION_NOTES_Oct2026.md. Then do **Phase 1 of the runbook only**: use the correct Kannada numerals in my xls/xlsx files in `vol10/numerals/` to correct as many `[?]` as possible in `Rigveda_Samhita_Vol10_English_Translation.md`. **Do not view any page image and do not read the scan in Phase 1.** First describe the files' format in `vol10/numerals/README.md`; write and test `vol10/tools/apply_numerals.py` on one sūkta and show me nothing — just verify with the asserts (headings count, one progress note, only numerals changed); apply unit by unit (a sūkta or ~30 pages per Sonnet worker if the job is large; otherwise do it yourself), log every change in `vol10/review/numerals_applied_v10.tsv` and every unmatched/conflicting row in `vol10/review/numerals_unmatched_v10.tsv`; commit and push after each unit; record progress in `vol10/parts/session_state.md`.

When the files are exhausted, give me ONE short report — per sūkta: `[?]` before/after, rows applied, unmatched, conflicting; total `[?]` left — and **STOP. Ask me explicitly whether to start Phase 2 (the page-reading pass). Do not start Phase 2 until I answer yes.**
