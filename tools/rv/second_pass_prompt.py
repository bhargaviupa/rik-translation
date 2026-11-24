#!/usr/bin/env python3
"""Write the second-pass prompt of a volume (Vols 1-6 so far): one common template, the facts of the volume from the table below.

  python3 tools/rv/second_pass_prompt.py [N ...]     writes docs/prompts/second_pass/VOLN.md

The facts are taken from volN/STATUS.md and docs/REQUIREMENTS.md Part L (Nov 24 2026); when a volume changes, change the table, not the prompt."""
import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
V = {
1: dict(scope="Pūrva-pīṭhikā, Sāyaṇa's Bhāṣya-bhūmikā and Maṇḍala 1 Sūktas 1–2: printed pp. 1–720; the first 605 pages are continuous prose (preface, introduction, the Bhūmikā chapters), the Ṛk layout starts at p. 606.",
 text="Three supplied files in `vol1/html/`: `rig_1_1.md` (front matter and pp. 1–224), `rig_1_2.md` (pp. 225–572, converted from HTML on Nov 18), `rig_1_3.md` (pp. 575–720). The Kannada file in `vol1/kannada/` was made from the old HTML form and **must be made again from the three markdown files**.",
 english="`vol1/Rigveda_Samhita_Vol1_English_Translation.md` and `vol1/Rigveda_Samhita_Vol1_Gaps_English_Translation.md` (printed pp. 95–167, 191–205, 261–283 and 288–295, inserted by `publish/vol1_clean.py`); about 291,000 words; about 120 `[?]`.",
 special=["**Prose volume.** There is no unit structure for continuous prose yet (REQUIREMENTS: not built). Work page by page; do not invent a unit scheme.",
  "**Known gaps:** printed pp. 17–24 are missing in the source; about 148 pages have no Sanskrit; about 256 Sanskrit citations were converted from transliteration unverified; the records disagree on which page ranges were skipped or translated later (pp. 95–167, 119–191, 215–229, 285–307, 312–319). List what the files really contain, page by page, before reading anything.",
  "**Uniform files for every volume come from Vol 1:** the portrait pages (p. 4 king, p. 5 guru), the thank-you page and the bibliography (p. 39 of the PDF, the base of the abbreviation list). Cut them out as picture files and list them in `vol1/review/uniform_files.md`; the user decides the directory (REQUIREMENTS F35). Do not move anything.",
  "**Sāyaṇa's Bhāṣya-bhūmikā** is Sanskrit prose that may not be in the Wikisource index (the index holds the Ṛks and their commentary; check its `other` pages). Report whether it is; do not fetch anything from the site.",
  "**Legacy conventions (`[?]`, bracketed remarks) stay.** The old re-check prompt (`vol1/CONTINUE_PROMPT_HTML.md`) said not to convert Vol 1 to `NOTE`; the user has not changed that (REQUIREMENTS F7, M6). Reuse its rules for settling `[?]`: numbers and references are taken from the supplied text; text from context; only a place the context does not decide stays `[?]`."]),
2: dict(scope="Maṇḍala 1 Sūktas 3–19 (First Adhyāya of the First Aṣṭaka): printed pp. 2–808.",
 text="`vol2/html/rig_2_1.md` (front matter and pp. 2–385, Sūktas 3–10) and `rig_2_2.md` (pp. 386–808, Sūktas 10–19): the whole volume. Pages without their own running head (first pages of a sūkta or section): 9, 98, 123, 178, 194, 222; 415, 420, 551, 628, 662, 679, 735.",
 english="`vol2/Rigveda_Samhita_Vol2_English_Translation.md`. **The user did its translation and second reading from scans and called it good: do not re-translate, and be sparing with repairs.** Cleaned of our remarks on Nov 17 (`vol2/CLEANUP_PROMPT.md`, `vol2/review/repair_log.md`).",
 special=["**Kept by the user's decision:** `[?]` (429, lists in `vol2/review/open_readings.tsv` and `refs_marked.tsv`) and `[sic]` (143). Do not remove or convert them; where the supplied text settles a `[?]` with certainty, correct it and log it (that is the second pass's job).",
  "**Accents:** the 176 Ṛks of Sūktas 3–19 were replaced by the accented verses of the old reference text (`review/verse_corrections.tsv`). The reference is now the Wikisource index (REQUIREMENTS B1.2): compare, and list the differences; do not replace again without the user's word.",
  "**Open items on record:** varga numerals unreconciled with the colophons; a stray Cyrillic string; the second-scan cross-check was unfinished (pp. 1–30 and 75 on); 4 pictures in `vol2/html/figures/`.",
  "**Glosses:** the gloss sessions replaced labelled glosses by `**GLOSS**` (see `vol2/review/` and `vol2/STATUS.md`; the status gives no count); do not touch them."]),
3: dict(scope="Maṇḍala 1 Sūktas 20–32 (Second Adhyāya of the First Aṣṭaka): printed pp. 2–647.",
 text="`vol3/html/rig_3_1.md` (front matter and pp. 2–285; supplied as HTML and converted to markdown with pandoc) and `rig_3_2.md` (pp. 286–647): the whole volume. 37 pictures are in `vol3/html/figures/`.",
 english="`vol3/Rigveda_Samhita_Vol3_English_Translation.md` (about 799 print pages); the *anāhitāgni* note (Sūkta 31, p. 576) is a separate section at the end. 35 `**GLOSS**` markers; 13 labelled glosses left in `review/glosses_left.tsv`; about 537 doubt marks.",
 special=["**Sūkta 29 Ṛks 6–7 and all of Sūkta 30 (pp. 452–517)** were first written while page-image views were failing, then redone from the images on Oct 27 2026 (`vol3/Session_Report_Vol3_Sukta29-32.md`). Read these pages with extra care against the supplied text.",
  "**Rule of the scan period for any scanned page:** if an image view returns no image, stop and report; never write that page.",
  "**Glosses:** unlabelled glosses were not yet looked for; list them in `review/second_pass/questions.tsv` if you meet them, do not replace them."]),
4: dict(scope="Maṇḍala 1 Sūktas 33–46 (Third Adhyāya of the First Aṣṭaka): printed pp. 2–608.",
 text="`vol4/html/rig_4_1.md` (front matter and pp. 2–286, Sūktas 33–37) and `rig_4_2.md` (pp. 287–608, to Sūkta 46; ends with the closing lines). 15 page numbers have no running head of their own. 38 pictures are in `vol4/html/figures/`.",
 english="`vol4/Rigveda_Samhita_Vol4_English_Translation.md`. 82 `**GLOSS**` markers; 31 labelled glosses left; about 151 doubt marks and 103 accent doubts (`accent ?`).",
 special=["**Accent doubts (103)** concern the verses: the Saṃhitā now comes from the Wikisource index, so these are not corrected by hand; list the Ṛks and leave them for the later build.",
  "Nothing else is on record for Vol 4 beyond `[?]` readings."]),
5: dict(scope="Maṇḍala 1 Sūktas 47–61 (Fourth Adhyāya) and the Kannada Pariśiṣṭa on the deities and persons of the Ṛgveda (printed pp. 531–708, translated at the user's request): printed pp. 1–529 and 531–708 (p. 530 is blank).",
 text="Seven files in `vol5/html/` (the list of page ranges and the pages without a head is in `vol5/STATUS.md`); pp. 273–286 and 584 stand in two files each. The two files of the repair pilot were replaced by these.",
 english="`vol5/Rigveda_Samhita_Vol5_English_Translation.md`. 91 `**GLOSS**` markers; 18 labelled glosses left. **A repair pilot already compared printed pp. 1–184 with the supplied text** (`vol5/review/html_repair_log.tsv`, `tools/rv/repair_worksheet.py`, `compare_html_scan.py`).",
 special=["**The Pariśiṣṭa (pp. 531–708) is continuous prose** with no Ṛks: read it as prose (no layers, no bhāṣya).",
  "**The user's own readings for pp. 578–625 were never applied** (`vol5/review/`; look for the readings file named in `vol5/STATUS.md` and `vol5/README.md`). Apply them where the supplied text agrees or is silent; where it disagrees, put both in `questions.tsv`.",
  "Start the page batches **after** p. 184 (already compared), unless the pilot's log shows pages that were not finished."]),
6: dict(scope="Maṇḍala 1 Sūktas 62–80 (Fifth Adhyāya of the First Aṣṭaka): printed pp. 2–619.",
 text="`vol6/html/rig_6_1.md` (front matter and pp. 2–81), `rig_6_1_0.md` (**p. 82 alone**: it joins p. 81 and p. 83 without a gap; the word-meaning list of Sūkta 63 Ṛk 6 ends on p. 81, p. 82 opens with its Bhāvārtha, and its last sentence runs on into p. 83), `rig_6_2.md` (pp. 83–382) and `rig_6_3.md` (pp. 383–619, to the printer's line). 60 pictures in `vol6/html/figures/`.",
 english="`vol6/Rigveda_Samhita_Vol6_English_Translation.md`. 115 `**GLOSS**` markers; 17 labelled glosses left.",
 special=[]),
}
COMMON = """# Second pass of Volume {n} — prompt for a new session (Sonnet is enough)

You carry out the **second pass of Volume {n}** of the Rigveda translation (repo `bhargaviupa/rik-translation`). Volume {n} is a legacy volume (made from page scans; REQUIREMENTS Part L, family L1). The supplied machine-read text of the whole volume now exists, and the decisions of Nov 21–24 2026 (DESIGN §14, REQUIREMENTS Draft 5) say what the second pass is. One session, one volume, one writer. You may start subagents (Sonnet) for page batches; you do not use the API and spend no money.

## The volume
- **Scope:** {scope}
- **Supplied text:** {text}
- **English:** {english}
- **Numerals (user, Nov 24 2026): the supplied Kannada documents of Vols 1–6 have correct numerals; the user does not verify them.** Take every number and reference from the supplied text; the user's numeral files (where they exist) are not needed. A difference between the English and the supplied text is settled in favour of the supplied text with a logged repair, with no question to the user. Never settle a number from memory.
{special}

Read first: `CLAUDE.md`, `volN/STATUS.md` (here `vol{n}/STATUS.md`), `docs/REQUIREMENTS.md` Parts B, I, J, K9, L, M, `docs/DESIGN.md` §14, `docs/LESSONS.md`, `docs/ERROR_KINDS.md` (the kind codes you will use). `pip install indic-transliteration rapidfuzz openpyxl`.

## Rules
1. **Supplied Kannada text:** it may be edited by this pass (REQUIREMENTS B1.6, decided Nov 23 2026), only where the intended reading is certain, every edit one row of `vol{n}/data/source_fixes.tsv` (place, as supplied, as corrected, reason, basis, who decided). Where it is not certain, the place stays and becomes a row of `vol{n}/review/second_pass/questions.tsv`.
2. **The Wikisource text (`refs/wikisource`, index `python3 tools/rv/ws_index.py build`; commands `get M.S[.R[.P]]`, `search`) is never edited, never compared per Ṛk and never flagged,** except the three known defects of REQUIREMENTS B5.6. It is the source of the Saṃhitā, the Pada and Sāyaṇa's bhāṣya. Do not visit the site.
3. **English:** repairs of the existing English are separate edits, each a line of `vol{n}/review/repair_log.md` (page, old → new, why, the finding it answers). Do not re-translate; change a sentence only where the Kannada shows it wrong. A change of reading that changes the meaning also changes the English that depends on it; say so in the log.
4. **No number where the print has none; no letter or number from memory or from another edition.** Reference numbers are never changed by hand; `python3 tools/rv/refs_apply.py {n}` (preview) is the only way names of works change.
5. **Legacy conventions stay** (`[?]`, `[sic]`, bracketed remarks, `**GLOSS**` markers): inventory them, do not convert or remove them (REQUIREMENTS F7, M6) unless a rule above settles the place.
6. **No per-volume tools or prompts.** If you need a script, write it in `tools/rv/` taking the volume as an argument. Never print `RIK_API_KEY`; do not call the API.
7. **Git:** work on the branch this session was given; commit and push after every stage and every batch; never force-push; no pull request; no merge into `main` unless the user says so. Report only what finished commands showed; quote `git log -1` for every commit you claim.

## Stages (each ends with a short report to the user; stop after S0 and after the S2 pilot and wait)
**S0. Set-up and sieve (scripts, no model).** (a) Merge or list the supplied files; page map; missing pages; pages without a head (list, do not chase). (b) `python3 tools/rv/batch.py audit {n}` if it runs for this volume (it may not: legacy), else report the invariants you could check. (c) Script checks, each printing what it compared: numbers and references of the English against the supplied text (`tools/rv/recheck.py`, `recheck_numbers.py`, `numerals.py`); abbreviations against `rv/references.tsv` (`refs_apply.py {n}` preview only); letters of other scripts in the English and Kannada; inventory of `[?]`, `[sic]`, remarks, `**GLOSS**`; Sanskrit citations of the English against the supplied text. (d) Write the results to `vol{n}/review/second_pass/sieve.md` and show the user the table (page, counts, differences) **before any batch starts**: it tells how big S2 is.

**S1. Kannada book from the supplied text (A5).** Make `vol{n}/Rigveda_Samhita_Vol{n}_Kannada_Text.md` from the supplied files by the shared scripts (`tools/rv/html_to_kn.py`, `prose_kn.py` for prose pages): the text of the original page by page, page marks, no remarks of ours. Its Sanskrit blocks stay as supplied (they are not part of the English; the later build takes the Saṃhitā, Pada and bhāṣya from Wikisource). Edits to the supplied text go through `source_fixes.tsv` (rule 1).

**S2. Reading in page batches.** Pilot first: **10 printed pages from the middle of the volume**, then batches of about 30 pages, one fresh Sonnet subagent per batch, one batch at a time. Per page the agent reads the supplied Kannada against the English once and looks for, in this order: (R1) a number or reference missing, changed or supplied from memory; a name or term wrong; roles reversed; an addition the Kannada does not have; an omission inside a paragraph; a misprint silently put right; (R6) a Kannada word that is not a word, a name or term misread for a look-alike, vowel signs of the wrong script, a page-break sentence cut; (R3) a Sanskrit quotation inside the commentary that is not a word or not the text the English cites. It does not read the Saṃhitā, Pada or bhāṣya blocks. Every finding is one row of `vol{n}/review/second_pass/findings.tsv` with the columns `page, kind (a code of ERROR_KINDS), reader (R1|R3|R6), place (the words), as_found, proposed, basis, decision (applied|question), log`. **Decision rule:** {numrule} a text place is changed only where the Kannada sentence, the grammar of the quotation or the gloss that follows it decides; otherwise `question`. Report the pilot: pages read, findings by kind, applied, questions, tokens used; show five applied repairs with old and new text. Wait for the user before the batches.

**S3. Repairs.** Apply the `applied` rows: English repairs to the English file and `repair_log.md`; Kannada source edits to the supplied file and `source_fixes.tsv`. Re-run the S0 checks and show the before and after counts.

**S4. Sāyaṇa-bhāṣya layers (checks only; no English of the bhāṣya yet).** List which Maṇḍala.Sūkta.Ṛk addresses the volume covers (from the Wikisource index) and check by count that every Ṛk of the volume's scope has its Saṃhitā, Pada and bhāṣya in the index, none missing, none twice (REQUIREMENTS D17); write the list to `vol{n}/review/second_pass/ws_coverage.tsv`. **Do not translate the bhāṣya**: that needs the user's decision on cost, model and the user's own second reading (REQUIREMENTS K4.3, F49).

**S5. Pictures.** `python3 tools/rv/figures_sheet.py {n} --pdf` gives the contact sheet (`vol{n}/review/Vol{n}_pictures.pdf`); report the cover pictures (pictures 1 and 2 of the first supplied file) and the pictures that hold text. Do not transcribe pictures that hold a verse (REQUIREMENTS B6.6).

**S6. Records.** Update `vol{n}/STATUS.md` (what was read, counts, what is open), tick the second pass for Vol {n} in `PUBLICATION_TODO.md` with the date, commit and push. List every open question of `questions.tsv` in a table for the user (HR1, HR2 of Part J).

## Not part of this pass
Translating the bhāṣya; removing the bhāṣya blocks from the English file (the removal script is not built, K7.3); the dictionary and the tag document (Part O); converting `[?]` to `NOTE`; the scan check R7 (it needs the scans, which are not in the repository; ask the user only if they offer them); the finishing checklist and PDFs.

## Stop and tell the user when
a check you cannot interpret; a batch whose findings are mostly questions (the supplied text may be worse than assumed); anything that would change a number or a Sanskrit letter without a certain basis; the usage limit is near (commit and push first; the next session resumes with this same prompt: S0's sieve file and `findings.tsv` show where you stopped).
"""
def main():
    ns = [int(a) for a in sys.argv[1:]] or sorted(V)
    d = os.path.join(ROOT, 'docs', 'prompts', 'second_pass'); os.makedirs(d, exist_ok=True)
    for n in ns:
        v = V[n]; special = '\n'.join('- ' + x for x in v['special'])
        numrule = "a number or reference is taken from the supplied text, whose numerals are correct (user, Nov 24 2026), with no question to the user;"
        t = COMMON.format(n=n, scope=v['scope'], text=v['text'], english=v['english'], special=special, numrule=numrule)
        t = t.replace('`volN/STATUS.md` (here `vol%d/STATUS.md`)' % n, '`vol%d/STATUS.md`' % n)
        open(os.path.join(d, f'VOL{n}.md'), 'w', encoding='utf-8').write(t); print(f'VOL{n}.md', len(t.split()), 'words')
main()
