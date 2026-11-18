#!/usr/bin/env python3
"""Sāyaṇa-bhāṣya reader: a by-product book built from a volume's English file.

Keeps, per Ṛk: Saṃhitā-pāṭha, Pada-pāṭha (Devanagari + IAST as in the volume),
Sāyaṇa-bhāṣya (as in the volume) and the English Gist of the bhāṣya.
Leaves out: Pratipadārtha, Bhāvārtha, the printed English translation, Special
Topics, the translator's Anuvāda, printed-page markers. Sūkta particulars
(seer, deity, metre, counts) are kept. Nothing is retyped or edited: lines are
selected, never rewritten (CLAUDE.md rule 2).

    python3 publish/bhashya_book.py 17 --sukta 40 [--sukta 41 ...] [--out DIR] [--html]

Writes DIR/Rigveda_Bhashya_Reader_VolN_<sel>.md (default DIR = publish/out) and,
with --html, a standalone HTML file via pandoc. Prints counts from finished
work only (Ṛks, bhāṣya words, gist words, NOTE markers).
"""
import argparse, json, pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
KEEP = {'samhita': 'Saṃhitā-pāṭha', 'pada': 'Pada-pāṭha',
        'bhashya': 'Sāyaṇa-bhāṣya', 'gist': 'Gist of the bhāṣya'}


def kind(heading):
    if 'Saṃhitā-pāṭha' in heading: return 'samhita'
    if 'Pada-pāṭha' in heading: return 'pada'
    if 'Sāyaṇa-bhāṣya' in heading: return 'bhashya'
    if heading.startswith('Gist of the bhāṣya'): return 'gist'
    return 'other'   # Pratipadārtha, Bhāvārtha, Wilson, Special Topics, Anuvāda, Particulars


PARTICULARS = re.compile(r'^(Om\.|Sūkta \d+[.;])')


def select(lines, suktas):
    """Yield output lines for the chosen sūktas."""
    out, in_sukta, sec, rk_seen = [], False, None, False
    para = []

    def flush():
        nonlocal para
        if not para: return
        text = '\n'.join(para)
        para = []
        first = text.lstrip('> ').lstrip()
        if sec == 'other' or sec is None:
            if PARTICULARS.match(first) and not rk_seen: out.extend(['*' + text.strip() + '*', ''])
            return
        if sec == 'gist':
            if first.startswith('Anuvāda'): return
            if PARTICULARS.match(first) and not rk_seen:
                out.extend(['*' + text.strip() + '*', '']); return
        out.extend([text, ''])

    for ln in lines:
        m = re.match(r'^(#{1,6}) (.*)', ln)
        if m:
            flush()
            lvl, head = len(m.group(1)), m.group(2).strip()
            if lvl == 2:
                ms = re.match(r'Sūkta\s+(\d+)\s+\(Maṇḍala\s+(\d+)\)', head)
                if ms:
                    in_sukta = int(ms.group(1)) in suktas; sec, rk_seen = None, False
                    if in_sukta: out.extend([f'## {head}', ''])
                else:
                    in_sukta = False
                continue
            if not in_sukta: continue
            if lvl == 4:
                if '(continued)' not in head:
                    rk_seen = True; out.extend([f'### {head}', ''])
                sec = None; continue
            if lvl == 5:
                sec = kind(head)
                if sec != 'other': out.extend([f'#### {head}', ''])
                continue
            continue   # '### Printed p. N' and any other: dropped, section continues
        if not in_sukta: continue
        if ln.strip() == '': flush(); continue
        if sec in ('samhita', 'pada', 'bhashya', 'gist') or sec in ('other', None):
            para.append(ln)
    flush()
    return out


def stats(md):
    rks = len(re.findall(r'^### Ṛk', md, flags=re.M))
    bh = gi = 0
    sec = None
    for ln in md.splitlines():
        if ln.startswith('#### '): sec = kind(ln[5:]); continue
        if sec == 'bhashya': bh += len(ln.lstrip('> ').split())
        elif sec == 'gist': gi += len(ln.split())
    return rks, bh, gi, md.count('**NOTE**')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('vol', type=int)
    ap.add_argument('--sukta', type=int, action='append', required=True)
    ap.add_argument('--out', default=str(ROOT / 'publish' / 'out'))
    ap.add_argument('--html', action='store_true')
    a = ap.parse_args()
    cfg = json.loads((ROOT / f'vol{a.vol}' / 'volcfg.json').read_text(encoding='utf-8'))
    src = ROOT / cfg['out']['en']
    lines = src.read_text(encoding='utf-8').splitlines()
    body = select(lines, set(a.sukta))
    md = '\n'.join(body).strip() + '\n'
    sel = '-'.join(str(s) for s in a.sukta)
    title = f"Sāyaṇa's Ṛgveda-bhāṣya in English: reader (Vol {a.vol}, Sūkta {', '.join(map(str, a.sukta))})"
    md = f'# {title}\n\n' + md
    out = pathlib.Path(a.out); out.mkdir(parents=True, exist_ok=True)
    f = out / f'Rigveda_Bhashya_Reader_Vol{a.vol}_S{sel}.md'
    f.write_text(md, encoding='utf-8')
    rks, bh, gi, notes = stats(md)
    print(f'wrote {f}: {rks} Ṛks; bhāṣya (Devanagari) words {bh}; English gist words {gi}; **NOTE** markers {notes}')
    if a.html:
        h = f.with_suffix('.html')
        css = out / 'bhashya_reader.css'
        css.write_text('body{max-width:46em;margin:2em auto;padding:0 1em;font:17px/1.6 "Noto Serif Devanagari","Noto Serif",serif}'
                       'blockquote{border-left:3px solid #bbb;margin:.6em 0;padding-left:1em}'
                       'h4{font-size:.85em;letter-spacing:.04em;color:#666;margin:1em 0 .2em}'
                       'h3{border-top:1px solid #ccc;padding-top:.6em}\n', encoding='utf-8')
        subprocess.run(['pandoc', str(f), '-s', '--metadata', f'title={title}', '-c', css.name, '-o', str(h)], check=True)
        print(f'wrote {h}')


if __name__ == '__main__':
    sys.exit(main())
