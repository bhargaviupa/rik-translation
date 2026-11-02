#!/usr/bin/env python3
"""Apply the user's numeral sheets BY LOCATION (user decision, Nov 2: "my data are right; apply them based on the location context").

For every PDF page covered by a sheet: the sheet's multi-part numbers (e.g. 1-181-7, 22-7) in printed line order are aligned, in order,
with the multi-part numbers found in the English text of that page (Latin or Devanagari digits; optional [?] flag; 'N-[?]' prefixes; a
bare '[?]' after a source abbreviation). The alignment is an order-preserving DP; a pair is allowed only if the numbers are plausibly the
same citation (same first component or within 2 digit edits, or prefix-compatible, or a blank [?]). Gaps are free (the sheet may omit a
reference, the English may carry numbers the sheet does not have). Each aligned pair whose English number differs from the sheet is set to
the sheet value (the [?] flag is removed). Everything changed is logged in vol10/review/numerals_aligned_v10.tsv (old, new, page, sheet row,
score) so the user can review.  Asserts: headings and the single progress note unchanged; only digits / hyphens / [?] / one space / backticks change.
Usage: apply_numerals_aligned.py [--from PDF] [--to PDF] [--write]
"""
import re, os, sys, glob, argparse, collections
import openpyxl
sys.path.insert(0, os.path.dirname(__file__))
import apply_numerals as A

DV = A.DV
D = '[0-9' + DV + ']'
# English tokens: full numbers (>=2 parts) with optional flag, prefixes 'N-[?]', and flagged bare [?] handled separately
TOK_FULL = re.compile(r'(?<![\w\-.])(' + D + r'+(?:[-‐‑]' + D + r'+)+)((?: ?`?\[\?\]`?)?)(?![\w\-]|\.' + D + ')')
TOK_PREFIX = re.compile(r'(?<![\w\-.])(' + D + r'+(?:-' + D + r'+)*)-(\[\?\])(?![\w\-]|' + D + ')')

def ed(a, b):
    d = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        p = d[:]; d[0] = i
        for j, y in enumerate(b, 1):
            d[j] = min(p[j] + 1, d[j - 1] + 1, p[j - 1] + (x != y))
    return d[-1]

def sim(en, sh, kind):
    """score of aligning English token (norm string en, kind full/prefix) with sheet number sh; None = not allowed"""
    if kind == 'prefix':
        if sh.startswith(en + '-') and sh.count('-') == en.count('-') + 1:
            return 8
        return None
    if en == sh:
        return 10
    ec, sc = en.split('-'), sh.split('-')
    if len(ec) != len(sc):
        return None
    e = ed(en.replace('-', ''), sh.replace('-', ''))
    if e <= 1: return 6
    if e <= 2: return 4
    if ec[0] == sc[0]: return 2
    return None

def english_tokens(blk, base):
    out = []  # (start, end, norm, kind, text, flagged)
    for m in TOK_FULL.finditer(blk):
        num = A.norm(m.group(1))
        if not re.fullmatch(r'\d+(-\d+)+', num): continue
        out.append((base + m.start(), base + m.end(), num, 'full', m.group(0), bool(m.group(2))))
    for m in TOK_PREFIX.finditer(blk):
        num = A.norm(m.group(1))
        out.append((base + m.start(), base + m.end(), num, 'prefix', m.group(0), True))
    out.sort()
    return out

def align(en, sh):
    n, m = len(en), len(sh)
    NEG = -10**9
    best = [[0] * (m + 1) for _ in range(n + 1)]; back = [[None] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            b, bk = best[i - 1][j], ('e',)
            if best[i][j - 1] > b: b, bk = best[i][j - 1], ('s',)
            s = sim(en[i - 1][2], sh[j - 1][1], en[i - 1][3])
            if s is not None and best[i - 1][j - 1] + s > b:
                b, bk = best[i - 1][j - 1] + s, ('m', s)
            best[i][j], back[i][j] = b, bk
    pairs = []; i, j = n, m
    while i > 0 and j > 0:
        bk = back[i][j]
        if bk is None: break
        if bk[0] == 'm': pairs.append((i - 1, j - 1, bk[1])); i -= 1; j -= 1
        elif bk[0] == 'e': i -= 1
        else: j -= 1
    return pairs[::-1]

def load_sheets():
    byp = collections.defaultdict(list)
    for f in sorted(glob.glob(os.path.join(A.NUMD, 'Rigveda_Clean_Numerals_%s_*.xlsx' % A.VOLN))):
        mm = re.search(r'_(\d+)_(\d+)_(\d+)\.xlsx$', f)      # Vol 9 style: ..._9_<firstPDFpage>_<lastPDFpage>.xlsx
        if mm: base = int(mm.group(2)) - 1
        else: base = 100 * (int(re.search(r'_(\d+)\.xlsx$', f).group(1)) - 1)
        ws = openpyxl.load_workbook(f, read_only=True).active
        for i, r in enumerate(list(ws.iter_rows(values_only=True))[1:], start=2):
            if r[0] is None or not r[3]: continue
            num = A.norm(str(r[3]))
            if not re.fullmatch(r'\d+(-\d+)+', num): continue
            g = int(r[0]) + base
            byp[g].append((int(r[1] or 0), num, os.path.basename(f), i, str(r[4])))
    for g in byp:
        byp[g].sort(key=lambda x: (x[0], x[3]))
    return byp

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--from', dest='a', type=int, default=0)
    ap.add_argument('--to', dest='b', type=int, default=10**6)
    ap.add_argument('--write', action='store_true')
    ap.add_argument('--min', type=int, default=6, help='lowest alignment score applied; lower-scoring pairs go to the review list')
    args = ap.parse_args()
    t = open(A.EN, encoding='utf-8').read()
    heads = list(A.HEAD.finditer(t))
    nh, nnote, nq = len(re.findall(r'^#{1,6} ', t, re.M)), t.count('**Progress note:**'), t.count('[?]')
    sheets = load_sheets()
    edits, log, stats, review = [], [], collections.Counter(), []
    for i, h in enumerate(heads):
        g = int(h.group(2))
        if not (args.a <= g <= args.b) or g not in sheets: continue
        end = heads[i + 1].start() if i + 1 < len(heads) else len(t)
        blk = t[h.start():end]
        en = english_tokens(blk, h.start())
        # tokens of a duplicated PDF page marker are handled once per block
        sh = [(s[0], s[1], s[2], s[3], s[4]) for s in sheets[g]]
        pairs = align(en, sh)
        stats['pages'] += 1; stats['sheet_rows'] += len(sh); stats['english_tokens'] += len(en); stats['aligned'] += len(pairs)
        for ei, sj, score in pairs:
            s0, e0, num, kind, text, flagged = en[ei]
            row = sh[sj]
            new_num = row[1]
            if kind == 'full' and num == new_num and not flagged:
                stats['already_equal'] += 1; continue
            m0 = re.match(r'[^\[\s`]+', text)
            like = text
            digits = out = new_num
            if any(c in DV for c in text): digits = A.out_digits(new_num, text)
            if kind == 'prefix':
                new_text = digits
            else:
                new_text = digits   # flag removed
            if new_text == text:
                continue
            if score < args.min:
                stats['review_only'] += 1
                review.append((g, 'proposed', text, new_text, '%s row %d' % (row[2], row[3]), row[0], score)); continue
            kindname = 'confirmed' if (kind == 'full' and num == new_num) else ('filled' if kind == 'prefix' else 'changed')
            stats[kindname] += 1
            edits.append((s0, e0, new_text, text))
            log.append((g, kindname, text, new_text, '%s row %d' % (row[2], row[3]), row[0], score))
    edits.sort()
    for a_, b_ in zip(edits, edits[1:]):
        assert a_[1] <= b_[0], 'overlap'
    new_t = t
    for s, e, new, old in reversed(edits):
        new_t = new_t[:s] + new + new_t[e:]
    assert len(re.findall(r'^#{1,6} ', new_t, re.M)) == nh and new_t.count('**Progress note:**') == nnote == 1
    allowed = re.compile(r'[0-9' + DV + r'\[\]?` \-‐‑]*')
    for s, e, new, old in edits:
        assert allowed.fullmatch(old) and allowed.fullmatch(new), (old, new)
    print(dict(stats), '[?] %d -> %d' % (nq, new_t.count('[?]')))
    if args.write:
        open(A.EN, 'w', encoding='utf-8').write(new_t)
        p = os.path.join(A.REV, 'numerals_aligned_v10.tsv')
        new_file = not os.path.exists(p)
        with open(p, 'a', encoding='utf-8') as f:
            if new_file: f.write('PDF page\tkind\told (English)\tnew (sheet)\tsheet row\tline in sheet\tscore\n')
            for r in log: f.write('\t'.join(map(str, r)) + '\n')
    if args.write:
        with open(os.path.join(A.REV, 'numerals_aligned_review_v10.tsv'), 'a', encoding='utf-8') as f:
            for r in review: f.write('\t'.join(map(str, r)) + '\n')
    return log

if __name__ == '__main__':
    main()
