#!/usr/bin/env python3
"""Add Maṇḍala / Sūkta / Ṛk headings to a volume's Kannada text file, taken from the structure of the English file.

  python3 tools/rv/kn_headings.py N [--write]

The English file has `## Maṇḍala M`, `## Sūkta N (Maṇḍala M)` and `#### Ṛk N`; the Kannada file has only page marks and section labels.
Alignment (checked, never guessed):
  * Ṛk N heading  -> placed before the i-th `*ಸಂಹಿತಾಪಾಠಃ*` label (the i-th Ṛk heading of the English file that is not a '(continued)' heading);
  * Sūkta heading -> placed before the printed line `ಮಂಡಲ—M ॥ ಅನುವಾಕ—A ॥ ಸೂಕ್ತ—N ॥` (the Pīṭhike of the sūkta, if any, is printed above it);
  * `## ಮಂಡಲ M` -> before the first sūkta of a new Maṇḍala.
The counts are compared with the English file first (a mismatch writes nothing). A sūkta number in the Kannada line that disagrees with the English order is a WARN (printed/OCR slip in the supplied text): the heading follows the English order and the warning goes to the repair log.
Without --write: report only. With --write: file rewritten (nothing else changes), a line is added to volN/review/repair_log.md."""
import re, sys, pathlib, datetime
root = pathlib.Path(__file__).resolve().parents[2]
vol = int(sys.argv[1]); write = '--write' in sys.argv
en = (root / f'vol{vol}' / f'Rigveda_Samhita_Vol{vol}_English_Translation.md').read_text(encoding='utf8').split('\n')
kf = root / f'vol{vol}' / f'Rigveda_Samhita_Vol{vol}_Kannada_Text.md'
kn = kf.read_text(encoding='utf8').split('\n')
KD = str.maketrans('0123456789', '೦೧೨೩೪೫೬೭೮೯'); ED = {c: str(i) for i, c in enumerate('೦೧೨೩೪೫೬೭೮೯')}
def kdig(n): return str(n).translate(KD)
def edig(s): return int(''.join(ED[c] for c in s))
# English structure
ev = []
for l in en:
    m = re.match(r'## Maṇḍala (\d+)\s*$', l)
    if m: ev.append(('mandala', int(m.group(1)))); continue
    m = re.match(r'## Sūkta (\d+) \(Maṇḍala (\d+)\)', l)
    if m: ev.append(('sukta', int(m.group(1)), int(m.group(2)))); continue
    m = re.match(r'#### Ṛk (\d+)\s*$', l)
    if m: ev.append(('rk', int(m.group(1))))
suktas = [e for e in ev if e[0] == 'sukta']; riks = [e for e in ev if e[0] == 'rk']
# Kannada anchors
sl = []
for i, l in enumerate(kn):
    m = re.match(rf'^(?:[॥।]\s*)?ಮಂಡಲ\s*[-—–]\s*([೦-೯]+).*ಸೂಕ್ತ\s*[-—–]\s*([೦-೯]+)', l.strip())
    if m: sl.append((i, edig(m.group(1)), edig(m.group(2))))
labs = [i for i, l in enumerate(kn) if l.strip() == '*ಸಂಹಿತಾಪಾಠಃ*']
prob = []; warn = []
if len(sl) != len(suktas): prob.append(f'sūkta lines: Kannada {len(sl)} vs English {len(suktas)}')
else:
    for (i, m, s), e in zip(sl, suktas):
        if (s, m) != (e[1], e[2]): warn.append(f'Kannada line {i+1} reads Maṇḍala {m} Sūkta {s} (as supplied); the English file has Sūkta {e[1]} (Maṇḍala {e[2]}) at this position: heading follows the English order')
if len(labs) != len(riks): prob.append(f'Saṃhitā labels: Kannada {len(labs)} vs English Ṛk headings {len(riks)}')
print(f'English: {len(suktas)} sūktas, {len(riks)} Ṛk headings; Kannada: {len(sl)} sūkta lines, {len(labs)} Saṃhitā labels')
for p in prob: print('PROBLEM', p)
for w in warn: print('WARN', w)
if prob: sys.exit(1)
ins = {}
prev_m = None
for (i, _m, _s), e in zip(sl, suktas):
    s, m = e[1], e[2]                      # the English file is the authority for the numbers
    pre = []
    if m != prev_m and prev_m is not None: pre += [f'## ಮಂಡಲ {kdig(m)}', '']
    pre += [f'## ಸೂಕ್ತ {kdig(s)} (ಮಂಡಲ {kdig(m)})', '']
    ins.setdefault(i, []).extend(pre); prev_m = m
for i, e in zip(labs, riks):
    ins.setdefault(i, []).extend([f'#### ಋಕ್ {kdig(e[1])}', ''])
out = []
for i, l in enumerate(kn):
    if i in ins and out and out[-1].strip():          # pandoc/markdown: a heading needs a blank line before it
        out.append('')
    out += ins.get(i, []); out.append(l)
print(f'{len(sl)} sūkta and {len(labs)} Ṛk headings to insert')
if write:
    kf.write_text('\n'.join(out), encoding='utf8')
    with (root / f'vol{vol}' / 'review' / 'repair_log.md').open('a', encoding='utf8') as g:
        g.write(f'- {datetime.date.today()}: tools/rv/kn_headings.py: {len(sl)} Sūkta and {len(labs)} Ṛk headings (and Maṇḍala headings) added to the Kannada file from the structure of the English file (no other text changed)'+''.join(f' [WARN: {w}]' for w in warn)+'. Sūkta headings stand before the printed "ಮಂಡಲ—M ॥ ಅನುವಾಕ ॥ ಸೂಕ್ತ—N" line; a Pīṭhike printed above that line belongs to the sūkta that follows.\n')
