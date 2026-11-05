# Vol 15

Maṇḍala 2 onwards (Vol 14 stops in Maṇḍala 2, Sūkta 15; the accent reference `refs/mandala/rv_mandala2.html` covers Maṇḍala 2 to its end, Sūkta 43; for Maṇḍala 3 add `refs/mandala/rv_mandala3.html`).
Workflow: `tools/rv/RUNBOOK.md` (dispatcher) and `tools/rv/TRANSLATOR_RULES.md` (translator). The base text is the machine-read HTML/markdown the user supplies; no page images are read.

| Path | What |
|---|---|
| `volcfg.json` | volume configuration: `source` (file@FIRST-LAST printed pages), `window` (3), output files, branch guard; edit `source` when the files are in `html/` |
| `html/` | the supplied HTML/markdown (strip embedded base64 images from markdown before committing) |
| `numerals/` | the user's numeral file(s), optional (cross-check only) |
| `scans/` | optional, spot checks only |
| `work/` | one directory per window (`wPPPP/`: kn.md, en.md, numerals.txt, pages.json, PROMPT.txt); ignored by git |
| `review/` | `doubts.tsv` (places left `[?]` at commit), `accent_report.tsv` |
| `parts/` | `batch_costs.md` (agent tokens/minutes per window) |
| `Rigveda_Samhita_Vol15_English_Translation.md` | English file; the last block is the single progress note ("Done through printed p. N") that holds the position |
| `Rigveda_Samhita_Vol15_Kannada_Text.md` | Kannada text, made by script from the supplied text and appended with the English file |

Start: put the supplied file(s) in `html/`, set `source` in `volcfg.json`, check the page split with `python3 tools/rv/html_pages.py FILE`, then `python3 tools/rv/batch.py prep 15` (branch `claude/vol15`).
