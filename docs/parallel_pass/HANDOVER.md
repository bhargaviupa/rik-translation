# Parallel numeral / [?] / accent pass — Vols 3, 4, 5 (handover, Oct 29, 2026)

Status: **PAUSED by the user (Oct 29, ~04:40 UTC).** All 9 workers finished their current Ṛk, pushed, and stopped. All 10 scheduled tasks are **disabled** (not deleted). **All 9 branches were merged into `main` on Oct 29 at their pause points** (each merge checked: every added line present, no heading lost or duplicated, [?] counts add up: Vol 3 760→537, Vol 4 2,136→976, Vol 5 1,918→1,238). New workers should start from `main` (or fast-forward their branch to `main` first).

## Workers (one branch, one range each; same translation file per volume, disjoint ranges)

| ID | Range (printed pages) | Branch | Done through | Resume at | Worker session |
|---|---|---|---|---|---|
| v3a | Vol 3: Sūkta 24 Ṛk 14 – end of Sūkta 29 (pp. 288–458) | claude/numerals-vol3-a | Ṛk 26.9 (p. 370) | Ṛk 26.10 (pp. 370–373, PDF 384–387) | session_01CtcBQSb2sRQVbtSgeb7zSF |
| v3b | Vol 3: Sūkta 30 – end, incl. moving the *anāhitāgni* note into Ṛk 31.15 (pp. 459–647) | claude/numerals-vol3-b | Ṛk 31.3 (p. 534) | Ṛk 31.4 (pp. 534–540, PDF 548–554) | session_01CtcBQSHTxDQuaAbUUddrnA |
| v4a | Vol 4: Ṛk 33.7 – end of Sūkta 35 (pp. 33–175) | claude/numerals-vol4-a | Ṛk 34.9 (p. 116) | Ṛk 34.10 (p. 117, PDF 132) | session_01CtcBQU4Bny24ygpNprETA2 |
| v4b | Vol 4: Sūktas 36–38 (pp. 176–338) | claude/numerals-vol4-b | Ṛk 37.10 (p. 281) | Ṛk 37.11 (pp. 281–284, PDF 296–299) | session_01CtcBQV88CXYA9oEPddoyfd |
| v4c | Vol 4: Sūktas 39–43 (pp. 339–492) | claude/numerals-vol4-c | Ṛk 40.7 (p. 406) | Ṛk 40.8 (p. 406, PDF 421) | session_01CtcBQRhdisW1Sy6mpBMitG |
| v4d | Vol 4: Sūktas 44–46 to the end (pp. 493–608) | claude/numerals-vol4-d | Ṛk 46.1 (p. 573) | Ṛk 46.2 (pp. 574–576, PDF 589–591) | session_01CtcBQSAwnAMjVPjvK28qjY |
| v5a | Vol 5: Sūktas 47–51 (pp. 1–211) | claude/numerals-vol5-a | Ṛk 49.1 (p. 94) | Ṛk 49.2 (pp. 95–98, PDF 111–114) | session_01CtcBQU2HgyokVbsYSr9QVP |
| v5b | Vol 5: Sūktas 52–56 (pp. 212–391) | claude/numerals-vol5-b | Ṛk 53.7 (p. 290) | Ṛk 53.8 (pp. 290–294, PDF 304–308; reading notes kept) | session_01CtcBQRvX7R3usyZtXPcWRS |
| v5c | Vol 5: Sūktas 57–61 + Pariśiṣṭa (pp. 392–708) | claude/numerals-vol5-c | Ṛk 60.2 (p. 468) | Ṛk 60.3 (p. 469, PDF 485) | session_01CtcBQRm9oLEPL2WTzgp1Lu |

Each worker keeps its own state in `volN/parts/<id>_state.md` (authoritative resume point) and its log in `volN/review/edits_<id>.txt`; its own tools end in `_<id>.py`. Pages left at the pause: Vol 3 ≈ 201, Vol 4 ≈ 241, Vol 5 ≈ 458 (≈ 900 total).

## Rules every worker follows (prompt template: `worker_prompt_template.txt`)
- **Scope (user, Oct 29): local corrections only, as in the Vol 4 runbook** — numerals, [?], clear misreadings, Saṃhitā accents; no wholesale re-transcription or rewriting of sound text (Vol 3 workers rewrote whole Ṛks until the pause; that stops).
- Only its own range; exact, local replacements only — **never a whole-file script** (no `add_iast.py` on the whole file, no un-ranged `sed -i`), so the branches merge cleanly.
- **No OCR for any reading**; numbers and words only from crops actually viewed. **Blank image view → stop**, write nothing for that page.
- Never edit the shared `volN_state.md`, pass log, CLAUDE.md, runbooks, shared tools, `.docx`/`.pdf`; never merge into main; no PR, force-push or reset.
- Commit and push after every Ṛk; when the range is done: first line of the part state file = `RANGE DONE`.
- No time cut-off (the earlier 21:15 UTC stop was cancelled by the user); work until the range is done.

## To resume
- **Recommended (fresh context, lower cost):** start a new session per worker (model Opus, repo `bhargaviupa/rik-translation`, branch as above) with `worker_prompt_template.txt` filled in (`{BRANCH} {RUNBOOK} {STATE} {PART} {EDITS} {ID}` + a `YOUR RANGE:` line from the table) plus: "Continue from your part state file; the branch already exists."
- **Or** revive the old sessions with a message "resume", and re-enable the scheduled tasks (they still contain an obsolete "stop at 21:15 UTC" line — tell workers to ignore it, or create new check-ins from the new sessions).
- Usage limit: 9 Opus workers use up a 5-hour allowance in ~20–35 min, then wait for the reset; hourly check-ins restart them.

## Scheduled tasks (all disabled)
Coordinator audit `trig_01GYaxKuuZXviNciKT6heymR` (posts into the old coordinator session session_01WfQHJf2G1dSc1yQq4WzMMc). Worker check-ins: v3a `trig_01UBoowwxzd24ffj2BBc3yjD`, v3b `trig_01CaYLdvTmXKpshAY7cyjcyw`, v4a `trig_01L6a5YJQR9PyQUNKuvshtfo`, v4b `trig_01TjwMTGu5gvv5EkWPtcmLX3`, v4c `trig_01PTCSQk4adm8yqUpx7ioTEb`, v4d `trig_01KfrcJGDnKG1FaAvBhUaubh`, v5a `trig_01J4dffbaa7W38jNSbooo5yK`, v5b `trig_017T5QghAFUvHJQb83THxGfW`, v5c `trig_01FW4vLuwByoiLmphCZDGXwc`. A task's prompt can be edited only from the session it posts into; if new sessions are used, delete these and create new ones from there.

## Coordinator duties (hourly; keep output to one line per branch)
1. `python3 docs/parallel_pass/audit.py` — per branch: commits, line span of changes (must lie inside its range), file size, [?] count, OCR mentions, blank-image reports, files touched.
2. Stalled/failed worker with an unfinished range → message it to continue. Rule break → interrupt and tell it what to fix.
3. Branch whose part file starts `RANGE DONE` → merge into `main`, **one at a time, no work lost**: diff only inside its range; after the merge every Ṛk heading of both sides present, none duplicated; its edits present unchanged; [?] count changed only by its own resolutions; conflicts resolved by hand keeping both sides (record them); fold its part state into `volN_state.md`; push; delete its check-in.
4. All 9 merged → rebuild the Vol 3/4/5 DOCX (CLAUDE.md recipe; check no ◌), push, report pages done and [?] before/after.

## Baseline (main at commit 1bbf31b, Oct 28 ~15:05 UTC)
[?] counts: Vol 3 760, Vol 4 2,136, Vol 5 1,918.

## Facts found during the pass (fold into the state files at merge)
- **Vol 5 better-scan page map** (v5b/v5c): PDF 17–247 printed = PDF − 16; **pp. 232–233 missing** (read from the old `Rig_Vol5.pdf`, PDF 248–249, `V5OLD=1`); PDF 248–467 printed = PDF − 14; **PDF 466–467 duplicate pp. 450–451**; PDF 468–724 printed = PDF − 16 (Pariśiṣṭa p. 531 = PDF 547; p. 644 = PDF 660 exists). `vol5/tools/view.py` can clip the right edge; `view_v5b.py` crops by whole-page fractions.
- **Vol 3:** two OCR commits (ffbb3a0, 870868a) by an earlier session were reverted (wrong substitutions, e.g. p. 467 Pā. 3-3-93 → "1-62"); Ṛk 24.15 OCR-assisted readings (7d0fb01) to be re-checked from crops.
- **Vol 4 page map:** printed = PDF − 14 to PDF 101, PDF 102 duplicates 101, then − 15 (confirmed by v4c through p. 406; p. 368 is printed "268").
