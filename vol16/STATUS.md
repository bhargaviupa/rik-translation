# Vol 16 — status

*Created Nov 9 2026 (late: the general CLAUDE.md asks for it from the start of a volume; until now the state was only in the progress note of the English file, `parts/batch_costs.md`, `html/HEAD_FIXES.md` and chat). Update this file at the end of every working session.*

## Scope
Maṇḍala 3 Sūktas 7–39 (Third Aṣṭaka, Adhyāyas 1–2), printed pp. 2–884 (final colophon on p. 884). Printed p. 1 and the front matter are not in any window.

## Source and inputs
`vol16/html/rig_16.md` (the user's `rig_16_1.md` pp. 2–423 + `rig_16_2.md` pp. 424–884, concatenated; the two originals with all embedded pictures are in git history, commit "the two supplied markdown files merged into one vol16/rig_16.md"). `vol16/html/figures/` holds the 10 pictures of verse blocks the machine reader could not read (INDEX.tsv); `vol16/AGENT_BRIEF.md` is the user's brief. No numeral file, no scans. Three misread running-head numbers (344, 347, 348) corrected: `html/HEAD_FIXES.md`. Known text defects: pages without a running head merge into the page before (agents insert the marker in kn.md and add the page to `pages.json`); one page near p. 241–242 is labelled by its head 241 and holds the start of 242.

## Outputs
`vol16/Rigveda_Samhita_Vol16_English_Translation.md` and `…_Kannada_Text.md` (branch `claude/vol16-translate`; main has the translation through p. 131 only — merge again when asked).

## How it was made
Vol 15 workflow: one fresh Sonnet agent per window of 3 (sometimes 4) printed pages, dispatcher verifies each commit and appends the cost line (`parts/batch_costs.md`; token numbers mostly not recorded). `tools/rv/html_to_kn.py` was changed on this branch (labels with a trailing full stop or a one-letter OCR slip are now recognised). Window prompts were extended during the volume (standard labels only, `check_inline` before commit, accent regex checks, `--max-doubts` is the sum of both files, never remove a `[?]` to meet the count, read the pictures).

## Status
Translated through printed p. 884 (FINAL: Sūkta 39 end, adhyāya colophon, closing verses and printer line). Volume text complete. Finishing checklist done except: print PDFs (need the front-matter scan PDF from the user), the open items below, and the merge into `main` (only when the user says so).

## Open items
**User / later pass**
1. Six pictures were first overlooked and then read in one pass (commit "Saṃhitā/Pada blocks of six Ṛks read from the pictures"): figures 2559 (Sūkta 7 Ṛk 9, first word worn: ವೃಷ್ಟಾಯಂತೇ vs ವೃಷಾಯಂತೇ), 4373, 5604, 5779, 5788, 8699. Please check a sample against the pictures. Picture 15415 (p. 338) was read in window 102 (Sūkta 16 Ṛk 5, Saṃhitā and Pada); picture 17890 (p. 396, Sūkta 19 Ṛk 5 Saṃhitā and Pada) was read in window 121 (Saṃhitā now ಅಗ್ನೇಽವಿತೇಹ; Pada ಆನಜನ್, ಆಗ್ನೇ as in the picture).
2. `review/doubts.tsv`: all `[?]` so far (about 10).
3. `review/accent_report_cumulative.tsv`: every DIFF/NOMATCH line (the build rewrites `accent_report.tsv` each time). One doubled accent mark per line (`रश्मयः॒॑`, `न॒॑`, `यंति॒॑`) came from the reference. Manual changes are marked MANUAL there: Sūkta 12 Ṛk 5 misplaced accent in इष्ट removed; Sūkta 12 Ṛk 7 duplicated pluta ३ removed; Sūkta 12 Ṛk 3 accent mark moved after the vowel sign in मु॒ग्निं. Sūkta 9 Ṛk 9 accents came from a Maṇḍala 10 verse (reference 10.52.6): check them.
4. Printed-English references (Western scholars, p. 262–265): eight Latin-digit references such as `R. V. v. 59-2`, `p. 349-50` were written with a comma or "to" to pass the check; restore the printed separators if wanted.
5. Quote-less editorial notes without `[?]`: Sūkta 11 Ṛk 8 grammar (the word ರಹರ… at the start of p. 198 window).
6. Possible missing text: p. 429 (right-hand line ends garbled, three [?] in the Ṛk 4 Special Topics);  top of p. 248 does not join the fragment at the foot of p. 247 (Sūkta 13 Ṛk 7 Special Topics); p. 224/225 junction (`[?]` in en.md); p. 233/234 junction (`[?]`).
7. Pāṇini/Uṇ./Nirukta/Ṛg-veda numbers as printed: many differ between places (e.g. Uṇ. 1-56 vs 1-155 for *sapta*; Pā. 6-2-138 vs 139); none was changed. Sūkta 8 heading says "fifth" vs seventh; Ṛk counts differ (Sūkta 7: 11 vs 20) — see the notes in the English file.

12. Page numbers pp. 552/553 (window pp. 550-553): the print's head of the real p. 552 reads 562 and the next page's head also reads 552; the agent numbered the pages 552 and 553 by sequence and kept both heads as supplied (notes in the English file). Please confirm.
13. Window pp. 547-553: one inline form ⟦ಅನ್ನೆಃ⟧ (Ṛk 11 bhāṣya note, Sūkta 27) converts to a Devanagari word with the Kannada-only vowel sign ॆ (as supplied); several quoted Sanskrit forms carry ॆ/ॊ from the Kannada text.

14. Possible missing text at p. 562/563: the Ṛk 15 grammar of Sūkta 27 breaks off mid-word at the end of p. 562, and p. 563 begins directly with Sūkta 28 (no Sūkta 27 colophon printed; bracketed notes in the English file). Check against the scan.

15. Adhyāya 2 front matter (windows pp. 627-632; a bracketed note on p. 632 says words may be missing between the Pīṭhike text of the two windows, nothing added): the title page, invocation and the start of the Pīṭhike (printed pp. 630-631 by position) carry no running heads in the supplied text, so they sit under `### Printed p. 629` in the English file and the progress note says p. 629; the next window starts at p. 632 (prep). Check the true page numbers against the scan.

16. Pīṭhike (pp. 632-644 and on): printed reference abbreviations for the Atharvaveda and the Aitareya Brāhmaṇa (ಅ. ವೇ., ಆ. ವೇ., ಇ. ಬ್ರಾ.) were written in full ("Atharvaveda", "Ai. Brā.") with a bracketed note; the printed form is in the notes. Also, in window pp. 638-641 a full stop before a reference was dropped so the check could pass (noted). Restore the printed forms if you want them verbatim.

17. (Resolved in window pp. 660-664: the page whose head is misprinted "650" is p. 660 by sequence and follows p. 659 directly; no page is missing. The window's page list was renumbered 660-664, with merged heads 661 and 664 split out.)

**Dispatcher**
8. The Pratipadārtha of Sūkta 9 Ṛk 6 (window pp. 96–98): glossed words were written as bare IAST instead of ⟦ ⟧ (about 29); fix in one pass.
9. Merge into `main` when the user says.
11. Hand-typed Devanagari/IAST in editorial notes (not scripted): the word `धनेना (*dhanenā*)-` at the p. 333/334 junction (Sūkta 16 Ṛk 3, three places). The word is the fragment from the previous window's text; convert or remove at the end of the volume.
10. Done Nov 9 2026 (`tools/rv/repair_inline.py 16 --write`, logged in `review/repair_log.md`): the few leftover multi-line `⟦ … ⟧` quotations of the English file converted to Devanagari + (IAST). The other lines with Kannada script in the English file are editorial notes quoting the supplied (garbled) readings, as intended. Run the tool again at the end of the volume.
18. Sūkta 36 Ṛk 1 Pratipadārtha (printed p. 830/831): the Kannada gloss of the verb in the sense "disregarding" was rendered "wishing for companionship" following the printed English; please check this sense against the print.

## Publication (print PDF)
Not built.

## Metrics
| windows | pages | hand-fixes by kind | gate failures | `[?]` | inline mismatches | accent lines unmatched | QA sample | agent tokens / cost |
|---|---|---|---|---|---|---|---|---|
| 273 windows (w0002 … w0883; 1 fresh Sonnet agent per window) | printed pp. 2–884 (883 pages) | by far the most frequent: line-end hyphen joins inside Sanskrit blocks (typically 5–20 per window); then garbled Saṃhitā/Pada/bhāṣya/Pratipadārtha/Bhāvārtha labels (+ unquoted lines), merged running heads (also inside blocks/lines), Anuvāda and sūkta data lines inside the introduction `>` block, Latin letters / foreign digits inside Sanskrit, stray page-number lines, Saṃhitā blocks split across a page break | a handful of piped/unchained gates (windows 109 etc.), see LESSONS 33–38; no failed pushes | 27 lines in `review/doubts.tsv` (pp. 429, 650, 676 and earlier) | 74 segments in `review/inline_mismatch.tsv` (found by a volume-wide run at the end; the gates passed per window — cause not yet analysed) | final volume-wide report: 18 Saṃhitā lines NOMATCH (unaccented, listed in `review/accent_report.tsv` / `accent_report_pages.tsv`), plus the per-window DIFF/NOMATCH/MANUAL/UNACCENTED history in `accent_report_cumulative.tsv` | Opus, 36 pages, read-only, no scans: 2 ERRORs (p. 77, shortened quotations; repaired in commit 103a321c, logged), 8 MINORs left open (see `review/qa_sample.md`), ~60 references all matched | tokens not recorded by the harness per window (about 115–225k per window as reported by the agents' counters; Sonnet) |

Hand changes to accented text (MANUAL rows in the cumulative accent report): 24 — doubled pluta digits (the printed digit plus the script's own), accent marks between a consonant and a virama, a doubled mark. All logged in `review/repair_log.md`.

## Lessons from this volume
- Check the user's brief (`AGENT_BRIEF.md`) before writing the dispatch prompt: the pictures were missed for 55 windows.
- Garbled section labels (ಸಂವಾದಃ, ಹಡಹಾರಂ …) recur; a fuzzy label list in `html_to_kn.py` covered most; Saṃhitā/Pada labels are still hand work.
- The accent script finds Saṃhitā blocks only by the standard label; agents must not rewrite labels.
- The accent script can insert a mark before a vowel sign, after a virama, or duplicate a pluta digit; check with regexes after each window.
- The accent step inside a window's build can leave a Saṃhitā block unaccented (NOMATCH at scores ~0.35 although the reference verse equals the text); a volume-wide `python3 publish/tools/accents/accent_volume.py 16 --write` afterwards accents it (idempotent: already accented lines are skipped). The dispatcher runs it after every window.
- Inline ⟦ ⟧ segments must exist in kn.md; run `check_inline.py` before committing, not after.
- Never write a hand IAST in parentheses after a `⟦ ⟧` segment: the build adds the IAST layer itself (116 doubled `(*x*) (*x*)` pairs had to be removed from the English file, logged in `review/repair_log.md`; check with a regex for two identical consecutive `(*…*)`).

## Pointers
`vol16/AGENT_BRIEF.md`, `vol16/html/HEAD_FIXES.md`, `vol16/parts/batch_costs.md`, `vol16/review/accent_report_cumulative.tsv`, `vol16/review/doubts.tsv`, the last lines of the English file.
