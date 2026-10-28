# Vol 4 numeral + [?] + accent pass — state

**START HERE: work in page order from the front.** Resume at the first unfinished page of Ṛk 33.2 (printed p. 8, old-scan PDF 22), after re-checking the unsettled readings of pp. 1–8 below on the BETTER scan. Do NOT begin with the end of the scan (PDF 621–701): the 78 unexplained pages are for the last batch only; the extra page near PDF 101–105 is handled when the batch reaches it.

Status: **in progress** (Oct 28, 2026). **Last PDF page done: PDF 22 (printed p. 8), part of Ṛk 33.2.** Batch PDF 1–100 is **not closed**: Ṛk 33.1 is closed (its one open reading is the Pā. 6-4-77 reference); Ṛk 33.2 is partly done. `[?]` in the file: 2,216 at start → 2,191 now (25 cleared; each needed a page view and often a zoom). Review pages for PDF 1–100 are built (`vol4/review/review_PDF1-100.html/.json`, 627 numeral boxes, no edits file yet). Scan: `Rig_Vol4.pdf` at the repo root (the `vol4/scans/` placeholder is empty).

**RE-BASE NOTE (Oct 28, later the same day):** the 22 PDF pages / printed pp. 1–8 recorded above were worked on the OLD scan (`../Rig_Vol4.pdf`) before the better scan arrived. Their results stand in the main file, but: (1) the PDF numbers in this file and in the file's `### Page N (PDF M)` headings are OLD-scan numbers; (2) `review/review_PDF1-100.*` was built from the old scan and its box coordinates are **obsolete for the better scan — rebuild the review pages from the better scan** (`tools/cfg.py` now points at it); (3) the better scan's page map still has to be settled (see Reference); (4) the readings marked "not settled" above (Pā. 6-4-77 on p. 6, "upetya", Pā. 6-1-34) are worth re-reading on the better scan first, and whatever was read from the old scan should be spot-checked there.

## Reference
- **Better scan (user, Oct 28):** `scans/04 RigvedaSamhithaVolume04 1.pdf` … `7.pdf` = 701 PDF pages (part 1 has 101, the rest 100; plain git files, ~30 MB each), global PDF page = position in the 7 parts in order (`tools/cfg.py`). Latin-digit page numbers in the headers.
- **Page map (provisional, from `pnum.py` OCR of the header numbers, noisy):** printed = PDF − 14 for about PDF 1–101; printed = PDF − 15 from about PDF 105 on, so **one extra page (duplicate/inserted) lies between PDF 101 and 105: deal with it only when the batch reaches PDF ~100 (check each page's header number against the map as you go) and record it in `tools/pages.py` (`DUP`)**. Printed p. 608 (last page of the old scan) should be PDF 623. **PDF 624–701 (78 pages) are unexplained** (OCR sees no header numbers): look at them first with a contact sheet; they may be an index, blanks/duplicates or another volume's start. Check also for missing printed pages.
- Old scan: `../Rig_Vol4.pdf` (622 pages, printed = PDF − 14), the one the existing text was written from. Existing headings in the main file say "Page N (PDF M)" with the OLD scan's PDF numbers.
- Main file: `Rigveda_Samhita_Vol4_English_Translation.md` (repository root, ~2 MB, 246 `###` sections, ~1,300 lines with `[?]`). Its header says the preface (PDF 7–10 of the old scan) was deliberately not translated; the existing `.docx` covers only Sūktas 33–38 (rebuild at the end).
- Sūktas 33–46 (Ṛk counts per the file header): 33:15, 34:12, 35:11, 36:20, 37:15, 38:15, 39:10, 40:8, 41:9, 42:10, 43:9, 44:14, 45:10, 46:15.
- Tools in `tools/` are Vol 3's, retargeted (`cfg.py` = 7 scan parts; `zoom_*.py` = the zoom helpers, work folder `/tmp/v4num/`). Not persistent in a new session: `apt-get install tesseract-ocr tesseract-ocr-kan` (needed by `locate.py`, `pnum.py`).

## To do
Batches PDF 1–100, 101–200, 201–300, 301–400, 401–500, 501–622 — steps in `vol4_runbook.md`. End of volume: rebuild print PDF
(`python3 publish/build_vol45.py 4 full`), check no ◌, rebuild DOCX, write "done" here.

## Open readings
- PDF 19–20 (printed pp. 5–6), Ṛk 33.1: the reference after *dhātu—* on p. 6 (cited as Pā. 6-4-77 in the file). At 300 dpi it reads as ∩, a 7/ट-like glyph, 4, then a pair that may be 22 or 77; not settled. Needs a better scan or a 450-dpi crop.
- PDF 22 (printed p. 8), Ṛk 33.2: "upetya [?] patāmi" (the print shows उपेत्य or उपेत्या; not settled); "Pā. 6-1-34 [?]" (the last digit of the ref is unclear: ೦ or ೪).
- Sūtra references the file cites as "Pā. 6-1-186" (Ṛk 33.1, 33.2, and p. 15 of 33.3): **6-1-186 is not printed on pp. 6–7**; the Ṛk 33.1 instance has been reworded to say so; the others are still to check.
- Ṛk 33.2 Ni. 5-4 [?] and Pā. 3-2-74 [?], 3-1-97 [?]: to check on pp. 8–10.
- Sūkta 46 opening words "eṣo uṣā [?]" (TOC, line 26) and its Ṛk references: later batch (PDF 501–622).

Working method (this run): `view.py` crops to the text block, so its fractions do **not** map to the page; for crops use full-page 300-dpi renders with fractions of the whole page. Tesseract digit reads are unreliable (e.g. it read ೬-೮ as ೯-೪). Zoom at 300 dpi is just enough for Pā. references of two or three digits; the doubtful ones need 450 dpi.

## To be reviewed
- Ṛk 33.1 Pā. 6-4-77 reference (above). The sūtra attributions in grammar notes from Ṛk 33.1 onwards are checked against the print only when a page is viewed; not all of them are.
- Batch 1 still has ~150 `[?]` in Ṛk 33.2–34.12 and the Ṛk 33 Vyākaraṇa pages; front matter PDF 1–14 untouched.
