#!/usr/bin/env python3
"""Volume 4 / 5 print build.  python3 build_vol45.py 4|5 [pilot|full]"""
import re, sys, html, pathlib
from weasyprint import HTML
import build as B
import vol45_clean, vol67_clean, voice

PUB = B.PUB
PLAIN_NO = re.compile(r'^(#|<|>|\s*[-*] |\d+\. |\||:::)')
CFG = {
 4: dict(title='Maṇḍala 1 · Sūktas 33–46 · Third Adhyāya of the First Aṣṭaka', cover='cover_vol4.jpg',
         expected={33:15,34:12,35:11,36:20,37:15,38:15,39:10,40:8,41:9,42:10,43:9,44:14,45:10,46:15}),
 5: dict(title='Maṇḍala 1 · Sūktas 47–61 and the Pariśiṣṭa · Fourth Adhyāya of the First Aṣṭaka', cover='cover_vol5.jpg',
         expected={47:10,48:16,49:4,50:13,51:15,52:15,53:11,54:11,55:8,56:6,57:6,58:9,59:7,60:5,61:16}),

 6: dict(title='Maṇḍala 1 · Sūktas 62–80 · Fifth Adhyāya of the First Aṣṭaka', cover='cover_vol6.jpg',
         expected={62:13,63:9,64:15,65:5,66:5,67:5,68:5,69:5,70:6,71:10,72:10,73:10,74:9,75:5,76:5,77:5,78:5,79:12,80:16}),
 7: dict(title='Maṇḍala 1 · Sūktas 81–94 · Sixth Adhyāya of the First Aṣṭaka', cover='cover_vol7.jpg',
         expected={81:9,82:6,83:6,84:20,85:12,86:10,87:6,88:6,89:10,90:9,91:23,92:18,93:12,94:16}),
}

def short_label(title):
    t = re.sub(r'[*`]', '', title).strip()
    t = t.split(' — ')[0] if ' — ' in t and len(t.split(' — ')[0]) > 8 else t
    if len(t) > 58: t = t[:55].rsplit(' ', 1)[0] + '…'
    return t.replace(',', ';')

def transform(md):
    out, notes, seen, label = [], [], set(), 'Introduction'
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
    t = re.sub(r'<[^>]+>', '', text).strip()
    m = re.match(r'Rik (\d+)\.(\d+)\b', t)
    if m: return int(m.group(1)), int(m.group(2))
    m = re.match(r'Rik (\d+)\b', t)
    if m and cur: return cur, int(m.group(1))
    return None

def build(vol, mode='full'):
    cfg = CFG[vol]
    (vol67_clean if vol >= 6 else vol45_clean).clean(vol)
    md = (PUB / 'work' / f'vol{vol}_clean.md').read_text(encoding='utf-8')
    if mode == 'pilot': md = md[:50000]
    B.FN_STORE.clear()
    body_md, notes = transform(md)
    body_html = B.resolve_refs(B.pandoc_html(body_md))

    parts, state, got = [], {'h2': 0, 'h3': 0, 'cur': None}, set()
    def tag(m):
        tg, inner = m.group(1), m.group(2)
        text = re.sub(r'<[^>]+>', '', inner).strip()
        if tg == 'h1':
            pid = f'part{len(parts)+1}'
            cls = 'part first' if not parts else 'part'
            parts.append([pid, text, []])          # [id,label,items]; items: ('s',id,short,sno,riks) or ('c',id,label)
            return f'<h1 class="{cls}" id="{pid}">{inner}</h1>'
        if tg == 'h2':
            state['h2'] += 1; cid = f'ch{state["h2"]}'
            mm = re.match(r'S[ūu]kta\s+(\d+)\s+—\s+["“]?([^"”]+)', text)
            if mm:
                sno = int(mm.group(1)); state['cur'] = sno
                short = f"Sūkta {sno} · {mm.group(2).strip()}"
                parts[-1][2].append(['s', cid, short, sno, []])
                return f'<h2 class="sukta" id="{cid}" data-short="{html.escape(short)}">{inner}</h2>'
            state['cur'] = None
            parts[-1][2].append(['c', cid, text])
            return f'<h2 class="chapter" id="{cid}" data-short="{html.escape(short_label(text))}">{inner}</h2>'
        state['h3'] += 1; hid = f'h{state["h3"]}'
        r = rik_of(inner, state['cur'])
        items = parts[-1][2]
        if r and r not in got and items and items[-1][0] == 's' and r[0] == items[-1][3]:
            got.add(r); items[-1][4].append((hid, f'Rik {r[1]}'))
        return f'<h3 id="{hid}">{inner}</h3>'
    body_html = re.sub(r'<(h1|h2|h3)[^>]*>(.*?)</\1>', tag, body_html, flags=re.S)

    suk = [it for p in parts for it in p[2] if it[0] == 's']
    bad = [(s[3], len(s[4]), cfg['expected'].get(s[3])) for s in suk if len(s[4]) != cfg['expected'].get(s[3])]
    print('Rik-count check (sūkta, found, expected) mismatches:', bad)

    toc = ['<section class="toc"><h2>Contents</h2><ul class="chap">']
    for pid, plabel, items in parts:
        toc.append(f'<li class="su"><a href="#{pid}">{html.escape(plabel)}</a></li>')
        for it in items:
            if it[0] == 'c':
                toc.append(f'<li class="ch"><a href="#{it[1]}">{html.escape(it[2])}</a></li>')
            else:
                toc.append(f'<li class="ch sk"><a href="#{it[1]}">{html.escape(it[2])}</a></li>')
                if it[4]:
                    toc.append('<li class="rl"><ul class="riks">' + ''.join(f'<li><a href="#{r}">{html.escape(l)}</a></li>' for r, l in it[4]) + '</ul></li>')
    toc.append('<li class="su"><a href="#notes">Collected Notes</a></li></ul></section>')

    res = [x for _, b in notes for x in voice.residual(b)]
    if res: print('FIRST-PERSON RESIDUAL:', len(res), res[:5])
    doc = f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>Ṛgveda-saṃhitā, Volume {vol}</title><link rel="stylesheet" href="style.css"><link rel="stylesheet" href="style_vol1.css"></head><body>
{B.front_matter(vol, cfg["title"], [], cover=cfg["cover"], toc_html=chr(10).join(toc))}
{body_html}
{B.notes_appendix(notes)}
</body></html>'''
    out = PUB / 'out'; out.mkdir(exist_ok=True)
    (out / f'vol{vol}_{mode}.html').write_text(doc, encoding='utf-8')
    HTML(string=doc, base_url=str(PUB)).write_pdf(out / f'vol{vol}_{mode}.pdf')
    print(f'notes: {len(notes)}; sūktas: {len(suk)}; wrote out/vol{vol}_{mode}.pdf')

if __name__ == '__main__':
    build(int(sys.argv[1]), sys.argv[2] if len(sys.argv) > 2 else 'full')
