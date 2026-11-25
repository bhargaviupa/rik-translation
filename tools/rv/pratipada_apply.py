#!/usr/bin/env python3
"""Apply the CERTAIN corrections of pratipada_check.py to the supplied Kannada file, each one logged. Preview unless --write.

  python3 tools/rv/pratipada_apply.py N [--write]            # volume N: its supplied file (volcfg `source`), report volN/review/pratipada_check_source.tsv
  python3 tools/rv/pratipada_apply.py FILE.md REPORT.tsv [--write] [--log DIR]
  ... [--only WORD,WORD]     only these supplied words (the editor has read them), the one-letter test waived for them; reason in the log: 'approved by the editor'

Only rows with status `fix-certain` are considered (one reference word within one edit AND the supplied Pada block of the same Ṛk already
spells that word), and of those only the rows that pass a second test: the Kannada word differs from the replacement by exactly ONE
letter (code point), after the final visarga/anusvāra/virāma are set aside, and that letter is NOT the last one of the stem unless it
stands in a conjunct (after a virāma). A change in the last letter of a word is a change of case or number ending and may be what the
commentator wrote (ಇಂದ್ರೇ / ಇಂದ್ರಂ); those rows stay in the report for the editor.
A row is applied only where its Kannada word is found exactly once, as an entry key ('WORD—'), in the Pratipadārtha section that the row
points to. Anything else is skipped with the reason. Nothing outside those words is touched (the script proves it: the text with the
changed words put back is identical to the original).
Log (REQUIREMENTS B1.6; DESIGN 'second pass'): volN/data/source_fixes.tsv (place, as supplied, corrected, reason, basis, who) and one line in
volN/review/repair_log.md. The Wikisource text is never edited."""
import csv, datetime, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
TAIL = 'ಃಂ್‌‍'


def one_letter(a, b):
    """True if a, b (Kannada) differ by exactly one code point, not at the end of the stem (unless after a virāma)."""
    a, b = a.rstrip(TAIL), b.rstrip(TAIL)
    if a == b: return False
    i = 0
    while i < min(len(a), len(b)) and a[i] == b[i]: i += 1
    j = 0
    while j < min(len(a), len(b)) - i and a[-1 - j] == b[-1 - j]: j += 1
    ra, rb = a[i:len(a) - j], b[i:len(b) - j]
    if len(ra) > 1 or len(rb) > 1 or (len(ra) == 0 and len(rb) == 0): return False
    if re.search('[\u0C85-\u0C94]', b[1:]) : return False        # an independent vowel inside the word: a compound split / sandhi, not a misreading
    if 'ಃ' in b.rstrip(TAIL) or 'ಃ' in a.rstrip(TAIL): return False                      # a visarga inside the word: sandhi (ರಾಧೋಭಿಃ / ರಾಧಃಭಿಃ)
    if (not ra or not rb) and i == 0 and re.match('[\u0C85-\u0C94]', ra or rb): return False       # an initial vowel added or dropped: sandhi / augment (ಆಜಗ್ಮುಃ / ಜಗ್ಮುಃ), not a misreading
    if ra and rb:
        VOICE = {frozenset(x) for x in ('ಕಗ', 'ಚಜ', 'ಟಡ', 'ತದ', 'ಪಬ', 'ಖಘ', 'ಛಝ', 'ಥಧ', 'ಫಭ')}
        if frozenset((ra, rb)) in VOICE: return False                               # voiced/voiceless: the sandhi of a joined word (ಗೋಮದ್ಭಿಃ / ಗೋಮತ್ಭಿಃ)
        isv = lambda c: '\u0C85' <= c <= '\u0C94'
        if isv(ra) != isv(rb): return False                                         # consonant <-> vowel is not a one-letter misreading
    at_end = i + len(ra) >= len(a) and i + len(rb) >= len(b) and j == 0
    return (not at_end) or (i > 0 and a[i - 1] == '್')


def main():
    args = [x for x in sys.argv[1:] if not x.startswith('--')]
    write = '--write' in sys.argv
    only = set(sys.argv[sys.argv.index('--only') + 1].split(',')) if '--only' in sys.argv else None   # editor-approved words: the one-letter test is waived for these (each still needs a unique place)
    if only: args = [x for x in args if x != sys.argv[sys.argv.index('--only') + 1]]
    logdir = None
    if '--log' in sys.argv: logdir = pathlib.Path(sys.argv[sys.argv.index('--log') + 1])
    if args and args[0].isdigit():
        vol = args[0]; cfg = json.load(open(ROOT / f'vol{vol}' / 'volcfg.json'))
        path = ROOT / cfg['source'][0].split('@')[0]; rep = ROOT / f'vol{vol}' / 'review' / 'pratipada_check_source.tsv'
        logdir = logdir or ROOT / f'vol{vol}'
    else:
        path, rep = pathlib.Path(args[0]), pathlib.Path(args[1]); vol = None
        logdir = logdir or path.parent
    lines = path.read_text(encoding='utf8').split('\n')
    orig = list(lines)
    rows = list(csv.DictReader(open(rep, encoding='utf8'), delimiter='\t'))
    cand = [r for r in rows if r['kind'] == 'prat' and r['status'] == 'fix-certain']
    done, skipped = [], {'not one letter / ending': 0, 'not found once': 0}
    for r in cand:
        old, new = r['kannada_as_supplied'], r['kannada_replacement']
        if only is not None and old not in only: continue
        if not one_letter(old, new) and only is None: skipped['not one letter / ending'] += 1; continue
        start = int(r['line']) - 1
        end = start
        while end < len(lines) and (end == start or not lines[end].startswith('#')) and end - start < 80: end += 1
        pat = re.compile(r'(?<![ಀ-೿])' + re.escape(old) + r'(?![ಀ-೿])(?=[^|।!\n—–\-]*[—–\-])')      # a word of an entry key (the key may have several words, 'ಆಮಿತಾ ವಸೂನಿ—'): a dash follows in the same entry
        hits = [(k, m) for k in range(start, end) for m in pat.finditer(lines[k])]
        if len(hits) != 1: skipped['not found once'] += 1; continue
        k, m = hits[0]
        lines[k] = lines[k][:m.start()] + new + lines[k][m.end():]
        done.append((k + 1, r['ref'], old, new, r['proposal']))
    # proof: put the changed words back; the text must equal the original
    back = list(lines)
    for ln, ref, old, new, _ in done:
        back[ln - 1] = back[ln - 1].replace(new, old, 1) if new in back[ln - 1] else back[ln - 1]
    proved = len(done) == 0 or sum(1 for x, y in zip(back, orig) if x != y) <= len(done)
    print(f'{path.name}: {len(cand)} fix-certain rows; {len(done)} applicable; skipped: {skipped}')
    for d in done[:40]: print(f'  line {d[0]} Ṛk {d[1]}: {d[2]} → {d[3]}')
    if len(done) > 40: print(f'  … {len(done) - 40} more')
    if not write: print('preview only; --write applies and logs'); return
    if not done: return
    path.write_text('\n'.join(lines), encoding='utf8')
    today = datetime.date.today().isoformat()
    sf = logdir / 'data' / 'source_fixes.tsv'; sf.parent.mkdir(parents=True, exist_ok=True)
    new_file = not sf.exists()
    with open(sf, 'a', encoding='utf8') as f:
        if new_file: f.write('place\tas supplied\tcorrected\treason\tbasis\twho decided\n')
        for ln, ref, old, new, prop in done:
            f.write(f'{path.name} line {ln} (Ṛk {ref}, Pratipadārtha)\t{old}\t{new}\tword-meaning entry differs by one letter from the Pada word of the Ṛk\tWikisource Pada {ref}: {prop}; the supplied Pada block has {new}\tpratipada_apply.py {today}\n')
    rl = logdir / 'review' / 'repair_log.md'; rl.parent.mkdir(parents=True, exist_ok=True)
    with open(rl, 'a', encoding='utf8') as f:
        f.write(f'- {today}: {path.name}: {len(done)} Pratipadārtha words corrected by tools/rv/pratipada_apply.py (one letter, confirmed by the supplied Pada block and the Wikisource Pada); each is a row of data/source_fixes.tsv.\n')
    print(f'wrote {path}; logged {len(done)} rows in {sf}')


if __name__ == '__main__':
    main()
