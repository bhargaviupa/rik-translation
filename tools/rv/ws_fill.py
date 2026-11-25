#!/usr/bin/env python3
"""Fill the [[block: samhita|pada|bhashya]] markers of a scan-made text from the Wikisource index (shared tool; Vol 25 first). No API, no network.

  python3 tools/rv/ws_fill.py VOL [--show M.S.R] [--write] [--src FILE] [--out FILE]
      reads volN/html/rig_N.md (the file made by tools/rv/scan_assemble.py), finds the sūkta headings (the box with `ಮಂಡಲ—… ಸೂಕ್ತ—…`),
      numbers the Ṛks of each sūkta by its [[block: samhita]] markers, and prints what it could fill. Without --write nothing is written.
      --show M.S.R  also prints the three blocks as they would be filled for that Ṛk (look at one before running on the volume).
      --start M.S   the file begins inside that sūkta (a later part of a volume): its Ṛks are numbered from the end of the sūkta.
      --write       writes volN/html/rig_N.filled.md (the source file stays as it is) and volN/review/ws_fill_log.tsv.

WHAT IT FILLS (Kannada script made with publish/tools/translit/deva_to_kannada.py; Wikisource is never edited, never compared):
  samhita  the Ṛk's plain Saṃhitā (index column `samhita`, no accents), the Ṛk number as `|| ೧ ||`
  pada     the Ṛk's plain Pada (`pada`), words as `a | b | c`, `ऽ` kept as `ಽ`, the Ṛk number as `|| ೧ ||`
  bhashya  Sāyaṇa's text printed after that Ṛk (index: the Ṛk's own section; Sāyaṇa often comments on two or three Ṛks together
           and the text stands after the last of them, so the Ṛks before it have NO bhāṣya block in the print: `rik.bh_at`)
           and, before the sūkta heading, the sūkta introduction (index `sukta.intro`).
  The wiki's quotation marks that mark the headwords (“ ” ") are not in the print and are left out; ‘ ’ and footnote marks [१] stay.
  danda `।` → `|`, double danda `॥` → `||` (as in the supplied files).

HOW THE MARKERS ARE READ. A marker line preceded (within the two lines before) by a label line (ಸಂಹಿತಾಪಾಠ…, ಪದಪಾ…, ಸಾಯಣಭಾಷ್ಯ…) starts a block. A bare marker
of the same kind as the one before, with no prose between, is the continuation of that block over a page break and is dropped (the block is
filled once, at the first marker). In a sūkta: samhita starts Ṛk n+1; pada belongs to it; a bhashya after the pada belongs to that Ṛk when the
index has a bhāṣya for it, otherwise (and always after the last Ṛk) it is the introduction of the next sūkta.

CHECKS (REQUIREMENTS D17): a sūkta is filled only if the count is right: Ṛks = index `n_rik` (and the heading's `ಋಕ್ಸಂಖ್ಯೆ` when it can be read), every Ṛk has
one samhita and one pada, the Ṛks with a bhāṣya in the index have exactly one bhashya block and no other Ṛk has one, the introduction is there when the
index has one. Otherwise the sūkta is left as it is and the reason is logged. Sūktas whose layout in the index is not `per-rik` (5.5.11, 9.97 Ṛk 10,
10.27 Ṛk 1: known defects of the pages, REQUIREMENTS B5.6) are left as they are and logged."""
import os, re, sys, json, sqlite3
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'publish', 'tools', 'translit'))
from deva_to_kannada import deva2kn
DB = os.path.join(ROOT, 'refs', 'wikisource', 'index', 'ws.sqlite')
KD = str.maketrans('೦೧೨೩೪೫೬೭೮೯', '0123456789')
DD = str.maketrans('०१२३४५६७८९', '0123456789')
LABEL = re.compile(r'^[\s॥|#\[\]•*]*(ಸಂಹಿತಾಪಾ|ಪದಪಾ|ಸಾಯಣಭಾಷ್ಯಂ|ಸಾಯಣಭಾಷ್ಯಮ್|ಸಾಯಣ ಭಾಷ್ಯಂ)[^\n]{0,12}$')   # a label line, not the running head (…ಸಾಯಣಭಾಷ್ಯಸಹಿತಾ / ಋಗ್ವೇದಸಂಹಿತಾ)
MARK = re.compile(r'^\[\[block:\s*(samhita|pada|bhashya)\s*\]\]\s*$')

def num(s):
    s = re.sub(r'\[\?\]', '', s).translate(KD); m = re.search(r'\d+', s)
    return (int(m.group()) if m else None)

ACC = re.compile('[\u0951-\u0954\u1CD0-\u1CFF\uA8E0-\uA8F7]')      # Vedic accent signs: the supplied machine text has none (a few pages of the index give the plain Saṃhitā with accents)

def kn(text, number_tail=True):
    t = re.sub(r'<ref[^>]*/>|<ref[^>]*>.*?</ref>', '', text, flags=re.S)          # wiki footnote markup that the index left in a layer (9.52.2 Saṃhitā: a Skandapurāṇa verse): not text of the layer
    t = ACC.sub('', t).replace('“', '').replace('”', '').replace('"', '')
    t = re.sub(r'॥\s*([०-९]+)\s*॥?\s*$', lambda m: '|| ' + m.group(1) + ' ||', t, flags=re.M)
    t = t.replace('।', '|').replace('॥', '||')
    return deva2kn(t)

def parse(src):
    """events: ('H', line, M, S, rikcount|None, flags) / (kind, line, is_new, parent_line) with kind sa|pa|bh; a continuation points at the line of the block it continues."""
    L = src.split('\n'); ev = []; lastkind = None; prose = False; parent = None
    for i, l in enumerate(L):
        if re.search('ಮಂಡಲ[—–-]', l):
            mm = re.search(r'ಮಂಡಲ[—–-]\s*([^\s।॥|]+)', l); ss = re.search(r'ಸೂಕ್ತ[—–-]\s*([^\s।॥|]+)', l)
            if mm and ss:
                flags = []
                if '[?]' in mm.group(1) or '[?]' in ss.group(1): flags.append('heading digits marked [?]')
                rc = None
                for k in range(i + 1, min(i + 6, len(L))):
                    r = re.search(r'ಋಕ್ಸಂಖ್ಯೆ[—–-]\s*([^\s।॥|]+)', L[k])
                    if r: rc = num(r.group(1)); break
                ev.append(('H', i, num(mm.group(1)), num(ss.group(1)), rc, flags)); lastkind = 'H'; prose = False; continue
        m = MARK.match(l.strip())
        if m:
            kind = {'samhita': 'sa', 'pada': 'pa', 'bhashya': 'bh'}[m.group(1)]
            prev = [x.strip() for x in L[max(0, i - 3):i] if x.strip()][-2:]
            labelled = any(LABEL.match(x) for x in prev)
            new = labelled or kind != lastkind or prose
            if new: parent = i
            ev.append((kind, i, new, parent)); lastkind = kind; prose = False; continue
        s = l.strip()
        if s and s != '---' and not LABEL.match(s) and 'ಋಗ್ವೇದಸಂಹಿತಾ' not in s and 'ಸಾಯಣಭಾಷ್ಯಸಹಿತಾ' not in s and not s.startswith('xxv') and not s.startswith('<!--') and not (len(s) < 90 and re.search(r'ಮಂ\.\s*[೦-೯]|ಸೂ\.\s*[೦-೯]|ವ\.\s*[೦-೯]', s)) and not re.match(r'^\[?\s*(xxv)?\.?\s*[0-9A-Za-z೦-೯]{1,4}\s*\]?\.?$', s):
            prose = True
    return L, ev

def paras(con, m, s, r):
    return '\n'.join(x[0] for x in con.execute('select deva from para where m=? and s=? and r=? order by p', (m, s, r)))

def main():
    a = sys.argv[1:]
    show = None; write = '--write' in a
    if write: a.remove('--write')
    src_f = out_f = start = None
    for opt in ('--show', '--src', '--out', '--start'):
        if opt in a:
            i = a.index(opt); v = a[i + 1]; del a[i:i + 2]
            if opt == '--show': show = v
            elif opt == '--src': src_f = v
            elif opt == '--start': start = v
            else: out_f = v
    vol = a[0]
    src_f = src_f or os.path.join(ROOT, f'vol{vol}', 'html', f'rig_{vol}.md'); out_f = out_f or os.path.join(ROOT, f'vol{vol}', 'html', f'rig_{vol}.filled.md')
    L, ev = parse(open(src_f, encoding='utf8').read())
    con = sqlite3.connect(DB); con.row_factory = sqlite3.Row
    log = []; suk = {}; order = []; cont = {}                # cont: continuation line -> line of the block it continues
    cur = None; r = 0; phase = None; pending = []
    if start:                                                # the file begins inside a sūkta (the later part of a volume): its Ṛks are counted from the end of the sūkta
        m_, s_ = [int(x) for x in start.split('.')]
        cur = {'ref': f'{m_}.{s_}', 'm': m_, 's': s_, 'rc': None, 'flags': [f'file begins inside the sūkta (--start {start}); Ṛks numbered from the end'], 'riks': {}, 'intro': [], 'line': 0, 'partial': True}
        cur['idx'] = con.execute('select * from sukta where m=? and s=?', (m_, s_)).fetchone()
        cur['rows'] = {x['r']: x for x in con.execute('select * from rik where m=? and s=? order by r', (m_, s_))}
        suk[(m_, s_)] = cur; order.append((m_, s_)); phase = 'start'
    for e in ev:
        k = e[0]
        if k == 'H':
            _, i, m_, s_, rc, fl = e; fl = list(fl)
            if cur is not None:                                      # the heading digits are read from a small old-style face: the sequence decides when they disagree
                exp = (cur['m'], cur['s'] + 1)
                if (m_, s_) != exp:
                    er = con.execute('select n_rik from sukta where m=? and s=?', (exp[0], exp[1])).fetchone()
                    if er and (rc is None or er[0] == rc or fl):
                        fl.append(f'heading read {m_}.{s_}, taken as {exp[0]}.{exp[1]} (the next in sequence)'); m_, s_ = exp
            cur = {'ref': f'{m_}.{s_}', 'm': m_, 's': s_, 'rc': rc, 'flags': fl, 'riks': {}, 'intro': pending, 'line': i}
            pending = []; r = 0; phase = 'H'
            cur['idx'] = con.execute('select * from sukta where m=? and s=?', (m_, s_)).fetchone()
            cur['rows'] = {x['r']: x for x in con.execute('select * from rik where m=? and s=? order by r', (m_, s_))}
            suk[(m_, s_)] = cur; order.append((m_, s_)); continue
        _, i, new, parent = e
        if not new: cont[i] = parent; continue
        if cur is None:
            if k == 'bh': pending.append(i)
            continue
        if cur.get('partial') and r == 0 and k in ('pa', 'bh'): cur.setdefault('orphans', []).append((k, i)); continue   # the rest of a Ṛk whose Saṃhitā is on an earlier page, outside this file
        if k == 'sa':
            if phase == 'sa': cont[i] = cur['riks'][r]['sa']; continue     # a second samhita label with no pada between: the same Ṛk
            r += 1; cur['riks'].setdefault(r, {})['sa'] = i; phase = 'sa'
        elif k == 'pa':
            if r == 0 or phase in ('pa', 'bh'): cur.setdefault('bad', []).append(f'pada marker at line {i + 1} without a samhita marker of its own'); continue
            cur['riks'][r]['pa'] = i; phase = 'pa'
        else:
            if phase in ('pa', 'sa'): cur['riks'][r]['bh'] = i; phase = 'bh'      # the bhāṣya after a Ṛk's pada (or samhita, when the pada marker is missing) belongs to that Ṛk
            else: pending.append(i); phase = 'bh_intro'               # a second one, or one before any Ṛk: the introduction of the next sūkta
    for c in suk.values():                                   # a sūkta that begins before the file: the last Ṛk printed is the last of the sūkta
        if c.get('partial') and c['idx'] is not None and c['riks']:
            shift = (c['idx']['n_rik'] if c['idx']['layout'] == 'per-rik' else c['idx']['n_plain']) - len(c['riks']); c['first'] = shift + 1
            c['riks'] = {x + shift: v for x, v in c['riks'].items()}
    fill = {}; ok = bad = 0
    for key in order:
        c = suk[key]; ref = c['ref']; idx = c['idx']; why = []
        if idx is None: log.append((ref, 'SKIP', 'not in the index')); bad += 1; continue
        if idx['layout'] not in ('per-rik', 'partial'): log.append((ref, 'SKIP', f'index layout {idx["layout"]} (known defect of the page)')); bad += 1; continue
        n = idx['n_rik'] if idx['layout'] == 'per-rik' else idx['n_plain']; got = len(c['riks']); why.extend(c.get('bad', []))
        first = c.get('first', 1)
        if got != n - first + 1: why.append(f'Ṛks in print {got}, index {n}')
        if c['rc'] and c['rc'] != n and idx['layout'] == 'per-rik': why.append(f'heading says {c["rc"]} Ṛks, index {n}')
        gaps = [f'{len(c["orphans"])} block marker(s) of a Ṛk begun on an earlier page left as they are (lines {[x[1] + 1 for x in c["orphans"]]})'] if c.get('orphans') else []
        for x in range(first, n + 1):
            blk = c['riks'].get(x, {}); row = c['rows'].get(x)
            if row is None: why.append(f'Ṛk {x}: not in the index'); continue
            if 'sa' not in blk: gaps.append(f'Ṛk {x}: no samhita block in print')
            if 'pa' not in blk: gaps.append(f'Ṛk {x}: no pada block in print')
            if bool(row['n_para']) != ('bh' in blk): gaps.append(f'Ṛk {x}: bhāṣya block {"missing in print" if row["n_para"] else "in print, none in the index"}')
        intro_idx = bool((idx['intro'] or '').strip()); intro_ok = intro_idx and len(c['intro']) >= 1
        if intro_ok and len(c['intro']) > 1: gaps.append(f'{len(c["intro"])} bhāṣya blocks before the heading: the last (line {c["intro"][-1] + 1}) taken as the introduction, the others (lines {[x + 1 for x in c["intro"][:-1]]}) left as markers: check')
        if intro_idx and not intro_ok and not c.get('partial'): gaps.append('introduction not filled: no bhāṣya block before the heading in print, index has one')
        if not intro_idx and c['intro']: gaps.append('introduction block in print, none in index (not filled)')
        if why: log.append((ref, 'SKIP', '; '.join(why) + ((' | ' + '; '.join(c['flags'])) if c['flags'] else ''))); bad += 1; continue
        for x in range(first, n + 1):
            row = c['rows'][x]; blk = c['riks'].get(x, {})
            if 'sa' in blk: fill[blk['sa']] = kn(row['samhita'])
            if 'pa' in blk: fill[blk['pa']] = kn(row['pada'])
            if 'bh' in blk and row['n_para']: fill[blk['bh']] = kn(paras(con, c['m'], c['s'], x))
        if intro_ok: fill[c['intro'][-1]] = kn(idx['intro'])
        note = '; '.join(gaps + c['flags'])
        log.append((ref, 'FILLED' if not gaps else 'PARTIAL', f'{n} Ṛks' + ((' | ' + note) if note else ''))); ok += 1
    if pending: log.append(('-', 'NOTE', f'{len(pending)} bhāṣya block(s) after the last sūkta heading, not assigned (lines {[x + 1 for x in pending][:5]})'))
    markers = sum(1 for l in L if MARK.match(l.strip())); dropped = [i for i, par in cont.items() if par in fill]
    print(f'{len(order)} sūkta headings read; filled {ok}, left {bad}; {len(fill)} blocks filled; markers in the file {markers}, continuation markers dropped {len(dropped)}')
    for ref, st, tx in log:
        if st != 'FILLED': print(f'  {st} {ref}: {tx}')
    if show:
        m_, s_, r_ = [int(x) for x in show.split('.')]
        c = suk.get((m_, s_))
        if not c or r_ not in c['riks']: print('--show: that Ṛk is not in the file')
        else:
            for kind in ('sa', 'pa', 'bh'):
                b = c['riks'][r_].get(kind)
                print(f'--- {show} {kind} (marker at line {b + 1 if b is not None else "-"}) ---'); print((fill.get(b, '(not filled: the sūkta was left)')) if b is not None else '(no block in print)')
    if write:
        drop = set(dropped); out = [fill[i] if i in fill else l for i, l in enumerate(L) if i not in drop]
        open(out_f, 'w', encoding='utf8').write('\n'.join(out))
        os.makedirs(os.path.join(ROOT, f'vol{vol}', 'review'), exist_ok=True)
        logname = 'ws_fill_log.tsv' if os.path.basename(out_f) == f'rig_{vol}.filled.md' else 'ws_fill_log_' + os.path.basename(out_f).split('.')[0] + '.tsv'
        with open(os.path.join(ROOT, f'vol{vol}', 'review', logname), 'w', encoding='utf8') as g:
            g.write('sukta\tstatus\ttext\n')
            for x in log: g.write('\t'.join(x) + '\n')
        print(f'written: {os.path.relpath(out_f, ROOT)} and vol{vol}/review/{logname}')

if __name__ == '__main__': main()
