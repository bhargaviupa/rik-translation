# Vol 23 — page flags (Nov 24 2026)

Source: `vol23/html/rig_23.md` (770 pages for printed 1–856 by `tools/rv/html_pages.py`).

## Printed numbers with no page of their own (84)
7, 10, 11, 18, 20, 26, 36, 40, 48, 49, 64, 66, 68, 70, 71, 78, 79, 85, 87, 88, 89, 92, 93, 102, 106, 107, 110, 114, 120, 130, 138, 144, 150, 156, 172, 173, 174, 176, 177, 180, 183, 188, 202, 211, 212, 218, 229, 265, 266, 269, 278, 279, 282, 327, 380, 386, 394, 400, 403, 419, 423, 424, 431, 439, 510, 543, 548, 549, 578, 594, 634, 635, 640, 645, 646, 699, 712, 747, 791, 820, 830, 831, 843, 847

The text of such a page stands inside the page before it (the splitter found no running head, or the OCR read the head number differently from the sequence, so the offset rule gave another number: for 57 of these a head-like line with the number exists in the file, for example `20 ಸಾಯಣಭಾವ್ಯಸಹಿತಾ [ ಮಂ. ೭. ಆ ೫. ಸೂ. ೮೨`, `26 ಸಾಯಣಭಾಷ್ಯಸಹಿ ತಾ …`, `ಸಾರಥ್ಯಭಾಷ್ಯಸಹಿತಾ …`). Effect on the output: the English and Kannada files carry no page mark for these pages (the gates compare the two files, so they agree); the pages are not lost. To do: make `html_pages.py` recognise these head variants (shared tool, then a rebuild of the page marks, not a re-translation).

## Pages repaired by hand
- pp. 372–373: heads misread as 572/573 (source corrected, translated separately, inserted before p. 374).
- p. 843: no running head; `<!-- printed 843 -->` inserted in the Kannada file by hand.

## Windows that stopped at a gate
w0008, w0016, w0045, w0067, w0140, w0206, w0264, w0337, w0389, w0396, w0524, w0588, w0631, w0740, w0802, w0835, w0841 (details in `repair_log.md`).
