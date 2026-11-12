# What we keep, what it is for, how it is used — proposal (DRAFT)

**Nov 12 2026, for the user's review. Nothing has been moved, renamed or deleted.** This answers the user's point: "there are so many scripts and tools and reports and logs all around; we need to define what we really need, for what purpose and how to use it." It belongs with `docs/REQUIREMENTS.md` (what a volume must be) and `docs/ERROR_KINDS.md` (what goes wrong); the design document will build on all three.

## 1. What is in the repository today (counted Nov 12 2026)

| Kind | Count | Where |
|---|---|---|
| Python scripts | 357 | 271 in per-volume folders (`vol1/tools` … `vol14/tools`) from the scan period; 23 shared pipeline scripts in `tools/rv/`; 13 print scripts in `publish/`; 50 in `publish/tools/` |
| Documents of rules and reports | 19 in `docs/`, plus 3 in `tools/rv/`, plus state, pass-log, handoff and runbook files in most volume folders | rules are spread over `CLAUDE.md`, `HANDBOOK.md`, `BRIEF.md`, `RUNBOOK.md`, `TRANSLATOR_RULES.md`, `LESSONS.md` and per-volume prompts |
| Review files per volume | about 40 different kinds of file name across the volumes | `volN/review/` — doubts, edits, notes, flags, numerals, accent reports, QA samples, repair logs |
| Working files | about 1,400 small files | `volN/work/` — five files for every translated window |

Three causes: each scan-period volume grew its own scripts; each problem found added a report of its own kind; rules were written where the problem was met.

## 2. Principle
Everything kept must answer one of four questions. Anything that answers none is archived.

| Question | Answered by |
|---|---|
| What must a volume be? | one requirements document |
| How is a volume made, checked and printed? | one design document and one set of commands |
| What is the state of volume N, and what does the editor still have to decide? | a fixed, small set of files in every volume folder, same names everywhere |
| Why is a rule there? | one lessons file |

## 3. Documents — proposed set

| Keep | Purpose | Who reads it | Replaces |
|---|---|---|---|
| `docs/REQUIREMENTS.md` | what a volume must contain and how it must look | the user; every session | the "what" parts of `CLAUDE.md`, `HANDBOOK.md` §1, §2, §7, §8, `BRIEF.md` |
| `docs/DESIGN.md` (to be written) | how the work is done: structure by script, translation, second reading, checks, print | every session | `HANDBOOK.md` §4–§6, §9, §11, `RUNBOOK.md`, `TRANSLATOR_RULES.md`, `VERIFY_PASS_REQUIREMENTS.md` |
| `docs/OPERATING.md` (to be written; one page) | the commands, in the order they are run, with what each prints when all is well | the session that runs a volume | per-volume `CONTINUE_PROMPT` files, `HANDBOOK.md` §5, §14 |
| `docs/REFERENCES.md` (to be written) | the one list of works cited, abbreviations, known mistakes (requirement B3) | translator, checks, the user | `refs_fix.py` comments, the per-volume abbreviation notes |
| `docs/LESSONS.md` | why each rule exists | whoever wants to change a rule | — (kept; duplicates removed) |
| `docs/ERROR_KINDS.md` | the errors found so far, by kind | the user; design work | scattered QA summaries |
| `CLAUDE.md` | ten lines: what the project is, the rules that are never bent, and "read REQUIREMENTS, DESIGN, OPERATING" | loaded by every session | its present long form |
| `tools/rv/BRIEF.md` | the instruction the translator model receives; derived from REQUIREMENTS, nothing in it that is not there | the model | — |

**To the archive (`docs/archive/`), kept but out of the way:** `HANDBOOK.md` once its content is in the three documents above, `HISTORY.md`, `LEGACY_SCAN_WORKFLOW.md`, `PASS_LOG*.md`, `NUMERAL_*`, `COORDINATION_NOTES`, `CLEANUP_*`, `REPO_REVIEW.md`, `KANNADA_OCR_REQUIREMENTS.md`, `Translation_Conventions_Handoff.*`, `SESSION_REPORT_*`, and the per-volume `*_state.md`, `*_pass_log.md`, `*_handoff.md`, `*_runbook.md`.

## 4. Tools — proposed set
One command with a few verbs, the same for every volume, instead of many scripts called by name. Behind it are the existing shared scripts; what changes is that a session needs to know only this table.

| Step | Command (proposed) | What it does | Existing scripts behind it |
|---|---|---|---|
| 1. Prepare | `rv prepare N` | merges the supplied files, finds the pages, makes the Kannada file and the page-by-page structure; lists the faults of the supplied text (missing pages, garbled labels) | `merge_md`, `html_pages`, `html_to_kn`, `refs_fix`, `kn_headings` |
| 2. Translate | `rv translate N` (estimate first, then send, then collect) | sends the English work to the model and puts the answers into the structure | `api_batch`, `api_front`, `batch`, `convert` |
| 3. Second reading | `rv reread N` (new) | every page read again against the Kannada; findings listed, the safe ones applied | new |
| 4. Check | `rv check N` | all whole-volume checks in one run, one result file, each check saying how much it compared | `batch audit`, `check_labels`, `check_inline`, `rkheads`, accent report, abbreviation check (new), Ṛk numbers against the reference (new) |
| 5. Print | `rv print N` | English and Kannada PDFs in the standard front-matter order | `volbook`, `add_iast`, `accent_volume`, `fm_extract`, `contents_parse` |
| Repair | `rv repair N …` | a logged change to finished text | `batch fix`, `to_note_style` |

**Shared scripts that would no longer be called directly or would go to the archive:** `run_volume.py` (never run), `repair_inline.py`, `repair_worksheet.py`, `compare_html_scan.py`, `page.py`, `numerals.py`, `annotate_report.py` (scan period or one-off repairs); `publish/build*.py`, `vol*_clean.py`, `lighten.py`, `voice.py`, `review_*.py` (print builds of Vols 1–7, replaced by `volbook` when those volumes are rebuilt); `publish/tools/ref_check`, `numeral_pass`, `verify11`, `pageprep`, `english_ocr` (scan period).
**The 271 scripts in `volN/tools/`** belong to the scan period and are not used by any current step: to an archive folder or branch, by the user's decision.

## 5. Records — the same small set in every volume

| File | Purpose | Written by | Read by |
|---|---|---|---|
| `volN/STATUS.md` | where the volume stands: pages done, cost, what is open — one screen | each step | the user, the next session |
| `volN/review/notes.tsv` | every place that needs the editor's decision, with its question and a column for the decision | translate, second reading | the user |
| `volN/review/source_faults.tsv` (new name) | faults of the supplied text and deviations from the reference: missing page marks, garbled labels, verse differs from the reference, stray letters removed | prepare, check | the user |
| `volN/review/checks.md` (new name) | the result of the last run of every check, with what each compared; the QA sample and the second-reading summary are sections of it | check, second reading | the user, the next session |
| `volN/review/repair_log.md` | every change made to finished text, with the reason | repair | anyone asking "why does the text read so" |
| `volN/parts/costs.md` | API cost by stage | translate, second reading | the user |

**Would be folded into these or archived:** `doubts*.json/tsv`, `edits_*.txt`, `notes_PDF*.txt`, `flags_*.md`, `page_flags.md`, `inline_readings.tsv`, `inline_mismatch.tsv`, `accent_report*.tsv`, `qa_sample.md`, `remarks_removed.tsv`, `legacy_compare*.tsv`, `numerals_*`, `review_PDF*.html/json`.
**Working files (`volN/work/`)** are needed while a volume is being made and until its checks and QA are finished. After that they could leave the working tree (the git history keeps them). To be decided.

## 6. How a volume is run with this set (the whole of it)
1. The user uploads the supplied files. `rv prepare N` → the user reads `source_faults.tsv` (missing pages and the like) before anything is sent.
2. `rv translate N` prints the estimate → the user says yes → it sends and collects.
3. `rv reread N` (estimate, yes, run).
4. `rv check N` → `checks.md`. Anything not passing is repaired (`rv repair`, logged) or listed for the user.
5. `rv print N` → the PDFs. The user reads; decisions go into `notes.tsv`.

## 7. Decisions for the user
1. Is the document set of §3 the right one — in particular one requirements document, one design document and a one-page operating guide in place of the handbook?
2. One command with verbs (§4), or keep the scripts called by name and only document which are in use?
3. The record set of §5: are six files per volume enough for you as the editor, and are the names clear?
4. The scan-period scripts and reports (271 scripts, the per-volume state and log files): to an archive folder inside the repository, or to a separate branch so that `main` holds only what is in use?
5. Working files of finished volumes: keep in the working tree or remove once a volume's checks are done?

Nothing of this is urgent for the content of the books; it decides how easy the next volumes are to run and to review. It should be settled together with the design, so that the new structure-by-script and second-reading steps are built once, in their final place.
