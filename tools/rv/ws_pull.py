#!/usr/bin/env python3
"""Pull the Ṛgveda pages of sa.wikisource.org through its API and keep the raw wikitext (data only).

    python3 tools/rv/ws_pull.py            # list the pages, fetch what is new or changed, write refs/wikisource/raw/
    python3 tools/rv/ws_pull.py --force    # fetch everything again

Pages taken: every `ऋग्वेदः सूक्तं M.S` (the 1028 sūktas), the ten `ऋग्वेदः मण्डल N` pages, `ऋग्वेदः खिलसूक्तानि/…`,
`ऋग्वेदः ऋषिसूची`, `ऋग्वेदः/संहिता/सस्वरपाठः/…` and `ऋग्वेदः`. (The Brāhmaṇa and Āraṇyaka pages under `ऋग्वेदः/…`
are left out: they are not the Saṃhitā.) Nothing is changed: each line of a file is one page,
{"title","pageid","revid","parentid","timestamp","fetched","wikitext"}; the revision id says exactly which text it is.
Files: refs/wikisource/raw/M01.jsonl … M10.jsonl (the sūktas of a maṇḍala, in order) and other.jsonl.
The site asks automated clients to send a descriptive User-Agent; it carries no personal detail.
"""
import datetime, json, pathlib, re, subprocess, sys, time, urllib.parse

ROOT = pathlib.Path(__file__).resolve().parents[2]
RAW = ROOT / 'refs' / 'wikisource' / 'raw'
UA = 'rik-reference-fetch/1.0 (private research tool)'
API = 'https://sa.wikisource.org/w/api.php?'
DEV = str.maketrans('०१२३४५६७८९', '0123456789')


def api(**p):
    for attempt in range(4):
        r = subprocess.run(['curl', '-sS', '-m', '90', '-A', UA, API + urllib.parse.urlencode(p)], capture_output=True)
        try:
            return json.loads(r.stdout)
        except Exception:
            time.sleep(2 * (attempt + 1))
    raise RuntimeError('API did not answer: ' + str(p)[:200])


def all_titles():
    out, cont = [], {}
    while True:
        d = api(action='query', format='json', list='allpages', apprefix='ऋग्वेदः', aplimit='500', apnamespace='0', **cont)
        out += [x['title'] for x in d['query']['allpages']]
        if 'continue' not in d:
            return out
        cont = {'apcontinue': d['continue']['apcontinue']}


def wanted(t):
    return bool(re.fullmatch(r'ऋग्वेदः सूक्तं [०-९]+\.[०-९]+|ऋग्वेदः मण्डल [०-९]+|ऋग्वेदः खिलसूक्तानि/अध्यायः [०-९]+|'
                             r'ऋग्वेदः ऋषिसूची|ऋग्वेदः/संहिता/सस्वरपाठः/.+|ऋग्वेदः', t))


def key(t):
    m = re.fullmatch(r'ऋग्वेदः सूक्तं ([०-९]+)\.([०-९]+)', t)
    return (0, int(m.group(1).translate(DEV)), int(m.group(2).translate(DEV))) if m else (1, 0, t)


def main(a):
    force = '--force' in a
    RAW.mkdir(parents=True, exist_ok=True)
    titles = sorted((t for t in all_titles() if wanted(t)), key=key)
    have = {}
    for f in RAW.glob('*.jsonl'):
        for line in f.read_text(encoding='utf-8').splitlines():
            r = json.loads(line); have[r['title']] = r
    got, today = {}, datetime.date.today().isoformat()
    todo = [t for t in titles if force or t not in have]
    print(f'{len(titles)} pages on the site, {len(have)} already saved, {len(todo)} to fetch')
    def fetch(batch):
        d = api(action='query', format='json', prop='revisions', rvprop='ids|timestamp|content', rvslots='main',
                titles='|'.join(batch))
        for p in d['query']['pages'].values():
            rv = p.get('revisions')
            if not rv:
                print('  no text for', p.get('title')); continue
            r = rv[0]
            got[p['title']] = {'title': p['title'], 'pageid': p['pageid'], 'revid': r['revid'], 'parentid': r.get('parentid'),
                               'timestamp': r['timestamp'], 'fetched': today, 'wikitext': r['slots']['main']['*']}
    for i in range(0, len(todo), 40):
        batch = todo[i:i + 40]
        try:
            fetch(batch)
        except RuntimeError:
            for t1 in batch:                      # a batch the API would not answer: one page at a time
                try:
                    fetch([t1])
                except RuntimeError:
                    print('  FAILED', t1)
        print(f'  {min(i + 40, len(todo))}/{len(todo)}', flush=True)
        time.sleep(0.5)
    have.update(got)
    files = {}
    for t in titles:
        if t not in have:
            print('MISSING', t); continue
        m = re.fullmatch(r'ऋग्वेदः सूक्तं ([०-९]+)\.[०-९]+', t)
        name = f'M{int(m.group(1).translate(DEV)):02d}' if m else 'other'
        files.setdefault(name, []).append(have[t])
    for name, rows in files.items():
        (RAW / f'{name}.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows), encoding='utf-8')
    n = sum(len(v) for v in files.values())
    size = sum(f.stat().st_size for f in RAW.glob('*.jsonl'))
    print(f'saved {n} pages in {len(files)} files, {size / 1e6:.1f} MB, to {RAW.relative_to(ROOT)}')


if __name__ == '__main__':
    main(sys.argv[1:])
