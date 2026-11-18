#!/usr/bin/env python3
"""State of the bhāṣya-English run, read from the repository (no state file).

    python3 tools/rv/bhashya_run.py status          # per volume: sūktas done / total
    python3 tools/rv/bhashya_run.py next [K]        # the next K sūktas without a verified English file (default 1)
    python3 tools/rv/bhashya_run.py verify VOL M.S  # the check for one sūkta; exit 0 only on VERIFIED

A sūkta is done when volN/bhashya_en/M<m>_S<sss>.md exists and passes publish/bhashya_check.py.
Volumes are taken in the order of ORDER; a volume in an older layout is reported and skipped.
"""
import pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / 'publish'))
import bhashya_book as bb

ORDER = list(range(1, 21))


def volume(vol):
    """(None, reason) or ([(mand, sukta, done)], '')."""
    import json
    cfgf = ROOT / f'vol{vol}' / 'volcfg.json'
    src = (ROOT / json.loads(cfgf.read_text(encoding='utf-8'))['out']['en'] if cfgf.exists()
           else ROOT / f'vol{vol}' / f'Rigveda_Samhita_Vol{vol}_English_Translation.md')
    if not src.exists(): return None, 'no English file'
    lines = src.read_text(encoding='utf-8').splitlines()
    sl = bb.sukta_list(lines)
    if not sl or not any(l.startswith('##### ') and 'Saṃhitā-pāṭha' in l for l in lines): return None, 'older layout'
    return [(m, n, bb.en_path(vol, m, n).exists()) for m, n, _ in sl], ''


def verify(vol, ms):
    r = subprocess.run([sys.executable, str(ROOT / 'publish' / 'bhashya_check.py'), str(vol), ms], capture_output=True, text=True)
    last = (r.stdout.strip().splitlines() or [r.stderr.strip()])[-1]
    return r.returncode == 0 and last.startswith('VERIFIED'), r.stdout


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'status'
    if cmd == 'verify':
        ok, out = verify(sys.argv[2], sys.argv[3]); print(out.strip()); return 0 if ok else 1
    todo, tot, done = [], 0, 0
    for v in ORDER:
        if not (ROOT / f'vol{v}').exists(): continue
        sl, why = volume(v)
        if sl is None:
            if cmd == 'status': print(f'Vol {v}: skipped ({why})')
            continue
        d = sum(1 for _, _, x in sl if x)
        tot += len(sl); done += d
        if cmd == 'status': print(f'Vol {v}: {d} of {len(sl)} sūktas have an English file')
        todo += [(v, f'{m or 0}.{n}') for m, n, x in sl if not x]
    if cmd == 'status':
        print(f'Total: {done} of {tot}; to do: {len(todo)}'); return 0
    k = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    for v, ms in todo[:k]: print(v, ms)
    if not todo: print('ALL DONE')
    return 0


if __name__ == '__main__':
    sys.exit(main())
