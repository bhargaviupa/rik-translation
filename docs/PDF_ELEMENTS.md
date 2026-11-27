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
