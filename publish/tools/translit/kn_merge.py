#!/usr/bin/env python3
"""Merge a hand-typed Kannada page draft with the Devanagari blocks of the English file.

Usage: kn_merge.py DRAFT.md EN.md KN.md
 DRAFT holds page sections starting '<!-- PDF M · printed N -->'; a line '<<D>>' stands for the next
 Devanagari blockquote paragraph (not the italic IAST one) of the English file's '### Printed p. N' section,
 converted to Kannada script (deva_to_kannada.py). The pages are inserted before the final 'Progress note'
 of KN (which is kept, but replaced if DRAFT ends with a '**Progress note:**' paragraph).
Asserts: every <<D>> finds a block; every block of the page is used (else warns)."""
import re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from deva_to_kannada import deva2kn

def en_blocks(en, printed):
    # all sections headed '### Printed p. N' (a continuation heading after a Sūkta break counts too)
    secs = re.findall(r'^### Printed p\. %s\b.*?$(.*?)(?=^### Printed p\. |^## |\Z)' % re.escape(printed), en, re.M | re.S)
    secs += re.findall(r'^### Printed p\. %s\b.*?$(.*?)(?=^### Printed p\. |^## |\Z)' % re.escape(printed), '', re.M | re.S)
    assert secs, 'no English section for printed p. ' + printed
    # sections that follow a '## Sūkta' heading carry the same page number (continuation): find them separately
    blocks, cur = [], []
    for sec in secs:
        for ln in sec.split('\n') + ['']:
            if ln.startswith('> ') and not ln.startswith('> *'):
                cur.append(ln[2:])
            elif cur:
                blocks.append('\n'.join(cur)); cur = []
    return blocks

def main(draft, en_path, kn_path):
    d = open(draft, encoding='utf8').read()
    en = open(en_path, encoding='utf8').read()
    kn = open(kn_path, encoding='utf8').read()
    parts = re.split(r'(?m)^(?=<!-- PDF )', d)
    out, note = [], None
    for p in parts:
        if not p.strip(): continue
        m = re.match(r'<!-- PDF (\d+) · printed (\w+)', p)
        if not m:
            raise SystemExit('draft chunk without page marker: ' + p[:60])
        pm = re.search(r'\n\*\*Progress note:\*\*.*\Z', p, re.S)
        if pm: note = pm.group(0).strip(); p = p[:pm.start()] + '\n'
        blocks = en_blocks(en, m.group(2)); it = iter(blocks); used = 0
        def rep(_):
            nonlocal used
            try: b = next(it)
            except StopIteration: raise SystemExit('too many <<D>> on printed p. ' + m.group(2))
            used += 1
            return '\n'.join('> ' + x for x in deva2kn(b).split('\n'))
        p = re.sub(r'<<D>>', rep, p)
        if used != len(blocks): print('WARNING: printed p. %s uses %d of %d Devanagari blocks' % (m.group(2), used, len(blocks)))
        out.append(p.rstrip() + '\n')
    i = kn.rfind('**Progress note:**')
    assert i > len(kn) - 20000, 'progress note not near the end'
    head = kn[:i].rstrip() + '\n\n'
    old_note = kn[i:].strip()
    new = head + '\n'.join(out) + '\n---\n\n' + (note or old_note) + '\n'
    assert len(new) >= len(kn) - len(old_note)
    assert new.count('**Progress note:**') == 1
    open(kn_path, 'w', encoding='utf8').write(new)
    print('merged', len(out), 'pages')

if __name__ == '__main__': main(*sys.argv[1:4])
