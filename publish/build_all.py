#!/usr/bin/env python3
"""Build the review PDFs of many volumes the same way and record the result (user, Nov 26 2026: the rules go into the requirements and the
shared scripts first, then they are applied uniformly).

  python3 publish/build_all.py [N …] [--cleanup] [--kan]

For each volume: (--cleanup: `tools/rv/cleanup_remarks.py N all --write` first, with the headings of the book compared before and after),
the volume's builder (1: build_vol1.py; 2: build_vol2.py; 3: build.py; 4-10: build_vol45.py; a volume with volN/pubcfg.json: volbook.py),
then publish/pdf_check.py.  Every builder runs the same print step (publish/printfix.py, publish/style_footer.css).
Writes publish/BUILD_STATUS.md: one row per volume with the date, pages, what the print step did and what the check found.
Without volume numbers: every volume that has a builder."""
import re, sys, subprocess, pathlib, datetime, json
PUB = pathlib.Path(__file__).resolve().parent; ROOT = PUB.parent
sys.path.insert(0, str(PUB))
def builder(n):
    cfgp = ROOT / f'vol{n}' / 'pubcfg.json'
    if cfgp.exists() and not json.loads(cfgp.read_text(encoding='utf8')).get('kannada_only'): return ['python3', str(PUB / 'volbook.py'), str(n)], ROOT
    if n == 1: return ['python3', 'build_vol1.py', 'full'], PUB
    if n == 2: return ['python3', 'build_vol2.py', 'full'], PUB
    if n == 3: return ['python3', 'build.py', '3', 'full'], PUB
    if 4 <= n <= 10: return ['python3', 'build_vol45.py', str(n), 'full'], PUB
    return None, None
def heads(n):
    f = PUB / 'out' / f'vol{n}_full.html'
    if not f.exists(): f = PUB / 'out' / f'vol{n}_full_Eng.html'
    return [re.sub(r'<[^>]+>', '', h).strip() for h in re.findall(r'<h[12][^>]*>(.*?)</h[12]>', f.read_text(encoding='utf8'), flags=re.S)] if f.exists() else []
def run(cmd, cwd):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr
def check(pdf):
    r = subprocess.run(['python3', str(PUB / 'pdf_check.py'), str(pdf)], capture_output=True, text=True).stdout
    pages = re.search(r': (\d+) pages', r); fails = re.findall(r'FAIL\s+(.*)', r); counts = re.search(r'COUNT (.*?)\s{3}', r)
    return (pages.group(1) if pages else '?'), fails, (counts.group(1) if counts else '')
def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]; cleanup = '--cleanup' in sys.argv
    vols = [int(a) for a in args] or [n for n in range(1, 31) if builder(n)[0]]
    rows = []
    for n in vols:
        cmd, cwd = builder(n)
        if not cmd: rows.append((n, 'no builder (no pubcfg.json)', '', '', '', '')); print(f'vol{n}: no builder'); continue
        note = ''
        if cleanup and not (ROOT / f'vol{n}' / 'pubcfg.json').exists():
            run(cmd, cwd); before = heads(n)
            rc, out = run(['python3', str(ROOT / 'tools' / 'rv' / 'cleanup_remarks.py'), str(n), 'all', '--write'], ROOT)
            cnt = {}
            for k, v in re.findall(r': (session|paren|ownnote|twin|leaders) (\d+)', out): cnt[k] = cnt.get(k, 0) + int(v)
            note = 'clean-up: ' + ', '.join(f'{k} {v}' for k, v in cnt.items() if v) if any(cnt.values()) else 'clean-up: nothing to remove'
        rc, out = run(cmd, cwd)
        cfgp = ROOT / f'vol{n}' / 'pubcfg.json'
        if not rc and cfgp.exists() and json.loads(cfgp.read_text(encoding='utf8')).get('kannada_only'):        # the Kannada book of an old volume
            rc2, out2 = run(['python3', str(PUB / 'volbook.py'), str(n), 'kan'], ROOT); out += out2
        if rc: rows.append((n, 'BUILD FAILED: ' + out.strip().split('\n')[-1][:150], '', '', '', note)); print(f'vol{n}: build failed'); continue
        if cleanup and note.startswith('clean-up:') and 'nothing' not in note:
            after = heads(n); lost = [h for h in before if h not in after]
            if lost: note += f'; HEADINGS LOST after clean-up: {len(lost)} (e.g. {lost[0][:50]!r}) — look before keeping'
        fixline = '; '.join(m for m in re.findall(r'\[printfix\] (.*)', out)[:1])
        pdfs = sorted((ROOT / f'vol{n}' / 'review').glob(f'vol{n}_full*.pdf'))
        for pdf in pdfs:
            pages, fails, counts = check(pdf)
            rows.append((n, pdf.name, pages, '; '.join(fails) or 'passes', counts, (fixline + ('; ' if note and fixline else '') + note) if pdf == pdfs[0] else ''))
            print(f'vol{n}: {pdf.name} {pages} pages; {"; ".join(fails) or "passes"}')
    f = PUB / 'BUILD_STATUS.md'; old = {}
    if f.exists():
        for l in f.read_text(encoding='utf8').split('\n'):
            m = re.match(r'\| (\d+) \| ([^|]*) \|', l)
            if m: old[(int(m.group(1)), m.group(2).strip())] = l
    today = datetime.datetime.now(datetime.timezone.utc).strftime('%-d %b %Y %H:%M UTC')
    for n, name, pages, res, counts, note in rows:
        for k in [k for k in old if k[0] == n and (not name.endswith('.pdf') or not k[1].endswith('.pdf') or k[1] == name)]: old.pop(k)
        old[(n, name)] = f'| {n} | {name} | {today} | {pages} | {res} | {counts} | {note} |'
    head = ('# Build status of the review PDFs\n\n*Written by `publish/build_all.py`; do not edit by hand. Every builder runs the same print step (`publish/printfix.py`, `publish/style_footer.css`; '
            'rules: `docs/REQUIREMENTS.md` A4 "Print rules", B4.6, D19). "Check" is `publish/pdf_check.py`; the counts are lines of the PDF that still show a mark or remark (0 wanted for a release).*\n\n'
            '| Vol | PDF | Built | Pages | Check | Still printed | Print step and clean-up |\n|---|---|---|---|---|---|---|\n')
    f.write_text(head + '\n'.join(old[k] for k in sorted(old)) + '\n', encoding='utf8')
    print('written', f.relative_to(ROOT))
if __name__ == '__main__': main()
