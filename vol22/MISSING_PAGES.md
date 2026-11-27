# Vol 22 — page coverage (every text page matched to the source PDF; the 127 gaps then transcribed)

Updated 2026-11-25. Method: `Rig_Vol22.pdf` (626 pages; PDF page = printed page + 26) was OCR'd page by page (Tesseract, Kannada);
every transcribed page from all 20 uploads was matched to its PDF page by character-n-gram similarity (cosine, threshold 0.30),
so the OCR labels (`## Page N`), which were mixed up by different agents, are ignored. Result: `vol22/html/rig_22_ordered.md`
(one `## Page <printed>` block per printed page that has text; front matter as `## Page F<pdf page>`).
Scripts: `tools/rv/pdf_order/` (draft; paths inside point at the session scratch directory).

Printed pages 1–600 (PDF 27–626): **473 have text, 127 do not.**

| Missing printed pages | PDF pages (re-run OCR on these) | Count |
|---|---|---|
| 40–41 | 66–67 | 2 |
| 43–53 | 69–79 | 11 |
| 71 | 97 | 1 |
| 125 | 151 | 1 |
| 155–156 | 181–182 | 2 |
| 161 | 187 | 1 |
| 184–185 | 210–211 | 2 |
| 193–194 | 219–220 | 2 |
| 215–230 | 241–256 | 16 |
| 264 | 290 | 1 |
| 266–274 | 292–300 | 9 |
| 279–284 | 305–310 | 6 |
| 296–297 | 322–323 | 2 |
| 300–307 | 326–333 | 8 |
| 330 | 356 | 1 |
| 365–380 | 391–406 | 16 |
| 382–389 | 408–415 | 8 |
| 416 | 442 | 1 |
| 420–430 | 446–456 | 11 |
| 432–434 | 458–460 | 3 |
| 439 | 465 | 1 |
| 450 | 476 | 1 |
| 452–471 | 478–497 | 20 |
| 494 | 520 | 1 |

Caveats: a page counts as missing when no transcribed page reaches similarity 0.30 with it; a page whose scan is hard to OCR could be a false
"missing" (isolated single pages 71, 125, 161, 184–185, 193–194, 330, 416, 439, 494 are the likeliest). Front matter: PDF 1–5 have no text.
Which copy of a page is kept: the longest among those within 0.05 of the best similarity. Pages the user's labels placed wrongly are now in
their true place (e.g. labels 64–66 are printed 54–56).

## Update (2026-11-25, later): the 127 gaps have been transcribed

All 127 missing printed pages were transcribed by Claude agents from the PDF page images (files `vol22/html/transcribed/pdfN.md`, N = PDF page)
and inserted into `vol22/html/rig_22_ordered.md`, which now has all 600 printed pages (printed 1–600 = PDF 27–626).
Limits of these 127 pages (from the agents' own reports): Vedic accent marks were left out almost everywhere; 19 `[?]` marks on 13 pages
(66, 182, 219, 245, 249, 293, 294, 295, 332, 442, 459, 483, 493); many Sanskrit words and the running-head numbers are best readings without a mark;
pages 293–295 and 484–497 come from low-resolution scans; the agents of groups 5 and 7 flagged few doubts but said so. A proofread against the scan is needed
(PDF page = printed + 26). The other 473 pages are the earlier machine transcriptions, placed by matching to the PDF.
