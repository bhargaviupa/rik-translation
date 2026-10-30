# Vol 14 — start prompt for a NEW, independent session (not coordinated or monitored by any other session)

How to use: open a fresh Claude Code session on the repo `bhargaviupa/rik-translation` and paste everything below the line. Upload the scan parts to `vol14/scans/` first (or tell the session where they are). For every later session paste `vol14/CONTINUE_PROMPT.md` instead.

---

You are translating Volume 14 of the Rigveda Samhita (a 1949 Kannada commentary: Sāyaṇa's Sanskrit bhāṣya + H. P. Venkata Rao's Kannada explanation) into English. This session is independent: no coordinator, nobody monitors it. You work alone and report to me (the user) in this chat.

REPO RULES. Repo bhargaviupa/rik-translation. Create your own branch `claude/vol14` from origin/main (git fetch origin main; git checkout -B claude/vol14 origin/main); push with `git push -u origin claude/vol14` after every sūkta, or after every ~15 printed pages, whichever comes first. Never force-push, never reset a pushed branch, no pull requests, merge into main only when I say. Do not edit any file outside vol14/ and `Rigveda_Samhita_Vol14_English_Translation.md` (and `..._Kannada_Text.md` if I ask for it). Commit messages end with the attribution lines given in your system reminder.

READ FIRST: CLAUDE.md (conventions: three-layer Sanskrit = Devanagari + IAST + English; per-Ṛk structure; progress note pattern; digit key; cost-saving rules for Vol 11 onwards), then vol14/README.md, vol14/vol14_state.md, vol14/vol14_runbook.md. For style, look at an already finished Vol 11 sūkta in `Rigveda_Samhita_Vol11_English_Translation.md` and copy its format. (Vol 13 is being done in another session on branch claude/vol13; you may read its notes/runbook from there if useful, but do not edit them.)

SCAN. `vol14/scans/` (parts in page order; `vol14/tools/cfg.py` maps a global PDF page to a part + page; `git lfs pull` if the files are pointers). Use the best scan only; the older single-file `Rig_Vol14.pdf` at the repo root (if present) is a fallback. A first thing to check: whether any scan pages are upside down or missing/duplicated (vol14/tools/orient_v14.py is a locating aid; in Vol 13 none were upside down).

PHASE 1 — SET-UP (do it once; then tell me the results and WAIT for my go-ahead before translating):
1. Page map: printed page = PDF − k (read printed page numbers/headers from crops you viewed; note where k changes; list missing/duplicate/out-of-order pages); set OFFSET in vol14/tools/cfg.py.
2. Read the title page, contents table (viṣayānukramaṇike) and Pīṭhike headings: record in vol14/vol14_state.md the Maṇḍala / Aṣṭaka / Adhyāya / Sūkta range, Ṛk counts per sūkta, dvaipada sūktas, the printed start page of each sūkta; update vol14/README.md.
3. Digit key: confirm the key of CLAUDE.md on ~20 headings/varga numerals/references at 300–450 dpi crops (Kannada ೧ ೨ ೩ ೪ ೫ ೬ ೭ ೮ ೯ ೦; usual confusions 2/7, 3/5, 6/7, 8/9); record any glyph rules.
4. Scan quality: view 5 pages (including a dense reference page and a grammar page) and tell me how legible the small numerals are at this scan's resolution; ask me whether I want (a) English only or (b) English + the Kannada text file alongside (as Vol 11), and which model to use for drafting.
5. Make small tools only if needed (crop by whole-page fractions; stack several line crops into one image; apply edits with unique-match asserts; a Kannada→Devanagari→IAST converter: see publish/tools/translit/add_iast.py).

PHASE 2 — TRANSLATION (after my go-ahead), sūkta by sūkta, in the format of Vol 11 (per Ṛk: Saṃhitā-pāṭha, Pada-pāṭha, Sāyaṇa-bhāṣya kept in Sanskrit with a one-line gist (≤ 25 words) where needed, Pratipadārtha, Bhāvārtha, printed English, Special Topics, grammar pages noted briefly). Keep a page-anchored structure: mark each printed page number as you reach it, never carry numbers from another scan. Read numerals at zoom the first time (never from memory); `[?]` only where still undecidable. Printed English of each Ṛk: reproduce from the page as printed, misprints marked [sic]. IAST layer by script (python3 publish/tools/translit/add_iast.py FILE.md). No OCR for readings (Tesseract may only help locate a line). If an image view returns no image: STOP and write nothing for that page.

SESSION LIMITS (important). A session can only look at about 45–60 images before its context fills; view stacked line crops (several lines per image), not whole pages at high dpi, and push often. After every sūkta (or ~15 pages) update vol14/parts/session_state.md (done through printed page / Ṛk, next step, open doubts) and the file's trailing **Progress note**. When your context is getting full, finish the current Ṛk, push, update the state, and tell me: "start a new session with vol14/CONTINUE_PROMPT.md".

DOUBTS. Keep a running list of unresolved readings in vol14/review/doubts_pFIRST-LAST.json (rows {page, y0, y1 (fractions of the WHOLE page height; a band of a few lines), kind, file, ctx, note}) and build a single review page for me with vol14/tools/doubts_v14.py when I ask.

Keep replies short. Begin with PHASE 1.
