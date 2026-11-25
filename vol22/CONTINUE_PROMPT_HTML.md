# Prompt for the Vol 22 session (paste into a new Claude Code session on this repo; Sonnet is enough)

You are the dispatcher for **Volume 22** of the Rigveda translation (repo `bhargaviupa/rik-translation`), made **by agents, not by the Batch API**. You do not translate yourself: you start one Sonnet agent per batch of three windows and check its result. Nothing in this job calls the API. Read `CLAUDE.md`, then the last ten entries of `docs/LESSONS.md`, then `vol22/STATUS.md` (all of it: how the supplied text was ordered, which 127 pages were transcribed from the scan and have no accents, the scope).

## Start
1. `git fetch origin main && git merge origin/main` on the branch this session was given (`claude/hopeful-fermi-kypcts`). Never force-push; no pull request; `main` only when the user says so.
2. `pip install indic-transliteration rapidfuzz openpyxl`
3. The volume is already set up (Nov 25 2026): `vol22/volcfg.json`, `vol22/html/rig_22.md` (600 printed pages, `<!-- page P -->` markers), `vol22/STATUS.md`. `python3 tools/rv/batch.py audit 22` must print `AUDIT PASS`. Printed p. 1 holds the title page, the Ganesha invocation, the preface (ಪೀಠಿಕೆ) and the start of Sūkta 20: they are part of window w0001 (no separate preface job). Scope: Maṇḍala 7 from Sūkta 20 (`"mandalas": [7]`; the end of the range is to be read from the text).
4. Pages 1-600 only; the 127 pages transcribed from the scan carry no Vedic accents and some doubtful words (`vol22/html/pages_map.tsv`): translators mark nothing extra for that; the second pass proofreads them.

## Loop (repeat until the volume is finished; the user has said: keep going unless you are stuck)
Start ONE agent (Agent tool, `model: sonnet`, `subagent_type: general-purpose`, foreground) with exactly this prompt, wait for its report, then start the next. Never two at once, and nothing else on the repo meanwhile (the agent's `done` commits and pushes).

> You are the translator agent for THREE consecutive windows of Vol 22 of the Rigveda translation in this repository (the branch is already checked out; never switch branches or touch git yourself; `batch.py done` does the committing).
>
> For each of the three windows, in order:
> 1. Run: python3 tools/rv/batch.py next 22
>    If it prints AUDIT FAIL or "no further window", stop and report that line.
> 2. Read the TASK.md of the window it names (and tools/rv/BRIEF.md once, in the same message as the first TASK.md). Follow BRIEF.md exactly.
> 3. Write the window's en.md in one go. Each window has about 6 printed pages: translate every paragraph completely; never shorten or summarise because of the length, also in the second and third window. Every Ṛk gets its heading `#### Ṛk N` with the number the text prints, and each of its parts stands under its own label in the order of kn.md; place every block `[[bN]]` under the label it stands under in kn.md. Write a `**Saṃhitā-pāṭha**` (or any other part) label ONLY where kn.md has that label at that place; where kn.md has none, write none. NEVER use a `## ` heading except for a sūkta or maṇḍala heading that kn.md has (verify fails otherwise); every other heading, including appendix headings and sub-headings of introductions, is a bold line. Each sūkta that kn.md announces (a "ಸೂಕ್ತವು" line, a `ಸೂಕ್ತ—N` head) gets its own `## Sūkta N (Maṇḍala M)` heading with the number printed in the `ಸೂಕ್ತ—N` head line (where the spoken-number line disagrees, use the head-line number and mark a NOTE). Use ⟦first words~~last words⟧ for long Sanskrit quotations: START and END must each be copied exactly from kn.md as whole space-separated words (kn.md often glues words together: copy the glued form; never retype a word, copy it; if a quotation cannot be copied, translate it into English instead of writing Sanskrit in Latin letters), START must occur only once in kn.md (the same passage often stands in both the bhāṣya and the Kannada commentary: then take more words or copy the whole passage inside ⟦ ⟧), and END must follow within 900 characters.
> 4. Never change a letter, a number or a reference from memory: a Pāṇini sūtra number, a verse number or a reference is written as kn.md has it; where it looks wrong, write it as supplied and mark `**NOTE**{question}`. No translator remarks in the text (also no parenthetical remarks of your own), no Kannada script, no letters of other scripts inside English words.
> 5. Where the text quotes a verse or passage from elsewhere and the Kannada gives no meaning for it, do not compose a translation of it: give the quotation and its reference as supplied and write the marker `**GLOSS**` after it (the gloss is filled later from our own edition). Where the Kannada explains the quotation, translate the Kannada as usual.
> 6. Run `python3 tools/rv/batch.py done 22 WIN --note "…"` until it prints VERIFIED. Only then go to the next window. Never change what the print says to pass a gate. If `done` fails after it has committed, report exactly what failed and stop; do not hand-edit output files. Do not use `--api` (no API key is available or wanted); accent gaps stay listed.
> Use as few tool calls as possible. Final report in <= 6 lines: the DONE line of each `done`, hand-fixes, doubts, anything recurring.

**After each report** (the token count arrives with the agent's completion notice, a moment after its report; wait for it): in ONE shell command append `| through p. N (three windows in one agent: pp. …) | sonnet | TOOL_USES | TOKENS | MINUTES |` to `vol22/parts/batch_costs.md`, run `python3 tools/rv/batch.py audit 22`, and commit + push the cost line (`audit` fails on an uncommitted file, so commit first, then audit). Expect `AUDIT PASS`. Every 5 batches give the user one line: page reached, number of `**NOTE**` and `**GLOSS**` marks, tokens of the last batches.

**An agent stops after one or two windows** because `done` printed `VERIFY FAIL` after it had committed. The window is committed but the audit fails. Typical causes seen in the earlier volumes, each repaired by **you, the dispatcher, as a logged repair** (one line in `vol22/review/repair_log.md`; look at the lines first; edit the volume file and the window's `en.md`; never touch the Kannada file or the Sanskrit; commit, push, `audit`, then start the next batch with the cause named in the agent prompt):
- a `## ` heading that is not a sūkta/maṇḍala/preface ("chapter-level heading"): make it a bold line;
- "N Saṃhitā labels in the Kannada file but N+1 sub-headings in the English": remove the extra `**Saṃhitā-pāṭha**` label the agent wrote where kn.md has none (in the volume file it stands as `##### ॥ संहितापाठः ॥ (Saṃhitā-pāṭha)`; remove that line and its blank line).
Do not run `git checkout` or `git restore` on `work/` or any output file.
If you cannot repair it, stop and tell the user.

**Stage check** (every 10 batches, and at the end; by script, costs nothing):
1. `python3 tools/rv/check_labels.py 22` must report 0 under the wrong label.
2. Sequence by script: every `## Sūkta N` heading present in order (the headings of the earlier volumes: Sūkta 86 was missing because the Kannada's spoken number was wrong and the agent did not write it; look for a sūkta whose Ṛk headings run 1…n and then 1…m again), each sūkta's `#### Ṛk` headings run 1…n without gap, `## Maṇḍala M` before its first sūkta. Repair what is missing by a logged repair.
3. Print one complete Ṛk of the new pages and look at it.
4. Update `vol22/STATUS.md` (page reached, batches, tokens, hand repairs, NOTE and GLOSS counts), commit, push.

## Stop and tell the user when
- `audit` prints `AUDIT FAIL` that you cannot repair as above (quote it), or an agent reports that `done` could not reach `VERIFIED` for a reason not listed;
- an agent says it changed a letter or number that the supplied text prints differently, or shortened a passage;
- the scope in `vol22/STATUS.md` does not fit what the text shows (a sūkta number out of sequence that the head line does not explain, a missing page range);
- `next` prints "no further window": the volume is finished (colophon and closing lines, nothing added). Run the stage check, update `STATUS.md` with the totals, commit, push, report. The finishing checklist (`docs/HANDBOOK.md` §11) and the second reading are separate jobs: do not start them without the user;
- the usage limit is near: commit and push the cost log and `STATUS.md` first. The next session resumes with this same prompt (`next` continues after the last committed page).
Otherwise keep going from batch to batch without asking.

**The preface** (if the volume has one; it stands before printed p. 1, so no window covers it): translate it with one Sonnet agent by the same rules into `vol22/work/preface/en.md`, and tell the user it is there; installing it into the English file is a logged repair done with the user's yes.

**Known tool gaps seen on the earlier volumes** (do not fix inside this job unless they stop you; they are in `docs/LESSONS.md`): the bhāṣya block swallowing the Pratipadārtha/Bhāvārtha lines under a garbled label (agents repair it with `batch.py fix`); a quotation START repeated in appendix passages; garbled Bhāvārtha labels (ಭಾಸಪಥ, ಭಾಸ್ಕರ); a page head missing inside a long page (agents add the marker with `batch.py fix`).

## What the user decided for this edition (in `volcfg.json` and `tools/rv/BRIEF.md`; do not change without asking)
No translator remarks in the English text, one mark `**NOTE**` with the question in `review/notes.tsv`; no Kannada script in the English text; every part of a Ṛk under its own sub-heading; the bhāṣya block in Devanagari only, followed by a Gist that covers most of it; transliteration everywhere else; Pratipadārtha one word per line; the edition's printed English headed "English translation" with no translator's name; a grammar section, where the volume has one, rendered in Sanskrit; abbreviations of works as in `docs/REFERENCES.md`; a quoted Ṛk that the Kannada leaves unexplained gets the marker `**GLOSS**`, not a gloss of ours (Nov 17 2026). PDFs are not built in this session.
