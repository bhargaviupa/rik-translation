# Vol 30 contents source (2026-11-28)
- `contents_scan.pdf`: the user's scan of the original contents (12 pages).
- `contents_kn.md`: the contents text, taken from the machine-read `vol30/html/rig_30.md` (lines 256-625) and compared page by page with the scan (all 12 pages looked at as images; entries and page numbers agree). Edits to the machine text: three sukta numbers lost by the OCR restored from the scan (123, 154, 165); a stray `## XX-` (page mark) dropped; the page number 593 joined to its line; the first heading and the Adhyaya headings marked `##`; start/end marker lines added for the parser.
- Not corrected: the ordinal word of Sukta 160 is printed/read as "ಅರವತ್ತೊಂದನೆಯ" (161st); the English uses the number. Incipit of Sukta 136 as read: "ಕೇಶ್ಯ ೧ ಗ್ನಿಂ" (stray numeral, as in the scan).
- `../contents.json` (parser output), `../contents_en.json` (English, one row per source line), `../frontmatter_en.json` (heading only).
- Printed pp. 243, 339, 941, 973 have no page mark in the English file: `contents_target_overrides` in `pubcfg.json` link those entries to the last mark before.
