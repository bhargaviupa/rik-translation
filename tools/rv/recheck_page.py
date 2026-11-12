#!/usr/bin/env python3
"""One command for the re-check agents: the page's report, its English section and the supplied Kannada of that page, together.
  python3 tools/rv/recheck_page.py VOL PAGE [PAGE ...]"""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import recheck as R
vol = sys.argv[1]; d = f'vol{vol}'
EN = R.read_en([p for p in (f'{d}/Rigveda_Samhita_Vol{vol}_English_Translation.md', f'{d}/Rigveda_Samhita_Vol{vol}_Gaps_English_Translation.md') if os.path.exists(p)])
KN, NOTIN = R.read_kn(f'{d}/kannada/Rigveda_Samhita_Vol{vol}_Kannada_Text.md')
for a in sys.argv[2:]:
    k = int(a) if a.isdigit() else a
    rp = f'{d}/review/recheck/p{k:04d}.md' if isinstance(k, int) else f'{d}/review/recheck/p_{k}.md'
    print(f'\n######## PAGE {k} ########\n--- REPORT ---\n' + (open(rp, encoding='utf8').read() if os.path.exists(rp) else '(nothing listed)'))
    print(f'--- ENGLISH (### Page {k}) ---\n' + EN.get(k, '(none)').strip())
    print(f'--- SUPPLIED KANNADA (printed {k}) ---\n' + (KN.get(k, '(not in the supplied text)').strip()))
