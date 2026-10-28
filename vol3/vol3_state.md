# Vol 3 numeral + [?] + accent pass — state

Status: **in progress** (started Oct 27, 2026, after Vol 2 was done).
**Last PDF page done: 305** (printed p. 291); batches PDF 1–100, 101–200 logged; PDF 201–300 logged (`review/notes_PDF201-300.txt`); batch PDF 301–400 **in progress**: done PDF 301–305 as far as Ṛk 24.13's grammar (pp. 287–288 upper, written into the file) and Ṛk 24.14 *read* from the print (Saṃhitā accents, bhāṣya, grammar numerals) but **not yet written into the file** (old unchecked text for Ṛks 24.14–15 still stands from printed p. 288 on).
**Oct 28 zoom pass:** the grammar numerals on pp. 276, 278–284 and the open numerals of Ṛks 24.9–24.13 were zoom-checked and entered; then the 120 [?] of the checked part (to p. 288) were zoom-read: **23 [?] remain there** (`review/open_qmarks_up_to_p288.md`), mostly small-type Uṇādi numbers that stay unreadable, and a few word readings. The unreached part (printed p. 288–647) still has about 680 [?].
Counts: see the Oct 28 correction below.
Next: write Ṛk 24.14 (pp. 288–291) from the print, then Ṛk 24.15, close Sūkta 24, continue in order to PDF 400; then notes_PDF301-400.txt, pass_log, review pages for PDF 401–500.
Open numerals kept "as printed": Pā. 5-8-27 (p. 78), 6-1-167 (p. 145), 3-1-83 vs 3-1-53 (pp. 281/283), 8-8-41 (p. 108), Uṇ. 3-497 (p. 89), Uṇ. 4-12/4-452 and 4-227/4-662.

**Oct 28 correction:** readings entered while image views returned no image were **reverted to the old text** (with their `[?]`): the grammar numerals pp. 276–284 and the Ṛk 24.9–24.13 numerals (commit fbb6116, reverted), and every reading of the pp. 8–146 zoom pass (batches applied before images displayed again, reverted from the saved batch files). **Kept** (read from images that did display): the Ṛk 24.13 grammar pp. 287–288 (p. 287 sūtra numbers re-checked against the page), and the readings for pp. ~166–286 made after images were working again (paribhāṣā 7[6/9], Uṇ. 3-317 [p. 121 corrected], 3-312, 4-442, Nirukta 2-21/2-28/2-2[6/9], Ai. Brā. 7-18, 3-52-3 list, U. 4-528, Paribhā. 36/90, Uṇ. 1-135, 2-163, 1-7, 3-305, the root पत्ऌ, पथिन्यब्दस्य, तदेतत्…ऋक्कृतगाथं note). Even those should be spot-checked before merging to main. `[?]` count after the revert: 792 in the .md and the DOCX (was 803 at the start of the day; 706 before the revert was inflated by unverified edits).

**Redo of pp. 8–146 (Oct 28, with images displaying; every number below read from a crop I saw):** settled and entered: p. 8 Uṇ. 4-5-57; p. 12 page "75"; p. 19 paribhāṣā 95; p. 26 Uṇ. 2-251, 2-252; p. 30 Uṇ. 5-236; p. 31 Uṇ. 3-14 (printed ३. १४); p. 32 Ai. Brā. Bhā. 5-7; p. 33 pages 416–417, Uṇ. 3-294, 3-290, 3-286; p. 37 Uṇ. 3-323; p. 40 Uṇ. 4-491, 4-488; p. 41 paribhāṣā 58; p. 45 Ni. 7-8; p. 57 Uṇ. 2-2-42 and 4-4-97; p. 68 Uṇ. 2-159. Read but NOT settled (kept `[?]` with the glyph facts): p. 17 and p. 23 Uṇ. "1-1…54" (four glyphs after 1-1: ∩, 3-like, 5, 4; the two prints do not agree), p. 33 pages "432–433" (smudged). **Not yet redone** (the small-type numbers have no review box, so the line must be found on the page first): pp. 71, 77, 78, 80, 84, 86, 89–91, 93, 95, 98, 104–106, 108, 112, 114–116, 121, 144–146; they still carry their old `[?]`.

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

The scheduled task was deleted by the user (Oct 28); further work is run by hand in new sessions.
