# Vol 22 — status

*Update this file at the end of every working session.*

## Scope
Maṇḍala 7 (expected: from Sūkta 20; the running heads read `ಮಂ. ೭ … ಸೂ. ೨೦…`), Aṣṭaka 5, Adhyāyas 2–4(5), printed pp. 1–600 (PDF pp. 27–626). The Kannada preface (ಪೀಠಿಕೆ) stands before p. 1. The exact sūkta range is to be confirmed from the text.

## Source and inputs
The supplied text is the user's machine-read markdown (many OCR passes by different agents, merged and in part out of order), **re-ordered by page** by matching every text page to the scan PDF `Rig_Vol22.pdf` (626 pages; PDF page = printed + 26): `tools/rv/pdf_order/` (draft), result `vol22/html/rig_22_ordered.md` → `vol22/html/rig_22.md` (a `<!-- page P -->` marker before every printed page, `<!-- body -->` after the 21 front-matter pages; map of printed page → PDF page and source in `vol22/html/pages_map.tsv`).
- 473 pages: the user's machine transcription (best of the copies; accents present).
- **127 pages transcribed by Claude agents from the scan images** (verbatim rule, but low-resolution scans; **Vedic accent marks left out almost everywhere; 19 `[?]` on pp. 40, 156, 193, 219, 223, 267–269, 306, 416, 433, 467 (printed numbers = PDF − 26); many Sanskrit words are best readings; proofread against the scan needed**). Listed in `pages_map.tsv` (source = transcribed from scan). Details: `vol22/MISSING_PAGES.md`.
- `html_pages.py` now honours explicit `<!-- page N -->` markers on every page (≥ 50 markers): markers decide the pages; the printed head right after a marker is that page's head. 600 pages, printed 1–600, no gaps, no anomalies.
- Old intermediate files: `vol22/html/rig_22_merged.md` (merged by label; labels unreliable), `rig_22_ordered.md`.

## Outputs
`vol22/Rigveda_Samhita_Vol22_English_Translation.md`, `…_Kannada_Text.md` (empty so far), `vol22/work/`.

## How it was made
Agent route as Vols 19–21 (one Sonnet agent per batch of three windows; no API). Prepared Nov 25 2026 on branch `claude/hopeful-fermi-kypcts`.

## Status
Done through printed p. 0. Set-up complete; no window translated yet.

## Open items
1. User: the 127 transcribed pages need a proofread against the scan (accents, uncertain words).
2. Dispatcher: confirm sūkta range and the preface from the text before/while translating.
