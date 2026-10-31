# Coordination notes — Oct 29–31, 2026

What was done by the coordinator session ("Numeral pass coordination Vols 3–5") over about three days, what was tried, and what it taught. Written so the next coordinator (or the user) does not repeat the experiments. Details of each volume: `docs/HISTORY.md` and each volume's runbook/state files.

## 1. What was done

**Correction passes on Vols 3–6** (numerals, accents, `[?]` readings) by parallel worker sessions, one branch per range (`claude/pass2-vol3`, `-vol4-a/-b`, `-vol5-a/-b/-c`, `pass2-vol6-a/-b/-c/-d`). Roughly 70 worker sessions, almost all Sonnet, 20–60 minutes each, one unit (a sūkta, a few Ṛks, or 30–50 pages) per session. Everything was merged into `main` with a "no work lost" check each time.
- **Vol 5**: all Sūktas, then the Pariśiṣṭa (pp. 566–708) in several passes; the user's readings from the 578–625 doubts page are recorded (`vol5/review/pending_doubts_p578-625_user_readings.txt`) but **not applied** (user: "leave it for now").
- **Vol 6**: full pass pp. 1–620 (w6a, w6b), ~600 unresolved `[?]` put on one consolidated doubts page; the user's readings were applied by w6c (one row, p. 618, not applied: `vol6/review/user_readings_apply_notes.txt`); 183 numeral rows (w6d) are on the "Vol 6 Numerals" page awaiting the user's typed digits.
- **Vol 3/4**: bare-`?` references fixed (`wr` session); Vol 3 grammar-note conflict check against the print still open (`vol3_merge_conflict_record.md`).
- **Doubts pages** (private Artifact pages with the `db` capability; edits saved per row) for Vols 5, 6 and 13.

**New-volume set-up:** folders for Vols 6, 12, 13, 14 (runbook, state file, tools, scans). Vol 12's scan is poor (300 dpi, 1-bit) and was deferred. **Vol 13** was translated by the user's own independent session (Sūktas 166–183, 657 pp., ~2,250 `[?]`) and merged. **Vol 14** is being translated by a dispatcher session the user runs (branch `claude/vol14-pilot`; 49 pages were done here as a pilot).

**Rebuild of deliverables** (docx/PDF for Vols 1–6 and 13, print PDFs for 1–6) was done by one session and pushed to `claude/rebuild-vols-1-6-13`; **not yet merged** (user deferred).

**Vol 13 zoom-fix** (re-view every logged doubt at 300–450 dpi and correct): 99 of 192 doubts of part 2 done (printed pp. 279–377; 94 resolved, 5 unresolved), merged. Parts 1, 3, 4 and the rest of part 2 not done; the user's 39 readings for part 1 are recorded (`vol13/review/user_readings_part1.tsv`), not applied.

## 2. Learnings

**Running parallel sessions**
- A worker session fills its context after ~45–60 image views (earlier ceiling ~240k tokens; newer sessions report a 1M window with compaction). One unit per session, a fresh session for the next unit, state in a part file in the repo (`parts/wXX_state.md`: done-through, next step, open items). Archive finished sessions.
- Workers stop early ("shall I continue?") unless told not to pause; "do not stop, continue until X" works only within the context budget. Put "never wait for an answer; if blocked write it in the state file and stop" in the prompt.
- Sessions started by a scheduled trigger have no git repo access (push 403): use `create_session` with the repo as source for anything that must commit.
- Never switch the working branch of a folder while a sub-agent is writing in it (this happened once; recovered because the file was committed first). Use `git worktree add` for side merges, with `GIT_LFS_SKIP_SMUDGE=1` (LFS checkout of the scans takes minutes).
- A per-session limit of 10 watched artifacts exists: do not watch doubts pages.
- Merge check that worked: count the added lines of the branch against the merged file, count headings, assert exactly one "**Progress note:**".
- Deleting remote branches by `git push` is blocked in these sessions: the user deletes them in the GitHub UI. `archive/old-history` must be kept (it was deleted by mistake once and restored from a local ref).

**Review pages**
- Publish only doubts pages, not "check" pages: the user found workers' readings almost always right.
- One row per doubt, crop + empty box; page = printed + offset; crops are whole-page fractions (a text-block/whole-page mismatch once shifted every crop). Artifact limit 16 MB per page: ~100 crops per 8–10 MB at 150 dpi/JPEG q45, ≤ 192 rows per page. Prefer one flat list over per-page/per-unit grouping.
- The user's typed readings are data: record them in the repo before anything else; apply only when asked.

**Reading the scans**
- Viewer limit: the Read tool shows an image up to ~2000 px unshrunk (a 2341-px strip was shown at 2000). The scans are ~660 ppi 1-bit, so full-width strips at ~360 dpi (`vol14/tools/page.py`) are read at full detail; a whole page at 400 dpi is shrunk and wasteful.
- Zoom-fix of logged doubts works: on Vol 13, 94 of 99 doubts were resolved at 300–450 dpi. The first-pass viewing at ~110 dpi was the cause of most `[?]`.
- Digit glyphs (see CLAUDE.md, correction of Oct 31): round open-loop = 2, hooked ಇ/ಖ-like = 3 (most often misread as 2), flat-footed = 7; calibrate against the running header in the same crop. Ma/ya with a hook ≠ u.
- Zoom coordinates: a model often mis-aims a zoom box; give the box in the pixel coordinates of the image as displayed (multiply by the viewer's stated factor) and check the zoom shows the intended word. `page.py --strip K --box …` prints the doubt coordinates.
- Sonnet vs Opus on Vol 14 (3 vs 5 batches of 6 pages): similar tokens per batch (~130–160k); Sonnet left 5–20 `[?]` places per batch and mis-aimed more zooms, Opus 2–7. Sonnet is acceptable for the Vol 13 zoom-fix (narrow, mechanical task), Opus for first-pass translation.

**Method decisions for new volumes** (`vol14/vol14_runbook.md`): offset by sampling ~6–8 header strips, no audits/inventories/orientation checks, English-only file, IAST by script (`add_iast.py` on the chunk only), a fresh translator agent per 6-page batch (an agent cannot drop old images from its context; the file holds the continuity), one doubts entry per zoomed place (zoomed places go to the user's review whether resolved or not).

## 3. Open items (as of Oct 31)
1. Vol 14: dispatcher session (user's) in progress; merge `claude/vol14-pilot`/`claude/vol14` to `main` when the user says.
2. Vol 13: zoom-fix of part 2 from entry 99 (printed ~377–471), then parts 1, 3, 4; apply the user's 39 part-1 readings; rebuild docx/PDF afterwards.
3. Vol 6: 183 numeral rows await the user's digits → a worker applies them → merge. Vol 6 p. 618 row not applied.
4. Vol 5: the user's recorded readings (pp. 578–625) not applied.
5. Rebuild branch `claude/rebuild-vols-1-6-13` not merged; rebuild again after the open passes (and Vol 14).
6. Vol 12 (poor scan): deferred.
7. Check Vol 14 numerals read before the 2/3/7 correction (pp. 2–55) against the glyph rule.
