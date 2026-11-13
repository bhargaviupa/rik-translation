"""List every [?] (and 'as read') in a line range of the Vol 6 file with context.  python3 qctx.py FIRSTLINE LASTLINE [CHARS] [REGEX]"""
import sys,os,re
sys.path.insert(0,os.path.dirname(__file__))
from cfg import EN
a,b=int(sys.argv[1]),int(sys.argv[2]); w=int(sys.argv[3]) if len(sys.argv)>3 else 100
rx=re.compile(sys.argv[4] if len(sys.argv)>4 else r'\[\?\]')
for i,l in enumerate(open(EN,encoding='utf8').read().split('\n'),1):
    if a<=i<=b:
        for m in rx.finditer(l): print(f'{i}:',repr(l[max(0,m.start()-w):m.end()+40]))
