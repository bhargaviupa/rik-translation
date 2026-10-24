"""List every [?] on given PDF pages with context:  python3 ctx.py 72 73"""
import re,sys
from cfg import EN as ENF, KN as KNF
def pages(f,kind):
    t=open(f,encoding='utf8').read()
    if kind=='en':
        out={}
        for s in re.split(r'\n(?=### Printed p\. )',t):
            m=re.match(r'### Printed p\. (\S+)\s+\(.*?PDF (\d+)',s)
            if m: out[int(m.group(2))]=out.get(int(m.group(2)),'')+s+'\n'
        return out
    out={}
    for s in re.split(r'\n(?=<!-- PDF )',t):
        m=re.match(r'<!-- PDF (\d+)',s)
        if m: out[int(m.group(1))]=s
    return out
EN=pages(ENF,'en'); KN=pages(KNF,'kn')
for n in map(int,sys.argv[1:]):
    for nm,D in (('EN',EN),('KN',KN)):
        s=D.get(n,''); ms=list(re.finditer(r'\[\?\]',s))
        print(f'##### {nm} PDF{n}: {len(ms)}')
        for i,m in enumerate(ms):
            print(f'{i}: ...{s[max(0,m.start()-70):m.start()].replace(chr(10)," ")}[?]{s[m.end():m.end()+30].replace(chr(10)," ")}')
