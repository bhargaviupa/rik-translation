# Vol 6 numeral + [?] + accent pass — runbook (DRAFT, to be agreed with the user)

Opens `Rigveda_Samhita_Vol6_English_Translation.md` (and later its `.docx/.pdf`) for **numeral corrections, `[?]` resolution, Saṃhitā accents, and correction of clear errors found against the scan**. Nothing else changes; no other volume is touched. Method = Vol 5 (`vol5/vol5_runbook.md`) + the short-session rules of `docs/parallel_pass/worker_prompt_template_v2.txt`. Branch: the one the session is given (`claude/pass2-vol6-*`); commit and push each unit; merge to `main` only when the user says; no PRs. Each run is a fresh short session: read CLAUDE.md, this file and `vol6/vol6_state.md`, continue where the state/part file says.

## Inputs
- **Scan:** the better scan in `vol6/scans/` (6 parts, 639 PDF pp.); `vol6/tools/cfg.py` maps a global PDF page to part + page. **Printed page = PDF − 19** (PDF 20 = p. 1, 21 = p. 2). Check the printed number on every crop; note missing/duplicate pages in the part file. Old scan `Rig_Vol6.pdf` (printed = PDF − 18) is a fallback (`V6OLD=1`).
- **File layout:** per printed page (`### Page N (PDF M)`), with `### Rik 62.1 (pp. 2–6)` overview headings. **The PDF numbers in the headings are the old scan's (= printed + 18); the better scan has printed + 19.** Always go by the printed number.
- Header: even pages "Maṃ. 1 A. 20 Sū. N" (Anuvāka 11 → 12 at Sūkta 65 … check), odd pages "Aṣṭaka 1, Adhyāya 5, Varga N". Sūktas 65–70 are *dvaipada* (Ṛks counted by printed units).

## What to look at (targeted viewing — images are the biggest cost)
1. Per unit (one sūkta, or ~30 printed pages) list from the file ONLY: lines with `[?]`, `[accent ?]`, bare `?` standing for an unread digit/letter (e.g. `1-?-?`), and the Saṃhitā verse line of every Ṛk (for accents). `python3 vol6/tools/qctx.py FIRSTLINE LASTLINE` lists the `[?]`s with context. Pages with none of these are not opened.
2. View crops of those lines once at ~120 dpi; zoom (300 dpi, 450 only if needed) on the doubtful digit/letter/accent only. Never view whole pages at high dpi; never re-view a page.
3. **No OCR for any reading** (Tesseract only to locate a line). If an image view returns no image: STOP, write nothing for that page, note it.
4. **Digit key:** ೧ ∩; ೦ ○; ೭ flat-footed "2"; ೨ curled "2"; ೬ hook top-left; ೮ like ಲ/ಅ; ೯ like ಕ; ೪ like ಳ; ೫ like ಣ; ೩ like ಇ; confusions 3/5, 6/7, 2/9, 8/9, 2/7. Record what is printed; `[?]` where doubtful; never fill from memory. Many sūtra numbers are not printed: give none.

## Fixes (local only — fix errors, do not rewrite)
- Fill/correct numerals; delete "as read" once settled; keep `[?]` only where the print does not settle it.
- Re-read garbled Sanskrit/Kannada words (three layers; `publish/tools/translit/add_iast.py`).
- Correct clear misreadings (counts, names, Ṛk/sūkta numbers, page labels).
- **Accents (required):** Saṃhitā-pāṭha of every Ṛk as printed — anudātta ॒ below, svarita ॑ above; the mark goes after a visarga/anusvara (`भिः॑`); IAST line acute on the udātta syllable; `[accent ?]` after the line where a mark cannot be read; Pada stays unaccented. 9 files labels "accents not reproduced" remain to be replaced by "accents as printed".
- Do not re-transcribe bhāṣya, re-translate, or rewrite Pratipadārtha/Bhāvārtha/Special Topics/grammar.
- Apply with `vol6/tools/apply.py BATCH.json` (exact-unique replacements, all-or-nothing). Never `git checkout`/restore the file; keep exactly one progress note.

## Pariśiṣṭa-style numeral lists / review pages
Vol 6 has no Pariśiṣṭa, but dense reference lists in Special Topics (and any block with many `?` numerals) can use the Vol 5 HTML-review method (`vol5/tools/build_review_v5.py`, `build_verify_v5.py`, `make_artifact_v5.py`, `apply_edits_v5.py`; copy and adapt to `vol6/tools/`): crops + boxes, the user corrects, edits applied by the coordinator. Decide per sūkta; ask the user.

## Workers and sessions
Short sessions (one sūkta or ~30 printed pages), one worker per part file `vol6/parts/w6X_state.md`, edits log `vol6/review/edits_w6X.txt` (lines `  p. N: OLD -> NEW`). Several workers in parallel on separate sūkta ranges and branches; coordinator merges with the no-work-lost check (all added lines present, headings unchanged, one progress note).

## Order (proposal)
Sūktas 62–64 (pp. 1–153) · 65–70 (pp. 154–281, *dvaipada*) · 71–74 (pp. 282–~440) · 75–80 (rest, to p. 620). Exact page starts to be filled in `vol6_state.md` from the file's headings.

## At the end
Rebuild `.docx` (`pandoc -f markdown-yaml_metadata_block FILE.md -o FILE.docx --toc --toc-depth=2` + `python3 publish/tools/numeral_pass/docx_csfont.py FILE.docx "Lohit Devanagari"`; no ◌; Devanagari counts match), designed PDF (`python3 publish/build_vol45.py 6 full`, cleaner `publish/vol67_clean.py`), worklist (`python3 publish/review_all.py`).
