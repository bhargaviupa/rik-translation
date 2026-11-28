#!/usr/bin/env python3
"""Render the stored common pages in order.json (placeholders as they are) to one review PDF/HTML. Not the embedder."""
import json, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ASSETS = (HERE.parent / 'assets').as_uri()
order = json.loads((HERE / 'order.json').read_text(encoding='utf8'))
body = []
for p in order['pages']:
    if not p['enabled'] or not p['file']: continue
    h = (HERE / p['file']).read_text(encoding='utf8')
    h = h.replace('class="fm ', f'class="fm {"recto " if p["start"]=="recto" else "verso " if p["start"]=="verso" else ""}', 1)
    body.append(h.replace('{{assets}}', ASSETS).replace('{{fm_assets}}', (HERE / 'assets').as_uri()).replace('{{vol}}', '17').replace('{{range_line}}','Maṇḍala 3 · Sūktas 40–62 and Maṇḍala 4 · Sūktas 1–18').replace('{{adhyaya_line}}','Third, Fourth and Fifth Adhyāyas of the Third Aṣṭaka').replace('{{press}}','Sree Vinayak Printing Works, Mysore'))
body = [b.replace('<div class="fm-slot"', '<p>Sample text of the slot, for the preview only.</p><div class="fm-slot"') for b in body]   # a slot has a body, so the footer can be checked
if '--body' in sys.argv:    # a stand-in for the text, to see the footer under the front pages and arabic 1 on its first page
    body.append('<div class="fm-bodystart" data-orig=""></div><h3 class="pg" data-p="1">1</h3><h1>Text of the book</h1><p>First page of the text.</p>')
    sys.argv.remove('--body')
html = ('<!doctype html><meta charset="utf-8"><style>@page{size:6.5in 9.5in;margin:.8in .7in}html{font-size:10pt}</style>'
        f'<link rel="stylesheet" href="{(HERE/"fm.css").as_uri()}"><link rel="stylesheet" href="{(HERE.parent/"style_footer.css").as_uri()}">' + '\n'.join(body))
out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else HERE / 'preview.html')
out.write_text(html, encoding='utf8')
try:
    from weasyprint import HTML
    HTML(string=html, base_url=str(HERE)).write_pdf(str(out.with_suffix('.pdf'))); print('wrote', out.with_suffix('.pdf'))
except ImportError:
    print('wrote', out, '(WeasyPrint not installed: no PDF)')
