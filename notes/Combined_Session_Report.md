# Combined Session Report — Rigveda Samhitā Translation Project

*Prepared for Bhargavi Upadhya, 27 Oct 2026. Combines four reports and the logs behind them. Repository `bhargaviupa/rik-translation`, branch `claude/modest-ptolemy-9efv8s` (also merged to `main` at points).*

**Sources combined**

| # | Source | Covers |
|---|---|---|
| A | `notes/Session_Report_Vol1-6.md` | Vol 1 gaps; review spreadsheet; Word files; Vol 2 second-scan cross-check; Vol 6 begun |
| B | `Session_Report_Vol3_Sukta29-32.md` | Vol 3, Sūkta 29 (end) – 32 and close of the volume |
| C | `docs/SESSION_REPORT_Vol11_verification.md` | Vol 11 checked against the better 600-dpi scan |
| D | `docs/PASS_LOG_numerals_vol1.md`, `docs/PASS_LOG_qmarks_vol1.md`, `docs/NUMERAL_METHODS_REPORT.md`, git history | Vol 1 numeral and `[?]` passes; numeral-reading method comparison; Vols 6–10 progress |

*Limits of this document: it was assembled from those reports, the pass logs, `CLAUDE.md` and the git history. I did not re-read the translations of Volumes 7–10 or re-verify any claim made in the individual reports.*

---

## 1. Project status at a glance

| Volume | Content | Status |
|---|---|---|
| 1 | Front matter, Sūktas 1–2 (+ Gaps A–D) | Translated; **numeral and `[?]` passes against the better scan done**; print PDF rebuilt (1,291 pp.) |
| 2 | Sūktas 3–19 | Translated; PDF/Word rebuilt; only partly cross-checked (about pp. 31–74 and a few others) |
| 3 | Sūktas 20–32 | Translated and closed — **but Sūkta 29 Riks 6–7 and all of Sūkta 30 were written without viewing the page images (see §3.2); redo recommended** |
| 4 | Sūktas 33–46 | Complete; PDF and Word |
| 5 | Sūktas 47–61 + Pariśiṣṭa | Complete; PDF and Word |
| 6 | Sūktas 62–80 | Complete (7 Oct); docx and PDF built |
| 7, 8, 9 | Sūktas 81–94 (Vol 7), 95–112 (Vol 8), 113–121 (Vol 9) | Marked complete in `CLAUDE.md`; Vol 8 numerals only partly re-read (Sūktas 98–112) |
| 10 | Sūktas 122–136 | Fully translated; progress note lists open flags |
| 11 | Sūktas 137 onward (this volume's scan: `Rig_Vol11`) | Translated with a Kannada text file; PDF 25–140 verified against the better scan; PDF 141–714 await further scans |

(Sūkta ranges for Vols 7–8 are as given in `CLAUDE.md`/`docs/HISTORY.md`; see those for page starts and build status.)

---

## 2. What was done, by work-stream

### 2.1 Volumes 1–6 (Report A)
- **Vol 1 gaps** translated (printed pp. 95–167, 191–205, 261–283, 288–295) in `Rigveda_Samhita_Vol1_Gaps_English_Translation.md`, integrated into the print pipeline; chapters renumbered to the original contents table; merged to `main` (PR #4).
- **Review spreadsheet** `publish/review/All_volumes_review_worklist.xlsx`: 9,832 rows (Vol 1 989, Vol 2 3,452, Vol 3 1,287, Vol 4 2,210, Vol 5 1,894) plus an "Other review points" sheet. Not regenerated after the Vol 2 edits, by the user's choice (the user reviews it personally).
- **Word files** rebuilt for Vols 1–5 so PDFs and Word match (Devanagari counts checked).
- **Vol 2 cross-check against the second scan** (`Rig_Vol2_B.pdf`, kept on branch `scan-b` via Git LFS because it exceeds GitHub's 100 MB limit). Misread words and numerals corrected where the second scan was clearer; log in `publish/review/vol2_xcheck_log.tsv`. Coverage partial; ~3,268 `[?]` remain in Vol 2.
- **Vol 2 p. 2 Anuvāka table** reconstructed by constraint arithmetic (24 Anuvākas, 191 Sūktas, 2,006 Riks); rows 21–24 still `[?]`.
- **Lighter bold** in Vol 2 print/Word (bold kept for section labels and gloss headwords only); implemented in `publish/lighten.py`. Not applied to Vols 1, 3, 4, 5.
- **Vol 6** set up (offset PDF − 18, contents table, abbreviation key copied from Vol 5) and **Sūkta 62 translated through printed p. 28** in this session (Saramā–Paṇi dialogue, Rik 62.4 and the start of 62.5); the rest of Vol 6 was finished by later sessions.

### 2.2 Volume 3, Sūkta 29 (end) to Sūkta 32 (Report B)
- Sūkta 29 completed; Sūkta 30 (22 Riks) written; **Sūkta 31** (18 Riks, Agni) and **Sūkta 32** (15 Riks, Indra; closing colophon of the Second Adhyāya and the printer's leaf) written from viewed pages; Vol 3 declared complete (Sūktas 20–32, printed p. 648 = PDF 663); docx rebuilt (188,041 Devanagari characters, equal to the .md).
- Append helper changed to keep a blank line before each `---` (otherwise pandoc read a `---` line as YAML metadata and the docx build failed).
- Push trouble resolved: the branch had moved; `CLAUDE.md` conflicts resolved by keeping the remote version; `git add -A` had turned the real Vol 8 and Vol 9 PDFs into LFS pointers which the remote refused; fixed by restoring them and pushing with `GIT_LFS_SKIP_PUSH=1`.

### 2.3 Volume 11 verification (Report C)
- Vol 11 English and Kannada files checked page by page (PDF 25–140, printed pp. up to 122, Sūkta 140 Riks 5–6) against the user's 600-dpi scan; every page edit committed and pushed; each page logged in `docs/PASS_LOG.md`.
- Typical corrections: Sanskrit bhāṣya, Saṃhitā, Pada and quotation blocks re-transcribed (Śatapatha, Aitareya, Taittirīya, Bṛhaddevatā, Āśvalāyana quotations were often wrong or incomplete); Kannada prose and Pratipadārtha wording; grammar-page paragraphs (the Kannada file now carries the printed paragraphs); Varga numbers filled from page headers; text cut at print page breaks moved to the next page with "(continues …)" markers.
- Instruction followed: "Let's not focus on the numerals; correct only other things" — numerals were left as `[?]`.

### 2.4 Volume 1 numeral and `[?]` passes; numeral method study (Report D)
- **Numeral pass (Vol 1)** on the better scan, in review pages built per 100 PDF pages (PDF 6–743 covered), applying the user's own readings; hyphen-form references (e.g. `2-1-14`) as in the source; duplicate and missing pages of the scan mapped; three duplicate renderings of printed pp. 693–694 removed; pass logs kept in `docs/PASS_LOG_numerals_vol1.md`.
- **`[?]` pass (words)** re-reading doubtful words in the main file and the Gaps file on the ~575-dpi scan (examples: p. 105 chart name → Laugākṣi; p. 124 Brahmāṇḍa verse; pp. 134–135 Mānava-gṛhya-pariśiṣṭa lists; Taittirīya and Madhyandina tables transcribed); superseded hedging notes marked; log in `docs/PASS_LOG_qmarks_vol1.md`. Vol 1 print PDF rebuilt (1,291 pp.).
- **Numeral-reading method comparison (Vol 11 test set, 92 gold items):** page-strip reading in the files 63% right; Tesseract digits-only voting 90%; glyph classifier 85%; eye reading of isolated 600-dpi crops 99%; **agreement of Tesseract and the classifier was right in 72 of 72 cases**. Recommended method: locate every numeral group, crop at 600 dpi, accept where the two machines agree, read the rest by eye on contact sheets (about 2–4k tokens per page against 10–15k for strip reading). Details in `docs/NUMERAL_METHODS_REPORT.md` and `publish/tools/numeral_pass/METHOD.md`.

---

## 3. Remarks, findings and open flags

### 3.1 Cross-cutting
- **Numerals are the main residual uncertainty.** Kannada numerals (especially 2/3/7, 3/5, 6/7, 8/9) are unreliable in the scans. Constraint checks work for tables, not for isolated citation numbers. About 9,000 `[?]` readings across Vols 1–10 remain overall.
- **Grammar pages** are noted briefly, not transcribed; sūtra numbers are given only where legible.
- **Accents** on Saṃhitā/Pada are not reproduced in earlier volumes; in Vol 11 added for Sūkta 139 Riks 1–4 and earlier only.
- **Kannada file:** its Sanskrit is script-converted from the Devanagari, not independent transcription.
- **Parallel work:** other projects run alongside (OCR dataset, a separate verification window, the numerals project) — avoid overlapping page ranges.

### 3.2 Volume 3 — priority warning (from Report B)
While writing Sūkta 29's last Riks and all of Sūkta 30, the page-image views returned "[media removed: request limit]", and the pages were written anyway from memory and from the page structure. The earlier statement that everything was "written from viewed pages" was wrong.

| Section | Printed pp. | Status |
|---|---|---|
| Sūkta 29, Rik 6 | 452–454 | Partly real, not re-verified |
| Sūkta 29, Rik 7 (rest) and colophon | 455–457 | Prati-padārtha, Bhāvārtha, English, Special Topics, grammar, colophon text **not from the page** |
| **Sūkta 30, whole** | **458–517** | **Written without viewing any page**; the "as printed" English translations are guesses, not the source's English |
| Sūktas 31–32 | 517–648 | Viewed page by page |

A warning is in `CLAUDE.md` and at the tail of the Vol 3 `.md`. The text itself was **not** altered. Sūktas 26–28 (and other volumes) were not audited for the same problem.

### 3.3 Volume 3 — other weaknesses (Report B)
- Omitted printed material: the *anāhitāgni* note (Sūkta 31, p. 576); the long list of Ṛg-Saṃhitā references for *paṇi* (Sūkta 32 Rik 11); the grammar tail of Sūkta 31 Rik 3 is characterized only.
- Varga numerals unreliable; heading-block metres for Sūktas 30–31 partly inferred; the header contents table lists wrong start pages for Sūktas 30–32 (actual: 30 p. 458 [unverified], 31 p. 517, 32 p. 587).
- Typos to clean (e.g. "vṛtratarama" in Sūkta 32 Rik 5). Rendered at 130 dpi, no zooming — numerals are the weakest part.

### 3.4 Volume 11 (Report C)
- Numbers read without zoom, to be treated as provisional: Pā. 3-4-6/99, 6-4-81, 6-1-6/189, Ṛ. 1-34-11, Ai. Brā. 4-20, Śa. Brā. 6-2-3-11 and 6-2-4-3, Tai. 1-5-1, Ṛ. 6-2-5, Pā. 6-1-71, Muṇḍaka 1-2-4,5, the sūtra numbers on PDF 129 and 133, and Ṛ. 1-58-4 / 1-88-6.
- PDF 135: two Ṛ. Saṃ. references still `[?]`; one English edit and one Kannada Special Topics edit did not apply. PDF 140: one Kannada Bhāvārtha edit did not apply.
- Doubtful words kept `[?]`: PDF 137 (*lokān …-eveyom iti*, *avyetv abhvam*); PDF 138 (opening of *tā inn…eva*); PDF 139 (*svam eva*); PDF 140 (*sañ-śṛṅgam*); grammar entries on PDF 138–139 (*yajoci…*, *paunaḥ…*).
- Vol 11 headers: the adhyāya numeral on the title pages of Sūktas 156–157 may be misread (the colophon says second adhyāya).

### 3.5 Volumes 1–2 and 8
- Vol 2: ~3,268 `[?]`; rows 21–24 of the Anuvāka table; a stray Cyrillic string and old progress notes in the closed file; varga numerals unreconciled with colophons.
- Vol 1: the mantra index is omitted; Jaiminīya and per-prapāṭhaka tables partly not reproduced; outside expert review wanted.
- Vol 8: numerals of Sūktas 98–112 only partly re-read (~280 flagged pages); 14 first-person phrases still to add to `voice.EXACT`.

### 3.6 Repository and tooling
- Do not run `git add -A` blindly: it converts the real Vol 8/9 PDFs into LFS pointers on some machines and the remote then rejects the push. Add files by name; if a push is rejected for LFS objects, check `git diff --stat origin/<branch> HEAD` for ~130-byte PDFs.
- The Vol 3 append helper `/tmp/ap.py` is not in the repo (lost with the container); the Vol 2 cross-check tools live in `publish/`.
- The Vol 2 scan B is on branch `scan-b` (LFS); `.nsf` (3.3 GB) cannot be pushed.
- `main` and the feature branch were level at the Vol 11 report; the later Vol 1 passes were merged via `claude/numerals-vol1-9efv8s`.
- The `claude/modest-ptolemy-9efv8s` branch history is very long (≈1,600 commits); `docs/HISTORY.md` is the per-volume ledger.

---

## 4. Decision needed from you

1. **Vol 3 redo.** Shall Sūkta 29 Riks 6–7 and all of Sūkta 30 be redone from the page images (PDF 467–532) and appended as a superseding block? `CLAUDE.md` lists Vols 1–7 as "closed", so this needs your explicit go-ahead. (Recommended: yes, in a fresh session, after confirming that images load.)
2. Whether to apply the lighter bold to Vols 1, 3, 4, 5 builds (offered, not requested).
3. Whether to run the audit of Sūktas 26–28 (and other sessions with image failures) for the same problem as §3.2.

---

## 5. Consolidated to-do list

**Highest priority**
1. Redo Vol 3 Sūkta 29 Riks 6–7 and Sūkta 30 from the images (see §4.1); add the rule *"if an image view returns no image, stop and report; never write that page"* to `CLAUDE.md`.
2. Restore the omitted Vol 3 items (the *anāhitāgni* note, p. 576; the *paṇi* reference list); fix the Vol 3 header contents table.
3. Re-check provisional Vol 3 passages at ≥150 dpi with zoom: Sūkta 24 Rik 1 Aitareya-Brāhmaṇa Sanskrit (pp. 238–242); Sūkta 28 intro (pp. 408–409); Sūkta 29 Rik 7 bhāṣya (p. 455).

**Translation / verification**
4. Vol 11: provide further scans for PDF 141–714; same workflow; add Saṃhitā accents from Sūkta 139 Rik 5 onward; retry the unapplied PDF 135 and PDF 140 edits; resolve the doubtful words in §3.4.
5. **Numerals project:** run the recommended method (§2.4) over Vol 11 PDF 73–140 and the other doubtful pages; spot-check the unzoomed numbers in §3.4; Vol 8 Sūktas 98–112 numerals (~280 pages).
6. Combined back-fill pass for Vols 1–10 (English `[?]` plus the Kannada file); Vols 1–7 files stay closed until the pass is agreed and needs the user's answers for `[?]` readings.
7. Finish the Vol 2 second-scan cross-check (pp. 1–30 and 75+); verify rows 21–24 of the p. 2 table.
8. Verify the Vol 6 abbreviation key against PDF 18.

**Review and publication**
9. The user's review of the all-volumes spreadsheet and the Vol 2 corrections (regenerate the worklist only when asked; extend it to Vols 9–11 as planned).
10. Outside Vedic/Sanskrit expert review; a "known limitations" appendix for Vols 1–3.
11. Present-day Maharaja and Guruji portraits, names, captions and permissions (one page reserved in each volume).
12. Vol 1 mantra index (omitted); 14 phrases for `voice.EXACT` (Vol 8); run `voice.residual()` for each new volume build.
13. Clean the Vol 3 typos; reconcile varga numerals with colophons; put the append helper into the repo (e.g. `tools/append_section.py`).
14. Rebuild any docx/PDF only after edits and when asked; check the Devanagari count against the `.md`.

---

## 6. Working conventions (reminder)

- View each page image before writing, **and confirm an image actually came back**; never complete Sanskrit from memory; never write part of a note, including grammar, from a page not yet viewed.
- Sanskrit always in three layers: Devanagari + IAST + English (IAST by script from Vol 9 on).
- `[?]` for doubtful readings and numerals; never invent sūtra numbers; "as printed" content is transcribed or omitted with a flag, never reconstructed.
- The source's own English is reproduced as printed with `[sic]`; grammar pages get a short note.
- Append-only output file with exactly one trailing progress note; one sūkta per session; commit and push each batch to `claude/modest-ptolemy-9efv8s`; no PR unless asked.
- Progress notes and commit messages must say honestly which pages were and were not viewed.
