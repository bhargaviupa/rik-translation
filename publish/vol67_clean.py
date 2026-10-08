#!/usr/bin/env python3
"""Clean Volume 6 / Volume 7 working drafts for publication.  python3 vol67_clean.py 6|7"""
import re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = pathlib.Path(__file__).resolve().parent / "work"; OUT.mkdir(exist_ok=True)
ADH = {6: 'The Fifth Adhyāya of the First Aṣṭaka', 7: 'The Sixth Adhyāya of the First Aṣṭaka'}
SAM = re.compile(r'^\*\*(?:॥ संहिता(?:पाठः|खण्डः) ॥ — )?Saṃhitā')

def clean(vol):
    audit = []
    def log(kind, ln, text): audit.append(f"- **{kind}** (draft line {ln}): {text[:240].replace(chr(10), ' ')}{'…' if len(text) > 240 else ''}")
    text = (ROOT / f"Rigveda_Samhita_Vol{vol}_English_Translation.md").read_text(encoding='utf-8')
    incipit = {int(n): re.sub(r'\s+', ' ', re.sub(r'[*­\[\]?]', '', w)).strip() for n, w in re.findall(r'(?m)^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*\d+\s*\|\s*$', text)}
    i = text.rfind('**Progress note')
    if i > 0: text = text[:i]; log('removed (trailing progress note)', 0, '')
    text = re.sub(r'(?<!\n)\n(?=#{1,6} )', '\n\n', text)
    text = re.sub(r'(?m)^(#{1,6} .*)\n(?!\n)', r'\1\n\n', text)
    blocks, cur, start = [], [], 1
    for ln, l in enumerate(text.split('\n'), 1):
        if l.strip() == '':
            if cur: blocks.append((start, '\n'.join(cur))); cur = []
        else:
            if not cur: start = ln
            cur.append(l)
    if cur: blocks.append((start, '\n'.join(cur)))
    out, started, cur_s, rik, explicit = [], False, None, 0, False
    for ln, blk in blocks:
        first = blk.split('\n', 1)[0]; rest = blk.split('\n', 1)[1] if '\n' in blk else ''
        if not started:
            if first.startswith('## ॥') or first.startswith('## ಪೀಠಿಕೆ'):
                started = True
            else: log('removed (draft header / contents table)', ln, blk); continue
        if first.startswith('## ಪೀಠಿಕೆ'):
            out.append('# Pīṭhike — Preface of H. P. Venkata Rao'); log('converted heading', ln, first); continue
        if first.startswith('## ॥'):
            out.append('# ' + ADH[vol])
            if vol == 7: out.append('## Sūkta 81 — "%s"' % incipit.get(81, '')); cur_s = 81
            continue
        if blk.strip() == '---': continue
        if blk.startswith('*(Running head') or blk.startswith('*(Translated at the user'):
            log('removed (working remark)', ln, blk); continue
        m = re.match(r'^## (?:SŪKTA|Sūkta) (\d+)\b', first)
        if not m:
            m2 = re.match(r'^\*\*[^*]*— Sūkta (\d+)\*\*', first)
            if m2 and cur_s and int(m2.group(1)) == cur_s + 1: m = m2; blk = '## Sūkta %s' % m2.group(1) + ('\n' + rest if rest else ''); first = blk.split('\n',1)[0]
        if m:
            n = int(m.group(1)); cur_s = n; rik = 0; explicit = False
            out.append(f'## Sūkta {n} — "{incipit.get(n, "")}"' if incipit.get(n) else f'## Sūkta {n}')
            pg = re.search(r'printed pp?\. (\d+)', first)
            if pg: out.append(f'<div class="pgmark">original p. {pg.group(1)}</div>')
            if rest.strip(): out.append(rest)
            continue
        m = re.match(r'^#{3,4} (?:Sūkta \d+, )?Rik (\d+)(?:\.(\d+))?(?: \(([^)]*)\))?', first)
        if m:
            rk = int(m.group(2) or m.group(1))
            if rk != rik:
                rik = rk; out.append(f'### Rik {rk}')
            explicit = True
            if rest.strip(): out.append(rest)
            continue
        m = re.match(r'^### Pages? (\w+)(?:–\w+)?(?: \(PDF [^)]*\))?(.*)$', first)
        if m:
            out.append(f'<div class="pgmark">original p. {m.group(1)}</div>')
            tail = m.group(2)
            if re.search(r'SOURCE PAGE MISSING|mis-placed', tail):
                out.append('*(' + re.sub(r'[*]', '', tail).strip(' —') + ')*')
            if rest.strip(): out.append(rest)
            continue
        if first.startswith('### (continued'): continue
        if SAM.match(first) and not re.search(r'Rik \d+\.\d+,? ?\(?(?:concluded|continued)', first) and 'Saṃhitā text (concluded' not in first:
            m = re.search(r'Rik (\d+)\.(\d+)', first)
            rk = int(m.group(2)) if m else (rik if explicit else rik + 1)
            if rk != rik:
                rik = rk; out.append(f'### Rik {rk}')
            explicit = False
        out.append(blk)
    md = '\n\n'.join(out) + '\n'
    (OUT / f'vol{vol}_clean.md').write_text(md, encoding='utf-8')
    (OUT / f'vol{vol}_audit.md').write_text(f'# Volume {vol} cleaning audit\n\n' + '\n'.join(audit) + '\n', encoding='utf-8')
    print(f'vol{vol}:', len(blocks), 'blocks in;', len(out), 'out; incipits:', len(incipit))
if __name__ == '__main__': clean(int(sys.argv[1]))
