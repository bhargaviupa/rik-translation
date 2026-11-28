#!/usr/bin/env python3
"""Kannada-only front matter: put the volume's own Pīṭhike (from the supplied text) into volN's Kannada file as '## ಪೀಠಿಕೆ'.

  python3 tools/rv/kn_front.py VOL FIRST_LINE LAST_LINE [--source html/FILE.md] [--html] [--install]

For volumes whose English file already has the preface (Vols 2, 7-10, 25).  Same cleaning as tools/rv/api_front.py (html_to_kn.clean_line,
hyphen joins, roman page numbers as `<!-- roman iii -->`).  Without --install it only writes volN/work/preface_kn/kn.md and prints it
for checking.  --install inserts it after the title lines, before the first `<!-- printed` mark; refuses if '## ಪೀಠಿಕೆ' is there.
The supplied text is not changed; the repair is logged in volN/review/repair_log.md."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rvlib, html_to_kn
ROOT = rvlib.ROOT
a = sys.argv[1:]
if len(a) < 3: sys.exit(__doc__)
vol = int(a[0]); lo, hi = int(a[1]), int(a[2])      # legacy volumes have no volcfg.json: paths are by name
KN = os.path.join(ROOT, f'vol{vol}', f'Rigveda_Samhita_Vol{vol}_Kannada_Text.md')
src = os.path.join(ROOT, a[a.index('--source') + 1] if '--source' in a else rvlib.Cfg(a[0]).source[0].split('@')[0])
out = []
import html as H
for l in open(src, encoding='utf8').read().split('\n')[lo - 1:hi]:
    if '--html' in a: l = re.sub(r'<br\s*/?>', '\n', l); l = H.unescape(re.sub(r'<[^>]+>', '', l)).replace('This image contains no text. It depicts a decorative floral or geometric pattern.', '')
    l = html_to_kn.clean_line(l)
    if not l or l == '---': continue
    m = re.fullmatch(r'#*\s*([ivxl]+)\s*', l)
    if m: out += ['', f'<!-- roman {m.group(1)} -->', '']; continue
    out.append(re.sub(r'^#+\s*', '', l))
kn = '\n'.join(html_to_kn.join_hyphens(out)).strip() + '\n'
w = os.path.join(ROOT, f'vol{vol}', 'review'); os.makedirs(w, exist_ok=True); open(os.path.join(w, 'preface_kn.md'), 'w', encoding='utf8').write(kn)
print(f'vol{vol}: {len(kn)} chars, {len(kn.splitlines())} lines -> {w}/preface_kn.md')
if '--install' in a:
    k = open(KN, encoding='utf8').read()
    if '## ಪೀಠಿಕೆ' in k: sys.exit('the Kannada file already has a preface')
    j = k.index('<!-- printed ') if '<!-- printed ' in k else len(k)
    open(KN, 'w', encoding='utf8').write(k[:j] + '## ಪೀಠಿಕೆ\n\n' + kn + '\n' + k[j:])
    os.makedirs(os.path.join(ROOT, f'vol{vol}', 'review'), exist_ok=True)
    open(os.path.join(ROOT, f'vol{vol}', 'review', 'repair_log.md'), 'a', encoding='utf8').write(f"- 2026-11-28 front matter: the editor's Pīṭhike (source lines {lo}-{hi} of {os.path.relpath(src, ROOT)}) inserted as '## ಪೀಠಿಕೆ' before the first printed page of the Kannada file (tools/rv/kn_front.py); no change to the English file.\n")
    print('installed')
