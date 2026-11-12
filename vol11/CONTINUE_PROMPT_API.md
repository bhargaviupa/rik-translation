# Vol 11 — session prompt (Batch API route; written Nov 12 2026)

You translate Volume 11 of the Rigveda Saṃhitā (Maṇḍala 1 Sūktas 137–157, Second Aṣṭaka, Second Adhyāya; printed pp. 1–696) from the user's machine-read Kannada text into English, with the Batch API pipeline. Vol 11 was translated long ago from scans; this is a **re-translation from the supplied text** (the old files are kept as `vol11/Rigveda_Samhita_Vol11_scan_*`, for comparison only; do not edit or rebuild them). Everything is set up and committed; **nothing has been sent to the API yet**.

## Start
1. Work on branch `claude/gallant-dijkstra-e9ze2x` (it holds the whole set-up and tool state; `git fetch origin claude/gallant-dijkstra-e9ze2x`, check out or base your session branch on it). If your session branch has another name, set `"branch"` in `vol11/volcfg.json` to it before the first `done`/`collect`. Never force-push; no pull request and no merge into `main` unless the user asks.
2. `pip install indic-transliteration rapidfuzz openpyxl anthropic` (anthropic is needed by `api_batch.py`). `RIK_API_KEY` must be set in the environment (it was in the previous session; never print it).
3. Read: `CLAUDE.md`, `vol11/STATUS.md` (section "Re-translation from the supplied text"), `docs/LESSONS.md` (50–65 matter most: the Vol 17/18 batch runs and the Vol 18 QA bug), `tools/rv/BRIEF.md`.
4. `python3 tools/rv/batch.py audit 11` must say AUDIT PASS (progress note "Done through printed p. 0").

## What was decided (user, Nov 11–12 2026)
- Source: `vol11/html/rig_11.md` (the two supplied md files merged; the originals are in git history), 659 pages found, printed 1–696. 33 pictures are in `vol11/html/figures/` and appear as `[figure: …]` lines.
- **Printed p. 1** prints no number (the opening "ॐ" page): marker `<!-- page 1 -->` is in the file. **All pages exist even where the running head's number is missing**: 37 numbers have no head of their own (6, 24, 42, 66, 78, 100, 104, 129, 137, 140, 144, 149, 160, 176, 180, 210, 211, 226, 250, 262, 266, 278, 314, 334, 350, 382, 416, 457, 458, 482, 496, 510, 514, 532, 590, 651, 668); the script inserts their markers and says so in each window's TASK.md.
- **Printed p. 212 is not decided** (the head reads 211; pages 210 and 211 have no head): the mark `**NOTE**{printed page number 212? …}` goes on that page; `page_notes` in `volcfg.json` puts the instruction into the window's TASK.md. Do not decide it; keep the question in `review/notes.tsv`.
- Conventions of Vols 17–18 (`volcfg.json`): `note_style` NOTE (no remarks, no `[?]`, no "as supplied"), bhāṣya block Devanagari only + Gist, grammar rendered into Sanskrit (⟪ ⟫), sub-heading layout, window = 6 pages, Sonnet 5.5, effort medium. IAST of Saṃhitā/Pada blocks is made at print time (not stored). The heading of the English printed in the edition stays "Printed English".
- Route: **Batch API** (user's choice; no pilot wanted). Stages as in Vol 18 (lesson 55–58): stage 1 = the first 41 windows (printed pp. 1–267), then QA, then the rest.

## Tools taken in from the Vol 17/18 work (already in this branch; verify they run)
`html_to_kn.drop_dup_figures` (a figure line before a verse block/label is dropped and logged), `convert.expand` label restoration, `html_to_kn.quote_follows`, `batch.mandala_heading`, `collect` skips pages already appended, `done` runs `rk_headings` and checks the Kannada file first, the **label-mismatch gate** (`convert.label_mismatches`, lesson 61) and `tools/rv/check_labels.py` (also run by `batch.py audit` for sub-heading volumes). Lesson 60 says these have not yet run on a live batch: **Vol 11 stage 1 is their live test**; if one misbehaves, fix the shared tool, never a per-volume workaround, and log it in `docs/LESSONS.md`.

## The run
1. `python3 tools/rv/api_batch.py plan 11 --windows 41` (free; regenerates `vol11/work/`). Last plan: 41 windows, pp. 1–267, 1,061,173 input tokens (≈3,974 per page), estimate input $1.06 + output $2.65–6.37 (Vol 17 measured output ≈ 0.45 × input; the whole volume was estimated at $9.5–19 before retries). Show the user the estimate.
2. **`submit 11` spends money and the permission layer blocks it unless the user approves it directly: ask the user to approve or to run `python3 tools/rv/api_batch.py submit 11` themselves.** Do not work around the block.
3. `status 11`, then `collect 11` (writes each window's `en.md`, logs real cost in `vol11/parts/batch_costs.md`, runs the gates and commits window after window in page order, and stops at the first window whose gates fail). When it stops: read the gate message, repair that window (shared tool first, `batch.py fix …` for a one-off, repair logged in `vol11/review/repair_log.md`), `collect` again. After a hand repair of a window that `done` already committed set `"done": true` for it in `work/api_batch.json` (lesson 55). Typical stops in Vol 18: a figure line, a verse without `#### Ṛk N`/labels, a Ṛk continued across a window boundary.
4. **After stage 1 and before stage 2 (lesson 61): a QA sample** — about 24 pages, 3 fresh agents (≈100k tokens each), by a model that is not told what to expect, reading the English against `kn.md` for: labels one section off, Sanskrit shortened or paraphrased, English added to Sanskrit, wrong numbers/references. Run `python3 tools/rv/check_labels.py 11` and `python3 tools/rv/batch.py audit 11`. Report to the user: pages, cost (from `batch_costs.md`), windows that stopped and why, QA findings. Stage 2 only after the user has seen it.
5. Keep `vol11/STATUS.md` current; at the end add the lessons to `docs/LESSONS.md` and follow `docs/HANDBOOK.md` §11 (finishing checklist; print build is a separate decision).

## Rules to keep in mind
The supplied text is the base: never correct a letter or number from memory or another edition. The translator never types Devanagari or IAST. Output files are append-only, written only by `tools/rv/batch.py`. Quote counts/costs only from finished commands. Commit **and push** after every collect step.

## Stop and tell the user when
a window fails the same gate twice for a reason you cannot repair with a shared-tool fix; the real cost of a stage exceeds twice its estimate; the QA sample finds more than about one real error per four pages (compare Vol 12: one in four); a correction would change a heading or verse number structure; the usage limit is near (commit and push first; the next session resumes from this file and `vol11/STATUS.md`).

## Parked, not to be touched here
Vol 1 re-check against the supplied text (user reviewing; state in `vol1/STATUS.md`, `vol1/review/recheck/`, `vol1/parts/batch_costs.md`). The old Vol 11 build scripts (`publish/`, `publish/tools/verify11/`) still point to the old file names: update them only when the new Vol 11 is built.
