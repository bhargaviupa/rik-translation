# Prompt for the front-pages session (the one that made `publish/frontmatter/` on branch `claude/clever-lamport-qr34vh`): scope limited to pages 1–6; align before the merge

**Your scope (user, Nov 28 2026): only the pages up to and including the thank-you page** — the two title pages (`01_title`, `02_imprint`), the king, the guru, the present-day page, the thank-you page (`03`–`06`). Nothing after the thank-you page is yours any more: not our preface (`07`), not the frames of the original preface, contents, abbreviations and introduction (`08`–`11`), not the closing-remarks page (`12`), and **not the embedding script**. Leave the files `07`–`12` in the folder exactly as they are (do not edit, delete or extend them) and do not build an embedder: they are taken over by a separate piece of work after the merge.

## 0. Set-up
`git fetch origin main && git merge origin/main` into your branch (it is based on an older `main`). Read `docs/REQUIREMENTS.md` **A2a** (order of the pages, and the user's decisions of Nov 28 2026) and **A4 "Print rules"**, `publish/style_footer.css` (footer of every page: REVIEW COPY, page number, "Kannada edition p. N", build number). Install the fonts: `apt-get install -y fonts-noto-core fonts-lohit-deva fonts-lohit-knda` and `pip install weasyprint pypandoc lxml`; **render with the real fonts** (a preview in fallback fonts proves nothing). `publish/tools/frontmatter/` (older tools) is a different folder from your `publish/frontmatter/`.

## 1. What to carry into pages 1–6
1. Pages 1–6 carry **no page number** (`numbering: none`); the blank pages that a `recto`/`verso` start adds carry none either and **count** in the numbering that follows (the roman numbers of the later pages continue after them). Check `@page :blank` prints nothing.
2. **No Kannada script** in any page text (the photos' own captions inside the pictures are fine), nothing about Claude or how the file was made, no remark of ours.
3. The imprint page takes its values from `publish/release.json` (rule 6: rights, ISBN, publisher live only there); the title page takes the volume's values from `volN/pubcfg.json`, or `volN/volcfg.json`/`volN/STATUS.md` where a volume has none: say in the hand-over which token reads which file, and which fields a volume without `pubcfg.json` lacks.
4. The king and guru pages stay as they are; the present-day page keeps its two frames on one page.
5. Do not duplicate the footer rules (REVIEW COPY, build number, original's page) in `fm.css`: they are the shared ones in `publish/style_footer.css` and `printfix.stamp`. A change there is a rule first (A4), then code in the shared step.

## 2. Do not
Do not edit a volume's text or `pubcfg.json`, the cleaners, `printfix.py`, `publish/style_footer.css`, `publish/build*.py`, `publish/volbook.py`, `docs/REQUIREMENTS.md` (the user's decisions: if you disagree, say so), or `publish/release.json`. Do not run `build_all.py` and do not commit any volume PDF. Do not push to `main`; push to your branch; the user merges. Your preview (`preview.py`) stays a review aid.

## 3. Hand over
In a few lines: what you changed (points 1–4); where the title and imprint read their values; what you saw in the rendered pages (with the real fonts, as images); anything in A2a that contradicts your pages. Do not report on pages 7–12.
