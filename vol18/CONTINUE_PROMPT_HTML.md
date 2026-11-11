# Prompt for the Vol 18 session (paste into a new Claude Code session on this repo; Sonnet is enough)

You run **Volume 18** of the Rigveda translation (repo `bhargaviupa/rik-translation`) by the **Batch API route**. You do not translate yourself and you start no translator agents: windows go to the API as batches, scripts check and commit them. Read `CLAUDE.md`, then `vol18/STATUS.md`, then the last four entries of `docs/LESSONS.md`. Do not read other volumes.

## Start (once)
1. Get the current tools and the prepared Vol 18 files: `git fetch origin main && git merge origin/main` on the branch this session was given. Add that branch's name to `"branches"` in `vol18/volcfg.json` (and set `"branch"` to it), commit, push. Never force-push; no pull request; merge into `main` only when the user says so.
2. `pip install indic-transliteration rapidfuzz openpyxl anthropic`
3. `python3 tools/rv/batch.py audit 18` must print `AUDIT PASS` (nothing translated yet: "done through printed p. 0"). The API key is the environment variable `RIK_API_KEY`; never print it.
4. Money: every `submit` and every `api_front.py` call spends from the user's API budget. **Show the user the estimate that `plan` prints and wait for a yes before each `submit`.** Ask the user how much of the budget is left for this volume before the first one.

## Order of work
1. **The preface first** (it stands before printed p. 1, so no window covers it): `python3 tools/rv/api_front.py 18 113 677 preface` (one request, about $0.25; line numbers from `vol18/html/_layout.json`). If it prints PROBLEMS, repair `vol18/work/preface/en.md` by hand as the message says and rebuild; then `python3 tools/rv/api_front.py 18 113 677 preface --install`, `audit 18`, commit, push.
2. **The body in stages of about 40 windows** (about 240 pages, about $3 each at Vol 17's rate; 851 pages in all):
   - `python3 tools/rv/api_batch.py plan 18 --windows 40` (free: prepares the windows, counts tokens, prints the estimate) → tell the user → on yes `python3 tools/rv/api_batch.py submit 18`.
   - Wait in the background (one job, nothing else on the repo meanwhile): poll `python3 tools/rv/api_batch.py status 18` every 30 s until it says `ended`, then `python3 tools/rv/api_batch.py collect 18`. `collect` applies each answer, lets the scripts settle what they can (quotations, quotation markers, references, remarks, unplaced blocks, duplicate headings: all logged, `**NOTE**` where a decision is needed), runs the gates and commits window after window in page order. **No retries are sent** (default).
   - If `collect` stops at a window (`STOP at …`): read `WIN/gate_failure.txt`, repair `WIN/en.md` or `WIN/kn.md` by hand (`batch.py fix`; letters of the supplied text unchanged; never change what the print says to pass a gate), check with `python3 tools/rv/batch.py done 18 WIN --dry-run`, then run `collect 18` again: finished windows are skipped. Only if a whole page was left untranslated, re-send that stage's failures on purpose with `collect 18 --retries 1` and say so.
   - While `collect` runs do not commit, push or switch branches yourself: it commits and pushes every window. Afterwards: `audit 18`, update `vol18/STATUS.md` (page reached, cost of the stage from `vol18/parts/batch_costs.md`, windows that needed a hand repair, number of `**NOTE**` marks), commit, push, and report to the user in a few lines before planning the next stage.
3. **After each stage look at the text itself**, not only at the counts: print one complete Ṛk of the new pages and the first lines of `vol18/review/notes.tsv` additions; check that `## Maṇḍala 5` stands before `## Sūkta 1 (Maṇḍala 5)` when that point is reached (insert it by a logged repair if the window did not write it) and that no sūkta heading is missing in sequence.
4. **End of the volume** (p. 851: colophon of the eighth adhyāya and the closing lines, nothing added): update `STATUS.md` with the totals and stop. The finishing checklist (`docs/HANDBOOK.md` §11: accent pass, Kannada headings, QA sample, PDFs) is a separate job: do not start it without the user.

## Stop and tell the user when
- `audit 18` fails and you cannot see why, or `collect` stops twice at the same window;
- a stage costs more than twice its estimate;
- the scope in `vol18/STATUS.md` does not fit what the text shows (a sūkta number out of sequence, a missing page range);
- the usage limit is near: commit and push first; the next session resumes with this same prompt (`plan` continues after the last committed page).

## What the user decided for this edition (already in `volcfg.json` and `tools/rv/BRIEF.md`; do not change without asking)
No translator remarks in the English text, one mark `**NOTE**` with the question in `review/notes.tsv`; no Kannada script in the English text; every part of a Ṛk under its own sub-heading; the bhāṣya block in Devanagari only, followed by a Gist that covers most of it; transliteration everywhere else; Pratipadārtha one word per line; the edition's printed English headed "English translation (H. H. Wilson)" (the user is still checking this attribution); a grammar section, where the volume has one, rendered in Sanskrit.
