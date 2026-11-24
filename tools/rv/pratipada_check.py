#!/usr/bin/env python3
"""Check the Pratipadārtha (word-meaning) words of a volume against the Wikisource Pada-pāṭha, Ṛk by Ṛk. Edits NOTHING.

  python3 tools/rv/pratipada_check.py N            # volume N: its Kannada text, mandalas from volcfg.json, report volN/review/pratipada_check.tsv
  python3 tools/rv/pratipada_check.py FILE.md --mandala 7[,8] [--out X.tsv]     # any file (e.g. a merged OCR file, or a window kn.md)

Needs refs/wikisource/index/ws.sqlite (python3 tools/rv/ws_index.py build; it is built from the committed refs/wikisource/raw/).

Method. The text is cut at every Pada-pāṭha block (*ಪದಪಾಠಃ* / ## ಪಡಪಾಠಃ). The block (Kannada → Devanagari, normalised) is matched to the
closest reference Ṛk of the volume's mandalas (rapidfuzz; the score is reported; below 75 the Ṛk is not trusted and its words are
listed as 'noref'). The Pratipadārtha section after it ('WORD—meaning । WORD—meaning …') gives one word per entry; each word is
compared with the words of THAT Ṛk (Pada-pāṭha words, and the Saṃhitā words for forms with sandhi). Spelling is normalised only for
what the sources differ in: accents, ZWNJ/ZWJ, avagraha/hyphen, final virama, visarga, nasal + consonant = anusvāra.
Status per word:  ok            found among the Ṛk's words
                  fix           not found; exactly ONE Ṛk word is within one edit (the proposal) → a candidate for `batch.py fix` (certain readings only)
                  fix-certain   as 'fix', and the supplied Pada block of the same Ṛk already has the proposed word: only the Pratipadārtha entry is off
                  near          not found; several or farther candidates (listed) → the editor's decision / **NOTE**
                  absent        no candidate near → editor
                  noref         the Ṛk could not be matched to the reference
The supplied Pada block itself is checked the same way (status of its words: ok / fix / near / absent, kind 'pada').
A mismatch means "look here", not "the supplied text is wrong": the Wikisource Pada has typos (docs/WIKISOURCE_NOTES.md), and the
bhāṣya's own forms differ from the Pada. Letters of the supplied text are never changed by this script."""
import json, pathlib, re, sqlite3, sys
from rapidfuzz import fuzz, process
from rapidfuzz.distance import Levenshtein
from indic_transliteration import sanscript as S

ROOT = pathlib.Path(__file__).resolve().parents[2]
DB = ROOT / 'refs' / 'wikisource' / 'index' / 'ws.sqlite'
DROP = re.compile('[॒॑॓॔᳐-᳿‌‍​­]')
SPLIT = re.compile(r'[\s।॥|,;:!?.()\[\]\d०-९*>]+')


def norm(w):
    w = DROP.sub('', w)
    w = re.sub('[ऽ\\-]', '', w)
    w = re.sub('[नमणङञ]्(?=[क-ह])', 'ं', w)           # nasal + virama + consonant -> anusvara
    w = re.sub('म्$', 'ं', w)                          # final m = anusvara (the print writes ಂ)
    w = w.replace('ः', '').replace('ँ', 'ं')
    w = re.sub('(?<=[क-ह])्$', '', w)                   # final virama
    w = w.replace('ळ', 'ल')
    return w


def kn2dev(t):
    return S.transliterate(DROP.sub('', t), S.KANNADA, S.DEVANAGARI)


def words(t):
    return [w for w in SPLIT.split(t) if w]


def load_ref(mandalas):
    con = sqlite3.connect(DB)
    ref = []
    q = ','.join('?' * len(mandalas))
    for r, pada, sam in con.execute(f'select ref,pada,samhita from rik where m in ({q}) order by m,s,r', mandalas):
        pw = [norm(w) for w in words(pada or '')]
        sw = [norm(w) for w in words(re.sub(r'॥.*', '', sam or ''))]
        ref.append((r, pw, set(sw), ' '.join(pw)))
    return ref


PADA = re.compile(r'^\W*(?:\*+)?\W*(?:ಪದಪಾಠಃ|ಪಡಪಾಠಃ|ಪದಪಾಠ|ಪಡಪಾಠ)\W*$')
PRAT = re.compile(r'^\W*(?:\*+)?\W*(?:ಪ್ರತಿಪದಾರ್ಥ|ಪ್ರತಿಸದಾರ್ಥ|ಪ್ರತಿಪದಾರ್ಥಃ)\W*$')
END = re.compile(r'^\W*(?:\*+)?\W*(?:\[.*|ಭಾವಾರ್ಥ.*|ಭಾಷಾರ್ಥ.*|English Translation.*|ಸಂಹಿತಾಪಾಠಃ.*|ಸಾಯಣಭಾಷ್ಯಂ.*|ಸಾಯಣಭಾಷ್ಯಮ್.*)$')


def sections(lines):
    """yield (pada_line_no, pada_text, prat_line_no, [entry words (Kannada)])"""
    i, n = 0, len(lines)
    while i < n:
        if PADA.match(lines[i]) or (lines[i].startswith('#') and re.search('ಪದಪಾಠ|ಪಡಪಾಠ', lines[i])):
            pl = i + 1; j = i + 1; buf = []
            while j < n and not (PRAT.match(lines[j]) or END.match(lines[j]) or lines[j].startswith('#') or PADA.match(lines[j])):
                buf.append(lines[j]); j += 1
            # pratipada may follow after the bhashya block: search ahead up to the next pada block
            k = j; pr = None
            while k < n and not (PADA.match(lines[k]) or re.search('ಪದಪಾಠ|ಪಡಪಾಠ', lines[k]) and lines[k].startswith('#')):
                if PRAT.match(lines[k]) or (lines[k].startswith('#') and re.search('ಪ್ರತಿಪದಾರ್ಥ|ಪ್ರತಿಸದಾರ್ಥ', lines[k])): pr = k; break
                k += 1
            ents = []
            if pr is not None:
                m = pr + 1; body = []
                while m < n and not (END.match(lines[m]) or lines[m].startswith('#') or PADA.match(lines[m])):
                    body.append(lines[m]); m += 1
                txt = ' '.join(body)
                for e in re.split(r'\s*[।|!]\s*', txt):
                    e = re.sub(r'\([^)]*\)', ' ', e)
                    mm = re.match(r'\s*([^—\-–]+?)\s*[—–\-]', e)
                    if mm: ents.append(mm.group(1).strip())
            yield pl, ' '.join(buf), (pr + 1 if pr is not None else None), ents
            i = max(j, i + 1)
        else:
            i += 1


def judge(w, rw):
    """w: normalised word; rw: set of reference words of the Ṛk → (status, proposals)"""
    if w in rw: return 'ok', []
    near = sorted((Levenshtein.distance(w, x), x) for x in rw)
    c1 = [x for d, x in near if d <= 1]
    if len(c1) == 1: return 'fix', c1
    c2 = [x for d, x in near if d <= max(2, len(w) // 4)][:4]
    return ('near', c2) if c2 else ('absent', [])


def main():
    a = [x for x in sys.argv[1:] if not x.startswith('--')]
    opt = {sys.argv[i]: sys.argv[i + 1] for i in range(1, len(sys.argv) - 1) if sys.argv[i].startswith('--')}
    if not a: sys.exit(__doc__)
    if a[0].isdigit():
        cfg = json.load(open(ROOT / f'vol{a[0]}' / 'volcfg.json'))
        path = ROOT / cfg['out']['kn']; mand = cfg.get('mandalas') or [cfg['mandala']]
        out = pathlib.Path(opt.get('--out') or ROOT / f'vol{a[0]}' / 'review' / 'pratipada_check.tsv')
    else:
        path = pathlib.Path(a[0]); mand = [int(x) for x in opt['--mandala'].split(',')]
        out = pathlib.Path(opt.get('--out') or path.with_suffix('.pratipada_check.tsv'))
    if not DB.exists(): sys.exit('missing refs/wikisource/index/ws.sqlite: run  python3 tools/rv/ws_index.py build')
    ref = load_ref(mand)
    choices = [r[3] for r in ref]
    lines = path.read_text(encoding='utf8').split('\n')
    rows = []; stat = {}
    for pl, ptxt, prl, ents in sections(lines):
        pw = [norm(w) for w in words(kn2dev(ptxt))]
        if not pw: continue
        best = process.extractOne(' '.join(pw), choices, scorer=fuzz.ratio)
        rk, score = (ref[best[2]], best[1]) if best else (None, 0)
        trusted = rk is not None and score >= 75
        rw = (set(rk[1]) | rk[2]) if trusted else set()
        rid = rk[0] if trusted else ''
        for kind, ln, ws in (('pada', pl, pw), ('prat', prl, [norm(x) for e in ents for x in words(kn2dev(e))])):
            orig = pw if kind == 'pada' else None
            for idx, w in enumerate(ws):
                if not w: continue
                if not trusted: st, pr = 'noref', []
                else:
                    st, pr = judge(w, set(rk[1]) | rk[2] if kind == 'prat' else set(rk[1]))
                    if kind == 'prat' and st == 'fix' and pr[0] in set(pw): st = 'fix-certain'   # the supplied Pada block of this Ṛk has the reference word
                stat[(kind, st)] = stat.get((kind, st), 0) + 1
                if st != 'ok':
                    rows.append((kind, ln, rid, f'{score:.0f}', w, st, ' / '.join(pr)))
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, 'w', encoding='utf8') as f:
        f.write('kind\tline\tref\tmatch\tword(devanagari,normalised)\tstatus\tproposal\n')
        for r in rows: f.write('\t'.join(map(str, r)) + '\n')
    print(f'{path.name}: mandalas {mand}; report {out} ({len(rows)} rows not ok)')
    for k in sorted(stat): print(' ', k[0], k[1], stat[k])


if __name__ == '__main__':
    main()
