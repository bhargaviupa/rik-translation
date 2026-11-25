#!/usr/bin/env python3
"""List every `[?]` of a legacy volume's English file with the evidence the sources give (shared tool; Vol 2 first). Nothing is changed.

  python3 tools/rv/qmark_resolve.py VOL

Writes volN/review/second_pass/qmarks.tsv: id, line, page, class, text before the mark, text after the mark, evidence, proposal.
Classes: `number` (the mark follows a number or a reference), `deva` (follows Devanagari), `latin` (follows a word), `remark` (inside a remark of ours).
Evidence for a number: the supplied Kannada text (the Kannada file made from it) of printed pages N-1..N+1 has the same number (Kannada digits read as ASCII)
-> `supplied page has it`; otherwise the numbers of that page that differ by one digit are listed. Numerals of the supplied text are correct (user, Nov 24 2026)."""
import os, re, sys, csv
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
vol = sys.argv[1]; d = os.path.join(ROOT, f'vol{vol}')
KD = str.maketrans('೦೧೨೩೪೫೬೭೮೯०१२३४५६७८९', '01234567890123456789')
DEV = re.compile('[ऀ-ॿ]')
kn = open(os.path.join(d, f'Rigveda_Samhita_Vol{vol}_Kannada_Text.md'), encoding='utf8').read()
pages = {}
for m in re.finditer(r'<!-- printed (\S+?)(?::[^>]*)? -->(.*?)(?=<!-- printed |\Z)', kn, re.S): pages[m.group(1)] = m.group(2)
def toks(t):
    t = t.translate(KD); refs = set(re.sub(r'\s*[-.:–]\s*', '-', x) for x in re.findall(r'\d+(?:\s*[-.:–]\s*\d+)+', t)); nums = set(re.findall(r'(?<![\d-])\d{1,4}(?![\d-])', t)); return refs, nums
cache = {}
def page_toks(p):
    out = (set(), set())
    for q in (p - 1, p, p + 1):
        if str(q) not in pages: continue
        if q not in cache: cache[q] = toks(pages[str(q)])
        out = (out[0] | cache[q][0], out[1] | cache[q][1])
    return out
L = open(os.path.join(d, f'Rigveda_Samhita_Vol{vol}_English_Translation.md'), encoding='utf8').read().split('\n')
page = None; rows = []
for i, l in enumerate(L):
    m = re.match(r'### Page (\d+)', l)
    if m: page = int(m.group(1))
    for k in re.finditer(r'\[\?\]', l):
        pre = l[max(0, k.start() - 70):k.start()]; post = l[k.end():k.end() + 50]
        remark = l.startswith('*(') or l.startswith('(')
        t = pre.translate(KD); mm = re.search(r'(\d+(?:\s*[-–.]\s*\d+)*)[\s"”’)\]*]*$', t)
        cls = 'remark' if remark else 'number' if mm else 'deva' if DEV.search(pre[-25:]) else 'latin'
        ev = ''; prop = ''
        if cls == 'number' and page:
            tok = re.sub(r'\s*[-–.]\s*', '-', mm.group(1)); refs, nums = page_toks(page)
            if tok in refs or tok in nums: ev = 'supplied page has it'; prop = 'remove [?]'
            else:
                near = sorted(r for r in refs if len(r.split('-')) == len(tok.split('-')) and sum(a != b for a, b in zip(r, tok)) <= 1 and len(r) == len(tok))
                ev = 'not on the page; one digit off: ' + ', '.join(near[:4]) if near else 'not on the page'
        rows.append((f'q{len(rows)+1}', i + 1, page, cls, pre.replace('\t', ' '), post.replace('\t', ' '), ev, prop))
os.makedirs(os.path.join(d, 'review', 'second_pass'), exist_ok=True)
with open(os.path.join(d, 'review', 'second_pass', 'qmarks.tsv'), 'w', encoding='utf8', newline='') as f:
    w = csv.writer(f, delimiter='\t'); w.writerow(['id', 'line', 'page', 'class', 'before', 'after', 'evidence', 'proposal']); w.writerows(rows)
from collections import Counter
print(len(rows), 'marks;', Counter(r[3] for r in rows)); print('number marks by evidence:', Counter(r[6].split(':')[0] for r in rows if r[3] == 'number'))
