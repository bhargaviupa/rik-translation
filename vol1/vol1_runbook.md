# Vol 1 finalisation pass — runbook for unattended sessions

Authorised by the user (Oct 27, 2026): finish Vol 1 by **the Vol 2 method** (Claude reads every crop from the better
scan; no readings from the user are awaited), **up to PDF 743 (printed p. 715)**. The pages after it (the alphabetical
mantra index, PDF 744–945) are out of scope. Vol 1 files (`vol1/Rigveda_Samhita_Vol1_English_Translation.md`, the main
file, and `vol1/Rigveda_Samhita_Vol1_Gaps_English_Translation.md`, the late-translated portions) are opened for
**numeral corrections, `[?]` resolution, correction of other errors found against the better scan, and the Saṃhitā
accents**. Nothing else changes. `vol1/kannada/` (the Kannada text and its review list) is **not** part of this pass —
leave it alone. No other volume is touched.

Work on the branch the session is given (or `claude/numerals-vol2`, which carries the `vol1/` layout); commit and push
after every batch; **merge into `main` only when the user says so**; no PRs; never `git reset --hard`, never force-push.
No progress messages to the user. Each run is a fresh session: read this file and `vol1/vol1_state.md` first, continue
from where `vol1_state.md` says, update `vol1_state.md` (done / to do / open readings / to be reviewed) before stopping.

## Where Vol 1 starts from
The numeral pass is already done for PDF 1–743 (user's readings placed, logged in `vol1/vol1_pass_log.md`; word-[?]
pass in `vol1/vol1_qmarks_log.md`). What is left is a **finishing pass** over the same pages:
1. every `[?]` still in the two files (≈105 main, ≈14 Gaps — many are header-note conventions, not open readings);
2. numerals the locator never boxed (look for `[?]`, `.?`, `?-` placeholders and "as I read" hedges in references);
3. the Saṃhitā-pāṭha accents of Sūktas 1–2 (18 Ṛks; the blocks already carry accents, but they were never checked
   against the print);
4. the reviewer worklist cross-check;
5. end-of-volume rebuild.

## Inputs (all under `vol1/`; see `vol1/README.md`)
- The two translation files above.
- Better scan in `vol1/scans/`, ten parts (Git LFS — `git lfs pull` if a file is a small pointer), global PDF page →
  part by `vol1/tools/cfg.py` (`part_of()`): parts start at PDF 1, 101, 201, 301 (named `… 4,pdf.pdf`), 401, 501, 601,
  701, 801, 876. Original scans `Rig_Vol1(1).pdf`, `Rig_Vol1(2).pdf` for comparison only.
- Page map (`vol1/tools/pages.py`, `printed()`): printed = PDF − 24 for PDF 25–383, with duplicates/gaps after it
  (PDF 384–385 repeat pp. 358–359; pp. 372–373, 447 missing; PDF 410–411, 475, 508–509 duplicates); PDF 510–743 =
  printed PDF − 28. Front matter and skipped pages: `FRONT`, `DUP`, `SKIP` in `pages.py` / `build_review.py`.
- Tools in `vol1/tools/` (run them from that folder; file paths below are from the repository root — from
  `vol1/tools/`, `vol1/review/…` is `../review/…`): the Vol 1 pass tools (`qctx.py en|gaps PRINTED` lists the `[?]` of
  a page; `hedge.py`; `secrep.py`, `apply.py` (`[file, old, new]`, file = `en` or `gaps`), `addnote.py`, `pass_log.py`,
  `view.py`, `crop.py`) plus the Vol 2 reading tools (`montage.py`, `zc.py`, `zoom.py`, `acc.py`, `ruler.py`,
  `samcrop.py`, `accent.py`, `sam.py`). Existing review pages and the user's readings: `vol1/review/`.

## Steps (per run, in 100-PDF-page batches: 1–100, 101–200, … 701–743)
1. **List the open spots** of the batch: `qctx.py` per printed page for both files, plus a grep for placeholders
   (`[?]`, `.?`, `?-`, "as I read", "[number as printed") in the batch's sections. Skip header-note conventions
   ("[?] where unclear"), but reword them to "no open reading" when the page no longer has one.
2. **Read every spot yourself** from the better scan: `ruler.py OUT.png PDF` to locate the line, then `acc.py PDF Y0 Y1
   OUT.png [x0 x1]` (450 dpi strip) or `zc.py REVIEW.json OUT.png ID…` / `zoom.py` for boxed numerals. Digit key: ೧ ∩;
   ೦ ○; ೭ flat-footed "2"; ೨ curled "2"; ೬ hook top-left; ೮ like ಲ; ೯ like ಕ; ೪ like ಳ; ೫ like ಣ/ಜ; ೩ like ಇ.
   Usual confusions 3/5, 6/7, 2/9, 8/9, 2/7 — zoom every doubtful digit; check sequences and printed totals. The
   user's earlier readings (`vol1/review/edits_*.txt`) win where they exist; change one only if the print plainly
   shows a slip, and say so in the notes.
3. **Place the readings** (`apply.py`, `secrep.py`, `addnote.py`): hyphen form `2-1-14` (never `2.1.14`); `[as
   printed]` where the print differs from the usual number; keep `[?]` only where the print does not settle it. Re-read
   garbled Sanskrit/Kannada next to the spot from the print (Devanagari + IAST by `add_iast.py`'s `deva_to_iast`);
   never fill from memory; glosses not in the source are "mine and tentative". Fix the IAST line whenever its
   Devanagari changes. Do not change the printed English blocks.
4. **Other errors:** while the page is open, correct clear misreadings next to what you checked (wrong numbers, names,
   counts, a grammar summary that misstates the print). Do not restyle sound text.
5. **Saṃhitā accents** (batch with Sūktas 1–2): for each Ṛk's Saṃhitā-pāṭha block, read the marks with `samcrop.py`
   (guide lines for svarita strokes and anudātta bars) and rewrite the block with `sam.py` where it differs: anudātta ॒
   below, svarita ॑ above, udātta unmarked; the mark goes **after** a visarga/anusvāra (`नः॑`, never `न॑:` with a
   colon); print anusvāra kept. `[accent ?]` after a line where a mark cannot be read. Pada-pāṭha stays unaccented.
5b. **Reviewer worklist:** `publish/review/All_volumes_review_worklist.xlsx` (sheet "Worklist", Volume "Vol 1", by
   "Original page"): apply any filled "Reviewer's reading" / "Decision"; make sure every flag it lists for the batch
   is resolved or listed in `vol1_state.md`. Its page numbers come from an older build and can be off.
6. **Log:** notes in `vol1/review/notes_finish_PDFA-B.txt`; `pass_log.py A B NOTES` (appends to
   `vol1/vol1_pass_log.md`). Commit and push.
7. **Update `vol1_state.md`**, commit, push.

## When PDF 743 is done
Rebuild the print PDF (`python3 publish/build_vol1.py full`; needs `pip install weasyprint pypandoc` and
`apt-get install fonts-lohit-deva fonts-noto-core`), check there are no dotted circles (◌) in `pdftotext`, commit
`publish/out/vol1_full.pdf` and `publish/work/vol1_clean.md`; regenerate the worklist (`python3 publish/review_all.py`);
write "done" in `vol1_state.md`.

The earlier session prompt (user-review method) is kept as `vol1/vol1_review_prompt.md`; the earlier handoff with the
pass's rules as `vol1/vol1_handoff.md`.
