#!/usr/bin/env python3
"""Saṃhitā, Pada and Sāyaṇa-bhāṣya blocks of a volume's English markdown, taken from the Wikisource index.

Used by publish/volbook.py when a build is asked for `--wikisource` (or pubcfg.json has "wikisource": true). In memory only:
no volume file is changed. For every Ṛk of the volume the three blocks are replaced by the text of
refs/wikisource/index/ws.sqlite (tools/rv/ws_index.py): the accented Saṃhitā, the accented Pada (the plain Pada where the page has
no accented one) and Sāyaṇa's paragraphs for that Ṛk; the sūkta introduction of Sāyaṇa replaces the bhāṣya block before Ṛk 1.
Everything else in the volume (Gist, Pratipadārtha, Bhāvārtha, Special Topics, page marks, remarks) stays as it is. The IAST of the
Saṃhitā and Pada blocks is made afterwards by volbook.py as for any block; the bhāṣya stays Devanagari only.

A block the index cannot give (a Ṛk it lacks, a Ṛk whose commentary is shared with another and stands with the last of them) is left as the
volume has it, and counted in the report. Nothing is corrected. Where the volume's own text writes न्स (or न् स) and Wikisource न्त्स
(मघवन्त्सुवीर्यं), see docs/WIKISOURCE_NOTES.md: it is the traditional spelling and not a difference of text.
"""
import importlib.util, pathlib, re, sqlite3

ROOT = pathlib.Path(__file__).resolve().parents[2]
DB = ROOT / 'refs' / 'wikisource' / 'index' / 'ws.sqlite'
SUKTA = re.compile(r'^## S[ūu]kta\s+(\d+)(?:\s+\(Maṇḍala\s+(\d+)\))?')
RIK = re.compile(r'^#### Ṛk\s+(\d+)(\s+\(continued\))?\s*$')
USE = re.compile('सूत्रितं|इत्येषा|इत्यृच|सवने|शस्त्रे|याज्या|पशौ|प्रस्थित|षष्ठेऽहनि|सोमातिरेके')


def connect():
    if not DB.exists():
        spec = importlib.util.spec_from_file_location('ws_index', ROOT / 'tools' / 'rv' / 'ws_index.py')
        wi = importlib.util.module_from_spec(spec); spec.loader.exec_module(wi)
        wi.build()                                            # from refs/wikisource/raw/ (tools/rv/ws_pull.py makes it)
    return sqlite3.connect(DB)


def sukta_paras(con, m, s):
    """{Ṛk number (0 = introduction): [paragraphs]} in Sāyaṇa's order. A paragraph after the first one of a Ṛk that states a ritual use
    (the index marks it `prelude`) belongs to the NEXT Ṛk and is put at its front: Sāyaṇa states the use before the Ṛk."""
    rows = con.execute('select r, p, deva, prelude from para where m=? and s=? order by r, p', (m, s)).fetchall()
    by = {}
    for r, p, deva, pre in rows:
        by.setdefault(r, []).append((deva, pre))
    last = max((r for (r,) in con.execute('select r from rik where m=? and s=?', (m, s))), default=0)
    out, carry = {}, []
    for r in sorted(by):
        items = by[r]
        cut = next((k for k, (_, pre) in enumerate(items) if pre), None)
        own, move = ([d for d, _ in items], []) if cut is None or r >= last else ([d for d, _ in items[:cut]], [d for d, _ in items[cut:]])
        out[r] = carry + own
        carry = move
    if carry and last + 1 not in out:
        out[last] = out.get(last, []) + carry
    return out


def _quote(lines):
    return [f'> {l.strip()}' for l in lines if l.strip()]


def _quote_paras(paras):
    out = []
    for i, p in enumerate(paras):
        if i: out.append('>')
        out += [f'> {x.strip()}' for x in p.split('\n') if x.strip()]
    return out


def apply(md, default_mandala=None):
    """Return (new markdown, report dict)."""
    con = connect()
    rep = {'samhita': 0, 'pada': 0, 'bhashya': 0, 'intro': 0, 'kept': []}
    cache = {}
    def paras_of(m, s):
        if (m, s) not in cache: cache[(m, s)] = sukta_paras(con, m, s)
        return cache[(m, s)]
    M = S = R = None
    qkind, cont_ok, done = None, False, set()
    out = []
    for line in md.split('\n'):
        mm = SUKTA.match(line)
        if mm:
            S = int(mm.group(1)); M = int(mm.group(2)) if mm.group(2) else default_mandala
            R, qkind, cont_ok, done = 0, None, False, set()
            out.append(line); continue
        mm = RIK.match(line)
        if mm:
            R = int(mm.group(1))
            if not mm.group(2): qkind, done = None, {k for k in done if k[0] != R}
            cont_ok = bool(mm.group(2))
            out.append(line); continue
        if line.startswith('### Printed p'):
            cont_ok = True; out.append(line); continue
        if line.startswith('##### '):
            kind = ('samhita' if 'संहितापाठः' in line else 'pada' if 'पदपाठः' in line else 'bhashya' if 'सायणभाष्यम्' in line else None)
            if kind is None:
                cont_ok = False; out.append(line); continue
            qkind, cont_ok = kind, True
            if S is None or R is None:
                out.append(line); continue
            key = (R, kind)
            if key in done:                                   # the volume repeats a label for a Ṛk already given in full: drop it
                continue
            block = None
            if kind == 'bhashya':
                ps = paras_of(M, S).get(R)
                if ps: block = _quote_paras(ps)
                if R == 0 and block: rep['intro'] += 1
            else:
                row = con.execute('select samhita_acc, samhita, pada_acc, pada from rik where m=? and s=? and r=?', (M, S, R)).fetchone() if R else None
                if row:
                    txt = (row[0] or row[1]) if kind == 'samhita' else (row[2] or row[3])
                    if txt: block = _quote(txt.split('\n'))
            if block is None:
                rep['kept'].append((M, S, R, kind)); out.append(line); qkind = None; continue   # left as the volume has it
            out += [line, ''] + block + ['']
            done.add(key)
            if kind == 'bhashya' and R:
                rep['bhashya'] += 1
            elif kind != 'bhashya':
                rep[kind] += 1
            continue
        if line.startswith('>') and qkind and cont_ok and (R, qkind) in done:
            continue                                          # the volume's own lines of a block that has been replaced
        out.append(line)
    text = '\n'.join(out)
    text = re.sub(r'\n(?:#### Ṛk \d+ \(continued\)\n(?:\s*\n)*)(?=###? |#### |##### |\Z)', '\n', text)    # a "(continued)" heading left empty
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text, rep
