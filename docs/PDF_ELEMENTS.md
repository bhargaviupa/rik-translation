# What each volume's files contain — basis for choosing the content of a PDF

*Made Nov 27 2026 by `python3 tools/rv/element_scan.py --matrix --en|--kn` (read-only; counts are lines that are headings or labels, digits normalised). Re-run it to refresh. Counts in the matrix include bracketed garbled-label notes in the Kannada files (Vol 29: 308 canonical `*ಪ್ರತಿಪದಾರ್ಥ*` labels = its 308 Ṛks, 101 more in `*[…]*` notes), so use `--vol N --kn --examples KEY` for exact counts.*

## Kannada Text files: uniform
- All 25 volumes that have a file carry the same canonical labels (`*ಸಂಹಿತಾಪಾಠಃ*`, `*ಪದಪಾಠಃ*`, `*ಸಾಯಣಭಾಷ್ಯಂ*`, `*ಪ್ರತಿಪದಾರ್ಥ*`, `*ಭಾವಾರ್ಥ*`, `*English Translation.*`, `*ವಿಶೇಷವಿಷಯಗಳು*`, `*ವ್ಯಾಕರಣಪ್ರಕ್ರಿಯಾ*`), `<!-- printed N -->` markers and `>` Sanskrit blocks. A section can be found by its label and ends at the next label.
- `## ಸೂಕ್ತ` / `#### ಋಕ್` headings exist only where `kn_headings.py` was run (Vols 11, 12, 15–18, 23, 24, 27–30). Not needed to find a section.
- Not uniform: Vol 22 (221 of 601 pages), Vols 4/22/25/26 gap marks, Vols 7–10 (no Kannada file) and 13 (empty file); Vol 28 came in with main and is complete (671 pages).

## English files: three generations
| Family | Volumes | Section headings | Per-Ṛk? |
|---|---|---|---|
| A, current | 11, 16–30 | `#### Ṛk N`, `##### ॥ संहितापाठः ॥ …`, `##### Gist of the bhāṣya`, `##### भावार्थ (Bhāvārtha)`, `##### English translation` (or `(H. H. Wilson)` in 16, 17; `Printed English` in 11, 18) | yes |
| B, bold labels | 10, 12, 14, 15 | `**॥ संहितापाठः ॥**`, `**Printed English translation**` | yes (10 has no printed English, no word meanings, no Bhāvārtha) |
| C, legacy | 1–9 | four dialects: `**॥ Saṃhitā-pāṭhaḥ ॥**`, `**Pada-pāṭha** *(p. N)*`, `### Rik N.N`, `### Page N (PDF N)` (Vols 6–9 are page-based, not per Ṛk) | 1–5 partly; 6–9 no |
Vol 13: file empty. Vols 22, 25: no English file.

Different spellings of one element across the English files: printed English 50, Sāyaṇa-bhāṣya 148, special topics 129, grammar 122, NOTE/GLOSS 165, running-head remarks 360.

## Consequences for "choose what goes into the PDF"
1. Kannada PDF: a profile can work now for every volume with a Kannada file (labels are uniform).
2. English PDF: a profile works for family A at once; B needs a label table; C (and the page-based Vols 6–9) needs a different segmenter or conversion first.
3. Rule 3 (output files append-only) means the English files of B and C are not to be rewritten by hand; either a reader with an alias table, or a logged script conversion (like `to_note_style.py`), decided by the user.

## The reader (made Nov 27 2026): choosing the content of a PDF
`publish/tools/elements.py` (alias table, one regex per element and language) is called by `publish/volbook.py`; the `.md` files are never changed.
- **Elements:** `samhita, pada, bhashya, gist, pratipada, bhavartha, printed_en, special, grammar, anuvada, particulars`.
- **Choose:** `python3 publish/volbook.py N [eng|kan] --without printed_en,grammar` (both PDFs), `--without kan:printed_en eng:gist` (per PDF), or per volume in `volN/pubcfg.json`: `"without": ["printed_en"]` or `{"kan": [...], "eng": [...], "both": [...]}`. Nothing is left out unless named.
- **Dry run on any file:** `python3 publish/tools/elements.py FILE.md --lang kn|en --without printed_en [--out X.md]` prints sections and lines removed per element.
- **Rules:** a section runs from its label to the next label or heading; page markers and the running head after them are kept (so `p. N` links and the contents survive); a remark `*[…]*` right before a label goes with it; the printed English also ends at the first line with Kannada/Devanagari letters (Vol 24 Kannada: 50 cases, each the next sūkta's introduction line, which would otherwise have been deleted with it).
- **Every run prints** sections/lines removed and a `LONG` line for each removed section over 150 lines: look at it before using the PDF.

### What was checked (Nov 27 2026)
- Sweep of every element over every volume's English and Kannada file (dry run). **Reliable** (sections ≈ Ṛk count, longest section under about 60 lines): `printed_en`, `samhita`, `pada`, `pratipada`, `bhavartha`, and `gist` in family A, in all volumes of families A and B and in the Kannada files; families A/B English `printed_en`: Vol 17 441 sections = 441 Ṛks, Vol 24 730 = 730, Vol 15 277 of 278.
- **Not to be trusted without looking:** `special` and `grammar` (long essays are real: Vol 29 Kannada pp. 574–659 is one Special Topics section of 2,810 lines, 86 pages, no Sanskrit block inside; but Vol 5 Kannada `grammar` is one section of 6,262 lines, and Vol 16 `grammar` 1,817, Vol 28 Kannada `bhashya` 703, Vol 15 `bhashya` 415/266: probably a missing label). `bhashya` in family B is long because the remarks between its blocks have no label.
- Legacy English (Vols 1–9) was swept as a dry run only; Vols 6–9 are page-based, so per-Ṛk counts there mean nothing yet.
- Builds (HTML stage, WeasyPrint is not installed here): Vol 17 Kannada and English, Vol 15 English, Vol 11: page marks equal the markers of the file, with and without `--without printed_en`. Vol 17 Kannada with it: 441 labels `English Translation.` → 0, long Latin runs 50 → 6 (other Latin text).
- **A defect found on the way, fixed in the shared builder:** `pandoc_html()` now puts a blank line before every heading. A `### Printed p. N` mark glued to the line above was swallowed by pandoc (Vol 17 Kannada PDF was missing pp. 7, 494, 531, 571, 811; now 1,001 of 1,001). Other volumes' PDFs built before this fix may be missing marks too: rebuild them.
- Not tested: a real PDF (WeasyPrint), Vols 23 and 30 (their front-matter and contents source files are missing: `vol30/html/rig_21.md`, `volN/frontmatter_en.json`).
