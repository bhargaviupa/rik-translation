#!/usr/bin/env python3
"""Re-check of an already translated (legacy) volume's English against the Kannada made from the supplied machine-read text.

  python3 tools/rv/recheck.py VOL [--en FILE ...] [--kn FILE] [--pages A-B] [--no-write]

Per English page (`### Page N`, N printed page or roman numeral; front matter = the block above the first `<!-- printed N -->` of the Kannada file)
writes VOL/review/recheck/pNNNN.md and VOL/review/recheck/summary.tsv. Compared (by script, nothing is decided here):
  * every `[?]` of the English page, with the Kannada words that correspond to it (Devanagari run or IAST/Latin word before the mark, converted to
    Kannada and aligned with rapidfuzz in the Kannada of that page and its neighbours);
  * every Devanagari quotation of the English page, converted to Kannada and aligned with the Kannada page: differences of letters (spacing,
    punctuation, anusvara/nasal, avagraha, line breaks ignored) are listed old -> supplied, or 'no match' when the best alignment is poor;
  * numbers and references: references with separators (8-69-12) and plain numbers of 2+ digits that the English page has and the Kannada pages
    do not, and references of the Kannada page that the English page lacks;
  * pages that exist in one source and not in the other.
There is no Kannada-versus-Kannada comparison (the scan-read Kannada of Vol 1 was a 64-page pilot and was deleted on Nov 11 2026)."""
import re, sys, os, difflib, glob
from rapidfuzz import fuzz
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'publish', 'tools', 'translit'))
from deva_to_kannada import deva2kn
KD = str.maketrans('೦೧೨೩೪೫೬೭೮೯', '0123456789')
DEVA = '[ऀ-ॣ०-ॿ]'
ROMAN = re.compile(r'^[ivxlc]+$', re.I)
NASAL = {'ಙ': 'ಕಖಗಘಙ', 'ಞ': 'ಚಛಜಝಞ', 'ಣ': 'ಟಠಡಢಣ', 'ನ': 'ತಥದಧನ', 'ಮ': 'ಪಫಬಭಮ'}

def norm_kn(s):
    """letters only: no spaces, punctuation, digits, ZWJ/ZWNJ, avagraha, line marks; homorganic nasal + virama -> anusvara"""
    s = re.sub('[^ಀ-೿]', '', s.translate(str.maketrans('', '', '‌‍')))
    s = re.sub('[೦-೯ಽ।॥]', '', s)
    s = re.sub('([ಙಞಣನಮ])್([ಕ-ಭ])', lambda m: ('ಂ' + m.group(2)) if m.group(2) in NASAL[m.group(1)] else m.group(0), s)
    return s.replace('ಃ', 'ಃ')

def page_key(h):
    return int(h) if h.isdigit() else h.lower()

def read_en(paths):
    pages = {}
    for p in paths:
        t = open(p, encoding='utf8').read()
        parts = re.split(r'(?m)^### Page ([^\s—:]+)[^\n]*\n', t)
        for i in range(1, len(parts), 2):
            k = page_key(parts[i]); pages[k] = pages.get(k, '') + '\n' + parts[i + 1]
    return pages

def read_kn(path):
    t = open(path, encoding='utf8').read()
    parts = re.split(r'(?m)^<!-- printed (\d+)(?::[^\n]*)? -->\n', t)
    pages = {'front': parts[0]}
    for i in range(1, len(parts), 2): pages[int(parts[i])] = parts[i + 1]
    notin = {int(x) for x in re.findall(r'(?m)^<!-- printed (\d+): NOT IN THE SUPPLIED', t)}
    return pages, notin

def _roman(m):
    v = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100}; t = 0; r = m.lower()
    for i, ch in enumerate(r): t += -v[ch] if i + 1 < len(r) and v[ch] < v[r[i + 1]] else v[ch]
    return str(t)

def numbers(text, kn=False):
    """references with separators (the first part may be a Roman numeral in the English: I-32-6 = 1-32-6) and plain numbers of 2+ digits"""
    if kn: text = text.translate(KD)
    text = re.sub(r'(?<![A-Za-z])([IVXLC]{1,5})(?=\s?[-.:–]\s?[0-9])', lambda m: _roman(m.group(1)), text)
    refs = {re.sub(r'\s*[-.:–—]\s*', '-', m) for m in re.findall(r'(?<![0-9.])[0-9]+(?:\s?[-.:–]\s?[0-9]+)+(?![0-9])', text)}
    plain = set(re.findall(r'(?<![0-9-])[0-9]{2,}(?![0-9-])', text))
    return refs, plain

def quotes(en):
    """Devanagari lines of the English page, deduplicated by their normalised Kannada form"""
    out, seen = [], set()
    for l in en.split('\n'):
        d = len(re.findall(DEVA, l)); l2 = re.sub(r'^[>\s*]+', '', l).strip()
        if re.search('\u094d\\s|\\S-\\S', l2) and d >= 6: continue        # the sandhi-split reading (virama before a space, hyphens): not in the print
        if d >= 6 and d >= 0.5 * len(re.sub(r'\s', '', l2)):
            kn = deva2kn(re.sub(r'\[\?\]|\[[^\]]*\]', '', l2), anusvara=False); n = norm_kn(kn)
            if len(n) >= 6 and n not in seen: seen.add(n); out.append((l2, n))
    return out

def align(q, hay):
    r = fuzz.partial_ratio_alignment(q, hay)
    return (r.score, r.dest_start, r.dest_end) if r else (0, 0, 0)

def diffs(q, h):
    sm = difflib.SequenceMatcher(None, q, h, autojunk=False); out = []
    for op, a1, a2, b1, b2 in sm.get_opcodes():
        if op == 'insert' and (a1 == 0 or a1 == len(q)): continue        # the alignment window may overshoot the quotation at its ends
        if op != 'equal': out.append((q[max(0, a1 - 6):a1] + '[' + q[a1:a2] + '→' + h[b1:b2] + ']' + q[a2:a2 + 6]))
    return out

def qmark_context(en, hay_raw, hay_norm):
    """for each `[?]`: the line, and the Kannada words that correspond to the 1-6 tokens before it"""
    res = []
    for l in en.split('\n'):
        if '[?]' not in l: continue
        for m in re.finditer(r'\[\?\]', l):
            before = re.sub(r'[*_>`"“”]', '', l[:m.start()]).split()[-6:]; after = re.sub(r'[*_>`"“”]', '', l[m.end():]).split()[:3]
            cand = None
            dv = [w for w in before if re.search(DEVA, w)]
            if dv:
                q = norm_kn(deva2kn(' '.join(dv), anusvara=False))
                if len(q) >= 3:
                    sc, s, e = align(q, hay_norm)
                    cand = ('Devanagari ' + ' '.join(dv), q, sc, s, e)
            else:
                lat = [w for w in before if re.search(r'[A-Za-zāīūṛṝḷṃḥṅñṭḍṇśṣ]{3,}', w)]
                if lat:
                    try:
                        from indic_transliteration import sanscript
                        w = re.sub(r'[^\wĀ-ɏ]', '', lat[-1])
                        sch = sanscript.IAST if re.search('[āīūṛṝḷṃḥṅñṭḍṇśṣ]', w) else sanscript.ITRANS
                        q = norm_kn(sanscript.transliterate(w, sch, sanscript.KANNADA))
                        if len(q) >= 3:
                            sc, s, e = align(q, hay_norm); cand = ('Latin ' + w, q, sc, s, e)
                    except Exception: pass
            res.append((l.strip(), before, after, cand))
    return res

def kn_words_around(hay_raw, hay_norm, s, e, width=30):
    """map a span of the normalised text back to the raw text (approximately: same letter positions)"""
    idx = [i for i, ch in enumerate(hay_raw) if 'ಀ' <= ch <= '೿' and ch not in '೦೧೨೩೪೫೬೭೮೯ಽ']
    if not idx or s >= len(idx): return ''
    a = idx[max(0, min(s, len(idx) - 1))]; b = idx[min(len(idx) - 1, max(e - 1, 0))] + 1
    return re.sub(r'\s+', ' ', hay_raw[max(0, a - width):b + width]).strip()

def main():
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    vol = a[0]; d = f'vol{vol}'
    def opt(n, multi=False):
        r = []
        for i, x in enumerate(a):
            if x == n: r.append(a[i + 1])
        return r if multi else (r[0] if r else None)
    en_files = opt('--en', True) or [p for p in (f'{d}/Rigveda_Samhita_Vol{vol}_English_Translation.md', f'{d}/Rigveda_Samhita_Vol{vol}_Gaps_English_Translation.md') if os.path.exists(p)]
    kn_file = opt('--kn') or next(p for p in (f'{d}/kannada/Rigveda_Samhita_Vol{vol}_Kannada_Text.md', f'{d}/Rigveda_Samhita_Vol{vol}_Kannada_Text.md') if os.path.exists(p))
    rng = opt('--pages'); lo, hi = (map(int, rng.split('-')) if rng else (0, 10 ** 6))
    EN = read_en(en_files); KN, NOTIN = read_kn(kn_file)
    outdir = f'{d}/review/recheck'; os.makedirs(outdir, exist_ok=True)
    if '--no-write' not in a and not rng:
        for old in glob.glob(f'{outdir}/p*.md'): os.remove(old)      # a full run replaces the page files of the earlier run
    rows = []
    keys = sorted((k for k in EN if isinstance(k, int)), key=int) + sorted((k for k in EN if not isinstance(k, int)), key=lambda x: (len(x), x))
    for k in keys:
        if isinstance(k, int) and not (lo <= k <= hi): continue
        en = EN[k]; lines = []
        if isinstance(k, int):
            kk = [x for x in (k - 1, k, k + 1) if x in KN and x not in NOTIN]; own = KN.get(k) if k not in NOTIN else None
            if k not in KN or k in NOTIN: lines.append(f'**Page {k} is not in the supplied text**' + (' (its place is marked "not in the supplied text")' if k in NOTIN else '') + ': nothing can be compared.')
            hay_raw = '\n'.join(KN[x] for x in kk)
        else:
            own = KN['front']; hay_raw = KN['front']
        if (k in KN and k not in NOTIN) or not isinstance(k, int):
            hay = norm_kn(hay_raw)
            nq = len(re.findall(r'\[\?\]', en)); qm = qmark_context(en, hay_raw, hay) if nq else []
            if qm:
                lines.append(f'### `[?]` places ({len(qm)})')
                for l, bef, aft, cand in qm:
                    lines.append(f'- English: `{l[:300]}`'); lines.append(f'  - before the mark: `{" ".join(bef)}`; after: `{" ".join(aft)}`')
                    if cand:
                        lab, q, sc, s, e = cand
                        lines.append(f'  - {lab} → Kannada `{q}`; best alignment {sc:.0f}%: supplied `{kn_words_around(hay_raw, hay, s, e)}`')
                    else: lines.append('  - no word to align (see the Kannada page)')
            nd = 0; qs = quotes(en)
            qlines = []
            for l2, n in qs:
                sc, s, e = align(n, hay); h = hay[s:e]
                if sc >= 99.5 and n in hay: continue
                if sc >= 70:
                    df = diffs(n, h)
                    if df: nd += 1; qlines.append(f'- {sc:.0f}%: English `{l2[:120]}`\n  - differences (English → supplied): ' + '; '.join(f'`{x}`' for x in df[:8]) + (f' … (+{len(df) - 8})' if len(df) > 8 else ''))
                else: nd += 1; qlines.append(f'- no match (best {sc:.0f}%): English `{l2[:120]}`')
            if qlines: lines.append(f'### Devanagari quotations that differ ({nd} of {len(qs)})'); lines += qlines
            er, ep = numbers(re.sub(r'\*\*|\bPage \d+\b', '', en)); kr, kp = numbers(hay_raw if not isinstance(k, int) else '\n'.join(KN[x] for x in kk), True)
            kr_own, kp_own = numbers(own or '', True)
            miss_r = sorted(er - kr); miss_p = sorted(ep - kp - kr_own - kp_own, key=int)[:0] if False else sorted(ep - kp)
            extra_r = sorted(kr_own - er)
            if miss_r or extra_r or miss_p:
                lines.append('### Numbers and references')
                if miss_r: lines.append('- references in the English that the supplied text (pages ±1) does not have: ' + ', '.join(f'`{x}`' for x in miss_r))
                if extra_r: lines.append('- references of the supplied page that the English page lacks: ' + ', '.join(f'`{x}`' for x in extra_r))
                if miss_p: lines.append('- plain numbers (2+ digits) in the English that the supplied text does not have: ' + ', '.join(f'`{x}`' for x in miss_p[:25]) + (' …' if len(miss_p) > 25 else ''))
            rows.append((k, nq, nd, len(miss_r), len(extra_r), len(miss_p), 0))
        else:
            rows.append((k, len(re.findall(r'\[\?\]', en)), 0, 0, 0, 0, 1))
        if lines and '--no-write' not in a:
            name = f'p{k:04d}.md' if isinstance(k, int) else f'p_{k}.md'
            open(f'{outdir}/{name}', 'w', encoding='utf8').write(f'# Vol {vol}: page {k}\n\n' + '\n'.join(lines) + '\n')
    only_kn = sorted(p for p in KN if isinstance(p, int) and p not in EN and p not in NOTIN and lo <= p <= hi)
    with open(f'{outdir}/summary.tsv', 'w', encoding='utf8') as f:
        f.write('page\tqmarks\tquote_diffs\tref_en_only\tref_kn_only\tnumber_en_only\tnot_in_supplied\n')
        for r in rows: f.write('\t'.join(map(str, r)) + '\n')
        for p in only_kn: f.write(f'{p}\t0\t0\t0\t0\t0\tnot_in_english\n')
    tot = lambda i: sum(r[i] for r in rows)
    print(f'{len(rows)} English pages compared; [?] {tot(1)} (on {sum(1 for r in rows if r[1])} pages); pages with Devanagari quotations that differ: {sum(1 for r in rows if r[2])} ({tot(2)} quotations); '
          f'pages with a reference only in the English: {sum(1 for r in rows if r[3])} ({tot(3)}); with a reference only in the supplied text: {sum(1 for r in rows if r[4])} ({tot(4)}); '
          f'with plain numbers only in the English: {sum(1 for r in rows if r[5])} ({tot(5)}); pages with none of these: {sum(1 for r in rows if not any(r[1:6]))}; '
          f'English pages not in the supplied text: {[r[0] for r in rows if r[6]]}; supplied pages with no English page: {only_kn}')

if __name__ == '__main__': main()
