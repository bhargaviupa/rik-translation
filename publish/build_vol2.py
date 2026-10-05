#!/usr/bin/env python3
"""Volume 2 print build.  python3 build_vol2.py [pilot|full]"""
import re, sys, html, pathlib
import pypandoc
from weasyprint import HTML
import build as B
import vol2_clean

PUB = B.PUB
PLAIN_NO = re.compile(r'^(#|<|>|\s*[-*] |\d+\. |\||:::)')
ORD = {w: i for i, w in enumerate('First Second Third Fourth Fifth Sixth Seventh Eighth Ninth Tenth Eleventh Twelfth Thirteenth Fourteenth'.split(), 1)}
EXPECTED = {3:12,4:10,5:10,6:10,7:10,8:10,9:10,10:12,11:8,12:12,13:12,14:12,15:12,16:9,17:9,18:9,19:9}

def short_label(title):
    t = re.sub(r'[*`]', '', title).strip()
    t = t.split(' — ')[0] if ' — ' in t and len(t.split(' — ')[0]) > 8 else t
    if len(t) > 58: t = t[:55].rsplit(' ', 1)[0] + '…'
    return t.replace(',', ';')

def transform(md):
    out, notes, seen, label = [], [], set(), 'Translator’s Preface'
    for blk in B.split_blocks(md):
        first = blk.split('\n', 1)[0]
        if first.startswith('# ') or first.startswith('## '):
            m = re.search(r'S[ūu]kta\s+(\d+)', first)
            label = f'Sūkta {m.group(1)}' if m and first.startswith('## ') else short_label(first.lstrip('# '))
            seen.clear(); out.append(blk); continue
        if first.startswith('#') or first.startswith('<'):
            out.append(blk); continue
        nm = B.NOTE_RE.match(blk.replace('\n', ' '))
        if nm:
            body = B.fix_stars(nm.group(1).strip())
            if body in seen: continue
            seen.add(body); notes.append((label, body))
            ref = B.make_ref(body)
            j = next((k for k in range(len(out) - 1, max(len(out) - 5, -1), -1) if not PLAIN_NO.match(out[k])), None)
            if j is not None: out[j] = out[j].rstrip() + ' ' + ref
            else: out.append(ref)
            continue
        out.append(B.inline_notes(blk, notes, label, seen))
    return '\n\n'.join(out), notes

def rik_of(text, cur):
    t = re.sub(r'<[^>]+>', '', text)
    m = re.search(r'S[ūu]kta (\d+),? Rik (\d+)', t)
    if m: return int(m.group(1)), int(m.group(2))
    m = re.search(r'S[ūu]kta (\d+),? The (\w+) Mantra', t)
    if m and m.group(2) in ORD: return int(m.group(1)), ORD[m.group(2)]
    m = re.search(r'\bRik (\d+)\.(\d+)', t)
    if m: return int(m.group(1)), int(m.group(2))
    m = re.match(r'\s*Rik (\d+)\b', t)
    if m and cur: return cur, int(m.group(1))
    return None

def build(mode='full'):
    vol2_clean.clean()
    md = (PUB / 'work' / 'vol2_clean.md').read_text(encoding='utf-8')
    if mode == 'pilot':
        cut = md.index('# The Ṛgveda Saṃhitā'); md = md[:cut] + md[cut:cut + 60000]
    B.FN_STORE.clear()
    body_md, notes = transform(md)
    body_html = B.resolve_refs(B.pandoc_html(body_md))

    front, suktas = [], []          # front: (id,label); suktas: [id,label,sno,[(rid,'Rik n')]]
    state = {'h1': 0, 'h2': 0, 'h3': 0, 'cur': None}
    got = set()
    def tag(m):
        tg, inner = m.group(1), m.group(2)
        text = re.sub(r'<[^>]+>', '', inner).strip()
        if tg == 'h1':
            state['h1'] += 1
            return f'<h1 class="part first" id="part{state["h1"]}">{inner}</h1>'
        if tg == 'h2':
            state['h2'] += 1; cid = f'ch{state["h2"]}'
            mm = re.search(r'S[ūu]kta\s+(\d+)\s+—\s+["“]?([^"”(]+)', text)
            if mm and state['h1']:
                sno = int(mm.group(1)); state['cur'] = sno
                short = f"Sūkta {sno} · {mm.group(2).strip()}"
                suktas.append([cid, short, sno, []])
                return f'<h2 class="sukta" id="{cid}" data-short="{html.escape(short)}">{inner}</h2>'
            if state['h1']:
                state['cur'] = None
                front.append((cid, text, True))     # body chapter without sūkta number (invocation)
                return f'<h2 class="chapter" id="{cid}" data-short="{html.escape(short_label(text))}">{inner}</h2>'
            front.append((cid, text, False))
            return f'<h2 class="chapter" id="{cid}" data-short="{html.escape(short_label(text))}">{inner}</h2>'
        # h3
        state['h3'] += 1
        r = rik_of(inner, state['cur']) if state['h1'] else None
        hid = f'h{state["h3"]}'
        if r and r not in got and suktas and r[0] == suktas[-1][2]:
            got.add(r); suktas[-1][3].append((hid, f'Rik {r[1]}'))
        return f'<h3 id="{hid}">{inner}</h3>'
    body_html = re.sub(r'<(h1|h2|h3)[^>]*>(.*?)</\1>', tag, body_html, flags=re.S)
    k = body_html.index('<h1 class="part first"')
    body_html = '<div class="roman-body">' + body_html[:k] + '</div>' + body_html[k:]

    # QA: Rik counts
    bad = [(s[2], len(s[3]), EXPECTED.get(s[2])) for s in suktas if len(s[3]) != EXPECTED.get(s[2])]
    print('Rik-count check (sūkta, found, expected) mismatches:', bad)

    toc = ['<section class="toc"><h2>Contents</h2><ul class="chap">']
    for cid, lab, inbody in front:
        if not inbody: toc.append(f'<li class="ch rm"><a href="#{cid}">{html.escape(lab)}</a></li>')
    toc.append('<li class="su"><a href="#part1">The Ṛgveda Saṃhitā — Maṇḍala 1, Sūktas 3–19</a></li>')
    for cid, lab, inbody in front:
        if inbody: toc.append(f'<li class="ch"><a href="#{cid}">{html.escape(lab)}</a></li>')
    toc.append('</ul><ul>')
    for sid, short, sno, riks in suktas:
        toc.append(f'<li class="su"><a href="#{sid}">{html.escape(short)}</a></li>')
        if riks:
            toc.append('<li class="rl"><ul class="riks">' + ''.join(f'<li><a href="#{r}">{html.escape(l)}</a></li>' for r, l in riks) + '</ul></li>')
    toc.append('<li class="su"><a href="#notes">Collected Notes</a></li></ul></section>')

    doc = f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>Ṛgveda-saṃhitā, Volume 2</title><link rel="stylesheet" href="style.css"><link rel="stylesheet" href="style_vol1.css"></head><body>
{B.front_matter(2, "Maṇḍala 1 · Sūktas 3–19 · First Adhyāya of the First Aṣṭaka", [], cover='cover_vol2.jpg', toc_html=chr(10).join(toc))}
{body_html}
{B.notes_appendix(notes)}
</body></html>'''
    out = PUB / 'out'; out.mkdir(exist_ok=True)
    (out / f'vol2_{mode}.html').write_text(doc, encoding='utf-8')
    HTML(string=doc, base_url=str(PUB)).write_pdf(out / f'vol2_{mode}.pdf')
    print(f'notes: {len(notes)}; sūktas: {len(suktas)}; wrote out/vol2_{mode}.pdf')

if __name__ == '__main__':
    build(sys.argv[1] if len(sys.argv) > 1 else 'full')
