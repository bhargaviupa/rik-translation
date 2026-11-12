# Vol 11 — status

*Moved out of the general CLAUDE.md on Nov 8 2026. Update this file (not CLAUDE.md) whenever the state of this volume changes.*

## Decision (user, Nov 12 2026)
**Vol 11 is to be re-translated from the user's machine-read text**, by the Batch API route with the Vol 17/18 conventions (the old translation, read from page scans, has 2,602 `[?]` marks on 718 printed pages). The old files will be kept untouched in `vol11/legacy/` (to be moved by the session that starts the work). Next: `vol11/CONTINUE_PROMPT_HTML.md` in a new session, after the user uploads the text to `vol11/html/`. Nothing translated yet, nothing sent to the API.

## Scope
Maṇḍala 1 Sūktas 137–157 (Second Adhyāya of the Second Aṣṭaka).

## Source and inputs
Scan in `vol11/scans/`.

## Outputs
`vol11/Rigveda_Samhita_Vol11_English_Translation.md` and `…_Kannada_Text.md` (+ docx/pdf each).

## How it was made
Scan-based legacy workflow; accents by `accent_volume.py` (first volume with accents by script); Kannada text built alongside (decision Oct 2026).

## Status
Translated; accented; Kannada text exists.

## Open items
Verification pass: `docs/SESSION_REPORT_Vol11_verification.md`, `docs/VERIFY_PASS_REQUIREMENTS.md`, `publish/tools/verify11/`.

## Publication (print PDF)
Built with `build_vol45.py 11 full` (accent CSS); `publish/out/vol11_full.pdf`.

## Pointers
`docs/SESSION_REPORT_Vol11_verification.md`.
