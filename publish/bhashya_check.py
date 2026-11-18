#!/usr/bin/env python3
"""Check an English rendering of the Sāyaṇa-bhāṣya (tools/rv/BHASHYA_BRIEF.md) against its task file.

    python3 publish/bhashya_check.py TASK.md ENGLISH.md

TASK.md is a one-sūkta reader built by publish/bhashya_book.py. Checks:
  - the headings are exactly `## Introduction` (if the task has a bhāṣya block before Ṛk 1) and `## Ṛk N`
    for every Ṛk of the task, in order, each with text;
  - every ⟦…⟧ occurs letter for letter (spaces, line breaks and accent marks apart) in that unit's Devanagari;
  - no Devanagari outside ⟦ ⟧; no stray ⟦ or ⟧.
Prints the size of each unit (bhāṣya words → English words) and VERIFIED, or the faults and exit 1.
What it cannot check: whether the English is right. Only a reader can.
"""
import re, sys

SQUEEZE = re.compile('[\\s\\u0951\\u0952\\u1CD0-\\u1CFF\\uA8E0-\\uA8FF]+')   # spaces, line breaks, Vedic accent marks
DEVA = re.compile(r'[ऀ-ॿ]')


def task_units(path):
    """{'Introduction' | 'Ṛk N': {'deva': str without spaces, 'bh_words': int}} in order."""
    units, cur, sec = {}, None, None
    for ln in open(path, encoding='utf-8').read().splitlines():
        if ln.startswith('## '): cur, sec = 'Introduction', None; continue
        if ln.startswith('### '):
            cur, sec = ln[4:].strip(), None; continue
        if ln.startswith('#### '):
            sec = 'bh' if 'Sāyaṇa-bhāṣya' in ln else 'x'; continue
        if cur is None or not ln.startswith('>'): continue
        if not DEVA.search(ln): continue
        u = units.setdefault(cur, {'deva': '', 'bh_words': 0})
        u['deva'] += SQUEEZE.sub('', ln.lstrip('> '))
        if sec == 'bh': u['bh_words'] += len(ln.lstrip('> ').split())
    return {k: v for k, v in units.items() if k != 'Introduction' or v['bh_words']}


def main():
    if len(sys.argv) != 3: sys.exit(__doc__)
    units = task_units(sys.argv[1])
    text = open(sys.argv[2], encoding='utf-8').read()
    parts = re.split(r'^## (.+)$', text, flags=re.M)
    faults = []
    if parts[0].strip(): faults.append('text before the first heading')
    got = [(parts[i].strip(), parts[i + 1]) for i in range(1, len(parts), 2)]
    if [h for h, _ in got] != list(units):
        faults.append(f'headings are {[h for h, _ in got]}; expected {list(units)}')
    if re.search(r'^#(?!# )', text, flags=re.M): faults.append('a heading that is not `## …`')
    rows = []
    for h, body in got:
        u = units.get(h)
        if not u: continue
        if not body.strip(): faults.append(f'{h}: empty')
        if body.count('⟦') != body.count('⟧'): faults.append(f'{h}: unbalanced ⟦ ⟧')
        quotes = re.findall(r'⟦(.*?)⟧', body, flags=re.S)
        for q in quotes:
            if SQUEEZE.sub('', q) not in u['deva']:
                faults.append(f'{h}: ⟦{q[:50]}⟧ is not in this unit letter for letter')
        outside = re.sub(r'⟦.*?⟧', '', body, flags=re.S)
        m = DEVA.search(outside)
        if m: faults.append(f'{h}: Devanagari outside ⟦ ⟧ near "{outside[max(0, m.start() - 25):m.start() + 15].strip()}"')
        plain = re.sub(r'⟦.*?⟧', '', body, flags=re.S)
        rows.append((h, u['bh_words'], len(plain.split()), len(quotes), body.count('**NOTE**')))
    for h, b, e, q, n in rows: print(f'  {h}: bhāṣya {b} words → English {e} words; {q} quotations; {n} NOTE')
    tb, te = sum(r[1] for r in rows), sum(r[2] for r in rows)
    print(f'  total: bhāṣya {tb} words → English {te} words; {sum(r[3] for r in rows)} quotations; {sum(r[4] for r in rows)} NOTE')
    if faults:
        print('FAULTS:'); [print('  - ' + f) for f in faults]; return 1
    print('VERIFIED (form only: headings, quotations copied from the unit, no typed Devanagari)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
