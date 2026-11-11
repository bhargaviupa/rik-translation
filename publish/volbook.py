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
English PDF (volN/pubcfg.json: front_en, contents_en, contents_target_overrides): translated board/preface/abbreviations/contents (frontmatter_en.json, contents_en.json), remarks as footnotes, Introduction heading, Om on printed p. 1.
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

_C = '\u0915-\u0939\u0958-\u095F'
AKSHARA = re.compile('(?:[' + _C + ']\u093C?\u094D)*(?:[' + _C + ']\u093C?|[\u0904-\u0914\u0960\u0961\u093D\u0966-\u096F])[\u093E-\u094C\u0962\u0963]?[\u0900-\u0903]?[\u0951\u0952\u1CD0-\u1CFF\uA8E0-\uA8FF]*|\\S')

def mark_samhita(body):
    """The verse (Saṃhitā) in the traditional look: larger type and a little space after every syllable, so each accent mark sits clearly on its
    own letter (user decision, Nov 11 2026).  Only the HTML/PDF is changed: the first blockquote after a Saṃhitā label gets class "samhita", its
    lines are kept one under the other, and every akṣara is wrapped in <span class="ak"> (a conjunct stays whole).  Styling: style_volbook.css."""
    n = [0]
    def syl(text):
        return ' '.join(''.join(f'<span class="ak">{a}</span>' for a in AKSHARA.findall(w)) for w in text.split(' '))
    def rep(m):
        n[0] += 1
        inner = re.sub(r'(?<!>)\n(?!<)', '<br />\n', m.group(2).strip('\n'))                 # soft line breaks of the verse become real ones
        parts = re.split(r'(<[^>]+>)', inner)
        inner = ''.join(p if p.startswith('<') or not re.search('[\u0900-\u097F]', p) else '\n'.join(syl(x) for x in p.split('\n')) for p in parts)
        return f'{m.group(1)}<blockquote class="samhita">\n{inner}\n</blockquote>'
    body = re.sub(r'(संहितापाठः[^<]*(?:</strong></p>|</h[1-6]>)\s*)<blockquote>(.*?)</blockquote>', rep, body, flags=re.S)
    return body, n[0]

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
            tgt = {str(k): v for k, v in cfg.get('contents_target_overrides', {}).items()}.get(str(b['src']), pg)   # link target only; the printed number is shown
            link = f'<a href="#p{tgt}">{pg}</a>' if pg else ''
            out.append(f'<p class="cit"><span class="tx">{t}</span><span class="pn">{link}</span></p>')
    out.append('</section>')
    return '\n'.join(out), blocks


# ---------------------------------------------------------------- English front matter (translated pages), footnotes
def fn_html(text):
    """escape text and turn {{fn: ...}} into footnote spans"""
    out, pos = [], 0
    for m in re.finditer(r'\{\{fn:(.*?)\}\}', text, flags=re.S):
        out.append(html.escape(text[pos:m.start()])); out.append(f'<span class="fn">{html.escape(m.group(1).strip())}</span>'); pos = m.end()
    out.append(html.escape(text[pos:]))
    return ''.join(out)

def load_front_en(cfg):
    p = cfg.get('front_en')
    return json.loads((ROOT / p).read_text(encoding='utf8')) if p else None

def board_en(fe):
    b = fe['board']
    t = ''.join(f'<p class="bt{i}">{html.escape(x)}</p>' for i, x in enumerate(b['title_lines']))
    mem = ''.join(f'<li>{fn_html(x)}</li>' for x in b['members'])
    return (f'<section class="board"><div class="btitle">{t}</div><div class="rule">❖</div>'
            f'<p class="ed"><span class="lab">{html.escape(b["editor_label"])}</span><br><b>{html.escape(b["editor"])}</b></p>'
            f'<h3>{html.escape(b["list_title"])}</h3><ol>{mem}</ol></section>')

def preface_en(fe):
    f = fe['preface']
    paras = ''.join(f'<p>{fn_html(x)}</p>' for x in f['paragraphs'])
    dl = '<br>'.join(html.escape(x) for x in f['dateline']); sg = '<br>'.join(html.escape(x) for x in f['signature'])
    return (f'<section class="preface"><h2>{html.escape(f["title"])}</h2>{paras}'
            f'<div class="sign"><div class="dl">{dl}</div><div class="sg">{sg}</div></div></section>')

def abbreviations_en(fe):
    a = fe['abbreviations']
    rows = ''.join(f'<tr><td class="kn">{html.escape(x[0])}</td><td>{html.escape(x[1])}</td><td>{html.escape(x[2])}</td></tr>' for x in a['rows'])
    note = f'<p class="abnote">{html.escape(a["note"])}</p>' if a.get('note') else ''
    return (f'<section class="abbr"><h2>{html.escape(a["title"])}</h2><p class="abintro">{html.escape(a["intro"])}</p>'
            f'<table><tr><th>As printed</th><th>Here</th><th>Work</th></tr>{rows}</table>{note}</section>')

def contents_en_html(cfg, fe, suk_ids):
    """Contents translated into English; every entry links to the printed-page mark of the body, so the page shown is the page of THIS book.
    suk_ids: heading ids of the sūktas in order (the n-th sūkta line of the contents links to the n-th sūkta heading)."""
    en = {e['src']: e for e in json.loads((ROOT / cfg['contents_en']).read_text(encoding='utf8'))}
    c = cfg['contents']
    lines = (ROOT / cfg['supplied_md']).read_text(encoding='utf-8').split('\n')
    fxp = ROOT / c['fixes'] if c.get('fixes') else None
    f = json.loads(fxp.read_text(encoding='utf8')) if fxp and fxp.exists() else {}
    blocks = contents_parse.parse(lines, 'ವಿಷಯಾನುಕ್ರಮಣಿಕೆ', 'ಸಂಕೇತಾಕ್ಷರಗಳ', f)
    ov = {str(k): v for k, v in cfg.get('contents_target_overrides', {}).items()}
    h = fe['contents']['heading']
    def conv(t):
        return re.sub(r'⟦([^⟧]*)⟧', lambda m: '\0' + deva_to_iast(kn2deva(m.group(1))).replace('è', 'e').replace('ò', 'o') + '\1', t)
    def esc(t):
        t = html.escape(conv(t)); return t.replace('\0', '<i>').replace('\1', '</i>')
    out = [f'<section class="econtents"><p class="ph1">{html.escape(h[0])}</p><p class="ph2">{html.escape(h[1])}</p>']
    si = 0
    first_pg, cur = {}, None                       # printed page of the first item of each sūkta (the sūkta line shows where its text begins)
    for b in blocks:
        if b['t'] == 'sukta': cur = b['src']
        elif b['t'] == 'item' and cur is not None and cur not in first_pg: first_pg[cur] = ov.get(str(b['src']), b.get('page'))
    for b in blocks:
        e = en.get(b['src'], {}); t = esc(e.get('en', '')); fn = f'<span class="fn">{html.escape(e["note"])}</span>' if e.get('note') else ''
        if b['t'] == 'sukta':
            si += 1; pg = first_pg.get(b['src'])
            tgt = f'#p{pg}' if pg else (f'#{suk_ids[si-1]}' if si <= len(suk_ids) else '')
            out.append(f'<p class="csu"><a href="{tgt}">{t}{fn}</a></p>')
        elif b['t'] == 'mandala':
            out.append(f'<p class="cma">{t}</p>')
        elif b['t'] == 'center':
            out.append(f'<p class="cce">{t}</p>')
        else:
            pg = ov.get(str(b['src']), b.get('page'))
            out.append(f'<p class="cit"><a href="#p{pg}">{t}{fn}</a></p>' if pg else f'<p class="cit">{t}{fn}</p>')
    out.append(f'<p class="cnote">{html.escape(fe["contents"]["page_note"])}</p></section>')
    return '\n'.join(out)

NOTE_RX = re.compile(r'^(\[|Running head|\(The supplied|\(In the supplied|\(A small stray|\(Note|Note|Stray line|\(Readings|Title page of the volume)')
INLINE_GROUP = re.compile(r'\((?:[^()]|\([^()]*\)){0,500}\)|\[(?:[^\[\]]|\[[^\[\]]*\]){0,500}\]')
INLINE_REMARK = re.compile(r'as supplied|supplied text|as printed|so in the supplied|Doubt:|the print (?:has|reads)|kept as supplied|printed ', re.I)
def notes_to_footnotes(body):
    """The translator's notes (italic bracketed paragraphs such as running heads, stray lines, doubtful readings, and short inline
    parentheses 'as supplied …') become numbered footnotes (numbering restarts at every sūkta, see CSS). The .md is not changed."""
    import lxml.html
    from lxml import etree
    root = lxml.html.fragment_fromstring(body, create_parent='div')
    kids = list(root)
    def is_note(el):
        if el.tag != 'p' or len(el) != 1 or el[0].tag != 'em' or (el.text or '').strip(): return False
        tail = (el[0].tail or '').strip()
        if tail and not (tail.startswith('(') and tail.endswith(')') and len(tail) < 220): return False   # e.g. '*Running head: …* (Pīṭhike, continued …)'
        return bool(NOTE_RX.match(el[0].text_content().strip()))
    def is_carrier(el): return el.tag in ('p', 'blockquote') and not is_note(el)
    pending, nnote = [], 0
    def make_span(el):
        sp = etree.Element('span'); sp.set('class', 'fn')
        em = el[0]; txt = em.text_content().strip()
        if txt.startswith('[') and txt.endswith(']'):
            # strip the brackets inside the first/last text nodes
            sp.text = (em.text or '').lstrip()[1:] if (em.text or '').lstrip().startswith('[') else em.text
            for ch in em: sp.append(ch)
            last = sp[-1] if len(sp) else None
            if last is not None and (last.tail or '').rstrip().endswith(']'): last.tail = last.tail.rstrip()[:-1]
            elif last is None and sp.text and sp.text.rstrip().endswith(']'): sp.text = sp.text.rstrip()[:-1]
        else:
            sp.text = em.text
            for ch in em: sp.append(ch)
        tail = (em.tail or '').strip()
        if tail:                                           # trailing parenthetical of the same paragraph
            if len(sp): sp[-1].tail = (sp[-1].tail or '') + ' ' + tail
            else: sp.text = (sp.text or '') + ' ' + tail
        return sp
    def attach(carrier, span):
        tgt = carrier
        if carrier.tag == 'blockquote':
            ps = carrier.findall('p'); tgt = ps[-1] if ps else carrier
        tgt.append(span)
    for i, el in enumerate(kids):
        if not is_note(el): continue
        j = i - 1
        while j >= 0 and (is_note(kids[j]) or kids[j].getparent() is None): j -= 1       # skip neighbouring notes (already moved)
        carrier = kids[j] if j >= 0 and is_carrier(kids[j]) else None                     # a note right after a heading belongs to the text that follows
        if carrier is None:
            k = i + 1
            while k < len(kids) and not is_carrier(kids[k]): k += 1
            carrier = kids[k] if k < len(kids) else None
        if carrier is None: continue
        attach(carrier, make_span(el)); nnote += 1
        el.getparent().remove(el)
    # inline remarks: a parenthesis or bracket (one nesting level) that says 'as supplied', 'supplied text', 'as printed', 'Doubt:' … -> footnote
    ninl = 0
    def rep(m):
        nonlocal ninl
        g = m.group(0); inner = g[1:-1]
        if not INLINE_REMARK.search(re.sub(r'<[^>]+>', '', inner)) or re.fullmatch(r'\s*(?:\?|sic)\s*', inner): return g
        ninl += 1
        return '<span class="fn">' + inner[:1].upper() + inner[1:] + '</span>'
    for p in list(root.iter('p')):
        h = etree.tostring(p, encoding='unicode')
        segs = re.split(r'(<span class="fn">.*?</span>)', h, flags=re.S)
        new = ''.join(sg if k % 2 else INLINE_GROUP.sub(rep, sg) for k, sg in enumerate(segs))
        if new != h:
            np_ = lxml.html.fragment_fromstring(new)
            p.getparent().replace(p, np_)
    out = ''.join(etree.tostring(c, encoding='unicode', method='html') for c in root)
    print(f'[eng] notes moved to footnotes: {nnote} paragraphs, {ninl} inline')
    return out

def intro_headings(body):
    """'Pīṭhike (Introduction)' paragraphs become 'Introduction' headings; the first one (the volume's opening chapter) starts a new page"""
    first = [True]
    def rep(m):
        rest = m.group(1) or ''
        cls = 'intro first' if first[0] else 'intro'; first[0] = False
        return f'<h3 class="{cls}">Introduction{rest}</h3>'
    return re.sub(r'<p><strong>Pīṭhike \(Introduction\)([^<]*)</strong></p>', rep, body)

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
<p>This text is based on the Kannada edition of the <i>Ṛgveda-saṃhitā with the Sāyaṇa-bhāṣya</i>, edited and translated by Asthāna Mahāvidvān H. P. Venkata Rao and printed at Śrī Śāradā Press, Mysore, {cfg["year"]}, published by the gracious permission of His Highness Śrī Jayacāmarājendra Wadiyar Bahadur, G.C.B., G.C.S.I., Maharaja of Mysore. The cover, portrait and permission page are reproduced from the scanned front matter of that edition; the board of scholars, the preface, the contents and the list of abbreviations are translated.</p>
<p>Remarks on the state of the supplied text (garbled words, printed variants, stray lines) are given as numbered footnotes at the foot of the page. Numbers and readings are given as supplied; doubtful places are marked [?].</p>
<p><i>[Publisher, ISBN, edition and printing details — to be supplied. Permissions status of the {cfg["year"]} original and of the portraits — to be confirmed before publication.]</i></p></section>''')
    parts.append(f'<section class="scan"><h2 class="stitle">Patron of the First Edition</h2><img src="{fmi[r["portrait"]]}" alt="Maharaja of Mysore">'
                 '<p class="cap2">His Highness Śrī Jayacāmarājendra Wadiyar Bahadur, G.C.B., G.C.S.I., Maharaja of Mysore</p></section>')
    parts.append(scan(fmi[r['permission']], 'scan small', 'Permission page'))
    fe = load_front_en(cfg) if eng else None
    if fe:                                              # English PDF: the board page and the preface are translated, typeset pages
        parts.append(board_en(fe)); parts.append(preface_en(fe))
    else:
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
    body, nv = mark_samhita(body); print(f'[eng] verses set in the spaced Saṃhitā style: {nv}')
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
    fe = load_front_en(cfg)
    body = notes_to_footnotes(body)
    body = intro_headings(body)
    body = body.replace('<h3 class="pg" id="p1"><span>p. 1</span></h3>', '<h3 class="pg" id="p1"><span>p. 1</span></h3><div class="om">ॐ</div>', 1)
    suk_ids = [h for h, l, c in toc if c == 'sukta']
    if fe and cfg.get('contents_en'):
        ch = contents_en_html(cfg, fe, suk_ids); blocks = []
        ab = abbreviations_en(fe)
        idx = ''
    else:
        idx = '<section class="toc"><h2>Index of Sūktas</h2><ul>' + ''.join(f'<li class="{"su" if c == "part" else "ch sk"}"><a href="#{h}">{html.escape(l)}</a></li>' for h, l, c in toc) + '</ul></section>'
        ch, blocks = contents_html(cfg); ab = abbreviations(cfg)
    write(wrap(front(cfg, 'eng', fm(cfg), blocks), ch + '\n' + ab + '\n' + idx + '\n' + body, False, cfg['vol']), cfg['out'] + '_Eng', html_only)

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
