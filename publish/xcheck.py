#!/usr/bin/env python3
"""Cross-check helper for Volume 2.  python3 xcheck.py N  -> renders scan-B page for printed page N, prints md lines with [?] on that page."""
import re, sys, subprocess, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
MD = ROOT / 'Rigveda_Samhita_Vol2_English_Translation.md'
def section(n):
    L = MD.read_text(encoding='utf-8').split('\n')
    start = end = None
    for i, l in enumerate(L):
        m = re.match(r'^#{2,3} \[?Page (\d+)', l)
        if m:
            if int(m.group(1)) == n and start is None: start = i
            elif start is not None and end is None: end = i; break
    return L, start, end
if __name__ == '__main__':
    n = int(sys.argv[1]); dpi = sys.argv[2] if len(sys.argv) > 2 else '130'
    subprocess.run(['pdftoppm','-jpeg','-r',dpi,'-f',str(n+14),'-l',str(n+14),'/home/user/scanB/Rig_Vol2_B.pdf',f'/tmp/cmp/p{n}'])
    L, s, e = section(n)
    if s is None: print('no page marker'); sys.exit()
    print(f'page {n}: md lines {s+1}-{e}')
    for i in range(s, e):
        if i == s: print(i+1, L[i][:120])
        elif '[?]' in L[i]:
            for m in re.finditer(r'\[\?\]', L[i]):
                print(f'  L{i+1}@{m.start()}:', L[i][max(0,m.start()-70):m.end()+45].replace('\n',' '))
