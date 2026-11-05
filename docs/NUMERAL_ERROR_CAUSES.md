# Why the numerals go wrong — causes found in the project's own notes (Nov 5 2026)

Sources read: `CLAUDE.md`, `docs/NUMERAL_READING_BRIEF.md`, `docs/NUMERAL_METHODS_REPORT.md`, `publish/tools/numeral_pass/METHOD.md`, `vol13/review/numeral_glyph_notes.md`, `publish/tools/ref_check/NUMERAL_FILE_LESSONS.md`, `vol7/numerals/README.md`, `vol14/vol14_runbook.md`, `docs/COORDINATION_NOTES_Oct2026.md`. Nothing was re-measured; the figures are the notes' own.

## The causes, strongest first

**1. The numerals are read at too low a resolution, from the wrong kind of image.**
Reference numerals (`ಪಾ. ಸೂ. ೬-೧-೧೬೩`) are about 2.5 mm tall and sit in small type inside parentheses. First-pass reading used whole-page strips at 120–260 dpi, and the viewer shrinks any image over ~2,000 px. Measured on 92 gold numerals (Vol 11): strip reading from the file text was right on **63 %**; the same numerals cut out at 600 dpi and read by eye were right on **99 %**. The notes conclude the digit shapes are *not* ambiguous at 600 dpi: "the old errors come from reading numerals inside whole-page strips at low resolution".

**2. Look-alike glyphs, and the key itself changed twice.**
Recurring confusions: 3/5, 6/7, 2/9, 8/9, 1/7 (faint foot), 0/9. The digit key (CLAUDE.md step 3) was first "flat-footed 2-like = 7, curled 2-like = 2", then corrected on Oct 31 to three look-alikes: round open-loop = 2, hooked ಇ/ಖ-like = **3** (most often misread as 2), flat-footed ಒ-like = 7. Everything read before the correction used the weaker key: Vols 1–10, Vol 14 pp. 2–55, and ~13 Nirukta refs in Vol 13 (`Ni. 2-9` that may be 3-9).

**3. Mis-aimed zooms.**
The viewer displays a strip smaller than its pixels (factor ~1.04–1.09). Coordinates read off the screen land on the neighbouring line; "several zooms landed on the wrong line before we found this". The model then reads a clear, confident number from the wrong place, which is worse than a `[?]`. Sonnet mis-aimed more than Opus in the Vol 14 pilot.

**4. Reading what is expected, not what is printed.**
Early drafts supplied sūtra numbers from memory; others "corrected" printed numbers that differ from the usual ones (Pā. 6-1-128 for 6-1-178, 8-4-3 for 8-3-106, 6-1-183 for 6-1-193). Many sūtras have no number printed at all, and the model fills one in. Plausibility cannot choose between two legible-looking readings, and it destroys real information when it overrides the print.

**5. Multi-part references multiply the error.**
A reference is 2–5 numbers joined by hyphens (`Ṛ. Saṃ. 10-162-3`, `Uṇ. 4-557`). Each digit has its own chance of a slip, and separators get lost or misread (`)` read as a trailing 2; hyphen versus dot; `7-4-79` collapsed to `7-479`). The model's mistakes then show up as wrong *part counts*, not just wrong digits.

**6. Touching, faint or clipped glyphs; overlap with accent marks.**
Feet clipped, ink faint, digits touching. Accent strokes overlap numerals in page headers and hide digits. Related typeface quirks cause word errors next to numerals: plain *ma*/*ya* printed with a hook that looks like the *u* sign; the compound mark in Pada lines read as *ya*.

**7. The workflow deliberately trades accuracy for tokens.**
CLAUDE.md asks for numerals "correctly the first time (no second pass)", viewing at ~120 dpi, "small-type numerals: `[?]`, no zooming" (grammar notes, Vol 11+), 3-page batches, and Sonnet translators (cost). Reading and zooming cost 10,000–15,000 tokens per page. The result is thousands of numeral `[?]` (Vol 11: ~1,400 English, ~1,700 Kannada) and, more importantly, **confident wrong values that carry no `[?]`**.

**8. Wrong values are often not flagged, so review never finds them.**
Vol 7: 495 numerals differed from the user's file and most had never been marked `[?]`; going only through `[?]` misses them. Conversely a `[?]` on an already-correct value stays forever (291 of 291 checked were correct and the flag was dropped). Confidence marking does not track correctness.

**9. The same reference is written in several places, and edits reach only some.**
A citation appears on the Devanagari line, its IAST twin and the English rendering. Passes changed one and left the others (Vol 7: 174 English-only occurrences had to be swept afterwards; a citation sometimes lives only on an italic line or a roman-numbered front-matter page the scripts skipped).

**10. Page and header bookkeeping.**
Offsets change inside a volume (Vol 14: −18, −19, −20, −22; duplicated and missing PDF pages; Vol 3 pp. 487 and 646 missing; Vol 7 p. 413, Vol 8 p. 323). A numeral then gets attached to the wrong page, and header numerals (Aṣṭaka, Adhyāya, Varga) are small and unreliable ("closing notes are more reliable for varga numbers").

**11. No ground truth for a long time, and the "truth" is also noisy.**
Methods were judged by feel until the gold set was built (Nov). The user's numeral file is machine OCR too: it loses or shifts separators, reads digits as 0, merges rows, reads the same sūtra two ways on adjacent pages. Where Pāṇini numbering can check it, some file values are wrong (`7-4-71` read `7-4-31`). "Always correct" is a working rule, not a measured fact.

**12. Mixed scan quality.**
Old scans are 300 dpi 1-bit (Vols 10, 12), others ~575–665 ppi; numeral pass on the 600 dpi scan only covered part of a volume (Vol 11: better scan covers PDF 1–140 of 714). A faint original cannot be fixed by zooming.

## What was shown to work

| Method (Vol 11 gold set, 92 numerals) | Right |
|---|---|
| A. Current file text (strips, 120–260 dpi) | 63 % |
| B. Tesseract `kan`, digits-only whitelist, 3 scales voting | 90 % |
| C. Glyph cutter + nearest-neighbour classifier | 85 % |
| **B and C agree** (no viewing) | **72 of 72 right** |
| D. Eye reading of isolated 600 dpi crops on a contact sheet | 99 % |

Also: the user's numeral file aligned by context + reading order + digits (Vol 7: 1,412 SAME after the passes); calibrating on the running header in the same crop; format validators (Pāṇini 1–8/1–4, Nirukta ≤ 14 …) as "does this exist" flags; a consistency table of "cited item → numbers read on each page".

## What follows for Vol 15 onwards (Sonnet, Claude Code)
1. **Take numerals out of the translator's visual job.** Before a batch, produce a numeral sheet for its pages: the user's file rows if supplied, plus a local digits-only reader (method B + C, no tokens) on 600 dpi crops. The translator uses the sheet; where B and C disagree, the batch lists the crop for a contact-sheet reading (D) or the user.
2. **Never read numerals from page strips.** If a numeral has no sheet entry, `[?]` — no guess, no memory, no "normal number".
3. **Use ≥ 600 dpi crops for the numeral reader**; keep strips for words.
4. **Flag by agreement, not by confidence:** a numeral with no second reader agreeing is flagged, whatever the model felt.
5. **`batch.py` checks:** digit validators (Pāṇini/Uṇādi/Nirukta/Ṛg ranges), part counts, header sequence (Aṣṭaka/Adhyāya/Varga never decrease), twin consistency (the same reference on the Devanagari line, IAST twin and English line must be equal), sūkta Ṛk counts against the front matter.
6. **Write each reference once.** Mark it in the chunk (e.g. `⟦ref:Pā. Sū. 6-1-163⟧`) and let the script expand it for the Devanagari, IAST and English layers, so twins cannot diverge.
7. **Fix the page map first** (offsets, duplicates, missing pages in `volcfg.json`) before any numeral is attached to a page.
8. **Keep a small gold set per volume** (user-verified ~50–100 numerals) to score each method before trusting it.

These are proposals; nothing is built. They fit the toolkit in `docs/TOOLING_REVIEW_Vol15.md`.
