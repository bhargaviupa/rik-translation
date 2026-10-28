# Vol 4 numeral + [?] + accent pass — state

Status: **not started** (structure created Oct 28, 2026). **Last PDF page done: none.** Next: settle the page map (the extra page near PDF 101–105, the 78 extra pages after PDF 623), then batch PDF 1–100.

## Reference
- **Better scan (user, Oct 28):** `scans/04 RigvedaSamhithaVolume04 1.pdf` … `7.pdf` = 701 PDF pages (part 1 has 101, the rest 100; plain git files, ~30 MB each), global PDF page = position in the 7 parts in order (`tools/cfg.py`). Latin-digit page numbers in the headers.
- **Page map (provisional, from `pnum.py` OCR of the header numbers, noisy):** printed = PDF − 14 for about PDF 1–101; printed = PDF − 15 from about PDF 105 on, so **one extra page (duplicate/inserted) lies between PDF 101 and 105: find it by eye and record it in `tools/pages.py` (`DUP`)**. Printed p. 608 (last page of the old scan) should be PDF 623. **PDF 624–701 (78 pages) are unexplained** (OCR sees no header numbers): look at them first with a contact sheet; they may be an index, blanks/duplicates or another volume's start. Check also for missing printed pages.
- Old scan: `../Rig_Vol4.pdf` (622 pages, printed = PDF − 14), the one the existing text was written from. Existing headings in the main file say "Page N (PDF M)" with the OLD scan's PDF numbers.
- Main file: `Rigveda_Samhita_Vol4_English_Translation.md` (repository root, ~2 MB, 246 `###` sections, ~1,300 lines with `[?]`). Its header says the preface (PDF 7–10 of the old scan) was deliberately not translated; the existing `.docx` covers only Sūktas 33–38 (rebuild at the end).
- Sūktas 33–46 (Ṛk counts per the file header): 33:15, 34:12, 35:11, 36:20, 37:15, 38:15, 39:10, 40:8, 41:9, 42:10, 43:9, 44:14, 45:10, 46:15.
- Tools in `tools/` are Vol 3's, retargeted (`cfg.py` = 7 scan parts; `zoom_*.py` = the zoom helpers, work folder `/tmp/v4num/`). Not persistent in a new session: `apt-get install tesseract-ocr tesseract-ocr-kan` (needed by `locate.py`, `pnum.py`).

## To do
Batches PDF 1–100, 101–200, 201–300, 301–400, 401–500, 501–622 — steps in `vol4_runbook.md`. End of volume: rebuild print PDF
(`python3 publish/build_vol45.py 4 full`), check no ◌, rebuild DOCX, write "done" here.

## Open readings
*(none yet)*

## To be reviewed
*(none yet)*
