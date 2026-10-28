# Vol 4 numeral + [?] + accent pass — runbook for unattended sessions

Authorised by the user (Oct 27, 2026): Vol 4 (`vol4/Rigveda_Samhita_Vol4_English_Translation.md`) is opened for the same
pass as Vol 2: **numeral corrections, `[?]` resolution, correction of other errors found against the better scan, and the
printed Saṃhitā accents**. Nothing else in Vol 4 changes; no other volume is touched (Vol 2 has its own branch and runbook).
Work on branch `claude/numerals-vol4` (create it from `main` if missing; merge `main` into it first); commit and push after
every page batch; **merge into `main` only when the user says so**; no PRs. No progress messages to the user. Each run is a
fresh session: read this file and `vol4/vol4_state.md` first, continue from where `vol4_state.md` says, update
`vol4_state.md` before stopping. The scheduled task starts Vol 4 only when `vol2/vol2_state.md` says "done".

## Inputs
- Main file: `Rigveda_Samhita_Vol4_English_Translation.md` at the **repository root** (not in `vol4/`; the build reads it there). Same pass
  as Vol 3: numeral corrections, `[?]` resolution, other errors found against the scan, printed Saṃhitā accents.
- Scan: the better scan `scans/04 RigvedaSamhithaVolume04 1..7.pdf` (701 PDF pages, `tools/cfg.py`); page map notes in `vol4_state.md`. **Work strictly in page order from the front; the extra page near PDF 101–105 is handled when reached, the 78 unexplained pages after PDF 623 only in the last batch.** The old `Rig_Vol4.pdf` is the fallback for any missing page.
- Tools in `vol4/tools/` (copied from `vol3/tools/`; run from that folder; `cfg.py` holds the paths, `WORK=/tmp/v4num/`). Review pages, edits and
  notes go to `vol4/review/`; the batch log is `vol4/vol4_pass_log.md`.
- No Vol 3-style special sections are known for Vol 4 (no redone block, no restored note). The preface (PDF 7–10) is untranslated by design.

## Steps (per run, in 100-PDF-page batches: PDF 1–100, 101–200, … 501–622)
Run the tools from `vol4/tools/`; the paths below are from the repository root.
1. **Review pages:** `locate.py A B` → `latin_filter.py A B` → `build_review.py A B vol4/review/review_PDFA-B.html`.
   Commit the .html/.json.
2. **Read the numerals yourself:** for every box of the batch, read the crop (`crop.py ID OUT.png [above]`, or `view.py`
   page crops at 250–450 dpi for doubtful digits) and write `vol4/review/edits_PDFA-B.txt` (`ID: reading`, `?` for an
   unreadable digit). Page-header numerals (Aṣṭaka/Adhyāya/Varga) need no entry. Digit key: ೧ ∩; ೦ ○; ೭ flat-footed "2";
   ೨ curled "2"; ೬ hook top-left; ೮ like ಲ; ೯ like ಕ; ೪ like ಳ; ೫ like ಣ; ೩ like ಇ. Usual confusions 3/5, 6/7, 2/9, 8/9,
   2/7 — zoom every doubtful digit; check sūtra and verse sequences and printed totals.
3. **Place the numerals** page by page (`pagework.py`, `secrep.py`, `apply.py`): fix wrong references, fill `[?]`/`.?`
   placeholders, hyphen form `2-1-14` (never `2.1.14`; Vol 4 often writes "P. 6-1-37" — keep the file's "P." / "Pā." style
   on the page, change only the number); `[as printed]` where the print differs from the usual number. Never supply a
   sūtra number the print does not give.
4. **Resolve the other `[?]` and hedges** on the same pages (`qctx.py`, `hedge.py`): re-read the Sanskrit/Kannada from the
   scan; replace garbled Devanagari with the printed text and give IAST (`publish/tools/translit/add_iast.py`'s
   `deva_to_iast`); fix English renderings that the print shows to be misreadings. Never fill from memory; keep `[?]` where
   the print does not settle a reading. Glosses not in the source are "mine and tentative".
5. **Other errors:** while each page image is open, correct clear misreadings next to what you checked (wrong counts, names,
   maṇḍala/sūkta numbers). Where the bhāṣya is marked "compressed" or is garbled, re-transcribe it in full from the print
   (as was done in Vol 2), with its grammatical tail summarised in English in parentheses; grammar pages may be rewritten
   from the print where they misstate it (short, with the printed sūtra numbers), inserting `### Page N` headings at page
   breaks when a section is split. Do not restyle or rewrite sound text.
5a. **Saṃhitā-pāṭha accents (user's requirement):** every Ṛk's Saṃhitā-pāṭha block must carry the accents as printed.
   Read the marks from the scan (`samcrop.py`, `acc.py` at 450 dpi) and rewrite the block with `sam.py JSON`
   (`[["### Pages 2–5 — Sūkta 20, Rik 1", ["deva line 1", "deva line 2"]]]`; it writes the IAST line with acute accents —
   then fix the IAST word spacing by hand and use `m̐` for `~`). Anudātta ॒ below, svarita ॑ above, udātta unmarked; the mark
   goes **after** a visarga/anusvara (`भिः॑`). Never accent from memory; where a mark cannot be read, leave that syllable
   unmarked and put `[accent ?]` after the line. Replace the note under the block (`*(accent-marks printed; not
   reproduced)*`, `*(Accent-marks printed in the source; not reproduced.)*` and similar) with
   `*(Saṃhitā accents as printed; Pada unaccented.)*`. The Pada-pāṭha stays unaccented.
5b. **Cross-check with the reviewer worklist** `publish/review/All_volumes_review_worklist.xlsx` (sheet "Worklist",
   Volume = "Vol 4", by "Original page"; 1,287 rows, reviewer columns empty as of Oct 27): apply any reviewer decisions;
   make sure every flag it lists for the batch's pages is resolved or in vol4_state.md's open list. Its page numbers come from
   an older build and can be off by a page or two.
6. Log each batch: write `vol4/review/notes_PDFA-B.txt` and run `pass_log.py A B NOTES` (log `vol4/vol4_pass_log.md`).
   Commit and push (`git push -u origin claude/numerals-vol4`).
7. Update `vol4_state.md` (last PDF page done, open readings, items to be reviewed), commit, push.

When the whole volume is done: rebuild the print PDF (`cd publish && python3 build_vol45.py 4 full`; needs
`pip install weasyprint pypandoc_binary` and `apt-get install fonts-lohit-deva fonts-noto-core`), check no dotted circles
(◌) in `pdftotext`, rebuild the DOCX (`pandoc` + `publish/tools/numeral_pass/docx_csfont.py … "Lohit Devanagari"`, see
`CLAUDE.md`), commit, and write "done" in `vol4_state.md`.

Never `git reset --hard`, never force-push, never touch other volumes.

## Extra steps to reduce `[?]` (learned Oct 28, 2026)
1. **Zoom every `[?]`, do not guess.** A `[?]` is usually a small-type number. Render the page at 450 dpi and crop only the numeral group
   (pad 60–400 px, upscale ×3–5.5). Page-width reads of small type are what produced most `[?]`. Helper scripts (they use `/tmp/v3num/` as
   work folder and the review JSONs for box positions; run from `vol3/tools/`):
   `zoom_strips.py PDF N` (page → N reading strips, 2400 px wide), `zoom_zs.py PDF STRIP x0 y0 x1 y1 OUT [zoom]` (crop by strip coordinates),
   `zoom_mont2.py PRINTED_PAGE...` (montage of every review box on a printed page; PDF = page + 14), `zoom_multi.py OUT ID[:padL:padR] ...`
   (stacked tight crops of chosen boxes; `S=5` env sets the scale), `zoom_zb.py ID OUT` (one box), `zoom_apply_batch.py BATCH.json`
   (exact, count-checked replacements `[[old, new, expected_count], ...]`; refuses mismatches).
2. **Work from the list.** Make a list of the open `[?]` (line, page, context) before starting; work page by page with one montage per page
   (`zoom_mont2.py`); apply each page's readings with `zoom_apply_batch.py` and commit every ~20 readings.
3. **Digit glyph rule that worked:** round-headed curled 2 = 2; Latin-"2" shape with flat foot = 7; hook top-left = 6; flat bar with a small curl
   above (as in the sūtra 6-1-9) = 9; ಲ-shape = 8; lobed ಣ-shape = 5; ಇ-shape = 3; ಳ-like = 4. Compare a doubtful digit with a clear one
   from the same page (e.g. a known sūtra) before deciding.
4. **Use series to cross-check:** the Kannada grammar's Uṇādi numbers are one continuous series (3-286, 3-290, 3-294 …); Pāṇini numbers follow
   the page's sequence; Nirukta and Ṛgveda lists are ordered. A reading that breaks the order is probably wrong.
5. **A wrong printed number stays "as printed"** with the standard number noted; do not "fix" it. Say which digit is doubtful and why
   (e.g. "2 or 7 undecided") instead of leaving a bare `[?]`; keep `[?]` only where the glyph really cannot be settled.
6. **The same sūtra recurs.** Search the file for the sūtra text before zooming: one clear reading settles the repeats (check each repeat's
   own print, but they usually agree). Make repeats consistent (`2-242` on pp. 57, 106, 253).
7. **Numbers split over a line end** (paribhāṣā numbers, p. 166): zoom both line fragments; record the joined number and the doubt.
8. **Words with `[?]`:** crop the word at ×4, read letter by letter, bracket only the unreadable conjunct; never complete from memory.
9. **After the batch:** regenerate the open list, update `vol4_state.md` counts, rebuild the DOCX (`pandoc … --toc --toc-depth=2`, then
   `publish/tools/numeral_pass/docx_csfont.py … "Lohit Devanagari"`) and check `unzip -p FILE.docx word/document.xml | grep -o '\[?\]' | wc -l`
   equals the `.md` count. The DOCX is only as clean as the `.md`: pages not yet reached still carry their old `[?]`.
10. **Count the right thing:** `[?]` = unreadable reading; `[accent ?]` = doubtful accent; ordinary `?` marks in English questions are not defects;
    placeholders like `4-32-[?]3` or `6-4-11?` count too. Report all four separately.
11. **Order of work:** do the open `[?]` of already-checked pages first (small, finishes a region), then move on page by page.

(The zoom helper scripts live in `vol3/tools/zoom_*.py`; copy them to `vol4/tools/` and change their review-JSON path and `WORK` folder to Vol 4 before use.)

**No OCR for any reading (user, Oct 28):** numbers and words come only from crops actually viewed; OCR text may at most help locate a line on a page.
