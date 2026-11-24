#!/usr/bin/env python3
"""Contact sheet of the pictures of a volume's supplied text (shared tool; Vol 17 first).

  python3 tools/rv/figures_sheet.py VOL [--pdf]

Reads volN/html/<file>.md (the file named in volN/volcfg.json 'source', or the only .md in volN/html), finds every line
`[figure: PATH]`, and writes volN/review/VolN_pictures.html (and .pdf with --pdf, needs weasyprint): for each picture its number,
file, printed page, source line, the machine reading of the picture that follows it in the file, the line before it, and a suggested class
(decorative / verse / other text). The sheet changes nothing; it is for the editor to decide what is done with the pictures.
"""
import os, re, sys, html, json
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')); sys.path.insert(0, os.path.dirname(__file__))
import html_pages
from PIL import Image
vol = sys.argv[1]; pdf = '--pdf' in sys.argv
V = os.path.join(ROOT, f'vol{vol}'); H = os.path.join(V, 'html')
src = None
try:
    c = json.load(open(os.path.join(V, 'volcfg.json'), encoding='utf8'))['source']
    src = os.path.join(ROOT, c[0].split('@')[0]) if isinstance(c, list) else None
except Exception: pass
if not src or not os.path.exists(src):
    mds = sorted(f for f in os.listdir(H) if f.endswith('.md')); assert mds, 'no .md in ' + H
    srcs = [os.path.join(H, f) for f in mds]; src = srcs[0]          # several supplied files: all are read, in name order
else: srcs = [src]
SRC = []
for sp in srcs:
    try: pg = html_pages.load(sp)
    except ValueError: pg = {}
    wh = {}
    for p, t in pg.items():
        for m in re.finditer(r'\[figure: ([^\]]+)\]', t): wh[m.group(1)] = p
    SRC.append((sp, open(sp, encoding='utf8', errors='replace').read().split('\n'), wh))
VERSE = ('ಸಂಹಿತಾಪಾ', 'ಪದಪಾ', 'ಪದಸಾ', '॥', '||', '|')
def classify(cap, before):
    c = cap.strip()
    if not c: return 'no machine reading'
    if re.search(r'contains no text|decorative|illustration|portrait|photograph|emblem', c, re.I): return 'decorative picture'
    if any(x in before for x in ('ಸಂಹಿತಾಪಾ', 'ಪದಪಾ', 'ಸಂಹಿತಾಪಾರ')) or '||' in c or '॥' in c or '।' in c: return 'verse (Saṃhitā / Pada) or quotation'
    return 'other text'
items = []
for src, lines, where in SRC:
  for i, l in enumerate(lines):
      m = re.fullmatch(r'\[figure: ([^\]]+)\]', l.strip())
      if not m: continue
      path = m.group(1); b = i - 1
      while b >= 0 and not lines[b].strip(): b -= 1
      before = lines[b].strip() if b >= 0 else ''
      cap = []; k = i + 1
      while k < len(lines) and not lines[k].strip(): k += 1
      while k < len(lines) and lines[k].strip() and not lines[k].startswith('[figure:') and len(cap) < 14: cap.append(lines[k]); k += 1
      cap = '\n'.join(cap)
      try: w, h = Image.open(os.path.join(ROOT, path)).size
      except Exception: w = h = 0
      items.append(dict(n=len(items) + 1, path=path, line=i + 1, page=where.get(path), file=os.path.basename(src), before=before, cap=cap, cls=classify(cap, before), w=w, h=h))
out = os.path.join(V, 'review'); os.makedirs(out, exist_ok=True)
from collections import Counter
cnt = Counter(x['cls'] for x in items)
E = lambda s: html.escape(s)
h = [f'<!doctype html><html><head><meta charset="utf-8"><title>Vol {vol}: pictures of the supplied text</title><style>',
     '@page{size:A4;margin:16mm 14mm;@bottom-center{content:"Vol %s pictures · " counter(page);font-size:8pt;color:#666}}' % vol,
     'body{font-family:"DejaVu Sans","Noto Sans",sans-serif;font-size:9.5pt}h1{font-size:16pt}',
     'table{border-collapse:collapse;font-size:9pt}td,th{border:1px solid #bbb;padding:3px 7px}',
     'section.f{page-break-inside:avoid;border-top:1px solid #999;margin-top:14px;padding-top:6px}',
     'section.f img{max-width:100%;max-height:105mm;border:1px solid #ccc}pre{white-space:pre-wrap;font-family:"Noto Sans Kannada","Lohit Kannada","DejaVu Sans",sans-serif;font-size:9pt;background:#f6f6f6;padding:4px}',
     '.c{font-weight:bold}</style></head><body>',
     f'<h1>Volume {vol}: the pictures of the supplied text</h1>',
     f'<p>{len(items)} pictures in <code>{E(os.path.relpath(src, ROOT))}</code>. This sheet decides nothing: it shows each picture with the machine reading that follows it in the file, so that the editor can say what is done with each kind. Suggested classes come from the machine reading only.</p>',
     '<table><tr><th>Suggested class</th><th>Pictures</th></tr>' + ''.join(f'<tr><td>{E(k)}</td><td>{v}</td></tr>' for k, v in sorted(cnt.items())) + '</table>',
     '<p>Index: ' + '; '.join(f'{x["n"]} (p. {x["page"]})' for x in items) + '</p>']
for x in items:
    h.append(f'<section class="f"><div class="c">Picture {x["n"]} of {len(items)} — printed p. {x["page"]} — {x["file"]} line {x["line"]} — {x["w"]}×{x["h"]} px — <i>{E(x["cls"])}</i></div>'
             f'<div>file: <code>{E(x["path"])}</code></div>'
             f'<img src="{os.path.relpath(os.path.join(ROOT, x["path"]), out)}">'
             f'<div>Line before the picture: <code>{E(x["before"][:140])}</code></div><div>Machine reading that follows it:</div><pre>{E(x["cap"]) or "(none)"}</pre></section>')
h.append('</body></html>')
hp = os.path.join(out, f'Vol{vol}_pictures.html'); open(hp, 'w', encoding='utf8').write('\n'.join(h)); print(len(items), 'pictures;', dict(cnt), '→', os.path.relpath(hp, ROOT))
if pdf:
    import weasyprint
    pp = os.path.join(out, f'Vol{vol}_pictures.pdf'); weasyprint.HTML(hp).write_pdf(pp); print('pdf:', os.path.relpath(pp, ROOT), os.path.getsize(pp) // 1024, 'KB')
