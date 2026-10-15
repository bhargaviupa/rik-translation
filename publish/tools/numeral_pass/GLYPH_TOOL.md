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
