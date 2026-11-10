# Translator brief (one page; read once — `TASK.md` of each window carries everything else)

You translate one window (about 3 printed pages) of the Kannada Ṛgveda edition into English. **One read, one write, one command:**

1. Read `WIN/TASK.md` (the script's notes, the end of what is already translated, and `kn.md` with its Sanskrit blocks numbered `«bN»`).
2. Write `WIN/en.md` in one go.
3. Run `python3 tools/rv/batch.py done VOL WIN --note "what the window covers"`. It builds, runs every gate, commits, pushes and verifies. If it prints FAIL, fix what it lists and run it again; when it prints `VERIFIED`, report in ≤ 4 lines (its last line, hand-fixes you made, doubts). Never touch git or the volume files yourself.

## en.md
```
### Printed p. 197
*Running head: 197 Sāyaṇa-bhāṣya-sahitā [ಮಂ. ೧. ಅ. ೨೨. ಸೂ. ೧೬೨] (as supplied).*
## Sūkta 163 (Maṇḍala 1)            ← only where a sūkta begins (introduction block [[bN]], English Anuvāda, particulars)
#### Ṛk 5                            ← where a Ṛk begins
**Saṃhitā-pāṭha**
[[b1]]
**Pada-pāṭha**
[[b2]]
**Sāyaṇa-bhāṣya**
[[b3]]
*Gist:* ≤ 25 words; the grammatical tail is not explained.
**Pratipadārtha**
⟦ಮಾತರಿಶ್ವಾ⟧—the wind; ⟦ಏನಂ⟧—this (Agni); …
**Bhāvārtha**
English of the Kannada paragraph.
**Printed English**
The English printed in the book, exactly as supplied (misprints marked [sic]).
**Special Topics**
Faithful English of the Kannada; every Sanskrit quotation in full as ⟦…⟧ with its printed reference (Ni. 2-13).
*Grammar (transcribed, not explained):* 2–4 lines naming the words and the sūtras as printed (Pā. Sū. 6-1-163).
```
- `[[bN]]` alone on a line, every block exactly once, in the place where it belongs. A block that continues from the previous window goes first, under `[Continuing …]`.
- Inline Sanskrit: copy the Kannada-script words from kn.md inside `⟦ ⟧`. **Long quotation (more than about 8 words): write only its first and last words, `⟦first two words~~last two words⟧`; the script copies the passage from kn.md** (spaces do not matter; the first words must occur only once in kn.md — the same passage often stands in the bhāṣya and again in the commentary, then take more words; do not write your own expander script). Never add `(*iast*)` after a segment. Only text that stands in kn.md goes inside `⟦ ⟧`: grammar terms you derive yourself (suffix and augment names such as śānac, num, aṭ) are written in plain Latin letters, never as a segment. **Never type Devanagari or IAST** — scripts make them (and the accents).
- Do not write a Progress note. Do not repeat or rewrite anything shown under "Context".
- A sentence that started on the previous page: read the context lines and complete it; a sentence cut at the end of the window: translate what is there and say it continues.

## Rules that are never bent
- The supplied text is the base. **Never correct a letter or number from memory.** Odd word, misprint, wrong number → keep it and add a short italic note `*[as supplied: …]*`. A place that cannot be settled → `[?]` in kn.md **and** en.md, then `done … --max-doubts K`.
- Where the print gives no number, write none. References as in kn.md, in Latin digits. Reference abbreviations already corrected by script: write `Ni.`, `Ṛ. Saṃ.`, `Ai. Brā.`; any other odd abbreviation: keep as supplied and list it in your report.
- Sanskrit is quoted in full, never summarised. Nothing is dropped: stray lines stay as italic notes (the script already wrapped the usual ones).
- Running heads: ಮಂ. Maṇḍala · ಅ. between ಮಂ. and ಸೂ. Anuvāka · ಸೂ. Sūkta · other side ಅ./ಅ./ವ. Aṣṭaka/Adhyāya/Varga.

## What the QA of Vol 12 found (72 pages read against the Kannada: about one real error in four pages) — avoid these
- **Do not translate a Sanskrit quotation that the Kannada does not translate.** Quote it; render only the Kannada's own explanation. No English gloss in parentheses after a Sanskrit word unless the Kannada gives one.
- **Never read a misprint as the "obvious" word silently.** Translate what is printed, or give your reading with `*[as supplied: "ಕನ್ನಡ ಪದ"; read here as …]*`. A full stop in the wrong place, a missing headword, a number that does not add up: keep and note.
- **Only Sanskrit goes inside `⟦ ⟧`.** A Kannada gloss word or a misprinted Kannada word is translated; if it must be shown, it stands in Kannada letters inside an italic note.
- Quote Sanskrit to its end: the last words, the printed abridgement dots `.... ....` and the closing danda belong to the quotation; a Sanskrit phrase such as `ಇತಿ ಚ ಬ್ರಾಹ್ಮಣಂ` is quoted, not turned into English.
- Check who does what before writing a sentence with two actors (who helps whom, whose attribute it is); technical terms exactly (ādyudātta is not anudātta, a sautra root is not "Saura"). The Gist follows Sāyaṇa's Sanskrit, not the Kannada gloss, where they differ (and says so).

## kn.md (made by script; check it, do not retype it)
The script has already: standardised and inserted section labels (garbled ones kept as `*[…]*`), joined line-end hyphens, wrapped stray lines, inserted markers for missed running heads, rewritten Devanagari letters as Kannada. TASK.md lists what it did. If something is still wrong (prose inside a `> ` block or the reverse, a label in the wrong place), repair it with `python3 tools/rv/batch.py fix VOL WIN kn "OLD" "NEW"` (exact, unique; letters unchanged) and look at the new block numbers with `batch.py view VOL WIN`.
`[figure: …jpg]` line (handle it BEFORE the first `done`, which refuses a leftover figure line): look at the picture (Read tool); if it only repeats a Saṃhitā/Pada block that kn.md already has as text, remove the line with `batch.py fix` and say so in an italic note; otherwise write the verse block it holds into kn.md letter by letter in Kannada script, `[?]` for unsettled letters, remove the figure line, and say in an italic note in en.md that the block was read from the picture. Small hook/division marks in a picture's Pada line are not transcribed.
If you made the same hand-fix a third time, say "recurring: …" in the report: it becomes a script change.
