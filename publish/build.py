#!/usr/bin/env python3
"""Build a print PDF from a volume's working .md.  Pilot: python3 build.py 3 pilot
Never edits the source .md; all transformation happens in memory / build files."""
import re, subprocess, sys, html, pathlib
import pypandoc
from weasyprint import HTML

ROOT = pathlib.Path(__file__).resolve().parent.parent
PUB = ROOT / "publish"
NOTE_RE = re.compile(r'^\*\((.+)\)\*\s*$', re.S)   # standalone italic parenthetical = translator's note
H3_RE = re.compile(r'^###\s+Pages?\s+([\d–\-]+)\s+—\s+(S[ūu]kta\s+\d+),\s*(Rik\s+\d+)(.*)$')
CHAPTER_RE = re.compile(r'^##\s+(.*)$')

def split_blocks(text):
    return [b for b in re.split(r'\n{2,}', text.strip('\n'))]

def transform(md):
    """Return (markdown_with_footnotes, notes_by_rik) from raw section markdown."""
    out, notes, rik_label, sukta_label = [], [], "Sūkta introduction", ""
    for blk in split_blocks(md):
        first = blk.split('\n', 1)[0]
        m = H3_RE.match(first)
        if m:
            pp, sukta, rik, rest = m.groups()
            rik_label = f"{sukta}, {rik}"
            out.append(f'### {rik}{rest} <span class="pp">pp. {pp}</span>')
            continue
        if first.startswith('## '):
            sukta_label = re.sub(r'\*', '', first[3:])
            m2 = re.search(r'S[ūu]kta\s+(\d+)', first)
            rik_label = f"Sūkta {m2.group(1)}, introduction" if m2 else rik_label
            out.append(blk); continue
        if blk.startswith('*(Printed'):
            out.append(blk); continue
        nm = NOTE_RE.match(blk.replace('\n', ' '))
        if nm and out and not out[-1].startswith('#') and not blk.startswith('*(Printed'):
            body = nm.group(1).strip()
            notes.append((rik_label, body))
            out[-1] = out[-1].rstrip() + f' ^[{body}]'
            continue
        out.append(blk)
    return '\n\n'.join(out), notes

def notes_appendix(notes):
    by = {}
    for lab, body in notes: by.setdefault(lab, []).append(body)
    parts = ['<h1 class="appendix" id="notes">Collected Notes</h1>',
             '<p style="text-align:center;font-style:italic">Every translator’s note and editorial remark of this volume, gathered by Sūkta and Rik.</p>',
             '<div class="notes-app">']
    n = 0
    for lab, bodies in by.items():
        parts.append(f'<h3>{html.escape(lab)}</h3>')
        for b in bodies:
            n += 1
            inline = pypandoc.convert_text(b, 'html', format='markdown-smart').replace('<p>', '').replace('</p>', '')
            parts.append(f'<p><b>{n}.</b> {inline}</p>')
    parts.append('</div>')
    return '\n'.join(parts)

def pandoc_html(md):
    return pypandoc.convert_text(md, 'html', format='markdown-smart+raw_html',
                                 extra_args=['--lua-filter', str(PUB / 'notes.lua'), '--wrap=none'])

def front_matter(vol, vtitle, entries):
    """entries: list of (sukta_id, short_label, [(rik_id, rik_label), ...])"""
    toc = []
    for sid, lab, riks in entries:
        toc.append(f'<li class="su"><a href="#{sid}">{html.escape(lab)}</a></li>')
        if riks:
            toc.append('<li class="rl"><ul class="riks">' + ''.join(
                f'<li><a href="#{rid}">{html.escape(rl)}</a></li>' for rid, rl in riks) + '</ul></li>')
    toc = '\n'.join(toc)
    return f'''
<section class="cover"><img src="assets/cover_vol3.jpg" alt="Original Kannada cover">
  <div class="cap">Ṛgveda-saṃhitā &nbsp;·&nbsp; Volume {vol} &nbsp;·&nbsp; English Translation</div></section>
<section class="titlepage">
  <div class="inv dev">॥ श्री महागणाधिपतये नमः ॥</div>
  <h1>Ṛgveda-saṃhitā</h1>
  <div class="sub">with the Bhāṣya of Sāyaṇācārya<br>and the Kannada Commentary of H. P. Venkata Rao</div>
  <div class="orn">❖</div>
  <div style="font-size:15pt;letter-spacing:.1em">VOLUME {vol}</div>
  <div class="sub" style="margin-top:.2in">{vtitle}</div>
  <div class="orn">❖</div>
  <div class="who">English Translation by<br><span style="font-size:14pt;letter-spacing:.06em">Bhargavi Upadhya</span><br>
  <i style="font-size:9.5pt">prepared with the assistance of Claude, an AI model by Anthropic</i><br><br>
  <span style="font-size:9.5pt">Based on the Kannada edition of Asthāna Mahāvidvān H. P. Venkata Rao, Editor<br>
  Śrī Jayacāmarājendra Vedaratna-mālā · Mysore, 1949</span></div>
</section>
<section class="copyright"><p><b>© 2026 Bhargavi Upadhya.</b> The English translation, together with its notes, footnotes, collected notes and apparatus, is the copyright of Bhargavi Upadhya. All rights reserved.</p>
<p>This translation is based on the Kannada edition of the <i>Ṛgveda-saṃhitā with the Sāyaṇa-bhāṣya</i>, edited and translated by Asthāna Mahāvidvān H. P. Venkata Rao and printed at Śrī Śāradā Press, Mysore, 1949, published by the gracious permission of His Highness Śrī Jayacāmarājendra Wadiyar Bahadur, G.C.B., G.C.S.I., Maharaja of Mysore. The ornate cover reproduced on the first page is from that edition.</p>
<p>The English translation was prepared with the assistance of Claude, an artificial-intelligence model made by Anthropic, working from scanned pages of the original. Readings that remain uncertain are marked [?] in the text.</p>
<p><i>[Publisher, ISBN, edition and printing details — to be supplied. Permissions status of the 1949 original and of the portraits — to be confirmed before publication.]</i></p></section>
<section class="portrait"><h2>Patron</h2>
 <img class="pic" src="assets/maharaja.jpg" alt="Maharaja of Mysore">
 <p class="cap2">His Highness Śrī Jayacāmarājendra Wadiyar Bahadur, G.C.B., G.C.S.I.,<br>Maharaja of Mysore, by whose gracious permission the original edition was published.</p></section>
<section class="portrait"><h2>Guru</h2>
 <img class="pic" src="assets/guruji.jpg" alt="Guruji">
 <p class="cap2">Śrī Jagadguru Nāgaliṅga-parivrājakācārya-pīṭhādhyakṣa<br>Śilpasiddhānti Śivayogi Śrī Siddhaliṅga Svāmigaḷavaru,<br>President of the Veda-vimarśana Vidvan-maṇḍali</p></section>
<section class="toc"><h2>Contents</h2><p class="tocsub">Sūkta by Sūkta, and Rik by Rik</p><ul>{toc}<li class="su"><a href="#notes">Collected Notes</a></li></ul></section>
'''

def build(vol, mode):
    src = (ROOT / f"Rigveda_Samhita_Vol{vol}_English_Translation.md").read_text(encoding='utf-8').split('\n')
    heads = [i for i, l in enumerate(src) if l.startswith('## ') and re.search(r'S[ūu]kta\s+\d+', l)]
    s, e = heads[0], (heads[1] if mode == 'pilot' else len(src))
    section = '\n'.join(src[s:e])
    body_md, notes = transform(section)
    body_html = pandoc_html(body_md)
    entries = []
    def tag(m):
        tg, inner = m.group(1), m.group(2)
        text = re.sub(r'<[^>]+>', '', inner)
        if tg == 'h2':
            sid = f'sukta{len(entries)+1}'
            mm = re.search(r'S[ūu]kta\s+(\d+)\s+—\s+["“]?([^"”(]+)', text)
            short = f"Sūkta {mm.group(1)} · {mm.group(2).strip()}" if mm else text
            entries.append((sid, short, []))
            return f'<h2 class="sukta" id="{sid}" data-short="{html.escape(short)}">{inner}</h2>'
        rid = f'{entries[-1][0]}r{len(entries[-1][2])+1}'
        rl = re.sub(r'\s*\(.*$', '', re.sub(r'\s*pp\..*$', '', text)).strip()
        entries[-1][2].append((rid, rl))
        return f'<h3 id="{rid}">{inner}</h3>'
    body_html = re.sub(r'<(h2|h3)[^>]*>(.*?)</\1>', tag, body_html, flags=re.S)
    suktas = entries
    doc = f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>Ṛgveda-saṃhitā, Volume {vol}</title><link rel="stylesheet" href="style.css"></head><body>
{front_matter(vol, "Maṇḍala 1 · Sūktas 20–32 · Second Adhyāya of the First Aṣṭaka", entries)}
{body_html}
{notes_appendix(notes)}
</body></html>'''
    out = PUB / "out"; out.mkdir(exist_ok=True)
    (out / f"vol{vol}_{mode}.html").write_text(doc, encoding='utf-8')
    HTML(string=doc, base_url=str(PUB)).write_pdf(out / f"vol{vol}_{mode}.pdf")
    print(f"notes: {len(notes)}; sūktas: {len(suktas)}; wrote out/vol{vol}_{mode}.pdf")

if __name__ == '__main__':
    build(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else 'full')
