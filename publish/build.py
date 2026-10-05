#!/usr/bin/env python3
"""Build a print PDF from a volume's working .md.  Pilot: python3 build.py 3 pilot
Never edits the source .md; all transformation happens in memory / build files."""
import re, subprocess, sys, html, pathlib
import pypandoc
import voice
from weasyprint import HTML

ROOT = pathlib.Path(__file__).resolve().parent.parent
PUB = ROOT / "publish"
NOTE_RE = re.compile(r'^\*\((.+)\)\*\s*$', re.S)   # standalone italic parenthetical = translator's note
H3_RE = re.compile(r'^###\s+Pages?\s+([\d–\-]+)\s+—\s+(S[ūu]kta\s+\d+),\s*(Rik\s+\d+)(.*)$')
CHAPTER_RE = re.compile(r'^##\s+(.*)$')


FN_STORE = []          # note bodies; markdown carries only a placeholder token
LONG_NOTE = 900        # longer remarks stay on the page as small-type note blocks, not page-foot footnotes

def make_ref(body):
    FN_STORE.append(body)
    return f'QQFN{len(FN_STORE)-1}QQ'

PAGEREF_RE = re.compile(r'^(?:pp?\.)\s*[\d–\-, ]+(?:\s*lower half[^;]*)?$')
INLINE_RE = re.compile(r'(?<!\*)\*\((.+?)\)\*(?!\*)')
MINE_RE = re.compile(r'\*\*(Translation|Translation of [^*]*?) \((mine[^)]*)\):\*\*')

def fix_stars(body):
    """Notes written as *( … )* with inner * toggles: after the outer italics are stripped an odd number of
    asterisks remain; the segments between toggles were roman-in-italic (emphasised words) -> render them italic."""
    body = voice.fix(body)
    if '*' in body:
        parts = body.split('*')
        def emph(p):
            core = p.strip()
            return p[:len(p)-len(p.lstrip())] + (f'*{core}*' if core else '') + p[len(p.rstrip()):]
        body = ''.join(emph(p) if i % 2 else p for i, p in enumerate(parts))
    return voice.fix(body)

def inline_notes(blk, notes, rik_label, seen):
    """Turn inline *( … )* remarks into footnotes; bare source page-references are dropped
    (they are recorded in the Rik headings); exact repeats within a Sūkta are footnoted once."""
    if blk.lstrip().startswith(('>', '#', '|')):
        return blk
    def sub(m):
        body = fix_stars(m.group(1).strip())
        if PAGEREF_RE.match(body):
            return ''
        body = re.sub(r'^pp?\.\s*[\d–\-, ]+(?:\s*lower half[^;]*)?;\s*', '', body)   # leading page ref
        if body in seen:
            return ''
        seen.add(body)
        notes.append((rik_label, body))
        return make_ref(body)
    blk = INLINE_RE.sub(sub, blk)
    def mine(m):
        body = m.group(2)
        if body in seen: return f'**{m.group(1)}:**'
        full = voice.fix(body[0].upper()+body[1:] + '.')
        seen.add(body); notes.append((rik_label, full))
        return f'**{m.group(1)}:**' + make_ref(full)
    blk = MINE_RE.sub(mine, blk)
    return re.sub(r'[ \t]+\n', '\n', blk)

def split_blocks(text):
    text = re.sub(r'(?<!\n)\n(?=#{1,6} )', '\n\n', text)   # a heading always starts its own block
    return [b for b in re.split(r'\n{2,}', text.strip('\n'))]

def transform(md):
    """Return (markdown_with_footnotes, notes_by_rik) from raw section markdown."""
    out, notes, rik_label, sukta_label = [], [], "Sūkta introduction", ""
    seen = set()
    for blk in split_blocks(md):
        first = blk.split('\n', 1)[0]
        m = H3_RE.match(first)
        if m:
            pp, sukta, rik, rest = m.groups()
            rik_label = f"{sukta}, {rik}"
            out.append(f'### {rik}{rest} <span class="pp">pp. {pp}</span>')
            continue
        if first.startswith('## '):
            seen.clear()
            sukta_label = re.sub(r'\*', '', first[3:])
            m2 = re.search(r'S[ūu]kta\s+(\d+)', first)
            rik_label = f"Sūkta {m2.group(1)}, introduction" if m2 else rik_label
            out.append(blk); continue
        if blk.startswith('*(Printed'):
            out.append(blk); continue
        nm = NOTE_RE.match(blk.replace('\n', ' '))
        if nm and out and not out[-1].startswith('#') and not blk.startswith('*(Printed'):
            body = fix_stars(nm.group(1).strip())
            notes.append((rik_label, body))
            if len(body) > LONG_NOTE:
                out.append(make_ref(body))
            else:
                out[-1] = out[-1].rstrip() + ' ' + make_ref(body)
            continue
        out.append(inline_notes(blk, notes, rik_label, seen))
    return '\n\n'.join(out), notes

def notes_appendix(notes):
    by = {}
    for lab, body in notes: by.setdefault(lab, []).append(body)
    parts = ['<h1 class="appendix" id="notes">Collected Notes</h1>',
             '<p style="text-align:center;font-style:italic">Every translator’s note and editorial remark of this volume, gathered by Sūkta and Rik.</p>',
             '<div class="notes-app">']
    cur = None
    for lab, bodies in by.items():
        parts.append(f'<h3>{html.escape(lab)}</h3>')
        for b in bodies:
            sk = lab.split(',')[0]
            if sk != cur: cur, n = sk, 0
            islong = len(b) > LONG_NOTE
            if not islong: n += 1
            inline = pypandoc.convert_text(b, 'html', format='markdown-smart').replace('<p>', '').replace('</p>', '')
            parts.append(f'<p><b>{"¶" if islong else str(n)+"."}</b> {inline}</p>')
    parts.append('</div>')
    return '\n'.join(parts)

def resolve_refs(htm):
    def one(m):
        body = FN_STORE[int(m.group(1))]
        inner = pypandoc.convert_text(body, 'html', format='markdown-smart+raw_html').strip()
        inner = re.sub(r'^<p>(.*)</p>$', r'\1', inner, flags=re.S)
        if len(body) > LONG_NOTE:      # inline inside a paragraph: small-type note
            return f'<span class="longnote">{inner}</span>'
        return f'<span class="fn">{inner}</span>'
    return re.sub(r'QQFN(\d+)QQ', one, htm)

def pandoc_html(md):
    return pypandoc.convert_text(md, 'html', format='markdown-smart+raw_html',
                                 extra_args=['--lua-filter', str(PUB / 'notes.lua'), '--wrap=none'])

def front_matter(vol, vtitle, entries, cover='cover_vol3.jpg', toc_html=None):
    """entries: list of (sukta_id, short_label, [(rik_id, rik_label), ...])"""
    toc = []
    for sid, lab, riks in entries:
        toc.append(f'<li class="su"><a href="#{sid}">{html.escape(lab)}</a></li>')
        if riks:
            toc.append('<li class="rl"><ul class="riks">' + ''.join(
                f'<li><a href="#{rid}">{html.escape(rl)}</a></li>' for rid, rl in riks) + '</ul></li>')
    toc = '\n'.join(toc)
    toc_block = toc_html or ('<section class="toc"><h2>Contents</h2><p class="tocsub">Sūkta by Sūkta, and Rik by Rik</p><ul>' + toc + '<li class="su"><a href="#notes">Collected Notes</a></li></ul></section>')
    return f'''
<section class="cover"><img src="assets/{cover}" alt="Original Kannada cover">
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
<section class="portrait"><h2>Patron of the First Edition</h2>
 <img class="pic" src="assets/maharaja.jpg" alt="Maharaja of Mysore">
 <p class="cap2">His Highness Śrī Jayacāmarājendra Wadiyar Bahadur, G.C.B., G.C.S.I.,<br>Maharaja of Mysore, by whose gracious permission the original edition was published.</p></section>
<section class="portrait"><h2>Guru &amp; President of the Board of Scholars</h2>
 <img class="pic" src="assets/guruji.jpg" alt="Guruji">
 <p class="cap2">Śrī Jagadguru Nāgaliṅga-parivrājakācārya-pīṭhādhyakṣa<br>Śilpasiddhānti Śivayogi Śrī Siddhaliṅga Svāmigaḷavaru,<br>President of the Veda-vimarśana Vidvan-maṇḍali</p></section>
<section class="portrait pair"><h2>The Present Day</h2>
 <div class="placeholder half">[Portrait of the present Maharaja — to be supplied]<br><br>[Name, title and caption]</div>
 <div class="placeholder half">[Portrait of the present Guruji — to be supplied]<br><br>[Name, title and caption]</div></section>
{toc_block}
'''

def build(vol, mode):
    src = (ROOT / f"Rigveda_Samhita_Vol{vol}_English_Translation.md").read_text(encoding='utf-8').split('\n')
    heads = [i for i, l in enumerate(src) if l.startswith('## ') and re.search(r'S[ūu]kta\s+\d+', l)]
    s, e = heads[0], (heads[1] if mode == 'pilot' else len(src))
    section = '\n'.join(src[s:e])
    body_md, notes = transform(section)
    body_html = resolve_refs(pandoc_html(body_md))
    entries = []
    def tag(m):
        tg, inner = m.group(1), m.group(2)
        text = re.sub(r'<[^>]+>', '', inner)
        if tg == 'h2':
            sid = f'sukta{len(entries)+1}'
            mm = re.search(r'S[ūu]kta\s+(\d+)\s+—\s+["“]?([^"”(]+)', text)
            short = f"Sūkta {mm.group(1)} · {mm.group(2).strip()}" if mm else text
            entries.append((sid, short, []))
            cls = 'sukta first' if not entries[:-1] else 'sukta'
            return f'<h2 class="{cls}" id="{sid}" data-short="{html.escape(short)}">{inner}</h2>'
        h3n = getattr(tag, 'n', 0) + 1; tag.n = h3n
        rid = f'{entries[-1][0]}h{h3n}'
        rl = re.sub(r'\s*\(.*$', '', re.sub(r'\s*pp\..*$', '', text)).strip()
        if re.fullmatch(r'Rik\s+\d+', rl):
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
