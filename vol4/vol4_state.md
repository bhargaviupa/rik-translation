# Vol 4 numeral + [?] + accent pass — state

Status: **not started** (structure created Oct 28, 2026). **Last PDF page done: none.** Next: PDF 1–14 front matter / PDF 15 (p. 1).

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
*(none yet)*

## To be reviewed
*(none yet)*
