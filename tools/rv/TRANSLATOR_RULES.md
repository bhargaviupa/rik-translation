# Translator rules for one 3-page window (Vol 15 onwards, Claude Code, Sonnet) — text-based

**Base text (user decision, Nov 5 2026):** the machine-read HTML/markdown the user supplies, not the scan. Tests on Vol 5 (54 pages, 79,787 characters) showed it matches an independent reading of the scan on 98.85 % of characters and the user found its numerals correct; its known weak points are `||` (double danda) and the avagraha (`s`), both repaired by script, and occasional single-letter OCR slips. **You do not look at page images.** The scan (if present) is used only for a spot check when the user asks.

You are given a window directory `volN/work/wPPPP/` made by `python3 tools/rv/batch.py prep N`: `kn.md` (the Kannada text of the 3 printed pages, made by script from the supplied text), `numerals.txt` (rows of the user's numeral file, if supplied), `pages.json`, `PROMPT.txt`. You write **`en.md`**; scripts do everything else (Devanagari, IAST, accents, labels, checks, appending).

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
- The user found the numerals of the supplied text correct, so the **numeral file is optional** (user, Nov 5 2026). If `numerals.txt` has rows, `check` compares them with kn.md (NEAR = differs by 1–2 characters, rows with no counterpart, English references with no Kannada twin all FAIL) and a disagreement is reported with both values, never guessed. With no numeral file the numerals are taken from kn.md as supplied; `check` still requires every reference in en.md to have the same reference in kn.md.
- In en.md write each reference as in kn.md, in Latin digits (`Pā. 6-1-163`). Plain numbers (counts, page ranges, Ṛk numbers) are taken from kn.md.
- Where the supplied text prints no number, write none (never supply one from memory).

## Doubts
There is no zoom step any more. The aim is still zero `[?]` at commit; leftovers (`--max-doubts N`) are listed for the user with the exact words/digits in doubt. No OCR, no outside sources.

## Lessons from Vol 15 (binding; full list in `docs/LESSONS.md`)
- **Sanskrit is quoted in full, never paraphrased or summarised** — Special-Topics quotations, bhāṣya glosses that carry meaning, Nirukta/Brāhmaṇa passages. Use `⟦…⟧` copied from `kn.md` (script with start/end markers), never retype.
- **Printed oddities stay and are noted**: a word that looks like a misprint, a doubled reference, a wrong head, a verb that differs between Pratipadārtha and Bhāvārtha → keep as supplied and add a short bracketed italic note ("as supplied"); do not choose the 'obvious' reading silently. Translate what the Kannada says, not what the Sanskrit probably meant.
- **Running heads**: ಮಂ. = Maṇḍala, ಅ. between ಮಂ. and ಸೂ. = **Anuvāka** (not Aṣṭaka), ಸೂ. = Sūkta, ಅ./ವ. on the other side = Adhyāya/Varga. Write the head as printed, expand only with this legend, and say "(printed …)" when the print looks odd.
- **Every stray line is kept** as an italic note (page numbers, ornaments, "This image contains…", converter lines, Tamil numerals); never delete. Characters of other scripts inside Kannada (Devanagari ॐ, Telugu, Latin S for avagraha) → rewrite letter for letter as Kannada in `kn.md` and note it.
- **Gates, in this order, joined with `&&`**: `batch.py build` → `batch.py check` → `tools/rv/check_inline.py WIN` → `batch.py commit`. After any edit of `en.md`/`kn.md` confirm the edit really applied (print "applied"); read the commit output to the end (`git: pushed`).
- **Report with evidence** (≤ 15 lines): the exact last sentence written, `git log -1 --oneline`, `git status -sb`, the tail of the English file (progress note), grep results for `XXX` and `⟦ (*⟦*)⟧`, and every hand-fix kind you used (the dispatcher counts them for the volume metrics). If something failed, say so first.
- **Accent/doubt/page-flag lines are logged to the volume's review files**, not only mentioned in the report.
- **Improve the process**: if you do the same hand-fix a third time in a volume, say so in the report ("recurring: …") so the dispatcher can turn it into a tool change (`docs/LESSONS.md`, CLAUDE.md §15).
- **Reference abbreviations (user's reading of the print, Nov 9 2026)**: ಸಿ. is ನಿ. = Nirukta → write `Ni.`; ಮಿ. ಸಂ., ಮ. ಸಂ., ಪು. ಸಂ. are ಋ. ಸಂ. = Ṛgveda-saṃhitā → write `Ṛ. Saṃ.`; ಇ. ಬ್ರಾ. is ಐ. ಬ್ರಾ. = `Ai. Brā.`. `kn.md` already has them corrected (script); write the corrected Latin form in `en.md` without a 'printed …' remark. Doubtful other abbreviations → ask the user, never guess.
- **Footnotes**: your bracketed italic remarks (running heads, stray lines, doubtful readings, 'as supplied …') are printed as numbered footnotes; keep each remark short and self-contained; put the remark right after the sentence it concerns; leave `[?]` and `[sic]` in the running text.
- **Page breaks**: a sentence that continues over a printed-page break must be translated completely: read the last words of the previous page with the first words of the next before writing either (a lost phrase at a page break was the user's first review finding).
