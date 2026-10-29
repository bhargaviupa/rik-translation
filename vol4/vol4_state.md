# Vol 4 numeral + [?] + accent pass — state

**Parallel pass (Oct 28–29):** from Ṛk 33.7 the volume was split between workers v4a (pp. 33–175), v4b (176–338), v4c (339–492) and v4d (493–608); all four branches were merged into main on Oct 29 at their pause points (v4a through Ṛk 34.9, v4b through 37.10, v4c through 40.7, v4d through 46.1). Resume points and open items: `vol4/parts/v4*_state.md`; plan and rules: `docs/parallel_pass/HANDOVER.md`. [?] count after the merge: 976.

**START HERE (Oct 28, 2026, session 2):** work in page order. **Done: Ṛk 33.1–33.6, i.e. better-scan PDF 1–47 (printed pp. 1–33) for numerals/[?]** (see "Settled" below). **Next: PDF 47 lower half (printed p. 33, Saṃhitā of Ṛk 33.7) onwards** — Ṛk 33.7 (pp. 33–36, 8 open [?]). **Saṃhitā accents (runbook 5a): done for Ṛk 33.1–33.6** (each mark read on a native-resolution crop: underline below a syllable = anudātta ॒, short vertical stroke above = svarita ॑; IAST acute only on an unmarked syllable directly before a svarita or directly after an anudātta). Flags: `[accent ?]` in Ṛk 33.1 (underline between *da* and *sya* of *dasya*) and Ṛk 33.2 (underline between *sa* and *ti* of *vasatiṃ*). Also corrected: Ṛk 33.5 Devanagari had an extra *va* in *vavṛjus*; the unaccented duplicate IAST lines under the Saṃhitā of 33.2–33.5 were removed. The Pada-pāṭha is also accented in the print but stays unaccented. **Next: accents for Ṛk 33.7 onward, together with each Ṛk's numerals.** Old-scan numbering in the `### Page N (PDF M)` headings (M = old scan) is still not rewritten.

**Page map (settled):** printed = PDF − 14 for PDF 15–101; **PDF 102 is a pixel-identical duplicate of PDF 101** (recorded in `tools/pages.py` `DUP`); printed = PDF − 15 from PDF 103 on (OCR majority, to be re-checked as the batch reaches it). I confirmed headers by eye at PDF 20–47: printed = PDF − 14 holds there (p. 33 = PDF 47). PDF 624–701 still unexplained (last batch).

**Image check:** images displayed all session (page headers read: 20, 21, 24–33 matched the map). No page was written from a blank image.

**Method used (differs from the runbook's review-HTML route):** I did not rebuild `review_PDF1-100.*` (the old obsolete ones were deleted); instead `tools/zoom_strips.py PDF 4` for text, then `tools/nat.py PDF OUT S x0 y0 x1 y1 …` (new: re-renders chosen strip regions at the scan's native 658 dpi, stacked) for every numeral group, and `tools/zoom_apply_batch.py` for exact replacements. `tools/mont.py`, `tools/qlist.py A B` (lists the [?] with context in file lines A–B) are also new. Tools now resolve paths from `cfg.py` (worktree-safe).

**Counts:** `[?]` 2,216 at start of the pass → see git log/`grep -o '\[?\]'` (2,134 at the end of this session); `[accent ?]` 2.

**Settled this session (numerals zoom-checked at 658 dpi unless stated):**
- Ṛk 33.1: Pā. 6-4-77 on p. 6 is printed **16-4-77** (clear ∩, hooked 6, 4, 7, 7) — kept "as printed".
- Ṛk 33.2 (pp. 7–11): *upetya* read (no [?]); Ni. 5-4; Pā. 3-2-74; **3-1-19 printed 3-2-19**; Pā. 6-1-186; Pā. 6-1-34; **3-1-97 printed 3-1-91**.
- Ṛk 33.3 (pp. 11–16): Pā. 3-3-93, 8-3-9, 2-4-73; Phiṭ-sūtras printed "Phi. Sū. 17" and "14"; no further [?] remain on those pages except small-print ones noted below.
- Ṛk 33.4 (pp. 16–22): Ai. Brā. 3-20; Pā. 2-4-43, 8-2-28, 8-2-63, 7-4-69; **Pā. 6-1-127 vārtika 2** (not 6-1-115) for *īṣākṣādiṣu*; Ṛ.Saṃ. 3-29-14 and 10-69-12 (zoomed on strips; not separately re-zoomed).
- Ṛk 33.5 (pp. 22–26): Pā. 7-1-20, **6-1-42 printed for *śi sarvanāmasthānam* (usual 1-1-42)**, 6-1-60, 6-1-70 not printed on p. 23 (so removed), **7-4-55 printed for *ur at* (usual 7-4-66)**, 7-3-84/1-1-5/1-2-5, 3-2-103, 6-2-2, Phi. Sū. 80, **8-2-18 printed (usual 8-2-15)**, 8-3-3, 7-3-78.
- Ṛk 33.6 (pp. 26–33): Ṛg 5-29-12 (*navagvāsaḥ sutasomāsa* citation, with the print's "idraṃ"), 9-10-84 (as printed), 10-62-6, 1-62-4, 3-39-5, 10-14-6, 4-51-4; Ath. Saṃ. **19-1-56; 18-3-20** (replaces 18-1-36; 19-2-30); Ni. **3-2** (replaces 2-2); Pā. 6-1-9, 1-2-10, 1-1-5, **7-2-1 as printed** (usual 7-2-10), 1-3-62, 3-2-124, 2-2-28, 6-2-1, 3-1-26, 1-4-55, 3-3-174, 6-4-40 (+ vārtika 6-4-40-2), **16-4-83 as printed**, **3-2-29 as printed** for *kvip ca* (usual 3-2-76), 3-2-26 (Kā.), 6-3-137, 7-2-44, 3-2-102, 7-2-15, 8-2-36, 6-2-49, 6-1-71, 7-3-86, **7-1-80 as printed** (usual 7-1-70).

**Not settled / open (Ṛk 33.1–33.6):**
- Ṛk 33.6, p. 32: the sūtra after *ūj ca gamādīnām* on the final-letter replacement: name unreadable, number 1-1-53 or 1-1-59 (3 vs 9) — one [?] left in the file.
- Ṛk 33.6, pp. 27–28 bhāṣya-tail: several small numbers (about 1-2-10, 2-2-10/7-2-10, 6-4-40, Kā. 3-2-…) zoomed once but not all settled; one [?] re-added there honestly.
- Ṛk 33.6 vārtika *anyeṣām api dṛśyate* printed 6-3-137 is as in the file; 6-3-82 for *vopasarjanasya* and 6-2-1 were only read at strip width (crops cut off).
- My glosses in Ṛk 33.6's Special Topics ([?] after "opens", "obtained", "swift ones", "*phaliga*", "brave") are word-meaning doubts of the translation, not numerals: left.
- Ṛk 33.3–33.5 other [?] outside the grammar notes (Pratipadārtha etc.) were not touched.

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
