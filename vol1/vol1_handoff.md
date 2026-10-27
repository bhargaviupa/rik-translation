# Vol 1 numeral + [?] pass — handoff (state at end of session, Oct 2026)

**Scope (user's authorisation):** Vol 1 only — `Rigveda_Samhita_Vol1_English_Translation.md` (main) and
`Rigveda_Samhita_Vol1_Gaps_English_Translation.md`. Numerals, plus every `[?]` (words too) resolvable from the better
scan; a garbled word/passage next to a fixed numeral may be re-read from the print (note it). Nothing else; no other
volumes; leave `vol1/kannada/Rigveda_Samhita_Vol1_Kannada_Text.md` alone. Branch `claude/numerals-vol1-9efv8s`; commit +
push small batches; never push to main, no PR, no `git reset --hard`.

**User's rules:** the user's reading wins over the file. References in hyphen form `2-1-14` (as the book prints them),
never `2.1.14`. `[as printed]` where a printed number differs from the usual one; `[?]` only when the print does not
settle it. Printed English blocks ("Embedded English translation") are the source's text: do not change them.
**No progress messages to the user during or after the work until asked.** Keep tool output small (grep the lines
around a reference; crop images to the needed lines; ~100 dpi pages, 300–450 dpi zooms only for doubtful digits).

**Done:** PDF 1–600 (printed pp. 1–572): user's numeral edits placed, `[?]` resolved, all dotted references in the
main file converted to hyphen form (447). Log: `vol1/vol1_pass_log.md`. Remaining genuine `[?]`: Gaps
pp. 127, 132, 139 (table rows 6–7 vs printed 664), 273; main p. 556 first word of the TA 2-16 quote.

**Next:** scan parts 7–10 (`vol1/scans/01 Rigveda Samhitha Volume 1 7.pdf` … `10.pdf`) are on `origin/main`.
1. Extract them into the working tree: `git show "origin/main:vol1/scans/01 Rigveda Samhitha Volume 1 7.pdf" > "kannada/…7.pdf"`
   (same for 5–10 as needed; parts 5–6 are also only on main), and add them to `.git/info/exclude` (do not commit).
2. Add them to `PARTS` in `vol1/tools/cfg.py` (first global PDF page of each = previous first +
   previous part's page count; `pdfinfo` gives counts; part 6 starts at 501).
3. Extend `printed()` in `pages.py` for PDF 601+: last known offset is printed = PDF − 28 (PDF 510–600); check headers
   (`locate.py` writes `WORK/headers.json`) for duplicates/missing pages; add duplicate scans to `SKIP` in
   `build_review.py`.
4. Build review pages in runs of 100 PDF pages:
   `python3 locate.py A B` → `python3 latin_filter.py A B` → `python3 build_review.py A B vol1/review/review_PDFA-B.html "Vol 1 PDF A–B"`;
   commit the .html/.json, then stop and wait for the user's edits (they paste lines `PDF_index: reading`; save as
   `vol1/review/edits_PDFA-B.txt`).
5. Placing edits: `pagework.py REVIEW.json EDITS.txt A B` (user's readings vs file text per page); `view.py PDF OUT.png
   [DPI] [y0 y1]`; `qctx.py en|gaps PRINTED` lists `[?]` per page; `secrep.py` (per-page reference replace,
   `=` prefix = literal) and `apply.py` (exact unique replacements) apply JSON batches. Notes per page go to a notes file;
   `pass_log.py A B NOTES` appends the log.

**Digit key** (Kannada): ೧ ∩-like; ೦ ○; ೭ flat-footed "2"; ೨ curled "2"; ೬ hook top-left; ೮ like ಲ; ೯ like ಕ; ೪ like
ಳ; ೫ like ಣ; ೩ like ಇ. My usual confusions 3/5, 6/7, 2/9, 8/9 — zoom every doubtful digit, and check tables against
printed totals.
