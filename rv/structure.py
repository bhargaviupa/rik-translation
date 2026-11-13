"""Step 2 of docs/DESIGN.md: the structure of a volume, made by script.

Input: the volume's Kannada text as the existing scripts make it from the supplied text (page marks, section labels, Sanskrit blocks) and the
reference text of the verses.  Output: volN/data/units.jsonl — one unit per part of a Ṛk (and per sūkta introduction, and the front matter),
each with its Kannada-side content in order; and the report of what does not fit (volN/review/source_faults.tsv, structure_report.md)."""
import re, os, difflib, collections
from .common import *

LABELS = {'ಸಂಹಿತಾಪಾಠಃ': 'samhita', 'ಪದಪಾಠಃ': 'pada', 'ಸಾಯಣಭಾಷ್ಯಂ': 'bhashya', 'ಸಾಯಣಭಾಷ್ಯಮ್': 'bhashya', 'ಪ್ರತಿಪದಾರ್ಥ': 'pratipada', 'ಭಾವಾರ್ಥ': 'bhavartha',
          'English Translation': 'english', 'ವಿಶೇಷವಿಷಯಗಳು': 'vishesha', 'ವ್ಯಾಕರಣಪ್ರಕ್ರಿಯಾ': 'grammar'}
ORDER = ['intro', 'samhita', 'pada', 'bhashya', 'summary', 'pratipada', 'bhavartha', 'english', 'vishesha', 'grammar']
TITLE = re.compile(r'\s*\S+(\s+\S+)?\s+ಸೂಕ್ತವು\s*[.।]?\s*')            # the sūkta's title line: an ordinal and 'sūktavu', nothing else

def parse_kn(vol):
    """-> (units in order, counters).  A unit: {kind, m, s, rk, kn: [items]}; an item is ['text', line] | ['block', [lines]] | ['page', n, head] | ['figure', path] | ['break']."""
    L = open(vol_paths(vol)['kn'], encoding='utf8').read().split('\n'); st = collections.Counter()
    units = []; cur = None; m = s = rk = None; expect_head = False; lastpage = None; pending = None      # pending: the introduction of the next sūkta, begun at its title line
    def start(kind):
        nonlocal cur
        cur = dict(kind=kind, m=m, s=s, rk=rk, kn=[]); units.append(cur); return cur
    def ensure():
        if cur is None: start('front' if s is None else ('intro' if rk is None else 'loose'))
        return cur
    for i, l in enumerate(L):
        t = l.strip()
        if i < 6 and (l.startswith('# ') or (t.startswith('*The Kannada text') and t.endswith('*'))): continue
        if t == '---' or t.startswith('**Progress note:**'): continue
        mm = re.match(r'<!-- (printed|roman) (\S+) -->', t)
        if mm:
            lastpage = [ 'page', (int(mm.group(2)) if mm.group(1) == 'printed' else mm.group(2)), '']; ensure()['kn'].append(lastpage); expect_head = True; st['pages'] += 1; continue
        if t.startswith('*[') and t.endswith(']*'):
            if expect_head and lastpage is not None: lastpage[2] = t[2:-2].strip(); expect_head = False; st['running heads'] += 1
            else: st['bracketed lines of the Kannada file (not original text)'] += 1; ensure()['kn'].append(['knnote', t[2:-2]])
            continue
        if t: expect_head = False
        mm = re.match(r'## ಮಂಡಲ ([೦-೯]+)\s*$', t)
        if mm: m = int(mm.group(1).translate(KD)); continue
        mm = re.match(r'## ಸೂಕ್ತ ([೦-೯]+) \(ಮಂಡಲ ([೦-೯]+)\)', t)
        if mm:
            s = int(mm.group(1).translate(KD)); m = int(mm.group(2).translate(KD)); rk = None; st['sūktas'] += 1
            if pending is not None: pending['m'], pending['s'] = m, s; cur = pending; pending = None; st['sūkta introductions begun at their title line'] += 1
            else: start('intro')
            continue
        if t == '## ಪೀಠಿಕೆ': start('front'); cur['kind'] = 'preface'; continue
        mm = re.match(r'#### ಋಕ್ ([೦-೯]+)', t)
        if mm: rk = int(mm.group(1).translate(KD)); cur = None; st['Ṛk headings'] += 1; continue
        mm = re.fullmatch(r'\*([^*\[\]]+?)[.:]?\*', t)
        if mm and mm.group(1).strip() in LABELS:
            kind = LABELS[mm.group(1).strip()]; st['label ' + kind] += 1
            if pending is not None or (cur is not None and cur['kind'] == 'intro' and rk is None): ensure()['kn'].append(['label', kind]); continue      # a label inside a sūkta's introduction (Sāyaṇa's introductory block)
            prev = next((u for u in reversed(units) if u['s'] == s and u['rk'] == rk and u['m'] == m and u['kind'] == kind), None) if rk else None
            if prev is not None: cur = prev; cur['kn'].append(['break'])          # the label repeated after a page break: the same part goes on
            else: start(kind)
            continue
        if not t:
            if cur is not None and cur['kn'] and cur['kn'][-1][0] != 'break': cur['kn'].append(['break'])
            continue
        if TITLE.fullmatch(t) and pending is None and s is not None:                 # the title line of the next sūkta: its introduction begins here
            pending = dict(kind='intro', m=m, s=None, rk=None, kn=[]); units.append(pending); cur = pending
        u = ensure()
        if l.startswith('> '):
            if u['kn'] and u['kn'][-1][0] == 'block': u['kn'][-1][1].append(l[2:].rstrip())
            else: u['kn'].append(['block', [l[2:].rstrip()]]); st['Sanskrit blocks'] += 1
        elif t.startswith('[figure'): u['kn'].append(['figure', t]); st['figures'] += 1
        else: u['kn'].append(['text', l.rstrip()])
    for u in units:
        while u['kn'] and u['kn'][-1][0] == 'break': u['kn'].pop()
    return units, st

def words(s): return [w for w in re.split(r'[\s।॥]+', strip_ac(s)) if w and not re.fullmatch('[०-९0-9]+', w)]

def compare_verses(vol, units, ref):
    """Every Saṃhitā unit against the reference verse of its number: is it that verse, and where do the letters differ?
    A differing word of the edition is 'supported' when the same letters stand in the Pada-pāṭha or the bhāṣya of the same Ṛk (so it is the
    edition's reading, not a slip of the machine reading: DESIGN §13, F17); otherwise 'unsupported'."""
    by = {(u['m'], u['s'], u['rk'], u['kind']): u for u in units}; rows = []; st = collections.Counter()
    for u in units:
        if u['kind'] != 'samhita': continue
        key = (u['m'], u['s'], u['rk']); st['Saṃhitā units'] += 1
        ed = ' '.join(kn2deva(x) for it in u['kn'] if it[0] == 'block' for x in it[1])
        if key not in ref: st['no reference verse with this number'] += 1; rows.append((key, 'no reference verse', '', ed[:60], '')); u['ref'] = None; continue
        rv = ' '.join(ref[key]); u['ref'] = ref[key]
        a, b = canon(rv), canon(ed); ratio = difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()
        u['match'] = round(ratio, 3)
        if a == b or habit(rv) == habit(ed): st['equal to the reference (letters; spelling habits apart)'] += 1; u['diffs'] = []; continue
        if ratio < 0.6: st['does not look like the reference verse of its number'] += 1; rows.append((key, 'not this verse?', rv[:60], ed[:60], f'{ratio:.2f}')); u['diffs'] = None; continue
        st['same verse, letters differ'] += 1
        rw, ew = words(rv), words(ed); support = ''
        for kind in ('pada', 'bhashya'):
            o = by.get((u['m'], u['s'], u['rk'], kind))
            if o: support += ' ' + canon(' '.join(kn2deva(x) for it in o['kn'] if it[0] == 'block' for x in it[1]))
        diffs = []
        sm = difflib.SequenceMatcher(None, [canon(w) for w in rw], [canon(w) for w in ew], autojunk=False)
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == 'equal': continue
            r_, e_ = ' '.join(rw[i1:i2]), ' '.join(ew[j1:j2])
            if canon(r_) == canon(e_) or habit(r_) == habit(e_) or ''.join(habit(w) for w in rw[i1:i2]) == ''.join(habit(w) for w in ew[j1:j2]): st['places that differ in spelling habit only (not listed)'] += 1; continue
            state = 'supported' if e_ and all(canon(w) in support for w in ew[j1:j2] if len(canon(w)) > 2) and any(len(canon(w)) > 2 for w in ew[j1:j2]) else 'unsupported'
            diffs.append([r_, e_, state]); st['differing places: ' + state] += 1
            rows.append((key, 'verse differs: ' + state, r_, e_, ''))
        u['diffs'] = diffs
        if not diffs: st['same verse, letters differ'] -= 1; st['equal to the reference (letters; spelling habits apart)'] += 1
    return rows, st

def build(vol, mandalas):
    units, st = parse_kn(vol); ref = read_reference(mandalas)
    # merge parts that the Kannada file gives twice under one key (should not happen after the label rule above)
    first = next((u for u in units if u['kind'] == 'intro'), None)               # what stands after the preface and before the first sūkta heading is that sūkta's introduction
    loose = [u for u in units if u['s'] is None and u['kind'] != 'preface']
    if first is not None and loose:
        pre = []
        for u in loose: pre += ([['label', u['kind']]] if u['kind'] in ('bhashya',) else []) + u['kn']; units.remove(u)
        first['kn'] = pre + first['kn']; st['parts before the first sūkta heading joined to its introduction'] = len(loose)
    for u in units: u['id'] = unit_id(vol, u)
    ids = collections.Counter(u['id'] for u in units); st['unit ids used twice'] = sum(1 for v in ids.values() if v > 1)
    # the skeleton from the reference: which sūktas, how many verses
    suktas = sorted({(u['m'], u['s']) for u in units if u['s'] is not None}); sk = []
    for (m, s) in suktas:
        nref = len({r for (mm, ss, r) in ref if mm == m and ss == s}); have = sorted({u['rk'] for u in units if u['m'] == m and u['s'] == s and u['kind'] == 'samhita'})
        sk.append((m, s, nref, len(have), 'ok' if have == list(range(1, nref + 1)) else f'Ṛks present: {have}'))
    rows, st2 = compare_verses(vol, units, ref)
    P = vol_paths(vol); os.makedirs(P['data'], exist_ok=True); os.makedirs(P['review'], exist_ok=True)
    save_units(vol, units)
    with open(os.path.join(P['review'], 'source_faults.tsv'), 'w', encoding='utf8') as f:
        f.write('maṇḍala.sūkta.ṛk\tkind\treference\tKannada edition (supplied text)\tnote\tdecision\n')
        for key, kind, a, b, n in rows: f.write(f'{key[0]}.{key[1]}.{key[2]}\t{kind}\t{a}\t{b}\t{n}\t\n')
    kinds = collections.Counter(u['kind'] for u in units)
    rep = [f'# Vol {vol}: structure report (rv structure)', '', f'Units: {len(units)} (' + ', '.join(f'{k} {v}' for k, v in sorted(kinds.items())) + ')', '',
           '## Read from the Kannada file'] + [f'- {k}: {v}' for k, v in sorted(st.items())] + ['',
           '## Against the reference text (verses)', f'- sūktas in the volume: {len(sk)}; with every reference verse present once, in order: {sum(1 for x in sk if x[4] == "ok")}'] + \
          [f'  - {m}.{s}: reference {n} verses, volume {h}: {note}' for m, s, n, h, note in sk if note != 'ok'] + [f'- {k}: {v}' for k, v in sorted(st2.items())] + ['',
           'Every differing place is a row of `review/source_faults.tsv` (column "decision" for the editor).']
    open(os.path.join(P['review'], 'structure_report.md'), 'w', encoding='utf8').write('\n'.join(rep) + '\n')
    print('\n'.join(rep)); return units
