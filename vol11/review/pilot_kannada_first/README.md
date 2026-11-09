# Pilot: Kannada-first bhāṣya transcription (Vol 11, Nov 5 2026)
3 pages with the most `[?]` per word in the existing Devanagari bhāṣya (PDF 171, 276, 435; 300 ppi scan `vol11/scans/Rig_Vol11.pdf`).
A separate Sonnet agent transcribed the Sanskrit bhāṣya blocks **in Kannada script** (blind: it did not see the existing text; no zooming); `publish/tools/translit/kannada_to_deva.py` converted to Devanagari; `comparison.txt` diffs it against the existing Devanagari (compared with `canon`, so anusvāra vs nasal+virama does not count).
Files: `pdfN_kn.txt` (Kannada-first), `existing_devanagari_N.txt`, `comparison.txt`.

| PDF | existing words / `[?]` | Kannada-first words / `[?]` | identical words |
|---|---|---|---|
| 171 | 61 / 12 | 54 / 2 | 27 |
| 276 | 69 / 11 | 60 / 1 | 35 |
| 435 | 83 / 13 (+ "largely illegible" note) | 125 / 6 | 31 |

Checked against the page image (300 dpi strips) by the coordinator: PDF 276 (all 14 differing spots readable: the Kannada-first reading matches the print everywhere I could read it; the existing text is wrong in about 8 places; two spots, `ಚ್ಛಾಂದಸೀ`/`ಸೇ` and `ತೈರ್ಹವಿಷಃ`, are marginal at this resolution) and PDF 435 (the Kannada-first text matches the print in the lines checked; the existing "illegible" note was not warranted, the page is legible at 300 ppi). PDF 171 not adjudicated.
Limits: 3 pages, 213 existing words, chosen as the worst pages by `[?]` density (improvement likely overstated for typical pages); single reading, no zoom; coordinator's check was by eye on 2 of 3 pages.

(Note, Nov 9 2026: the 300 ppi scan `vol11/scans/Rig_Vol11.pdf` named above has since been removed from the working tree and from git history; the user holds the originals. `publish/tools/translit/kannada_to_deva.py`, written for this pilot, is used by the Vol 15+ pipeline.)
