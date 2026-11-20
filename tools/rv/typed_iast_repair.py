#!/usr/bin/env python3
"""Repair of Sanskrit words that a translator TYPED in Latin letters inside double quotes in the English prose (Gists, Special Topics) instead of copying them
inside ⟦ ⟧ from kn.md (rule 1, found Nov 18 2026 in Vol 19: 133 places, mostly pp. 50-100).

  python3 tools/rv/typed_iast_repair.py N [--write]

A quoted word with an IAST diacritic is turned into Kannada letters by script and looked for as a whole word in the Kannada file on the same printed page and the
pages next to it. Found: the quotation marks and the typed word are replaced by what the build writes for ⟦word⟧ (Devanagari from kn.md and its IAST in *…*).
Not found: left as it is and listed (the editor decides). Prints counts; with --write changes the volume's English file (a logged repair, review/repair_log.md)."""
import re, sys, os
sys.path.insert(0, os.path.dirname(__file__)); sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'publish', 'tools'))
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
import rvlib, convert
vol = sys.argv[1]; write = '--write' in sys.argv
cfg = rvlib.load(int(vol)) if hasattr(rvlib, 'load') else None
root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
F = os.path.join(root, f'vol{vol}', f'Rigveda_Samhita_Vol{vol}_English_Translation.md'); K = os.path.join(root, f'vol{vol}', f'Rigveda_Samhita_Vol{vol}_Kannada_Text.md')
L = open(F, encoding='utf8').read().split('\n'); KL = open(K, encoding='utf8').read().split('\n')
pk = {}; p = 0
for l in KL:
    m = re.match(r'<!-- printed (\d+)', l)
    if m: p = int(m.group(1))
    pk.setdefault(p, []).append(l)
toks = {p: set(re.findall(r'[ಀ-೿‌‍]+', ' '.join(v))) for p, v in pk.items()}
dia = 'āīūṛṝḷṅñṭḍṇśṣṃḥ'
pat = re.compile(r'"([A-Za-z' + dia + r'\-]*[' + dia + r'][A-Za-z' + dia + r'\-]*)"')
def deva_iast(kn):
    d = convert.kn2deva(kn)
    return d, transliterate(d, sanscript.DEVANAGARI, sanscript.IAST)
page = 0; tot = fixed = 0; left = []
for i, l in enumerate(L):
    m = re.match(r'### Printed p\. (\d+)', l)
    if m: page = int(m.group(1))
    if l.startswith(('>', '#', '-')) or '⟦' in l: continue
    def rep(m):
        global tot, fixed
        w = m.group(1); tot += 1
        kn = transliterate(w.replace('-', ''), sanscript.IAST, sanscript.KANNADA)
        cand = set()
        for q in (page - 1, page, page + 1): cand |= toks.get(q, set())
        if kn in cand:
            d, ia = deva_iast(kn); fixed += 1; return f'{d} (*{ia}*)'
        left.append((page, w)); return m.group(0)
    L[i] = pat.sub(rep, l)
print(f'quoted IAST words: {tot}; replaced by the build\'s form (found on the printed page or its neighbours): {fixed}; left: {len(left)}')
for pg, w in left: print('  left  p.', pg, w)
if write: open(F, 'w', encoding='utf8').write('\n'.join(L)); print('written', F)
