# Supplied numeral files (Vol 14)

`Rigveda_Clean_Numerals_14_1_350.xlsx` (user, Nov 2 2026; covers file pages 1–350): one sheet, columns **Page Number | Line Number | Extracted Pattern (Kannada digits) | Equivalent English Numbers | Raw Line Context** (the context is noisy OCR; the digits are the value). One row per numeric pattern found on a line (references, sūtra numbers, ranges, header numbers).

**Page mapping:** the file's page numbers = `printed + 18` throughout, i.e. = our PDF page up to PDF 222, and = our PDF page − 1 from PDF 224 on (the file has no duplicate of PDF 222, so its pages ≥ 223 correspond to our PDF page + 1). Our PDF 223 (duplicate) has no rows. Checked Nov 2: with this shift 798 of 871 numerals on already-translated pages (PDF 20–332) agree with the translation (digits-only match); without the shift most pages ≥ 225 disagree.

**How translators use it:** default value for each reference/sūtra/header numeral; verify against the strip; zoom only where they differ (see `../vol14_runbook.md`, last section). Known weaknesses of the file: dropped hyphens ("61-198" for 6-1-198), occasional digit misreads, ranges split, rows from page headers/noise; it does not list numerals it failed to find, so absence of a row is not a reason to omit a printed number.

`../review/numeral_file_disagreements_pdf1-332.tsv`: the 73 rows (49 pages) on already-translated pages where the file's digits do not occur among the translation's numerals on that page. In the one page checked (PDF 188) the file was right where the Opus-era reading said 1-116-1 / 1-116-20 (the page prints 1-117-1 / 1-117-20); another place there (10-39-6 vs 10-39-7) could not be settled at strip resolution. These 73 are the worklist for a correction pass (not yet done).
