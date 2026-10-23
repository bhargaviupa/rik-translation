#!/usr/bin/env python3
"""Append one measurement line per batch: pass_log.py FIRST LAST [note]  (PDF pages of Vol 11)."""
import sys,subprocess,datetime,re
sys.path.insert(0,'/tmp/v11')
a,b=int(sys.argv[1]),int(sys.argv[2]); note=' '.join(sys.argv[3:])
def cnt(path,kind):
    t=open(path,encoding='utf8').read(); n=0
    for p in range(a,b+1):
        m=re.search(r'PDF %d\b'%p,t)
        if not m: continue
        nx=re.search(r'PDF %d\b'%(p+1),t[m.end():]); seg=t[m.end():m.end()+nx.start()] if nx else t[m.end():]
        n+=seg.count('[?]')
    return n
e=cnt('Rigveda_Samhita_Vol11_English_Translation.md','en'); k=cnt('Rigveda_Samhita_Vol11_Kannada_Text.md','kn')
open('docs/PASS_LOG.md','a',encoding='utf8').write(f"{datetime.datetime.now(datetime.timezone.utc):%Y-%m-%d %H:%M} PDF {a}-{b}: remaining [?] EN {e}, KN {k}. {note}\n")
