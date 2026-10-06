#!/usr/bin/env python3
"""Clean the Volume 2 working draft for publication -> work/vol2_clean.md + work/vol2_audit.md"""
import re, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "Rigveda_Samhita_Vol2_English_Translation.md"
OUT = pathlib.Path(__file__).resolve().parent / "work"; OUT.mkdir(exist_ok=True)
audit = []
def log(kind, ln, text):
    audit.append(f"- **{kind}** (draft line {ln}): {text[:240].replace(chr(10), ' ')}{'…' if len(text) > 240 else ''}")

SUKTA3 = '## ॥ ಮೂರನೆಯ ಸೂಕ್ತವು ॥ — Sūkta 3 — "aśvinā yajñavīriṇaḥ" ("The Third Sūkta")'
def clean():
    text = SRC.read_text(encoding='utf-8')
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

    out, seen_pref, cut_tail = [], False, False
    for ln, blk in blocks:
        first = blk.split('\n', 1)[0]
        if not seen_pref:
            if first.startswith("## Translator's Preface"): seen_pref = True
            else: log('removed (draft header)', ln, blk); continue
        if re.match(r'\*\*Progress note — printed page 808', blk): cut_tail = True
        if cut_tail: log('removed (closing progress note / open flags)', ln, blk); continue
        if blk.strip() == '---': continue
        if blk.startswith('*(The scan ends here'): log('removed (scan-end remark)', ln, blk); continue
        if re.match(r'\*\*(Progress|Target for next session)', blk):
            log('removed (progress / target)', ln, blk); continue
        if re.match(r'\*\((Printed p\. \d+ then continues|A printed ornament follows)', blk):
            log('removed (next-sūkta working remark)', ln, blk); continue
        m = re.match(r'^(\*\*End of Sūkta \d+\.\*\*) \*\(.*\)\*\s*$', blk, flags=re.S)
        if m:
            log('trimmed (next-sūkta working remark)', ln, blk); out.append(m.group(1)); continue
        # page headings -> markers
        m = re.match(r'^### Pages? ([\d–\-]+)(?: \(lower half\))?(?: — (.*))?$', first)
        if m:
            pg, title = m.group(1), (m.group(2) or '').strip()
            out.append(f'<div class="pgmark">original p{"p" if "–" in pg or "-" in pg else ""}. {pg}</div>')
            if title and not title.startswith('[') and not re.match(r'^opening of Sūkta', title):
                out.append('### ' + title)
            rest = blk.split('\n', 1)[1] if '\n' in blk else ''
            if rest.strip(): out.append(rest)
            if title.startswith('[Maṇḍala 1, Adhyāya 1, Sūkta 3]'): out.insert(len(out) - 1, SUKTA3)
            continue
        # bold sūkta title lines (Sūktas 8–13) -> h2
        m = re.match(r'^\*\*(॥ [^\n]*— Sūkta (\d+) — [^\n]*)\*\*\s*$', blk)
        if m and int(m.group(2)) in (8, 9, 10, 11, 12, 13):
            out.append('## ' + m.group(1)); log('converted to heading', ln, blk); continue
        if first.startswith('# Part II — Saṃhitā Text, Continued'):
            out.append('# The Ṛgveda Saṃhitā — Maṇḍala 1, Sūktas 3–19'); out.append('## Opening Invocation and Introduction to the Saṃhitā'); continue
        blk = blk.replace(' in a later session', '').replace('in this batch', 'in this volume').replace('in this section of the volume', 'in this volume')
        blk = re.sub(r'^## Table of Contents \(Vishayanukramanike\) — Roadmap for This Volume', '## Table of Contents (Vishayanukramanike) of the Original Edition', blk)
        out.append(blk)
    # Sūkta 3 heading: if the page-2 heading was dropped before insertion
    md = '\n\n'.join(out) + '\n'
    from lighten import lighten
    md = lighten(md)
    (OUT / 'vol2_clean.md').write_text(md, encoding='utf-8')
    (OUT / 'vol2_audit.md').write_text('# Volume 2 cleaning audit\n\n' + '\n'.join(audit) + '\n', encoding='utf-8')
    print(len(blocks), 'blocks in;', len(out), 'out;', len(audit), 'audit entries')
if __name__ == '__main__': clean()
