#!/usr/bin/env python3
"""Clean Volume 4 / Volume 5 working drafts for publication.  python3 vol45_clean.py 4|5"""
import re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = pathlib.Path(__file__).resolve().parent / "work"; OUT.mkdir(exist_ok=True)
ADH = {4: ('तृतीयो', 'The Third Adhyāya of the First Aṣṭaka'), 5: ('चतुर्थो', 'The Fourth Adhyāya of the First Aṣṭaka')}

def clean(vol):
    audit = []
    def log(kind, ln, text): audit.append(f"- **{kind}** (draft line {ln}): {text[:240].replace(chr(10), ' ')}{'…' if len(text) > 240 else ''}")
    text = (ROOT / f"Rigveda_Samhita_Vol{vol}_English_Translation.md").read_text(encoding='utf-8')
    incipit = {int(n): re.sub(r'\s+', ' ', re.sub(r'[*\u00ad]', '', w)).strip() for n, w in re.findall(r'(?m)^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*[^|]*\|\s*$', text)}
    text = re.sub(r'(?<!\n)\n(?=#{1,6} )', '\n\n', text)
    text = re.sub(r'(?m)^(#{1,6} .*)\n(?!\n)', r'\1\n\n', text)
    blocks, cur, start = [], [], 1
    for i, l in enumerate(text.split('\n'), 1):
        if l.strip() == '':
            if cur: blocks.append((start, '\n'.join(cur))); cur = []
        else:
            if not cur: start = i
            cur.append(l)
    if cur: blocks.append((start, '\n'.join(cur)))

    word, adh_title = ADH[vol]
    out, started, cut_tail, skip_sec, cur_s = [], False, False, False, None
    for ln, blk in blocks:
        first = blk.split('\n', 1)[0]
        if not started:
            if first.startswith('## ॥ ' + word):
                started = True; out.append('# ' + adh_title); continue
            log('removed (draft header / contents table)', ln, blk); continue
        if re.match(r'\*\*(Summary of Volume 4|Progress note — Volume)', blk): cut_tail = True
        if cut_tail: log('removed (closing summary / progress / open flags)', ln, blk); continue
        if blk.strip() == '---': continue
        if skip_sec:
            if first.startswith('#'): skip_sec = False
            else: log('removed (inside working section)', ln, blk); continue
        if first.startswith("## END OF THE USER'S REQUESTED RANGE"):
            skip_sec = True; log('removed (working marker)', ln, first); continue
        if re.match(r'\*\*Beginning of Sūkta \d+ \(identification only', blk) or 'next batch' in blk and blk.startswith('*('):
            log('removed (next-sūkta / next-batch working remark)', ln, blk); continue
        # PARIŚIṢṬA part opener (Vol 5)
        if first.startswith('## PARIŚIṢṬA'):
            out.append('# Pariśiṣṭa — Appendix on the Deities and Persons of the Ṛgveda'); log('converted to part heading', ln, first); continue
        # Sūkta headings
        m = re.match(r'^## SŪKTA (\d+)\b(.*)$', first)
        if m:
            n = int(m.group(1)); cur_s = n; ann = m.group(2)
            pg = re.search(r'printed p\. (\d+)', ann)
            sub = re.sub(r'printed p\.[^;)]*?(?:PDF[^;)]*)?[;)]', '', ann)
            sub = re.sub(r'\(?printed p\. [^,;)]*(?:,|;)?\s*(?:PDF [^;)]*)?\)?', '', ann).strip(' *()—-;, ')
            sub = re.sub(r'^\s*[–—-]\s*', '', sub).strip(' *()—-;, ')
            title = f'## Sūkta {n} — "{incipit.get(n, "")}"' if incipit.get(n) else f'## Sūkta {n}'
            out.append(title)
            if pg: out.append(f'<div class="pgmark">original p. {pg.group(1)}</div>')
            if sub: out.append(f'*({sub[0].upper() + sub[1:]}.)*')
            rest = blk.split('\n', 1)[1] if '\n' in blk else ''
            if rest.strip(): out.append(rest)
            continue
        # Rik headings
        m = re.match(r'^### Rik (\d+)\.(\d+)(?: \(([^)]*)\))?(.*)$', first)
        if m:
            sn, rk, par, tail = m.group(1), m.group(2), m.group(3) or '', m.group(4).strip()
            pg = re.search(r'pp?\. ?(\d+)(?:–(\d+))?', par)
            if pg:
                out.append(f'<div class="pgmark">original p{"p" if pg.group(2) else ""}. {pg.group(1)}{"–" + pg.group(2) if pg.group(2) else ""}</div>')
            extra = re.search(r';\s*(metre [^;)]*)', par)
            h = f'### Rik {rk}' if int(sn) == cur_s else f'### Rik {sn}.{rk}'
            if tail: h += ' ' + tail
            if extra: h += f' — {extra.group(1)}'
            out.append(h)
            rest = blk.split('\n', 1)[1] if '\n' in blk else ''
            if rest.strip(): out.append(rest)
            continue
        # page headings
        m = re.match(r'^### (?:Page|Printed p\.) (\d+)(?: lower half)?(?: \(PDF [^)]*\))?(?: [—–-] (.*))?$', first)
        if m:
            out.append(f'<div class="pgmark">original p. {m.group(1)}</div>')
            title = (m.group(2) or '').strip()
            if title and not title.startswith('[') and not re.match(r'^opening of', title): out.append('### ' + title)
            rest = blk.split('\n', 1)[1] if '\n' in blk else ''
            if rest.strip(): out.append(rest)
            continue
        blk = blk.replace(' (my note)', '').replace('(my note)', '')
        if blk.startswith('**Correction to the heading of Sūkta 43'):
            out.append('*(' + blk.replace('\n', ' ').replace('**', '') + ')*'); log('converted to note (correction)', ln, blk); continue
        out.append(blk)
    md = '\n\n'.join(out) + '\n'
    (OUT / f'vol{vol}_clean.md').write_text(md, encoding='utf-8')
    (OUT / f'vol{vol}_audit.md').write_text(f'# Volume {vol} cleaning audit\n\n' + '\n'.join(audit) + '\n', encoding='utf-8')
    print(f'vol{vol}:', len(blocks), 'blocks in;', len(out), 'out;', len(audit), 'audit entries; incipits found:', len(incipit))
    return incipit

if __name__ == '__main__': clean(int(sys.argv[1]))
