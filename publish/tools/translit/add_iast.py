#!/usr/bin/env python3
"""Add the IAST layer to a Markdown translation by script, so only Devanagari + English need to be written.

Block form (as in Volumes 1-8): a run of consecutive Devanagari lines in a blockquote
    > देवा अदितिः ॥ १ ॥
    > ...
becomes the same run followed by the matching italic IAST lines
    > *devā aditiḥ ‖ 1 ‖*
unless an italic IAST run already follows (then it is left alone).
Inline form: ⟦देवा⟧ becomes  देवा (*devā*)  (use for Sanskrit quoted inside prose).

Usage:
  python3 add_iast.py FILE.md            # rewrite in place
  python3 add_iast.py FILE.md --check    # only compare existing IAST layers with the Devanagari and list differences
Needs: pip install indic-transliteration
"""
import re, sys, unicodedata
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

DEV = re.compile('[ऀ-ॿ]')

def deva_to_iast(s):
    s = s.replace('‌', '').replace('‍', '')
    s = re.sub('ऽ', "'", s)
    t = transliterate(s, sanscript.DEVANAGARI, sanscript.IAST)
    t = t.replace('ḻ', 'ḷ').replace('||', '‖').replace('|', '|')
    t = re.sub(r"(?<=\S)'", " '", t)           # kūpe 'vahitam
    t = t.translate(str.maketrans('०१२३४५६७८९', '0123456789'))
    return t

def norm(s):
    s = unicodedata.normalize('NFC', s.lower()).replace('ṁ', 'ṃ').replace('ḻ', 'ḷ')
    return re.sub(r"[\s|‖।॥\-*_.,;:!?\d\[\]()'’\"“”]", '', s)

def process(lines):
    out, i = [], 0
    while i < len(lines):
        L = lines[i]
        if L.startswith('>') and DEV.search(L):
            block = []
            while i < len(lines) and lines[i].startswith('>') and DEV.search(lines[i]):
                block.append(lines[i]); out.append(lines[i]); i += 1
            j = i
            while j < len(lines) and lines[j].strip() == '': j += 1
            has = j < len(lines) and lines[j].lstrip('> ').startswith('*') and not DEV.search(lines[j])
            if not has:
                out.append('')
                for b in block: out.append('> *' + deva_to_iast(b.lstrip('> ').strip()) + '*')
        else:
            out.append(re.sub('⟦([^⟧]+)⟧', lambda m: m.group(1) + ' (*' + deva_to_iast(m.group(1)) + '*)', L)); i += 1
    return out

def check(lines):
    i, n, bad = 0, 0, []
    while i < len(lines):
        if lines[i].startswith('>') and DEV.search(lines[i]):
            D = []
            while i < len(lines) and lines[i].startswith('>') and DEV.search(lines[i]): D.append(lines[i].lstrip('> ').strip()); i += 1
            while i < len(lines) and lines[i].strip() == '': i += 1
            I = []
            while i < len(lines) and lines[i].startswith('>') and not DEV.search(lines[i]) and lines[i].lstrip('> ').startswith('*'): I.append(lines[i].lstrip('> ').strip('* ')); i += 1
            if len(D) == len(I):
                for d, t in zip(D, I):
                    n += 1
                    if norm(deva_to_iast(d)) != norm(t): bad.append((d[:60], t[:60]))
        else: i += 1
    return n, bad

if __name__ == '__main__':
    if len(sys.argv) < 2: sys.exit(__doc__)
    f = sys.argv[1]
    lines = open(f, encoding='utf-8').read().split('\n')
    if '--check' in sys.argv:
        n, bad = check(lines)
        print(f'{n} aligned lines, {len(bad)} differ')
        for d, t in bad[:40]: print(' ', d, '|', t)
    else:
        open(f, 'w', encoding='utf-8').write('\n'.join(process(lines)))
