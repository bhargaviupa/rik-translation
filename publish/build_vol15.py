#!/usr/bin/env python3
"""Volume 15 print build:  python3 publish/build_vol15.py [--html-only]

Reads vol15/Rigveda_Samhita_Vol15_English_Translation.md (never modified) and writes
publish/out/vol15_full.html and vol15_full.pdf (pandoc -> HTML -> WeasyPrint, style.css).

Differences from build_vol45.py (which expects the older heading layout of Vols 4-13):
  * headings are '## Sūkta N (Maṇḍala M)' / '#### Ṛk N'; page marks are '### Printed p. N'
  * Sūkta 39 and 40 have no '##' heading in the file (only a bold / italic heading note): the two
    headings are supplied here, in memory only
  * Sanskrit quoted in Kannada script inside ⟦ … ⟧ that the build never converted (multi-line
    quotations, ~450 places) is converted here to Devanagari + (IAST), in memory only
"""
import re, sys, html, pathlib, subprocess, unicodedata
PUB = pathlib.Path(__file__).resolve().parent
ROOT = PUB.parent
sys.path.insert(0, str(ROOT / 'publish' / 'tools' / 'translit'))
from kannada_to_deva import kn2deva
from add_iast import deva_to_iast

SRC = ROOT / 'vol15' / 'Rigveda_Samhita_Vol15_English_Translation.md'
KN = re.compile('[ಀ-೿]')

def convert_inline(md):
    """⟦kannada⟧ (may span lines) -> devanagari (*iast*), as the normal build does for one-line quotes"""
    n = [0]
    def rep(m):
        s = m.group(1)
        if not KN.search(s):
            return m.group(0)
        n[0] += 1
        d = kn2deva(re.sub(r'\s*\n\s*', ' ', s).strip())
        return f'{d} (*{deva_to_iast(d)}*)'
    return re.sub(r'⟦([^⟧]*)⟧', rep, md), n[0]

def add_missing_headings(md):
    """Sūkta 39 and 40 have no '##' heading: put one in front of the first line that announces them"""
    out, done = [], set()
    for line in md.split('\n'):
        m39 = re.match(r'\*\*Sūkta 39\*\*', line)
        m40 = re.match(r'\*\[The heading lines of the supplied text, kept as a note: ಸೂಕ್ತ—೪೦', line)
        for flag, m, no in (('39', m39, 39), ('40', m40, 40)):
            if m and flag not in done:
                done.add(flag); out += [f'## Sūkta {no} (Maṇḍala 2)', '']
        out.append(line)
    return '\n'.join(out), sorted(done)

def pandoc_html(md):
    r = subprocess.run(['pandoc', '-f', 'markdown-yaml_metadata_block-smart+pipe_tables', '-t', 'html5', '--wrap=none'],
                       input=md, capture_output=True, text=True, check=True)
    return r.stdout

def build(html_only=False):
    md = SRC.read_text(encoding='utf-8')
    md = re.sub(r'\n---\n+\*\*Progress note:\*\*.*\Z', '\n', md, flags=re.S)   # position marker is not part of the book
    md, added = add_missing_headings(md)
    md, nconv = convert_inline(md)
    left = len(re.findall('⟦', md))
    print(f'added headings for Sūkta {added}; converted {nconv} Kannada-script quotations; ⟦ left: {left}')
    body = pandoc_html(md)

    toc, state = [], {'n': 0}
    def head(m):
        tag, inner = m.group(1), m.group(2)
        text = re.sub(r'<[^>]+>', '', inner).strip()
        state['n'] += 1; hid = f'h{state["n"]}'
        if tag == 'h1':
            return f'<h1 class="book" id="{hid}">{inner}</h1>' if state['n'] > 1 else ''
        if tag == 'h2':
            mm = re.match(r'S[ūu]kta\s+(\d+)\s+\(Maṇḍala\s+(\d+)\)', text)
            lab = f'Maṇḍala {mm.group(2)} · Sūkta {mm.group(1)}' if mm else text
            cls = 'sukta' if mm else 'part'
            toc.append((hid, lab, cls))
            return f'<h2 class="{cls}" id="{hid}" data-short="{html.escape(lab)}">{inner}</h2>'
        if tag == 'h3':
            mm = re.match(r'Printed p\.\s*(\d+)', text)
            if mm:
                return f'<h3 class="pg" id="{hid}"><span>p. {mm.group(1)}</span></h3>'
        return f'<{tag} id="{hid}">{inner}</{tag}>'
    body = re.sub(r'<(h1|h2|h3|h4)[^>]*>(.*?)</\1>', head, body, flags=re.S)

    tochtml = ['<section class="toc"><h2>Contents</h2><ul>']
    for hid, lab, cls in toc:
        tochtml.append(f'<li class="{"su" if cls == "part" else "ch sk"}"><a href="#{hid}">{html.escape(lab)}</a></li>')
    tochtml.append('</ul></section>')

    title = 'Maṇḍala 2 · Sūktas 24–43 and Maṇḍala 3 · Sūktas 1–6 · Seventh and Eighth Adhyāyas of the Second Aṣṭaka'
    front = f'''
<section class="titlepage">
  <div class="inv dev">॥ श्री महागणाधिपतये नमः ॥</div>
  <h1>Ṛgveda-saṃhitā</h1>
  <div class="sub">with the Bhāṣya of Sāyaṇācārya<br>and the Kannada Commentary of H. P. Venkata Rao</div>
  <div class="orn">❖</div>
  <div style="font-size:15pt;letter-spacing:.1em">VOLUME 15</div>
  <div class="sub" style="margin-top:.2in">{title}</div>
  <div class="orn">❖</div>
  <div class="who">English Translation by<br><span style="font-size:14pt;letter-spacing:.06em">Bhargavi Upadhya</span><br>
  <i style="font-size:9.5pt">prepared with the assistance of Claude, an AI model by Anthropic</i><br><br>
  <span style="font-size:9.5pt">Based on the Kannada edition of Asthāna Mahāvidvān H. P. Venkata Rao, Editor<br>
  Śrī Jayacāmarājendra Vedaratna-mālā · Mysore, 1949</span></div>
</section>
<section class="copyright"><p>Working text. Printed pages 1–800 of the supplied Kannada text; the front matter of the Kannada volume (title page, imprint, dedication, translator's note, preface, contents, abbreviations) is not yet translated.</p>
<p>Square-bracketed italic notes record the state of the supplied text (garbled words, printed variants, stray lines). Numbers and readings are given as supplied; doubtful places are marked [?].</p></section>'''
    doc = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Ṛgveda-saṃhitā, Volume 15</title>
<link rel="stylesheet" href="../style.css"><link rel="stylesheet" href="../style_vol15.css"></head><body>
{front}
{chr(10).join(tochtml)}
{body}
</body></html>'''
    out = PUB / 'out'; out.mkdir(exist_ok=True)
    (out / 'vol15_full.html').write_text(doc, encoding='utf-8')
    print('wrote out/vol15_full.html', len(doc) // 1024, 'KB')
    if not html_only:
        from weasyprint import HTML
        HTML(string=doc, base_url=str(out)).write_pdf(out / 'vol15_full.pdf')
        print('wrote out/vol15_full.pdf')

if __name__ == '__main__':
    build('--html-only' in sys.argv)
