# Vol 13 — state

Status: **set-up done (lean); translation not started — waiting for the user's go-ahead.** Branch `claude/vol13`.

## Facts established (all from viewed crops)
- Scan: 6 parts, 677 PDF pages, ~665 ppi 1-bit, in `scans/`. `tools/cfg.py` maps PDF page -> part+page. **No upside-down pages** (header strips PDF 22–677 and views of PDF 1–26 all upright); no gaps, duplicates or out-of-order pages.
- **Printed page = PDF − 20** for PDF 21–677 (PDF 21 = title page = printed 1; PDF 22 = printed 2; last PDF 677 = printed 657). PDF 654 (printed 634) has no printed number. Front matter: PDF 7–19 = roman i–xiii (Pīṭhike i–vi = PDF 7–12; contents vii–xiii = PDF 13–19; PDF 13 unnumbered but counted); PDF 20 = abbreviations; PDF 1–6 cover/title/plate. Map: `review/page_map_v13.json`.
- Content: Part 13, Second Aṣṭaka, **Fourth Adhyāya**, Maṇḍala 1 **Sūktas 166–183 (18 sūktas)** — title page "೧೬೬–೧೮೩" and the contents' last heading (ಎಂಭತ್ತ್ಮೂರನೆಯ) agree. Anuvāka 23 (heading block of 166–171 reads "ಅನುವಾಕ—೨೩"; later anuvāka numbers: read at each sūkta). Headers: even pages "ಮಂ. ೧ ಅ. ೨೩ ಸೂ. N", odd "ಅ. ೨ ಅ. ೪ ವ. N".
- Each sūkta opens with a heading block (ಸೂಕ್ತ—N, ಮಂಡಲ/ಅನುವಾಕ/ಅಷ್ಟಕ/ಅಧ್ಯಾಯ/ವರ್ಗ, **ಋಕ್ಸಂಖ್ಯೆ**, ಋಷಿ, ದೇವತಾ, ಛಂದಃ); read it when starting the sūkta.
- Sūkta topic start pages (printed, from the contents): 166:1 (heading block p. 3) · 167:73 · 168:113 · 169:146 · 170:176 · 171:192 · 172:226 · 173:236 · 174:313 · 175:361 · 176:397 · 177:427 · 178:446 · 179:468 · 180:496 · 181:551 · 182:591 · 183:624; last topic 652; text ends p. 657.
- Ṛk counts read so far (heading blocks/prose): 166: 15 · 167: 11 · 168: 10 · 169: 8 · 170: 5 · 171: 6 (heading "೬"); 172–183: read at the start of each sūkta. Dvaipada sūktas: none noted yet.
- Digit key: standard key of CLAUDE.md held on the headers/contents read (flat-footed 2-like = 7); zoom only a doubtful digit.

## Remaining checklist (lean — do only when needed)
- [x] scans, page map, offset, contents, title range, tools (`view.py` whole-page crops, `stack.py`, `numsheets.py`)
- [ ] translation, sūkta by sūkta (per runbook "Lean mode"); doubts zoomed only when in doubt
- [ ] user decision: model for drafting (Sonnet vs Opus) — no test run, to save cost
