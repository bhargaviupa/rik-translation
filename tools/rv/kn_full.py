#!/usr/bin/env python3
"""Whole-volume Kannada Text file, made by script from the supplied machine-read text (Nov 26 2026; no English file is read or written).

  python3 tools/rv/kn_full.py VOL [--source FILE[@LO-HI] ...] [--out FILE] [--mandala N ...] [--write] [--force]

Sources: --source, else `source` of volN/volcfg.json (so no volcfg.json is needed).  Default output: volN/Rigveda_Samhita_VolN_Kannada_Text.md.
Without --write nothing is written (report only).  An existing output file is never overwritten (--force is for the file this tool made itself).
Method: html_pages.load_many (page split) + html_to_kn.kn_pages (cleaning, labels, structure repairs), all pages in one run, in the format of Vol 29.
A page missing from the supplied text gets `<!-- printed N: NOT IN THE SUPPLIED TEXT -->` and a row in volN/review/kn_gaps.md; nothing is invented.
Gates (the file is refused when one fails):
  * every printed page between the first and the last has exactly one marker, in order;
  * digits: per page, the multiset of digits (Kannada and Latin counted alike) of the output equals that of the supplied page text + its head;
  * Kannada letters: per page, no letter of the supplied text may be missing from the output (labels may ADD letters, nothing may be lost or changed);
    the only documented changes are those of html_to_kn (|→।, Latin s→ಽ, Devanagari→Kannada, hyphen join, label insertion).
Kannada Sūkta/Ṛk headings (tools/rv/kn_headings.py) are not made: they need an English file of the same structure."""
import re, sys, os, json, collections
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
ROOT = os.path.abspath(os.path.join(here, '..', '..'))
import html_pages, html_to_kn
KD = str.maketrans('೦೧೨೩೪೫೬೭೮೯०१२३४५६७८९', '01234567890123456789')
HEADER = '# ಋಗ್ವೇದ ಸಂಹಿತಾ — ಸಂಪುಟ {v} (Kannada text)\n*The Kannada text of the printed pages, made by script from the supplied machine-read text (tools/rv/kn_full.py, html_to_kn.py) and not yet checked by a translator; no English text is involved. `[?]` marks a doubtful reading.*\n\n---\n\n'

def norm_src(s):
    """the supplied text as html_to_kn sees it: cleaned line by line (documented cleaning only), label lines left out (their wording is normalised)"""
    out = []
    for l in s.split('\n'):
        l = html_to_kn.clean_line(l)
        if not l: continue
        l = html_to_kn.deva_to_kn_line(l)[0]
        if html_to_kn.label_of(l): continue
        out.append(l)
    return '\n'.join(out)
def norm_out(s):
    return '\n'.join(l for l in s.split('\n') if not re.fullmatch(r'\*(%s)\*' % '|'.join(map(re.escape, html_to_kn.CANON.values())), l))
def digits(s): return collections.Counter(re.findall(r'\d', s.translate(KD)))
def letters(s): return collections.Counter(re.findall(html_to_kn.KL, s))


ROMAN = re.compile(r'^\**\s*[ivxlcIVXLC]{1,6}\s*\**$')
def head_number(lines):
    """printed number from the first lines of a `## Page N` block: a line of digits only, 'NNN ಸಾಯಣಭಾಷ್ಯಸಹಿತಾ', or '… ಋಗ್ವೇದಸಂಹಿತಾ NNN'"""
    for l in [x for x in lines if x.strip()][:5]:
        t = l.strip().strip('*').strip().translate(KD)
        m = re.fullmatch(r'(\d{1,4})', t) or re.match(r'(\d{1,4})\s+\S', t) or re.search(r'ಸಂಹಿತಾ\s*\.?\s*(\d{1,4})\s*$', t)
        if m: return int(m.group(1))
    return None
def scan_pages(specs, tmp):
    """`## Page N` transcription (scan page numbers, Vol 22): printed number = scan number - local median offset of the pages whose own head has a number;
    the scan header is replaced by `<!-- page K -->`; pages before the first numbered head with a roman head (front matter) are returned as plain text"""
    outs = []; front = []; log = []
    for sp in specs:
        f, _, r = sp.partition('@'); L = open(f, encoding='utf8').read().split('\n')
        idx = [i for i, l in enumerate(L) if re.match(r'## Page \d+\s*$', l)]
        blocks = [(int(L[i].split()[2]), L[i + 1:(idx[j + 1] if j + 1 < len(idx) else len(L))]) for j, i in enumerate(idx)]
        num = [(n, head_number(b)) for n, b in blocks]
        num = [(n, h) for n, h in num if h is not None and not any(ROMAN.match(x.strip()) for x in [y for y in dict(blocks)[n] if y.strip()][:2])]
        offs = [n - h for n, h in num]; ofs = {}
        for k, (n, h) in enumerate(num):
            nb = sorted(offs[max(0, k - 4):k] + offs[k + 1:k + 5]); ofs[n] = nb[len(nb) // 2] if nb else offs[k]
            if offs[k] != ofs[n]: log.append(f'scan page {n}: head number {h} disagrees with its neighbours; printed number taken as {n - ofs[n]}')
        keys = sorted(ofs); first = keys[0] if keys else None; o = []
        for n, b in blocks:
            if first is None or n < first:
                front.append((n, [x for x in b])); continue
            near = min(keys, key=lambda x: abs(x - n)); k = n - ofs[near]
            o.append(f'<!-- page {k} -->'); o.extend(b)
        d = os.path.join(tmp, 'scan_' + os.path.basename(f)); open(d, 'w', encoding='utf8').write('\n'.join(o))
        outs.append(d + ('@' + r if r else ''))
    return outs, front, log

def main(a):
    vol = a[0]; opt = lambda k: [a[i + 1] for i, x in enumerate(a) if x == k]
    cfgp = os.path.join(ROOT, f'vol{vol}', 'volcfg.json'); cfg = json.load(open(cfgp, encoding='utf8')) if os.path.exists(cfgp) else {}
    srcs = opt('--source') or cfg.get('source') or sys.exit('no --source and no volcfg.json source')
    specs = [os.path.join(ROOT, s.split('@')[0]) + ('@' + s.split('@')[1] if '@' in s else '') for s in srcs]
    mand = [int(x) for x in opt('--mandala')] or cfg.get('mandalas') or None
    out = (opt('--out') or [os.path.join(ROOT, f'vol{vol}', f'Rigveda_Samhita_Vol{vol}_Kannada_Text.md')])[0]
    if os.path.exists(out) and '--write' in a and '--force' not in a: sys.exit(f'REFUSED: {out} exists (not overwritten)')
    import tempfile
    tmp = tempfile.mkdtemp(prefix='kn_full_'); nfig = []
    def collapse(sp):      # a multi-line <figure><img title="OCR of the picture"> block becomes one `[figure: file]` line (scratch copy; the supplied file is not touched)
        f, _, r = sp.partition('@'); t = open(f, encoding='utf8', errors='replace').read()
        def rep(m):
            nm = re.search(r'src="[^"]*?([^/"]+)"', m.group(0)); nfig.append((os.path.basename(f), nm.group(1) if nm else '?')); return '[figure: %s]' % (nm.group(1) if nm else '?')
        t = re.sub(r'<figure\b.*?</figure>', rep, t, flags=re.S)
        d = os.path.join(tmp, str(len(nfig)) + '_' + os.path.basename(f)); open(d, 'w', encoding='utf8').write(t); return d + ('@' + r if r else '')
    specs = [collapse(sp) for sp in specs]
    front = []; scan_log = []
    if '--scan-pages' in a:
        specs, front, scan_log = scan_pages(specs, tmp)
    heads = {}; P = html_pages.load_many(specs, heads); anomalies = list(html_pages.ANOMALIES)
    if not P: sys.exit('no pages found in the sources')
    lo, hi = min(P), max(P); allp = list(range(lo, hi + 1)); gaps = [p for p in allp if p not in P]
    txt, _ = html_to_kn.kn_pages(specs, allp, None, mand, warm=0)
    extra = list(html_to_kn.EXTRA); log = list(html_to_kn.LOG)
    txt = re.sub(r'(?m)^<!-- printed (\d+): NOT IN THE SUPPLIED TEXT -->$', r'<!-- printed \1: NO PAGE OF ITS OWN IN THE SUPPLIED TEXT (no running head; its text, if present, stands in the page before) -->', txt)
    gaps = [p for p in gaps if p not in extra]
    # gates
    marks = [int(x) for x in re.findall(r'(?m)^<!-- printed (\d+)(?::[^>]*)? -->$', txt)]
    bad = []
    if marks != sorted(set(marks)): bad.append('page markers repeated or out of order')
    miss = [p for p in allp if p not in set(marks)]
    if miss: bad.append(f'markers missing for {miss[:10]}')
    parts = re.split(r'(?m)^(?=<!-- printed \d+(?::[^>]*)? -->$)', txt); pg = {}
    for part in parts:
        m = re.match(r'<!-- printed (\d+)', part)
        if m: pg[int(m.group(1))] = part
    dbad = []; lbad = []
    for p in allp:
        if p not in P or (p in extra and p not in P): continue
        o = re.sub(r'(?m)^<!-- printed \d+(?::[^>]*)? -->$', '', pg.get(p, '') + (pg.get(p + 1, '') if (p + 1) in extra else ''))
        s = norm_src(heads.get(p, '') + '\n' + P[p]); o = norm_out(o)
        s = re.sub(r'\[figure[^\]]*\]', '', s); o = re.sub(r'\[figure[^\]]*\]', '', o)
        dd = digits(s) - digits(o); de = digits(o) - digits(s)
        if dd or de: dbad.append((p, dict(dd), dict(de)))
        ll = letters(s) - letters(o)
        if sum(ll.values()) > 0: lbad.append((p, sum(ll.values()), ''.join(list(ll)[:12])))
    if dbad: bad.append(f'digits differ on {len(dbad)} pages, first: {dbad[:5]}')
    if lbad: bad.append(f'Kannada letters lost on {len(lbad)} pages, first: {lbad[:5]}')
    print(f'Vol {vol}: sources {srcs}; pages {lo}-{hi}; made {len(P)}; gaps {len(gaps)} {gaps[:15]}; extra markers by script {extra}; head anomalies {len(anomalies)}; notes {len(log)}; picture blocks collapsed {len(nfig)}')
    for b in bad: print('GATE FAILED:', b)
    if '--write' in a:
        if bad and '--accept-gates' not in a: sys.exit('not written (gates failed; see above)')
        os.makedirs(os.path.dirname(out), exist_ok=True)
        fm = ''.join(f'<!-- front matter: scan page {n} -->\n\n' + '\n'.join(html_to_kn.clean_line(x) for x in b if html_to_kn.clean_line(x)) + '\n\n' for n, b in front)
        open(out, 'w', encoding='utf8').write(HEADER.format(v=vol) + (fm + '---\n\n' if fm else '') + txt)
        rv = os.path.join(ROOT, f'vol{vol}', 'review'); os.makedirs(rv, exist_ok=True)
        if gaps:
            open(os.path.join(rv, 'kn_gaps.md'), 'w', encoding='utf8').write(f'# Vol {vol}: printed pages not in the supplied text\n\nMarked `<!-- printed N: NO PAGE OF ITS OWN IN THE SUPPLIED TEXT … -->` in the Kannada Text file (no running head was found for the page: either it is missing or it was merged into the page before) (tools/rv/kn_full.py).\n\n' + ', '.join(map(str, gaps)) + '\n')
        open(os.path.join(rv, 'kn_full_notes.md'), 'w', encoding='utf8').write(f'# Vol {vol}: notes of tools/rv/kn_full.py\n\nHead anomalies (line, number read, number used, head):\n\n' + '\n'.join(f'- {x}' for x in anomalies) + '\n\nPicture blocks (<figure>, OCR text of a picture) replaced by one `[figure: file]` line:\n\n' + '\n'.join(f'- {x}' for x in nfig) + '\n\nScan-page numbering (--scan-pages):\n\n' + '\n'.join(f'- {x}' for x in scan_log) + '\n\nScript notes:\n\n' + '\n'.join(f'- {x}' for x in log) + '\n')
        print('written', out, len(txt.split('\n')), 'lines')
    return 1 if bad else 0
if __name__ == '__main__': sys.exit(main(sys.argv[1:]))
