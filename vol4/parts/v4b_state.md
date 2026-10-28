# v4b state (numeral/[?]/accent pass, Vol 4)
- **Range:** Sūktas 36–38 (file: from "## SŪKTA 36", printed p. 176, to the section before "## SŪKTA 39", p. 339). Branch `claude/numerals-vol4-b`.
- **Page map checked:** better-scan PDF 191 = printed 176, PDF 192 = 177, PDF 193 = 178 (printed = PDF − 15).
- **Done through:** Ṛk 36.11 (PDF 232, printed p. 217 upper part).
- **Next unit:** Ṛk 36.12 (pp. 217–220, PDF 232–235).
- **Tool:** `vol4/tools/zoom_v4b.py PDF OUT S x0 y0 x1 y1 …` (crops from the 450-dpi page render of `zoom_strips.py PDF 4`, displayed-strip coordinates; Z = scale).
- **Open items:** Ṛk 36.1 tail group "siddha[?]nveti" (p. 179); Uṇ. 1-23 headword "pṝbhidi" [?] (p. 181); Ṛk 36.2 Ni. ref for sahaḥ (p. 184) and Uṇ. 2-26 last digit (p. 185); Ṛk 36.3 Uṇ. 4-628 [?] (p. 188); Ṛk 36.4 Uṇ. 1-152/1-158 third digit (pp. 190–191); Ṛk 36.7 samindhate accent, Paribhā. 9[?] (p. 202); Ṛk 36.9 accents aruṣam, darśatam (p. 207); Ṛk 36.10 second-line accents, Pā. 3-3-174 middle digit (p. 214); Ṛk 36.11 dīdiyuḥ accent, Paribhā. 3[?] (p. 217).
- **Tool:** `vol4/tools/band_v4b.py PDF OUT S y0 y1 …` (full-width line bands cut in K pieces; my y estimates from the strip views run ~1 line high, so take generous bands).
- **Tool:** `vol4/tools/lines_v4b.py PDF N` (labelled line strips) and `lines_v4b.py PDF OUT a-b …` (crop runs; K, Z, GAP, PITCH env). Accent strokes above a line can fall outside a run: use zoom_v4b.py for Saṃhitā lines.
