# Vol 1 — status

*Moved out of the general CLAUDE.md on Nov 8 2026. Update this file (not CLAUDE.md) whenever the state of this volume changes.*

## Scope
Pūrva-pīṭhikā, Sāyaṇa's Bhāṣya-bhūmikā and Maṇḍala 1 Sūktas 1–2 (front matter and the introductory chapters of the commentary).

## Source and inputs
Scans in `vol1/scans/` (old scans; extra scans `Rig_Vol1(1).pdf`, `(2).pdf` were added by the user but are not in use). Printed-page offsets are in `vol1/vol1_runbook.md`.

## Re-check against the supplied text (started Nov 11 2026)
Inputs in `vol1/html/` (user, Nov 11 2026): `rig_1_1.md` (250 source pages: front matter + printed pp. 1–224; **one line `<!-- body -->` inserted before "ಪೂರ್ವಪೀಠಿಕೆ 1"** so the splitter ignores the series-list lines in the front matter), `rig_1_2.html` (349 source pages, pp. 225–573), `rig_1_3.md` (pp. 575–720; last two heads read 718, 720). The three files are of two kinds (md, html) so they are not merged into one file; `tools/rv/prose_kn.py` reads them as page specs (`html_pages.load_many`). Splitter fixes (`tools/rv/html_pages.py`): HTML even-page heads of 8–12 characters were not recognised; Vol 1 head words added to the md splitter; optional `<!-- body -->` marker.
Kannada from the supplied text: `kannada/Rigveda_Samhita_Vol1_Kannada_Text.md` (`tools/rv/prose_kn.py`: prose pages 1–605; `html_to_kn.py` Ṛk pass from p. 606). It replaces the scan-read pilot file (printed i–iii, 1–45; deleted Nov 11 2026 at the user's request; no Kannada-vs-Kannada comparison is needed). `kannada/…_Kannada_Review.md` (the pilot's list) is still there.

**Nov 18 2026:** the user uploaded the three files again (identical to those of Nov 11) and asked for `rig_1_2.html` to be converted to markdown: `vol1/html/rig_1_2.md` (`pandoc -f html-auto_identifiers -t markdown --wrap=preserve`) replaces it. The markdown keeps text the HTML reader dropped (the words read inside pictures, which stand in the pictures' alt text: verse blocks among them). Page split of the markdown: 343 pages, 225–572 (the HTML reader found 346: pp. 409, 473 and 573 have no head the markdown reader recognises and join the page before). `html_pages.pages_md` now takes the line after pandoc's `::: header` as a running head whatever its words (file 3: 142 pages found instead of 135). **The Kannada file in `vol1/kannada/` was made from the HTML form and is to be made again from the three markdown files.**

## Outputs
`vol1/Rigveda_Samhita_Vol1_English_Translation.md` (closed) plus `Rigveda_Samhita_Vol1_Gaps_English_Translation.md` (printed pp. 95–167, 191–205, 261–283 and 288–295, translated later and inserted by `publish/vol1_clean.py`); Kannada text in `vol1/kannada/`; docx/pdf in the folder.

## How it was made
Scan-based legacy workflow (`docs/LEGACY_SCAN_WORKFLOW.md`). Accents: citations only.

## Status
Translated and closed. Files are closed (do not edit) except agreed passes.

## Open items
Outside Vedic/Sanskrit expert review still wanted. ~59 best-effort/illegible places should become a 'known limitations' appendix. A few chapter headings carry unresolved bracketed numbers (check against the contents table). ~9,000 `[?]` readings in Vols 1–2 together. Only one source diagram (lineage chart, p. 48) was reproduced as an image.

## Publication (print PDF)
Built (1,249–1,291 pp.) with `publish/build_vol1.py` + `publish/vol1_clean.py`; `publish/out/vol1_full.pdf`. Front matter is the model for the other volumes (cover, title, credits, portraits, contents).

## Pointers
`vol1/README.md`, `vol1/vol1_state.md`, `vol1/vol1_runbook.md`, `vol1/vol1_handoff.md`, `vol1/vol1_qmarks_log.md`, `docs/HISTORY.md`.

## Second pass (Nov 24–25 2026) — state
Report: `review/second_pass/STATUS_REPORT.md` (made by `tools/rv/sp_report.py 1`); S0 sieve with the S3 before/after table: `review/second_pass/sieve.md`. S1: new Kannada book `Rigveda_Samhita_Vol1_Kannada_Text.md` from the three supplied files (720 page marks; the old file is `kannada/Rigveda_Samhita_Vol1_Kannada_Text_OLD_scan_html.md`). S2: **all 720 printed pages read** in 23 batches by Sonnet readers (pilot pp. 360–369); 1,812 findings, 1,548 applied (1,553 edits, none failed, each a line of `review/repair_log.md`), the rest kept (English kept, settled by rule: `review/second_pass/kn_misprints.tsv` 262 rows, `decided_by_default.tsv` 131 rows; `questions.tsv` empty by the user's decision of Nov 25). Method: numbers from the supplied Kannada (user, Nov 24); a number the print lacks is removed; Sanskrit lines of the English are derived data and were not hand-edited (pp. 1–180 and the pilot: Sanskrit edits were made with the first version of the gate before this rule; pp. 181–720 none); readers follow `tools/rv/SECOND_PASS_BRIEF.md`.
Open items (`review/second_pass/open.tsv`, 78 rows): pages absent in the supplied text (**p. 215 is a copy of p. 216**; p. 345; pp. 594–595; p. 716; pp. 54, 199, 409, 422, 428, 473, 573, 651 have no head of their own but their text is inside the page before); English sections missing for printed pp. 372–373 and 447 (not translated); Kannada numbers that look odd or contradict the Kannada's own totals, applied as printed (pp. 13, 14, 66, 67, 77, 100, 113, 114, 117, 121, 138, 139, 142, 150, 224, 239, 241, 271, 276, 277, 283, 291, 351, 380, 575–576); scholars' names changed to the Kannada forms on pp. 310–311 (look at them once with a scholar).
S4: `review/second_pass/ws_coverage.tsv` — Maṇḍala 1 Sūktas 1–2: 18 Ṛks, each with Saṃhitā, Pada and bhāṣya, none missing, none twice. The Bhāṣya-bhūmikā of the volume is in the Wikisource export M00: `review/second_pass/bhumika_map.md` (Vol 1 pp. 346–592 ↔ export pp. 89–137, by script). S5: `review/Vol1_pictures.pdf` (10 pictures; picture 3 is the king's portrait, binarised and poor: `review/uniform_files.md` lists what the uniform pages need from a scan PDF: guru portrait, thank-you page). Not part of this pass: the bhāṣya, `[?]`→NOTE, R7, PDFs.
