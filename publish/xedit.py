#!/usr/bin/env python3
"""Apply cross-check decisions to the Vol 2 text within one printed-page section.
usage: from xedit import apply;  apply(35, [(old,new),...], log=[(old,decision)])"""
import re, pathlib, csv
ROOT = pathlib.Path(__file__).resolve().parent.parent
MD = ROOT / 'Rigveda_Samhita_Vol2_English_Translation.md'
LOG = ROOT / 'publish' / 'review' / 'vol2_xcheck_log.tsv'
def bounds(s, n):
    ms = list(re.finditer(r'(?m)^#{2,3} \[?Page (\d+)', s))
    for k, m in enumerate(ms):
        if int(m.group(1)) == n:
            return m.start(), (ms[k+1].start() if k+1 < len(ms) else len(s))
    raise SystemExit(f'page {n} not found')
def apply(n, edits, clear_refs=True, note=''):
    s = MD.read_text(encoding='utf-8'); a, b = bounds(s, n); seg = s[a:b]; cnt = 0
    for old, new in edits:
        c = seg.count(old)
        if c == 0: print('  !! not found on p', n, ':', old[:60]); continue
        seg = seg.replace(old, new); cnt += c
    if clear_refs:   # reference-number flags confirmed on the page: "(… [?])" inside parentheses
        pass
    s = s[:a] + seg + s[b:]; MD.write_text(s, encoding='utf-8')
    LOG.parent.mkdir(exist_ok=True)
    with open(LOG, 'a', encoding='utf-8', newline='') as f:
        csv.writer(f, delimiter='\t').writerow([n, cnt, note])
    print(f'p{n}: {cnt} replacements; remaining [?] on page: {seg.count("[?]")}')
def clear_all(n, keep=(), note=''):
    """remove every ' [?]' on page n except those whose line contains a string in keep"""
    s = MD.read_text(encoding='utf-8'); a, b = bounds(s, n); lines = s[a:b].split('\n'); k = 0
    for i, l in enumerate(lines):
        if '[?]' in l and not any(x in l for x in keep) and not l.lstrip().startswith('*(Source note') and not re.search(r'(marked|flagged|bracketed|marks|mark)[^.]{0,40}\[\?\]|\[\?\] (marks|means|is used)', l):
            lines[i] = l.replace(' [?]', '').replace('[?]', ''); k += 1
    s = s[:a] + '\n'.join(lines) + s[b:]; MD.write_text(s, encoding='utf-8')
    with open(LOG, 'a', encoding='utf-8', newline='') as f: csv.writer(f, delimiter='\t').writerow([n, f'cleared lines {k}', note])
    print(f'p{n}: cleared {k} lines')
