"""`rv print N [--pdf]`: the working copy and the review copy, printed from the units (docs/DESIGN.md §6).

Everything about how the book looks is decided here and nowhere else: names of the parts, transliteration under every Sanskrit block (made now,
not stored), the verse from the reference text with every akṣara set apart, no page marks in the body, the original's page in the footer.
Phase A: front matter is a skeleton (requirement A2 order, placeholders); review copy only — the release gate is not built yet."""
import os, re, sys, html, subprocess, collections
from .common import *
sys.path.insert(0, os.path.join(ROOT, 'publish'))

NAMES = {'samhita': 'Saṃhitā-pāṭha', 'pada': 'Pada-pāṭha', 'bhashya': "Sāyaṇa-bhāṣya — Sāyaṇa's Explanation", 'summary': 'Summary', 'pratipada': 'Word-to-word meaning',
         'bhavartha': 'Gist', 'english': 'English translation', 'vishesha': 'Viśeṣa-viṣaya', 'grammar': 'Grammar (Vyākaraṇa-prakriyā)', 'loose': ''}
INTRO_LABELS = {'bhashya': "Sāyaṇa's introduction to the sūkta"}
NOTE_RX = re.compile(r'\s*⟨NOTE:(\d+)⟩')

def iast_lines(deva_lines): return ['*' + deva_to_iast(strip_ac(x)).strip() + '*' for x in deva_lines]

def quote(lines, two_space=True): return ['> ' + x + ('  ' if two_space and i < len(lines) - 1 else '') for i, x in enumerate(lines)]

def sanskrit_block(deva_lines):
    """a Sanskrit block and its transliteration, as Markdown"""
    return quote(deva_lines) + [''] + quote(iast_lines(deva_lines)) + ['']

def mark_samhita(body):
    """after pandoc: the verse block gets its class and every akṣara its own span (the look piloted in Vol 17)"""
    C = '\u0915-\u0939\u0958-\u095F\u0978-\u097F'; START = re.compile('[' + C + '\u0904-\u0914\u0960\u0961\u093D\u0966-\u096F]')
    def aksharas(w):
        """a word cut into akṣaras: a new one begins at a consonant that does not follow a virāma, or at an independent vowel; a final
        consonant with virāma (as in नाम्) stays with the akṣara before it"""
        out = []
        for i, ch in enumerate(w):
            if START.match(ch) and not (i and w[i - 1] == '\u094D') or not out: out.append(ch)
            else: out[-1] += ch
        if len(out) > 1 and re.fullmatch('(?:[' + C + ']\u093C?\u094D)+[\u0951\u0952\u1CD0-\u1CFF]*', out[-1]): last = out.pop(); out[-1] += last
        return out
    def syl(t): return ' '.join(''.join(f'<span class="ak">{a}</span>' for a in aksharas(w)) for w in t.split(' ') if w)
    def rep(m):
        parts = re.split(r'(<[^>]+>)', m.group(2))
        return m.group(1) + '<blockquote class="samhita">' + ''.join(p if p.startswith('<') or not DEVA.search(p) else '\n'.join(syl(x) for x in p.split('\n')) for p in parts) + '</blockquote>'
    return re.sub(r'(<h5[^>]*>Saṃhitā-pāṭha(?:<span[^>]*></span>)*</h5>\s*)<blockquote>(.*?)</blockquote>', rep, body, flags=re.S)

def render(vol, units, review=True, for_html=False):
    out = []; st = collections.Counter(); cur_m = cur_s = cur_rk = None
    def notes(t):
        if review: return NOTE_RX.sub(lambda mm: f'<sup class="q">?{mm.group(1)}</sup>', t)
        return NOTE_RX.sub('', t)
    def anchors(u):                                                           # the original's pages that begin in this unit: carried by the unit's heading (footer)
        return ''.join(f'<span class="kp" data-p="{it[1]}"></span>' for it in u.get('kn', []) if it[0] == 'page') if for_html else ''
    for u in units:
        kind = u['kind']
        if kind == 'preface':
            out += ['<section class="placeholder-page">', '', '## Preface to the English edition', '', '*[To be written by the translator-editor.]*', '', '</section>', '', '## Preface of the original edition' + anchors(u), '']
            out += body_items(u, units, notes, st); continue
        if u['m'] != cur_m and u['s'] is not None:
            cur_m = u['m']; out += [f'# Maṇḍala {cur_m}', '']
        if kind == 'intro':
            cur_s = u['s']; cur_rk = None; out += [f'## Sūkta {cur_s} (Maṇḍala {cur_m})' + anchors(u), '']; st['sūktas'] += 1
            out += body_items(u, units, notes, st); continue
        if u['rk'] != cur_rk or u['s'] != cur_s:
            cur_s, cur_rk = u['s'], u['rk']; out += [f'#### Ṛk {cur_rk}', '']; st['Ṛks'] += 1
        if NAMES.get(kind): out += [('###### ' if kind == 'summary' else '##### ') + NAMES[kind] + anchors(u), '']
        elif anchors(u): out += [anchors(u), '']
        if kind == 'samhita':
            ref = u.get('ref')
            if ref:
                lines = [re.sub(r'\s*।\s*$', ' ।', x) for x in ref]; lines[-1] = lines[-1].rstrip('।॥ ') + ' ॥ ' + str(u['rk']).translate(DD) + ' ॥'; st['verses printed from the reference'] += 1
            else:
                lines = [kn2deva(x) for it in u['kn'] if it[0] == 'block' for x in it[1]]; st['verses printed from the supplied text (no reference verse)'] += 1
            out += quote(lines) + [''] + quote(iast_lines(lines)) + ['']
            for r_, e_, state in (u.get('diffs') or []):
                if state == 'supported' and e_:
                    out += [f'<p class="ednote">Kannada edition: {e_} ({deva_to_iast(strip_ac(e_)).strip()})' + (f' for {r_}' if r_ else '') + (' <span class="q">— proposed by script, to confirm</span>' if review else '') + '</p>', '']; st['edition readings shown under the verse'] += 1
        elif kind in ('pada', 'bhashya'):
            for it in u['kn']:
                if it[0] == 'block': out += sanskrit_block([kn2deva(x) for x in it[1]]); st['Sanskrit blocks printed from the source'] += 1
        elif kind == 'english':
            para = []
            for it in u['kn'] + [['break']]:
                if it[0] == 'text': para.append(it[1].strip())
                elif it[0] == 'break' and para: out += [' '.join(para), '']; para = []
        else: out += body_items(u, units, notes, st)
    return '\n'.join(out), st

def body_items(u, units, notes, st):
    """the English of a prose unit, in its order; a Sanskrit block inside it is printed from the source when the unit has as many blocks there"""
    out = []; kb = [it[1] for it in u.get('kn', []) if it[0] == 'block']; eb = [it for it in u.get('en', []) if it[0] == 'block']; same = len(kb) == len(eb); i = 0; lst = False
    for it in u.get('en', []):
        if it[0] == 'text':
            t = notes(it[1]); islist = t.startswith('- ')
            if lst and not islist: out.append('')
            out.append(t)
            if not islist: out.append('')
            lst = islist
        elif it[0] == 'block':
            if lst: out.append(''); lst = False
            if same: out += sanskrit_block([kn2deva(x) for x in kb[i]]); st['Sanskrit blocks printed from the source'] += 1
            else: out += sanskrit_block(it[1]); st['Sanskrit blocks printed from the English file (count differs from the source)'] += 1
            i += 1
        elif it[0] == 'label':
            if lst: out.append(''); lst = False
            name = next((INTRO_LABELS[v] for k, v in (('सायणभाष्यम्', 'bhashya'),) if k in it[1]), re.sub(r'^॥\s*|\s*॥.*$', '', it[1]))
            out += ['##### ' + name, '']
    if lst: out.append('')
    return out

CSS = """
span.kp { string-set: kp attr(data-p); }
h1 { string-set: volhead content(); page-break-before: always; text-align: center; }
h2 { string-set: sukhead content(text); page-break-before: always; }
h5 { font-size: 10pt; margin: 1.1em 0 .35em; letter-spacing: .02em; page-break-after: avoid; }
h6 { font-size: 9.5pt; font-style: italic; font-weight: normal; margin: .8em 0 .3em; page-break-after: avoid; }
p.ednote { font-size: 8.5pt; margin: -.2em 0 .6em 1em; color: #333; }
sup.q, span.q { color: #a00; font-size: 7.5pt; }
section.placeholder-page { page-break-before: always; page-break-after: always; }
section.title { text-align: center; padding-top: 2in; page-break-after: always; }
section.fm { page-break-after: always; } section.fm li { margin: .25em 0; }
@page { @bottom-center { content: "Kannada edition p. " string(kp, first) "  ·  REVIEW COPY"; font: 8pt "Noto Serif"; color: #555; } }
"""

def run(vol, pdf=False):
    P = vol_paths(vol); units = load_units(vol); os.makedirs(P['review'], exist_ok=True)
    md, st = render(vol, units, review=True, for_html=False)
    wp = os.path.join(P['review'], f'Vol{vol}_working_copy_English.md')
    open(wp, 'w', encoding='utf8').write(f'# Ṛgveda-saṃhitā, Volume {vol} — working copy printed from the units (rv print)\n\n*Not edited by hand: change the units and print again. `?N` marks question N for the editor.*\n\n' + md + '\n')
    print(f'working copy: {os.path.relpath(wp, ROOT)}  ({len(md.splitlines())} lines)'); print(' ', dict(st))
    if not pdf: return
    mdh, _ = render(vol, units, review=True, for_html=True)
    body = subprocess.run(['pandoc', '-f', 'markdown-yaml_metadata_block-smart+pipe_tables', '-t', 'html5', '--wrap=none'], input=mdh, capture_output=True, text=True, check=True).stdout
    body = mark_samhita(body)
    sk = [(u['m'], u['s']) for u in units if u['kind'] == 'intro']
    front = f'''<section class="title"><div class="dev">॥ श्री महागणाधिपतये नमः ॥</div><h1 style="string-set:none;page-break-before:auto">Ṛgveda-saṃhitā</h1>
<p><i>with the Bhāṣya of Sāyaṇācārya and the Kannada Commentary of H. P. Venkata Rao</i></p><p style="letter-spacing:.1em;margin-top:.6in">VOLUME {vol}</p>
<p>Maṇḍala {sk[0][0]} · Sūkta {sk[0][1]} to Maṇḍala {sk[-1][0]} · Sūkta {sk[-1][1]}</p><p style="margin-top:1in;color:#a00">REVIEW COPY — printed from the units, Phase A</p></section>
<section class="fm"><h2 style="page-break-before:auto">Front matter (requirement A2) — to be supplied</h2><ol><li>Cover with this volume's number in Kannada</li><li>Portrait of the king (Vol 1)</li><li>Portrait of the guru, with the English of its text (Vol 1)</li><li>List of scholars</li><li>Present king and present guru</li><li>Translation credentials</li><li>Copyright; thanks</li><li>Contents</li></ol></section>
<section class="fm"><h2>Sūktas in this volume</h2><ul>''' + ''.join(f'<li>Maṇḍala {m} · Sūkta {s}</li>' for m, s in sk) + '</ul></section>'
    doc = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Ṛgveda-saṃhitā, Volume %d (review copy)</title><link rel="stylesheet" href="../../publish/style.css">'
           '<link rel="stylesheet" href="../../publish/style_vol1.css"><link rel="stylesheet" href="../../publish/style_volbook.css"><style>%s</style></head><body>\n%s\n%s\n</body></html>') % (vol, CSS, front, body)
    hp = os.path.join(P['review'], f'Vol{vol}_review_copy_English.html'); open(hp, 'w', encoding='utf8').write(doc)
    from weasyprint import HTML
    pp = hp[:-5] + '.pdf'; HTML(string=doc, base_url=P['review'] + '/').write_pdf(pp); os.remove(hp)
    print(f'review copy: {os.path.relpath(pp, ROOT)}')
