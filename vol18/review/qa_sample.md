# Vol 18 — QA sample (Nov 12 2026)

24 printed pages checked against the Kannada by three fresh Opus agents (read-only, not told what to expect): 12 general pages spread over the volume (g36 g106 g177 g247 g318 g388 g459 g530 g602 g675 g746 g816) and 12 pages with long Special Topics (s21 s48 s100 s137 s204 s368 s481 s576 s676 s736 s783 s807). Four groups: numbers/references, names/terms/quotations, negations/attribution, omissions/additions. Findings are the agents' own, **not all re-checked by me** except those marked "checked".

**Result: 4 ERROR, 30 MINOR on 24 pages; 8 pages clean.** The checklist (HANDBOOK §11.5) asks for a doubled sample when ERRORs are found: not done yet.

## ERRORs
| page | finding | status |
|---|---|---|
| g318 | the block under "Sāyaṇa-bhāṣya" is the Saṃhitā of the next Ṛk (Ṛk 3), the bhāṣya of Ṛk 2 is missing there | **checked, real; systematic**: in 6 windows the model counted the `[[bN]]` blocks one off, so Saṃhitā/Pada/bhāṣya text stands under the label of another section: w0162 (pp. 162–167), w0223 (223–228), w0316 (316–321), w0371 (371–376), w0445 (445–450), w0729 (729–734). The text is all there; labels and positions are wrong. Found by script afterwards (`convert.label_mismatches`), no earlier gate saw it. **Not repaired** (see STATUS). New gate in `batch.py check` now stops such a window. |
| g177 | Gist: "O Maruts, you are like the wind in speed, and you are birds" — the bhāṣya's vocative is the birds ("O you birds, like the Maruts in speed") | **reworded + NOTE (Nov 12)**: the Kannada Pratipadārtha has "O Maruts", so not certainly an error; the editor decides |
| s736 | a quoted verse (Bṛ. De.) is cut to "… ādarāt ‖ **NOTE**" though the Kannada is readable except one word | **repaired (Nov 12)**: the full verse given, NOTE on the printed word |
| s783 | Gist gives the son-role to the sacrificer instead of Agni ("you being the son…") | **repaired (Nov 12)** |

## MINOR (by kind)
- Translator remarks left in the text (rule 2): s100 (Gist: "The explanation of द्यौः begins at the end of the block, which breaks off here."), s481 (bracketed "(printed सूक्तद …)").
- Silent normalisations of the supplied letters without NOTE (rule 2): g388 (अकारिषं), g746 (अनुक्थाः for अनुक्ताः), s48 (क for the garbled word), g530 / g459 (printed English "ast", "foud" without NOTE).
- Missing NOTE at garbled places: g675 (two places).
- Unnecessary NOTE: s48 (page break plus OCR slip).
- Wording: g602, g106, g459 (two), g530, s100 (two), s137, s204 (three), s676 (three), s783 (two).
- Script layer: s368 doubled daṇḍa after IAST; s676 broken bracket in the IAST of 1-112-7; s576 inline Sanskrit typed as plain IAST (no ⟦ ⟧); headings "विशेषविषयगळु" (Kannada word in Devanagari) on s676, s736, s783, s807; s807 Kannada pratipadārtha glosses run into the bhāṣya block shown as Sanskrit.
- g318: first Gist sentence is a fragment.

Files: `/tmp`-side page extracts were scratch only; the sample page numbers are above.

# Round 2 (Nov 12 2026, after the repairs)

30 pages by three fresh Opus agents, with a brief that also asked for structure checks (block under its own heading, Gist matches its block, no Kannada prose in a Sanskrit block): 12 new general pages (g30 g99 g168 g237 g305 g373 g441 g511 g580 g649 g719 g789), 12 new Special-Topics pages (s38 s86 s110 s155 s227 s421 s508 s630 s717 s752 s787 s815) and 6 pages of the repaired windows (r166 r224 r316 r320 r447 r734).

**Result: 8 ERROR, 47 MINOR on 30 pages.** On the 24 new pages: **2 ERROR** (s86 Gist "bring" for "reach"; g580 the nighāta rule stated backwards) and 31 MINOR; on the 6 repaired pages: 6 ERROR (r166: the two continuation blocks of Sūkta 26's introduction stood after the particulars instead of after their block; r734: one Kannada prose line shown as a Sanskrit block, the roles reversed in the Bṛhaddevatā story, "died" turned into "was sorrowful", the piśācī passage misread, the sāman passage misread) and 16 MINOR. All 8 ERRORs repaired the same day (`review/repair_log.md`); of the MINOR items the 13 translator remarks, the p. 30 garbled Pada label and a few wordings were repaired, the rest are listed below.
**The rule of the checklist (HANDBOOK §11.5: ERRORs found → double the sample) is met a second time (2 ERRORs on 24 new pages): a full second read of the volume is the user's decision** (see STATUS).

MINOR items not repaired (reviewed): "ಶಮೀಭಿಃ" instrumental p. 305 (Pratipadārtha fixed, Gist not); two comparisons run together in one Gist p. 441; "within his house" added p. 511; Special Topics heading at the head of a page where the print continues (pp. 511, 676); Gist set in quotation marks p. 227; six Pratipadārtha entries with IAST only p. 421; "Hymn" for "Sūkta" p. 166; "of the anuvāka" added p. 447; "also" added and "The Bṛhaddevatā account runs:" p. 168; "ಠಾಜ್ಞಾ" copied without NOTE p. 168; "hiteṣu" as "friendly" p. 717; missing second alternative p. 752 (NOTE missing); two Special-Topics lemmas with English only p. 717; Gist "are to come"/"joined you together" p. 316; the stray "। ऐ." inside a quotation p. 316; unreadable Devanagari "सूक्तदल्लिरुव ऋक्संख्यॆ" in the sūkta particulars blocks (the Kannada phrase "number of Ṛks in the sūkta", pages 30, 316 and about 25 other sūkta heads); the particulars block inside the bhāṣya block p. 789; the Kannada-word heading "विशेषविषयगळु" (every Special-Topics section; user's decision pending).
