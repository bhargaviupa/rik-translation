#!/usr/bin/env python3
"""Fill the `[[block: samhita|pada|bhashya]]` placeholders of a scan-based volume's assembled text from the Wikisource index (shared tool).

  python3 tools/rv/ws_fill.py VOL                 # dry run: count table per sūkta, nothing written
  python3 tools/rv/ws_fill.py VOL --show M.S.R    # dry run: print the three blocks as they would be placed for one Ṛk
  python3 tools/rv/ws_fill.py VOL --write         # fill the sūktas whose counts agree; the others stay untouched and are listed
  options: --file PATH (default volN/html/rig_N.md)   --keep-marks (keep the wiki's “ " pratīka marks in the bhāṣya)

WHAT IT DOES. The file is made by scan_assemble.py from page transcriptions that skipped the three Sanskrit layers (they are
the worst-read part of a scan). Each skipped block is a marker line. This tool
  1. finds the sūktas by their header line (`ಮಂಡಲ—8 ॥ ಅನುವಾಕ—7 ॥ ಸೂಕ್ತ—68 ॥`; Kannada digits); a header whose number is not the
     expected next one is used as read only if it is in the index, otherwise the expected number is taken and the sūkta is listed;
  2. joins consecutive markers of one kind that only a page break separates (running head, `---`, the label line) into ONE block;
  3. the bhāṣya block just before a header is the sūkta introduction (Ṛk 0); the k-th `samhita` block of a sūkta is Ṛk k, the k-th
     `pada` block is Ṛk k, the other bhāṣya blocks go in order to the Ṛks that carry Sāyaṇa's text (the commentary of two or three
     Ṛks stands with the last of them; the ritual-use paragraph that Sāyaṇa states before the next Ṛk is moved as `ws_layers.sukta_paras` does);
  4. compares the counts with the index. A sūkta whose counts do not agree is NOT filled and is listed. Nothing in Wikisource is
     edited or compared with the print; its known defects (5.5.11, 9.97 Ṛk 10, 10.27 Ṛk 1) are listed if met.
The Devanagari of the index is converted letter for letter by publish/tools/translit/deva_to_kannada.py: Saṃhitā and Pada plain (no accent marks), the
bhāṣya as Sāyaṇa's paragraphs, one per line, blank line between paragraphs. The wiki's pratīka marks (“ ") are dropped from the bhāṣya unless --keep-marks.
Report: volN/review/ws_fill_report.tsv (one row per sūkta).
"""
import os, re, sys, sqlite3, importlib.util
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'publish', 'tools', 'translit')); sys.path.insert(0, os.path.join(ROOT, 'publish', 'tools'))
from deva_to_kannada import deva2kn
import ws_layers

MARK = re.compile(r'^\[\[block:\s*(samhita|pada|bhashya)\s*\]\]\s*$')
HEAD = re.compile(r'ಸಾಯಣ ?ಭಾಷ್ಯ ?ಸ[ಹಂ]ಿತಾ|ಋಗ್ವೇದ ?ಸಂಹಿತಾ|ಮಂ\. ?[೦-೯]+')
LABEL = re.compile(r'^[॥।|#*\s]*(ಸಂಹಿತಾ ?ಪಾ.{0,3}|ಪದ ?ಪಾ.{0,3}|ಸಾಯಣ ?ಭಾಷ್ಯಂ)[॥।|#*\s]*$')
SIG = re.compile(r'^\[?\s*(xxv\.?\s*\S{0,3}|[0-9]{1,3})\s*\]?$')   # printer's signature at the foot of a page: [ xxv. 2 ]
HDR = re.compile(r'ಮಂಡಲ\s*[—–-]\s*([೦-೯0-9]+)[^ಸ\n]*?ಸೂಕ್ತ\s*[—–-]\s*([೦-೯0-9]+)')
KD = str.maketrans('೦೧೨೩೪೫೬೭೮೯', '0123456789')
KNOWN_DEFECT = {(5, 5): 'Ṛk 11', (9, 97): 'Ṛk 10', (10, 27): 'Ṛk 1'}


def parse(lines):
    """-> (groups, headers). group = dict(kind, lines=[marker line numbers]); header = (line no, m, s)"""
    marks = [(i, MARK.match(l).group(1)) for i, l in enumerate(lines) if MARK.match(l)]
    heads = [(i, int(m.group(1).translate(KD)), int(m.group(2).translate(KD))) for i, l in enumerate(lines) for m in [HDR.search(l)] if m]
    groups = []
    for i, kind in marks:
        if groups and groups[-1]['kind'] == kind:
            j = groups[-1]['lines'][-1]
            between = [l.strip() for l in lines[j + 1:i]]
            if all(not t or t == '---' or HEAD.search(t) or LABEL.match(t) or SIG.match(t) for t in between) and not any(h[0] > j and h[0] < i for h in heads):
                groups[-1]['lines'].append(i); continue
        groups.append({'kind': kind, 'lines': [i]})
    return groups, heads


def plan(lines, con):
    """per sūkta: dict(m, s, intro, samhita[], pada[], bhashya[], header line)"""
    groups, heads = parse(lines)
    events = sorted([(g['lines'][0], 'g', g) for g in groups] + [(h[0], 'h', h) for h in heads], key=lambda e: e[0])
    suk, cur, prev = [], None, None
    for k, (pos, typ, x) in enumerate(events):
        if typ == 'h':
            _, m, s = x
            note = ''
            exp = None if prev is None else ((prev[0], prev[1] + 1))
            if not con.execute('select 1 from sukta where m=? and s=?', (m, s)).fetchone() or (exp and (m, s) != exp and (m, s) != (prev[0] + 1, 1)):
                if exp: note = f'header read {m}.{s}, expected {exp[0]}.{exp[1]}: expected number used'; m, s = exp
                else: note = f'header {m}.{s} not in the index'
            cur = {'m': m, 's': s, 'line': pos, 'intro': None, 'samhita': [], 'pada': [], 'bhashya': [], 'note': note, 'order': [], 'gaps': []}
            suk.append(cur); prev = (m, s)
            if k and events[k - 1][1] == 'g' and events[k - 1][2]['kind'] == 'bhashya' and events[k - 1][2].get('_pending'):
                cur['intro'] = events[k - 1][2]
        else:
            if k + 1 < len(events) and events[k + 1][1] == 'h' and x['kind'] == 'bhashya':
                x['_pending'] = True
                # the introduction belongs to the NEXT header: attach when that header is created (above)
            elif cur is not None:
                last = [e for e in cur['order'] if True][-1:] if cur['order'] else []
                if last and (last[0][0], x['kind']) not in (('samhita', 'pada'), ('pada', 'bhashya'), ('pada', 'samhita'), ('bhashya', 'samhita')):
                    cur['gaps'].append(f"{last[0][0]} then {x['kind']} at lines {last[0][1] + 1}, {x['lines'][0] + 1} (Ṛk {len(cur['samhita'])})")
                cur['order'].append((x['kind'], x['lines'][-1])); cur[x['kind']].append(x)
    # the introductions of the first sūkta of a file stand before its header: attach (done above through _pending)
    return suk


def block_text(kind, con, m, s, r, paras, keep_marks):
    if kind == 'bhashya':
        ps = paras.get(r, [])
        if not ps: return None
        out = []
        for p in ps:
            t = p if keep_marks else re.sub('[“"]', '', p)
            out += [deva2kn(x.strip()) for x in t.split('\n') if x.strip()] + ['']
        return out[:-1]
    row = con.execute(f'select {"samhita" if kind == "samhita" else "pada"} from rik where m=? and s=? and r=?', (m, s, r)).fetchone()
    if not row or not row[0]: return None
    return [deva2kn(x.strip()) for x in row[0].split('\n') if x.strip()]


def main():
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    vol = a[0]; write = '--write' in a; keep = '--keep-marks' in a
    show = a[a.index('--show') + 1] if '--show' in a else None
    path = a[a.index('--file') + 1] if '--file' in a else os.path.join(ROOT, f'vol{vol}', 'html', f'rig_{vol}.md')
    lines = open(path, encoding='utf8').read().split('\n')
    con = ws_layers.connect()
    suk = plan(lines, con)
    rows, repl, listed = [], {}, []
    for S in suk:
        m, s = S['m'], S['s']
        n = con.execute('select count(*) from rik where m=? and s=?', (m, s)).fetchone()[0]
        paras = ws_layers.sukta_paras(con, m, s)
        keys = [r for r in sorted(paras) if r >= 1]
        has_intro = 0 in paras
        got = (len(S['samhita']), len(S['pada']), len(S['bhashya']), 1 if S['intro'] else 0)
        want = (n, n, len(keys), 1 if has_intro else 0)
        ok = got == want and n > 0
        rows.append((m, s, n, *got, *want[2:], 'filled' if ok else 'NOT FILLED', '; '.join(filter(None, [S['note']] + ([] if ok else S['gaps'])))))
        if (m, s) in KNOWN_DEFECT: listed.append(f'{m}.{s}: known Wikisource defect at {KNOWN_DEFECT[(m, s)]} (NOTE)')
        if not ok: continue
        def put(g, text):
            repl[g['lines'][0]] = text
            for j in g['lines'][1:]: repl[j] = None
        if S['intro']: put(S['intro'], block_text('bhashya', con, m, s, 0, paras, keep))
        for k, g in enumerate(S['samhita'], 1): put(g, block_text('samhita', con, m, s, k, paras, keep))
        for k, g in enumerate(S['pada'], 1): put(g, block_text('pada', con, m, s, k, paras, keep))
        for r, g in zip(keys, S['bhashya']): put(g, block_text('bhashya', con, m, s, r, paras, keep))
        if show == f'{m}.{s}.{1}' or (show and show.startswith(f'{m}.{s}.')):
            r = int(show.split('.')[2])
            print(f'--- {show}: Saṃhitā ---'); print('\n'.join(block_text('samhita', con, m, s, r, paras, keep) or ['(none)']))
            print(f'--- {show}: Pada ---'); print('\n'.join(block_text('pada', con, m, s, r, paras, keep) or ['(none)']))
            print(f'--- {show}: Bhāṣya (blocks under Ṛk {r}) ---'); print('\n'.join(block_text('bhashya', con, m, s, r, paras, keep) or ['(no bhāṣya block under this Ṛk)']))
    hdr = ('M', 'S', 'riks_index', 'samhita_blocks', 'pada_blocks', 'bhashya_blocks', 'intro_blocks', 'bhashya_expected', 'intro_expected', 'status', 'note')
    print('\t'.join(hdr))
    for r in rows: print('\t'.join(map(str, r)))
    bad = [r for r in rows if r[9] != 'filled']
    print(f'\n{len(rows)} sūktas found; {len(rows) - len(bad)} agree with the index; {len(bad)} do not (listed, not filled). Known defects met: {listed or "none"}')
    left = sum(1 for l in lines if MARK.match(l))
    if write:
        out = []
        for i, l in enumerate(lines):
            if i in repl:
                if repl[i] is not None: out += repl[i]
            else: out.append(l)
        open(path, 'w', encoding='utf8').write('\n'.join(out))
        rep = os.path.join(ROOT, f'vol{vol}', 'review', 'ws_fill_report.tsv'); os.makedirs(os.path.dirname(rep), exist_ok=True)
        open(rep, 'w', encoding='utf8').write('\t'.join(hdr) + '\n' + '\n'.join('\t'.join(map(str, r)) for r in rows) + '\n')
        left2 = sum(1 for l in out if MARK.match(l))
        print(f'written {os.path.relpath(path, ROOT)}; marker lines before {left}, after {left2}; report {os.path.relpath(rep, ROOT)}')


if __name__ == '__main__':
    main()
