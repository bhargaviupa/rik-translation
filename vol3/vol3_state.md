# Vol 3 numeral + [?] + accent pass — state

Status: **in progress** (started Oct 27, 2026, after Vol 2 was done).
**Last PDF page done: 100** (batch PDF 1–100 done and logged Oct 27). Batch PDF 101–200 in progress: done through PDF 109 upper, printed p. 95 upper, end of Ṛk 22.10; edits in `review/edits_PDF101-200.txt`. Next: PDF 109 (p. 95 lower, Ṛk 22.11). Open from batch 1–100: small-type Uṇādi/paribhāṣā numbers left [?]; Pāṇini numbers read with doubt (bahuvrīhau "6-1-7" p. 77, na lokāvyaya "2-6-69" p. 80, devāt tal "5-4-27" p. 78, aniṭ-kārikā "7-2-10" p. 71); a few Saṃhitā marks [accent ?] (Ṛks 21.5, 22.4, 22.5, 22.6).

Rendering note: `view.py` crops the right edge of these scans; use full-page renders (pdftoppm at ~230 dpi cut into five strips) for reading, and `acc.py` for zooms.

Per-batch detail will go to `review/edits_PDF*.txt` (every numeral read, by box id), `review/notes_PDF*.txt` (what changed),
and `vol3_pass_log.md` (one entry per batch).

## Reference

**Better scan** (`scans/03 Rigveda Samhitha Volume 03 1.pdf` … `7.pdf`, 100+100+100+100+100+80+80 = 660 PDF pages, uploaded by
the user Oct 27). Page map, from the page headers (Oct 27: every page's header number read by Tesseract — the printed numbers are Latin digits — 490 of the 646 text pages confirmed directly; the rest, mostly odd pages whose number was cut off, all lie between confirmed pages with the same offset, and the longest unconfirmed runs, PDF 17–23, 85–89, 471–475, 621–623, were checked by eye; the only breaks are the two missing pages and the duplicate below):
- PDF 1–14: front matter: cover (PDF 1), title pages, dedication, portraits, preface (Bhūmikā, signed 6-10-1949),
  abbreviations (PDF 10), contents *Viṣayānukramaṇike* (PDF 11–14). The old scan has the same front matter plus a second copy of
  the cover (its PDF 1–15).
- PDF 15 = printed p. 1 (the invocation page); **printed = PDF − 14 for PDF 15–500** (PDF 500 = p. 486).
- **Printed p. 487 is missing** from the better scan; read it from `scans/Rig_Vol3.pdf` PDF 502.
- **PDF 501 is a second copy of p. 488** (identical to PDF 502): skip it.
- **printed = PDF − 14 for PDF 502–659** (PDF 659 = p. 645).
- **Printed p. 646 is missing**; read it from `scans/Rig_Vol3.pdf` PDF 661.
- PDF 660 = p. 647, the last page (end of Sūkta 32 and of the Second Adhyāya).
`tools/pages.py` encodes this map (`DUP`, `MISSING`).

**Old scan** `scans/Rig_Vol3.pdf` (663 PDF pages): printed = PDF − 15; the file's existing text was written from it.

**File layout:** by Ṛk, headings `### Pages A–B — Sūkta N, Rik M`, with `*(p. N)*` markers. Sūkta 29 Ṛks 6–7 and Sūkta 30
(pp. 452–517) are the text redone from the page images, in place since Oct 27 (the unverified first version was removed).

Tools: `tools/` (copied from `vol2/tools/` on Oct 27; `cfg.py` = the seven parts, `WORK=/tmp/v3num/`; `pages.py` = the map above;
`sam.py` also finds the short `**Saṃhitā-pāṭha**` label of the redone Sūkta 29–30 text).

## Done

| Batch | Printed pp. | What was done |
|---|---|---|
| setup (Oct 27) | — | files moved into `vol3/`; paths fixed (`publish/build.py`, `publish/review_all.py`, `CLAUDE.md`); `.gitattributes` cut to the two files really in Git LFS (`Rig_Vol9.pdf`, `Rig_Vol11.pdf`; the other 17 rules named plain files and made git report them as modified); tools copied and set for the seven-part scan; page map checked; runbook written |

## To do

1. Batches PDF 1–100, 101–200, 201–300, 301–400, 401–500 (+ p. 487 from the old scan), 501–600 (skip PDF 501),
   601–660 (+ p. 646 from the old scan) — steps in `vol3_runbook.md`.
2. Saṃhitā accents for every Ṛk (none carry them yet; the blocks have notes such as "accent-marks printed; not reproduced").
3. Bhāṣya passages marked "compressed": re-transcribe from the print as the pages are reached.
   At p. 576 move the separate "Restored note" (*anāhitāgni*, end of the file) into Sūkta 31 Ṛk 15's Special Topics.
   The file header's contents table has wrong start pages for Sūktas 30–32 (actual 458, 517, 587): correct it in batch PDF 1–100.
4. Reviewer worklist `publish/review/All_volumes_review_worklist.xlsx`: 1,287 Vol 3 rows (reviewer columns empty, Oct 27);
   cross-check each batch's pages. Regenerate it (`python3 publish/review_all.py`) after the Vol 3 rebuild.
5. End of volume: rebuild the print PDF (`cd publish && python3 build.py 3 full`), check no ◌, rebuild the DOCX, write "done" here.

## Decided

- **Sūkta 29 Ṛks 6–7 and Sūkta 30 (user, Oct 27):** the unverified first version was removed and the redone text (formerly the
  "SUPERSEDING REDO" block at the end of the file) put in its place; the file's progress note says so.
- **`.gitattributes` (user, Oct 27):** cut to the two files really in Git LFS, on `main` and the Vol 2/Vol 3 branches.

## Open readings

*(none yet; numerals and words the print does not settle are listed here by printed page as the batches go.)*

## To be reviewed

*(none yet; "as printed" numbers and [sic] English kept from the print are listed here by printed page.)*
