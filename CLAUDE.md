# Rigveda Samhita Translation — Volumes 1–5 complete (Volume 6 in progress: Sūktas 62–74 done)

Translating a 1949 Kannada commentary on the Rigveda (Sayana's Sanskrit bhashya + Kannada
explanation by H. P. Venkata Rao) into English. Volume 1 (complete — `Rigveda_Samhita_Vol1_English_Translation.md`) covered the
front-matter plus Suktas 1–2 of Mandala 1; Volume 2 (complete) covered Suktas 3–19; Volume 3 (complete) covered Suktas 20–32;
Volume 4 (complete — `Rigveda_Samhita_Vol4_English_Translation.md`, `.docx` rebuilt) covered Suktas 33–46 (the Third Adhyaya).
**Volume 5** covers Mandala 1, **Suktas 47–61** (the Fourth Adhyaya of the First Ashtaka). **Volume 6** (`Rig_Vol6.pdf`, 638 PDF pages; Sūktas 62–80, the Fifth Adhyāya) is set up in `Rigveda_Samhita_Vol6_English_Translation.md` (printed page = PDF − 18); its tail carries the progress note.

**Current source file:** `Rig_Vol5.pdf` (724 pages, scanned; contents table in the header of the output file).
**Current output file:** `Rigveda_Samhita_Vol5_English_Translation.md` — append-only; never rewrite earlier sections.
Volumes 1–4 files are closed; do not edit them. (`Rig_Vol1(1).pdf`, `Rig_Vol1(2).pdf` are extra Volume 1 scans added by the user; not in use.)

## Current position

**Volume 5 is COMPLETE, including the Pariśiṣṭa:** Sūktas 47–61 (printed pp. 1–529 = PDF 17–545, with the Fourth Adhyāya's closing colophon on p. 529; p. 530 blank) and the Kannada Pariśiṣṭa on the deities and persons of the Ṛgveda (printed pp. 531–708 = PDF 547–724; translated at the user's request, appended to the same file). Output: `Rigveda_Samhita_Vol5_English_Translation.md` (+ `.docx`). Its tail carries a final progress note with the open [?] flags. The file header still says the Pariśiṣṭa is not translated: that is out of date (append-only file). Pariśiṣṭa conventions: plain English rendering page by page (printed page marked), Sanskrit in three layers, the small Kannada reference numerals given as read and unverified ("?" where illegible). Confirmed sūkta starts (printed pp.): 48→30, 49→91, 50→106, 51→147, 52→212, 53→264, 54→303, 55→341, 56→371, 57→392, 58→411, 59→439, 60→461, 61→478.
**Current job — Volume 6 in progress:** source `Rig_Vol6.pdf` (638 PDF pages; printed page = PDF − 18), output `Rigveda_Samhita_Vol6_English_Translation.md` (append-only, one trailing progress note). **Sūktas 62–74 are complete** (printed pp. 1–454); **Sūkta 75** (five Ṛks, Gāyatrī, ṛṣi Gotama Rāhūgaṇa, second sūkta of Anuvāka 13) is begun on pp. 454–455 (introduction and Rik 75.1 up to the bhāṣya's tail); **next: printed p. 456 (PDF 474)**. Sūktas 65–70 are *dvaipada* (Dvipadā Virāṭ): two half-Ṛks are printed joined as one four-pāda Ṛk ("1 || 2 ||"); follow the print's numbering. Sūktas 71–73 are ordinary ten-Ṛk Triṣṭup hymns to Agni (ṛṣi Parāśara Śākti). Lesson: when a Special Topics passage runs across a page break, split it where the print splits it (a merged-page draft had to be corrected twice). Working method: batches of 3 pages, view each page before writing, commit and push each batch to `claude/modest-ptolemy-9efv8s` (helper: strip only the trailing "**Progress note:**" within the last ~2,500 characters, append the section, assert exactly one note). No PR and no docx/PDF rebuild unless the user asks. The Volume 5 .docx must be rebuilt (pandoc command below) after any edit to that file. The scheduled routines are paused. The branch was merged to `main` once (PR #1, Sūktas 47–61); the Pariśiṣṭa and Volume 6 work are on the branch after that merge and not yet on `main`.
Lessons from Volume 5: keep Vyākaraṇa notes short and name only legible sūtras; a sūkta may end with only the grammar paragraph; the last sūkta of an adhyāya is followed by a Sanskrit colophon and a Kannada closing line (transcribe in three layers); an appendix of continuous prose can be done 4 pages per batch with a short progress note after each batch.

**PDF-to-printed-page offset (Volume 5): printed page = PDF page − 16.** (Volume 4: − 14; Volumes 2–3: − 15.) Printed p. 1 is PDF 17 (title of the Fourth Adhyāya
and Sāyaṇa's introduction); the heading of Sūkta 47 is on printed p. 2 (PDF 18). Page headers are as before ("Maṇḍala 1, Aṣṭaka 1, Adhyāya 3, Varga N").
Re-check the offset at the start of the next volume rather than assuming it.

**Lessons from Sūkta 33 (add to the working habits):** (a) the Pada-pāṭha is printed *after* the Saṃhitā on the next page: do not write a reading note on
word-division under the Saṃhitā until the Pada has been viewed; (b) never supply sūtra numbers from memory: give a number only where it was read in the
print, mark the rest [?]; (c) the bhāṣya's own grammatical tail (after the main sense) and the separate Vyākaraṇa-prakriyā pages are both characterized, not
transcribed; (d) a small helper that strips the single trailing "Progress note" and appends a section, run with the section and note as files, worked well
(strip only within the last ~6000 characters; assert exactly one note afterwards); (e) Ṛgveda citations in the Special Topics are left untranslated by
the source: transcribe in three layers, give a short gloss labelled "mine and tentative", mark every reference numeral [?].

## Starting the next volume (Volume 5 and later)

Volumes 1–3 are closed. When the user supplies the next volume (after Volume 4)'s PDF:

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

## Publication build (print PDF) — added after the translation was complete

Goal: publish Volumes 1–5 as print-ready PDFs, **one volume at a time**. The closed translation `.md` files are never edited; `publish/build.py` reads them and writes `publish/out/volN_full.pdf` (+ `.html`).
- Run: `cd publish && python3 build.py <vol> full` (≈1m45s for Vol 3; `pilot` builds front matter + first Sūkta). Needs `pip install pypandoc_binary weasyprint` and `apt-get install fonts-noto-core` (Noto Serif / Devanagari / Kannada).
- Design (approved by the author): 6.5×9.5 in page, running heads (book title left / Sūkta right), roman folios for front matter then Arabic from the first Sūkta, each Sūkta opens on a right-hand page, Rik-wise contents with page numbers, translator's remarks as per-Sūkta numbered footnotes plus a "Collected Notes" appendix (numbers match). Remarks longer than 900 characters stay on the page as small-type "Note —" blocks (marked ¶ in the appendix). Inline `[?]` marks stay in the text.
- Front matter: original cover (assets/cover_volN.jpg), title page (English translation by Bhargavi Upadhya, prepared with the assistance of Claude), copyright page (© 2026 Bhargavi Upadhya for the English), 1949 Maharaja and Guruji portraits (assets/maharaja.jpg, guruji.jpg — low resolution), one page reserved for the present Maharaja and Guruji (photos, names and captions still to be supplied), contents.
- Lessons: a heading must start its own block (source headings sometimes follow a line with no blank line); never put note text inside pandoc `^[...]` (unbalanced brackets swallow headings) — use placeholder tokens; bold-wrapped `**(…)**` Sanskrit is not a note.
- Status: Vol 3 built (799 pp.); Vol 1 built (1,249 pp. — now complete: the four portions the draft had skipped, printed pp. 95–167, 191–205, 261–283 and 288–295, are translated in `Rigveda_Samhita_Vol1_Gaps_English_Translation.md` and inserted in place of the former edition notices by `vol1_clean.load_gap`; chapters renumbered to the original contents table (draft "Fourteen" = 16, "Fifteen?" = 17, "Seventeen" = 18, "Eighteen" = 19, "Nineteen" = 20). In the rishi index the Kannada-numeral hymn references are not reproduced (names and bracketed verse-counts only); Jaiminīya and per-prapāṭhaka tables on pp. 117–118, 138–139, 150–151 are likewise not reproduced — all noted in the text) with its own pipeline: `python3 publish/build_vol1.py full` (calls `publish/vol1_clean.py`, which strips the working draft — progress messages, 'to be continued', QA logs, session summaries — logs every change to `publish/work/vol1_audit.md`, and writes `publish/work/vol1_clean.md`; page headings become 'original p. N' markers; skipped portions become boxed 'Editorial notice' blocks; the unfinished mantra index is dropped with a notice). Vol 2 built (1,221 pp.) with `python3 publish/build_vol2.py full` (uses `publish/vol2_clean.py`, audit in `publish/work/vol2_audit.md`; Rik starts are detected from heading text and checked against the expected Rik count of each Sūkta). Vols 4 (872 pp.) and 5 (1,031 pp. incl. Pariśiṣṭa) built with `python3 publish/build_vol45.py 4|5 full` (cleaner `publish/vol45_clean.py`; Rik counts verified per Sūkta — Vol 4 against the author's tallies, Vol 5 against the standard counts, Sūkta 59 has 7 per the source). All five PDFs are in `publish/out/volN_full.pdf`. Still to do: present-day portraits; first-person wording in notes is now rewritten impersonally at build time by `publish/voice.py` (author's choice; sample in `publish/work/voice_sample.md`; for a new volume run the build, then `voice.residual()` on its notes and add any new phrases to `voice.EXACT`); outside expert review of the ~9,000 `[?]` readings.
