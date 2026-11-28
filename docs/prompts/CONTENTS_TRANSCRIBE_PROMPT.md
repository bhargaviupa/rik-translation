# Prompt: the printed contents of ONE volume — Kannada transcription and English translation

*Nov 28 2026. One agent per volume. You work on volume N only and touch only `volN/contents_src/` (and `volN/contents_en.json`, made by the tool). **No git, no PDF builds, no other file** — the dispatcher does configs, builds and commits. Read `CLAUDE.md` rules 1, 2 and 4 first.*

## Inputs
- `volN/contents_src/contents_scan.pdf` — the user's scan of the printed contents (pages v–…; render it: `pdftoppm -r 150 -png volN/contents_src/contents_scan.pdf /tmp/cN` and view each page in two halves, cropped with PIL, so that single letters and digits can be read).
- The supplied machine-read text of the volume (`volN/html/*.md`, the file whose first lines hold the contents; find the heading `ವಿಷಯಾನುಕ್ರಮಣಿಕೆ`). Its contents are an OCR with letter and digit errors, sometimes with HTML tables (`python3 -c "import sys; sys.path.insert(0,'publish/tools/frontmatter'); import contents_parse as cp; ..."`, `cp.flatten_tables(lines)` flattens them). Volumes where the supplied text has no contents or a scrambled one (e.g. Vol 28: merged table cells, wrong digits): transcribe from the scan alone.
- **Worked example: Vol 4** — `vol4/contents_src/contents_kn.md`, `contents_en.tsv`, `NOTES.md`, and `vol4/contents_en.json`. Copy its form exactly.

## 1. `volN/contents_src/contents_kn.md` (Kannada)
One line per printed line: `text page` (page number last, separated by a space), headings as `## …`; a sūkta line `೩೩. incipit ಎಂಬ …ನೆಯ ಸೂಕ್ತವು—`; Kannada digits for sūkta numbers as printed. Build it from the supplied OCR and **compare every line with the scan**: every page number, every letter you can see; correct the OCR where the scan differs and list each correction (`old` → `new`, page) in `NOTES.md`. Rules:
- **A number printed wrongly stays as printed** (a misprint such as 882 for 682, 986 for 936, a 9 for an inverted 6): never correct it from the sequence; list it in `NOTES.md` ("printed X, expected Y: the user decides"). Do not guess a digit you cannot read: say so in `NOTES.md` with your best reading.
- Page signatures (`vi`, `vii`, `ಪುಟಸಂಖ್ಯೆ` column heads), ornaments and the printer's colophon are not entries: leave them out (note the colophon text in `NOTES.md`: it names the press).
- Last line: `<!-- end of contents -->` (not print; it ends the region for the parser).
- A page of the printed contents that is in the supplied text but not in the PDF: keep the supplied text for it, mark it "not compared with a scan" in `NOTES.md`.
- Check with the parser (must give: every entry a page, sūkta numbers in sequence = the volume's range, pages never going backwards except printed misprints you listed):
```python
import sys; sys.path.insert(0,'publish/tools/frontmatter'); import contents_parse as cp
L=open('volN/contents_src/contents_kn.md',encoding='utf8').read().split('\n'); b=cp.parse(L,'ವಿಷಯಾನುಕ್ರಮಣಿಕೆ','end of contents',{})
```
(print blocks, sūktas, items, items without a page, page range, backward steps; `x['src']` is the line number of `contents_kn.md`.) Also check the volume's Kannada Text file (`volN/Rigveda_Samhita_VolN_Kannada_Text.md`) for the words that are Sanskrit incipits: the body prints them as verse text.

## 2. `volN/contents_src/contents_en.tsv` (English)
One row per parsed block: `src<TAB>English` (src = line of `contents_kn.md`), a header line starting with `#` is allowed. `{S}` for a sūkta row (the tool writes "33. The thirty-third sūkta, beginning ⟦incipit⟧"). Style (as Vols 28–30 and 4): "Introduction to the sūkta.", "The application (viniyoga) of the sūkta.", "The seer, deity and metres.", "The subject of the seer X.", "Explanation of the meaning of the word ⟦ಶಬ್ದ⟧.", "Explanation of the meaning of the Ṛks, etc."; adhyāya lines "The Third Adhyāya of the First Aṣṭaka."; "Here ends the … Adhyāya …" for an end line. **Sanskrit words: never typed in Devanagari or IAST — write them in Kannada script inside `⟦ ⟧`, copied from the Kannada line of that row** (the build turns them into Devanagari + IAST; the tool refuses a ⟦word⟧ that does not occur in the line). Proper names in the English sentence are written in IAST as in Vol 28 (Kutsa, Bṛhaspati, Aśvin …). Do not translate what you cannot read: ask in `NOTES.md`.
Run: `python3 publish/tools/frontmatter/make_contents_en.py N --end 'end of contents'` — it must print `written volN/contents_en.json` and no `FAIL`.

## 3. `volN/contents_src/NOTES.md`
Scan: pages and what they cover; which printed pages the PDF lacks; corrections list; misprints kept as printed; readings you are unsure of; the press from the colophon if the scan or supplied text has it; anything the dispatcher must decide.

## Report (your final message, short)
Volume; pages in the scan; entries (blocks / sūktas / items); pages range; corrections made to the supplied text (count); misprints and doubts (each with line and page); what the scan does not cover; the tool's last output line. Say what was verified and how, and what was not.
