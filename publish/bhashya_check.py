#!/usr/bin/env python3
"""Check an English rendering of the Sāyaṇa-bhāṣya (tools/rv/BHASHYA_BRIEF.md) against its task file.

    python3 publish/bhashya_check.py VOL M.S          # e.g. 17 3.40: the task and English files of that sūkta
    python3 publish/bhashya_check.py TASK.md ENGLISH.md

TASK.md is built by `publish/bhashya_book.py VOL --task M.S`. Checks:
  - the headings are exactly `## Introduction` (if the task has a bhāṣya block before Ṛk 1) and `## Ṛk N`
    for every Ṛk of the task, in order, each with text;
  - every ⟦…⟧ occurs letter for letter (spaces, line breaks and accent marks apart) in that unit's Devanagari;
  - no Devanagari outside ⟦ ⟧; no stray ⟦ or ⟧;
  - every numbered reference (2-3-4, 5.10) stands with the same numbers in that unit's block;
  - no Sanskrit gloss typed in Roman letters inside brackets, e.g. (ramate, krīḍati): it must be copied with ⟦ ⟧;
  - an optional last section `## Readings` (misread words of the supplied text and the reading translated), one
    line each: `- Ṛk N: ⟦supplied⟧ → reading adopted — basis`.
Prints the size of each unit (bhāṣya words → English words) and VERIFIED, or the faults and exit 1.
What it cannot check: whether the English is right. Only a reader can.
"""
import re, sys

SQUEEZE = re.compile('[\\s\\u0951\\u0952\\u1CD0-\\u1CFF\\uA8E0-\\uA8FF]+')   # spaces, line breaks, Vedic accent marks
DEVA = re.compile(r'[ऀ-ॿ]')


REF = re.compile(r'(?<![\w.-])\d+(?:[-.–]\d+)+(?![\w-])')
DIAC = re.compile('[āīūṛṝḷṅñṭḍṇśṣṃḥ]')
ENGLISH = set('the of a an in is that or and to with by for as its it this are be from on at his he who which not i e'.split())
TO_DEVA = str.maketrans('0123456789', '०१२३४५६७८९')


def roman_gloss(body):
    """Bracketed runs of lower-case Sanskrit in Roman letters, e.g. (ramate, krīḍati)."""
    out = []
    for m in re.finditer(r'\(([^()⟦⟧{}\d]{2,60})\)', body):
        words = re.findall(r'[^\W\d_]+', m.group(1))
        if (words and len(words) <= 5 and DIAC.search(m.group(1)) and all(w.islower() for w in words)
                and not ENGLISH & set(words)):
            out.append(m.group(0))
    return out


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
    task, eng = sys.argv[1], sys.argv[2]
    if task.isdigit():
        import pathlib, subprocess
        root = pathlib.Path(__file__).resolve().parent.parent
        r = subprocess.run([sys.executable, str(root / 'publish' / 'bhashya_book.py'), task, '--task', eng], capture_output=True, text=True)
        got = re.findall(r'^(?:task|write your English to): (\S+)', r.stdout, flags=re.M)
        if r.returncode or len(got) != 2: sys.exit((r.stdout + r.stderr).strip() or 'could not build the task file')
        task, eng = str(root / got[0]), str(root / got[1])
        if not pathlib.Path(eng).exists(): sys.exit(f'no English file yet: {got[1]}')
    units = task_units(task)
    text = open(eng, encoding='utf-8').read()
    parts = re.split(r'^## (.+)$', text, flags=re.M)
    faults = []
    if parts[0].strip(): faults.append('text before the first heading')
    got = [(parts[i].strip(), parts[i + 1]) for i in range(1, len(parts), 2)]
    readings = got.pop()[1] if got and got[-1][0] == 'Readings' else ''
    alldeva = ''.join(u['deva'] for u in units.values()).replace('-', '')
    nread = 0
    for ln in readings.splitlines():
        if not ln.strip(): continue
        nread += 1
        if not re.match(r'^- (Introduction|Ṛk \d+): ⟦[^⟧]+⟧ → .+ — .+', ln):
            faults.append(f'Readings: line not in the form "- Ṛk N: ⟦supplied⟧ → reading adopted — basis": {ln[:70]}')
        for q in re.findall(r'⟦(.*?)⟧', ln):
            if SQUEEZE.sub('', q).replace('-', '') not in alldeva: faults.append(f'Readings: ⟦{q[:50]}⟧ is not in this sūkta letter for letter')
        if DEVA.search(re.sub(r'⟦.*?⟧', '', ln)): faults.append(f'Readings: Devanagari outside ⟦ ⟧: {ln[:70]}')
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
            if SQUEEZE.sub('', q).replace('-', '') not in u['deva'].replace('-', ''):      # a line-end hyphen of the supplied text does not count
                faults.append(f'{h}: ⟦{q[:50]}⟧ is not in this unit letter for letter')
        outside = re.sub(r'⟦.*?⟧', '', body, flags=re.S)
        m = DEVA.search(outside)
        if m: faults.append(f'{h}: Devanagari outside ⟦ ⟧ near "{outside[max(0, m.start() - 25):m.start() + 15].strip()}"')
        refs = re.sub(r'[.–—]', '-', u['deva'])
        for r in REF.findall(re.sub(r'\*\*NOTE\*\*\{[^{}]*\}', '', outside)):
            if re.sub(r'[.–]', '-', r).translate(TO_DEVA) not in refs:
                faults.append(f'{h}: the reference {r} is not in this unit\'s block (nothing may be supplied from elsewhere)')
        for g in roman_gloss(outside):
            faults.append(f'{h}: Sanskrit in Roman letters inside brackets {g}: cite the word with ⟦ ⟧, or give only the English; a technical term stands without brackets')
        plain = re.sub(r'⟦.*?⟧', '', body, flags=re.S)
        rows.append((h, u['bh_words'], len(plain.split()), len(quotes), body.count('**NOTE**')))
    for h, b, e, q, n in rows: print(f'  {h}: bhāṣya {b} words → English {e} words; {q} quotations; {n} NOTE')
    tb, te = sum(r[1] for r in rows), sum(r[2] for r in rows)
    print(f'  total: bhāṣya {tb} words → English {te} words; {sum(r[3] for r in rows)} quotations; {sum(r[4] for r in rows)} NOTE; {nread} readings logged')
    if faults:
        print('FAULTS:'); [print('  - ' + f) for f in faults]; return 1
    print('VERIFIED (form only: headings, quotations and references copied from the unit, no typed Sanskrit in brackets)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
