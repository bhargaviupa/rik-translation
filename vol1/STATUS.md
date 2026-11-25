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
Built (1,249–1,291 pp.) with `publish/build_vol1.py` + `publish/vol1_clean.py`; `vol1/review/vol1_full.pdf`. Front matter is the model for the other volumes (cover, title, credits, portraits, contents).

## Pointers
`vol1/README.md`, `vol1/vol1_state.md`, `vol1/vol1_runbook.md`, `vol1/vol1_handoff.md`, `vol1/vol1_qmarks_log.md`, `docs/HISTORY.md`.
