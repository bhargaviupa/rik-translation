#!/usr/bin/env python3
"""flags.py N [M] : list [?] flags (compact) on printed pages N..M of Vol 2 and render scan-B pages at 130 dpi"""
import re, sys, subprocess, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
s = (ROOT/'Rigveda_Samhita_Vol2_English_Translation.md').read_text(encoding='utf-8')
ms = list(re.finditer(r'(?m)^#{2,3} \[?Pages? (\d+)(?:\s*[–-]\s*(\d+))?', s))
def run(n):
    for k, m in enumerate(ms):
        lo = int(m.group(1)); hi = int(m.group(2) or lo)
        if lo <= n <= hi:
            seg = s[m.start():(ms[k+1].start() if k+1 < len(ms) else len(s))]
            fl = []
            for line in seg.split('\n'):
                if line.lstrip().startswith('*(Source note'): continue
                for mm in re.finditer(r'\[\?\]', line):
                    if re.search(r'[A-Za-z]', line[max(0,mm.start()-30):mm.start()]) and not re.search(r'[ऀ-ॿ]', line[max(0,mm.start()-30):mm.start()]) and not re.search(r'\d', line[max(0,mm.start()-12):mm.start()]): 
                        pass
                    fl.append(line[max(0, mm.start()-60):mm.end()+25].replace('\n', ' '))
            print(f'== p{n} (section {lo}-{hi}) flags: {len(fl)}')
            seen=set()
            for f in fl:
                if f not in seen: print('  ', f); seen.add(f)
            subprocess.run(['pdftoppm','-jpeg','-r','140','-f',str(n+14),'-l',str(n+14),'/home/user/scanB/Rig_Vol2_B.pdf',f'/tmp/cmp/q{n}'])
            return
    print('no section', n)
if __name__ == '__main__':
    a = int(sys.argv[1]); b = int(sys.argv[2]) if len(sys.argv) > 2 else a
    for n in range(a, b+1): run(n)
