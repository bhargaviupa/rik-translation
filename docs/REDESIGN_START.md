# Prompt for the redesign session (paste into a new Claude Code session on this repo)

You continue the redesign of how the Ṛgveda volumes of this repository (`bhargaviupa/rik-translation`) are made, corrected, checked and published. The thinking was done in an earlier session on Nov 12 2026 and is written down; **nothing of the new design has been built**. Work with the user: they decide, you propose and build in small proven steps.

## Read first, in this order
1. `docs/REQUIREMENTS.md` — what a volume must be (draft 3; Parts A–H; **Part F lists the user's open questions**).
2. `docs/DESIGN.md` — how it is to be done (draft 1): the book as data ("units"), structure by script, packets that the API or agents can do, second reading, release gate, import of old volumes. §12 is the order of building; §13 the assumed answers to the open questions.
3. `docs/ERROR_KINDS.md` — every error kind in the records, scan-based and html-based volumes separately, each with what would prevent or catch it.
4. `docs/review/USER_REVIEW_2026-11-12.md` — the user's review comments, verbatim. The requirements must stay true to them.
5. `docs/TOOLKIT_PROPOSAL.md` (which documents, tools and records to keep) and `docs/LEGACY_VOLUMES_PLAN.md` (Vols 1–10 and 13 at low cost).
6. `CLAUDE.md` for the standing rules (git, honesty, no force-push, spending). `docs/HANDBOOK.md` and `tools/rv/BRIEF.md` describe the present method, which the design replaces; `docs/AUDIT_2026-11-11.md` is a snapshot of all volumes from Nov 11.

**The design (`docs/DESIGN.md`) was approved by the user on Nov 13 2026.** The other documents are still drafts. Do not treat an assumed answer in DESIGN §13 as decided.

## Where things stand (Nov 12 2026)
- **Translated from the supplied text and on `main`:** Vols 11 (new), 12, 14, 15, 16, 17, 18. None meets the requirements yet; all PDFs in `publish/out/` are review copies.
- **Vol 16** was changed on Nov 12 by `tools/rv/to_note_style.py`: layout brought to the Vol 17 form, then comments containing "as supplied" removed. The second step left about 70 places with broken punctuation (measured; see `vol16/STATUS.md`). Not repaired, not reverted: the user has not decided.
- **Vol 13:** old text in `vol13/legacy/`, scaffold for a new translation, supplied text not yet uploaded.
- **Vols 1–10:** scan-based, no Kannada files (except Vol 1), supplied text not in the repo (Vol 5 has one file).
- **Branch `claude/dreamy-cerf-z4h3f4`** is kept unmerged on purpose (DESIGN §7): consult its build-time transliteration and `strip_iast.py` when the printer is built, then it can go.
- **Money:** the user has little API credit left and must be able to choose agents for any task (DESIGN §5.2). Ask for the current figure before proposing anything that spends.
- **Blocking for publication, not for building:** rights in the Kannada edition, the licence of the reference text for the verses, portraits, and the statement of method (REQUIREMENTS H1).

## How to proceed
1. **Go through REQUIREMENTS Part F with the user** (16 questions). Most are print settings and can wait; F1 (deviations), F6 (grammar), F7 (older volumes), F12 (length) and F13 (release standard) shape the build. Update the drafts with each answer.
2. **The design is approved** (Nov 13 2026). Still challenge it where you see a weakness while building; say so plainly and get the user's agreement before departing from it.
3. **Build Phase A only** (DESIGN §12): cut Vol 17 into units from its supplied text and the reference, lay its present English into them, print it in the final format. It costs nothing. Proof to show the user: every English paragraph of today's file placed once; every Sanskrit block equal to the source; verse count equal to the reference; a review PDF. If Vol 17 cannot be cut cleanly, the design is wrong: stop and say so.
4. Then Phases B–G in order, each ending in the test named there. Do not start or change any volume by the present method meanwhile.

## Rules for this work
- No volume file, tool or existing document is changed until the user has approved the step. New code goes beside the old (the old pipeline must keep working until Phase A is proven).
- Every check you write prints how many items it compared.
- Work on the branch this session is given; commit and push; `main` only when the user asks; never force-push.
- Reports say what was verified and how. Estimates are called estimates.
