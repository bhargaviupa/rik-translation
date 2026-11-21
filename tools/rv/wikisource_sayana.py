#!/usr/bin/env python3
"""Fetch Sāyaṇa's bhāṣya (with Saṃhitā and Pada) for sūktas from sa.wikisource.org, as data files.

    python3 tools/rv/wikisource_sayana.py fetch M S [S2]      # sūktas M.S .. M.S2, saved to refs/wikisource/
    python3 tools/rv/wikisource_sayana.py show M S [N]        # print what was saved (N = one Ṛk; 0 = introduction)

Page: https://sa.wikisource.org/wiki/ऋग्वेदः_सूक्तं_M.S  (HTML only; the raw/API routes are refused here).
Saved per sūkta: refs/wikisource/M<mm>_S<sss>.json =
  {"url", "revision", "fetched", "editor_notes" (the wiki editors' टिप्पणी boxes: NOT Sāyaṇa, kept apart), "intro": str, "rks": [{"n", "samhita", "pada_accented", "pada", "bhashya"}], "checks": [...]}
Nothing is corrected. The page's own text is kept as it is (accents, quotation marks, spaces).
`checks` lists what the parser could not confirm (Ṛk count, accent-stripped Saṃhitā against the plain Saṃhitā at the
top of the page); an empty list means the parse agrees with the page's own plain verse text.
It is a wiki: the text is a source to compare with, not an authority (see docs/REQUIREMENTS.md Part K).
"""
import html, json, pathlib, re, subprocess, sys, time, urllib.parse, datetime

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / 'refs' / 'wikisource'
URL = 'https://sa.wikisource.org/wiki/' + urllib.parse.quote('ऋग्वेदः_सूक्तं_') + '{m}.{s}'  # numbers in Devanagari digits
TODEV = str.maketrans('0123456789', '०१२३४५६७८९')
ACC = re.compile('[॒॑॓॔᳐-᳿]')
DIG = str.maketrans('०१२३४५६७८९', '0123456789')
MARK = re.compile(r'॥\s*([०-९0-9]+)\s*(?:॥)?\s*$')


def fetch_html(m, s):
    r = subprocess.run(['curl', '-sS', '-L', '-m', '60', '-w', '\n%{http_code}', URL.format(m=str(m).translate(TODEV), s=str(s).translate(TODEV))],
                       capture_output=True)
    body, _, code = r.stdout.decode('utf-8', 'replace').rpartition('\n')
    if code.strip() != '200':
        raise RuntimeError(f'{m}.{s}: HTTP {code.strip()} {r.stderr.decode()[:200]}')
    return body


def text_of(fragment):
    t = re.sub(r'<br\s*/?>', '\n', fragment)
    return html.unescape(re.sub(r'<[^>]+>', '', t)).strip()


def strip_acc(x):
    x = ACC.sub('', x)
    x = re.sub(r'[\s।॥ऽ]|[०-९0-9]', '', x)
    return re.sub('[ङञणनम]्(?=[क-ह])', 'ं', x)  # the page spells nasals both ways; compare them as one


def parse(page, m, s):
    checks = []
    rev = re.search(r'"wgRevisionId":(\d+)', page)
    # plain Saṃhitā at the top (before the collapsible bhāṣya)
    k = page.find('सायणभाष्यम्')
    if k < 0:
        raise RuntimeError('no bhāṣya section on the page')
    top, rest = page[:k], page[k:]
    top_txt = text_of(top[top.rfind('mw-content-text'):])
    plain, buf = [], []
    for line in top_txt.split('\n'):
        line = line.strip()
        if not line:
            continue
        buf.append(line)
        if re.search(r'॥\s*[०-९0-9]+\s*॥\s*$', line):
            plain.append('\n'.join(buf)); buf = []
    # paragraphs of the bhāṣya section
    body = rest[rest.find('mw-collapsible-content'):]
    end = body.find('</big></big></div>')               # Sāyaṇa's own box ends here; later boxes are wiki editors' notes
    tipp = [text_of(x) for x in re.findall(r'<b>टिप्पणी</b>.*?mw-collapsible-content">(.*?)</div>', body[end:], flags=re.S)]
    body = body[:end] if end > 0 else body
    paras = []
    for p in re.findall(r'<p>(.*?)</p>', body, flags=re.S):
        t = text_of(p)
        for line in t.split('\n'):
            line = line.strip()
            if line:
                paras.append(line)
    for k_, l_ in enumerate(paras):                      # the site's list of sūkta links follows the last bhāṣya
        if re.fullmatch(r'सूक्तं\s+[०-९]+\.[०-९]+', l_):
            paras = paras[:k_]
            break
    # per Ṛk three marker lines: Saṃhitā (accented, no ' । '), Pada (accented, with ' । '), Pada (plain, with ' । ')
    def mk(i):
        mm = MARK.search(paras[i])
        return int(mm.group(1).translate(DIG)) if mm else None
    rks, i = [], 0
    while i < len(paras):
        l = paras[i]
        if mk(i) is not None and ACC.search(l) and ' । ' not in l and len(l) < 300:
            n, a = mk(i), i
            b = next((j for j in range(a + 1, min(a + 6, len(paras))) if mk(j) == n and ACC.search(paras[j])), None)
            c = next((j for j in range(b + 1, min(b + 6, len(paras))) if mk(j) == n and not ACC.search(paras[j])), None) if b else None
            if b is None or c is None:
                checks.append(f'Ṛk {n}: could not find its two Pada lines after line {a}')
                i += 1
                continue
            st = a
            while st - 1 >= 0 and ACC.search(paras[st - 1]) and ' । ' not in paras[st - 1] and len(paras[st - 1]) < 200 \
                    and mk(st - 1) is None and (not rks or st - 1 > rks[-1]['_c']):
                st -= 1
            rks.append({'n': n, '_a0': st, '_a': a, '_b': b, '_c': c})
            i = c + 1
        else:
            i += 1
    # assemble
    first_start = rks[0]['_a0'] if rks else len(paras)
    intro = '\n'.join(paras[:first_start]).strip()
    out = []
    for j, r in enumerate(rks):
        nxt = rks[j + 1]['_a0'] if j + 1 < len(rks) else len(paras)
        out.append({
            'n': r['n'],
            'samhita': '\n'.join(paras[r['_a0']:r['_a'] + 1]),
            'pada_accented': '\n'.join(paras[r['_a'] + 1:r['_b'] + 1]),
            'pada': '\n'.join(paras[r['_b'] + 1:r['_c'] + 1]),
            'bhashya': '\n'.join(paras[r['_c'] + 1:nxt]).strip(),
        })
    # checks
    if [r['n'] for r in out] != list(range(1, len(out) + 1)):
        checks.append(f'Ṛk numbers are not 1..{len(out)}: {[r["n"] for r in out]}')
    if plain and len(plain) != len(out):
        checks.append(f'plain Saṃhitā at the top has {len(plain)} Ṛks, the parse {len(out)}')
    else:
        for r, pl in zip(out, plain):
            if not strip_acc(pl).endswith(strip_acc(r['samhita'])):  # (first plain Ṛk may carry the page header)
                checks.append(f'Ṛk {r["n"]}: accent-stripped Saṃhitā differs from the plain Saṃhitā at the top of the page')
    for r in out:
        if not r['bhashya']:
            checks.append(f'Ṛk {r["n"]}: no bhāṣya text found')
    return {'url': URL.format(m=str(m).translate(TODEV), s=str(s).translate(TODEV)), 'revision': int(rev.group(1)) if rev else None, 'editor_notes': tipp,
            'fetched': datetime.date.today().isoformat(), 'intro': intro, 'rks': out, 'checks': checks}


def path_for(m, s):
    return OUT / f'M{int(m):02d}_S{int(s):03d}.json'


def fetch(m, s):
    d = parse(fetch_html(m, s), m, s)
    OUT.mkdir(parents=True, exist_ok=True)
    path_for(m, s).write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return d


def main(a):
    if len(a) < 3 or a[0] not in ('fetch', 'show'):
        sys.exit(__doc__)
    cmd, m = a[0], int(a[1])
    if cmd == 'fetch':
        lo = int(a[2]); hi = int(a[3]) if len(a) > 3 else lo
        for s in range(lo, hi + 1):
            try:
                d = fetch(m, s)
                print(f'{m}.{s}: {len(d["rks"])} Ṛks, intro {len(d["intro"])} letters, revision {d["revision"]}, '
                      f'{len(d["checks"])} checks open' + ''.join(f'\n   - {c}' for c in d['checks']))
            except Exception as e:
                print(f'{m}.{s}: FAILED {e}')
            time.sleep(0.7)
    else:
        d = json.loads(path_for(m, int(a[2])).read_text(encoding='utf-8'))
        n = int(a[3]) if len(a) > 3 else None
        if n in (None, 0):
            print('## intro\n' + d['intro'] + '\n')
        for r in d['rks']:
            if n in (None, r['n']):
                print(f'## Ṛk {r["n"]}\n{r["samhita"]}\n{r["pada"]}\n{r["bhashya"]}\n')


if __name__ == '__main__':
    main(sys.argv[1:])
