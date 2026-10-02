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

Through **printed page 30** of the source. Just finished the full apparatus for Rik 3.3
(closing the three-verse Ashvin group) and opened Rik 3.4, the first verse of the sukta's
Indra group (mantras 4–6). **Next task: Sayana's commentary on Rik 3.4, starting printed
page 31.** The tail of the output file has the exact stopping point and a running progress
note — read the last ~80 lines before starting any new batch.

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
