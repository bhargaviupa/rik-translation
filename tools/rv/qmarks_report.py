#!/usr/bin/env python3
"""List every [?] of a page-marked source file with the text around it and the page strip that shows it, for the editor to verify.

  python3 tools/rv/qmarks_report.py vol22/html/rig_22.md STRIPS_DIR OUT_DIR --offset 26 --repo-url URL
Writes OUT_DIR/qmarks_to_verify.md (a table: no., printed page, PDF page, the line with the mark in ⟦ ⟧, the strip image) and copies the strips (p{PDF}_a.png /
p{PDF}_b.png; the top strip when the mark lies in the first half of the page text, else the bottom one) to OUT_DIR/img/. Pages before '<!-- body -->' are front
matter ('F' + PDF page; PDF page from '<!-- front page, pdf N -->'). The position of the mark in the page text decides the strip (lines are of similar height)."""
import re, sys, os, shutil
args = sys.argv[1:]
def opt(n, d=None):
    if n in args:
        i = args.index(n); v = args[i+1]; del args[i:i+2]; return v
    return d
off = int(opt('--offset', 26)); repo = opt('--repo-url', '')
src, strips, out = args
t = open(src, encoding='utf8').read()
fm, body = t.split('<!-- body -->')
pages = []
for m in re.finditer(r'<!-- front page, pdf (\d+) -->\n(.*?)(?=\n<!-- front page|\Z)', fm, re.S): pages.append(('F', int(m.group(1)), m.group(2)))
pg = re.split(r'<!-- page (\d+) -->\n', body)
for i in range(1, len(pg), 2): pages.append((int(pg[i]), int(pg[i]) + off, pg[i+1]))
os.makedirs(os.path.join(out, 'img'), exist_ok=True)
rows = []; n = 0
for pr, pdf, text in pages:
    for m in re.finditer(r'\[\?\]', text):
        n += 1; frac = m.start() / max(1, len(text))
        which = 'a' if frac < 0.5 else 'b'
        fn = f'p{pdf}_{which}.png'; srcf = os.path.join(strips, fn)
        if os.path.exists(srcf): shutil.copy(srcf, os.path.join(out, 'img', fn))
        ls = text.rfind('\n', 0, m.start()) + 1; le = text.find('\n', m.end()); le = len(text) if le < 0 else le
        line = text[ls:le]; k = m.start() - ls
        ctx = (line[max(0, k-70):k] + '⟦?⟧' + line[k+3:k+40]).replace('|', '\\|')
        rows.append((n, pr, pdf, ctx, fn, round(frac * 100)))
base = repo.rstrip('/') + '/img/' if repo else 'img/'
with open(os.path.join(out, 'qmarks_to_verify.md'), 'w', encoding='utf8') as f:
    f.write(f'# Marks [?] to verify — {len(rows)} places on {len({(r[1]) for r in rows})} pages\n\nEach row: the page (printed / PDF), the text around the mark (the unread word is marked ⟦?⟧; the line may continue), and the strip of the scan that shows it '
            f'(strip a = top 56% of the page, strip b = bottom 54%; "Position" = how far down the page text the mark lies, so look there first). Tell me the right word; I correct `rig_22.md`.\n\n')
    f.write('| No. | Printed p. | PDF p. | Text around the mark | Position | Scan strip |\n|---|---|---|---|---|---|\n')
    for n_, pr, pdf, ctx, fn, pos in rows:
        f.write(f'| {n_} | {pr} | {pdf} | {ctx} | {pos}% | [{fn}]({base}{fn}) |\n')
print(len(rows), 'marks on', len({r[1] for r in rows}), 'pages')
