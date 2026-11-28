# Prompt for the session that embeds the common front pages 01–06 into the volume PDFs

Pages 01–06 are finished as far as the user has decided (title, imprint, king, guru, present-day, thank-you). Your job is only to make the embedding script **use them**; you do not redesign them. The **texts of the present-day and thank-you pages (and any change to the imprint page) are not decided yet**: the user will supply them later, so the script must take them from the page files (and `publish/release.json`), never hard-code them.

## Where things are
Branch `claude/clever-lamport-qr34vh` (merge `origin/main` and that branch if the last commits `e71a1017`, `6495a061` are not yet in `main`). Folder `publish/frontmatter/`: `order.json` (the one list: order, `enabled`, `start` recto/verso, `numbering`, master switch `"embed": false`), `pages/01_title.html` … `06_thank_you.html`, `fm.css`, `assets/`, `preview.py` (review aid only), `README.md` (the contract; read it first).

## The six pages
| page | file | content | per volume? |
|---|---|---|---|
| 01 title | `01_title.html` | Vol 1 title-page frame (`assets/title_frame_vol1.jpg`, centre and press plaque cleared) + live text: `{{vol}}`, `{{range_line}}`, `{{adhyaya_line}}` in the centre, `{{press}}` in the plaque | yes |
| 02 imprint | `02_imprint.html` | the layout of the typeset title page the builders made (invocation, title, volume and scope `{{range_line}}`/`{{adhyaya_line}}`, translator, source edition `{{imprint}}`, © 2026 line, release lines) inside the plate border (`assets/thanks_frame_vol1.jpg`); **no reference to Claude or to how the file was made**; texts may still be edited by the user | yes (`{{vol}}`, scope, imprint) + `publish/release.json` (empty now: print its "to be supplied" placeholder) |
| 03 king | `03_king_photo.html` | `assets/king_vol1.jpg` (user's Vol 1 scan) + English caption | no |
| 04 guru | `04_guru_photo.html` | `assets/guru_vol1.jpg` + English caption | no |
| 05 present day | `05_present_day.html` | two placeholder frames on one page (photos and captions to come) | no |
| 06 thank you | `06_thank_you.html` | `assets/thanks_frame_vol1.jpg` (empty ornamental plate border) with heading "With Gratitude" and a **placeholder** for the text | no |

## Tokens the embedder replaces (no others)
`{{vol}}`, `{{vol_roman}}`, `{{range_line}}`, `{{adhyaya_line}}`, `{{imprint}}`, `{{year}}`, `{{press}}` ← `volN/pubcfg.json` (`vol` also from `volN/volcfg.json`); `{{release.*}}` ← `publish/release.json`; `{{assets}}` = `publish/assets`; **`{{fm_assets}}` = `publish/frontmatter/assets`** (new). Volumes with a `pubcfg.json` today: 1, 11, 15, 17, 18, 19, 20, 21, 23, 27, 30; Vol 15 has no `press`; a volume without a pubcfg lacks range, adhyāya, imprint, press and year (there is no machine-readable source: say what the title page does then, e.g. leave the lines out, and report it; do not invent text). `{{vol_title}}` has no source and no page uses it.

## What the script must do
1. Insert the enabled pages 01–06 of `order.json`, in order, at the start of the finished HTML (last step of `printfix.fix()`, one place for `build.py`, `build_vol1/2/45.py` and `volbook.py`), and remove what the builders emit today in their place (cover, title page, copyright, king, guru, present-day sections: class names `cover`, `titlepage`, `copyright`, `portrait`, `portrait pair`). Pages 07 onward belong to a different piece of work; leave them.
2. Honour `start` (recto/verso: add a class and let `fm.css` open the page on that side; blank pages carry no number) and `numbering: none` for 01–06 (named page `front`, no footer). **No volume's PDF may change while `"embed": false`**; the user turns it to `true`.
3. Do not touch the footer rules (`publish/style_footer.css`, `printfix.stamp`); `fm.css` only sets the footer name string `orig` (empty on these pages).
4. Layout facts: trim 6.5 × 9.5 in; the two framed pages (01, 06) are fixed at **5.1 in wide** (trim minus .7 in margins) with text sizes in pt for that width: if a builder uses other margins, report it, do not rescale silently.
5. Images are loaded by file URL relative to the built HTML: check that `{{assets}}`/`{{fm_assets}}` resolve from where each builder writes its HTML.

## Test (no volume PDFs committed, no `build_all.py`)
Render a saved HTML of one old-builder volume (Vol 7) and one `volbook.py --html-only` volume (Vol 21) with `embed` set to true in a scratch copy of `order.json`; fonts: `apt-get install -y fonts-noto-core fonts-lohit-deva fonts-lohit-knda`, `pip install weasyprint`. Look at pages 1–7 as images (title with the volume's own numbers and press, king, guru, present-day, blank, thank-you) and report what you saw, with the numbers a volume without pubcfg gets.

## Do not
Edit the page files' design, `docs/REQUIREMENTS.md` A2a, `publish/release.json`, a volume's text or `pubcfg.json`; push to `main` (push to your branch, the user merges).
