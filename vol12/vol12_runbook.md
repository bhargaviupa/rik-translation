# Vol 12 — translation runbook (DRAFT, to be agreed)

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
