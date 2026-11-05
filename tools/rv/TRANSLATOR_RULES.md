# Translator rules for one 3-page window (Vol 15 onwards, Claude Code, Sonnet) — text-based

**Base text (user decision, Nov 5 2026):** the machine-read HTML/markdown the user supplies, not the scan. Tests on Vol 5 (54 pages, 79,787 characters) showed it matches an independent reading of the scan on 98.85 % of characters and the user found its numerals correct; its known weak points are `||` (double danda) and the avagraha (`s`), both repaired by script, and occasional single-letter OCR slips. **You do not look at page images.** The scan (if present) is used only for a spot check when the user asks.

You are given a window directory `volN/work/wPPPP/` made by `python3 tools/rv/batch.py prep N`: `kn.md` (the Kannada text of the 3 printed pages, made by script from the supplied text), `numerals.txt` (rows of the user's numeral file), `pages.json`, `PROMPT.txt`. You write **`en.md`**; scripts do everything else (Devanagari, IAST, accents, labels, checks, appending).

Read first (once): `CLAUDE.md` conventions, the last ~80 lines of the English output file (format), this file. Do not re-read other volumes.

## Order of work (target <= 8 tool calls per window)
1. **Read `kn.md` and `numerals.txt`** (one parallel message).
2. **Check `kn.md` against its own structure** (see "Checking kn.md"); fix with `batch.py fix N WIN kn "OLD" "NEW"` (exact, unique). Do not retype the file.
3. **Write `en.md`** (one heredoc): the English-file chunk.
4. `python3 tools/rv/batch.py build N WIN` then `python3 tools/rv/batch.py check N WIN`. Fix what the check lists, re-run until PASS.
5. `python3 tools/rv/batch.py commit N WIN --note "short note"` (appends to both volume files, commits, pushes). Never edit the volume files by hand; never `git checkout`/restore them.

## Checking kn.md (the text is the supplied text; letters and numbers are NOT changed by the script)
- The script wrote the page markers `<!-- printed N -->`, the running head, the section labels (standard form) and turned the Saṃhitā, Pada and Sāyaṇa-bhāṣya lines into `> ` blocks. Check: (a) the first lines of the window: if the window starts inside a section, the lines may have come out as prose (or as the wrong section): add or remove the leading `> ` accordingly; (b) a block that is really a Ṛk's Saṃhitā or Pada must not be mixed with prose; (c) a Sanskrit quotation inside the Special Topics stays prose in kn.md (mark it in en.md with `⟦ ⟧`).
- **Never "correct" a letter or number from memory.** If a word or digit looks impossible (a Latin letter inside Kannada, a wrong sūtra number against the numeral file), report it: the user decides. If a place cannot be settled, write `[?]` after it in kn.md and in en.md and pass `--max-doubts N` to `commit`; the place goes to the doubts log for the user.
- Known weak points of the supplied text: single-letter OCR slips such as `ಕ`/`ಣ`, `ಐ`/`ಯ್ಯ`, `ಸ`/`ಪ`, label spellings like `ಪಾರಃ` for `ಪಾಠಃ` (the script repairs the labels), a duplicated garbled line. If two readings of a verse line differ between the Saṃhitā and the Pada or the bhāṣya quotation of the same words, note it.

## en.md — the English-file chunk
- Format exactly as the end of the English output file: page headings `### Printed p. N` (one per page of the window), sūkta heading blocks, `#### Ṛk N`, label lines. **Do not write the Progress note.**
- Write labels in English (`**Saṃhitā-pāṭha**`, `**Pada-pāṭha**`, `**Sāyaṇa-bhāṣya**`, `**Pratipadārtha**`, `**Bhāvārtha**`, `**Special Topics**`); the labels are normalised by script.
- **Sanskrit blocks: write `[[bN]]` alone on a line** (N = number of the `> ` block in kn.md, counted from 1 across the whole window, in order of appearance) where the block belongs, under its label. Every block must be placed exactly once (the build fails otherwise). **Never type Devanagari or IAST.** Inline Sanskrit in English prose: write the Kannada-script word inside `⟦ ⟧`, copied from kn.md.
- Bhāṣya: no English rendering, only a gist (<= 25 words) per Ṛk when the sense is not obvious from the Pratipadārtha. Grammar pages: a 2–4 line note naming words and legible sūtras. Pratipadārtha, Bhāvārtha, Special Topics: translate the Kannada prose faithfully. The printed English translation of each Ṛk is in the supplied text (Latin letters): reproduce it as given, misprints marked [sic].
- Accents: automatic (Saṃhitā only, from `refs/mandala/`). Do nothing.

## Numerals
- `numerals.txt` lists the user's file rows (references with separators) per page. `check` compares them with kn.md: NEAR (differs by 1–2 characters), file rows with no counterpart in kn.md, and English references with no Kannada twin all FAIL. The user's file and the supplied text are both machine-read: where they disagree, do not guess — put `[?]` and report both values.
- In en.md write each reference as in kn.md, in Latin digits (`Pā. 6-1-163`). Plain numbers (no separators: counts, page ranges, Ṛk numbers) are not in the file: take them from kn.md.
- Where the supplied text prints no number, write none (never supply one from memory).

## Doubts
There is no zoom step any more. The aim is still zero `[?]` at commit; leftovers (`--max-doubts N`) are listed for the user with the exact words/digits in doubt. No OCR, no outside sources.
