#!/usr/bin/env python3
"""Clean-up of `[accent ?]` marks in a legacy volume's English file (shared tool; Vol 2 first). Dry run by default.

  python3 tools/rv/qmark_cleanup.py VOL accent [--apply]

The Saṃhitā verses of the volume have been replaced by the accented verses of the reference (and agree with the Wikisource index except the conventions of
docs/WIKISOURCE_NOTES.md), so the doubts about the accent marks of the old reading are settled by those texts:
  * ` [accent ?]` at the end of a transliteration line (`> *...*` [accent ?]) is removed;
  * a whole-line remark `*( ... [accent ?] ... )*` is deleted (our remark about the accents of the print, B4.1).
Every change is one row of volN/review/repair_log.md (tag ACCENT: line, old, new)."""
import os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
vol = sys.argv[1]; mode = sys.argv[2]; apply = '--apply' in sys.argv
assert mode == 'accent'
p = os.path.join(ROOT, f'vol{vol}', f'Rigveda_Samhita_Vol{vol}_English_Translation.md')
L = open(p, encoding='utf8').read().split('\n'); out = []; log = []; ends = rem = 0
for i, l in enumerate(L):
    if '[accent ?]' not in l: out.append(l); continue
    if l.startswith('> *') and l.rstrip().endswith('[accent ?]'):
        new = re.sub(r'\s*\[accent \?\]\s*$', '', l); out.append(new); ends += 1; log.append((i + 1, 'end mark', l[-40:], new[-40:]))
    elif l.startswith('*(') and l.rstrip().endswith(')*'):
        rem += 1; log.append((i + 1, 'remark deleted', l[:110], ''))
        if out and out[-1] == '' and i + 1 < len(L) and L[i + 1] == '': out.pop()      # no double blank line
    else: out.append(l); print('left (other form):', i + 1, l[:100])
print(f'end marks removed {ends}, remark lines deleted {rem}', '(applied)' if apply else '(dry run)')
if apply:
    open(p, 'w', encoding='utf8').write('\n'.join(out))
    with open(os.path.join(ROOT, f'vol{vol}', 'review', 'repair_log.md'), 'a', encoding='utf8') as f:
        f.write('\n## Second pass: accent doubts (tag ACCENT)\n- The verses of the volume are the accented verses of the reference (and agree with Wikisource apart from its conventions): the doubts about the accents of the old reading are settled; %d end marks and %d remark lines removed (`tools/rv/qmark_cleanup.py %s accent`). Rows: old line numbers of the file before this edit.\n' % (ends, rem, vol))
        for r in log: f.write(f'  - line {r[0]}: {r[1]}: `{r[2]}` → `{r[3]}`\n')
