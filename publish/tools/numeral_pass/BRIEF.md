# Brief: numeral second-pass for Vol 8 (Rigveda translation), Sūkta 95

Project: /home/user/rik-translation. Output file `Rigveda_Samhita_Vol8_English_Translation.md` is an English translation of a 1949 Kannada commentary. Kannada numerals in it were read from a poor scan and are often wrong or flagged "[?]". We re-read every numeral from a clean 600 ppi scan of the same book.

## Scan
`/tmp/altwt/w/Rig_Vol8_alt.pdf` (853 pages). For printed page P of the Seventh Adhyāya main text: alt PDF page = P + 21 (printed p. 28 = alt PDF 49). In the .md, each printed page has a heading `### Page P (PDF Q)` (Q = P+20, our older scan).

## Tools (already written; run from anywhere)
- `python3 /tmp/claude-0/-home-user-rik-translation/4b61173c-0ed7-5073-81ed-e66fb47d38a4/scratchpad/pg.py ALT K` renders alt page ALT at 200 dpi into K horizontal strips (`pg<ALT>_<i>.jpg` in the CURRENT directory; `cd` into your own work dir first, e.g. /tmp/agentwork_<yourname>). Use K=3. View the three strips with the Read tool to see the whole page.
- `python3 .../scratchpad/mont.py ALT K out.jpg 'strip,x,y,w,h;strip,x,y,w,h;...'` crops numerals from the strips (coordinates are in the pixel space of the viewed strip image; the crop is rendered at 600 dpi and stacked, labelled 1,2,3…). Make a montage of ALL numerals on a page (header, page number, every sūtra/verse/Nirukta/Manu/etc. reference, verse-end numbers ‖ N ‖), view it, and decode. Both scripts must be run from the same directory (mont.py reads the pg*.jpg that pg.py wrote there). Crop heights ~45 px, widths to fit the reference. If a crop misses, widen and retry.

## Glyph key for this print (CONFIRMED by the reader)
Kannada digits: ೧=1 looks like "∩"; ೦=0 looks like "○". **Flat-footed "2"-like glyph = 7. Curled "2"-like glyph = 2.** ೬ (6) has a hook at the top-left (like "ಓ"). ೮ (8) looks like "ಲ"/"ಅ". ೯ (9) looks like "ಕ"/"ೞ". ೪ (4) looks like "ಳ". ೫ (5) looks like "ಣ". ೩ (3) looks like "ಇ"/"ಞ". Known confusions of mine: 3 vs 5, 6 vs 7, 2 vs 9, 8 vs 9. Zoom and decide per glyph; context (the verse or sūtra being cited; you may use standard references only as a sanity check) helps but the PRINT wins: record what is printed, and if it differs from the standard number say so in the note.

## What to do
For each printed page assigned to you: view it, find EVERY Kannada/Indic numeral that is part of a reference: running head (ಮಂ. ೧ ಅ. ೧೫ ಸೂ. ೯೫ / ಅ ೧ ಅ ೭ ವ ೧ ; page number), Ṛ. Saṃ. / Vā. Saṃ. / Tai. Saṃ. / Brā. / Ni. / Pā. Sū. / Uṇ. / Dhā. / Bṛ. De. / Manu / Śa. Brā. etc. references, counts (ಹತ್ತು etc. are words, ignore), ‖ N ‖ verse numbers, and numerals inside the Sanskrit bhāṣya. Then compare with how the .md renders that page (read the page section of the .md: look for numbers like `Pā. 6-1-197 [?]`, `(Ṛ. Saṃ. 4-4-4 as read [?])`, `Ni. 2-10 [?]`, etc.).

Output a JSON list of PATCHES to `/tmp/claude-0/-home-user-rik-translation/4b61173c-0ed7-5073-81ed-e66fb47d38a4/scratchpad/agents/patches_<yourname>.json`. Each patch: `{"page": P, "old": "<exact text from the .md, unique within that page's section>", "new": "<replacement>", "confidence": "high|medium|low", "note": "<why; what the print shows>"}`. Rules for patches:
- Change ONLY numerals/references and their "[?]" / "as read" qualifiers. Never alter Devanagari, IAST words, or English prose otherwise.
- If the .md number is already right: if it carries a "[?]" or "as read [?]" and your reading is high/medium confidence, patch to remove the qualifier (e.g. `Pā. 6-1-197 [?]` → `Pā. 6-1-197`). If it has no flag and is right, no patch.
- If the .md is wrong: patch to your reading. For low confidence keep or add a `[?]`.
- If the .md gives a number the print does not give at all (e.g. a sūtra number the print omits), patch to remove just the number/parenthetical and mention it in the note.
- If the .md omits a number that the print has (e.g. "no number given"), add it in the same style when the place is clear; otherwise report it only in `unplaced`.
- `old` must be copied verbatim from the .md (use Grep/Read to copy exactly, including `*` italics and non-breaking forms) and must occur exactly once in the section of that page. Make `old` long enough to be unique but short enough to avoid copying surrounding Sanskrit when possible; when a number appears twice on a page with different contexts, include a few words of context in both old and new.
- Also output a list `unplaced` of numerals you read but could not place (page, text after which, reading, confidence).
Write the final file as `{"patches":[...],"unplaced":[...]}`. Do NOT edit the .md or any other repo file. Do not run git.
- Do not review images beyond numerals; do not retranscribe text.
- Work through ALL your pages; do not stop early. Budget: about 6–10 tool calls per page.

## Already-known readings (from the reader; authoritative)
See `agents/Vol8_Sukta95_user_corrections.md` (Uṇ. numbers) and the reading logs `agents/rows95*.py` for pages 1–27 (examples of the style and of confirmed readings). The reader confirmed: 10-2-7 and 7-78-3 (glyph rule above); p. 4 numerals all correct.

Final message: one short paragraph: pages done, number of patches, number of low-confidence items, anything odd.

## Addendum (wave 2: Sūktas 96–112)
- The `.md` page headings are `### Page N (PDF M)` (M = N+20); alt PDF page = N+21. A page's section runs to the next `### Page` heading even if it contains a `## Sūkta NN` heading line (a new sūkta can start mid-page; its heading block with ‖ Maṇḍala … ‖ numerals counts).
- Rik-end markers ‖ N ‖ and Sūkta/Ṛk counts (ಋಕ್ಸಂಖ್ಯೆ) are numerals too: check them. Verse numbers in the Saṃhitā/Pada text lines matter.
- `mont.py` now uses a per-process temp name, so parallel runs no longer clash.
- Page 102's printed p. 323 may be missing in one scan; if a page you are given has no matching heading in the .md, skip it and report it.
- Work conservatively: an unflagged number that looks right needs no patch. Do not remove a flag from a number you could not read clearly.
