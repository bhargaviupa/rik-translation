# Prompt for the Vol 13 session (paste into a new Claude Code session on this repo; Sonnet is enough)

You **re-translate Volume 13** of the Rigveda translation (repo `bhargaviupa/rik-translation`) from the user's machine-read text, by the **Batch API route**, exactly as Vols 17 and 18 were made. The user decided this on Nov 11 2026: the old Vol 13, read from page scans, has 1,482 `[?]` marks on 517 of 653 pages and no Kannada file, so it is redone, not repaired. You do not translate yourself and you start no translator agents: windows go to the API as batches, scripts check and commit them. Read `CLAUDE.md`, then `vol13/STATUS.md`, then `vol17/STATUS.md` (what the first batch-API volume showed) and `docs/LESSONS.md` 41–54.

**The old translation is kept, untouched, in `vol13/legacy/`** (`…_English_Translation_scan.md`, docx, pdf). It is not a source for the new text and nothing is copied from it. It is used once, at the end, as a second reading (see "After the last page").

## Start (once)
1. Get the current tools and the Vol 13 scaffold: `git fetch origin main && git merge origin/main` on the branch this session was given. Add that branch's name to `"branches"` in `vol13/volcfg.json` (and set `"branch"` to it), commit, push. Never force-push; no pull request; merge into `main` only when the user says so.
2. `pip install indic-transliteration rapidfuzz openpyxl anthropic`
3. `python3 tools/rv/batch.py audit 13` must print `AUDIT PASS` (nothing translated yet: "done through printed p. 0"). The API key is the environment variable `RIK_API_KEY`; never print it.
4. Money: every `submit` and every `api_front.py` call spends from the user's API budget. **Show the user the estimate that `plan` prints and wait for a yes before each `submit`.** Ask the user how much of the budget is left for this volume before the first one.

## Prepare the text (once, before anything is sent)
The scaffold is there (`vol13/volcfg.json` with the Vol 17 conventions, empty output files); the supplied text is not. Do what `vol18/STATUS.md` ("Source and inputs") describes for Vol 18:
1. Ask the user to upload the files (`rig_13_1.md`, …); put them in `vol13/html/`, merge them losslessly into `vol13/html/rig_13.md` with `tools/rv/merge_md.py`; pictures out to `vol13/html/figures/`; converter footer lines removed; nothing else changed.
2. `python3 tools/rv/html_pages.py` on it: page range (the scan edition had printed pp. 1–657), **missing page numbers** (list them in `STATUS.md` now, lesson 54), where printed p. 1 begins (insert `<!-- page 1 -->` there if the text has no marker, as in Vol 18). Record the front-matter line numbers (preface, contents, abbreviations) in `vol13/html/_layout.json`.
3. Set `source` in `volcfg.json` to the real page range; scope from the text itself (expected: Maṇḍala 1 Sūktas 166–183, Fourth Adhyāya of the Second Aṣṭaka; say so if the text shows otherwise). Confirm with the user that the English printed under the verses is to be headed "English translation (H. H. Wilson)" as in Vols 17–18.
4. `python3 tools/rv/batch.py audit 13` passes; `python3 tools/rv/api_batch.py plan 13 --windows 5` (free) for the token count per page. Update `vol13/STATUS.md`, commit, push, and tell the user what the text looks like before any `submit`.

## Order of work
1. **The preface first** (it stands before printed p. 1, so no window covers it): `python3 tools/rv/api_front.py 13 FIRST LAST preface` (one request; line numbers from `vol13/html/_layout.json`; skip if this volume has no preface). If it prints PROBLEMS, repair `vol13/work/preface/en.md` by hand as the message says and rebuild; then `python3 tools/rv/api_front.py 13 113 677 preface --install`, `audit 13`, commit, push.
2. **The body in stages of about 40 windows** (about 240 pages, about $3 each at Vol 17's rate; about 657 pages in all):
   - `python3 tools/rv/api_batch.py plan 13 --windows 40` (free: prepares the windows, counts tokens, prints the estimate) → tell the user → on yes `python3 tools/rv/api_batch.py submit 13`.
   - Wait in the background (one job, nothing else on the repo meanwhile): poll `python3 tools/rv/api_batch.py status 13` every 30 s until it says `ended`, then `python3 tools/rv/api_batch.py collect 13`. `collect` applies each answer, lets the scripts settle what they can (quotations, quotation markers, references, remarks, unplaced blocks, duplicate headings: all logged, `**NOTE**` where a decision is needed), runs the gates and commits window after window in page order. **No retries are sent** (default).
   - If `collect` stops at a window (`STOP at …`): read `WIN/gate_failure.txt`, repair `WIN/en.md` or `WIN/kn.md` by hand (`batch.py fix`; letters of the supplied text unchanged; never change what the print says to pass a gate), check with `python3 tools/rv/batch.py done 13 WIN --dry-run`, then run `collect 13` again: finished windows are skipped. Only if a whole page was left untranslated, re-send that stage's failures on purpose with `collect 13 --retries 1` and say so.
   - While `collect` runs do not commit, push or switch branches yourself: it commits and pushes every window. Afterwards: `audit 13`, update `vol13/STATUS.md` (page reached, cost of the stage from `vol13/parts/batch_costs.md`, windows that needed a hand repair, number of `**NOTE**` marks), commit, push, and report to the user in a few lines before planning the next stage.
3. **After each stage look at the text itself**, not only at the counts: print one complete Ṛk of the new pages and the first lines of `vol13/review/notes.tsv` additions; check that no sūkta heading is missing in sequence.
4. **End of the volume** (the last printed page with its colophon and closing lines, nothing added): do the three steps of "After the last page", update `STATUS.md` with the totals and stop. The rest of the finishing checklist (`docs/HANDBOOK.md` §11: accent report, QA sample, PDFs) is a separate job: do not start it without the user.

## After the last page (free, by script; no API)
1. `python3 tools/rv/batch.py rkheads 13 --dry-run` must say "nothing to change"; every sūkta's Ṛks numbered 1…n; `python3 tools/rv/kn_headings.py 13 --write`.
2. **Second reading from the old translation**: compare, per printed page, the numerals and references (book.chapter.verse, verse numbers, Pāṇini sūtra numbers) of `vol13/legacy/…_scan.md` with the new English. Put the result in `vol13/review/legacy_compare.tsv` (page, old, new). Do not change the new text from it: the supplied text is the base. The list is for the user. Write this as a shared script in `tools/rv/` (Vol 14 has 466 `[?]` and may go the same way).
3. `vol13/review/user_readings_part1.tsv` holds 38 readings the user gave for the old file (key = page_doubt number). List next to each what the new text has at that place; where they differ, add a `**NOTE**` row. The user's reading is not overruled silently.

## Stop and tell the user when
- `audit 13` fails and you cannot see why, or `collect` stops twice at the same window;
- a stage costs more than twice its estimate;
- the scope in `vol13/STATUS.md` does not fit what the text shows (a sūkta number out of sequence, a missing page range);
- the usage limit is near: commit and push first; the next session resumes with this same prompt (`plan` continues after the last committed page).

## What the user decided for this edition (already in `volcfg.json` and `tools/rv/BRIEF.md`; do not change without asking)
No translator remarks in the English text, one mark `**NOTE**` with the question in `review/notes.tsv`; no Kannada script in the English text; every part of a Ṛk under its own sub-heading; the bhāṣya block in Devanagari only, followed by a Gist that covers most of it; transliteration everywhere else; Pratipadārtha one word per line; the edition's printed English headed "English translation (H. H. Wilson)" (the user is still checking this attribution); a grammar section, where the volume has one, rendered in Sanskrit.
