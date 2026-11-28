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

## Where the tokens of pages 01–02 are read (embedder to implement; page 03–06 need only `{{assets}}`)
| token | read from | a volume without `pubcfg.json` |
|---|---|---|
| `{{vol}}` | `volN/pubcfg.json` `vol` | `volN/volcfg.json` `vol` (present in all volumes) |
| `{{vol_roman}}` | computed from `vol` | same |
| `{{range_line}}`, `{{adhyaya_line}}` | `pubcfg.json` | **missing**: only prose in `volN/STATUS.md` (no field); `volcfg.json` has just `mandala(s)` |
| `{{imprint}}`, `{{year}}` | `pubcfg.json` | **missing** (press, year of the original; `press` also absent in Vols 15) |
| `{{release.publisher}}`, `.isbn`, `.edition_and_printing`, `.rights_statement` | `publish/release.json` (empty now: print the placeholder) | same |
| `{{vol_title}}` | no source exists in any volume; not used by the pages, drop it from the list unless a title field is added | |
Volumes with a `pubcfg.json` today: 1, 11, 15, 17, 18, 19, 20, 21, 23, 27, 30.

## King and guru photos (user, Nov 28 2026)
Both are taken from the Vol 1 front matter, from the user's high-resolution scans (`pic-king.pdf`, `pic-guru.pdf`, 1-bit, 567/585 ppi). `assets/king_vol1.jpg` and `assets/guru_vol1.jpg` are the photo plus the printed Kannada caption (inside the picture; the English caption stays as text under it), the ornamental border cut away, grey-scaled to 1600 px wide. Pages 03 and 04 use them through the token `{{fm_assets}}` (= `publish/frontmatter/assets`, a new token for the embedder); the old low-resolution `publish/assets/maharaja.jpg` / `guruji.jpg` are no longer used by these pages (the old builders still use them).

## Title page (page 01, from the user's Vol 1 scan `pic-front.pdf`, Nov 28 2026)
`assets/title_frame_vol1.jpg` is the ornamental frame of the Vol 1 title page (the scan is 1664×2193, 1-bit, the same as `publish/assets/cover_vol1.jpg`) with its centre text and the press plaque cleared. Page 01 sets, per volume: `{{vol}}`, `{{range_line}}`, `{{adhyaya_line}}` in the centre and `{{press}}` in the plaque (all from `volN/pubcfg.json`; Vol 15's pubcfg has no `press`, volumes without a pubcfg have none of them). Tokens added: `{{press}}`, `{{fm_assets}}`. The frame is 5.1 in wide (trim 6.5 in minus margins .7 in); the text sizes are in pt for that width.

## Imprint page (page 02, Nov 28 2026)
The layout of the typeset title page the builders made (user's `pic-trans.pdf`), inside the same plate border as the thank-you page (`assets/thanks_frame_vol1.jpg`, deskewed 0.8° and trimmed). The line "prepared with the assistance of Claude, an AI model by Anthropic" is removed (user). Tokens: `{{vol}}`, `{{range_line}}`, `{{adhyaya_line}}`, `{{imprint}}`, `{{release.*}}`.

## Present-day page (page 05, Nov 28 2026)
Upper half: the guru-parampara picture (`assets/present_gurus.jpg`, supplied by the user, black-and-white for now, the corner mark cropped off, the trust's banner kept as supplied) with a caption placeholder; lower half: placeholder for the present king's portrait (not yet received).
