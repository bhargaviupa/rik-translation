# Vol 12 — state

Status: **not started.** Folder created Oct 30.

## Set-up checklist (do all before translating; test on 3 pages with known answers)
- [ ] Scan uploaded to `vol12/scans/` (resolution? ~600 dpi preferred); `tools/cfg.py` maps global PDF page → part + page.
- [ ] Page inventory script run: printed page + header on every scan page → map (printed = PDF − k), missing/duplicate/out-of-order pages listed here.
- [ ] Contents table read: Sūkta ranges, Ṛk counts, anuvāka/aṣṭaka/adhyāya/varga headers (dvaipada sūktas noted).
- [ ] Digit key calibrated on header/varga numerals and a few references (record glyph rules in the runbook).
- [ ] Tools tested: crop (whole-page fractions only), apply (unique-match asserts), lint, doubts builder, Kannada→Devanagari→IAST script.
- [ ] Model chosen by a test: same 5 pages (with known answers) by Sonnet and Opus, compared.
- [ ] Runbook agreed with the user.
