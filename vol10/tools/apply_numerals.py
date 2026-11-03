#!/usr/bin/env python3
"""Phase 1 numeral application for Vol 10 (no page images, no scan).

Input : vol10/numerals/Rigveda_Clean_Numerals_10_N.xlsx  (N = scan part; sheet page p of part N
        = global PDF page p + 100*(N-1); this equals the "(PDF g)" in the '### Printed p. X (PDF g)'
        headings of the English file -- verified: >75% of rows' numbers occur on that page, <6% on +-1..3).
Sites : numeric references in the English file that carry a doubt flag, on the page of the row:
        (a) 'NUM [?]' / 'NUM `[?]`'  (number given, flagged)  -> exact: flag removed ("confirmed");
            same length and exactly one digit different from the page's only close row -> digit corrected;
        (b) 'A-B-[?]' (prefix given, last component missing) -> filled when exactly one row on the page
            has that prefix and exactly one more component.
Everything else is listed in the unmatched TSV (not guessed).
Only digits / the [?] flag / one space before it are changed (asserted).
Usage: apply_numerals.py [--from PDF] [--to PDF] [--write]   (default: dry run)
"""
import re, sys, os, glob, argparse, collections
import openpyxl

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
VOLN = os.environ.get('NUM_VOL', '10')   # '10' (default) or '9' etc.
EN = os.path.join(ROOT, 'vol%s' % VOLN, 'Rigveda_Samhita_Vol%s_English_Translation.md' % VOLN)
NUMD = os.path.join(ROOT, 'vol%s' % VOLN, 'numerals')
REV = os.path.join(ROOT, 'vol%s' % VOLN, 'review')
KN = '೦೧೨೩೪೫೬೭೮೯'; DV = '०१२३४५६७८९'
D = '[0-9' + DV + ']'

def to_ascii(s):
    return ''.join(str(KN.index(c)) if c in KN else str(DV.index(c)) if c in DV else c for c in s)

def norm(s):  # '22.7' / '22-7' -> '22-7'
    return re.sub(r'[.\-–]+', '-', to_ascii(s)).strip('-')

def load_rows():
    rows = []  # (global_pdf, norm_number, sheet, line, pattern_kn)
    for f in sorted(glob.glob(os.path.join(NUMD, 'Rigveda_Clean_Numerals_10_*.xlsx'))):
        n = int(re.search(r'_(\d+)\.xlsx$', f).group(1))
        ws = openpyxl.load_workbook(f, read_only=True).active
        for i, r in enumerate(list(ws.iter_rows(values_only=True))[1:], start=2):
            if r[0] is None or not r[3]:
                continue
            num = norm(str(r[3]))
            if not re.fullmatch(r'\d+(-\d+)*', num):
                continue
            rows.append((int(r[0]) + 100 * (n - 1), num, os.path.basename(f), i, str(r[2])))
    return rows

def out_digits(num, like):
    """write num using Devanagari digits if 'like' (the site text) uses them"""
    if any(c in DV for c in like):
        return ''.join(DV[int(c)] if c.isdigit() else c for c in num)
    return num

HEAD = re.compile(r'^### Printed p\. (\S+)\s+\(PDF (\d+)[^)]*\)', re.M)
SITE_FULL = re.compile(r'(?<![\w-])(' + D + r'+(?:-' + D + r'+)*)( ?`?)\[\?\](`?)(?![\w-])')
SITE_PREFIX = re.compile(r'(?<![\w-])(' + D + r'+(?:-' + D + r'+)*)-\[\?\](?![\w-])')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--from', dest='a', type=int, default=0)
    ap.add_argument('--to', dest='b', type=int, default=200)
    ap.add_argument('--write', action='store_true')
    ap.add_argument('--tag', default='')
    args = ap.parse_args()
    t = open(EN, encoding='utf-8').read()
    heads = list(HEAD.finditer(t))
    nh, nnote, nq = len(re.findall(r'^#{1,6} ', t, re.M)), t.count('**Progress note:**'), t.count('[?]')
    rows = load_rows()
    byp = collections.defaultdict(dict)  # page -> {num: first row}
    for r in rows:
        byp[r[0]].setdefault(r[1], r)
    edits = []  # (abs_start, abs_end, new, log)
    unmatched = []
    used_rows = set()
    for i, h in enumerate(heads):
        g = int(h.group(2))
        if not (args.a <= g <= args.b):
            continue
        end = heads[i + 1].start() if i + 1 < len(heads) else len(t)
        blk = t[h.start():end]
        prow = byp.get(g, {})
        # full-number sites
        for m in SITE_FULL.finditer(blk):
            num = norm(m.group(1)); asc = to_ascii(m.group(1))
            if not re.fullmatch(r'\d+(-\d+)*', num):
                continue
            ctx = blk[max(0, m.start() - 30):m.end() + 10].replace('\n', ' ')
            if num in prow:
                r = prow[num]; used_rows.add((r[2], r[3]))
                new = m.group(1)  # drop ' [?]' / ' `[?]`'
                edits.append((h.start() + m.start(), h.start() + m.end(), new,
                              (g, 'confirmed', blk[m.start():m.end()], new, r)))
                continue
            close = [r for n2, r in prow.items()
                     if not re.search(r'(?<![\d-])' + re.escape(n2) + r'(?![\d-])', to_ascii(blk))
                     and len(n2) == len(num) and [len(x) for x in n2.split('-')] == [len(x) for x in num.split('-')]
                     and sum(a != b for a, b in zip(n2, num)) == 1]
            if len(close) == 1:
                r = close[0]; used_rows.add((r[2], r[3]))
                new = out_digits(r[1], m.group(1))
                edits.append((h.start() + m.start(), h.start() + m.end(), new,
                              (g, 'corrected', blk[m.start():m.end()], new, r)))
            else:
                unmatched.append((g, 'no unique match' if not close else 'ambiguous close rows', ctx,
                                  ','.join(prow) if prow else '(no rows on page)'))
        # prefix sites
        for m in SITE_PREFIX.finditer(blk):
            pre = norm(m.group(1))
            ctx = blk[max(0, m.start() - 30):m.end() + 10].replace('\n', ' ')
            cand = [r for n2, r in prow.items() if n2.startswith(pre + '-') and n2.count('-') == pre.count('-') + 1]
            if len(cand) == 1:
                r = cand[0]; used_rows.add((r[2], r[3]))
                last = r[1].rsplit('-', 1)[1]
                new = m.group(1) + '-' + out_digits(last, m.group(1))
                edits.append((h.start() + m.start(), h.start() + m.end(), new,
                              (g, 'filled', blk[m.start():m.end()], new, r)))
            else:
                unmatched.append((g, 'prefix: %d candidates' % len(cand), ctx, ','.join(prow) if prow else '(no rows on page)'))
    # a row used to 'correct' two sites with different numbers is ambiguous: drop those corrections
    cnt = collections.defaultdict(set)
    for e in edits:
        if e[3][1] == 'corrected':
            cnt[(e[3][0], e[3][4][1])].add(e[3][2])
    bad = {k for k, v in cnt.items() if len(v) > 1}
    for e in [e for e in edits if e[3][1] == 'corrected' and (e[3][0], e[3][4][1]) in bad]:
        edits.remove(e)
        unmatched.append((e[3][0], 'two sites close to one row', e[3][2], e[3][4][1]))
    # rows not used and not present on page
    unused = []
    for r in rows:
        if not (args.a <= r[0] <= args.b):
            continue
        if (r[2], r[3]) in used_rows:
            continue
        unused.append(r)
    # apply (non overlapping, from the end)
    edits.sort()
    for a, b in zip(edits, edits[1:]):
        assert a[1] <= b[0], 'overlapping edits'
    new_t = t
    for s, e, new, log in reversed(edits):
        new_t = new_t[:s] + new + new_t[e:]
    # asserts: structure unchanged, only digits / [?] / backticks / space changed
    assert len(re.findall(r'^#{1,6} ', new_t, re.M)) == nh, 'heading count changed'
    assert new_t.count('**Progress note:**') == nnote == 1, 'progress note count'
    for s, e, new, log in edits:
        old = t[s:e]
        assert re.sub(r'[0-9' + DV + r'\[\]?` \-]', '', old) == re.sub(r'[0-9' + DV + r'\[\]?` \-]', '', new) == '', (old, new)
    print('sites edited: %d  (confirmed %d, corrected %d, filled %d); unmatched sites: %d; [?] %d -> %d' % (
        len(edits), sum(1 for x in edits if x[3][1] == 'confirmed'), sum(1 for x in edits if x[3][1] == 'corrected'),
        sum(1 for x in edits if x[3][1] == 'filled'), len(unmatched), nq, new_t.count('[?]')))
    if args.write:
        open(EN, 'w', encoding='utf-8').write(new_t)
        os.makedirs(REV, exist_ok=True)
        with open(os.path.join(REV, 'numerals_applied_v10.tsv'), 'a', encoding='utf-8') as f:
            for s, e, new, (g, kind, old, nw, r) in edits:
                f.write('\t'.join([str(g), kind, old.replace('\t', ' '), nw, '%s row %d' % (r[2], r[3]), r[4]]) + '\n')
        # per-row status of every sheet row: run vol10/tools/numerals_report.py
    return edits, unmatched, unused

if __name__ == '__main__':
    main()
