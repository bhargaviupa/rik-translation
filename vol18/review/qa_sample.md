# Vol 18 — QA sample (Nov 12 2026)

24 printed pages checked against the Kannada by three fresh Opus agents (read-only, not told what to expect): 12 general pages spread over the volume (g36 g106 g177 g247 g318 g388 g459 g530 g602 g675 g746 g816) and 12 pages with long Special Topics (s21 s48 s100 s137 s204 s368 s481 s576 s676 s736 s783 s807). Four groups: numbers/references, names/terms/quotations, negations/attribution, omissions/additions. Findings are the agents' own, **not all re-checked by me** except those marked "checked".

**Result: 4 ERROR, 30 MINOR on 24 pages; 8 pages clean.** The checklist (HANDBOOK §11.5) asks for a doubled sample when ERRORs are found: not done yet.

## ERRORs
| page | finding | status |
|---|---|---|
| g318 | the block under "Sāyaṇa-bhāṣya" is the Saṃhitā of the next Ṛk (Ṛk 3), the bhāṣya of Ṛk 2 is missing there | **checked, real; systematic**: in 6 windows the model counted the `[[bN]]` blocks one off, so Saṃhitā/Pada/bhāṣya text stands under the label of another section: w0162 (pp. 162–167), w0223 (223–228), w0316 (316–321), w0371 (371–376), w0445 (445–450), w0729 (729–734). The text is all there; labels and positions are wrong. Found by script afterwards (`convert.label_mismatches`), no earlier gate saw it. **Not repaired** (see STATUS). New gate in `batch.py check` now stops such a window. |
| g177 | Gist: "O Maruts, you are like the wind in speed, and you are birds" — the bhāṣya's vocative is the birds ("O you birds, like the Maruts in speed") | reported, not repaired |
| s736 | a quoted verse (Bṛ. De.) is cut to "… ādarāt ‖ **NOTE**" though the Kannada is readable except one word | reported, not repaired |
| s783 | Gist gives the son-role to the sacrificer instead of Agni ("you being the son…") | reported, not repaired |

## MINOR (by kind)
- Translator remarks left in the text (rule 2): s100 (Gist: "The explanation of द्यौः begins at the end of the block, which breaks off here."), s481 (bracketed "(printed सूक्तद …)").
- Silent normalisations of the supplied letters without NOTE (rule 2): g388 (अकारिषं), g746 (अनुक्थाः for अनुक्ताः), s48 (क for the garbled word), g530 / g459 (printed English "ast", "foud" without NOTE).
- Missing NOTE at garbled places: g675 (two places).
- Unnecessary NOTE: s48 (page break plus OCR slip).
- Wording: g602, g106, g459 (two), g530, s100 (two), s137, s204 (three), s676 (three), s783 (two).
- Script layer: s368 doubled daṇḍa after IAST; s676 broken bracket in the IAST of 1-112-7; s576 inline Sanskrit typed as plain IAST (no ⟦ ⟧); headings "विशेषविषयगळु" (Kannada word in Devanagari) on s676, s736, s783, s807; s807 Kannada pratipadārtha glosses run into the bhāṣya block shown as Sanskrit.
- g318: first Gist sentence is a fragment.

Files: `/tmp`-side page extracts were scratch only; the sample page numbers are above.
