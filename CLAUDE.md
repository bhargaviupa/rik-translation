# Rigveda Samhita Translation — Volumes 1–3 (Volume 3 in progress)

Translating a 1949 Kannada commentary on the Rigveda (Sayana's Sanskrit bhashya + Kannada
explanation by H. P. Venkata Rao) into English. Volume 1 (complete — `Rigveda_Samhita_Vol1_English_Translation.md`) covered the
front-matter plus Suktas 1–2 of Mandala 1; Volume 2 (complete — `Rigveda_Samhita_Vol2_English_Translation.md`) covered Suktas 3–19
(the First Adhyaya of the First Ashtaka). **Volume 3** covers Mandala 1, **Suktas 20–32** (the Second Adhyaya of the First Ashtaka).

**Current source file:** `Rig_Vol3.pdf` (663 pages, scanned; contents list in the header of the output file).
**Current output file:** `Rigveda_Samhita_Vol3_English_Translation.md` — append-only; never rewrite earlier sections.
Volumes 1–2 files are closed; do not edit them.

## Current position

Volume 3 translation is under way: **Sūkta 20 ("ayaṃ devāya janmane", to the Ṛbhus; eight Riks) in progress — through printed page 37, Riks 1–7 done.**
**Next task: continue Sūkta 20 at Rik 8 (the last rik), at the head of printed p. 38 (PDF page 53).** Sūktas and their first
pages: 20 p.1; 21 p.43; 22 p.63; 23 p.141; 24 p.234; 25 p.295; 26 p.345; 27 p.374; 28 p.408; 29 p.438; 30 ~p.447; 31 p.517; 32 p.587; the volume
ends about printed p. 648. The tail of the output file has the progress note and the open flags — read the last ~40 lines before starting any new batch.

**PDF-to-printed-page offset (Volume 3): printed page = PDF page − 15.** (Same as Volume 2.) The first printed page is PDF page 16, the heading
page of Sūkta 20.

## Starting the next volume (Volume 3 and later)

Volumes 1–2 are closed. When the user supplies the next volume (after Volume 3)'s PDF:

1. **Confirm the basics first, before translating:** the PDF filename, its page count, the PDF-to-printed-page offset (view the first
   pages: title page, preface, contents), and which sūktas/maṇḍala it covers (from its own table of contents). Then replace
   "Source file / Output file" and "Current position" above with the new volume's values, and keep the Volume 2 files untouched.
2. **New output file per volume**, e.g. `Rigveda_Samhita_Vol3_English_Translation.md`, append-only, with its own single trailing progress note.
   Open it with a short header stating the volume, the source PDF, the first sūkta, and that conventions are carried over from Volumes 1–2.
3. **All conventions in this file carry over unchanged** (three-layer Sanskrit, view each page before writing, [?] for doubtful readings and
   numerals, the source's own English reproduced with [sic], grammar pages noted briefly). Re-check each new volume for changes in
   print (script of the bhāṣya, accent marks, header layout) and record any change here rather than assuming.
4. **Append-script safety (learned in Volume 2):** the helper that appends a section must (a) strip *only* the final "Progress note"
   block (assert it lies within the last few thousand characters), (b) assert the file did not shrink, and (c) be followed by a check that
   the file ends in exactly one full progress note. Never run `git checkout`/restore on the output file mid-session; work on a copy if a
   repair is needed.
5. **One session per sūkta** remains the cost-saving rule; each fresh session starts by reading this file and the last ~40 lines of the
   current volume's output file.
6. **Docx:** rebuild with the pandoc command above and check the Devanagari count matches the .md, when the user asks (or at the end of each sūkta, as has been the practice).
7. **Carried-over unresolved items** (not blockers): old mid-file progress notes and a stray Cyrillic string in the Volume 2 file; varga numerals
   unreconciled with colophons; a known-limitations appendix and outside expert review still wanted for Volumes 1–2.

## Working pipeline, per page

1. Render the page: `pdftoppm -jpeg -r 150 -f <n> -l <n> Rig_Vol3.pdf /tmp/page` (adjust `<n>`
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
5. **Dense Vyakarana-prakriya (grammar) sections** (see "Cost-saving rules" below for the short-note form) may be characterized/summarized rather than
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

## Cost-saving rules (added after Sūkta 6; they override the slower habits above)

- **One session per sūkta.** Start a fresh session at each sūkta boundary; this file and the tail of the output file carry the position.
- **View each page once, then write immediately.** Never view a page in one turn and write it in a later one; never re-view a page already written.
- **Render at 150 dpi and zoom only where needed:** Rik texts (Saṃhitā/Pada), the Sāyaṇa-bhāṣya, and numeral tables/citations. Do **not** zoom grammar pages.
- **Grammar pages (Vyākaraṇa-prakriyā) get a short note, not an outline:** 2–4 lines naming the words treated and the sūtras cited (sūtras in three layers only where legible at 150 dpi; otherwise leave the number as [?]). Say explicitly "grammar page, noted briefly." Do not chase uncertain numerals on these pages. The Rik text, bhāṣya, Pratipadārtha, Bhāvārtha, English and Special Topics keep full treatment.
- **Batch writes:** append a whole Rik (or a whole 4–6 page run) in one call, not page by page.
- **Use a cheaper model for transcription if the user selects one;** any pass needing judgement on a doubtful reading should be flagged [?] rather than resolved by memory.

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

## Conventions added during Volume 2 (pp. 31–257)

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
- **Numeric tables** (e.g. the viṣṭuti/paryāya tables, pp. 144–148): read from enlarged slices, add up each row against the
  stated total, record any row that does not add up rather than adjusting it.
- **Closing notes** at the end of a sūkta ("illige … sūktavu samāptavu … vargavu mugidudu") are printed large and are
  more reliable than the small-numeral page headers for varga numbering; prefer them.
- **A helper script** that appends a section and a trailing "progress" stub must remove the previous stub first; check
  that the file ends in exactly one full progress note before committing.
