# Prompt to start the Vol 4 numeral / [?] / accent pass (paste into a new session)

```
Start the Vol 4 numeral/[?]/accent pass in bhargaviupa/rik-translation (Kannada Rigveda Saṃhitā commentary → English).

BRANCH: claude/numerals-vol4 (already has main merged, so the Vol 4 scans are in vol4/scans/). Check it out and pull first.
Never merge into main, open a PR, force-push or reset. Work only on Vol 4. Keep replies short.

READ FIRST, in this order (and nothing else big):
1. CLAUDE.md
2. vol4/START_PROMPT.md (this text) and vol4/vol4_state.md
3. vol4/vol4_runbook.md (it ends with "Extra steps to reduce [?]" — follow them)
4. vol3/vol3_runbook.md only if something in the Vol 4 runbook is unclear
5. head/grep of Rigveda_Samhita_Vol4_English_Translation.md (repo root; ~2 MB — NEVER cat it; use grep -n "^###" and sed -n ranges)

WHAT THE JOB IS
The Vol 4 English file (Sūktas 33–46, Third Adhyāya) was written from the OLD scan (../Rig_Vol4.pdf, 622 pages, printed = PDF − 14). The user supplied a BETTER 7-part scan (vol4/scans/04 RigvedaSamhithaVolume04 1..7.pdf, 701 pages). The job, as for Vol 3: against the better scan, (a) resolve numerals and [?], (b) fix translation/transcription mistakes, (c) write the printed Saṃhitā accents, (d) rewrite pages from the print where the old text is unchecked or compressed (bhāṣya in full, grammar pages rewritten with "### Page N" headings and printed sūtra numbers). The user's main complaint on Vol 3 was that too many [?] were left, so reducing [?] honestly is the point. Count what you settle.

STEP 0 — TEST THAT IMAGES DISPLAY
Before any batch, view one small crop and confirm you actually see an image. If any view returns "[media removed …]" or no image: STOP, tell the user, and do not write a number or word from that page. This rule was broken in Vol 3 on Oct 28 (about 100,000 tokens of readings from blank images had to be reverted). Check again after every few images, not only at the start.

STEP 1 — SETTLE THE PAGE MAP (cheap, do it first, then record it in vol4/tools/pages.py and vol4/vol4_state.md)
- Provisional (from OCR of header numbers): printed = PDF − 14 for PDF ≈ 1–101, printed = PDF − 15 from ≈ 105 on → ONE EXTRA PAGE (duplicate/inserted) between PDF 101 and 105. Find it by eye with a small header montage (tools/header_montage.py) → put it in DUP.
- Printed p. 608 (last page in the old scan) should be PDF 623. PDF 624–701 (78 pages) are UNEXPLAINED: look at them with ONE low-res contact sheet before anything else. They may be an index, blanks/duplicates or another volume.
- Check for missing printed pages (the old scan may have them: printed = PDF − 14 there). Note gaps in the text.
- OCR of the header page numbers is noisy; use majority per 50 pages and confirm by eye only at the break points.
- Front matter PDF 1–14: the Kannada preface (old-scan PDF 7–10) was deliberately not translated; leave it.

SETUP (a new container has none of this)
- apt-get update && apt-get install -y tesseract-ocr tesseract-ocr-kan   (locate.py, pnum.py need it)
- git lfs is NOT needed for these scans (plain git files).
- Work folder /tmp/v4num/ (tools/cfg.py). Run tools from vol4/tools/.
- Review pages per batch (numeral crops): locate.py A B → latin_filter.py A B → build_review.py A B vol4/review/review_PDFA-B.html; commit the .html/.json. Zoom helpers: tools/zoom_strips.py, zoom_zs.py, zoom_mont2.py, zoom_multi.py, zoom_zb.py, zoom_apply_batch.py (usage at the end of the runbook).

BATCHES (100 PDF pages each): PDF 1–100, 101–200, 201–300, 301–400, 401–500, 501–623 (+ whatever the 78 extra pages turn out to be). Start at PDF 15 (printed p. 1 per the old map; confirm), Sūkta 33, and go in order. Commit and push after each Ṛk (front matter: after each page batch). Close each batch: vol4/review/notes_PDFA-B.txt and edits_PDFA-B.txt, tools/pass_log.py A B NOTES, update vol4_state.md, build review pages for the next batch, commit, push.

NUMBER AND TEXT RULES (same as Vol 3)
- Read every number from the print with the digit key in CLAUDE.md. Glyph rule that worked: round-headed curled 2 = 2; flat-footed/open-top Latin-2 shape = 7; hook top-left = 6; flat bar with small curl on top = 9; ಲ-shape = 8; lobed ಣ-shape = 5; ಇ-shape = 3; ಳ-like = 4; ∩ = 1; ○ = 0. Compare a doubtful digit with a clear one on the same page before deciding.
- Zoom each doubtful digit once. A wrong printed number stays "as printed" (note the standard number). [?] only where the glyph really cannot be settled; say which digit is doubtful. Never fill a number or complete a Sanskrit word from memory. Never infer a number from a "series" or from the old text without seeing it.
- The accent mark goes after a visarga/anusvara; [accent ?] where doubtful. Sanskrit always in three layers (Devanagari + IAST + English). Printed English of each Ṛk reproduced with [sic]. Glosses I add are labelled "mine and tentative".
- Do NOT run add_iast.py on the whole main file. Run it on a copy of the new section and splice it in between the --- separators. A "*Gist:*" line or a bare ">" line right after a Devanagari block stops add_iast.py adding IAST; generate bhāṣya IAST yourself with deva_to_iast.
- Rewrite old unchecked text from the print: Saṃhitā with accents, Pada, bhāṣya in full incl. grammatical tail, Pratipadārtha, Bhāvārtha, printed English, Special Topics, grammar pages briefly with printed sūtra numbers.

TOKEN-SAVING RULES (learned the hard way; the user watches token use closely)
1. Never dump big output: no cat of the .md, no printing a whole json/OCR table (one careless print of 700 OCR rows cost thousands of tokens). Use head, tail, grep -c, sed -n A,Bp, python summaries that print counts.
2. Images are the main cost. View each page region once. Use 4 strips per page (tools/zoom_strips.py, 2400 px wide) for text, stacked tight crops (zoom_multi.py, S=4–6) for numerals; never full pages at 450 dpi unless asked. Grammar pages: read only the number/line you need.
3. Small-type numbers (Uṇādi, paribhāṣā, Nirukta, Ṛgveda lists) often have NO review box. Do not guess which box is which: build a one-line context list (line number, page, sūtra name) of the open [?] first, then locate each line on the page strip. Build a cheap locator (OCR the Kannada of a strip, search for the sūtra name) if it saves images.
4. Settle a page, then WRITE it (batch JSON of exact replacements [[old,new,expected_count],…], applied with zoom_apply_batch.py which refuses count mismatches). Never view a page twice. Save batch JSONs so a bad batch can be reversed.
5. The same sūtra recurs on many pages: one clear reading settles repeats (still check each print), and the numbers are one continuous series in the Kannada grammar (use only to cross-check, never to fill).
6. Work from the open-[?] list page by page; regenerate the list after each batch; report [?] / [accent ?] / placeholder "?" / ordinary question marks separately.
7. Do the already-checked pages' [?] before moving on; do not re-derive facts already in vol4_state.md.
8. Rebuild the DOCX only at batch close (pandoc … --toc --toc-depth=2, then publish/tools/numeral_pass/docx_csfont.py … "Lohit Devanagari"), and check its [?] count equals the .md count. The DOCX is only as clean as the .md; unreached pages keep their old [?].

HONESTY
Report settled vs not honestly, by Ṛk: zoom-checked / read at page width / [?]. Do not describe a number as settled unless you saw it in an image that displayed. If you notice you wrote something from a blank image, say so immediately and revert it.

Commit trailers:
Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>
Claude-Session: <the new session URL>

At the end, tell me how many numbers are settled and how many are not (zoom-checked / read at page width / [?]), by Ṛk, and what is next.
```
