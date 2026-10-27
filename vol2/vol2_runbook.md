# Vol 2 numeral + [?] pass — runbook for unattended sessions

Authorised by the user (Oct 2026): Vol 2 (`Rigveda_Samhita_Vol2_English_Translation.md`) is opened for
**numeral corrections, `[?]` resolution and correction of other errors found against the better scan**. Nothing
else in Vol 2 changes; no other volume is touched. Work on branch `claude/numerals-vol2` (create it from `main` if
missing); commit and push after every page batch; **merge into `main` only when the user says so**; no PRs.
No progress messages to the user. Each run is a fresh session: read this file and `vol2/vol2_state.md` first, continue from
where `vol2_state.md` says, update `vol2_state.md` before stopping.

## Inputs (all under `vol2/` since Oct 27; see `vol2/README.md`)
- Main file: `vol2/Rigveda_Samhita_Vol2_English_Translation.md` (and its `.docx`).
- Better scan parts in `vol2/scans/` (moved from `kannada/`; Git LFS — `git lfs pull` if a file is a small pointer), in page
  order: `02 Rigveda Samhitha Volume 02  1.pdf` (two spaces before `1`; global PDF 1–150), `… 2.pdf` (151–300),
  `… 3.pdf` (301–450), `… 4.pdf` (451–600), `… 5.pdf` (601–822). The older scan is `vol2/scans/Rig_Vol2.pdf`.
- Tools in `vol2/tools/` (run them from that folder; `cfg.py` holds the paths, `WORK=/tmp/v2num/`). Review pages, edits
  and notes go to `vol2/review/`; the batch log is `vol2/vol2_pass_log.md`.

## Steps (per run, in 100-PDF-page batches)
Run the tools from `vol2/tools/`; the file paths below are written from the repository root (from `vol2/tools/`,
`vol2/review/…` is `../review/…`).
1. **Review pages:** `locate.py A B` → `latin_filter.py A B` → `build_review.py A B vol2/review/review_PDFA-B.html`.
   Commit the .html/.json.
2. **Read the numerals yourself** (this replaces the user's review): for every box of the batch, read the crop
   (`crop.py ID OUT.png [above]`, or `view.py` page crops at 250–450 dpi for doubtful digits) and write
   `vol2/review/edits_PDFA-B.txt` (`ID: reading`, `?` for an unreadable digit). Page-header numerals
   (Aṣṭaka/Adhyāya/Varga) need no entry. Digit key: ೧ ∩; ೦ ○; ೭ flat-footed "2"; ೨ curled "2"; ೬ hook top-left;
   ೮ like ಲ; ೯ like ಕ; ೪ like ಳ; ೫ like ಣ; ೩ like ಇ. Usual confusions 3/5, 6/7, 2/9, 8/9, 2/7 — zoom every doubtful
   digit; check sūtra and verse sequences and printed totals.
3. **Place the numerals** in the Vol 2 file page by page (`pagework.py`, `secrep.py`, `apply.py`): fix wrong
   references, fill `[?]`/`.?` placeholders, hyphen form `2-1-14` (never `2.1.14`); `[as printed]` where the print
   differs from the usual number. Where the file only summarises, add a short italic note listing the printed
   references in order (`addnote.py`). Grammar pages stay summarised (note the references only).
4. **Resolve the other `[?]` and hedges** on the same pages (`qctx.py`, `hedge.py`): re-read the Sanskrit/Kannada from
   the scan; replace garbled Devanagari with the printed text and give IAST (`publish/tools/translit/add_iast.py`'s
   `deva_to_iast`); fix English renderings that the print shows to be misreadings. Never fill from memory; keep `[?]`
   where the print does not settle a reading. Glosses not in the source are "mine and tentative".
5. **Other errors:** while each page image is open, correct clear misreadings in the English next to what you checked
   (wrong counts, wrong names, wrong maṇḍala/sūkta numbers). Do not restyle or rewrite sound text.
5a. **Saṃhitā-pāṭha accents (user's requirement, Oct 2026):** every Ṛk's Saṃhitā-pāṭha block must carry the accents as
   printed. Only 4 of the 177 blocks have them now (Rk 3.1–3.2 style: `अ॒श्विना॒ यज्व॑रीरिषो …`). On each page that
   prints a Saṃhitā-pāṭha, read the accent marks from the scan (zoom 300–450 dpi) and rewrite the block: anudātta ॒
   below, svarita ॑ above, udātta unmarked, ꣳ etc. as printed; the mark goes **after** a visarga/anusvara (`भिः॑`).
   The IAST line follows the existing accented blocks (acute on the udātta syllable: *aśvínā yájvarīr iṣo*). Never
   accent from memory; where a mark cannot be read, leave that syllable unmarked and put `[accent ?]` after the line.
   Pada-pāṭha and quotations elsewhere stay as they are unless the print accents them. Check the DOCX/PDF build for
   dotted circles (◌) at the end of the volume.
5b. **Cross-check with the reviewer worklist** `publish/review/All_volumes_review_worklist.xlsx` (sheet "Worklist",
   Volume = "Vol 2", by "Original page"): if a reviewer has filled "Reviewer's reading" / "Decision", apply it; make sure
   every flag it lists for the batch's pages is either resolved or in vol2_state.md's open list. Its page numbers come from
   an older build and can be off by a page or two.
6. Log each batch: append notes to a notes file and run `pass_log.py A B NOTES` (log `vol2/vol2_pass_log.md`).
   Commit and push (`git push -u origin claude/numerals-vol2`).
7. Update `vol2_state.md` (last PDF page done, open flags), commit, push.

When the whole volume is done: rebuild the print PDF (`python3 publish/build_vol2.py full`; needs
`pip install weasyprint pypandoc` and `apt-get install fonts-lohit-deva fonts-noto-core`), check no dotted circles
(◌) in `pdftotext`, commit `publish/out/vol2_full.pdf` and `publish/work/vol2_clean.md`, and write "done" in `vol2_state.md`.

Never `git reset --hard`, never force-push, never touch Vols 1, 3–10.
