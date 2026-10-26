# Reading the small Kannada numerals — method comparison (Vol 11, Oct 2026)

Test set: 94 numeral groups cut from the better 600 dpi scan, PDF 25–90 (`docs/numeral_gold/`), chosen to contain the
hard digits; **gold = the user's reading of each crop** (92 answered, items 1–2 left blank). Scored on digits (separators ignored).

| Method | Right | Wrong | Left `[?]` | 3/5 | 6/7 | 2/9 | 8/9 |
|---|---|---|---|---|---|---|---|
| A. Current file text (page strips at 120–260 dpi, incl. the better-scan pass) — 68 of 92 located in the file | 43 (63%) | 7 | 18 | 33/51 | 24/38 | 33/47 | 17/28 |
| B. Tesseract `kan`, digits-only whitelist, crop at ~300 dpi, 3 scales voting | 83 (90%) | 9 | 0 | 63/68 | 50/56 | 57/63 | 33/38 |
| C. Glyph cutter + nearest-neighbour shape classifier (labels learnt from B's unanimous reads) | 78 (85%) | 14 | 0 | 57/68 | 51/56 | 54/63 | 33/38 |
| D. Eye reading of the isolated 600 dpi crops on a contact sheet | 91 (99%) | 0 | 1 | 67/68 | 56/56 | 62/63 | 37/38 |
| **B + C agree on the digits** (accepted without viewing) | 72 of 92, all right | 0 | — | | | | |
| D on the other 20 | 19 | 0 | 1 | | | | |

Per-pair columns count the gold items that contain either digit of the pair, read fully right.

## What the comparison shows
- The digit shapes are **not** ambiguous at 600 dpi: each of the ten classes is clean and distinct
  (`docs/numeral_gold/digit_classes.png`, 14 samples per digit). The old errors come from reading numerals inside
  whole-page strips at low resolution. File errors found: 3-36-6→**7**, 2-8-3→**7**-8-3, 1-22-21→1-2**3**-21,
  3-1-8→**8-3**-8, 5-4-3-12→5-4-3-1**7**, 5-53-10→5-5**6-9**, plus 18 numerals the file still flags `[?]` that read cleanly.
- B's errors are structural (`)` read as a trailing 2, lost hyphens) with one 6/7 confusion; C's are cutting errors
  (brackets, broken glyphs). They fail in different places, so **their agreement is a strong check: 72/72 right.**
- D is the most accurate single reader, but it is not infallible (item 1: eye 3-2-48, both machines 3-2-58 and the
  digit montage confirms 5); so D is used only where B and C disagree, and must agree with one of them.

## Recommended method (for PDF 73–140 and the doubtful pages)
1. `locate.py` (Tesseract word boxes) finds every numeral group on the page; crop each at 600 dpi.
2. B (`tess_digits.py`) and C (`glyphs.py`) read every crop. Digits equal → accepted (two independent confirmations).
3. The rest go on one contact sheet per batch of pages; read by eye (D). Accept when D agrees with B or C;
   otherwise zoom that crop once more; still split → keep `[?]` and log both candidates.
4. Match each read group to the Kannada file's page section by order (the Kannada text follows the print), and to
   the English section by value; edit both with `fx.py`; log with `pass_log.py`. Numbers the print has but the file lacks
   (e.g. PDF 60, ಪಾ. ಸೂ. ೬-೩-೨೬-೧) are added; numbers the file has but the print lacks are flagged for review.

Cost estimate: machines run locally (~3 s per numeral group, no tokens); about a quarter of the groups need the eye,
~100 tokens each on a contact sheet. With matching and editing, roughly 2–4k tokens per page, against 10–15k for strip reading.

Caveats: the gold items were found by Tesseract and have ≥ 3 digits; numerals Tesseract misses entirely, single
numbers and page headers are not yet tested. The separator (hyphen vs dot) is taken from B or the file, not from C.
