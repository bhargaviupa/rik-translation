"""`rv print N [--pdf]`: the working copy and the review copy, printed from the units (docs/DESIGN.md §6).

Everything about how the book looks is decided here and nowhere else: names of the parts, transliteration under every Sanskrit block (made now,
not stored), the verse from the reference text with every akṣara set apart, no page marks in the body, the original's page in the footer.
Phase A: front matter is a skeleton (requirement A2 order, placeholders); review copy only — the release gate is not built yet."""
import os, re, sys, html, subprocess, collections
from .common import *
sys.path.insert(0, os.path.join(ROOT, 'publish'))

NAMES = {'samhita': 'Saṃhitā-pāṭha', 'pada': 'Pada-pāṭha', 'bhashya': "Sāyaṇa-bhāṣya — Sāyaṇa's Explanation", 'summary': 'Summary', 'pratipada': 'Word-to-word meaning',
         'bhavartha': 'Gist', 'english': 'English translation', 'vishesha': 'Special Topics', 'grammar': 'Grammar (Vyākaraṇa-prakriyā)', 'loose': ''}
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
    # where the verse of the Kannada edition (as machine-read) differs from the reference verse that is printed: one footnote on the Ṛk
    # (user, Nov 13 2026: mention every difference, correct none for now; which are real readings of the edition is on the to-do list)
    def verse_note(u):
        d = [(r_, e_) for r_, e_, state in (u.get('diffs') or []) if (r_ or e_) and state != 'misread']      # a place the edition's own Pada-pāṭha or word meanings settle needs no footnote
        if not d: return ''
        parts = [(f'{e_} ({deva_to_iast(strip_ac(e_)).strip()})' if e_ else 'nothing') + (f' for {r_}' if r_ else ' (not in the reference)') for r_, e_ in d]
        return 'The verse is printed from the reference text. The Kannada edition, as machine-read, has: ' + '; '.join(parts) + '.'
    vnote = {(u['m'], u['s'], u['rk']): verse_note(u) for u in units if u['kind'] == 'samhita'}
    def notes(t):
        if review: return NOTE_RX.sub(lambda mm: f'<sup class="q">?{mm.group(1)}</sup>', t)
        return NOTE_RX.sub('', t)
    def anchors(u):                                                           # the original's pages that begin in this unit: carried by the unit's heading (footer)
        return ''.join(f'<span class="kp" id="kp{it[1]}" data-p="{it[1]}"></span>' for it in u.get('kn', []) if it[0] == 'page') if for_html else ''
    for u in units:
        kind = u['kind']
        if kind == 'preface':
            out += ['<section class="placeholder-page">', '', '## Preface to the English edition', '', '*[To be written by the translator-editor.]*', '', '</section>', '', '## Preface of the original edition' + anchors(u), '']
            out += body_items(u, units, notes, st); continue
        if u['m'] != cur_m and u['s'] is not None:
            cur_m = u['m']; out += [f'# Maṇḍala {cur_m}', '']
        if kind == 'intro':
            cur_s = u['s']; cur_rk = None; om = '<div class="om">ॐ</div>\n\n' if for_html and not st['sūktas'] else ''
            out += [om + f'## Sūkta {cur_s} (Maṇḍala {cur_m})' + (f'<span class="ks" data-s="{particulars(u)}"></span>' if for_html else '') + anchors(u), '']; st['sūktas'] += 1
            out += body_items(u, units, notes, st); continue
        if u['rk'] != cur_rk or u['s'] != cur_s:
            cur_s, cur_rk = u['s'], u['rk']; vn = vnote.get((u['m'], cur_s, cur_rk), '')
            if vn: st['Ṛks with a footnote on the verse'] += 1
            out += [f'#### Ṛk {cur_rk}' + (f'<span class="fn">{vn}</span>' if vn and for_html else ''), ''] + ([f'*Footnote: {vn}*', ''] if vn and not for_html else []); st['Ṛks'] += 1
        if NAMES.get(kind): out += [('###### ' if kind == 'summary' else '##### ') + NAMES[kind] + anchors(u), '']
        elif anchors(u): out += [anchors(u), '']
        if kind == 'samhita':
            ref = u.get('ref')
            if ref:
                lines = [re.sub(r'\s*।\s*$', ' ।', x) for x in ref]; lines[-1] = lines[-1].rstrip('।॥ ') + ' ॥ ' + str(u['rk']).translate(DD) + ' ॥'; st['verses printed from the reference'] += 1
            else:
                lines = [kn2deva(x) for it in u['kn'] if it[0] == 'block' for x in it[1]]; st['verses printed from the supplied text (no reference verse)'] += 1
            out += quote(lines) + [''] + quote(iast_lines(lines)) + ['']
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

def particulars(u):
    """Maṇḍala–Anuvāka–Sūkta and Aṣṭaka–Adhyāya–Varga of a sūkta, read from the particulars the edition prints at its head (for the footer)"""
    t = ' '.join(it[1] for it in u.get('kn', []) if it[0] == 'text'); g = {}
    for key, kn in (('Anu.', 'ಅನುವಾಕ'), ('Aṣṭ.', 'ಅಷ್ಟಕ'), ('Adhy.', 'ಅಧ್ಯಾಯ'), ('Va.', 'ವರ್ಗ')):
        mm = re.search(kn + r'\s*[—–-]\s*([೦-೯0-9]+(?:\s*,\s*[೦-೯0-9]+)*)', t)
        if mm: g[key] = re.sub(r'\s*,\s*', '–', mm.group(1).translate(KD))
    return ' · '.join([f"Maṃ. {u['m']}"] + ([f"Anu. {g['Anu.']}"] if 'Anu.' in g else []) + [f"Sū. {u['s']}"] + [f'{k} {g[k]}' for k in ('Aṣṭ.', 'Adhy.', 'Va.') if k in g])

def render_kn(vol, units):
    """the Kannada book: the text of the supplied file as the units hold it, with page anchors and sūkta and Ṛk headings; stray lines are not printed"""
    KL = {'samhita': 'ಸಂಹಿತಾಪಾಠಃ', 'pada': 'ಪದಪಾಠಃ', 'bhashya': 'ಸಾಯಣಭಾಷ್ಯಂ', 'pratipada': 'ಪ್ರತಿಪದಾರ್ಥ', 'bhavartha': 'ಭಾವಾರ್ಥ', 'english': 'English Translation.', 'vishesha': 'ವಿಶೇಷವಿಷಯಗಳು', 'grammar': 'ವ್ಯಾಕರಣಪ್ರಕ್ರಿಯಾ'}
    KD2 = str.maketrans('0123456789', '೦೧೨೩೪೫೬೭೮೯'); out = []; cur_s = cur_rk = cur_m = None; n = collections.Counter()
    def items(u):
        para = []
        def flush():
            if para: out.extend([' '.join(para), '']); para.clear()
        for it in u.get('kn', []):
            if it[0] == 'text': para.append(it[1].strip())
            elif it[0] == 'break': flush()
            elif it[0] == 'block': flush(); out.extend(quote(it[1]) + ['']); n['blocks'] += 1
            elif it[0] == 'label': flush(); out.extend(['##### ' + KL.get(it[1], it[1]), ''])
            elif it[0] == 'page': flush(); out.extend([f'<span class="kp" id="kp{it[1]}" data-p="{it[1]}"></span>', '']); n['pages'] += 1
            elif it[0] == 'stray': n['stray lines not printed'] += 1
        flush()
    for u in units:
        if not u.get('kn'): continue
        if u['kind'] == 'samhita' and u.get('kn_corrected'):                    # the verse corrected from the reference: printed in place of the supplied lines
            u = dict(u); done = False; kn2 = []
            for it in u['kn']:
                if it[0] == 'block':
                    if not done: kn2.append(['block', u['kn_corrected']]); done = True; n['verses printed with corrections from the reference'] += 1
                else: kn2.append(it)
            u['kn'] = kn2
        if u['kind'] == 'preface': out += ['## ಪೀಠಿಕೆ', '']; items(u); continue
        if u['s'] is not None and u['m'] != cur_m: cur_m = u['m']; out += [f"# ಮಂಡಲ {str(cur_m).translate(KD2)}", '']
        if u['kind'] == 'intro':
            cur_s, cur_rk = u['s'], None; out += [f"## ಸೂಕ್ತ {str(cur_s).translate(KD2)} (ಮಂಡಲ {str(cur_m).translate(KD2)})" + f'<span class="ks" data-s="{particulars(u)}"></span>', '']; items(u); continue
        if u['rk'] != cur_rk or u['s'] != cur_s: cur_s, cur_rk = u['s'], u['rk']; out += [f"#### ಋಕ್ {str(cur_rk).translate(KD2)}", '']
        if KL.get(u['kind']): out += ['##### ' + KL[u['kind']], '']
        items(u)
    return '\n'.join(out), n

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
h2 { string-set: sukhead content(text); page-break-before: always; counter-reset: footnote; }
h1 + h2, h1 + div.om, div.om + h2 { page-break-before: avoid; }      /* the first sūkta follows its Maṇḍala heading on the same page */
h5 { font-size: 10pt; margin: 1.1em 0 .35em; letter-spacing: .02em; page-break-after: avoid; }
h6 { font-size: 9.5pt; font-style: italic; font-weight: normal; margin: .8em 0 .3em; page-break-after: avoid; }
h4 span.fn { font-weight: normal; }
p.ednote { font-size: 8.5pt; margin: -.2em 0 .6em 1em; color: #333; }
sup.q, span.q { color: #a00; font-size: 7.5pt; }
section.placeholder-page { page-break-before: always; page-break-after: always; }
section.title { text-align: center; padding-top: 2in; page-break-after: always; }
section.fm { page-break-after: always; } section.fm li { margin: .25em 0; }
span.ks { string-set: ks attr(data-s); }
@page { @bottom-center { content: "Kannada edition p. " string(kp, first) "  ·  " string(ks, first) "  ·  REVIEW COPY"; font: 7.5pt "Noto Serif"; color: #555; } }
@page front { @bottom-center { content: none; } }
section.fm, section.title, section.cover, section.pic, section.placeholder-page { page: front; }
section.cover { page-break-after: always; text-align: center; } section.cover img { max-width: 100%; max-height: 7.2in; } section.cover p { font-size: 9.5pt; margin-top: .25in; }
section.pic { page-break-after: always; text-align: center; padding-top: .3in; } section.pic img { max-height: 5.2in; max-width: 80%; } section.pic h2 { margin-top: 0; } section.pic p { font-size: 9.5pt; }
section.cred .half { height: 3.4in; } section.cred .box { border: 0.5pt solid #999; height: 3.2in; display: flex; align-items: center; justify-content: center; color: #777; font-size: 9pt; }
.toc ul { list-style: none; padding: 0; } .toc li.sk { margin-top: .7em; font-weight: bold; } .toc li.ch { margin-top: 1em; text-align: center; font-style: italic; }
.toc a { color: inherit; text-decoration: none; } .toc a::after { content: leader(". ") target-counter(attr(href url), page); }
table.abbr { border-collapse: collapse; font-size: 9.5pt; width: 100%; } table.abbr td { padding: 2pt 6pt; vertical-align: top; border-bottom: 0.3pt solid #ccc; }
.om { text-align: center; font-size: 34pt; margin: .2in 0 .1in; }
body.kan p, body.kan blockquote, body.kan h1, body.kan h2, body.kan h4, body.kan h5 { font-family: "Noto Serif Kannada", "Lohit Kannada", "Noto Sans Kannada", serif; }
"""

def kn_inline(t): return re.sub(r'⟦([^⟧]*)⟧', lambda m: '<i>' + html.escape(deva_to_iast(kn2deva(m.group(1))).strip()) + '</i>', html.escape(t))

def front_matter(vol, units, have_pages):
    """the front matter in the order of requirement A2; what does not exist yet is a placeholder page that says so"""
    import json, csv
    P = vol_paths(vol); sk = [(u['m'], u['s']) for u in units if u['kind'] == 'intro']; ms = sorted({m for m, _ in sk})
    rng = ' and '.join(f"Maṇḍala {m} · Sūktas {min(s for mm, s in sk if mm == m)}–{max(s for mm, s in sk if mm == m)}" for m in ms)
    first = next(u for u in units if u['kind'] == 'intro'); pt = particulars(first); asht = re.search(r'Aṣṭ\. (\S+)', pt)
    rel = json.load(open(os.path.join(ROOT, 'publish', 'release.json'), encoding='utf8')); val = lambda k, d: rel.get(k) or d
    out = []
    cover = os.path.join(P['dir'], 'html', 'figures', 'fig1_line00004.jpg')
    out.append('<section class="cover">' + (f'<img src="../html/figures/fig1_line00004.jpg" alt="Cover">' if os.path.exists(cover) else '<div class="box">[Cover of this volume — to be supplied]</div>') +
               f'<p>Ṛgveda-saṃhitā · Volume {vol} · {rng}' + (f' · Aṣṭaka {asht.group(1)}' if asht else '') + '</p></section>')
    out.append('<section class="pic"><h2 style="page-break-before:auto;string-set:none">Patron of the First Edition</h2><img src="../../publish/assets/maharaja.jpg" alt="Maharaja of Mysore"><p>His Highness Śrī Jayacāmarājendra Wadiyar Bahadur, G.C.B., G.C.S.I., Maharaja of Mysore</p></section>')
    out.append('<section class="pic"><h2 style="page-break-before:auto;string-set:none">Guru and President of the Board of Scholars</h2><img src="../../publish/assets/guruji.jpg" alt="Guruji"><p>Śrī Jagadguru Nāgaliṅga-parivrājakācārya-pīṭhādhyakṣa<br>Śilpasiddhānti Śivayogi Śrī Siddhaliṅga Svāmigaḷavaru,<br>President of the Veda-vimarśana Vidvan-maṇḍali</p></section>')
    bp = os.path.join(P['data'], 'board_en.json')
    if os.path.exists(bp):
        b = json.load(open(bp, encoding='utf8')); e = html.escape
        out.append('<section class="fm"><h2 style="page-break-before:auto;string-set:none">' + '<br>'.join(e(x) for x in b.get('title_lines', [])) + '</h2>' +
                   f"<p><b>{e(b.get('editor_label', ''))}</b> {e(b.get('editor', ''))}</p>" + (f"<p><b>{e(b.get('associate_label', ''))}</b> {e(b.get('associate', ''))}</p>" if b.get('associate') else '') +
                   f"<h5>{e(b.get('list_title', ''))}</h5><ol>" + ''.join(f'<li>{e(x)}</li>' for x in b.get('members', [])) + '</ol></section>')
    else: out.append('<section class="fm"><h2 style="page-break-before:auto;string-set:none">Board of Scholars</h2><p><i>[To be supplied.]</i></p></section>')
    out.append('<section class="fm"><h2 style="page-break-before:auto;string-set:none">The Present Day</h2><div class="cred"><div class="half"><div class="box">[Portrait of the present Maharaja — to be supplied, with name and title]</div></div><div class="half"><div class="box">[Portrait of the present Guru — to be supplied, with name and title]</div></div></div></section>')
    out.append(f'<section class="fm cred"><div class="half"><div class="box">[Picture for the translation credentials — to be supplied]</div></div><div class="half" style="text-align:center"><h2 style="page-break-before:auto;string-set:none">Ṛgveda-saṃhitā</h2><p><i>with the Bhāṣya of Sāyaṇācārya and the Kannada Commentary of H. P. Venkata Rao</i></p><p>Volume {vol} · {rng}</p><p>English Translation by<br><span style="font-size:13pt;letter-spacing:.05em">Bhargavi Upadhya</span></p><p style="font-size:8.5pt">Based on the Kannada edition of Asthāna Mahāvidvān H. P. Venkata Rao, Mysore, 1952</p></div></section>')
    out.append('<section class="fm"><h2 style="page-break-before:auto;string-set:none">Copyright</h2><p>© 2026 Bhargavi Upadhya. ' + html.escape(val('rights_statement', 'All rights reserved.')) + '</p>' +
               f"<p>Publisher: {html.escape(val('publisher', '[to be supplied]'))}<br>ISBN: {html.escape(val('isbn', '[to be supplied]'))}<br>Edition: {html.escape(val('edition_and_printing', '[to be supplied]'))}</p>" +
               f"<p>The Kannada edition on which this translation is based: {html.escape(val('permissions_status_original', '[statement of rights — to be supplied]'))}<br>Portraits: {html.escape(val('permissions_status_portraits', '[statement of rights — to be supplied]'))}</p>" +
               '<h2 style="page-break-before:auto;string-set:none;margin-top:.5in">Thanks</h2><p><i>[To be written by the translator-editor.]</i></p></section>')
    cp = os.path.join(P['data'], 'contents_en.tsv')
    if os.path.exists(cp):
        items = []
        for r in csv.reader(open(cp, encoding='utf8'), delimiter='\t'):
            if len(r) < 3: continue
            kind, page, text = r[0].strip(), r[1].strip(), kn_inline(r[2].strip())
            if kind in ('chapter', 'range'): items.append(f'<li class="ch">{text}</li>')
            elif kind == 'sukta': items.append(f'<li class="sk">{text}</li>')
            elif page.isdigit() and int(page) in have_pages: items.append(f'<li><a href="#kp{page}">{text}</a></li>')
            else: items.append(f'<li>{text}' + (f' <span style="color:#777">(Kannada edition p. {page})</span>' if page else '') + '</li>')
        out.append('<section class="fm toc"><h2 style="page-break-before:auto;string-set:none">Contents</h2><p style="font-size:8.5pt"><i>Page numbers are the pages of this book.</i></p><ul>' + '\n'.join(items) + '</ul></section>')
    else:
        out.append('<section class="fm toc"><h2 style="page-break-before:auto;string-set:none">Contents</h2><p><i>[The printed contents of the volume, in English — being prepared.]</i></p><ul>' + ''.join(f'<li>Maṇḍala {m} · Sūkta {s_}</li>' for m, s_ in sk) + '</ul></section>')
    return '\n'.join(out)

def abbreviations_html():
    import csv
    rows = [r for r in csv.DictReader(open(os.path.join(ROOT, 'rv', 'references.tsv'), encoding='utf8'), delimiter='\t') if r['status'] == 'legend']
    return ('<section class="fm"><h2 style="string-set:none">Explanation of the Abbreviations</h2><table class="abbr">' +
            ''.join(f"<tr><td>{html.escape(kn2deva(r['kannada']))}</td><td>{html.escape(r['english'])}</td><td>{html.escape(r['work'])}</td></tr>" for r in rows) + '</table></section>')

def to_pdf(doc, path, base):
    from weasyprint import HTML
    HTML(string=doc, base_url=base + '/').write_pdf(path)

def run(vol, pdf=False, kan=False):
    P = vol_paths(vol); units = load_units(vol); os.makedirs(P['review'], exist_ok=True)
    pandoc = lambda t: subprocess.run(['pandoc', '-f', 'markdown-yaml_metadata_block-smart+pipe_tables', '-t', 'html5', '--wrap=none'], input=t, capture_output=True, text=True, check=True).stdout
    head = lambda title, extra='': ('<!doctype html><html><head><meta charset="utf-8"><title>%s</title><link rel="stylesheet" href="../../publish/style.css"><link rel="stylesheet" href="../../publish/style_vol1.css">'
                                    '<link rel="stylesheet" href="../../publish/style_volbook.css">%s<style>%s</style></head>') % (title, extra, CSS)
    if kan:
        mdk, n = render_kn(vol, units); print('Kannada book:', dict(n))
        doc = head(f'Ṛgveda-saṃhitā, Volume {vol} (Kannada text, review copy)', '<link rel="stylesheet" href="../../publish/style_volbook_kan.css">') + '<body class="kan">\n' + \
              f'<section class="title"><h1 style="string-set:none;page-break-before:auto">ಋಗ್ವೇದಸಂಹಿತಾ</h1><p>ಭಾಗ {vol}</p><p style="margin-top:1in;color:#a00">REVIEW COPY — Kannada text printed from the units</p></section>\n' + pandoc(mdk) + '\n</body></html>'
        pp = os.path.join(P['review'], f'Vol{vol}_review_copy_Kannada.pdf'); to_pdf(doc, pp, P['review']); print(f'review copy: {os.path.relpath(pp, ROOT)}'); return
    md, st = render(vol, units, review=True, for_html=False)
    wp = os.path.join(P['review'], f'Vol{vol}_working_copy_English.md')
    open(wp, 'w', encoding='utf8').write(f'# Ṛgveda-saṃhitā, Volume {vol} — working copy printed from the units (rv print)\n\n*Not edited by hand: change the units and print again. `?N` marks question N for the editor.*\n\n' + md + '\n')
    print(f'working copy: {os.path.relpath(wp, ROOT)}  ({len(md.splitlines())} lines)'); print(' ', dict(st))
    if not pdf: return
    mdh, _ = render(vol, units, review=True, for_html=True)
    # the user's preface and the original preface come first in the body; the abbreviations stand between the prefaces and the first sūkta
    body = mark_samhita(pandoc(mdh)); have = {it[1] for u in units for it in u.get('kn', []) if it[0] == 'page'}
    body = re.sub(r'(<h1[^>]*>Maṇḍala)', lambda m: abbreviations_html() + '\n' + m.group(1), body, count=1)      # abbreviations stand before the first Maṇḍala
    doc = head(f'Ṛgveda-saṃhitā, Volume {vol} (review copy)') + '<body>\n' + front_matter(vol, units, have) + '\n' + body + '\n</body></html>'
    pp = os.path.join(P['review'], f'Vol{vol}_review_copy_English.pdf'); to_pdf(doc, pp, P['review']); print(f'review copy: {os.path.relpath(pp, ROOT)}')
