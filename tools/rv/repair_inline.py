#!/usr/bin/env python3
"""One-off repair for English files built before convert.py joined multi-line ⟦…⟧ quotations:
every leftover ⟦Kannada-script Sanskrit⟧ (also over several lines) becomes `Devanagari (*IAST*)`, exactly like the one-line quotations.

  python3 tools/rv/repair_inline.py N [--write]

Without --write: report only. With --write the English file is rewritten (all other text unchanged; the progress note is untouched) and
vol N/review/repair_log.md gets a dated line. Run `git diff --stat` afterwards: only the quoted lines may change."""
import re, sys, pathlib, datetime
root = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(root / 'publish' / 'tools' / 'translit'))
from kannada_to_deva import kn2deva
from add_iast import deva_to_iast
vol = int(sys.argv[1]); write = '--write' in sys.argv
f = root / f'vol{vol}' / f'Rigveda_Samhita_Vol{vol}_English_Translation.md'
t = f.read_text(encoding='utf8')
KN = re.compile('[ಀ-೿]')
n = [0, 0]
def rep(m):
    s = m.group(1)
    if not KN.search(s): return m.group(0)
    n[0] += 1; n[1] += s.count('\n')
    d = kn2deva(re.sub(r'\s*\n\s*', ' ', s).strip())
    return f'{d} (*{deva_to_iast(d)}*)'
new = re.sub(r'⟦([^⟧]*)⟧', rep, t)
print(f'{n[0]} quotations converted ({n[1]} line breaks joined); ⟦ left: {new.count("⟦")}; Devanagari chars {len(re.findall("[ऀ-ॿ]", t))} -> {len(re.findall("[ऀ-ॿ]", new))}; Kannada chars {len(KN.findall(t))} -> {len(KN.findall(new))}')
if write:
    f.write_text(new, encoding='utf8')
    log = root / f'vol{vol}' / 'review' / 'repair_log.md'
    with log.open('a', encoding='utf8') as g:
        g.write(f'- {datetime.date.today()}: tools/rv/repair_inline.py: {n[0]} leftover multi-line ⟦Kannada Sanskrit⟧ quotations of the English file converted to Devanagari + (IAST) (no other text changed).\n')
