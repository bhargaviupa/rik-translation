#!/usr/bin/env python3
"""Sāyaṇa-bhāṣya reader: a by-product book built from a volume's English file.

Keeps, per Ṛk: Saṃhitā-pāṭha, Pada-pāṭha (Devanagari + IAST as in the volume),
Sāyaṇa-bhāṣya, the English Gist of the bhāṣya and the Grammar section where the
volume has one. Per sūkta: Sāyaṇa's introduction with its Gist, and the
particulars (seer, deity, metre, counts).
Leaves out: Pratipadārtha, Bhāvārtha, the printed English translation, Special
Topics, the Anuvāda, printed-page markers.

Lines are selected, never rewritten (CLAUDE.md rule 2). The only change to the
text is whitespace: a paragraph that a printed-page marker cut in two is put
back together (counted in the report).

    python3 publish/bhashya_book.py 17 --sukta 40            # one sūkta
    python3 publish/bhashya_book.py 17 --sukta 3.40 --sukta 4.1   # Maṇḍala.Sūkta
    python3 publish/bhashya_book.py 17 --all [--out DIR] [--html]

A bare sūkta number that occurs in two Maṇḍalas of the volume is refused: give
Maṇḍala.Sūkta. Reads volumes in the labelled layout (`## Sūkta`, `#### Ṛk`,
`##### ॥ संहितापाठः ॥ …`); an older layout is refused with a message.
Writes DIR/Rigveda_Bhashya_Reader_VolN_<sel>.md (default DIR = publish/out) and
prints a report; exits 1 if the built-in check fails.
"""
import argparse, json, pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
KEPT = ('samhita', 'pada', 'bhashya', 'gist', 'grammar')
SUKTA = re.compile(r'^Sūkta\s+(\d+)(?:\s+\(Maṇḍala\s+(\d+)\))?\s*$')
RK = re.compile(r'^Ṛk\s+\d+')
CONT = re.compile(r'\((continued|continuing)\b', re.I)
ANUVADA = re.compile(r'^[\W_]*Anuvāda\b')
PART_START = re.compile(r'^(Om\.?\s*|॥\s*ओं\s*॥\s*)?(Sūkta|Hymn|Maṇḍala|सूक्त|मंडल)')
KN_ANUV = re.compile(r'^>\s*अनुवादवु')              # Kannada Anuvāda copied into the Sanskrit block
KN_PART = re.compile(r'^>\s*(॥\s*ओं\s*॥|सूक्त\s*[—–-])')   # particulars copied into the Sanskrit block
END_PROSE = re.compile(r'[.?!:;)\]"”’*]\s*$')
END_QUOTE = re.compile(r'([।॥‖|*]|\s\s)$')


def kind(heading):
    if 'Saṃhitā-pāṭha' in heading: return 'samhita'
    if 'Pada-pāṭha' in heading: return 'pada'
    if 'Sāyaṇa-bhāṣya' in heading: return 'bhashya'
    if heading.startswith('Gist of the bhāṣya'): return 'gist'
    if heading.strip() == 'Grammar': return 'grammar'
    if heading.strip() == 'Particulars': return 'particulars'
    return 'other'   # Pratipadārtha, Bhāvārtha, printed English, Special Topics, Anuvāda


def is_particulars(par):
    whole = ' '.join(re.sub(r'^[>\-*\s]+', '', l) for l in par)
    return bool(PART_START.match(whole)) and ('Aṣṭaka' in whole or 'अष्टक' in whole)


def sukta_list(lines):
    """[(maṇḍala or None, sūkta, line index)] for every sūkta heading."""
    out, mand = [], None
    for i, ln in enumerate(lines):
        if not ln.startswith('## '): continue
        h = ln[3:].strip()
        m = re.match(r'^Maṇḍala\s+(\d+)\s*$', h)
        if m: mand = int(m.group(1)); continue
        m = SUKTA.match(h)
        if m:
            if m.group(2): mand = int(m.group(2))
            out.append((mand, int(m.group(1)), i))
    return out


def select(lines, chosen):
    """chosen: set of sūkta-heading line indexes. Returns (output lines, report)."""
    out, rep = [], {k: 0 for k in KEPT}
    rep.update(suktas=0, rks=0, joins=0, no_particulars=[], dropped_particulars=0, part_en=0, part_dev=0, anuvada_lines=0)
    st = dict(on=False, sec=None, rk=False, par=[], page=False, last=None, name='', cut='b', en=[], dev=[], done=True)

    def particulars():
        """Once per sūkta, before its first Ṛk: the English particulars, else the Devanagari ones."""
        if not st['on'] or st['done']: return
        st['done'] = True
        pars = st['en'] or st['dev']
        if not pars: rep['no_particulars'].append(st['name']); return
        rep['part_en' if st['en'] else 'part_dev'] += 1
        heading('#### Particulars')
        for par in pars: out.extend(par); out.append('')

    def heading(text):
        out.extend([text, '']); st['last'] = None

    def emit(par):
        quote = par[0].startswith('>')
        last = st['last']
        if (st['page'] and last and last[0] == quote and last[2] == st['sec']
                and not (END_QUOTE if quote else END_PROSE).search(last[1])):
            out.pop(); rep['joins'] += 1          # drop the blank line: one paragraph again
        out.extend(par); out.append('')
        st['last'] = (quote, par[-1], st['sec'])

    def flush():
        par, st['par'] = st['par'], []
        if not par: return
        sec = st['sec']
        if not st['rk'] and sec not in ('samhita', 'pada', 'bhashya', 'grammar'):
            if is_particulars(par):
                st['dev' if par[0].startswith('>') else 'en'].append(par)
                if sec != 'particulars': st['sec'] = 'other'
                st['page'] = False; return
            if sec == 'particulars': rep['dropped_particulars'] += 1
            if sec == 'gist':                      # the Anuvāda follows the Gist, sometimes without a blank line
                cut = next((k for k, l in enumerate(par) if ANUVADA.match(l)), None)
                if cut is not None:
                    if cut: emit(par[:cut])
                    st['sec'] = 'other'; st['page'] = False; return
        if not st['rk'] and sec in ('bhashya', 'gist') and par[0].startswith('>'):
            keep, part = [], []
            for l in par:
                if KN_ANUV.match(l): st['cut'] = 'a'
                elif KN_PART.match(l): st['cut'] = 'p'
                if st['cut'] == 'b': keep.append(l)
                elif st['cut'] == 'p': part.append(l)
                else: rep['anuvada_lines'] += 1
            if part: st['dev'].append(part)
            par = keep
            if not par: st['page'] = False; return
        if sec == 'grammar' and not par[0].startswith('- '): st['sec'] = sec = 'other'
        if sec in KEPT: emit(par)
        st['page'] = False

    for i, ln in enumerate(lines):
        m = re.match(r'^(#{1,6}) (.*)', ln)
        if m:
            flush()
            lvl, head = len(m.group(1)), m.group(2).strip()
            if lvl <= 2:
                particulars()
                st.update(on=i in chosen, sec=None, rk=False, last=None, page=False, name=head, cut='b', en=[], dev=[], done=False)
                if st['on']: rep['suktas'] += 1; heading(f'## {head}')
                continue
            if not st['on']: continue
            if lvl == 3 and head.startswith('Printed p.'):
                st['page'] = True; continue           # marker dropped, section continues
            if lvl == 4:
                if RK.match(head) and not CONT.search(head):
                    particulars(); st['rk'] = True; rep['rks'] += 1; heading(f'### {head}')
                st['sec'] = None; st['last'] = None; continue
            if lvl == 5:
                st['sec'] = kind(head); st['cut'] = 'b'
                if st['sec'] in KEPT: rep[st['sec']] += 1; heading(f'#### {head}')
                continue
            st['sec'] = None; continue
        if not st['on']: continue
        if ln.strip() == '': flush()
        else: st['par'].append(ln)
    flush(); particulars()
    return out, rep


def check(lines, chosen, slist, out, rep):
    """Independent of select(): every text line is in the source unchanged, and the
    Ṛk count equals the source's count of (non-continuation) Ṛk headings."""
    src = set(lines)
    bad = [l for l in out if l.strip() and not l.startswith('#') and l not in src]
    starts = sorted(i for _, _, i in slist)
    want = 0
    for s in chosen:
        nxt = [i for i in range(s + 1, len(lines)) if re.match(r'^#{1,2} ', lines[i])]
        end = nxt[0] if nxt else len(lines)
        want += sum(1 for l in lines[s:end] if re.match(r'^#### Ṛk\s+\d+', l) and not CONT.search(l))
    errs = []
    if bad: errs.append(f'{len(bad)} line(s) not in the source unchanged, e.g. {bad[0][:60]!r}')
    if want != rep['rks']: errs.append(f'Ṛk count {rep["rks"]} but the source has {want}')
    for k in ('samhita', 'pada'):
        if rep[k] != rep['rks']: errs.append(f'{k} sections {rep[k]} ≠ Ṛks {rep["rks"]}')
    return errs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('vol', type=int)
    ap.add_argument('--sukta', action='append', default=[], help='N or Maṇḍala.N; repeatable')
    ap.add_argument('--all', action='store_true')
    ap.add_argument('--out', default=str(ROOT / 'publish' / 'out'))
    ap.add_argument('--html', action='store_true')
    a = ap.parse_args()
    if not a.sukta and not a.all: ap.error('give --sukta or --all')
    cfgf = ROOT / f'vol{a.vol}' / 'volcfg.json'
    src = (ROOT / json.loads(cfgf.read_text(encoding='utf-8'))['out']['en'] if cfgf.exists()
           else ROOT / f'vol{a.vol}' / f'Rigveda_Samhita_Vol{a.vol}_English_Translation.md')
    if not src.exists(): sys.exit(f'no English file for Vol {a.vol}: {src}')
    lines = src.read_text(encoding='utf-8').splitlines()
    slist = sukta_list(lines)
    if not slist or not any(l.startswith('##### ') and 'Saṃhitā-pāṭha' in l for l in lines):
        sys.exit(f'Vol {a.vol} is not in the labelled layout this builder reads '
                 '(needs "## Sūkta N", "#### Ṛk N", "##### ॥ संहितापाठः ॥ (Saṃhitā-pāṭha)").')
    if a.all:
        chosen, sel, what = {i for _, _, i in slist}, 'all', 'complete'
    else:
        chosen = set()
        for s in a.sukta:
            mm = re.match(r'^(?:(\d+)\.)?(\d+)$', s)
            if not mm: sys.exit(f'--sukta {s}: write N or Maṇḍala.N')
            hits = [(m, n, i) for m, n, i in slist if n == int(mm.group(2)) and (not mm.group(1) or m == int(mm.group(1)))]
            if not hits: sys.exit(f'--sukta {s}: not in Vol {a.vol}')
            if len(hits) > 1:
                sys.exit(f'--sukta {s}: occurs {len(hits)} times in Vol {a.vol} '
                         f'({", ".join(f"{m}.{n}" for m, n, _ in hits)}); give Maṇḍala.Sūkta')
            chosen.add(hits[0][2])
        sel = 'S' + '-'.join(s.replace('.', '_') for s in a.sukta)
        what = 'Sūkta ' + ', '.join(a.sukta)
    body, rep = select(lines, chosen)
    errs = check(lines, chosen, slist, body, rep)
    title = f"Sāyaṇa's Ṛgveda-bhāṣya in English: reader (Vol {a.vol}, {what})"
    md = f'# {title}\n\n' + '\n'.join(body).strip() + '\n'
    out = pathlib.Path(a.out); out.mkdir(parents=True, exist_ok=True)
    f = out / f'Rigveda_Bhashya_Reader_Vol{a.vol}_{sel}.md'
    f.write_text(md, encoding='utf-8')
    print(f'wrote {f}')
    print(f'  sūktas {rep["suktas"]}; Ṛks {rep["rks"]}; sections: Saṃhitā {rep["samhita"]}, Pada {rep["pada"]}, '
          f'bhāṣya {rep["bhashya"]}, Gist {rep["gist"]}, Grammar {rep["grammar"]}')
    print(f'  particulars kept for {rep["part_en"] + rep["part_dev"]} of {rep["suktas"]} sūktas '
          f'({rep["part_en"]} in English, {rep["part_dev"]} only in Devanagari); '
          f'Kannada Anuvāda lines taken out of bhāṣya blocks {rep["anuvada_lines"]}')
    print(f'  paragraphs rejoined across a page break {rep["joins"]}; **NOTE** markers {md.count("**NOTE**")}')
    if rep['no_particulars']: print('  no particulars found: ' + '; '.join(rep['no_particulars']))
    if rep['dropped_particulars']:
        print(f'  paragraphs under a Particulars heading left out (not particulars): {rep["dropped_particulars"]}')
    if a.html:
        h = f.with_suffix('.html')
        css = out / 'bhashya_reader.css'
        css.write_text('body{max-width:46em;margin:2em auto;padding:0 1em;font:17px/1.6 "Noto Serif Devanagari","Noto Serif",serif}'
                       'blockquote{border-left:3px solid #bbb;margin:.6em 0;padding-left:1em}'
                       'h4{font-size:.85em;letter-spacing:.04em;color:#666;margin:1em 0 .2em}'
                       'h3{border-top:1px solid #ccc;padding-top:.6em}\n', encoding='utf-8')
        subprocess.run(['pandoc', str(f), '-s', '--metadata', f'title={title}', '-c', css.name, '-o', str(h)], check=True)
        print(f'wrote {h}')
    if errs:
        print('CHECK FAILED: ' + ' | '.join(errs)); return 1
    print('  check passed: every text line is in the source unchanged; Ṛk count matches the source')
    return 0


if __name__ == '__main__':
    sys.exit(main())
