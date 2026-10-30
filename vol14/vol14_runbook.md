# Vol 14 — translation runbook (LEAN MODE, Oct 30, 2026; from the Vol 13 experience)

Priority: **tokens**. Only the translation work; no audits, no sample tests, no calibration passes, no whole-volume scans. Conventions of CLAUDE.md apply (three-layer Sanskrit, per-Ṛk structure, printed English reproduced with [sic], progress-note pattern, digit key).

## Set-up (cheap; once)
1. **Page offset by sampling (about 6–8 pages, spread over the volume), not by reading every page.** View header-strip contact sheets of ~every 25th page: `python3 vol14/tools/numsheets.py FIRST LAST PREFIX` makes a sheet of header number strips (75 pages per sheet by default; build a sheet over a list/step by giving a small range, or a whole 75-page block when you need it). Offsets that agree at the sampled pages = no missing/duplicate pages in between; if the offset changes between two samples, bisect there. Front matter is numbered in roman (record its offset). Set OFFSET in vol14/tools/cfg.py; write the findings in vol14/vol14_state.md.
2. **Range only:** view the title page once (~100 dpi) for the Sūkta range; if a digit is doubtful, confirm it against the ordinal word on the title page or the last contents heading. Do NOT build lists of sūkta start pages or Ṛk counts up front: each sūkta opens with a heading block (Sūkta number, Ṛk count, ṛṣi, devatā, chandas) which you read when you reach it (a short crop; `python3 vol14/tools/findhead.py PDFPAGE` can locate it, locating only). No per-sūkta page counting.
3. Check by eye whether any scan page is upside down before building any tool for it (Vol 13's prompt claimed some were; none were).

## Work (per sūkta)
- View each page **once** at ~100–120 dpi (`python3 vol14/tools/view.py PDFPAGE OUT.png 110` — whole-page fractions; crops: `view.py PDFPAGE OUT.png DPI y0 y1 x0 x1`); **zoom only a crop that is in doubt** (small-type numerals, garbled letters); several doubtful lines can be stacked into one image: `python3 vol14/tools/stack.py OUT.png 300 PAGE:y0:y1 PAGE:y0:y1 …`.
- Write the English file page-anchored: mark each printed page as you reach it; never carry numbers from another scan. Append chunks with `python3 vol14/tools/append_en.py "PROGRESS NOTE" < chunk.md` (keeps exactly one trailing progress note; asserts the file did not shrink).
- Devanagari + English written by you; **IAST by script**: `python3 publish/tools/translit/add_iast.py FILE.md`. Sāyaṇa-bhāṣya stays in Sanskrit (Devanagari) with a one-line gist (≤ 25 words) where needed; grammar pages: 2–4 line note only (CLAUDE.md "Cost-saving rules").
- Numerals: read at zoom the first time when small; `[?]` if still undecidable; never from memory. Log a doubtful reading with its crop: `python3 vol14/tools/doubt.py PDFPAGE y0 y1 x0 x1 "note"` (→ vol14/review/doubts_v14.json); the user later reviews them on one page (`vol14/tools/doubts_v14.py`).
- No OCR for readings (Tesseract may at most help locate a line); if an image view returns no image: STOP and write nothing for that page.

## Hygiene
- Commit and push after every sūkta (or ~15 pages). One branch (`claude/vol14`); never force-push or reset; merge to main only when the user says; no PRs.
- Update `vol14/parts/session_state.md` (done-through printed page / Ṛk, next step) at every push. A session sees ~45–60 images before its context fills: finish the current Ṛk, push, tell the user to start the next session with `vol14/CONTINUE_PROMPT.md`.

## Lessons from the Vol 13 set-up (apply)
1. No whole-volume Tesseract scans (20+ min, dropped twice); contact sheets of header strips instead.
2. Never crop a header by a fixed fraction of the page; `numsheets.py` finds the header row from the ink profile. Crops everywhere are whole-page fractions.
3. A prompt's premises are claims to check by eye (e.g. "pages upside down").
4. Confirm range numerals from the contents' word forms.
5. Front matter is numbered separately (roman); the contents title page may be unnumbered but counted.
6. Git/LFS: if `git checkout -b … origin/main` fails with "should have been a pointer", use `GIT_LFS_SKIP_SMUDGE=1 git -c filter.lfs.clean=cat -c filter.lfs.process= -c filter.lfs.required=false checkout -f -b BRANCH origin/main`, then `git lfs pull` for the scans needed.
7. Background jobs: kill by PID, never `pkill -f PATTERN` (can kill your own shell); don't poll with sleep.
8. Ask before long or costly steps; give the cheap alternative in the same message.
