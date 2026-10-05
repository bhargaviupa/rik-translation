#!/usr/bin/env python3
"""Volume 1 print build: cleaned draft -> footnotes/collected notes -> PDF.  python3 build_vol1.py [pilot|full]"""
import re, sys, html, pathlib
import pypandoc
from weasyprint import HTML
import build as B
import vol1_clean

PUB = B.PUB
PLAIN_NO = re.compile(r'^(#|<|>|\s*[-*] |\d+\. |\||:::)')

def short_label(title):
    t = re.sub(r'[*`]', '', title).strip()
    t = t.split(' — ')[0] if ' — ' in t and len(t.split(' — ')[0]) > 8 else t
    t = re.sub(r'\s+', ' ', t)
    if len(t) > 58: t = t[:55].rsplit(' ', 1)[0] + '…'
    return t.replace(',', ';')

def transform_v1(md):
    out, notes, seen = [], [], set()
    label = 'Preface'
    for blk in B.split_blocks(md):
        first = blk.split('\n', 1)[0]
        if first.startswith('# ') or first.startswith('## '):
            label = short_label(first.lstrip('# ')); seen.clear()
            out.append(blk); continue
        if first.startswith('#') or first.startswith('<'):
            out.append(blk); continue
        nm = B.NOTE_RE.match(blk.replace('\n', ' '))
        if nm:
            body = B.fix_stars(nm.group(1).strip())
            if body in seen: continue
            seen.add(body)
            notes.append((label, body))
            ref = B.make_ref(body)
            j = next((k for k in range(len(out) - 1, max(len(out) - 5, -1), -1) if not PLAIN_NO.match(out[k])), None)
            if j is not None: out[j] = out[j].rstrip() + ' ' + ref
            else: out.append(ref)
            continue
        out.append(B.inline_notes(blk, notes, label, seen))
    return '\n\n'.join(out), notes

def build(mode='full'):
    vol1_clean.clean()
    md = (PUB / 'work' / 'vol1_clean.md').read_text(encoding='utf-8')
    if mode == 'pilot':                       # Preface .. first 40 blocks of Part I
        cut = md.index('# PART I')
        md = md[:cut] + md[cut:cut + 30000]
    B.FN_STORE.clear()
    body_md, notes = transform_v1(md)
    body_html = B.resolve_refs(B.pandoc_html(body_md))

    # tag headings; build contents
    parts, cur_part, n = [], None, {'h1': 0, 'h2': 0}
    front = [[None, 'Front matter', []]]; parts_list = front
    def tag(m):
        tg, inner = m.group(1), m.group(2)
        text = re.sub(r'<[^>]+>', '', inner).strip()
        if tg == 'h1':
            n['h1'] += 1; pid = f'part{n["h1"]}'
            cls = 'part first' if n['h1'] == 1 else 'part'
            parts_list.append([pid, text, []])
            return f'<h1 class="{cls}" id="{pid}">{inner}</h1>'
        if tg == 'h2':
            n['h2'] += 1; cid = f'ch{n["h2"]}'
            parts_list[-1][2].append((cid, text))
            return f'<h2 class="chapter" id="{cid}" data-short="{html.escape(short_label(text))}">{inner}</h2>'
        return m.group(0)
    body_html = re.sub(r'<(h1|h2)[^>]*>(.*?)</\1>', tag, body_html, flags=re.S)
    # wrap the roman-paged front matter (everything before PART I)
    k = body_html.index('<h1 class="part first"')
    body_html = '<div class="roman-body">' + body_html[:k] + '</div>' + body_html[k:]

    toc = ['<section class="toc"><h2>Contents</h2><ul class="chap">']
    for pid, plabel, chs in parts_list:
        if pid:
            toc.append(f'<li class="su"><a href="#{pid}">{html.escape(plabel)}</a></li>')
        for cid, cl in chs:
            toc.append(f'<li class="ch{" rm" if not pid else ""}"><a href="#{cid}">{html.escape(cl)}</a></li>')
    toc.append('<li class="su"><a href="#notes">Collected Notes</a></li></ul></section>')
    toc_html = '\n'.join(toc)

    doc = f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>Ṛgveda-saṃhitā, Volume 1</title><link rel="stylesheet" href="style.css"><link rel="stylesheet" href="style_vol1.css"></head><body>
{B.front_matter(1, "Pūrva-pīṭhikā · Sāyaṇa’s Bhāṣya-bhūmikā · Maṇḍala 1, Sūktas 1–2", [], cover='cover_vol1.jpg', toc_html=toc_html)}
{body_html}
{B.notes_appendix(notes)}
</body></html>'''
    out = PUB / 'out'; out.mkdir(exist_ok=True)
    (out / f'vol1_{mode}.html').write_text(doc, encoding='utf-8')
    HTML(string=doc, base_url=str(PUB)).write_pdf(out / f'vol1_{mode}.pdf')
    print(f'notes: {len(notes)}; parts: {n["h1"]}; chapters: {n["h2"]}; wrote out/vol1_{mode}.pdf')

if __name__ == '__main__':
    build(sys.argv[1] if len(sys.argv) > 1 else 'full')
