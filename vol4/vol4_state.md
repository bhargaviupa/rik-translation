# Vol 4 numeral + [?] + accent pass — state

Status: **in progress** (Oct 28, 2026). **Last PDF page done: PDF 22 (printed p. 8), part of Ṛk 33.2.** Batch PDF 1–100 is **not closed**: Ṛk 33.1 is closed (its one open reading is the Pā. 6-4-77 reference); Ṛk 33.2 is partly done. `[?]` in the file: 2,216 at start → 2,191 now (25 cleared; each needed a page view and often a zoom). Review pages for PDF 1–100 are built (`vol4/review/review_PDF1-100.html/.json`, 627 numeral boxes, no edits file yet). Scan: `Rig_Vol4.pdf` at the repo root (the `vol4/scans/` placeholder is empty).

## Reference
- Scan: `Rig_Vol4.pdf` at the repository root, 622 PDF pages. **Printed = PDF − 14** (PDF 15 = p. 1 … PDF 622 = p. 608, last page, ends with the
  Sanskrit colophon and Kannada closing sentences). Offset checked only on PDF 16/20/24 so far; **check headers for missing or duplicate
  pages in batch 1** and record them in `tools/pages.py` (`DUP`, `MISSING`).
- Main file: `Rigveda_Samhita_Vol4_English_Translation.md` (repository root). Its header says the preface (PDF 7–10) was deliberately not
  translated, and the existing `.docx` covers only Sūktas 33–38 (rebuild at the end).
- Sūktas 33–46 (Ṛk counts per the file header): 33:15, 34:12, 35:11, 36:20, 37:15, 38:15, 39:10, 40:8, 41:9, 42:10, 43:9, 44:14, 45:10, 46:15.
- Tools in `tools/` are copies of Vol 3's, adjusted for paths (`cfg.py`, `pages.py`, log file name). `locate.py` needs `apt-get install tesseract-ocr-kan`.

## To do
Batches PDF 1–100, 101–200, 201–300, 301–400, 401–500, 501–622 — steps in `vol4_runbook.md`. End of volume: rebuild print PDF
(`python3 publish/build_vol45.py 4 full`), check no ◌, rebuild DOCX, write "done" here.

## Open readings
- PDF 19–20 (printed pp. 5–6), Ṛk 33.1: the printed number after *ṅidadupadeśāt*... no; the one left is the reference after *dhātu—* on p. 6 (cited as Pā. 6-4-77 in the file). At 300 dpi it reads as ∩, a 7/ट-like glyph, 4, then a pair that may be 22 or 77; not settled. Needs a better scan or a 450-dpi crop.
- PDF 22 (printed p. 8), Ṛk 33.2: "upetya [?] patāmi" (the print shows उपेत्य or उपेत्या; not settled); "Pā. 6-1-34 [?]" (the last digit of the ref is unclear: ೦ or ೪).
- Sūtra references the file cites as "Pā. 6-1-186" (Ṛk 33.1, 33.2, and p. 15 of 33.3): **6-1-186 is not printed on pp. 6–7**; the Ṛk 33.1 instance has been reworded to say so; the others are still to check.
- Ṛk 33.2 Ni. 5-4 [?] and Pā. 3-2-74 [?], 3-1-97 [?]: to check on pp. 8–10.
- Sūkta 46 opening words "eṣo uṣā [?]" (TOC, line 26) and its Ṛk references: later batch (PDF 501–622).

Working method (this run): `view.py` crops to the text block, so its fractions do **not** map to the page; for crops use full-page 300-dpi renders with fractions of the whole page. Tesseract digit reads are unreliable (e.g. it read ೬-೮ as ೯-೪). Zoom at 300 dpi is just enough for Pā. references of two or three digits; the doubtful ones need 450 dpi.

## To be reviewed
- Ṛk 33.1 Pā. 6-4-77 reference (above). The sūtra attributions in grammar notes from Ṛk 33.1 onwards are checked against the print only when a page is viewed; not all of them are.
- Batch 1 still has ~150 `[?]` in Ṛk 33.2–34.12 and the Ṛk 33 Vyākaraṇa pages; front matter PDF 1–14 untouched.
