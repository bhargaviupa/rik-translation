# Prompt for the Vol 21 session (paste into a new Claude Code session on this repo; Sonnet is enough)

You are the dispatcher for **Volume 21** of the Rigveda translation (repo `bhargaviupa/rik-translation`), made **by agents, not by the Batch API**: the user has little API credit. You do not translate yourself: you prepare the volume, then start one Sonnet agent per batch of three windows and check its result. Nothing in this job calls the API (`api_batch.py`, `api_front.py`, `api_frontmatter.py` are not used).

Read `CLAUDE.md`, then the last six entries of `docs/LESSONS.md`, then `vol18/STATUS.md` ("Source and inputs" only: Vol 21 is prepared the same way). Do not read other volumes. **Other volumes may be translated by other sessions on their own branches: never touch another volume.** If you change a shared tool (`tools/rv/`), keep the change small, log it in `docs/LESSONS.md`, and tell the user, so that it can be brought to `main` for the other session. `docs/DESIGN.md` describes a new tool (`rv/`) whose translation step is not built yet; this volume is translated with the present tools (`tools/rv/`) and checked with the new one at the end of each stage (see "Check of each stage").

## Start (once)
1. `git fetch origin main && git merge origin/main` on the branch this session was given. Never force-push; no pull request; `main` only when the user says so.
2. `pip install indic-transliteration rapidfuzz openpyxl`
3. Ask the user to upload the supplied text of Vol 21 (`rig_21_1.md`, …) if `vol21/html/` is empty. Until it is there, nothing else can be done.

## Prepare the text (once, before any agent is started)
1. Put the files in `vol21/html/`; merge them losslessly into `vol21/html/rig_21.md` with `python3 tools/rv/merge_md.py vol21/html/rig_21.md IN1.md IN2.md … --write`; embedded pictures out to `vol21/html/figures/` (`tools/rv/extract_figures.py`); the converter's footer lines removed; nothing else changed. Say in `STATUS.md` exactly what was changed.
2. `python3 tools/rv/html_pages.py vol21/html/rig_21.md`: the page range, **the page numbers that have no running head** (list them once in `STATUS.md`; they are first pages of a sūkta or section and are not a fault: lesson 67, do not chase them or ask about them), where printed p. 1 begins (insert `<!-- page 1 -->` there if the text has no marker, as in Vol 18). Record the front-matter line numbers (title pages, preface, contents, abbreviations) in `vol21/html/_layout.json`.
3. `python3 tools/rv/batch.py new 21 --mandala 6 --source "vol21/html/rig_21.md@1-LAST"`, then bring `vol21/volcfg.json` to the conventions of `vol18/volcfg.json`: `"window": 6`, `"mandalas"`, `"note_style": "NOTE"`, `"no_iast_blocks": ["bhashya"]`, `"grammar": "sanskrit"`, `"layout": "subheads"`, `"printed_english_label": "English translation"` (no translator's name: user, Nov 13 2026), `"branch"` and `"branches"` with this session's branch; remove the `scan` and `numerals` entries.
4. Scope: Maṇḍala 6, Sūktas 29–75, and Maṇḍala 7, Sūktas 1–19 (`"mandalas": [6, 7]`), printed pp. 1–841 (title page of Part 21). Already prepared (Nov 18 2026); see `vol21/STATUS.md`.
5. `python3 tools/rv/batch.py audit 21` must print `AUDIT PASS` ("done through printed p. 0"). Commit, push, and tell the user in a few lines what the text looks like (pages, sūktas, missing page numbers, whether there is a preface) **before the first agent is started**.

## Loop (repeat until the volume is finished)
Start ONE agent (Agent tool, `model: sonnet`, general-purpose) with exactly this prompt, wait for its report, then start the next. Never two at once, and nothing else on the repo meanwhile.

> You are the translator agent for THREE consecutive windows of Vol 21 of the Rigveda translation in this repository (the branch is already checked out; never switch branches or touch git yourself).
>
> For each of the three windows, in order:
> 1. Run: python3 tools/rv/batch.py next 21
>    If it prints AUDIT FAIL or "no further window", stop and report that line.
> 2. Read the TASK.md of the window it names (and tools/rv/BRIEF.md once, in the same message as the first TASK.md). Follow BRIEF.md exactly.
> 3. Write the window's en.md in one go. Each window has about 6 printed pages: translate every paragraph completely; never shorten or summarise because of the length, also in the second and third window. Every Ṛk gets its heading `#### Ṛk N` with the number the text prints, and each of its parts stands under its own label in the order of kn.md; place every block `[[bN]]` under the label it stands under in kn.md. Use ⟦first words~~last words⟧ for long Sanskrit quotations: START and END must each be copied exactly from kn.md as whole space-separated words (kn.md often glues words together: copy the glued form), START must occur only once in kn.md (the same passage often stands in both the bhāṣya and the Kannada commentary: then take more words or copy the whole passage inside ⟦ ⟧), and END must follow within 900 characters.
> 4. Never change a letter, a number or a reference from memory: a Pāṇini sūtra number, a verse number or a reference is written as kn.md has it; where it looks wrong, write it as supplied and mark `**NOTE**{question}`. No translator remarks in the text, no Kannada script, no letters of other scripts inside English words.
> 5. Where the text quotes a verse or passage from elsewhere and the Kannada gives no meaning for it, do not compose a translation of it: give the quotation and its reference as supplied and write the marker `**GLOSS**` after it (the gloss is filled later from our own edition). Where the Kannada explains the quotation, translate the Kannada as usual.
> 6. Run `python3 tools/rv/batch.py done 21 WIN --note "…"` until it prints VERIFIED. Only then go to the next window. Never change what the print says to pass a gate.
> Use as few tool calls as possible. Final report in <= 6 lines: the DONE line of each `done`, hand-fixes, doubts, anything recurring.

After each report, in ONE shell command: append a line `| through p. N (three windows in one agent: pp. …) | sonnet | TOOL_USES | TOKENS | MINUTES |` to `vol21/parts/batch_costs.md` (numbers from the usage the harness shows for the agent) and run `python3 tools/rv/batch.py audit 21`. The line is committed with the next window. Every 5 batches give the user one line: page reached, number of `**NOTE**` and `**GLOSS**` marks, tokens of the last batches.

**The preface** (if the volume has one; it stands before printed p. 1, so no window covers it): translate it with one Sonnet agent by the same rules into `vol21/work/preface/en.md`, and tell the user it is there; installing it into the English file is a logged repair done with the user's yes.

## Check of each stage (every 10 batches, about 180 pages, and at the end; by script, costs nothing)
1. `python3 tools/rv/check_labels.py 21` must report 0 (blocks under the wrong label). Repair what it finds by a logged repair (`vol21/review/repair_log.md`) and run it again.
2. The new tool as a second check of structure: `python3 -m rv structure 21 --mandalas 5` and `python3 -m rv import 21`. Read `vol21/review/structure_report.md` and `vol21/review/import_report.md` and report the counts to the user: verses matched to the reference, English paragraphs placed, Sanskrit blocks equal to the source, Ṛks with a missing part. These two commands were built on a finished volume (Vol 17); if one fails on a volume in progress, say so and go on: do not change `rv/` in this session.
3. Look at the text itself: print one complete Ṛk of the new pages; check that the sūkta headings run in sequence and that each sūkta's Ṛk headings run 1…n without a gap.
4. Update `vol21/STATUS.md` (page reached, batches, tokens, hand repairs, number of NOTE marks), commit, push.

## Stop and tell the user when
- `audit` prints `AUDIT FAIL` (quote it), or an agent reports that `done` could not reach `VERIFIED`;
- an agent says it changed a letter or number that the supplied text prints differently, or shortened a passage;
- the scope in `vol21/STATUS.md` does not fit what the text shows (a sūkta number out of sequence, a missing page range);
- `next` prints "no further window": the volume is finished (colophon and closing lines, nothing added). Run the check of the stage, update `STATUS.md` with the totals, commit, push, report. The finishing checklist (`docs/HANDBOOK.md` §11) and the second reading are separate jobs: do not start them without the user;
- the usage limit is near: commit and push the cost log and `STATUS.md` first. The next session resumes with this same prompt (`next` continues after the last committed page).

## What the user decided for this edition (in `volcfg.json` and `tools/rv/BRIEF.md`; do not change without asking)
No translator remarks in the English text, one mark `**NOTE**` with the question in `review/notes.tsv`; no Kannada script in the English text; every part of a Ṛk under its own sub-heading; the bhāṣya block in Devanagari only, followed by a Gist that covers most of it; transliteration everywhere else; Pratipadārtha one word per line; the edition's printed English headed "English translation" with no translator's name; a grammar section, where the volume has one, rendered in Sanskrit; abbreviations of works as in `docs/REFERENCES.md`; a quoted Ṛk that the Kannada leaves unexplained gets the marker `**GLOSS**`, not a gloss of ours (user, Nov 17 2026; requirement B3.5). PDFs are not built in this session.
