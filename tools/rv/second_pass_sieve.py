#!/usr/bin/env python3
"""S0 sieve of the second pass of a legacy volume (docs/prompts/second_pass/VOLN.md): scripts only, no model, nothing is changed in the volume.

  python3 tools/rv/second_pass_sieve.py VOL [--kn FILE] [--out DIR]

The English file of a legacy volume is organised by Ṛk, not by page. Its page marks are the headings `### Page N`, `### Printed p. N`, `### Rik a.b (pp. N–M`
and the inline marks `(p. N`, `(pp. N–M`, `printed p. N`. A line belongs to the page of the nearest mark above it; the English between two marks is one
SEGMENT. The Kannada window of a segment = printed pages (first page - 1) .. (first page of the next segment), so that pages without a mark of their own
are covered. Per segment the script lists (never decides): references with separators and plain numbers (2+ digits) that the English has and the window
does not, references of the window's own pages that the segment lacks only when the segment covers them wholly (pages with one segment), `[?]`, `[sic]`,
bracketed remarks, `**GLOSS**` markers, letters of scripts that do not belong (English: not Latin/Devanagari/Greek-in-names; Kannada: Telugu, Tamil,
Malayalam, Bengali, Gujarati, Gurmukhi, Odia, Cyrillic, Arabic, CJK), and Devanagari quotations of the commentary (the Saṃhitā, Pada and bhāṣya blocks are
NOT compared: they come from Wikisource, REQUIREMENTS B5) that are absent from the window.
Writes OUT/sieve.tsv (one row per page: segments, counts) and OUT/sieve_segments.tsv (one row per segment) and prints the totals.
Kannada: the file made by tools/rv/prose_kn.py (`<!-- printed N -->` marks); default VOL/Rigveda_Samhita_VolN_Kannada_Text.md."""
import re, sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import recheck as R

MARK = re.compile(r'### Page (\d+) \(PDF|### Printed p\. (\d+)|### Pages? (\d+)[–-]|### Rik [\d.]+ \(pp?\. (\d+)|\((?:p|pp)\. ?(\d+)|printed p\. (\d+)|\*\(p\. ?(\d+)|^\*\*[^*\n]*\*\*(?: \*\()?(?:pp?\. ?(\d+))')
SKIP_LABELS = ('Saṃhitā', 'Pada-pāṭha', 'Sāyaṇa-bhāṣya')
OTHER_EN = re.compile('[Ѐ-ӿ؀-ۿঀ-ൿ一-鿿぀-ヿ฀-๿]')   # Cyrillic, Arabic, Bengali…Malayalam (incl. Kannada!) , CJK, Thai
OTHER_KN = re.compile('[Ѐ-ӿ؀-ۿঀ-౿ഀ-ൿ一-鿿]')                 # Kannada block (0C80-0CFF) and Devanagari (0900-097F) are allowed
REMARK = re.compile(r'\[(?!\?\]|sic)[^\]\[]{12,}\]|\[sic[^\]]*\]')

def segments(lines):
    """[(first_page, first_line, last_line, [lines])]; the page changes where a mark gives a page >= the current one"""
    segs = []; cur = None
    for i, l in enumerate(lines):
        pg = None
        for m in MARK.finditer(l):
            g = [x for x in m.groups() if x]
            if g: pg = int(g[0])
        if pg is not None and (cur is None or pg != cur[0]):
            if cur is not None and pg < cur[0] - 2 and not l.startswith('###'): pg = None   # a back reference inside a sentence ("see p. 12")
        if pg is not None and (cur is None or pg != cur[0]):
            cur = [pg, i + 1, i + 1, []]; segs.append(cur)
        if cur is None: cur = [0, i + 1, i + 1, []]; segs.append(cur)
        cur[3].append(l); cur[2] = i + 1
    return segs

def commentary(lines):
    """the lines of a segment without the Saṃhitā/Pada/bhāṣya blocks (the label state is carried by the caller)"""
    return lines

def main():
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    vol = a[0]; d = f'vol{vol}'
    kn_file = a[a.index('--kn') + 1] if '--kn' in a else f'{d}/Rigveda_Samhita_Vol{vol}_Kannada_Text.md'
    out = a[a.index('--out') + 1] if '--out' in a else f'{d}/review/second_pass'
    os.makedirs(out, exist_ok=True)
    en_file = f'{d}/Rigveda_Samhita_Vol{vol}_English_Translation.md'
    lines = open(en_file, encoding='utf8').read().split('\n')
    KN, NOTIN = R.read_kn(kn_file); kpages = sorted(k for k in KN if isinstance(k, int) and k not in NOTIN)
    segs = segments(lines)
    # label state (skip blocks) per line
    skip = [False] * len(lines); state = False
    for i, l in enumerate(lines):
        m = re.match(r'\*\*([^*]+)\*\*', l)
        if m: state = m.group(1).startswith(SKIP_LABELS)
        elif l.startswith('###') or l.startswith('## '): state = False
        elif l.startswith('**Translation:**') or l.startswith('**Grammatical') or l.startswith('---'): state = False
        skip[i] = state
    rows = []; perpage = collections.defaultdict(lambda: collections.Counter())
    for n, (pg, l1, l2, ls) in enumerate(segs):
        nxt = segs[n + 1][0] if n + 1 < len(segs) else pg
        lo = max(pg - 1, min(kpages)); hi = max(pg, nxt)
        win = [p for p in kpages if lo <= p <= hi]
        text = '\n'.join(ls); com = '\n'.join(x for j, x in enumerate(ls) if not skip[l1 - 1 + j])
        hay_raw = '\n'.join(KN[p] for p in win); hay = R.norm_kn(hay_raw)
        er, ep = R.numbers(re.sub(r'\*\*|\bPage \d+\b|\(PDF [0-9–-]+\)|PDF [0-9–-]+|\(pp?\. [0-9–-]+\)|Rik \d+\.\d+|Pp?\. ?\d+|printed p\. \d+', '', text))
        kr, kp = R.numbers(hay_raw, True)
        miss_r = sorted(er - kr); miss_p = sorted(ep - kp, key=int)
        nq = len(re.findall(r'\[\?\]', text)); nsic = len(re.findall(r'\[sic', text)); ngl = text.count('**GLOSS**')
        nrem = len(REMARK.findall(text)); oth_en = len(OTHER_EN.findall(text))
        # quotations of the commentary absent from the window
        qd = 0
        for l, nrm in R.quotes(com):
            sc, s, e = R.align(nrm, hay)
            if not (sc >= 99.5 and nrm in hay): qd += 1
        kn_own = '\n'.join(KN[p] for p in win if p in (pg,)) or ''
        oth_kn = len(OTHER_KN.findall(hay_raw)) if n == 0 or segs[n - 1][0] != pg else 0
        rows.append((pg, l1, l2, f'{lo}-{hi}', len(ls), len(miss_r), len(miss_p), qd, nq, nsic, nrem, ngl, oth_en, oth_kn, ' '.join(miss_r[:12]), ' '.join(miss_p[:12])))
    with open(f'{out}/sieve_segments.tsv', 'w', encoding='utf8') as f:
        f.write('page\tfirst_line\tlast_line\tkn_window\tlines\tref_en_only\tnum_en_only\tquote_not_found\tq_marks\tsic\tremarks\tgloss\tother_script_en\tother_script_kn\trefs_list\tnums_list\n')
        for r in rows: f.write('\t'.join(map(str, r)) + '\n')
    # per page
    pp = collections.OrderedDict()
    for r in rows:
        pg = r[0]; c = pp.setdefault(pg, [0] * 9)
        for j, k in enumerate(range(5, 14)): c[j] += r[k]
    other_kn_pages = {p: len(OTHER_KN.findall(KN[p])) for p in kpages if OTHER_KN.search(KN[p])}
    with open(f'{out}/sieve.tsv', 'w', encoding='utf8') as f:
        f.write('page\tin_kannada\tref_en_only\tnum_en_only\tquote_not_found\tq_marks\tsic\tremarks\tgloss\tother_script_en\tother_script_kn_page\n')
        for pg, c in pp.items():
            f.write(f'{pg}\t{"yes" if pg in KN and pg not in NOTIN else "NO"}\t' + '\t'.join(map(str, c[:8])) + f'\t{other_kn_pages.get(pg, 0)}\n')
    tot = lambda j: sum(c[j] for c in pp.values())
    print(f'{len(segs)} segments over {len(pp)} English pages (first page marks); Kannada pages {kpages[0]}-{kpages[-1]}: {len(kpages)} (not in the supplied text: {sorted(NOTIN)})')
    print(f'English pages never marked (covered only by a window): {[p for p in range(kpages[0], kpages[-1] + 1) if p not in pp]}'[:600])
    print(f'ref_en_only {tot(0)} in {sum(1 for c in pp.values() if c[0])} pages; num_en_only {tot(1)} in {sum(1 for c in pp.values() if c[1])}; quote_not_found {tot(2)} in {sum(1 for c in pp.values() if c[2])}; '
          f'[?] {tot(3)} in {sum(1 for c in pp.values() if c[3])}; [sic] {tot(4)}; remarks {tot(5)}; GLOSS {tot(6)}; other scripts in English {tot(7)} on {sum(1 for c in pp.values() if c[7])} pages; '
          f'Kannada pages with letters of other scripts: {len(other_kn_pages)}')

if __name__ == '__main__': main()
