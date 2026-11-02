# Vol 14 — token-reduction plan (proposal, Nov 2 2026; nothing built yet)

Where tokens go now: (1) viewing page images, (2) zoom loops, (3) writing Devanagari for every Saṃhitā/Pada/bhāṣya line by letter-conversion from Kannada script, (4) numerals, (5) re-appending notes. Aim: Claude reads text, looks only at crops where machines disagree, and never converts scripts.

## Pipeline (user runs locally; Claude does only the judgement steps)
1. **Prep pages (script A):** render each PDF page at 300–400 dpi, deskew, binarise, split into text lines; save a crop per line + a JSON of line boxes.
2. **Two or more OCR engines per line (script B):** e.g. Tesseract (Kannada `kan`, plus `eng` for the printed-English lines) and a stronger engine the user has access to (Google Cloud Vision / Document AI, or similar). Output per line: each engine's text + confidence.
3. **Consensus (script C):** tokens on which engines agree → "green"; disagreements/low confidence → "red" with the crop path. Numerals: user's numeral files override; Kannada digits normalised.
4. **Scripted conversion (script D):** Kannada-script Sanskrit (Saṃhitā, Pada, bhāṣya) → Devanagari → IAST with `indic_transliteration` (already installed), so Claude never types those layers. Section headings (ಪದಪಾಠ, ಪ್ರತಿಪದಾರ್ಥ, ಭಾವಾರ್ಥ, ವಿಶೇಷವಿಷಯಗಳು …) detected by keyword → skeleton .md per page with `### Printed p. N` markers and per-Ṛk headings pre-filled.
5. **Printed English (script E):** Latin OCR lines inserted as-is, with a spell-check list of probable misprints for [sic]; Claude only confirms.
6. **Claude's part (per 6 pages):** receive the skeleton + Kannada text of Pratipadārtha/Bhāvārtha/Special Topics (text, not images) + only the red crops; translate prose; write one-line gists; fix red tokens; append. Estimated image views drop from ~all lines to the red ones.
7. **Scripted checks (script F):** IAST present on every Devanagari block; one progress note; no repeated chunk; numerals match numeral files.

## Open decisions (user)
- The standing rule "no OCR for readings" (Oct 28) would be relaxed to: *OCR text is accepted only where ≥2 engines agree AND the numeral/word passes script F; every other token is read from its crop.* Needs the user's explicit OK.
- Which second engine is available to the user.
- Calibration first: run A–C on 3 pages already translated by Opus; compare green-token accuracy with the existing readings before trusting it.
- Kannada text costs more tokens than English; measure on one batch whether text-in beats image-in.
