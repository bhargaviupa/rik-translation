# Digit-glyph tool (prototype, Oct 2026)

`glyphs.py` renders nothing itself: give it 300-dpi grey PNGs of PDF pages
(`pdftoppm -r 300 -gray`), it finds free-standing hyphens (the "-" in 6-1-171),
cuts the digit components left/between/right of them, and saves 32x32 crops.

Experiment on Vol 9 (603 pages): clustering the crops (k-means) gives clean digit
clusters (arch = 1, ring = 0, curled 2, ಇ-like 3, ಳ-like 4, ಣ-like 5, hook 6,
flat-footed 7, ಲ 8, ಕ-like 9) that agree with the reader's digit key and with the
reader's Google-Docs OCR, so a classifier on these crops is feasible.

Status: NOT yet reliable end to end. On printed pp. 36-83, 44 reference numbers
decoded match the OCR exactly, 21 differ (mostly a dropped or extra digit), and
about 140 of the ~185 OCR numbers are not found at all: segmentation is the weak
point (hyphen touching a digit, digit split into pieces, "ಸೂ." picked up as a
digit). Needs: better segmentation (per-line projection, stricter hyphen test),
a reject class for letters, and a check against the OCR / my reading.
Use it as a second opinion, never as the only reading.

## Classifier attempt (Oct 2026, Vol 10) — `dc/`
- `dc/seed.py` cuts the reader's `Kannada_Numbers_0000_to_9999` sheets into 39,200 position-labelled digit glyphs.
- `dc/train.py` trains an SVM on augmented seed glyphs + self-labelled book glyphs + a junk class (10). The seed font transfers well: 0, 1, 3, 4, 5, 7, 9 are recognised confidently on Vol 10 book glyphs; 2, 6, 8 with lower confidence (visual gallery check). OCR-aligned weak labels (`dc/label.py`) were NOT usable (alignment mostly hit non-numeral hyphens).
- `dc/refs.py` finds and decodes hyphenated references per page (300 dpi). Visual check on 36 samples (PDF pp. 360–368): about half of real references decode fully correctly; typical failures are a dropped digit (hook-6, ಲ-8, a 2 after a 6), a missed hyphen, and false hits on Latin text ("English", "ation"). Comparison with the Google-Docs OCR (exact match 8 of 142 on PDF pp. 340–380) is not meaningful because the OCR itself drops digits.
- Verdict: NOT reliable end to end; do not use to overwrite readings. Next steps if continued: segmentation at 600 dpi, a digit-count/format validator (e.g. Pāṇini refs are a-b-c with a ≤ 8), and a human-checked test set of ~200 references to measure accuracy.
