# Vol 5 numeral + [?] + accent pass — runbook

Authorised by the user (Oct 2026): `Rigveda_Samhita_Vol5_English_Translation.md` (and its `.docx`) is opened for **numeral
corrections, `[?]` resolution, Saṃhitā accents, and correction of other errors found against the scan**. Nothing else in
Vol 5 changes; no other volume is touched. Method = the Vol 2 pass (`vol2/vol2_runbook.md`, `publish/tools/numeral_pass/METHOD.md`)
adapted to Vol 5's layout. Work on the branch the session is given; commit and push after every unit; merge into `main` only when
the user says so; no PRs. Each run is a fresh session: read this file and `vol5/vol5_state.md`, continue where the state says,
update the state before stopping.

## Inputs and differences from Vol 2
- Scan: `Rig_Vol5.pdf` at the repository root (724 PDF pp., Git LFS; `git lfs pull` if a small pointer). No "better scan" exists
  for Vol 5 (`vol5/scans/` is empty); the user may add one later — then point `V5SCAN`/`cfg.py` at it. **Printed page = PDF − 16**
  (Pariśiṣṭa: printed 531 = PDF 547). Even pages carry the header "Maṃ. 1 A. 9 Sū. N" (Anuvāka 9 = Sūktas 47–50, then 10, 11 …),
  odd pages "Aṣṭaka 1, Adhyāya 4, Varga N" (small Kannada numerals; the closing note "… vargavu mugidudu" is more reliable).
- The file is organised **per Ṛk** (`### Rik N.M (pp. a–b, PDF …)`), not per printed page (Vol 2 had `### Page N`). The unit of work
  is therefore one Ṛk section (or one sūkta introduction / closing block): view all its pages, then patch that section.
- No Tesseract in the cloud container: the review-box tools of Vol 2 (`locate.py`, `build_review.py`, `montage.py`) are not
  used. Numerals are read directly from page crops. Tools in `vol5/tools/` (run from the repo root): `view.py PDF OUT.png [DPI y0 y1 x0 x1]`
  (text-block crop, fractions allow a zoom strip: use 130 dpi for a whole page, 300–450 dpi for a doubtful strip), `apply.py BATCH.json`
  (exact-unique replacements `[[old,new],…]`, all-or-nothing; keeps exactly the same number of progress notes), `qctx.py A B [chars] [regex]`
  (every `[?]` / pattern with context in a line range), `pass_log.py LABEL NOTEFILE`.

## Steps per unit (a Ṛk section or sūkta intro/closing)
1. `grep -n '^### \|^## ' FILE` to find the unit; read its text; `qctx.py` lists its `[?]` and "as read".
2. View every page of the unit once (130 dpi), then zoom (300–450 dpi strips) on each doubtful numeral/letter. **Digit key**:
   ೧ ∩; ೦ ○; ೭ flat-footed "2"; ೨ curled "2"; ೬ hook top-left; ೮ like ಲ/ಅ; ೯ like ಕ; ೪ like ಳ; ೫ like ಣ; ೩ like ಇ.
   Usual confusions 3/5, 6/7, 2/9, 8/9, 2/7 — zoom every doubtful digit; sequences of sūtras/verses are a sanity check only.
   **Record what is printed**; if it differs from the standard number say "(as printed)". Many sūtra numbers are not printed at all
   in the grammar notes: then give none (never supply from memory). Reference form with hyphens: `Pā. 8-1-20`, `Ṛ. 1-116-13`, `Uṇ. 2-103`.
3. **Fix**: (a) fill/correct numerals and delete "as read [?]" when the print is now settled — keep `[?]` only where the print does
   not settle a digit/letter; (b) re-read garbled Sanskrit/Kannada words from the scan, give Devanagari + IAST (three layers:
   `publish/tools/translit/add_iast.py`), never fill from memory; (c) correct clear misreadings in the English (wrong counts, names,
   Ṛk/sūkta numbers, wrong page labels); do not restyle sound text; glosses not in the source are "mine and tentative";
   (d) Saṃhitā accents (below). Grammar pages stay summarised: note the references only.
4. Apply with `apply.py`, commit, push. Never `git checkout`/restore the file; never rewrite the progress note except at the end.
5. **Saṃhitā-pāṭha accents** (user's requirement): every Ṛk's Saṃhitā block carries the accents as printed — anudātta ॒ below, svarita ॑
   above, udātta unmarked; the mark goes **after** a visarga/anusvara (`भिः॑`, not `भि॑ः`). IAST line: acute on the udātta syllable
   (*aśvínā yájvarīr iṣo*). Read from a 300–450 dpi strip of the Saṃhitā lines; never accent from memory; where a mark cannot be read
   leave the syllable unmarked and put `[accent ?]` after the line. Pada-pāṭha and quotations stay unaccented unless the print accents them.
   Replace the "*accents not reproduced*" label with "*accents as printed*" once done.
6. Other pass items (from Vol 2): Special-Topics reference lists re-read and corrected; page-header vargas read; quotations re-read;
   `Ṛ. Saṃ.` etc. references checked; page labels "(p. N)" checked against the printed page numbers; Pariśiṣṭa small-digit references
   (printed pp. 531–708) read where legible.
7. Log per sūkta: write a notes file, `python3 vol5/tools/pass_log.py "Sūkta N" NOTES`; update `vol5/vol5_state.md`; commit, push.

At the end: rebuild `.docx` (`pandoc -f markdown-yaml_metadata_block FILE.md -o FILE.docx --toc --toc-depth=2`, then
`python3 publish/tools/numeral_pass/docx_csfont.py FILE.docx "Lohit Devanagari"`), check Devanagari counts and no ◌; the designed
print PDF (`python3 publish/build_vol45.py 5 full`) and the worklist (`python3 publish/review_all.py`) are rebuilt on request.
If an image view returns no image, STOP and report; never write that page.

**No OCR for any reading (user, Oct 28):** numbers and words come only from crops actually viewed; OCR text may at most help locate a line on a page.
