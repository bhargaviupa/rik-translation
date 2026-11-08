#!/usr/bin/env python3
"""Parse the printed contents (ವಿಷಯಾನುಕ್ರಮಣಿಕೆ) of a supplied machine-read volume text into structured JSON.

  python3 publish/tools/frontmatter/contents_parse.py vol15/html/rig_15_1.md --out vol15/contents.json [--fixes vol15/contents_fixes.json] [--check]

The contents region runs from the 2nd line containing the heading word (--start, default 'ವಿಷಯಾನುಕ್ರಮಣಿಕೆ') to the line
containing --end (default 'ಸಂಕೇತಾಕ್ಷರಗಳ', the list of abbreviations).
Blocks written: {"t":"center"|"mandala"|"sukta"|"item", "text":..., "no":"೨೪" (sukta), "page":int|null, "src":line_no}
Rules: '---', roman page marks (iv, *vii*, '## v'), image-description lines are dropped; a line starting with Kannada digits and
containing 'ಸೂಕ್ತ' is a sukta heading; a line ending in a number is an item with that page; a line without a number is joined with the
following one (max 2 lines) and written as an item without page if none follows.
--check lists what is suspicious: items without a page, pages that go DOWN inside the volume (OCR errors such as 125 read as 1).
--fixes: JSON {"<line_no>": page, ...} (line numbers of the source md, as printed by --check) applied before writing.
"""
import argparse, json, re, sys, pathlib

KDIG = '೦-೯'
ROMAN = re.compile(r'^(?:##\s*)?\*?(?:[ivxlc]{1,6})\*?$', re.I)

def parse(lines, start_word, end_word):
    idx = [i for i, l in enumerate(lines) if start_word in l]
    s = idx[1] if len(idx) > 1 else idx[0]
    e = next(i for i, l in enumerate(lines) if end_word in l and i > s)
    blocks, pend = [], None
    def flush():
        nonlocal pend
        if pend:
            blocks.append({'t': 'item', 'text': pend[1], 'page': None, 'src': pend[0]}); pend = None
    for i in range(s + 1, e):
        raw = lines[i].strip()
        if not raw or raw == '---' or ROMAN.match(raw) or 'This image contains' in raw: continue
        txt = re.sub(r'^##\s*', '', raw)
        if txt in ('॥ ಶ್ರೀಃ ॥',) or txt.startswith('ಋಗ್ವೇದಸಂಹಿತೆಯ') or txt.replace(' ', '') == 'ವಿಷಯಾನುಕ್ರಮಣಿಕೆ': continue
        m = re.match(rf'^([{KDIG}]+)[\.\s]+(.*ಸೂಕ್ತ.*)$', txt)
        if m:
            flush(); blocks.append({'t': 'sukta', 'no': m.group(1), 'text': m.group(2).strip(), 'src': i + 1}); continue
        if raw.startswith('## ') or re.search(r'(ಸಮಾಪ್ತವು|ಮಂಡಲದ—|ಮಂಡಲವು)\.?$', txt):
            flush()
            t = 'mandala' if re.search(r'ಮಂಡಲ', txt) and not raw.startswith('## ') else 'center'
            blocks.append({'t': t, 'text': txt.rstrip('—').strip(), 'src': i + 1}); continue
        m = re.match(r'^(.*?)[\s\.]+(\d{1,3})\.?$', txt)
        if m and m.group(1).strip():
            text = m.group(1).strip()
            if pend: text = pend[1] + ' ' + text; src = pend[0]; pend = None
            else: src = i + 1
            blocks.append({'t': 'item', 'text': text, 'page': int(m.group(2)), 'src': src})
        else:
            if pend: blocks.append({'t': 'item', 'text': pend[1], 'page': None, 'src': pend[0]})
            pend = (i + 1, txt)
    flush()
    return blocks

def check(blocks):
    prob, last = [], 0
    for b in blocks:
        if b['t'] != 'item': continue
        if b['page'] is None: prob.append((b['src'], 'no page number', b['text'][:60])); continue
        if b['page'] < last: prob.append((b['src'], f'page {b["page"]} after {last}', b['text'][:60]))
        else: last = b['page']
    return prob

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('md'); ap.add_argument('--out'); ap.add_argument('--fixes'); ap.add_argument('--check', action='store_true')
    ap.add_argument('--start', default='ವಿಷಯಾನುಕ್ರಮಣಿಕೆ'); ap.add_argument('--end', default='ಸಂಕೇತಾಕ್ಷರಗಳ')
    a = ap.parse_args()
    lines = pathlib.Path(a.md).read_text(encoding='utf-8').split('\n')
    blocks = parse(lines, a.start, a.end)
    if a.fixes and pathlib.Path(a.fixes).exists():
        fx = json.loads(pathlib.Path(a.fixes).read_text(encoding='utf8'))
        for b in blocks:
            if b['t'] == 'item' and str(b['src']) in fx: b['page'] = fx[str(b['src'])]
    print(f'{sum(b["t"]=="sukta" for b in blocks)} sūktas, {sum(b["t"]=="item" for b in blocks)} items')
    if a.check:
        for p in check(blocks): print('CHECK', *p, sep='\t')
    if a.out:
        pathlib.Path(a.out).write_text(json.dumps(blocks, ensure_ascii=False, indent=1), encoding='utf8'); print('wrote', a.out)

if __name__ == '__main__':
    main()
