# Vol 10 — correction method (Nov 2 2026, user decision; replaces the earlier draft)

**Models: Sonnet only, for the coordinator session and for every worker. Never Opus (cost).** CLAUDE.md rules apply (no OCR for readings; image view returns no image → STOP; never fill from memory; three-layer Sanskrit; one progress note).

## Phase 1 — numerals from the user's files (NO page images, no scan viewing)
1. The user puts `.xls/.xlsx` files with the correct Kannada numerals into `vol10/numerals/`. First action: open them, describe the format in `vol10/numerals/README.md` (nothing assumed).
2. Write `vol10/tools/apply_numerals.py`: for each row, find the one place in `Rigveda_Samhita_Vol10_English_Translation.md` it refers to (page marker `### Printed p. N` / page anchor + the surrounding words or the existing partial reference), convert Kannada digits to Arabic, and replace the `[?]` / `?` reference with the supplied number. **Apply only when the match is unambiguous (exactly one place, existing partial digits compatible with the supplied ones)**; otherwise list the row. Log every change as one line in `vol10/review/numerals_applied_v10.tsv` (page, old text, new text, file/row) and every unmatched or conflicting row in `vol10/review/numerals_unmatched_v10.tsv` with the reason. Never touch anything but the numerals; keep IAST/English layers consistent; the file must keep exactly one progress note and all headings (assert counts before/after).
3. Work in units (a range of pages or a sūkta) per worker; commit and push after each unit on `claude/pass2-vol10`; do not merge into main.
4. When the supplied files are exhausted: report the numbers **per sūkta** (`[?]` before / after, rows applied / unmatched / conflicting) and **STOP. Ask the user explicitly whether to start Phase 2. Do not start Phase 2 without an explicit yes.**

## Phase 2 — reading the remaining `[?]` from the scan (only after the user's explicit yes)
Method of the Vols 3–6 passes and the Vol 13 zoom-fix (`docs/COORDINATION_NOTES_Oct2026.md`):
1. Units: one sūkta or ~30 pages per Sonnet worker; state in `parts/wXX_state.md` (done-through, next step, open items); a fresh session per unit; archive finished sessions. Merge to main only when the user says, with the no-work-lost check (added lines, headings, one progress note).
2. Reading: `python3 vol10/tools/page.py PDFPAGE /tmp/pg` (trimmed strips; default 300 dpi = native resolution of the old scan; 400 for a better scan); view all strips of a page in one message. One zoom per doubtful place: `page.py PDFPAGE /tmp/z --strip K --box X0 Y0 X1 Y1 --dpi 450` (box in the coordinates of the image as displayed); it prints the fractions for `doubt.py`.
3. Places: every remaining `[?]` (page marker above it gives the page) plus running heads and Ṛk/Varga numbers. Correct with exact unique-match edits (`tools/apply.py`); keep IAST in step (`publish/tools/translit/add_iast.py` on the changed block).
4. Digits: CLAUDE.md digit key and the Oct 31 correction (round = 2, hooked = 3, flat-footed = 7; calibrate against the running header in the same crop).
5. Every zoomed place and every place left `[?]` goes to `review/doubts_v10.json` via `tools/doubt.py`; the user reviews one flat list (crop + empty box).
6. Turn economy: view all strips of a page in one parallel message, zoom in one message, write with one call, ~3 pages per sub-agent (`vol14/vol14_runbook.md`, "Turn economy").

## Hygiene
Never force-push or reset; no PRs; Git/LFS: `git lfs pull -I vol10/scans/Rig_Vol10.pdf` (Phase 2 only); use `git worktree` for side work; never switch branches while a worker writes in the same folder.
