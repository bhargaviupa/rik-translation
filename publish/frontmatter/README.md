# Common front and back pages (all volumes)

Stored pages only. Embedding them into the volume PDFs is done by another session's script, which reads `order.json`.

* **Order / insert / delete:** `order.json` is the one list. Remove a page by `"enabled": false`; add one by putting a fragment in `pages/` and adding a row.
* **Each page** is one self-contained `<section class="fm …" data-fm="id">` fragment; styles are in `fm.css` (6.5 × 9.5 in; uses the named pages `front` = no number, `roman` = roman number from `publish/style_footer.css`).
* **Tokens** the embedder replaces: `{{vol}}`, `{{assets}}` (folder of `publish/assets`), and others listed in `order.json`.
* **kind:** `designed` = final (king, guru photos); `placeholder` = dashed frame until the text/design arrives; `slot` = common frame + heading, body filled from the volume (`data-slot`: original_preface, contents, abbreviations, introduction); `volume` = the book text itself (no file).
* **start:** `recto`/`verso` = the embedder adds that class so the page opens on a right/left page (blank page inserted); `any` = follows directly.
* **optional_if_missing:** the introduction row is skipped for a volume that has none.
* Preview of the whole sequence with placeholders: `python3 publish/frontmatter/preview.py` (needs WeasyPrint).

## Contract with the volume sessions (Nov 28 2026; docs/prompts/FRONT_PAGES_ALIGNMENT_PROMPT.md)
* `order.json` has `"embed": false` (master switch; the user sets `true`). Nothing in this folder changes a volume PDF while it is false.
* Frame headings carry `data-orig` and `fm.css` sets the footer string `orig` from it: "Pīṭhike" (Preface), "Pūrva-pīṭhikā" (Introduction), empty everywhere else, so no name stays on later pages.
* Row `body`: the embedder inserts `<div class="fm-bodystart" data-orig=""></div>` before the text; it opens a right page, clears the footer name and makes that page arabic 1 (named page `fmbody`). Blank pages from `start: recto/verso` carry no number and count in the roman numbers.
* The closing-remarks row is `"enabled": false` until it has text.
* `python3 publish/frontmatter/preview.py --body` previews with sample slot text, the footer rules and a stand-in for the text.

## Ownership (user, Nov 28 2026)
The front-pages session owns only the rows up to and including the thank-you page (`title`, `imprint`, `king`, `guru`, `present_day`, `thanks`). The rows from `our_preface` on (our preface, original preface, contents, abbreviations, introduction, body marker, closing) and the embedder belong to other sessions; what is stored for them here is a starting point they may change or replace.
