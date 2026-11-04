# Using a user-supplied numeral file (xlsx) — lessons from Vol 7 (Nov 4 2026)

Read this before any numeral pass on a new volume. Scripts are in this folder; per-step results for Vol 7 are in `vol7/numerals/README.md`.

## The file
- Columns: Page | Line | Kannada digits | English digits | Raw line context (noisy Kannada OCR, "column E"). It lists **only references with separators** (4-5-2, 4.5.6); plain numbers (124, 34) are never in it. **Ask which file version is current and what the page offset is (Vol 7 newest file: file page = PDF page).** Keep every version in `volN/numerals/`.
- **The user treats the file as always correct** and said every row flagged DIFFERENT had the right value. It is still machine OCR: it sometimes loses/shifts separators (`7-4-79` → `7-479`, `79-4` for 7-9-4 — the user confirmed such values are right), reads digits as 0 (`2-00`, `0-08`) or merges rows. Never "fix" the file from memory; ask the user when a pairing looks like two different references.

## Mistakes to avoid (all happened in Vol 7)
1. **Only scanning Devanagari lines.** The md carries one reference on several lines: the Devanagari line, its italic IAST twin, English renderings. A citation can live **only on an italic `*…*` line** (Vol 7 p. v: Ṛ. Saṃ. 10-130-4) or on a plain English line (p. ii: "pages 221–231"). Scan **every non-table, non-heading line**, then **dedupe**: the same value within ~8 lines counts once.
2. **Page headings.** Front-matter headings are roman ("### Page ii (PDF 8)"); a regex `Page\s+(\d+)` silently skips them. Use `(\w+)`.
3. **Matching by page only.** The page-set pooling (exact, then nearest unused entry) is good enough for exact matches and one-digit slips but pairs doubtful numerals with unrelated leftovers at distance ≥ 3. Use **reading order** (monotone alignment of the file rows with the md numerals; `numeral_align_all.py`) plus column E context and the digit score.
4. **Running a replacement before checking its output.** Review a sample of the preview for impossible results (extra parts, zero parts, a list `119, 124, 125` paired with `10-113-2`) before `--apply`. First nearest-entry run produced `6-4-24` → `6-4-24-4` and `Ni. 2-17` → `8-0`.
5. **Applying only to Devanagari lines** leaves the IAST twin and English renderings with the old value. Apply to the same old value within ±8 lines, or sweep afterwards (`numeral_sweep_english.py`).
6. **Pairing across `[?]` only.** Many errors are NOT flagged `[?]`. Compare **every** md numeral with the file, irrespective of `[?]`, and report SAME / SAME-but-[?] / DIFFERENT / NOT FOUND.

## Recommended order for a new volume
1. `numeral_align_all.py --md MD --num XLSX --out volN/numerals/VolN_file_vs_md.xlsx` (report only; check pages 8/10-style spot rows the user names).
2. `numeral_drop_q_same.py`: drop `[?]` where the md equals the aligned file row (user checked 291 of 291 correct in Vol 7).
3. `numeral_apply_different.py … --parts-ok` for DIFFERENT rows (drop `--parts-ok` first to see the part-count-changing ones separately; ask the user). It skips edit distance ≥ 4 and plain lists — those are mis-pairings; list them for the user.
4. Remaining `[?]` and NOT FOUND rows: workbook (`unused_entries_xlsx.py`, `numeral_verify_certain.py`) for the user to mark (`C` = md correct, or the digits).
5. Log every step as TSV in `volN/numerals/`, commit after each, note results in that folder's README, user answers recorded as "User confirmed".

## Numbers from Vol 7 (for planning)
1,982 file rows; after the passes 1,035+ SAME, 495 DIFFERENT (all applied except 12 mis-pairings), 452 NOT FOUND (mostly Kannada-prose numerals not reproduced in the English md; not analysed). `rapidfuzz` and `indic_transliteration` are needed by `numeral_align_all.py` (`pip install rapidfuzz indic_transliteration`).
