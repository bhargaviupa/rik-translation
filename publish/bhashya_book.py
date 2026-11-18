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
    python3 publish/bhashya_book.py 17 --task 3.40    # task file for the translator of one sūkta
    python3 publish/bhashya_book.py 17 --notes        # the translators' questions → volN/review/bhashya_notes.tsv

The English of the bhāṣya (tools/rv/BHASHYA_BRIEF.md) lives in volN/bhashya_en/M<m>_S<sss>.md, one
file per sūkta. Where that file exists the book prints it in place of the Gist (`--gist` forces the
Gist): ⟦…⟧ becomes Devanagari + transliteration, **NOTE**{question} becomes **NOTE**.

A bare sūkta number that occurs in two Maṇḍalas of the volume is refused: give
Maṇḍala.Sūkta. Reads volumes in the labelled layout (`## Sūkta`, `#### Ṛk`,
`##### ॥ संहितापाठः ॥ …`); an older layout is refused with a message.
Writes DIR/Rigveda_Bhashya_Reader_VolN_<sel>.md (default DIR = publish/out) and
prints a report; exits 1 if the built-in check fails.
"""
import argparse, json, pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DEVA = re.compile('[\u0900-\u097F]')
NOTE = re.compile(r'\*\*NOTE\*\*\{([^{}]*)\}')
EN_HEAD = '#### English of the bhāṣya'


def en_path(vol, mand, sukta):
    return ROOT / f'vol{vol}' / 'bhashya_en' / f'M{mand or 0}_S{sukta:03d}.md'


def read_english(path):
    """{'Introduction' | 'Ṛk N': raw text} from one sūkta's English file."""
    parts = re.split(r'^## (.+)$', path.read_text(encoding='utf-8'), flags=re.M)
    return {parts[i].strip(): parts[i + 1].strip() for i in range(1, len(parts), 2)}


def render_english(raw, notes, where):
    """⟦X⟧ → X (*iast*); **NOTE**{q} → **NOTE**, the question going to `notes`."""
    sys.path.insert(0, str(ROOT / 'publish' / 'tools' / 'translit'))
    from add_iast import deva_to_iast
    def note(m):
        before = re.sub(r'[⟦⟧]', '', raw[max(0, m.start() - 60):m.start()]).replace('\n', ' ').strip()
        notes.append((*where, re.sub(r'[⟦⟧]', '', m.group(1)).strip(), before)); return '**NOTE**'
    text = NOTE.sub(note, raw)
    text = re.sub(r'(?<=\S)\*\*NOTE\*\*', ' **NOTE**', text)
    L = '[\u0900-\u0965\u0970-\u097F]'                                  # Devanagari letters and signs, not digits
    unhyphen = lambda q: re.sub(f'(?<={L})-\\s*(?={L})', '', q.strip())      # a line-end hyphen of the supplied text
    text = re.sub(r'⟦(.*?)⟧', lambda m: f'{unhyphen(m.group(1))} (*{deva_to_iast(unhyphen(m.group(1)))}*)', text, flags=re.S)
    return [l.rstrip() for l in text.splitlines()]
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


PDF_CSS = '''
@page { size: A4; margin: 20mm 19mm 20mm 19mm;
  @top-center { content: string(sukta); font: 8.5pt "Noto Serif", serif; color: #777; }
  @bottom-center { content: counter(page); font: 8.5pt "Noto Serif", serif; color: #777; } }
@page :first { @top-center { content: none; } }
html { font-family: "Noto Serif", "Lohit Devanagari", serif; font-size: 10.5pt; line-height: 1.55; color: #111; }
h1 { font-size: 16pt; line-height: 1.3; margin: 0 0 8mm; font-weight: 600; }
h2 { string-set: sukta content(); font-size: 14pt; margin: 8mm 0 3mm; padding-bottom: 1.5mm; border-bottom: 1.2pt solid #333; break-after: avoid; }
h3 { font-size: 12.5pt; margin: 9mm 0 2mm; padding-top: 2.5mm; border-top: .6pt solid #999; break-after: avoid; }
h4 { font-family: "Noto Serif", "Lohit Devanagari", serif; font-size: 8pt; font-weight: 600; letter-spacing: .06em; color: #666;
     margin: 4.5mm 0 1mm; break-after: avoid; }
h4.en { color: #7a3b00; }
blockquote { font-family: "Lohit Devanagari", "Noto Serif", serif; font-size: 12pt; line-height: 1.75; margin: 0 0 2mm;
     padding: 1.2mm 0 1.2mm 4mm; border-left: 2pt solid #c9c2b5; background: #faf8f3; text-align: left; }
blockquote p { margin: 0 0 1.5mm; }
blockquote em { font-family: "Noto Serif", serif; font-size: 9.5pt; color: #555; }
p { margin: 0 0 2.6mm; text-align: left; orphans: 2; widows: 2; }
p em { color: #555; font-size: 9.5pt; }
.note { font-weight: 700; font-size: 8pt; color: #fff; background: #b3261e; padding: 0 1.2mm; border-radius: 1mm; }
'''


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


def select(lines, chosen, english=None, lean=False):
    """chosen: set of sūkta-heading line indexes. english: {heading line index: (label, {unit: raw text})}
    for the sūktas whose Gist is replaced. lean: a translator's task (Devanagari of Saṃhitā, Pada and
    bhāṣya only). Returns (output lines, report)."""
    english = english or {}
    out, rep = [], {k: 0 for k in KEPT}
    rep.update(en_suktas=0, en_units=0, en_lines=set(), notes=[], remarks=0)
    rep.update(suktas=0, rks=0, joins=0, no_particulars=[], dropped_particulars=0, part_en=0, part_dev=0, anuvada_lines=0)
    st = dict(on=False, sec=None, rk=False, par=[], page=False, last=None, name='', cut='b', en=[], dev=[], done=True, unit=None, eng=None)

    def particulars():
        """Once per sūkta, before its first Ṛk: the English particulars, else the Devanagari ones."""
        if not st['on'] or st['done']: return
        st['done'] = True
        if lean: return
        pars = st['en'] or st['dev']
        if not pars: rep['no_particulars'].append(st['name']); return
        rep['part_en' if st['en'] else 'part_dev'] += 1
        heading('#### Particulars')
        for par in pars: out.extend(par); out.append('')

    def heading(text):
        out.extend([text, '']); st['last'] = None

    def close_unit():
        """The English of the unit that ends here (introduction or one Ṛk)."""
        if not st['on'] or not st['eng'] or st['unit'] is None: return
        raw = st['eng'][1].get(st['unit'])
        st['unit'] = None
        if not raw: return
        body = render_english(raw, rep['notes'], (st['eng'][0], st['unit_name']))
        heading(EN_HEAD); out.extend(body); out.append('')
        rep['en_units'] += 1; rep['en_lines'].update(body)

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
        if sec == 'bhashya' and not par[0].startswith('>') and '**NOTE**' not in par[0]:   # a remark of the volume's translator inside the block (its NOTE marks stay)
            rep['remarks'] += 1; st['page'] = False; return
        if (lean or st['eng']) and sec == 'gist' and not par[0].startswith('>'): sec = 'other'   # Gist prose not wanted
        if lean:
            par = [l for l in par if DEVA.search(l)]          # no transliteration lines
            if not par or sec == 'grammar': st['page'] = False; return
        if sec in KEPT: emit(par)
        st['page'] = False

    for i, ln in enumerate(lines):
        m = re.match(r'^(#{1,6}) (.*)', ln)
        if m:
            flush()
            lvl, head = len(m.group(1)), m.group(2).strip()
            if lvl <= 2:
                close_unit(); particulars()
                st.update(on=i in chosen, sec=None, rk=False, last=None, page=False, name=head, cut='b', en=[], dev=[], done=False,
                          unit='Introduction', unit_name='Introduction', eng=english.get(i))
                if st['on']:
                    rep['suktas'] += 1; heading(f'## {head}')
                    if st['eng']: rep['en_suktas'] += 1
                continue
            if not st['on']: continue
            if lvl == 3 and head.startswith('Printed p.'):
                st['page'] = True; continue           # marker dropped, section continues
            if lvl == 4:
                if RK.match(head) and not CONT.search(head):
                    close_unit(); particulars(); st['rk'] = True; rep['rks'] += 1; heading(f'### {head}')
                    st['unit'] = st['unit_name'] = re.match(r'^Ṛk\s+\d+', head).group(0)
                st['sec'] = None; st['last'] = None; continue
            if lvl == 5:
                st['sec'] = kind(head); st['cut'] = 'b'
                skip = (st['sec'] == 'gist' and (lean or st['eng'])) or (lean and st['sec'] == 'grammar')
                if st['sec'] in KEPT and not skip: rep[st['sec']] += 1; heading(f'#### {head}')
                continue
            st['sec'] = None; continue
        if not st['on']: continue
        if ln.strip() == '': flush()
        else: st['par'].append(ln)
    flush(); close_unit(); particulars()
    return out, rep


def check(lines, chosen, slist, out, rep):
    """Independent of select(): every text line is in the source unchanged, and the
    Ṛk count equals the source's count of (non-continuation) Ṛk headings."""
    src = set(lines)
    bad = [l for l in out if l.strip() and not l.startswith('#') and l not in src and l not in rep['en_lines']]
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
    ap.add_argument('--pdf', action='store_true', help='reading copy (needs weasyprint and the fonts of HANDBOOK §8)')
    ap.add_argument('--task', metavar='M.S', help='write the translator task file for one sūkta')
    ap.add_argument('--notes', action='store_true', help='write volN/review/bhashya_notes.tsv from all English files')
    ap.add_argument('--gist', action='store_true', help='print the Gist even where an English file exists')
    a = ap.parse_args()
    if a.task: a.sukta, a.all = [a.task], False
    if a.notes: a.all = True
    if not a.sukta and not a.all: ap.error('give --sukta, --all, --task or --notes')
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
    if a.task:
        m, n, i = next(x for x in slist if x[2] in chosen)
        body, rep = select(lines, chosen, lean=True)
        errs = check(lines, chosen, slist, body, rep)
        if errs: print('CHECK FAILED: ' + ' | '.join(errs)); return 1
        t = ROOT / f'vol{a.vol}' / 'work' / 'bhashya' / f'M{m or 0}_S{n:03d}.task.md'
        t.parent.mkdir(parents=True, exist_ok=True)
        t.write_text('\n'.join(body).strip() + '\n', encoding='utf-8')
        print(f'task: {t.relative_to(ROOT)}  ({rep["rks"]} Ṛks)')
        print(f'write your English to: {en_path(a.vol, m, n).relative_to(ROOT)}')
        return 0
    english = {}
    if not a.gist:
        for m, n, i in slist:
            ep = en_path(a.vol, m, n)
            if i in chosen and ep.exists(): english[i] = (f'{m or 0}.{n}', read_english(ep))
    body, rep = select(lines, chosen, english=english)
    errs = check(lines, chosen, slist, body, rep)
    if a.notes:
        nf = ROOT / f'vol{a.vol}' / 'review' / 'bhashya_notes.tsv'
        rows = ['sūkta\tunit\tquestion\twords before the mark\tdecision'] + ['\t'.join((*r, '')) for r in rep['notes']]
        nf.write_text('\n'.join(rows) + '\n', encoding='utf-8')
        print(f'wrote {nf.relative_to(ROOT)}: {len(rep["notes"])} questions from {rep["en_suktas"]} sūkta file(s)')
        rd = ['sūkta\tunit\tsupplied text\treading translated\tbasis']
        for i in sorted(english):
            lab, units = english[i]
            for ln in units.get('Readings', '').splitlines():
                m = re.match(r'^- (Introduction|Ṛk \d+): ⟦([^⟧]+)⟧ → (.+?) — (.+)$', ln.strip())
                if m: rd.append('\t'.join((lab, m.group(1), m.group(2), re.sub(r'[⟦⟧]', '', m.group(3)), m.group(4))))
        rf = nf.with_name('bhashya_readings.tsv')
        rf.write_text('\n'.join(rd) + '\n', encoding='utf-8')
        print(f'wrote {rf.relative_to(ROOT)}: {len(rd) - 1} readings')
        return 1 if errs else 0
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
    print(f'  English of the bhāṣya in place of the Gist: {rep["en_suktas"]} of {rep["suktas"]} sūktas, {rep["en_units"]} units')
    print(f'  paragraphs rejoined across a page break {rep["joins"]}; **NOTE** markers {md.count("**NOTE**")}')
    if rep['remarks']: print(f'  remarks of the volume inside bhāṣya blocks left out: {rep["remarks"]}')
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
    if a.pdf:
        import html as _h
        from weasyprint import HTML
        frag = subprocess.run(['pandoc', '-f', 'markdown', '-t', 'html'], input=md, capture_output=True, text=True, check=True).stdout
        frag = frag.replace('<strong>NOTE</strong>', '<span class="note">NOTE</span>')
        frag = re.sub(r'<h4[^>]*>English of the bhāṣya</h4>', '<h4 class="en">English of the bhāṣya</h4>', frag)
        doc = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{_h.escape(title)}</title>'
               f'<style>{PDF_CSS}</style></head><body>{frag}</body></html>')
        pf = f.with_suffix('.pdf')
        HTML(string=doc).write_pdf(str(pf))
        print(f'wrote {pf}')
    if errs:
        print('CHECK FAILED: ' + ' | '.join(errs)); return 1
    print('  check passed: every text line is in the source unchanged; Ṛk count matches the source')
    return 0


if __name__ == '__main__':
    sys.exit(main())
