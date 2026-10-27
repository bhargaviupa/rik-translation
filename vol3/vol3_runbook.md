# Vol 3 numeral + [?] + accent pass — runbook for unattended sessions

Authorised by the user (Oct 27, 2026): Vol 3 (`vol3/Rigveda_Samhita_Vol3_English_Translation.md`) is opened for the same
pass as Vol 2: **numeral corrections, `[?]` resolution, correction of other errors found against the better scan, and the
printed Saṃhitā accents**. Nothing else in Vol 3 changes; no other volume is touched (Vol 2 has its own branch and runbook).
Work on branch `claude/numerals-vol3` (create it from `main` if missing; merge `main` into it first); commit and push after
every page batch; **merge into `main` only when the user says so**; no PRs. No progress messages to the user. Each run is a
fresh session: read this file and `vol3/vol3_state.md` first, continue from where `vol3_state.md` says, update
`vol3_state.md` before stopping. The scheduled task starts Vol 3 only when `vol2/vol2_state.md` says "done".

## Inputs (all under `vol3/`; see `vol3/README.md`)
- Main file: `vol3/Rigveda_Samhita_Vol3_English_Translation.md` (and its `.docx`). It is organised by Ṛk: headings
  `### Pages A–B — Sūkta N, Rik M`, with `*(p. N)*` markers on the parts inside.
- **Sūkta 29 Ṛks 6–7 and all of Sūkta 30 (printed pp. 452–517):** the text under the headings from
  `### Pages 452–454 — Sūkta 29, Rik 6` up to the Sūkta 31 heading is **superseded** (written while page views failed;
  see `vol3/Session_Report_Vol3_Sukta29-32.md`). The text to correct for those pages is the **SUPERSEDING REDO** block
  near the end of the file (headings `### Sūkta 29 — Rik 6 (printed pp. 452–454)` … `### Sūkta 30 — Rik 22 … (printed
  pp. 515–517)`; its Saṃhitā label is `**Saṃhitā-pāṭha**`). Leave the superseded text as it is (removing it is the user's
  decision; listed in `vol3_state.md`). `tools/pages.py` already skips it and maps those pages to the REDO block.
- Better scan in `vol3/scans/`, seven parts in page order: `03 Rigveda Samhitha Volume 03 1.pdf` (global PDF 1–100),
  `… 2.pdf` (101–200), `… 3.pdf` (201–300), `… 4.pdf` (301–400), `… 5.pdf` (401–500), `… 6.pdf` (501–580),
  `… 7.pdf` (581–660). Plain git files (not LFS). The older scan is `vol3/scans/Rig_Vol3.pdf` (Git LFS — `git lfs pull` if it
  is a small pointer; 663 PDF pages, printed = PDF − 15 there).
- **Page map of the better scan** (from the page headers): printed = PDF − 14 (PDF 15 = p. 1, PDF 16 = p. 2 … PDF 500 =
  p. 486); **printed p. 487 is not in the scan**; PDF 501 is a second copy of p. 488 (= PDF 502), skip it; printed = PDF − 14
  for PDF 502–659 (PDF 659 = p. 645); **printed p. 646 is not in the scan**; PDF 660 = p. 647, the last page.
  Read pp. 487 and 646 from `scans/Rig_Vol3.pdf` (its PDF 502 and 661): `pdftoppm -f 502 -l 502 -r 300 -gray
  scans/Rig_Vol3.pdf /tmp/v3num/p487`. Front matter PDF 1–14 (contents PDF 11–14). See `vol3_state.md` for the full check.
- Tools in `vol3/tools/` (copied from `vol2/tools/`; run them from that folder; `cfg.py` holds the paths,
  `WORK=/tmp/v3num/`). Review pages, edits and notes go to `vol3/review/`; the batch log is `vol3/vol3_pass_log.md`.

## Steps (per run, in 100-PDF-page batches: PDF 1–100, 101–200, … 601–660)
Run the tools from `vol3/tools/`; the paths below are from the repository root.
1. **Review pages:** `locate.py A B` → `latin_filter.py A B` → `build_review.py A B vol3/review/review_PDFA-B.html`.
   Commit the .html/.json.
2. **Read the numerals yourself:** for every box of the batch, read the crop (`crop.py ID OUT.png [above]`, or `view.py`
   page crops at 250–450 dpi for doubtful digits) and write `vol3/review/edits_PDFA-B.txt` (`ID: reading`, `?` for an
   unreadable digit). Page-header numerals (Aṣṭaka/Adhyāya/Varga) need no entry. Digit key: ೧ ∩; ೦ ○; ೭ flat-footed "2";
   ೨ curled "2"; ೬ hook top-left; ೮ like ಲ; ೯ like ಕ; ೪ like ಳ; ೫ like ಣ; ೩ like ಇ. Usual confusions 3/5, 6/7, 2/9, 8/9,
   2/7 — zoom every doubtful digit; check sūtra and verse sequences and printed totals.
3. **Place the numerals** page by page (`pagework.py`, `secrep.py`, `apply.py`): fix wrong references, fill `[?]`/`.?`
   placeholders, hyphen form `2-1-14` (never `2.1.14`; Vol 3 often writes "P. 6-1-37" — keep the file's "P." / "Pā." style
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
   Volume = "Vol 3", by "Original page"; 1,287 rows, reviewer columns empty as of Oct 27): apply any reviewer decisions;
   make sure every flag it lists for the batch's pages is resolved or in vol3_state.md's open list. Its page numbers come from
   an older build and can be off by a page or two.
6. Log each batch: write `vol3/review/notes_PDFA-B.txt` and run `pass_log.py A B NOTES` (log `vol3/vol3_pass_log.md`).
   Commit and push (`git push -u origin claude/numerals-vol3`).
7. Update `vol3_state.md` (last PDF page done, open readings, items to be reviewed), commit, push.

When the whole volume is done: rebuild the print PDF (`cd publish && python3 build.py 3 full`; needs
`pip install weasyprint pypandoc_binary` and `apt-get install fonts-lohit-deva fonts-noto-core`), check no dotted circles
(◌) in `pdftotext`, rebuild the DOCX (`pandoc` + `publish/tools/numeral_pass/docx_csfont.py … "Lohit Devanagari"`, see
`CLAUDE.md`), commit, and write "done" in `vol3_state.md`.

Never `git reset --hard`, never force-push, never touch other volumes.
