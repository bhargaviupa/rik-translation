#!/usr/bin/env python3
"""Append one line per batch to the Vol 2 numeral log: pass_log.py FIRST LAST NOTE-FILE  (global PDF pages)."""
import sys,os,datetime
sys.path.insert(0,os.path.dirname(__file__))
from cfg import EN,ROOT
from pages import page_sections,text_of
a,b,nf=int(sys.argv[1]),int(sys.argv[2]),sys.argv[3]
seen=set(); n=0
for g in range(a,b+1):
    for (f,_,_,s,e) in page_sections(g):
        if (f,s) not in seen: seen.add((f,s)); n+=text_of(f)[s:e].count('[?]')
tot=sum(open(f,encoding='utf8').read().count('[?]') for f in (EN,))
L=os.environ.get('PASS_LOG_FILE',os.path.join(ROOT,'docs','PASS_LOG_numerals_vol2.md'))
if not os.path.exists(L): open(L,'w').write('# Vol 2 numeral pass (user review pages, better scan)\n\n')
note=open(nf,encoding='utf8').read().strip().replace('\n',' ')
open(L,'a',encoding='utf8').write(f"{datetime.datetime.now(datetime.timezone.utc):%Y-%m-%d %H:%M} PDF {a}-{b}: [?] on these pages {n}, file {tot}. {note}\n")
