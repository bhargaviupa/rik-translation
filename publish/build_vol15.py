#!/usr/bin/env python3
"""Volume 15 print build:  python3 publish/build_vol15.py [eng|kan] [--html-only]

Reads vol15/Rigveda_Samhita_Vol15_English_Translation.md (never modified) and writes
publish/out/vol15_full_Eng.pdf and vol15_full_Kan.pdf (+ .html) (pandoc -> HTML -> WeasyPrint, style.css).

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
KSRC = ROOT / 'vol15' / 'Rigveda_Samhita_Vol15_Kannada_Text.md'
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


def front(lang):
    """cover, title page, credits, portraits - the Vol 1 front-matter pattern (publish/build.py: front_matter)"""
    eng = lang == 'eng'
    cap = ('Ṛgveda-saṃhitā &nbsp;·&nbsp; Volume 15 &nbsp;·&nbsp; English Translation' if eng
           else 'Ṛgveda-saṃhitā &nbsp;·&nbsp; Volume 15 &nbsp;·&nbsp; Kannada Text')
    vt = 'Maṇḍala 2 · Sūktas 24–43 and Maṇḍala 3 · Sūktas 1–6<br>Seventh and Eighth Adhyāyas of the Second Aṣṭaka'
    who = ('English Translation by<br><span style="font-size:14pt;letter-spacing:.06em">Bhargavi Upadhya</span><br>'
           '<i style="font-size:9.5pt">prepared with the assistance of Claude, an AI model by Anthropic</i>' if eng else
           'Kannada text of the printed edition, transcribed from the supplied machine-read text<br>'
           '<i style="font-size:9.5pt">prepared with the assistance of Claude, an AI model by Anthropic</i>')
    credit = ('<p><b>© 2026 Bhargavi Upadhya.</b> The English translation, together with its notes, footnotes and apparatus, is the copyright of Bhargavi Upadhya. All rights reserved.</p>' if eng else
              '<p><b>© 2026 Bhargavi Upadhya.</b> This Kannada text is a transcription of the 1952 edition made from the supplied machine-read text; its apparatus is the copyright of Bhargavi Upadhya. All rights reserved.</p>')
    return f'''
<section class="cover"><img src="../assets/cover_vol15.jpg" alt="Cover, Volume 15">
  <div class="cap">{cap}</div></section>
<section class="titlepage">
  <div class="inv dev">॥ श्री महागणाधिपतये नमः ॥</div>
  <h1>Ṛgveda-saṃhitā</h1>
  <div class="sub">with the Bhāṣya of Sāyaṇācārya<br>and the Kannada Commentary of H. P. Venkata Rao</div>
  <div class="orn">❖</div>
  <div style="font-size:15pt;letter-spacing:.1em">VOLUME 15</div>
  <div class="sub" style="margin-top:.2in">{vt}</div>
  <div class="orn">❖</div>
  <div class="who">{who}<br>
  <span style="font-size:8.5pt;line-height:1.4;display:block;margin-top:.12in">Based on the Kannada edition of Asthāna Mahāvidvān H. P. Venkata Rao, Editor<br>
  Śrī Jayacāmarājendra Vedaratna-mālā · Kannada Sāhitya Pariṣat<br>Śrī Śāradā Press, Mysore, 1952</span></div>
</section>
<section class="copyright">{credit}
<p>This text is based on the Kannada edition of the <i>Ṛgveda-saṃhitā with the Sāyaṇa-bhāṣya</i>, edited and translated by Asthāna Mahāvidvān H. P. Venkata Rao and printed at Śrī Śāradā Press, Mysore, 1952, published by the gracious permission of His Highness Śrī Jayacāmarājendra Wadiyar Bahadur, G.C.B., G.C.S.I., Maharaja of Mysore. <i>The cover on the first page is a reconstruction: the arch artwork of the series with the Volume 15 lettering redrawn, until a scan of the original cover is supplied.</i></p>
<p>Square-bracketed italic notes record the state of the supplied text (garbled words, printed variants, stray lines). Numbers and readings are given as supplied; doubtful places are marked [?].</p>
<p><i>[Publisher, ISBN, edition and printing details — to be supplied. Permissions status of the 1952 original and of the portraits — to be confirmed before publication.]</i></p></section>
<section class="portrait"><h2>Patron of the First Edition</h2>
 <img class="pic" src="../assets/maharaja.jpg" alt="Maharaja of Mysore">
 <p class="cap2">His Highness Śrī Jayacāmarājendra Wadiyar Bahadur, G.C.B., G.C.S.I.,<br>Maharaja of Mysore, by whose gracious permission the original edition was published.</p></section>
<section class="portrait"><h2>Guru &amp; President of the Board of Scholars</h2>
 <img class="pic" src="../assets/guruji.jpg" alt="Guruji">
 <p class="cap2">Śrī Jagadguru Nāgaliṅga-parivrājakācārya-pīṭhādhyakṣa<br>Śilpasiddhānti Śivayogi Śrī Siddhaliṅga Svāmigaḷavaru,<br>President of the Veda-vimarśana Vidvan-maṇḍali</p></section>
<section class="portrait pair"><h2>The Present Day</h2>
 <div class="placeholder half">[Portrait of the present Maharaja — to be supplied]<br><br>[Name, title and caption]</div>
 <div class="placeholder half">[Portrait of the present Guruji — to be supplied]<br><br>[Name, title and caption]</div></section>'''

def wrap(front_html, rest, kan=False):
    css = '<link rel="stylesheet" href="../style_vol15.css">' + ('<link rel="stylesheet" href="../style_vol15_kan.css">' if kan else '')
    t = 'Ṛgveda-saṃhitā, Volume 15 (Kannada text)' if kan else 'Ṛgveda-saṃhitā, Volume 15 (English translation)'
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

def build_eng(html_only=False):
    md = SRC.read_text(encoding='utf-8')
    md = re.sub(r'\n---\n+\*\*Progress note:\*\*.*\Z', '\n', md, flags=re.S)
    md, added = add_missing_headings(md)
    md, nconv = convert_inline(md)
    print(f'[eng] added headings for Sūkta {added}; converted {nconv} Kannada-script quotations; ⟦ left: {len(re.findall("⟦", md))}')
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
            if mm: return f'<h3 class="pg" id="{hid}"><span>p. {mm.group(1)}</span></h3>'
        return f'<{tag} id="{hid}">{inner}</{tag}>'
    body = re.sub(r'<(h1|h2|h3|h4)[^>]*>(.*?)</\1>', head, body, flags=re.S)
    t = ['<section class="toc"><h2>Contents</h2><ul>']
    for hid, lab, cls in toc:
        t.append(f'<li class="{"su" if cls == "part" else "ch sk"}"><a href="#{hid}">{html.escape(lab)}</a></li>')
    t.append('</ul></section>')
    write(wrap(front('eng'), '\n'.join(t) + '\n' + body), 'vol15_full_Eng', html_only)

def kannada_front_matter():
    """Original Kannada front matter (title page ... list of abbreviations), up to the Pīṭhike (printed p. 1)."""
    lines = (ROOT / 'vol15' / 'html' / 'rig_15_1.md').read_text(encoding='utf-8').split('\n')
    end = next(i for i, l in enumerate(lines) if l.startswith('\u0950'))
    keep = []
    for l in lines[1:end]:
        if 'This image contains' in l: continue
        keep.append(re.sub(r'^## (.*)$', r'**\1**', l))
    md = re.sub(r'\n---\n', '\n\n<div class="pb"></div>\n\n', '\n'.join(keep))
    return ('<section class="kfront kn"><p class="kfnote">Original Kannada front matter, as supplied (machine-read text, not proofread): '
            'title page, imprint, dedication, board of scholars, translator\'s note, preface, contents and list of abbreviations.</p>'
            + pandoc_html(md) + '</section>')

def build_kan(html_only=False):
    md = KSRC.read_text(encoding='utf-8')
    md = re.sub(r'\A# [^\n]*\n(\*[^\n]*\*\n)?', '', md)                   # file title + its italic header line
    md = re.sub(r'\n---\n+\*\*Progress note:\*\*.*\Z', '\n', md, flags=re.S)
    md = re.sub(r'<!-- printed (\d+) -->', r'### Printed p. \1', md)
    md = re.sub(r'\n---\n', '\n', md)
    body = pandoc_html(md)
    state = {'n': 0}
    def head(m):
        tag, inner = m.group(1), m.group(2)
        state['n'] += 1
        mm = re.match(r'Printed p\.\s*(\d+)', re.sub(r'<[^>]+>', '', inner).strip())
        if mm: return f'<h3 class="pg" id="p{mm.group(1)}"><span>p. {mm.group(1)}</span></h3>'
        return f'<{tag}>{inner}</{tag}>'
    body = re.sub(r'<(h1|h2|h3|h4)[^>]*>(.*?)</\1>', head, body, flags=re.S)
    # section labels (*ಸಂಹಿತಾಪಾಠಃ* ... as one-line italic paragraphs) become small headings
    labels = '|'.join(['ಸಂಹಿತಾಪಾಠಃ', 'ಪದಪಾಠಃ', 'ಸಾಯಣಭಾಷ್ಯಂ', 'ಪ್ರತಿಪದಾರ್ಥ', 'ಭಾವಾರ್ಥ', 'English Translation\\.', 'ವಿಶೇಷವಿಷಯಗಳು'])
    body = re.sub(rf'<p><em>({labels})</em></p>', r'<p class="lab">\1</p>', body)
    write(wrap(front('kan') + kannada_front_matter(), body, kan=True), 'vol15_full_Kan', html_only)

def build(html_only=False):
    build_eng(html_only); build_kan(html_only)

if __name__ == '__main__':
    only = [a for a in sys.argv[1:] if a in ('eng', 'kan')]
    h = '--html-only' in sys.argv
    for w in (only or ['eng', 'kan']):
        (build_eng if w == 'eng' else build_kan)(h)
