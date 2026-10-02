# Rigveda Samhita Translation — Volume 2

Translating a 1949 Kannada commentary on the Rigveda (Sayana's Sanskrit bhashya + Kannada
explanation by H. P. Venkata Rao) into English. This is a direct continuation of Volume 1
(already complete — see `Rigveda_Samhita_Vol1_English_Translation.md`), which covered the
front-matter (Purva-pithika + Sayana's Bhumika) plus Suktas 1–2 of Mandala 1. Volume 2 covers
Suktas 3–19 of the same Adhyaya (its title page undersells this as "Suktas 3–9"; the internal
table of contents confirms it runs through Sukta 19).

**Source file:** `Rig_Vol2.pdf` (823 pages, scanned).
**Output file:** `Rigveda_Samhita_Vol2_English_Translation.md` — append-only; never rewrite
earlier sections.

## Current position

Through **printed page 135**, which closes **Sūkta 4** of Maṇḍala 1 (ten Riks). **Next task:
begin Sūkta 5 ("ā tvetā ni ṣīdata") at printed page 136** (PDF page 151). The tail of the output
file has the progress note and the open flags — read the last ~40 lines before starting any new batch.

PDF-to-printed-page offset: page 1 of the printed text is PDF page 16 (there are 15 pages of
front matter — title pages, royal dedication, the translator's preface, and the table of
contents — before the Sanskrit commentary itself begins).

## Working pipeline, per page

1. Render the page: `pdftoppm -jpeg -r 150 -f <n> -l <n> Rig_Vol2.pdf /tmp/page` (adjust `<n>`
   for the PDF-vs-printed offset above).
2. **View the actual rendered image before writing anything.** Never pattern-complete Sanskrit
   from memory or rhythm, even for verses that look familiar — this was a caught near-miss
   during Volume 1 and must not recur.
3. Transcribe and translate following the conventions below.
4. Append to the output markdown — never edit or rewrite earlier content.
5. Replace the trailing progress-note block with a fresh one (see below).

## Core conventions (carried over from Volume 1, unchanged)

1. **Sanskrit — always three layers, no exceptions:** Devanagari + IAST transliteration +
   English translation, on every citation. Never two layers, never IAST alone. This was the
   single most costly failure mode in Volume 1 (one wrong sentence in an earlier brief caused
   ~120 pages with no Devanagari before it was caught) — treat it as non-negotiable.
2. **Take the Kannada source at face value** — no default cross-verification against outside
   sources, except standardized reference material (e.g. classical meter names), which is
   worth a quick check.
3. **Preserve all Sanskrit, complete or incomplete, and all cross-references.** Never skip,
   summarize, or silently omit a citation.
4. **Honesty about uncertainty, calibrated to content type:** full confidence for clear prose;
   bracketed "[?]" or italicized paraphrase for dense numeric/citation codes or heavily
   compressed commentary; never fabricate. Formatting confidence (bold, clean citation
   layout) must never exceed actual reading confidence — if genuinely unsure, hedge visibly
   rather than presenting a guess as a reading.
5. **Dense Vyakarana-prakriya (grammar) sections** may be characterized/summarized rather than
   transcribed line-by-line when they are pure technical derivation with no bearing on the
   established sense already given in the Bhashya/Pratipadartha — say so explicitly when doing
   this, rather than silently thinning the content.
6. **No docx generation mid-stream** — only when explicitly asked. When needed:
   ```
   pandoc "Rigveda_Samhita_Vol2_English_Translation.md" -o "Rigveda_Samhita_Vol2_English_Translation.docx" \
     --toc --toc-depth=2 -V geometry:margin=1in -V mainfont="Noto Serif Devanagari"
   ```
   Verify with a LibreOffice PDF conversion + Devanagari character count
   (`grep -c` on Unicode range `\u0900-\u097F`), not just a page count.
7. **Scanning duplications occurred repeatedly in Volume 1's source** (same printed page
   number appearing twice due to scan errors). Check the printed page number visible on each
   newly rendered page against what was just translated; if it repeats, skip and note it.
8. **Progress-note pattern:** a running block at the very end of the .md file — exact
   printed page reached, one-line summary of what the batch covered, open flags. Each new
   note **replaces** the previous one at the tail; it does not accumulate. Anything meant to
   persist long-term belongs in this CLAUDE.md file instead, not just the progress note.
9. **Batch size:** work in reasonably large batches (10+ pages) rather than one page at a
   time, consistent with how Volume 2 has been paced so far — but accuracy always wins over
   speed; never skim the source image to go faster.

## Open items carried from Volume 1 (not yet resolved, revisit if relevant)

- Only one source diagram was ever extracted as an actual image (a lineage chart, Vol. 1
  p.48); other genealogies were rendered as text/bullets instead.
- Vol. 1 still needs an outside Vedic/Sanskrit expert review before being considered final.
- A handful of Vol. 1 chapter headings carry unresolved bracketed numbers needing a check
  against the source's own table of contents.
- Roughly 59 places in Vol. 1 are self-flagged as best-effort/illegible — worth a compiled
  "known limitations" appendix eventually.

Full detail on all of the above lives in `Translation_Conventions_Handoff.md`, included in
this repo — read it if any of these come up.

## Conventions added during Volume 2 (pp. 31–135)

- **The Sanskrit bhāṣya is printed in Kannada script** in this part of the source (the Saṃhitā
  and Pada texts too). Convert letter by letter to Devanagari + IAST; never complete a garbled
  word from memory — bracket it with [?]. A clearer later printing of the same phrase may be
  used to correct an earlier reading (say so in the text).
- **Kannada-script numerals** (references, counts, sūtra numbers) are the least reliable part
  of the scan. Zoom (`pdftoppm -r 240+ -x -y -W -H`) before trusting them, and mark any digit
  not certain with [?]. Sūtra numbers that match a known Pāṇini/Phiṭ/Uṇādi rule are worth a
  quick standard-reference check; say when you have done so.
- **Page headers:** even pages carry "Maṇḍala 1, Anuvāka 1, Sūkta N" on the right; odd pages
  carry "Aṣṭaka 1, Adhyāya 1, Varga N" on the left. (Varga 5 ended at p. 46; Varga 6 began p. 47.)
- **Accent-marks** on the Saṃhitā/Pada texts are *not* reproduced from Rik 3.5 onward (the
  Kannada notation could not be converted reliably); Riks 3.1–3.4 do carry them. Keep the
  inconsistency noted rather than guessing.
- **The source prints its own English translation of each Rik** (and English quotations of
  Western scholars). Reproduce it as printed, including misprints, marked [sic].
- **Grammar pages** (Vyākaraṇa-prakriyā): characterize rather than transcribe line by line, say
  so explicitly, and keep every cited sūtra in all three layers.
- Glosses I add to Ṛg-vedic citations that the source leaves untranslated must be labelled as
  mine and tentative where the text is uncertain.
- **Large grammar pages** (pp. 98–99, 106–107, 119–120, 133–135 and similar) are scholastic argument over
  accent and sandhi, not sense: characterize them in outline, keep every named sūtra in three layers,
  and say plainly which stretches of the print were too crowded to reproduce.
- **Page headers** keep the pattern above; their small Kannada numerals (varga numbers especially) are
  unreliable — record what is read with [?] and do not "fix" a mismatch silently.
