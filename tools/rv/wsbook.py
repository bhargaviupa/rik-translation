#!/usr/bin/env python3
"""Sāyaṇa-bhāṣya book from the Wikisource text (experiment, Vol 11): units, task files, English check, document.

    python3 tools/rv/wsbook.py units M S          # the numbered units of a sūkta (what the translator renders)
    python3 tools/rv/wsbook.py task M S           # writes vol<N>/sayana_book/task/M<m>_S<sss>.md, prints its path
    python3 tools/rv/wsbook.py check M S          # checks vol<N>/sayana_book/en/M<m>_S<sss>.md against the units
    python3 tools/rv/wsbook.py build VOL          # writes vol<VOL>/Rigveda_Samhita_Vol<VOL>_Sayana_Bhashya.md

Source: refs/wikisource/M<mm>_S<sss>.json (tools/rv/wikisource_sayana.py). Nothing is corrected.

REFERENCE NUMBERS. Every unit has one: SBh M.S.R.U = Sāyaṇa-bhāṣya, maṇḍala M, sūkta S, Ṛk R (0 = Sāyaṇa's
introduction to the sūkta), unit U in Sāyaṇa's order within it. A Ṛk's reference is SBh M.S.R. The volumes cite
"SBh 1.137.2" for the Ṛk; the book prints each unit under its own number, with an anchor.

UNITS. The page gives Sāyaṇa's text on a Ṛk as one or more paragraphs. A paragraph is cut after each ॥ (or ।।); a
piece under 12 words joins the one before; a piece over 90 words is cut at a । near its middle. A paragraph after
the first one of a Ṛk that announces the ritual use of the NEXT Ṛk (it has सूत्रितं, इत्येषा, सवने, शस्त्रे,
याज्या, पशौ, प्रस्थित…) is moved to the front of that Ṛk (Sāyaṇa states the use before the Ṛk); the moves are
listed in vol<N>/review/ws_structure.tsv so that they can be looked at.

THE ENGLISH FILE has one section per unit, `## SBh M.S.R.U`, nothing else. Sanskrit is cited as ⟦…⟧ copied from
the unit (checked letter for letter, as in tools/rv/BHASHYA_BRIEF.md rule 4); the script adds the transliteration.
A doubt is marked `**NOTE**{question}`; the question goes to vol<N>/review/ws_notes.tsv.
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'publish'))
sys.path.insert(0, str(ROOT / 'publish' / 'tools' / 'translit'))
import bhashya_check as bc                        # form rules of the older reader: reused, not copied
from add_iast import deva_to_iast

WS = ROOT / 'refs' / 'wikisource'
USE = re.compile('सूत्रितं|इत्येषा|इत्यृच|सवने|शस्त्रे|याज्या|पशौ|प्रस्थित|षष्ठेऽहनि|सोमातिरेके')
SQ = bc.SQUEEZE


def load(m, s):
    return json.loads((WS / f'M{int(m):02d}_S{int(s):03d}.json').read_text(encoding='utf-8'))


def cut(par):
    pieces = [x.strip() for x in re.split(r'(?<=॥)\s+(?=\S)|(?<=।।)\s+(?=\S)', par) if x.strip()]
    out = []
    for p in pieces:                                  # join short pieces to the one before
        if out and len(p.split()) < 12:
            out[-1] += ' ' + p
        else:
            out.append(p)
    if len(out) > 1 and len(out[0].split()) < 12:      # a short first piece joins the next
        out[1] = out[0] + ' ' + out[1]; out = out[1:]
    res = []
    for p in out:
        todo = [p]
        while todo:
            q = todo.pop(0)
            w = q.split()
            if len(w) <= 90:
                res.append(q); continue
            idx = [i for i, x in enumerate(w) if x.endswith('।') and 20 < i < len(w) - 20]
            if not idx:
                res.append(q); continue
            k = min(idx, key=lambda i: abs(i - len(w) / 2)) + 1
            todo[:0] = [' '.join(w[:k]), ' '.join(w[k:])]
    return res


def units(m, s):
    """[(ref, n, deva)] in Sāyaṇa's order, and the list of moved paragraphs."""
    d = load(m, s)
    ref = lambda n, k: f'{m}.{s}.{n}.{k}'
    out, moved, pre = [], [], []
    def add(n, pars):
        merged = []
        for par in pars:
            for u in cut(par):
                if merged and len(u.split()) < 12 and len(merged[-1].split()) < 40:
                    merged[-1] += ' ' + u                   # a short piece joins the one before, over a paragraph break too
                else:
                    merged.append(u)
        for k, u in enumerate(merged, 1):
            out.append((ref(n, k), n, u))
    add(0, [p for p in d['intro'].split('\n') if p.strip()])
    for r in d['rks']:
        pars = [p for p in r['bhashya'].split('\n') if p.strip()]
        own, nxt, flag = [], [], False
        for i, p in enumerate(pars):
            if i > 0 and (flag or USE.search(p)) and r['n'] < d['rks'][-1]['n']:
                flag = True; nxt.append(p)
            else:
                own.append(p)
        add(r['n'], pre + own)
        for p in nxt:
            moved.append((f'{m}.{s}', r['n'], r['n'] + 1, p[:70]))
        pre = nxt
    return out, moved, d


def vol_of(m):
    return {1: None}.get(m)


def volume_for(m, s):
    for v in sorted(ROOT.glob('vol*/volcfg.json')):
        c = json.loads(v.read_text(encoding='utf-8'))
        if m in c.get('mandalas', []) and (WS / f'M{m:02d}_S{s:03d}.json').exists():
            lo = re.search(r'Sūkta (\d+) ', (ROOT / c['out']['en']).read_text(encoding='utf-8')) if (ROOT / c['out']['en']).exists() else None
            txt = (ROOT / c['out']['en']).read_text(encoding='utf-8') if (ROOT / c['out']['en']).exists() else ''
            if re.search(rf'^## Sūkta {s} ', txt, flags=re.M):
                return c['vol']
    return None


def paths(m, s, vol):
    b = ROOT / f'vol{vol}' / 'sayana_book'
    return b / 'task' / f'M{m}_S{s:03d}.md', b / 'en' / f'M{m}_S{s:03d}.md'


def cmd_task(m, s):
    vol = volume_for(m, s)
    if vol is None:
        sys.exit(f'{m}.{s}: no volume has this sūkta')
    us, moved, d = units(m, s)
    tp, ep = paths(m, s, vol)
    tp.parent.mkdir(parents=True, exist_ok=True)
    L = [f'# Task: English of Sāyaṇa\'s bhāṣya on {m}.{s} (volume {vol}); text of sa.wikisource.org rev. {d["revision"]}', '',
         f'Write your English to `{ep.relative_to(ROOT)}` — one section `## SBh M.S.R.U` for each unit below, in this order, '
         'nothing else (rules: tools/rv/BHASHYA_BRIEF.md 1, 2, 4, 5, 6, 8 and docs/WSBOOK_BRIEF.md).', '']
    byn = {}
    for r in us: byn.setdefault(r[1], []).append(r)
    rks = {r['n']: r for r in d['rks']}
    for n in sorted(byn):
        L.append(f'## {"Introduction" if n == 0 else "Ṛk " + str(n)}')
        if n:
            L += ['', '> Saṃhitā: ' + rks[n]['samhita'].replace('\n', ' / '), '> Pada: ' + rks[n]['pada'].replace('\n', ' / ')]
        for ref, _, u in byn[n]:
            L += ['', f'### SBh {ref}', '', '> ' + u]
        L.append('')
    tp.write_text('\n'.join(L), encoding='utf-8')
    print(f'task: {tp.relative_to(ROOT)}\nwrite your English to: {ep.relative_to(ROOT)}\n{len(us)} units')
    return 0


def render(raw, notes, where):
    def note(mm):
        notes.append((where, re.sub(r'[⟦⟧]', '', mm.group(1)).strip(), re.sub(r'[⟦⟧]', '', raw[max(0, mm.start() - 60):mm.start()]).replace('\n', ' ').strip()))
        return '**NOTE**'
    t = re.sub(r'\*\*NOTE\*\*\{([^{}]*)\}', note, raw)
    t = re.sub(r'(?<=\S)\*\*NOTE\*\*', ' **NOTE**', t)
    L = '[ऀ-॥॰-ॿ]'
    unh = lambda q: re.sub(f'(?<={L})-\\s*(?={L})', '', q.strip())
    return re.sub(r'⟦(.*?)⟧', lambda x: f'{unh(x.group(1))} (*{deva_to_iast(unh(x.group(1)))}*)', t, flags=re.S)


def read_en(path):
    parts = re.split(r'^## (.+)$', path.read_text(encoding='utf-8'), flags=re.M)
    return parts[0], [(parts[i].strip(), parts[i + 1].strip()) for i in range(1, len(parts), 2)]


def check(m, s, quiet=False):
    vol = volume_for(m, s)
    us, _, _ = units(m, s)
    _, ep = paths(m, s, vol)
    if not ep.exists():
        print(f'{m}.{s}: no English file yet ({ep.relative_to(ROOT)})'); return 2
    pre, got = read_en(ep)
    faults = []
    if pre.strip(): faults.append('text before the first heading')
    want = [f'SBh {r[0]}' for r in us]
    if [h for h, _ in got] != want:
        gh = [h for h, _ in got]
        miss = [w for w in want if w not in gh]; extra = [g for g in gh if g not in want]
        faults.append(f'headings differ from the units: missing {miss[:6]}, unexpected {extra[:6]}, order {"ok" if not miss and not extra else "?"}')
    deva = {f'SBh {r[0]}': r[2] for r in us}
    words = 0
    for h, body in got:
        u = deva.get(h)
        if u is None: continue
        ud = SQ.sub('', u)
        if not body.strip(): faults.append(f'{h}: empty')
        if body.count('⟦') != body.count('⟧'): faults.append(f'{h}: unbalanced ⟦ ⟧')
        quotes = re.findall(r'⟦(.*?)⟧', body, flags=re.S)
        for q in quotes:
            if SQ.sub('', q).replace('-', '') not in ud.replace('-', ''):
                faults.append(f'{h}: ⟦{q[:50]}⟧ is not in this unit letter for letter')
            if bc.PROSE.search(q):
                faults.append(f'{h}: ⟦{q[:60]}⟧ takes in Sāyaṇa\'s connecting words: cite only the word or rule')
        outside = re.sub(r'⟦.*?⟧', '', body, flags=re.S)
        mm = bc.DEVA.search(outside)
        if mm: faults.append(f'{h}: Devanagari outside ⟦ ⟧ near "{outside[max(0, mm.start() - 25):mm.start() + 15].strip()}"')
        refs = re.sub(r'[.–—]', '-', ud)
        for r in bc.REF.findall(re.sub(r'\*\*NOTE\*\*\{[^{}]*\}', '', outside)):
            if re.sub(r'[.–]', '-', r).translate(bc.TO_DEVA) not in refs:
                faults.append(f'{h}: the reference {r} is not in this unit')
        for g in bc.roman_gloss(outside):
            faults.append(f'{h}: Sanskrit in Roman letters inside brackets {g}')
        words += len(outside.split())
    print(f'{m}.{s}: {len(us)} units, {sum(len(r[2].split()) for r in us)} Sanskrit words → {words} English words')
    if faults:
        print('FAULTS:'); [print('  - ' + f) for f in faults]; return 1
    print('VERIFIED (form only: units complete and in order, citations copied from the unit, no typed Sanskrit in brackets)')
    return 0


def volume_pages(vol):
    """{(sūkta, ṛk): printed page where the volume's heading 'Ṛk n' stands}, and {sūkta: first page}."""
    c = json.loads((ROOT / f'vol{vol}' / 'volcfg.json').read_text(encoding='utf-8'))
    page, s, pg, spg = None, None, {}, {}
    for l in (ROOT / c['out']['en']).read_text(encoding='utf-8').split('\n'):
        mm = re.match(r'### Printed p\. (\S+)', l)
        if mm: page = mm.group(1); continue
        mm = re.match(r'## Sūkta (\d+) ', l)
        if mm: s = int(mm.group(1)); spg[s] = page; continue
        mm = re.match(r'#### Ṛk (\d+)\s*$', l)
        if mm and s: pg[(s, int(mm.group(1)))] = page
    return pg, spg


def cmd_build(vol):
    c = json.loads((ROOT / f'vol{vol}' / 'volcfg.json').read_text(encoding='utf-8'))
    m = c['mandalas'][0]
    ss = sorted(int(p.stem.split('_S')[1]) for p in WS.glob(f'M{m:02d}_S*.json') if volume_for(m, int(p.stem.split('_S')[1])) == vol)
    pg, spg = volume_pages(vol)
    out, notes, moved_all, cover = [], [], [], []
    body = []
    for s in ss:
        us, moved, d = units(m, s)
        moved_all += moved
        _, ep = paths(m, s, vol)
        en = dict(read_en(ep)[1]) if ep.exists() else {}
        have = sum(1 for r in us if f'SBh {r[0]}' in en and en[f'SBh {r[0]}'].strip())
        cover.append((s, len(d['rks']), len(us), have, d['revision']))
        body += [f'', f'## Sūkta {m}.{s}', '',
                 f'*Volume {vol}: Sūkta {s} begins at printed p. {spg.get(s, "?")}. Text of sa.wikisource.org, revision {d["revision"]}.*', '']
        byn = {}
        for r in us: byn.setdefault(r[1], []).append(r)
        rks = {r['n']: r for r in d['rks']}
        for n in sorted(byn):
            title = 'Sāyaṇa\'s introduction' if n == 0 else f'Ṛk {n}'
            where = '' if n == 0 else f' — Volume {vol}, printed p. {pg.get((s, n), "?")}'
            body += [f'<a id="SBh-{m}.{s}.{n}"></a>', f'### SBh {m}.{s}.{n} · {title}{where}', '']
            if n:
                r = rks[n]
                body += ['**Saṃhitā**', '', '> ' + '  \n> '.join(r['samhita'].split('\n')), '',
                         '> *' + '*  \n> *'.join(deva_to_iast(x) for x in r['samhita'].split('\n')) + '*', '',
                         '**Pada**', '', '> ' + '  \n> '.join(r['pada'].split('\n')), '',
                         '> *' + '*  \n> *'.join(deva_to_iast(x) for x in r['pada'].split('\n')) + '*', '']
            for ref, _, u in byn[n]:
                h = f'SBh {ref}'
                e = en.get(h, '').strip()
                body += [f'<a id="SBh-{ref}"></a>', f'**{h}**', '', '> ' + u, '', f'*{deva_to_iast(u)}*', '']
                body += [render(e, notes, ref), ''] if e else ['**[English not yet written]**', '']
    tot_units = sum(x[2] for x in cover); tot_have = sum(x[3] for x in cover)
    head = [f'# Sāyaṇa\'s Ṛgveda-bhāṣya, Volume {vol} (Maṇḍala {m}, Sūktas {ss[0]}–{ss[-1]}): Sanskrit, transliteration and English',
            '', '*Experiment: the Sanskrit is the text of sa.wikisource.org (revision numbers below), not the volume\'s machine-read text. '
            'Nothing in it has been compared with the printed edition. The English is a direct translation of Sāyaṇa\'s Sanskrit, made unit by unit; '
            'it has not yet had a second reading by a person.*', '',
            '## How to cite', '',
            'Every unit has a number **SBh M.S.R.U**: Sāyaṇa-bhāṣya, maṇḍala M, sūkta S, Ṛk R (**0** = Sāyaṇa\'s introduction to the sūkta), '
            'unit U in Sāyaṇa\'s order. A Ṛk is **SBh M.S.R**; the volume\'s Ṛk headings can say "Sāyaṇa: SBh 1.137.2". Each unit is shown in Devanagari, '
            'in transliteration (made by script, accents not shown) and in English. The index gives, for every Ṛk, its units and the printed page of the volume where the Ṛk begins.', '',
            f'Coverage: {len(ss)} sūktas, {sum(x[1] for x in cover)} Ṛks, {tot_units} units; English written for {tot_have} of them.', '',
            '## Index', '', '| Sūkta | Ṛk | Units | Volume p. |', '|---|---|---|---|']
    for s in ss:
        us, _, d = units(m, s)
        byn = {}
        for r in us: byn.setdefault(r[1], []).append(r[0])
        for n in sorted(byn):
            a, b = byn[n][0], byn[n][-1]
            head.append(f'| {m}.{s} | {"intro" if n == 0 else n} | [{a}](#SBh-{m}.{s}.{n}) – {b.rsplit(".", 1)[1]} | {"—" if n == 0 else pg.get((s, n), "?")} |')
    doc = ROOT / f'vol{vol}' / f'Rigveda_Samhita_Vol{vol}_Sayana_Bhashya.md'
    doc.write_text('\n'.join(head + body) + '\n', encoding='utf-8')
    rv = ROOT / f'vol{vol}' / 'review'; rv.mkdir(exist_ok=True)
    (rv / 'ws_structure.tsv').write_text('sūkta\tparagraph at end of Ṛk\tmoved to the front of Ṛk\tbeginning of the paragraph\n' +
                                         ''.join('\t'.join(map(str, x)) + '\n' for x in moved_all), encoding='utf-8')
    (rv / 'ws_notes.tsv').write_text('unit\tquestion\tbefore\n' + ''.join('\t'.join(x) + '\n' for x in notes), encoding='utf-8')
    print(f'{doc.relative_to(ROOT)}: {len(ss)} sūktas, {tot_units} units, English for {tot_have}; {len(notes)} NOTEs; {len(moved_all)} paragraphs moved to the next Ṛk')
    return 0


def main(a):
    if len(a) < 2: sys.exit(__doc__)
    if a[0] == 'build': return cmd_build(int(a[1]))
    m, s = int(a[1]), int(a[2])
    if a[0] == 'units':
        us, moved, _ = units(m, s)
        for r in us: print(f'SBh {r[0]}  ({len(r[2].split())} words)  {r[2][:110]}')
        print(f'{len(us)} units; moved: {moved}'); return 0
    if a[0] == 'task': return cmd_task(m, s)
    if a[0] == 'check': return check(m, s)
    sys.exit(__doc__)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
