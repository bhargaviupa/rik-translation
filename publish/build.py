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

def front_matter(vol, vtitle, suktas):
    toc = '\n'.join(f'<li><a href="#{sid}">{html.escape(t)}</a></li>' for sid, t in suktas)
    return f'''
<section class="halftitle">Ṛgveda-saṃhitā</section>
<section class="titlepage">
  <div class="inv dev">॥ श्री महागणाधिपतये नमः ॥</div>
  <h1>Ṛgveda-saṃhitā</h1>
  <div class="sub">with the Bhāṣya of Sāyaṇācārya<br>and the Kannada Commentary of H. P. Venkata Rao</div>
  <div class="orn">❖</div>
  <div style="font-size:15pt;letter-spacing:.1em">VOLUME {vol}</div>
  <div class="sub" style="margin-top:.2in">{vtitle}</div>
  <div class="orn">❖</div>
  <div class="who">English Translation<br><i>[Translator’s name — to be supplied]</i><br><br>
  Originally published under the patronage of<br>His Highness Śrī Jayacāmarājendra Wadiyar Bahadur, Maharaja of Mysore<br>
  Śrī Jayacāmarājendra Vedaratna-mālā · Mysore, 1949</div>
</section>
<section class="copyright"><p><i>[Copyright, permissions and AI-assistance statement — wording to be supplied.]</i></p>
<p>Translation of the Kannada edition of 1949, <i>Ṛgveda-saṃhitā with the Sāyaṇa-bhāṣya</i>, edited and translated by Asthāna Mahāvidvān H. P. Venkata Rao, Mysore.</p></section>
<section class="creditspage"><h2>Frontispiece &amp; Benedictions</h2>
 <div class="placeholder">[Portrait of the present Maharaja — to be supplied]</div>
 <div class="placeholder">[Portrait of the present Guruji — to be supplied]</div></section>
<section class="toc"><h2>Contents</h2><ul>{toc}<li><a href="#notes">Collected Notes</a></li></ul></section>
'''

def build(vol, mode):
    src = (ROOT / f"Rigveda_Samhita_Vol{vol}_English_Translation.md").read_text(encoding='utf-8').split('\n')
    heads = [i for i, l in enumerate(src) if l.startswith('## ') and re.search(r'S[ūu]kta\s+\d+', l)]
    s, e = heads[0], (heads[1] if mode == 'pilot' else len(src))
    section = '\n'.join(src[s:e])
    body_md, notes = transform(section)
    body_html = pandoc_html(body_md)
    # give each sūkta heading an id + class
    suktas = []
    def tag(m):
        sid = f'sukta{len(suktas)+1}'
        text = re.sub(r'<[^>]+>', '', m.group(1))
        mm = re.search(r'S[ūu]kta\s+(\d+)\s+—\s+["“]?([^"”(]+)', text)
        short = f"Sūkta {mm.group(1)} · {mm.group(2).strip()}" if mm else text
        suktas.append((sid, short))
        return f'<h2 class="sukta" id="{sid}" data-short="{html.escape(short)}">{m.group(1)}</h2>'
    body_html = re.sub(r'<h2[^>]*>(.*?)</h2>', tag, body_html, flags=re.S)
    doc = f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>Ṛgveda-saṃhitā, Volume {vol}</title><link rel="stylesheet" href="style.css"></head><body>
{front_matter(vol, "Maṇḍala 1 · Sūktas 20–32 · Second Adhyāya of the First Aṣṭaka", suktas)}
{body_html}
{notes_appendix(notes)}
</body></html>'''
    out = PUB / "out"; out.mkdir(exist_ok=True)
    (out / f"vol{vol}_{mode}.html").write_text(doc, encoding='utf-8')
    HTML(string=doc, base_url=str(PUB)).write_pdf(out / f"vol{vol}_{mode}.pdf")
    print(f"notes: {len(notes)}; sūktas: {len(suktas)}; wrote out/vol{vol}_{mode}.pdf")

if __name__ == '__main__':
    build(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else 'full')
