# Vol 2 numeral + [?] pass — state

Status: in progress (scans present, 5 parts, 822 PDF pages).
**Last PDF page done: 200 (printed p. 186).** Next run starts at PDF 201.

Per-batch detail: `edits_PDF*.txt` (every numeral read, by box id), `notes_PDF*.txt` (what changed), and
`vol2/vol2_pass_log.md` (one entry per batch).

## Reference

Page map (checked from the page headers, PDF 1–822): printed = PDF − 14; printed pp. 224–225 are not in the scan
(PDF 237 = 223, PDF 238 = 226, so printed = PDF − 12 for PDF 238–289); PDF 290–291 repeat printed pp. 276–277;
PDF 292–822 printed = PDF − 14 (PDF 822 = p. 808, the last page). Front matter PDF 1–14 (contents PDF 9–13).

Tools: `vol2/tools/` (Vol 1 tools adapted) plus `montage.py` (crops with the file's reading,
60 per image), `zc.py`/`zoom.py` (450 dpi crops of boxes / full-width strips), `acc.py` (450 dpi page-fraction strip),
`ruler.py` (low-res page with a 0–100 ruler, to locate lines), `header_montage.py`, `samcrop.py` (Saṃhitā lines with
guide lines for svarita strokes / anudātta bars), `accent.py` (IAST acute from the marks), `sam.py` (replace a Ṛk's
Saṃhitā block), `addnote.py` (note on a printed page; handles "### Pages N–M" headings since Oct 27).

## Done

| Batch | Printed pp. | What was done |
|---|---|---|
| PDF 1–100 | front matter, 1–86 | all numeral boxes read and placed; references corrected (many Special-Topics lists were wrong, not only uncertain); quotations re-read; word [?] resolved where the print settles them; Saṃhitā accents Ṛks 3.1–3.12; note at Rk 3.5 (p. 38) rewritten (Saṃhitā accented, Pada unaccented); anuvāka table p. 2 read |
| PDF 101–200 | 87–186 | all 1593 boxes read and placed; references corrected / [?] resolved; grammar re-read and rewritten from the scan on pp. 155, 157, 158, 160, 162, 163, 165, 168–169, 171, 176, 178–179, 183–184, 186; bhāṣya garbles fixed pp. 158, 161, 171, 182, 186; page-header vargas read (pp. 89–109 = 7, 111–143 = 8, 145–173 = 9, 175– = 10); Saṃhitā accents Ṛks 4.1–4.10, 5.1–5.8; header notes pp. 87–186 now "Saṃhitā accents as printed; Pada unaccented." |

## To do

1. PDF 201–300 (printed 187–286): review page → read numerals → place → [?] → accents from Ṛk 5.9 on. Watch the page-map
   break at PDF 238 (printed pp. 224–225 missing) and the duplicate PDF 290–291 (skip in review).
2. PDF 301–400, 401–500, 501–600, 601–700, 701–822 — same steps.
3. Numeric [?] that had **no box on the review pages** (the locator missed them) and still need a manual look:
   p. 83 Ni. "2-23" [?] and "kvan" [?]; p. 84 Ṛ. Saṃ. "6-6[?]-1[?]"; p. 85 U. "4-196" [?]; p. 86 "Part II, page 3" [?]
   and "10th" [?] Ṛk; p. 91 U. "3-3[?]8"; p. 98 "6-2-102" [?]; p. 113 Ni. "2-1[?]"; p. 114 Ni. "3-8" [?] and Phiṭ
   "4-1[?]"; p. 119 "8-2-32" [?].
4. Remaining header notes of later pages that say "Accent-marks not reproduced; see the note at Rk 3.5" — change each
   as its Ṛk's Saṃhitā gets accents.
5. Regenerate `publish/review/All_volumes_review_worklist.xlsx` (`python3 publish/review_all.py`) after the Vol 2
   rebuild below — its Vol 2 rows are a snapshot of the old `publish/work/vol2_clean.md` and still list flags this pass
   has resolved. Optional tidy: the ~50 header notes on pp. 30–186 that say "[?] where unclear" show up there as flags
   though no reading is open on those pages.
6. End of volume: rebuild print PDF (`python3 publish/build_vol2.py full`), check no ◌ in `pdftotext`, commit
   `publish/out/vol2_full.pdf` and `publish/work/vol2_clean.md`, write "done" here.

## Cross-check with the reviewer worklist (`publish/review/All_volumes_review_worklist.xlsx`, Oct 27)

Its reviewer columns (reading / decision / comment) are empty for every volume — no outside decisions to import.
Vol 2 rows on printed pp. 1–186: 564. 260 of them could be matched word-for-word in the current file and are
resolved; 75 are still there (all are either the header-note conventions above or readings in the lists below); the
other 229 sit in passages this pass rewrote, so they cannot be matched by their text. For those, the current file
itself was scanned: every [?] still left on pp. 1–186 is listed below or under To do item 3, so none of the 229 is
open without being listed. The worklist added one reading the lists lacked (p. 112 "vocēyuḥ" [?], now listed). The worklist's page
numbers can be off by a page or two (e.g. its "pp. 168–169" Uṇādi "4-135" [?] is p. 214 in the file, next batch).

## Open readings (the print does not settle them; kept [?])

- p. 15 "पुरुभुजेममेधतुं [?]" (one letter); p. 31 one word in the Upaniṣad quotation; p. 33 "ibhrūtrūṇāṃ" [?] (Nirukta
  quotation); p. 34 "pāṇyaiḥ" [?]; p. 35 two verses printed without sense; p. 80 "bahulam uttarapadādiḥ" [?].
- p. 91 root list "ṛ-ṣap-śilp-…-parṣa" [?]; p. 106 Uṇādi list "…nvera-mālāḥ" [?]; p. 132 last word of the kampa verse
  "hito vitaḥ" [?]; p. 150 "prāg[?]-śarātrāt"; p. 155 "praṇetana" [?] (Mīmāṃsā quotation); p. 112 a stray syllable before "vocēyuḥ" [?] in the bhāṣya.
- Viṣṭuti names pp. 139/146: "pratiṣṭutiḥ / pariṣṭuti" [?], "sūrmī" (print ಸೂರ್ವಿ/ಸೂರ್ಮಿ) [?].
- Numbers: p. 133 U. "2-225" [?]; p. 164 "Ma. 3-1-3-7" [?] ("3-1-3-2" on p. 162); p. 166 "[?]-12-3" (first digit at a
  line-break); p. 168 "6-1-62" [?]; p. 184 "14-628" [?].
- Accents: [accent ?] on Ṛks 1.3 (p. 24), 3.5 (p. 38), 4.10 (p. 129) — a mark too faint to judge.

## To be reviewed by the user (changes beyond numerals, or judgement calls)

- Grammar paragraphs rewritten from the scan (list under Done, PDF 101–200): the earlier "characterized" text was
  replaced where it misstated the print; worth a read for style.
- p. 103: a "seventh varga is finished" line that is **not in the print** was removed (the 7th varga closes on p. 111).
- p. 177 Tai. Brā. 3-1-5: "jyaiṣṭhyai" corrected to the printed "jyeṣṭhāyai"; translation changed to "to Indra (and)
  Jyeṣṭhā".
- p. 147 pratyavarohiṇī table: strings add to 32 not 33 — confirmed as a source slip, left as printed.
- "[as printed]" kept where the print's number differs from the usual one, e.g. p. 91 Ṛ. Saṃ. "6-5-1" (verse "ā tvā
  rathaṃ yathotaye"), pp. 132/135 "7-1-102", p. 165 vs p. 168 Uṇādi numbering ("4-118" vs "4-5-58"); a clearer later
  printing was used to correct an earlier one where the text repeats (pp. 130/134, 152/157, 158/160).
- Batch 1 judgement calls: see `notes_PDF1-100.txt` and the PASS_LOG entry (anuvāka table, Maṇḍala list p. 3, p. 78
  "eight Ṛks" with seven references, "[as printed]" sūtra numbers pp. 18, 53, 63, 80).
