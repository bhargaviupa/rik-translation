# Kannada OCR dataset & fine-tune for a 1949 Vedic-commentary typeface — requirements

This document is self-contained. It is meant to be pasted into (or read by) a fresh Claude Code session that has no memory of the earlier work. Read it fully before doing anything.

## 1. Purpose

Build a small, openly shareable **training/evaluation dataset** and a **fine-tuned OCR model** for the Kannada typeface used in a 1949 printed edition of the Rigveda Saṃhitā with Sāyaṇa's Sanskrit bhāṣya and H. P. Venkata Rao's Kannada explanation. Document the method so others working on old Kannada print (mixed Kannada + Sanskrit-in-Kannada-script) can reuse it.

Why: the general Tesseract `kan` model gives roughly 85–90% word accuracy on plain prose from this book and fails badly on: Pāṇini/Uṇādi/Nirukta/Ṛg reference numerals, the abbreviation `ಪಾ. ಸೂ.` (read as `ವಾ ಸೂ`), Sanskrit quotations, conjunct letters, page headers; English paragraphs on the same pages come out as Kannada-digit garbage. A fine-tune on this typeface should fix much of that.

Non-goals: writing a new OCR engine; recognising Vedic accent marks (underline = anudātta, stroke above = svarita — they are not Kannada characters and will be ignored/stripped); translation.

## 2. Existing assets (repo `bhargaviupa/rik-translation`, branch `main`)

- `Rigveda_Samhita_Vol11_Kannada_Text.md` — faithful Kannada transcription of Vol 11. Page markers look like `<!-- PDF 43 · printed 25 -->`. `[?]` marks doubtful readings. Sanskrit blockquotes (`> ...`) are Kannada-script *conversions* of Devanagari made by script, not transcribed from the page, and **may differ from the print** (e.g. sandhi, accents) — treat them as lower-trust.
- `Rigveda_Samhita_Vol11_English_Translation.md` — English file; not needed for OCR except page structure (`### Printed p. N  (PDF M)`).
- `docs/PASS_LOG.md` — log of the page-by-page verification pass against better scans; lists pages and what was corrected.
- `CLAUDE.md` — project conventions (read the digit key and the `[?]` rules).
- `publish/tools/` — helper scripts (transliteration, numeral pass, English OCR). `publish/tools/numeral_pass/METHOD.md` describes numeral reading.
- Scans: not in the repo working tree you will have. The user holds two high-quality 600 dpi scans: `11_Rigveda_Samhitha_Volume_11-1-70.pdf` (PDF pages 1–70 of Vol 11) and `11_Rigveda_Samhitha_Volume_11-71-140.pdf` (pages 71–140). **Ask the user to place them in a local `scans/` folder** (do not commit them — see §8). PDF page N ↔ printed page N−18. The repo also has `Rig_Vol11.pdf` (Git LFS, lower quality).
- **Verified ground truth pages**: Kannada text for PDF pages 25–73 of Vol 11 was re-checked against the better scan (bhāṣya, reference numerals, headers). Pages before PDF 24 were checked only partly. Use PDF 25–73 as the trusted set; consult `docs/PASS_LOG.md`. Lines still containing `[?]` must be excluded from training.
- Before touching anything, run `git log --oneline | head -40` to see what has changed.

## 3. Environment (user's machine: macOS)

- Tesseract with Kannada is installed (`tesseract --list-langs` shows `kan`), plus OCRmyPDF; installed via Homebrew (`brew install tesseract tesseract-lang ocrmypdf`).
- Needed additionally: Python 3, `poppler` (`pdftoppm`), Pillow, numpy, OpenCV (`opencv-python`), `python-Levenshtein` or `rapidfuzz`, and for training either **tesstrain** (git clone https://github.com/tesseract-ocr/tesstrain; needs `make`, `wget`, and Tesseract built with training tools: `brew install tesseract --HEAD` or `tesseract` training tools package) **or** Kraken (`pip install kraken`) as an alternative. Check which works first and tell the user the plan before installing anything large.
- Work in a new folder `kannada_ocr/` in the repo. Large generated files (images, models) go under `kannada_ocr/data/` and `kannada_ocr/models/` and must be git-ignored unless the user decides otherwise.

## 4. Deliverables

1. `kannada_ocr/README.md` — what this is, how to reproduce, results table, licence/rights statement (see §8).
2. `kannada_ocr/scripts/`
   - `render_pages.py` — render chosen PDF pages to grayscale PNG at 300 dpi (also keep 600 dpi originals referenced, not copied).
   - `segment_lines.py` — find text lines on a page (projection-profile or OpenCV contours), crop each to a PNG with a small margin, save a manifest `lines.tsv` (page, line_no, bbox, image path). Must handle: two-column-free single-column layout, centred headings, indented paragraphs, blockquoted verse lines, and the narrower English paragraphs.
   - `align.py` — pair each line image with its correct text (see §5).
   - `make_trainset.py` — write `.png` + `.gt.txt` pairs in tesstrain layout (`data/<model>-ground-truth/`), with a train/validation/test split **by page** (no page appears in two splits).
   - `evaluate.py` — compute character error rate (CER) and word error rate (WER) of any Tesseract/Kraken model against the test split, broken down by line type (prose / Sanskrit-in-Kannada / numerals-and-references / headings).
3. `kannada_ocr/data/` — line images, `.gt.txt`, `lines.tsv`, split lists (not committed by default).
4. `kannada_ocr/models/` — fine-tuned `.traineddata`.
5. `kannada_ocr/results.md` — CER/WER for: baseline `kan`, baseline `kan+eng`, fine-tuned model, on the held-out test pages, with the five worst pages and example errors.
6. `kannada_ocr/GUIDE.md` — short method guide for others: preparing ground truth, alignment pitfalls, digit confusions, how to evaluate.

## 5. Alignment requirements (the hard part)

Our Kannada text is stored as paragraphs, not printed lines. Tesseract line recognitions are approximate versions of the printed lines.

- For each verified page: run baseline OCR (`tesseract page.png out -l kan --psm 6 tsv` or hOCR) to get line boxes + rough text. Do **not** use OCR text as ground truth.
- Take the page's trusted text from the Kannada md (between that page's `<!--` marker and the next). Normalise: drop markdown (`**`, `*`, `>` blockquote markers, `---`), drop bracketed editor notes (`[...]`, "(grammar page; headwords)" etc. — anything that is not printed on the page), keep Kannada punctuation (`।`, `॥` appear only in Sanskrit lines).
- Align the page's OCR line sequence to the ground-truth character stream with a fuzzy sequence alignment (e.g. Needleman–Wunsch / rapidfuzz partial ratio on a sliding window), assigning to each image line the ground-truth substring that best matches, breaking at spaces. The ground truth must contain exactly the characters printed on that line, no more.
- Quality gate: for each aligned line compute similarity between OCR text and assigned ground truth; **flag and hold out** lines with similarity < 0.6 or any line whose assigned text contains `[?]`, Latin letters, or markdown residue. Produce `alignment_review.html` showing the image next to the assigned text for all flagged lines and for a random 5% sample of unflagged lines, so the user can check them by eye.
- Known pitfalls to handle explicitly: (a) hyphenated words split across lines (print ends a line with `-`); (b) the Kannada glyph for ಮ looks like "ಮು"; ṅ (ಙ) is drawn like ಜ; (c) bold run-in headwords followed by an em dash (`—`); (d) Sanskrit verse lines in Kannada script that I (the earlier assistant) generated from Devanagari may not match the print — compare and prefer the OCR-agreeing form only if the user confirms, otherwise exclude those lines; (e) page headers/footers, running titles and printed page numbers must either be excluded or kept as separate line type "header".

Line types to label in `lines.tsv`: `prose`, `sanskrit` (Kannada-script Sanskrit), `ref` (contains parenthesised reference numerals), `verse` (centred Saṃhitā/Pada lines — these carry Vedic accent marks; train them separately or exclude), `heading`, `english` (Latin script), `header`.

## 6. Training requirements

- Starting point: Tesseract `kan` best/tessdata_best LSTM model, fine-tuned (not trained from scratch). Document the exact `tessdata` source and version.
- Start with prose + sanskrit + ref lines only. Exclude `verse` lines with accents and `english` lines (handle English with the stock `eng` model in a separate pass; document using `-l kan+eng` or two passes).
- Hold out ≥ 15% of **pages** as test; never tune on test.
- Report CER/WER before and after. Target (not guaranteed): halve the baseline CER on prose, and reduce numeral/reference-line CER by at least 30%. If the fine-tune does not beat baseline, say so plainly and record why.
- Keep training reproducible: record command lines, random seeds, iteration counts, and model checksums in `results.md`.

## 7. Acceptance criteria

- All scripts run end-to-end from a clean checkout on macOS given the scans, with a single documented command sequence in the README.
- At least 20 verified pages (≈ 600–1,000 lines) are in the dataset with passing alignment-quality checks; the review HTML exists and the user has been asked to spot-check it.
- `results.md` contains a numeric before/after comparison on pages never seen in training.
- No scan images, no copyrighted page images, and no full-text copy of the 1949 commentary are committed to a public location without the user's explicit approval (§8).
- The guide states clearly what the model cannot do: Vedic accents, `[?]` readings, trusting numerals without checking.

## 8. Constraints and rules

- **Rights.** The 1949 Kannada commentary and the page scans may still be under copyright (author and rights holder uncertain). The user must decide what may be shared. Until told otherwise: keep images and text local; publish only code, the method guide, and aggregate results. Do not push line images or transcriptions to GitHub or any other public place on your own initiative.
- **Honesty about uncertainty.** Never complete garbled text from memory. Keep `[?]` out of training data rather than guessing.
- **Digit key (Kannada numerals in this print):** ೧ looks like "∩"; ೦ like "○"; the flat-footed "2"-like glyph is ೭ (7); the curled "2"-like glyph is ೨ (2); ೬ has a hook at top-left; ೮ looks like ಲ/ಅ; ೯ like ಕ; ೪ like ಳ; ೫ like ಣ; ೩ like ಇ. Common confusions: 3/5, 6/7, 2/9, 8/9. Reference numerals must be checked against the image, not trusted from OCR.
- Do not edit the volume md files in this task (they are the project's main outputs). Work only in `kannada_ocr/`.
- Commit small and often; branch `claude/kannada-ocr` (create it); do not push to `main`; no pull requests unless the user asks.
- Ask the user before installing large toolchains and before starting any multi-hour training run; give a time estimate first.

## 9. Suggested order of work

1. Read `CLAUDE.md`, `docs/PASS_LOG.md`, and this document. Confirm the scans are available locally; list the verified page range.
2. Pilot on **3 pages** (e.g. PDF 50, 56, 62): render, segment, baseline-OCR, align, produce the review HTML. Show the user the pilot before scaling up.
3. Scale to ≥ 20 pages; produce the split by page; run baseline evaluation (`kan`, `kan+eng`).
4. Fine-tune; evaluate on test pages; write `results.md`.
5. Write `README.md` and `GUIDE.md`; summarise open issues; stop and ask the user about publication.

## 10. Open questions for the user

- Who is the intended audience or hosting venue (a Kannada-language group, a university, an Indic-OCR project)?
- May line images (not full pages) be shared? May the text be?
- Preferred engine: Tesseract (simplest to reuse) or Kraken (easier to train, different format)?
- Is the user willing to spot-check ~100 aligned lines from the review page before training?
