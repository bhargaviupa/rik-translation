#!/usr/bin/env python3
"""Review pages for the [?] flags of a volume: one self-contained HTML per sūkta with, for each flag,
the PDF page, an image crop of the estimated place on the Kannada page, and the words around the [?].
usage: make_review.py MD PDF OUTDIR [--dpi 130] [--procs 4]
The y-position of a flag on the page is ESTIMATED from its relative position in the text written for that page
(sections of one page share the page height in proportion to their length), so the crop is a generous band."""
import re, sys, os, base64, html, json, subprocess, tempfile, argparse, io
from multiprocessing import Pool
from PIL import Image

def parse(md):
    L = md.split('\n'); suk = 'Front matter'; rik = ''; secs = []; cur = None
    for line in L:
        m = re.match(r'## (Sūkta \d+[^\n]*)', line)
        if m: suk = m.group(1); rik = ''; cur = None
        m = re.match(r'#### (Ṛk \d+.*)', line)
        if m: rik = m.group(1)
        m = re.match(r'### Printed p\. (\d+)(.*?)\(PDF (\d+)', line)
        if m:
            cur = dict(printed=int(m.group(1)), pdf=int(m.group(3)), suk=suk, rik=rik, lines=[], flags=[])
            secs.append(cur); continue
        if line.startswith('**Progress note:**'): cur = None
        if cur is not None:
            if line.startswith('#### Ṛk'): pass
            cur['lines'].append((rik, line))
    return secs

def strip_md(t): return re.sub(r'[*_`>]+', '', t)

def build(md):
    secs = parse(md); items = []
    bypage = {}
    for s in secs:
        s['text'] = '\n'.join(l for _, l in s['lines']); bypage.setdefault(s['pdf'], []).append(s)
    for pdf, ss in bypage.items():
        tot = sum(max(len(s['text']), 1) for s in ss); acc = 0
        for s in ss:
            n = max(len(s['text']), 1); lo, hi = acc / tot, (acc + n) / tot; acc += n
            pos = 0
            for rik, line in s['lines']:
                for m in re.finditer(r'\[\?\]', line):
                    off = pos + m.start()
                    fr = lo + (hi - lo) * (off / n)
                    b = strip_md(line[:m.start()]).split()[-14:]; a = strip_md(line[m.end():]).split()[:14]
                    items.append(dict(suk=s['suk'], rik=rik or '', pdf=pdf, printed=s['printed'], frac=fr,
                                      before=' '.join(b), after=' '.join(a)))
                pos += len(line) + 1
    return items

def crop(args):
    pdf, pg, fracs, dpi = args
    with tempfile.TemporaryDirectory() as d:
        subprocess.run(['pdftoppm', '-r', str(dpi), '-gray', '-f', str(pg), '-l', str(pg), '-png', pdf, d + '/p'], check=True)
        im = Image.open(os.path.join(d, [x for x in os.listdir(d) if x.endswith('.png')][0])).convert('L')
    W, H = im.size; top = int(H * 0.06); bot = int(H * 0.95); body = bot - top; out = []
    for f in fracs:
        yc = top + int(body * min(max(f, 0), 1)); half = int(H * 0.15)
        y0 = max(0, yc - half); y1 = min(H, yc + half)
        c = im.crop((0, y0, W, y1)).convert('RGB')
        from PIL import ImageDraw
        dr = ImageDraw.Draw(c); ty = yc - y0
        dr.polygon([(0, ty - 7), (14, ty), (0, ty + 7)], fill=(200, 0, 0)); dr.polygon([(W, ty - 7), (W - 14, ty), (W, ty + 7)], fill=(200, 0, 0))
        buf = io.BytesIO(); c.save(buf, 'JPEG', quality=50); out.append(base64.b64encode(buf.getvalue()).decode())
    return pg, out

CSS = """body{font-family:system-ui,sans-serif;max-width:980px;margin:0 auto;padding:16px;background:#fafafa;color:#222}
.card{background:#fff;border:1px solid #ccc;border-radius:6px;padding:10px;margin:14px 0}
.hd{font-size:13px;color:#555;margin-bottom:6px}.hd b{color:#000}
img{width:100%;border:1px solid #bbb;display:block}
.ctx{font-size:16px;margin:8px 0;line-height:1.5}.q{background:#ffe08a;font-weight:bold;padding:0 3px;border-radius:3px}
.in{display:flex;gap:8px;flex-wrap:wrap}.in input{flex:1;min-width:220px;padding:5px}.in select{padding:5px}
.note{font-size:12px;color:#777}button{padding:6px 12px;margin:2px}nav a{margin-right:10px}
@media (prefers-color-scheme:dark){body{background:#181818;color:#ddd}.card{background:#222;border-color:#444}.hd b{color:#fff}.q{color:#000}}"""
JS = """const K='rev_'+document.title;function sv(){const d={};document.querySelectorAll('.card').forEach(c=>{d[c.id]=[c.querySelector('.rd').value,c.querySelector('.dc').value,c.querySelector('.cm').value]});localStorage.setItem(K,JSON.stringify(d))}
function ld(){try{const d=JSON.parse(localStorage.getItem(K)||'{}');for(const id in d){const c=document.getElementById(id);if(c){c.querySelector('.rd').value=d[id][0];c.querySelector('.dc').value=d[id][1];c.querySelector('.cm').value=d[id][2]}}}catch(e){}}
function ex(){let r=[['ID','PDF page','Printed page','Before','After','Reading','Decision','Comment']];document.querySelectorAll('.card').forEach(c=>{r.push([c.id,c.dataset.pdf,c.dataset.pr,c.dataset.b,c.dataset.a,c.querySelector('.rd').value,c.querySelector('.dc').value,c.querySelector('.cm').value])});
const t=r.map(x=>x.map(v=>'"'+String(v).replace(/"/g,'""')+'"').join(',')).join('\\n');const a=document.createElement('a');a.href=URL.createObjectURL(new Blob(['\\ufeff'+t],{type:'text/csv'}));a.download=document.title+'.csv';a.click()}
document.addEventListener('input',sv);ld();"""

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('md'); ap.add_argument('pdf'); ap.add_argument('out')
    ap.add_argument('--dpi', type=int, default=130); ap.add_argument('--procs', type=int, default=4); ap.add_argument('--vol', default='Vol 10'); a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    items = build(open(a.md, encoding='utf-8').read())
    pages = {}
    for it in items: pages.setdefault(it['pdf'], []).append(it)
    jobs = [(a.pdf, pg, [i['frac'] for i in its], a.dpi) for pg, its in sorted(pages.items())]
    with Pool(a.procs) as p: res = dict(p.map(crop, jobs, chunksize=4))
    for pg, its in pages.items():
        for it, img in zip(its, res[pg]): it['img'] = img
    groups = {}
    for it in items: groups.setdefault(it['suk'], []).append(it)
    idx = []; n = 0
    for k, (suk, its) in enumerate(groups.items(), 1):
        fn = f"review_{k:02d}.html"; its.sort(key=lambda i: (i['pdf'], i['frac']))
        cards = []
        for it in its:
            n += 1; cid = f"f{n}"
            cards.append(f'''<div class="card" id="{cid}" data-pdf="{it['pdf']}" data-pr="{it['printed']}" data-b="{html.escape(it['before'])}" data-a="{html.escape(it['after'])}">
<div class="hd"><b>#{n}</b> · {html.escape(it['suk'].split('—')[0].strip())} {html.escape(it['rik'])} · <b>PDF page {it['pdf']}</b> (printed p. {it['printed']})</div>
<img src="data:image/jpeg;base64,{it['img']}" alt="crop"><div class="note">Red marks show the estimated height of the flag on the Kannada page; the band is generous.</div>
<div class="ctx">…{html.escape(it['before'])} <span class="q">[?]</span> {html.escape(it['after'])}…</div>
<div class="in"><input class="rd" placeholder="Correct reading"><select class="dc"><option value=""></option><option>confirm</option><option>correct</option><option>illegible</option></select><input class="cm" placeholder="Comment"></div></div>''')
        title = f"{a.vol.replace(' ','')}_{suk.split('—')[0].strip().replace(' ','')}"
        open(os.path.join(a.out, fn), 'w', encoding='utf-8').write(f'<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><style>{CSS}</style></head><body><h2>{html.escape(a.vol)} — {html.escape(suk)}: {len(its)} flags</h2><p><a href="index.html">Index</a> · <button onclick="ex()">Export answers (CSV)</button> <span class="note">Answers are kept in this browser; export the CSV when done.</span></p>{"".join(cards)}<script>{JS}</script></body></html>')
        idx.append((fn, suk, len(its)))
    open(os.path.join(a.out, 'index.html'), 'w', encoding='utf-8').write(f'<!doctype html><html><head><meta charset="utf-8"><title>{a.vol} review</title><style>{CSS}</style></head><body><h2>{html.escape(a.vol)} — review of [?] flags ({n} in total)</h2><ul>' + ''.join(f'<li><a href="{f}">{html.escape(s)}</a> — {c}</li>' for f, s, c in idx) + '</ul></body></html>')
    print(n, 'flags,', len(idx), 'files')
if __name__ == '__main__': main()
