# Translator brief (one page; read once — `TASK.md` of each window carries everything else)

You translate one window (about 6 printed pages) of the Kannada Ṛgveda edition into English for a book that people will read. **One read, one write, one command:**

1. Read `WIN/TASK.md` (the script's notes, the end of what is already translated, and `kn.md` with its Sanskrit blocks numbered `«bN»`).
2. Write `WIN/en.md` in one go.
3. Run `python3 tools/rv/batch.py done VOL WIN --note "what the window covers"`. It builds, runs every gate, commits, pushes and verifies. If it prints FAIL, fix what it lists and run it again; when it prints `VERIFIED`, report in ≤ 4 lines. Never touch git or the volume files yourself.

## The English text carries no remarks of yours — only the mark `**NOTE**` (user decision, Nov 11 2026)
- **Never write into en.md:** running heads, "as supplied" / "as printed" remarks, `[?]`, `[sic]`, italic bracketed comments `*[…]*`, comments on garbled labels, stray lines, page numbers, ornaments or the state of the text. The Kannada file keeps all of that; the reader of the English must not see it.
- **Where something needs the editor's decision or a second look, write `**NOTE**{…}` right after the place**, with the question inside the braces: the Kannada words concerned (in Kannada letters) and what is doubtful. The script leaves only `**NOTE**` in the text and puts the braces' content into a list for the editor. Use it for: a reading you could not settle; a misprint whose intended word you had to guess (translate your best reading, then NOTE); a number or reference that does not fit (keep the printed number, then NOTE); text that seems to be missing or broken off; a printed-English misprint that changes the sense; an abbreviation you cannot expand; a place where the Kannada gloss and Sāyaṇa's Sanskrit disagree.
- Do **not** NOTE what needs no decision: an obvious spelling slip of the machine reader that leaves the sense certain, a garbled label, a stray line. Translate the sense and move on.
- A NOTE is short and factual: `**NOTE**{ಭಾಗ printed; "share"? read here as ಛಾಗ "he-goat"}`. No apology, no explanation of method.

## en.md
```
### Printed p. 197
## Sūkta 163 (Maṇḍala 1)            ← only where kn.md shows a sūkta beginning (introduction block [[bN]], English Anuvāda, particulars); number from kn.md
#### Ṛk 5                            ← where a Ṛk begins
**Saṃhitā-pāṭha**
[[b1]]
**Pada-pāṭha**
[[b2]]
**Sāyaṇa-bhāṣya**
[[b3]]
*Gist:* ≤ 25 words of what Sāyaṇa says (from his Sanskrit; the grammatical tail is not explained).
**Pratipadārtha**
- ⟦ಮಾತರಿಶ್ವಾ⟧—the wind
- ⟦ಏನಂ⟧—this (Agni)
- …                              ← one word per line, as a list, in the order printed
**Bhāvārtha**
English of the Kannada paragraph.
**Printed English**
The English printed in the book, exactly as supplied.
**Special Topics**
Faithful English of the Kannada; every Sanskrit quotation in full as ⟦…⟧ with its printed reference (Ni. 2-13).
**Grammar**
2–4 lines naming the words and the sūtras as printed (Pā. Sū. 6-1-163).
```
- One `### Printed p. N` heading per printed page, nothing else about the page. A section that continues from the previous window simply continues (its block first); no "[Continuing …]" line.
- `[[bN]]` alone on a line, every block exactly once, where it belongs. A Saṃhitā or Pada is always a block, never copied inline.
- Inline Sanskrit: copy the Kannada-script words from kn.md inside `⟦ ⟧`. **Never type Devanagari or IAST** — scripts make them (and the accents). Long quotation (more than about 8 words): write only its first and last words, `⟦first two words~~last two words⟧`; the script copies the passage from kn.md, with its closing danda (spaces do not matter; the first words must occur only once in kn.md — the same passage often stands in the bhāṣya and again in the commentary, then take more words; take the end words from one unbroken stretch without a danda). Only text of this window's kn.md, and only Sanskrit, goes inside `⟦ ⟧`: a Kannada gloss word is translated, a grammar term you derive yourself (śānac, num, aṭ) is written in Latin letters.
- Do not write a Progress note. Do not repeat anything shown under "Context". A sentence that started on the previous page: read the context lines and complete it; a sentence cut at the end of the window: translate what is there (the next window continues it).

## Rules that are never bent
- The supplied text is the base. **Never correct a letter or number from memory or from another edition.** What you cannot settle gets `**NOTE**{…}`.
- Where the print gives no number, write none. References as in kn.md, in Latin digits, **the abbreviation in Latin letters** (no Kannada script anywhere in the English text; the gate refuses it):
  ಋ. ಸಂ. Ṛ. Saṃ. · ನಿ. Ni. · ಪಾ. ಸೂ. Pā. Sū. · ಉ. ಸೂ. Uṇ. Sū. · ಫಿ. ಸೂ. Phi. Sū. · ಪಾ. ಶಿ. Pā. Śi. · ಐ. ಬ್ರಾ. Ai. Brā. · ಐ. ಆ. Ai. Ā. · ಐ. ಉ. Ai. U. · ತೈ. ಸಂ. Tai. Saṃ. · ತೈ. ಬ್ರಾ. Tai. Brā. · ತೈ. ಆ. Tai. Ā. · ಶ. ಬ್ರಾ. Śa. Brā. · ತಾ. ಬ್ರಾ. Tā. Brā. · ವಾ. ಸಂ. Vā. Saṃ. · ಮೈ. ಸಂ. Mai. Saṃ. · ಸಾ. ಸಂ. Sā. Saṃ. · ಅಥ. ಸಂ. Atha. Saṃ. · ಛಾ. ಉ. Chā. U. · ಬೃ. ಉ. Bṛ. U. · ಆ. ಸೂ. / ಆ. Ā. Sū. (Āśvalāyana) · ಆಪ. ಸೂ. Āpa. Sū. · ಜೈ. ಪೂ. ಸೂ. Jai. Pū. Sū. · ಬ್ರ. ಸೂ. Bra. Sū. · ವೇ. ಸೂ. Ve. Sū. · ಮ. ಭಾ. Ma. Bhā. · ಮ. ಸ್ಮೃ. Ma. Smṛ. · ಯಾ. ಸ್ಮೃ. Yā. Smṛ. · ವಾ. ಪು. Vā. Pu. · ವಿ. ಪು. Vi. Pu. · ಬೃ. ದೇ. Bṛ. De.
  An abbreviation that is not in this list, or looks misread: transliterate it letter for letter into Latin letters and add `**NOTE**{abbreviation ಕರ. printed}`.
- Sanskrit is quoted in full, never summarised: the last words, printed abridgement dots `.... ....` and the closing danda belong to the quotation; a Sanskrit phrase such as `ಇತಿ ಚ ಬ್ರಾಹ್ಮಣಂ` is quoted, not turned into English.
- **Do not translate a Sanskrit quotation that the Kannada does not translate**; render only the Kannada's own explanation. No English gloss in parentheses after a Sanskrit word unless the Kannada gives one.
- Check who does what before writing a sentence with two actors (who helps whom, whose attribute it is); technical terms exactly (ādyudātta is not anudātta, a sautra root is not "Saura"). The Gist follows Sāyaṇa's Sanskrit where it and the Kannada gloss differ (and that place gets a NOTE).
- Never change what the print says to pass a gate: keep it and report the gate message.

## kn.md (made by script; check it, do not retype it)
The script has already standardised and inserted section labels, joined line-end hyphens, wrapped stray lines, inserted markers for missed running heads and rewritten Devanagari letters as Kannada; TASK.md lists what it did. **Check the structure before writing:** every Saṃhitā, Pada and bhāṣya is a `> ` block under its standard label; Kannada prose (Pratipadārtha, Bhāvārtha, Special Topics, grammar) is not inside a block; a page that the script could not mark gets `<!-- printed N -->` + its head line. Repair with `python3 tools/rv/batch.py fix VOL WIN kn "OLD" "NEW"` (exact, unique; letters unchanged) and look at the new block numbers with `batch.py view VOL WIN`.
`[figure: …jpg]` line (handle it before the first `done`): look at the picture; if it only repeats a verse block that kn.md already has as text, remove the line with a fix; otherwise write the verse it holds into kn.md letter by letter in Kannada script and remove the line; a letter you cannot read gets a NOTE in en.md. Small hook or division marks in a picture's Pada line are not transcribed.
If you made the same hand-fix a third time, say "recurring: …" in the report: it becomes a script change.

*(Vols 12–16 were made under the older convention with "as supplied" remarks, `[?]` and `[sic]`; do not imitate their style.)*
