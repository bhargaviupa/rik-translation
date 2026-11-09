#!/usr/bin/env python3
"""Generic print build for the volumes translated from the supplied machine-read text (Vol 15 onwards).

  python3 publish/volbook.py N [eng|kan] [--html-only]

Reads volN/pubcfg.json and writes publish/out/<out>_Eng.pdf / <out>_Kan.pdf (+ .html).  Nothing in the volume's .md files is changed.

Per-volume inputs (see vol15/pubcfg.json):
  * front-matter page images from the user's scan PDF:  publish/tools/frontmatter/fm_extract.py UPLOAD.pdf --vol N --roles cover,title,...
    (roles are named in pubcfg 'front': cover, title, portrait, permission, board, preface[...])
  * the printed contents, parsed from the supplied md:  publish/tools/frontmatter/contents_parse.py  (+ optional fixes file)
  * the English translation md and the Kannada text md of the volume

Front matter (the Vol 1 pattern, aligned to the volume's own scans):
  English PDF: cover scan | typeset title page | credits | patron portrait scan | permission page scan | board of scholars scan |
               guru portrait | present-day placeholders | printed contents (typeset like the original) | sūkta index | body
  Kannada PDF: cover scan | title page scan | credits | portrait scan | permission scan | board scan | preface scans |
               guru portrait | present-day placeholders | printed contents | body (Kannada text)
Body conversions done in memory only: missing '## Sūkta N' headings are supplied (pubcfg 'missing_headings'); every leftover
⟦Kannada-script Sanskrit⟧ quotation (also multi-line) is converted to Devanagari + (IAST).
"""
import re, sys, html, json, pathlib, subprocess
PUB = pathlib.Path(__file__).resolve().parent
ROOT = PUB.parent
sys.path.insert(0, str(ROOT / 'publish' / 'tools' / 'translit'))
sys.path.insert(0, str(ROOT / 'publish' / 'tools' / 'frontmatter'))
from kannada_to_deva import kn2deva
from add_iast import deva_to_iast
import contents_parse

KN = re.compile('[ಀ-೿]')

# ---------------------------------------------------------------- text conversions (in memory)
def convert_inline(md):
    n = [0]
    def rep(m):
        s = m.group(1)
        if not KN.search(s): return m.group(0)
        n[0] += 1
        d = kn2deva(re.sub(r'\s*\n\s*', ' ', s).strip())
        return f'{d} (*{deva_to_iast(d)}*)'
    return re.sub(r'⟦([^⟧]*)⟧', rep, md), n[0]

def add_missing_headings(md, specs):
    out, done = [], set()
    have = set(md.split('\n'))                       # a heading already in the file is never added twice
    for line in md.split('\n'):
        for k, sp in enumerate(specs):
            if k not in done and sp['heading'] not in have and re.match(sp['find'], line):
                done.add(k); out += [sp['heading'], '']
        out.append(line)
    return '\n'.join(out), len(done)

def pandoc_html(md):
    r = subprocess.run(['pandoc', '-f', 'markdown-yaml_metadata_block-smart+pipe_tables', '-t', 'html5', '--wrap=none'],
                       input=md, capture_output=True, text=True, check=True)
    return r.stdout

# ---------------------------------------------------------------- front matter
def fm(cfg):
    d = json.loads((ROOT / cfg['assets'] / 'frontmatter.json').read_text(encoding='utf8'))
    rel = pathlib.Path(cfg['assets']).relative_to('publish')
    return {p['role']: f'../{rel}/{p["file"]}' for p in d['pages']}

def scan(img, cls='scan', alt=''):
    return f'<section class="{cls}"><img src="{img}" alt="{alt}"></section>'

def contents_html(cfg):
    c = cfg['contents']
    lines = (ROOT / cfg['supplied_md']).read_text(encoding='utf-8').split('\n')
    fxp = ROOT / c['fixes'] if c.get('fixes') else None
    f = json.loads(fxp.read_text(encoding='utf8')) if fxp and fxp.exists() else {}
    blocks = contents_parse.parse(lines, 'ವಿಷಯಾನುಕ್ರಮಣಿಕೆ', 'ಸಂಕೇತಾಕ್ಷರಗಳ', f)
    for b in blocks:
        if b['t'] == 'item' and isinstance(f.get(str(b['src'])), int): b['page'] = f[str(b['src'])]
    h = c['heading']
    out = [f'<section class="pcontents kn"><p class="ph1">{h[0]}</p><p class="ph2">{h[1]}</p><p class="ph3">{h[2]}</p>']
    for b in blocks:
        t = html.escape(b['text'])
        if b['t'] == 'sukta':
            out.append(f'<p class="csu"><span class="no">{b["no"]}.</span> {t}—</p>')
        elif b['t'] == 'mandala':
            out.append(f'<p class="cma">{t}—</p>')
        elif b['t'] == 'center':
            out.append(f'<p class="cce">{t}</p>')
        else:
            pg = b['page']
            link = f'<a href="#p{pg}">{pg}</a>' if pg else ''
            out.append(f'<p class="cit"><span class="tx">{t}</span><span class="pn">{link}</span></p>')
    out.append('</section>')
    return '\n'.join(out), blocks

def front(cfg, lang, fmi, toc_blocks):
    eng = lang == 'eng'
    v = cfg['vol']
    cap = f'Ṛgveda-saṃhitā &nbsp;·&nbsp; Volume {v} &nbsp;·&nbsp; ' + ('English Translation' if eng else 'Kannada Text')
    who = ('English Translation by<br><span style="font-size:14pt;letter-spacing:.06em">Bhargavi Upadhya</span><br>'
           '<i style="font-size:9.5pt">prepared with the assistance of Claude, an AI model by Anthropic</i>' if eng else
           'Kannada text of the printed edition, transcribed from the supplied machine-read text<br>'
           '<i style="font-size:9.5pt">prepared with the assistance of Claude, an AI model by Anthropic</i>')
    credit = ('<p><b>© 2026 Bhargavi Upadhya.</b> The English translation, together with its notes, footnotes and apparatus, is the copyright of Bhargavi Upadhya. All rights reserved.</p>' if eng else
              f'<p><b>© 2026 Bhargavi Upadhya.</b> This Kannada text is a transcription of the {cfg["year"]} edition made from the supplied machine-read text; its apparatus is the copyright of Bhargavi Upadhya. All rights reserved.</p>')
    r = cfg['front']
    parts = [f'<section class="cover"><img src="{fmi[r["cover"]]}" alt="Cover, Volume {v}"><div class="cap">{cap}</div></section>']
    if eng:
        parts.append(f'''<section class="titlepage">
  <div class="inv dev">॥ श्री महागणाधिपतये नमः ॥</div>
  <h1>Ṛgveda-saṃhitā</h1>
  <div class="sub">with the Bhāṣya of Sāyaṇācārya<br>and the Kannada Commentary of H. P. Venkata Rao</div>
  <div class="orn">❖</div>
  <div style="font-size:15pt;letter-spacing:.1em">VOLUME {v}</div>
  <div class="sub" style="margin-top:.2in">{cfg["range_line"]}<br>{cfg["adhyaya_line"]}</div>
  <div class="orn">❖</div>
  <div class="who">{who}<br>
  <span style="font-size:8.5pt;line-height:1.4;display:block;margin-top:.12in">Based on the Kannada edition of Asthāna Mahāvidvān H. P. Venkata Rao, Editor<br>{cfg["imprint"]}</span></div>
</section>''')
    else:
        parts.append(scan(fmi[r['title']], 'scan', 'Title page'))
    parts.append(f'''<section class="copyright">{credit}
<p>This text is based on the Kannada edition of the <i>Ṛgveda-saṃhitā with the Sāyaṇa-bhāṣya</i>, edited and translated by Asthāna Mahāvidvān H. P. Venkata Rao and printed at Śrī Śāradā Press, Mysore, {cfg["year"]}, published by the gracious permission of His Highness Śrī Jayacāmarājendra Wadiyar Bahadur, G.C.B., G.C.S.I., Maharaja of Mysore. The cover, title page, portrait, permission page and board of scholars are reproduced from the scanned front matter of that edition.</p>
<p>Square-bracketed italic notes record the state of the supplied text (garbled words, printed variants, stray lines). Numbers and readings are given as supplied; doubtful places are marked [?].</p>
<p><i>[Publisher, ISBN, edition and printing details — to be supplied. Permissions status of the {cfg["year"]} original and of the portraits — to be confirmed before publication.]</i></p></section>''')
    parts.append(f'<section class="scan"><h2 class="stitle">Patron of the First Edition</h2><img src="{fmi[r["portrait"]]}" alt="Maharaja of Mysore">'
                 '<p class="cap2">His Highness Śrī Jayacāmarājendra Wadiyar Bahadur, G.C.B., G.C.S.I., Maharaja of Mysore</p></section>')
    parts.append(scan(fmi[r['permission']], 'scan small', 'Permission page'))
    parts.append(f'<section class="scan"><img src="{fmi[r["board"]]}" alt="Board of scholars"><p class="cap2">{cfg["board_caption"]}</p></section>')
    for i, role in enumerate(r.get('preface', [])):
        if not eng: parts.append(scan(fmi[role], 'scan', f'Preface page {i + 1}'))
    parts.append('''<section class="portrait"><h2>Guru &amp; President of the Board of Scholars</h2>
 <img class="pic" src="../assets/guruji.jpg" alt="Guruji">
 <p class="cap2">Śrī Jagadguru Nāgaliṅga-parivrājakācārya-pīṭhādhyakṣa<br>Śilpasiddhānti Śivayogi Śrī Siddhaliṅga Svāmigaḷavaru,<br>President of the Veda-vimarśana Vidvan-maṇḍali</p></section>
<section class="portrait pair"><h2>The Present Day</h2>
 <div class="placeholder half">[Portrait of the present Maharaja — to be supplied]<br><br>[Name, title and caption]</div>
 <div class="placeholder half">[Portrait of the present Guruji — to be supplied]<br><br>[Name, title and caption]</div></section>''')
    return '\n'.join(parts)

# ---------------------------------------------------------------- documents
def wrap(front_html, rest, kan, vol):
    css = '<link rel="stylesheet" href="../style_volbook.css">' + ('<link rel="stylesheet" href="../style_volbook_kan.css">' if kan else '')
    t = f'Ṛgveda-saṃhitā, Volume {vol} ' + ('(Kannada text)' if kan else '(English translation)')
    return (f'<!doctype html><html lang="{"kn" if kan else "en"}"><head><meta charset="utf-8"><title>{t}</title>'
            f'<link rel="stylesheet" href="../style.css"><link rel="stylesheet" href="../style_vol1.css">{css}</head><body>\n{front_html}\n{rest}\n</body></html>')

def write(doc, name, html_only):
    out = PUB / 'out'; out.mkdir(exist_ok=True)
    (out / f'{name}.html').write_text(doc, encoding='utf-8')
    print(f'wrote out/{name}.html', len(doc) // 1024, 'KB')
    if not html_only:
        from weasyprint import HTML
        HTML(string=doc, base_url=str(out)).write_pdf(out / f'{name}.pdf')
        print(f'wrote out/{name}.pdf')

def abbreviations(cfg):
    role = cfg['front'].get('abbreviations')
    return scan(fm(cfg)[role], 'scan', 'List of abbreviations') + '\n' if role else ''

def build_eng(cfg, html_only):
    md = (ROOT / cfg['english_md']).read_text(encoding='utf-8')
    md = re.sub(r'\n---\n+\*\*Progress note:\*\*.*\Z', '\n', md, flags=re.S)
    md, added = add_missing_headings(md, cfg.get('missing_headings', []))
    md, nconv = convert_inline(md)
    print(f'[eng] headings added: {added}; Kannada-script quotations converted: {nconv}; ⟦ left: {md.count("⟦")}')
    body = pandoc_html(md)
    toc, st = [], {'n': 0}
    def head(m):
        tag, inner = m.group(1), m.group(2)
        text = re.sub(r'<[^>]+>', '', inner).strip()
        st['n'] += 1; hid = f'h{st["n"]}'
        if tag == 'h1': return f'<h1 class="book" id="{hid}">{inner}</h1>' if st['n'] > 1 else ''
        if tag == 'h2':
            mm = re.match(r'S[ūu]kta\s+(\d+)\s+\(Maṇḍala\s+(\d+)\)', text)
            lab = f'Maṇḍala {mm.group(2)} · Sūkta {mm.group(1)}' if mm else text
            cls = 'sukta' if mm else 'part'
            toc.append((hid, lab, cls))
            return f'<h2 class="{cls}" id="{hid}" data-short="{html.escape(lab)}">{inner}</h2>'
        if tag == 'h3':
            mm = re.match(r'Printed p\.\s*(\d+)', text)
            if mm: return f'<h3 class="pg" id="p{mm.group(1)}"><span>p. {mm.group(1)}</span></h3>'
        return f'<{tag} id="{hid}">{inner}</{tag}>'
    body = re.sub(r'<(h1|h2|h3|h4)[^>]*>(.*?)</\1>', head, body, flags=re.S)
    idx = ['<section class="toc"><h2>Index of Sūktas</h2><ul>']
    for hid, lab, cls in toc:
        idx.append(f'<li class="{"su" if cls == "part" else "ch sk"}"><a href="#{hid}">{html.escape(lab)}</a></li>')
    idx.append('</ul></section>')
    ch, blocks = contents_html(cfg)
    ab = abbreviations(cfg)
    write(wrap(front(cfg, 'eng', fm(cfg), blocks), ch + '\n' + ab + '\n'.join(idx) + '\n' + body, False, cfg['vol']), cfg['out'] + '_Eng', html_only)

def kannada_front_matter_fallback(cfg):
    """Only used when the volume has no preface scans: the supplied text up to the Pīṭhike (the Om line that opens printed p. 1)."""
    return ''

def build_kan(cfg, html_only):
    md = (ROOT / cfg['kannada_md']).read_text(encoding='utf-8')
    md = re.sub(r'\A# [^\n]*\n(\*[^\n]*\*\n)?', '', md)
    md = re.sub(r'\n---\n+\*\*Progress note:\*\*.*\Z', '\n', md, flags=re.S)
    md = re.sub(r'<!-- printed (\d+) -->', r'### Printed p. \1', md)
    md = re.sub(r'\n---\n', '\n', md)
    body = pandoc_html(md)
    toc, st = [], {'n': 0}
    def head(m):
        tag, inner = m.group(1), m.group(2)
        text = re.sub(r'<[^>]+>', '', inner).strip()
        st['n'] += 1; hid = f'k{st["n"]}'
        mm = re.match(r'Printed p\.\s*(\d+)', text)
        if mm: return f'<h3 class="pg" id="p{mm.group(1)}"><span>p. {mm.group(1)}</span></h3>'
        if tag == 'h2':                                   # '## ಸೂಕ್ತ N (ಮಂಡಲ M)' or '## ಮಂಡಲ M' (added from the English structure by kn_headings.py)
            cls = 'sukta' if text.startswith('ಸೂಕ್ತ') else 'part'
            toc.append((hid, text, cls))
            return f'<h2 class="{cls}" id="{hid}" data-short="{html.escape(text)}">{inner}</h2>'
        return f'<{tag} id="{hid}">{inner}</{tag}>'
    body = re.sub(r'<(h1|h2|h3|h4)[^>]*>(.*?)</\1>', head, body, flags=re.S)
    idx = ''
    if toc:
        idx = '<section class="toc"><h2>ಸೂಕ್ತಸೂಚಿ</h2><ul>' + ''.join(f'<li class="{"su" if c == "part" else "ch sk"}"><a href="#{h}">{html.escape(t)}</a></li>' for h, t, c in toc) + '</ul></section>\n'
    labels = '|'.join(['ಸಂಹಿತಾಪಾಠಃ', 'ಪದಪಾಠಃ', 'ಸಾಯಣಭಾಷ್ಯಂ', 'ಪ್ರತಿಪದಾರ್ಥ', 'ಭಾವಾರ್ಥ', 'English Translation\\.', 'ವಿಶೇಷವಿಷಯಗಳು'])
    body = re.sub(rf'<p><em>({labels})</em></p>', r'<p class="lab">\1</p>', body)
    ch, blocks = contents_html(cfg)
    write(wrap(front(cfg, 'kan', fm(cfg), blocks), ch + '\n' + abbreviations(cfg) + idx + body, True, cfg['vol']), cfg['out'] + '_Kan', html_only)

def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    vol = int(args[0]); which = args[1:] or ['eng', 'kan']
    cfg = json.loads((ROOT / f'vol{vol}' / 'pubcfg.json').read_text(encoding='utf8'))
    h = '--html-only' in sys.argv
    for w in which:
        (build_eng if w == 'eng' else build_kan)(cfg, h)

if __name__ == '__main__':
    main()
