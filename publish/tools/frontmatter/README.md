# Front matter and contents tools (reusable for every volume)

1. `fm_extract.py UPLOAD.pdf --vol N --roles cover,title,portrait,permission,board,preface1,...`
   Renders the user's scanned front-matter PDF to `publish/assets/volN/fm_NN.jpg` + `frontmatter.json` (role per page).
2. `contents_parse.py VOLUME_MD --check [--fixes volN/contents_fixes.json]`
   Parses the printed contents (ವಿಷಯಾನುಕ್ರಮಣಿಕೆ) of the supplied md; `--check` lists items without a page or with a page that goes down
   (OCR slips). Fixes are `{ "<md line no>": page }` and must be justified in `volN/review/contents_check.md`.
3. `volN/pubcfg.json` (copy `vol15/pubcfg.json`): titles, imprint, which scan role is which page, md paths, missing headings.
4. `python3 publish/volbook.py N [eng|kan]` → `publish/out/volN_full_Eng.pdf` / `_Kan.pdf` (see the module docstring).
Needs `pip install weasyprint` and `apt-get install fonts-lohit-deva fonts-noto-core fonts-lohit-knda`.
