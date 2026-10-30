# Vol 13 — translation runbook (DRAFT, to be agreed)

Goal: near-zero errors on the FIRST pass. Principles come from the Vol 5/6 correction passes.

1. **Page map first.** A script reads the printed page number and header on every scan page, writes the PDF→printed map and flags missing/duplicate/out-of-order pages. Use the best scan.
2. **Page-anchored file.** One section per printed page (`### Page N`), number read from the scan; never move text across pages except documented page-break splits. Never copy PDF numbers from another scan.
3. **Numerals right the first time.** Calibrate the digit key first (2/7, 3/5, 6/7, 8/9). Zoom every numeral to ~300 dpi when first seen; `[?]` only if still undecidable; never from memory.
4. **One source of truth.** Transcribe the Kannada once; generate Devanagari and IAST by script, so the Sanskrit layers cannot disagree; English from the Kannada. (Vol 11 setup.)
5. **Lint after every unit.** Impossible/out-of-range references, Ṛk/sūkta numbering gaps, non-monotonic vargas, the same reference read two ways. Fix or `[?]`.
6. **Doubts recorded while viewing.** Save crop-band coordinates (whole-page fractions, one coordinate system) for every doubtful item; build the doubts page at the end of each unit; the user reviews only doubts (empty box = accepted).
7. **Measured quality.** After each unit a separate session re-reads a random ~10% of lines blind and diffs; redo the unit if the disagreement exceeds the agreed threshold.
8. **Small sessions.** 15–25 pages per session, stacked crops of only the lines needed, a state file per worker, a fresh session per unit. No OCR for readings (locating only); if an image view returns no image STOP and write nothing.
9. **Worker hygiene.** One worker per page range and branch; never reset/force-push; merge to main only with the no-work-lost check; corrections from the user are applied by the owning worker.
10. Conventions of CLAUDE.md apply (three-layer Sanskrit, source's printed English reproduced with [sic], Special Topics, grammar pages noted briefly, progress note pattern).

## Lessons from the Vol 13 set-up (apply to every later volume)
1. **No whole-volume OCR scans.** Kannada Tesseract on a full page takes ~5–10 s; a 677-page orientation or heading scan runs 20+ min and was dropped twice. Find flipped pages and page numbers with **header-strip contact sheets** instead: `python3 vol13/tools/numsheets.py FIRST LAST PREFIX` (75 pages per sheet, ~2 s per sheet to build, 8 sheets for a whole volume). OCR only for a handful of pages, and only to locate.
2. **Never crop a header by a fixed fraction of the page** (it drifts between pages and cuts numbers). `numsheets.py` finds the header row from the ink profile (locating only) and crops tightly around it. Crops in `view.py`/`stack.py` are **whole-page fractions** (the old text-block auto-crop mis-scaled).
3. **Premises in a prompt are claims to check.** Vol 13's prompt said several pages were upside down; none were in the body (header strips PDF 22–677 and views of PDF 1–26). Check by eye first, then build tools only for what is really there.
4. **Read range numerals from words as well as digits.** The title page's last sūkta number was first read 184; the contents' word forms (ಎಂಭತ್ತ್ಮೂರನೆಯ = 83rd) and sequence showed 183. Zoom the digit, and confirm with the contents headings.
5. **Contents list topic start pages, not the heading block.** The "ಸೂಕ್ತ—N / ಮಂಡಲ—೧ ‖ ಅನುವಾಕ ‖ ಅಷ್ಟಕ ‖ ಅಧ್ಯಾಯ ‖ ವರ್ಗ / ಋಕ್ಸಂಖ್ಯೆ / ಋಷಿ / ದೇವತಾ / ಛಂದಸ್ಸು" block carries the Ṛk count, varga range, ṛṣi, devatā and metres; the prose "ಇದರಲ್ಲಿ … ಋಕ್ಕುಗಳಿರುವವು" just before it gives the count in words. View that block (a short crop) for each sūkta.
6. **Front matter is numbered separately** (roman). Record its offset; the contents title page may be unnumbered but counted.
7. **Git/LFS.** If `git checkout -b … origin/main` fails with "should have been a pointer", the working copy of a scan is the real file: use `GIT_LFS_SKIP_SMUDGE=1 git -c filter.lfs.clean=cat -c filter.lfs.process= -c filter.lfs.required=false checkout -f -b BRANCH origin/main`, then `git lfs pull` for the scans needed (scans are normal files in vol13/scans/).
8. **Background jobs.** `pkill -f PATTERN` can kill your own shell; kill by PID (`ps -eo pid,comm,args | awk … | xargs kill -9`). Kill a job you drop, and ignore expired-Monitor notices for it. Do not poll with sleep.
9. **Ask before long or costly steps**; give the cheap alternative in the same message.
