# Rigveda Saṃhitā translation (Kannada → English) — short rules

Loaded by every session **and every agent**, so it is kept short on purpose (Nov 10 2026: the long version cost ~8k tokens per agent). Full rules, formats, publication and checklists: **`docs/HANDBOOK.md`** (section numbers below refer to it). Volume state: `volN/STATUS.md` only. Read `docs/LESSONS.md` before starting a volume and extend it afterwards.

## What we make
From the 1949–52 Kannada edition of the Ṛgveda-saṃhitā (Sāyaṇa's bhāṣya + H. P. Venkata Rao's Kannada commentary), per volume: `volN/Rigveda_Samhita_VolN_English_Translation.md`, `…_Kannada_Text.md`, print PDFs (`publish/volbook.py`), `volN/STATUS.md`. Source from Vol 12/14 onwards: the user's machine-read text in `volN/html/` (no page scans).

## Rules that are never bent
1. **Sanskrit in three layers** (Devanagari + IAST + English) on every citation; made by script. The translator **never types Devanagari or IAST**: blocks are placed with `[[bN]]`, inline Sanskrit is copied from `kn.md` inside `⟦ ⟧`. Exceptions from Vol 17 on (user, Nov 11 2026; `volcfg.json` `no_iast_blocks`, `grammar`): the **Sāyaṇa-bhāṣya block is Devanagari only**, followed by an English Gist that covers most of the block (not the grammatical tail), and the **grammar section is rendered from the Kannada into Sanskrit** by the translator (written in Kannada script inside `⟪ ⟫`, one word per line, shown in Devanagari only). That Sanskrit is composed, not copied: no gate can check it; only the editor's reading does.
2. **The supplied text is the base. Never correct a letter or number from memory or from another edition.** From Vol 17 on (user decision, Nov 11 2026; `"note_style": "NOTE"` in `volcfg.json`): **the English text carries no translator remarks** — no running heads, no "as supplied", no `[?]`, no `[sic]`, no bracketed comments; every place that needs the editor's decision or a second look is marked `**NOTE**` in the text and its question is listed in `volN/review/notes.tsv` (the translator writes `**NOTE**{question}`; the script moves the braces' content to the list). Vols 12–16 keep the older remarks until the user asks for a conversion. No number where the print has none.
3. **Output files are append-only**, exactly one trailing `**Progress note:** Done through printed p. N`; only `tools/rv/batch.py` writes them. Repairs of earlier text are separate edits logged in `volN/review/repair_log.md`.
4. **Honest reports**: say what was verified and how; never report a commit not seen in `git log`.
5. **Git**: branch `claude/volN` (or the session's branch); commit and push every window; never force-push; no pull requests or merges into `main` unless asked.
6. **Private repo**: `refs/mandala/*` is for personal study; rights/ISBN are placeholders until the user decides.
7. No per-volume tools or prompts: fix the shared tool (`tools/rv/`, `publish/`). Twice is a pattern: a hand-fix used twice becomes a script change (§15).

## The translation loop (one window ≈ 6 printed pages; `window` in `volN/volcfg.json`)
- **Translator agent (Sonnet, fresh for every batch of three windows)**: for each window runs `python3 tools/rv/batch.py next N` (audit by script + prep), reads `WIN/TASK.md` (and `tools/rv/BRIEF.md` once), writes `WIN/en.md`, runs `python3 tools/rv/batch.py done N WIN --note "…"` (build, all gates, commit, push, self-verification) until it prints `VERIFIED`.
- **Dispatcher** (main session; Sonnet is enough): one Agent call per batch with the prompt in `volN/CONTINUE_PROMPT_HTML.md`; when the agent reports, append its token count to `volN/parts/batch_costs.md` and start the next batch. No manual `git log`/`grep` checks: `next` refuses to prepare a window while the audit fails. Never two writers on one volume.
- Measured on Vol 12 (Nov 10 2026): about 10k tokens per page this way, against 25–36k for one fresh agent per 3-page window (Vols 14–16).
- **Batch API route** (pilot on Vol 17; needs `RIK_API_KEY`): `python3 tools/rv/api_batch.py plan|submit|status|collect N` sends windows as one batch (half price, no agents); `plan` is free and prints the estimate, `submit` spends money: only after the user has seen the estimate.
- `python3 tools/rv/batch.py audit N` = the invariants at any time. A window is done only when `done` printed `VERIFIED` and `audit` passes.
- The script (`tools/rv/html_to_kn.py`) repairs the supplied text's structure before the translator sees it (garbled/missing labels, hyphen joins, stray lines, missed running heads); what it did is listed in `TASK.md`.

## Where things are
`tools/rv/` pipeline (`batch.py`, `html_to_kn.py`, `html_pages.py`, `convert.py`, `check_inline.py`, `BRIEF.md`, `RUNBOOK.md`) · `publish/volbook.py` + `publish/tools/` print build, transliteration, accents, front matter · `refs/mandala/` accented reference · `docs/HANDBOOK.md` everything else (§4 inputs, §5 new volume, §7 formats, §8 publication, §11 finishing checklist, §14 session hygiene, §15 keep improving) · `docs/LESSONS.md`, `docs/REPO_REVIEW.md`.

## Session hygiene
Cloud sessions are ephemeral: commit **and push** anything worth keeping. One long job at a time. `pip install indic-transliteration rapidfuzz openpyxl` at session start; fonts/WeasyPrint only for PDF builds (§8). Quote sizes and counts only from finished commands.
