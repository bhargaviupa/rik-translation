#!/usr/bin/env python3
"""A Saṃhitā of two (or more) lines whose later line stands at the top of the next window WITHOUT its label: the model gives that line its own
Ṛk heading and Saṃhitā sub-heading (verify then counts one Saṃhitā heading too many; Vol 23 w0524, w0740, Vol 30 w0560).

  python3 tools/rv/fix_split_samhita.py N --windows [--write]   the not yet committed windows of volume N: in en.md, '#### Ṛk R / **Saṃhitā-pāṭha** / [[b1]]'
                                                                 at the start is turned into '[[b1]]' when kn.md starts with a '> ' block before any label
  python3 tools/rv/fix_split_samhita.py N --file [--write]      the finished English file: the repeated Ṛk heading and Saṃhitā heading after a page heading are removed
Preview unless --write; every change is a line in volN/review/repair_log.md. Nothing else is touched."""
import re, sys, glob, os, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
n = sys.argv[1]; write = '--write' in sys.argv
log = []
if '--windows' in sys.argv:
    for w in sorted(glob.glob(f'{ROOT}/vol{n}/work/w0*')):
        kp, ep = f'{w}/kn.md', f'{w}/en.md'
        if not (os.path.exists(kp) and os.path.exists(ep)): continue
        kn = open(kp, encoding='utf8').read()
        body = [l for l in kn.split('\n') if l.strip() and not l.startswith('<!--') and not l.startswith('*[')]
        if not body or not body[0].startswith('>'): continue          # the window starts with a label: nothing to repair
        en = open(ep, encoding='utf8').read()
        m = re.match(r'(### Printed p\. \d+\n)\n?(?:#### Ṛk \d+(?: \(continued\))?\n)?\n?(?:\*\*Saṃhitā-pāṭha\*\*\n)\n?(\[\[b1\]\]\n)', en)
        if m and (kn.count('*ಸಂಹಿತಾಪಾಠಃ*') or True):
            new = m.group(1) + m.group(2) + en[m.end():]
            log.append(os.path.basename(w))
            if write: open(ep, 'w', encoding='utf8').write(new)
else:
    p = f'{ROOT}/vol{n}/Rigveda_Samhita_Vol{n}_English_Translation.md'
    t = open(p, encoding='utf8').read()
    pat = re.compile(r'(#### Ṛk (\d+)(?: \(continued\))?\n\n##### ॥ संहितापाठः ॥ \(Saṃhitā-pāṭha\)\n\n(?:> [^\n]*\n)+)\n(### Printed p\. \d+\n)\n?(?:#### Ṛk \2(?: \(continued\))?\n\n)+##### ॥ संहितापाठः ॥ \(Saṃhitā-pāṭha\)\n\n')
    def rep(m): log.append(f'Ṛk {m.group(2)} at {m.group(3).strip()}'); return m.group(1) + '\n' + m.group(3) + '\n'
    t2 = pat.sub(rep, t)
    if write and t2 != t: open(p, 'w', encoding='utf8').write(t2)
print(len(log), 'place(s):', ', '.join(log[:40]))
if write and log:
    open(f'{ROOT}/vol{n}/review/repair_log.md', 'a', encoding='utf8').write(f"- {datetime.date.today()}: fix_split_samhita.py ({'windows' if '--windows' in sys.argv else 'English file'}): the second line of a Saṃhitā at the top of a window had its own Ṛk heading and Saṃhitā sub-heading; removed at: {', '.join(log)} (no text changed).\n")
