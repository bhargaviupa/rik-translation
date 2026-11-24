#!/usr/bin/env python3
"""Export the Wikisource index (refs/wikisource/index/ws.sqlite) as plain UTF-8 tab-separated text, one file per maṇḍala, for reading.

    python3 tools/rv/ws_export.py            # writes refs/wikisource/export/M00.tsv (the bhūmikā) … M10.tsv

Columns: reference · layer · Devanagari text. Layers: `samhita` (accented Saṃhitā of the Ṛk), `pada` (accented Pada, plain where the page has
no accented one), `bhashya` (one paragraph of Sāyaṇa's text; reference M.S.R.P; R = 0 is his introduction to the sūkta). Lines of a verse are
joined with ` / `. M00 holds Sāyaṇa's Ṛgveda-bhāṣya-bhūmikā in four parts (S = 1–4; R = printed page). Nothing is changed or corrected;
the text is as the index has it (see docs/WIKISOURCE_NOTES.md). Needs the index: python3 tools/rv/ws_index.py build.
"""
import pathlib, sqlite3, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
DB = ROOT / 'refs' / 'wikisource' / 'index' / 'ws.sqlite'
OUT = ROOT / 'refs' / 'wikisource' / 'export'


def main():
    if not DB.exists(): sys.exit('no index: run  python3 tools/rv/ws_index.py build')
    OUT.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(DB)
    one = lambda s: s.replace('\n', ' / ').replace('\t', ' ')
    tot = 0
    for m in range(0, 11):
        rows = []
        for s, in con.execute('select s from sukta where m=? order by s', (m,)):
            if m:
                note = con.execute('select rishi, note from sukta where m=? and s=?', (m, s)).fetchone()
                rows.append((f'{m}.{s}', 'sukta', one(f'{note[0]} | {note[1]}')))
            ritems = {r: (a, p) for r, a, p in con.execute('select r, coalesce(nullif(samhita_acc,\'\'), samhita), coalesce(nullif(pada_acc,\'\'), pada) from rik where m=? and s=?', (m, s))}
            paras = {}
            for r, p, d in con.execute('select r, p, deva from para where m=? and s=? order by r, p', (m, s)):
                paras.setdefault(r, []).append((p, d))
            for r in sorted(set(ritems) | set(paras)):
                if r in ritems and m:
                    a, p = ritems[r]
                    rows.append((f'{m}.{s}.{r}', 'samhita', one(a)))
                    if p: rows.append((f'{m}.{s}.{r}', 'pada', one(p)))
                for p, d in paras.get(r, []):
                    rows.append((f'{m}.{s}.{r}.{p}', 'bhashya', one(d)))
        (OUT / f'M{m:02d}.tsv').write_text('reference\tlayer\ttext\n' + ''.join('\t'.join(x) + '\n' for x in rows), encoding='utf-8')
        tot += len(rows)
        print(f'M{m:02d}.tsv: {len(rows)} rows')
    print(f'{tot} rows in {OUT.relative_to(ROOT)}; {sum(f.stat().st_size for f in OUT.glob("*.tsv")) / 1e6:.1f} MB')


if __name__ == '__main__':
    main()
