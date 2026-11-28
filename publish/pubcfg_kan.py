#!/usr/bin/env python3
"""Make volN/pubcfg.json for the Kannada book of a volume (Nov 28 2026; one tool, data in publish/kan_titles.tsv).

  python3 publish/pubcfg_kan.py [N …] [--list]

Writes a `kannada_only` pubcfg for each named volume (default: every row of the table) that has a Kannada Text file and no pubcfg yet; never overwrites one.
Press and year are put in only where the table has them (from a colophon); an empty press/year is not guessed: the title page then names the series only,
and the volume is listed as "press/year to be supplied".  Build: `python3 publish/build_all.py N --kan` (or `python3 publish/volbook.py N kan`)."""
import csv, json, sys, pathlib
PUB = pathlib.Path(__file__).resolve().parent; ROOT = PUB.parent
SERIES = 'Śrī Jayacāmarājendra Vedaratna-mālā'
def main(a):
    rows = {int(r['vol']): r for r in csv.DictReader(open(PUB / 'kan_titles.tsv', encoding='utf8'), delimiter='\t')}
    vols = [int(x) for x in a if x.isdigit()] or sorted(rows)
    todo = []
    for v in vols:
        r = rows.get(v); kn = ROOT / f'vol{v}' / f'Rigveda_Samhita_Vol{v}_Kannada_Text.md'; p = ROOT / f'vol{v}' / 'pubcfg.json'
        if not r: print(f'vol{v}: no row in kan_titles.tsv'); continue
        if not kn.exists() or kn.stat().st_size < 2000: print(f'vol{v}: no Kannada Text file'); continue
        if p.exists(): print(f'vol{v}: pubcfg.json exists (kept)'); continue
        press, year = r['press'].strip(), r['year'].strip()
        cfg = {'vol': v, 'range_line': r['range_line'], 'adhyaya_line': r['adhyaya_line'].strip(),
               'imprint': SERIES + ('<br>' + press + (', ' + year if year else '') if press else ''),
               'year': year, 'press': press, 'kannada_md': f'vol{v}/Rigveda_Samhita_Vol{v}_Kannada_Text.md', 'out': f'vol{v}_full', 'kannada_only': True,
               '_note': 'Kannada book only (publish/pubcfg_kan.py from publish/kan_titles.tsv: ' + r['source'] + '). The English book of this volume has no print build yet.'}
        if not press: todo.append(v)
        p.write_text(json.dumps(cfg, ensure_ascii=False, indent=1) + '\n', encoding='utf8'); print(f'vol{v}: pubcfg.json written')
    if todo: print('press/year to be supplied (not in the Kannada file, not guessed):', ', '.join(map(str, todo)))
if __name__ == '__main__': main(sys.argv[1:])
