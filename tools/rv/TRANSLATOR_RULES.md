# Translator rules for one 3-page window (Vol 15 onwards, Claude Code, Sonnet)

You are given a window directory `volN/work/wPPPP/` (made by `python3 tools/rv/batch.py prep N`): `strips/` (page images, full width, top to bottom), `numerals.txt` (rows of the user's numeral file for these pages), `pages.json`, `PROMPT.txt`. You write **two files** there: `kn.md` and `en.md`. Scripts do everything else (Devanagari, IAST, accents, labels, checks, appending).

Read first (once): `CLAUDE.md` conventions, the last ~80 lines of the English output file (format), `tools/rv/TRANSLATOR_RULES.md` (this file). Do not re-read other volumes.

## Order of work (target <= 14 tool calls per window)
1. **One message: view every strip of all 3 pages** (parallel Read calls). Never view a strip, think, then view the next.
2. **Write `kn.md`** (one Bash heredoc): the whole printed page in Kannada script, exactly as printed (rules below).
3. **Write `en.md`** (one heredoc): the English-file chunk (rules below).
4. `python3 tools/rv/batch.py build N WIN` then `python3 tools/rv/batch.py check N WIN`.
5. **Resolve every `[?]` and every numeral problem the check lists** (see "Zero doubts" below), re-run build + check. Repeat until PASS.
6. `python3 tools/rv/batch.py commit N WIN --note "short note"` (appends to both volume files, commits, pushes). Never edit the volume files by hand; never `git checkout`/restore them.

## kn.md — the Kannada transcription (Kannada script only)
- Start each page with `<!-- PDF M · printed N -->` (values from pages.json), then the running head in italics `*[ಮಂ. ೧ ಅ. ೨೪ ಸೂ. ೧೮೫]*`.
- Content in printed order: section labels in italics as printed (*ಸಾಯಣಭಾಷ್ಯಂ*, *ಪ್ರತಿಪದಾರ್ಥ*, *ಭಾವಾರ್ಥ*, *ವಿಶೇಷವಿಷಯಗಳು*, *ವ್ಯಾಕರಣಪ್ರಕ್ರಿಯಾ*), bold headwords `**...**`, Kannada prose as paragraphs.
- **Every block of Sanskrit** (Saṃhitā, Pada, Sāyaṇa-bhāṣya, Sanskrit quotations) as `> ` lines, one per printed line, **in Kannada script as printed** (keep printed hyphenation at line ends, danda marks, the avagraha as ಽ). Consecutive `> ` lines are one block; the blocks are numbered b1, b2, … in order of appearance across the whole window.
- Inline Sanskrit words inside prose may be marked `⟦ಅಗ್ನಿಂ⟧`; the marks are removed in the Kannada file.
- Letter by letter. **Never complete, correct or normalise a word or number from memory**, however familiar the verse. Plain *ma*/*ya* are printed with a hook like the vowel sign u (ಮುರುತಃ = marutaḥ): do not read it as u. The small subscript stroke in Pada lines is the compound mark (ಽ in Devanagari; write what is printed).
- No Devanagari, no IAST, no English in kn.md (the printed English translation of a Ṛk goes only into en.md).

## en.md — the English-file chunk
- Format exactly as the end of the English output file: page headings `### Printed p. N  (PDF M)` (one per page, as many as in pages.json), sūkta heading blocks, `#### Ṛk N`, label lines, `**Progress note**` is NOT written by you.
- Write labels in English (`**Saṃhitā-pāṭha**`, `**Pada-pāṭha**`, `**Sāyaṇa-bhāṣya**`, `**Pratipadārtha**`, `**Bhāvārtha**`, `**Special Topics**`, `**Viśeṣaviṣayagaḷu**` variants are normalised by script).
- **Sanskrit blocks: write `[[bN]]` alone on a line** (N = block number in kn.md) where the block belongs, under its label. Every block must be placed exactly once (the build fails otherwise). **Never type Devanagari or IAST.** Inline Sanskrit in English prose: write the Kannada-script word inside `⟦ ⟧`, copied from kn.md.
- Bhāṣya: no English rendering, only a gist (<= 25 words) per Ṛk when the sense is not obvious from the Pratipadārtha. Grammar pages (Vyākaraṇa-prakriyā): a 2–4 line note naming words and legible sūtras.
- Pratipadārtha, Bhāvārtha, Special Topics: translate the Kannada prose faithfully. The printed English translation of each Ṛk (Latin type): reproduce as printed, misprints marked [sic].
- Accents: automatic (Saṃhitā only, from `refs/mandala/`). Do nothing.

## Numerals
- `numerals.txt` lists the user's file rows (references with separators) per page: file line | Kannada pattern | English digits | noisy context. Use them as the reading of each reference: look at the strip; if the row fits (same place, same shape), **use the file's digits**, in Kannada digits in kn.md and the same value in Latin digits in en.md (`Pā. 6-1-163`). The English file keeps the printed reference; the Kannada file keeps the printed Kannada digits.
- If the strip clearly differs from the file, zoom once. The zoom decides; if you override the file, add `file said X` in the note you pass to `commit`, and log the place.
- Plain numbers (no separators: counts, page ranges, Ṛk numbers) are not in the file: read them from the strip; zoom if unsure.
- Where the print gives no number, write none (never supply one from memory).
- `check` compares the file with kn.md: NEAR (differs by 1–2 characters), file rows with no counterpart in kn.md, and English references that have no Kannada twin all FAIL. Fix by zooming (not by guessing).
- Digit shapes (calibrate on the running head in the same crop): 2 round open loop, 3 hooked ಇ/ಖ-like, 7 flat-footed ಒ-like; 4 like ಳ; 5 like ಣ; 6 hook at top-left; 8 like ಲ/ಅ; 9 like ಕ; 1 like ∩; 0 like ○. Frequent confusions: 3/5, 6/7, 2/9, 8/9, 2/3/7.

## Zero doubts (the aim: near zero `[?]` before the window is committed)
1. Write the first draft with `[?]` after every word/digit group you cannot read with confidence (never guess silently; a wrong confident reading is worse than `[?]`).
2. After `build`, run `python3 tools/rv/batch.py zoomlist N WIN`. For every `[?]` and every NEAR/missing numeral: render a zoom, **all zooms in one parallel round** (several Bash calls to `python3 tools/rv/page.py N PDF /tmp/z_K --strip S --box X0 Y0 X1 Y1`, then one message with all the zoom Reads). The box is in the pixel coordinates of the strip *as displayed* (multiply by the viewer's scale factor if it reports one); make it a generous full line; check it shows the intended word.
3. Apply fixes with `python3 tools/rv/batch.py fix N WIN kn|en "OLD" "NEW"` (exact, unique). Fix the Kannada first; Devanagari and IAST are regenerated by `build`, so never patch them. Fix the English twin too (same reference, same word).
4. Re-run build + check. Maximum **2 zoom rounds**. What is still unreadable after that stays `[?]`; commit with `--max-doubts N` (N = the number left) and list each remaining place with your best reading in the commit note.
5. Do not use OCR. If an image view returns no image, STOP and report; never write that page.
