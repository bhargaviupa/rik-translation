"""Step 2 of docs/DESIGN.md: the structure of a volume, made by script.

Input: the volume's Kannada text as the existing scripts make it from the supplied text (page marks, section labels, Sanskrit blocks) and the
reference text of the verses.  Output: volN/data/units.jsonl — one unit per part of a Ṛk (and per sūkta introduction, and the front matter),
each with its Kannada-side content in order; and the report of what does not fit (volN/review/source_faults.tsv, structure_report.md)."""
import re, os, csv, difflib, collections
from .common import *

LABELS = {'ಸಂಹಿತಾಪಾಠಃ': 'samhita', 'ಪದಪಾಠಃ': 'pada', 'ಸಾಯಣಭಾಷ್ಯಂ': 'bhashya', 'ಸಾಯಣಭಾಷ್ಯಮ್': 'bhashya', 'ಪ್ರತಿಪದಾರ್ಥ': 'pratipada', 'ಭಾವಾರ್ಥ': 'bhavartha',
          'English Translation': 'english', 'ವಿಶೇಷವಿಷಯಗಳು': 'vishesha', 'ವ್ಯಾಕರಣಪ್ರಕ್ರಿಯಾ': 'grammar'}
STRAY = re.compile(r'[-–—_.:;,|\s0-9೦-೯]*[0-9೦-೯_][-–—_.:;,|\s0-9೦-೯]*')      # a loose figure or an ornament line: no letter in it
STRAY_LATIN = re.compile(r'[A-Za-z0-9\-]{1,8}')                                  # a short Latin scrap in Kannada text (page signature misread)
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
        elif STRAY.fullmatch(t) or (u['kind'] != 'english' and STRAY_LATIN.fullmatch(t)):
            u['kn'].append(['stray', t]); st['stray lines removed (record: review/stray_lines_removed.tsv)'] += 1
        else: u['kn'].append(['text', l.rstrip()])
    for u in units:
        while u['kn'] and u['kn'][-1][0] == 'break': u['kn'].pop()
    return units, st

def words(s): return [w for w in re.split(r'[\s।॥]+', strip_ac(s)) if w and not re.fullmatch('[०-९0-9]+', w)]

def compare_verses(vol, units, ref):
    """Every Saṃhitā unit against the reference verse of its number: is it that verse, and where do the letters differ?
    A differing word of the edition is 'supported' when the same letters stand in the Pada-pāṭha or the bhāṣya of the same Ṛk (so it is the
    edition's reading, not a slip of the machine reading: DESIGN §13, F17); otherwise 'unsupported'."""
    by = {(u['m'], u['s'], u['rk'], u['kind']): u for u in units}; rows = []; st = collections.Counter(); kfix = []
    dec = {}; dp = os.path.join(vol_paths(vol)['data'], 'verse_decisions.tsv')        # the editor's decisions from the printed book: they outlive every re-run
    if os.path.exists(dp):
        for r in list(csv.reader(open(dp, encoding='utf8'), delimiter='\t'))[1:]:
            if len(r) >= 4: dec[(r[0].strip(), canon(r[1]), canon(r[2]))] = r[3].strip()
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
        rw, ew = words(rv), words(ed)
        # the witnesses inside the edition itself: the Pada-pāṭha and the word meanings of the same Ṛk (user, Nov 13 2026: where they have
        # the reference form, the supplied verse is a misreading and is settled without the editor)
        wit = ''
        for kind in ('pada', 'pratipada'):
            o = by.get((u['m'], u['s'], u['rk'], kind))
            if not o: continue
            if kind == 'pada': wit += ' ' + ' '.join(habit(w) for it in o['kn'] if it[0] == 'block' for x in it[1] for w in kn2deva(x).split())
            else:                                                             # of the word meanings only the headwords (what stands before the dash of each entry)
                txt = ' '.join(it[1] for it in o['kn'] if it[0] == 'text')
                wit += ' ' + ' '.join(habit(w) for e in re.split(r'[।॥]', txt) for w in kn2deva(re.split(r'[—–-]', e)[0]).split())
        def judge(r_, e_):
            a_, b_ = habit(r_), habit(e_); rf = ef = False; seen = False
            for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a_, b_, autojunk=False).get_opcodes():
                if tag == 'equal': continue
                seen = True                                                   # several windows round the differing letters: sandhi changes a word's end in the verse
                for lo, hi in ((2, 0), (3, 0), (2, 1), (1, 1), (1, 2), (0, 2), (2, 2)):
                    g = a_[max(0, i1 - lo):i2 + hi]; h = b_[max(0, j1 - lo):j2 + hi]
                    if len(g) >= 3 and g in wit: rf = True
                    if len(h) >= 3 and h in wit: ef = True
            if not seen: return 'undecided'
            if rf: return 'misread'                       # the Pada-pāṭha or a headword of the word meanings has the reference form: the supplied verse is misread
                                                          # (also when the other of the two repeats the misreading: 3.40.2, Pada ತತೃಸಿಂ, headword ತಾತೃಪಿಂ; user, Nov 13 2026)
            if ef and not rf: return 'edition'            # they have the same form as the supplied verse: a reading of the edition
            return 'undecided'
        diffs = []
        sm = difflib.SequenceMatcher(None, [canon(w) for w in rw], [canon(w) for w in ew], autojunk=False)
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == 'equal': continue
            r_, e_ = ' '.join(rw[i1:i2]), ' '.join(ew[j1:j2])
            if canon(r_) == canon(e_) or habit(r_) == habit(e_) or ''.join(habit(w) for w in rw[i1:i2]) == ''.join(habit(w) for w in ew[j1:j2]): st['places that differ in spelling habit only (not listed)'] += 1; continue
            how = judge(r_, e_) if r_ and e_ else 'undecided'
            d_ = dec.get((f'{key[0]}.{key[1]}.{key[2]}', canon(r_), canon(e_)))
            # user, Nov 13 2026 (after checking six places against the printed book, all six agreeing with the reference): the reference is the
            # correct source; every difference of the supplied verse is taken as a misreading of the machine text and gets no footnote.
            # Only a place the editor marks 'edition' in data/verse_decisions.tsv (the printed book really differs) is footnoted.
            state = 'edition' if d_ == 'edition' else 'misread'
            why = ('the editor: the printed book differs' if d_ == 'edition' else 'checked by the editor against the printed book' if d_ == 'misread' else
                   'the Pada-pāṭha or the word meanings have the reference form' if how == 'misread' else 'by rule: the reference is taken as correct')
            diffs.append([r_, e_, state]); st['differing places: ' + ('footnoted (edition reading)' if state == 'edition' else why)] += 1
            rows.append((key, 'verse differs', r_, e_, ('edition reading — footnote' if state == 'edition' else 'misread — ' + why)))
        u['diffs'] = diffs
        # the Kannada book's verse, corrected from the reference in the same places (user, Nov 13 2026): only the differing words are replaced,
        # written in the edition's own spelling habit (anusvāra for the class nasal and for a final m); the supplied lines stay in u['kn']
        lines = [x for it in u['kn'] if it[0] == 'block' for x in it[1]]; spans = []
        for li, line in enumerate(lines):
            for mm in re.finditer(r'[^\s।॥]+', line):
                if not re.fullmatch('[೦-೯0-9]+', mm.group(0)): spans.append((li, mm.start(), mm.end()))
        if len(spans) == len(ew):
            edits = []
            for tag, i1, i2, j1, j2 in sm.get_opcodes():
                if tag == 'equal' or j1 == j2: continue
                r_, e_ = ' '.join(rw[i1:i2]), ' '.join(ew[j1:j2])
                if not r_ or canon(r_) == canon(e_) or habit(r_) == habit(e_) or ''.join(habit(w) for w in rw[i1:i2]) == ''.join(habit(w) for w in ew[j1:j2]): continue
                if dec.get((f'{key[0]}.{key[1]}.{key[2]}', canon(r_), canon(e_))) == 'edition': continue
                if spans[j1][0] != spans[j2 - 1][0]: st['Kannada verse: a correction that would cross a line, left'] += 1; continue
                new = ' '.join(deva2kn(re.sub('म्$', 'ं', w)) for w in rw[i1:i2]); edits.append((spans[j1][0], spans[j1][1], spans[j2 - 1][2], new))
            if edits:
                new_lines = list(lines)
                for li, a_, b_, new in sorted(edits, key=lambda x: (x[0], -x[1])):
                    kfix.append((key, new_lines[li][a_:b_], new)); new_lines[li] = new_lines[li][:a_] + new + new_lines[li][b_:]
                u['kn_corrected'] = new_lines; st['Kannada verses corrected from the reference'] += 1; st['Kannada verse words replaced'] += len(edits)
        else: st['Kannada verse: words could not be counted off against the comparison, left as supplied'] += 1
        if not diffs: st['same verse, letters differ'] -= 1; st['equal to the reference (letters; spelling habits apart)'] += 1
    return rows, st, kfix

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
    rows, st2, kfix = compare_verses(vol, units, ref)
    P = vol_paths(vol); os.makedirs(P['data'], exist_ok=True); os.makedirs(P['review'], exist_ok=True)
    save_units(vol, units)
    with open(os.path.join(P['review'], 'source_faults.tsv'), 'w', encoding='utf8') as f:
        f.write('maṇḍala.sūkta.ṛk\tkind\treference\tKannada edition (supplied text)\tnote\tdecision\n')
        for key, kind, a, b, n in rows:
            if kind != 'verse differs' or n.startswith('edition'): f.write(f'{key[0]}.{key[1]}.{key[2]}\t{kind}\t{a}\t{b}\t{n}\t\n')      # the editor's list holds only what is still open (user, Nov 13 2026)
    with open(os.path.join(P['review'], 'stray_lines_removed.tsv'), 'w', encoding='utf8') as f:      # a record only (user, Nov 13 2026: they really are strays; not a list for the editor)
        f.write('maṇḍala.sūkta.ṛk\tin\tline of the supplied text, not printed\n')
        for u in units:
            for it in u['kn']:
                if it[0] == 'stray': f.write(f"{u.get('m') or ''}.{u.get('s') or ''}.{u.get('rk') or ''}\t{u['kind']}\t{it[1]}\n")
    with open(os.path.join(P['review'], 'verse_misreadings_settled.tsv'), 'w', encoding='utf8') as f:      # the record of what the script settled; not a list for the editor
        f.write('maṇḍala.sūkta.ṛk\treference (printed)\tsupplied text (taken as misread)\thow it was settled\n')
        for key, kind, a, b, n in rows:
            if n.startswith('misread'): f.write(f'{key[0]}.{key[1]}.{key[2]}\t{a}\t{b}\t{n[10:]}\n')
    with open(os.path.join(P['review'], 'kannada_verse_corrections.tsv'), 'w', encoding='utf8') as f:
        f.write('maṇḍala.sūkta.ṛk\tsupplied text\tprinted in the Kannada book (from the reference)\n')
        for key, a, b in kfix: f.write(f'{key[0]}.{key[1]}.{key[2]}\t{a}\t{b}\n')
    kinds = collections.Counter(u['kind'] for u in units)
    rep = [f'# Vol {vol}: structure report (rv structure)', '', f'Units: {len(units)} (' + ', '.join(f'{k} {v}' for k, v in sorted(kinds.items())) + ')', '',
           '## Read from the Kannada file'] + [f'- {k}: {v}' for k, v in sorted(st.items())] + ['',
           '## Against the reference text (verses)', f'- sūktas in the volume: {len(sk)}; with every reference verse present once, in order: {sum(1 for x in sk if x[4] == "ok")}'] + \
          [f'  - {m}.{s}: reference {n} verses, volume {h}: {note}' for m, s, n, h, note in sk if note != 'ok'] + [f'- {k}: {v}' for k, v in sorted(st2.items())] + ['',
           'Every differing place is a row of `review/source_faults.tsv` (column "decision" for the editor).']
    open(os.path.join(P['review'], 'structure_report.md'), 'w', encoding='utf8').write('\n'.join(rep) + '\n')
    print('\n'.join(rep)); return units
