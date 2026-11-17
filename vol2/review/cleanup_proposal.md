# Vol 2 clean-up — Step A1 proposal (Nov 17 2026)

Nothing in the text has been changed. Counts are my own, taken by script from `Rigveda_Samhita_Vol2_English_Translation.md` (17,942 lines; page = last `### Page N` heading above).

| Kind | Count | Examples (page, line) | Proposed action |
|---|---|---|---|
| `[?]` in all | **432** | — | — |
| … in a sentence of ours about the marks ("marked [?] where unsure") | 44 (your estimate 66) | p. 37 L855, p. 39 L945, p. 66 L1656 | the whole sentence (usually the whole `*( … )*` note) goes |
| … after a number/reference | 25 on lines without Devanagari (your estimate ~259) | p. 83 L2113 "Nirukta 2-23 [?]", p. 86 L2170, p. 202 L4695 | mark goes, number stays |
| … on lines with Devanagari | 237 | p. 15 L381 (verse), p. 33 L739, p. 80 L2038 | mark goes, reading stays. Includes references after numbers inside Sanskrit lines (the 259 above overlap with this group) |
| … in IAST-only lines (twin of the Devanagari line) | 57 | p. 15 L382 | mark goes with its Devanagari twin |
| … elsewhere | 69 | p. 31 L662, p. 31 L697, p. 34 L757 | read each one (many sit inside notes of ours that go whole) |
| `[sic]` | 143 | (not yet sampled by page) | mark goes |
| `[as printed]` | 146 by exact form (234 counting "[…as printed]" variants) | p. 17 L418, p. 22 L497, p. 91 L2287 | mostly after a reference that differs from the standard one: mark goes, the figure stays. These are ours |
| other "as printed" | 901 in all; 511 inside `*( … )*` notes, 148 other, 8 on Sanskrit lines | p. 42 L1069, p. 37 L906 ("Phiṭ-sūtra 80 as printed"), p. 42 L1058 ("The list as printed:") | inside a note of ours: the note goes. The 148 "other": read a sample — some are Sāyaṇa's/the editor's words ("the list as printed") → I'd edit only the clear remarks and leave the rest; stop-and-ask case |
| "mine and tentative" | 92 | p. 67 L1680, p. 140 L3286, p. 261 L5733 | the remark goes; the gloss it is attached to: **your decision** (keep the gloss, or drop the gloss too? — the source gives no translation for these) |
| `Gloss:` lines | 100 (some end "[tentative]" or "not attempted") | p. 35 L793, p. 35 L805 | tags go; the "not attempted" ones need your word (line removed or kept?) |
| "I read / I am unsure / my best reading / I could" etc. (first person) | 123 lines with "I …", 35 with "my" | p. 31 L692, p. 32 L717, p. 37 L898, p. 55 L1374 | each is a note of ours → note goes whole. Read each |
| "garbled / blurred / unclear / not legible" | 83 lines | p. 31 L680, p. 33 L741 | as above: ours when in a note, check when in the translation |
| "the scan / the print / this scan" | 251 lines | p. 18 L446, p. 31 L662 | notes of ours; check for the few that quote the book itself |
| Whole-line italic notes `*( … )*` | **699** lines | p. 0 L46, p. 163 L3878, p. 414 L8691 | most hold the above. Plan: classify each by script as (a) process remark (goes), (b) reader's note that adds content (e.g. p. 414 L8691 "continued from p. 413") — **for these I need your rule**: do they stay? |
| Inline `*( … )*` inside a line | 724 lines | p. 167 L3966, p. 433 L8884 | read a sample; many are the commentary's/ours explanatory parentheses |
| "Page header: …" notes | 210 | p. 32 L701, p. 109 L2643, p. 187 L4360 | go (running-head remarks; "English as printed" etc.) |
| `[accent ?]` / `[tentative …]` tags | 246 lines | p. 24 L521, p. 387 L8292, p. 732 L15815 | `[accent ?]` goes **after Part B** (the reference decides the accents) — it is Part B's work list |
| "Oct 2026 numeral pass" notes | 26 | p. 17 L418, p. 25 L558 | go |
| "Target for next session" | 3 (p. 6 L190, p. 16 L410, p. 24 L539) | | go |
| Progress notes | 1 at end (L17938, "Volume 2 complete … accent pass complete (Oct 2026)") | | replace by the single trailing `**Progress note:** Done through printed p. 808` (rule 3) |
| Translator's Preface (L10), Table of Contents "Roadmap" (L28) at the head | 2 sections | | listed only; front matter is rebuilt later, the English text of the Preface is left until then |
| Cyrillic string (STATUS) | **0 found** in a search for Cyrillic, Arabic, Greek, Telugu, CJK | | nothing to remove (the STATUS entry looks stale) |
| Kannada letters in the English file | 39 lines | p. 0 L10, p. 201 L4673, p. 525 L10702 | all are section heads/quoted Kannada headings (not remarks); left |

## Differences from your estimates
- My `[?]` total is 432, as yours. My split by line type differs from yours (66/259/64/43) because I split by "contains Devanagari" first; the 259 "after a number" are mostly on Devanagari or IAST lines. The totals agree.
- A plain grep "as printed" gives 901; 234 of those are bracketed tags.

## Questions before Step A2
1. **Uncertain readings.** Proposal: every `[?]` leaves the text; where it stood for a really uncertain reading (Devanagari/IAST/reference), place, page and sentence go into `vol2/review/open_readings.tsv` (about 300 rows), so nothing is forgotten. Yes?
2. **"Mine and tentative" glosses (92) and `Gloss:` lines (100):** keep the English gloss, drop only the remark? Or drop the gloss where the source gives no translation?
3. **Whole-line italic notes** that are not process remarks but contain content (continuations, "see note at Rk 3.5", the commentary's structure): remove only process remarks, keep these?
4. The `[as printed]` tags: remove the mark and keep the number as it stands (which means a reference that differs from the standard one loses its flag; the flagged places go to `removed_remarks.tsv`). Yes?

## Decision of the user (Nov 17 2026)
`[?]` after a number or reference **stays in the text for now** (the user will review them). This applies on every line type (Devanagari, IAST and English lines alike): by my pattern (digit, optional `)`, optional space, `[?]`) that is 112 of the 432 marks. Those 112 are not touched in Part A; only a list of them (`vol2/review/refs_marked.tsv`: page, line, reference, sentence) is made for the review. The sentences of ours about the marks ("marked [?] where unsure") go as proposed, except that where a note explains marks that stay, it stays too until the review. Questions 2–4 above are still open.
