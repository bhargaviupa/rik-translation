# Common front and back pages (all volumes)

Stored pages only. Embedding them into the volume PDFs is done by another session's script, which reads `order.json`.

* **Order / insert / delete:** `order.json` is the one list. Remove a page by `"enabled": false`; add one by putting a fragment in `pages/` and adding a row.
* **Each page** is one self-contained `<section class="fm …" data-fm="id">` fragment; styles are in `fm.css` (6.5 × 9.5 in; uses the named pages `front` = no number, `roman` = roman number from `publish/style_footer.css`).
* **Tokens** the embedder replaces: `{{vol}}`, `{{assets}}` (folder of `publish/assets`), and others listed in `order.json`.
* **kind:** `designed` = final (king, guru photos); `placeholder` = dashed frame until the text/design arrives; `slot` = common frame + heading, body filled from the volume (`data-slot`: original_preface, contents, abbreviations, introduction); `volume` = the book text itself (no file).
* **start:** `recto`/`verso` = the embedder adds that class so the page opens on a right/left page (blank page inserted); `any` = follows directly.
* **optional_if_missing:** the introduction row is skipped for a volume that has none.
* Preview of the whole sequence with placeholders: `python3 publish/frontmatter/preview.py` (needs WeasyPrint).
