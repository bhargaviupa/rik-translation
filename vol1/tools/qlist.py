"""List the [?] spots of Vol 1 (both English files) on the pages of global PDF FIRST..LAST, numeral ones separated.
python3 qlist.py FIRST LAST [--words]"""
import sys,os,re
sys.path.insert(0,os.path.dirname(__file__))
from pages import page_sections,text_of,label
a,b=int(sys.argv[1]),int(sys.argv[2]); words='--words' in sys.argv
seen=set(); nw=nn=0
for g in range(a,b+1):
    for (f,_,_,s,e) in page_sections(g):
        if (f,s) in seen: continue
        seen.add((f,s)); t=text_of(f)[s:e]; line0=text_of(f)[:s].count('\n')+1
        for m in re.finditer(r'\[\?\]|⟦\?⟧',t):
            pre=t[max(0,m.start()-12):m.start()]
            num=bool(re.search(r'[\d೦-೯०-९][-.]?\s*$',pre))
            if num: nn+=1
            else: nw+=1
            if words and not num:
                ln=line0+t[:m.start()].count('\n')
                print(f"PDF {g} {label(g)} {os.path.basename(f)[19:23]}:{ln}: …{t[max(0,m.start()-90):m.end()+40]}…".replace('\n',' '))
print('word/other [?]:',nw,' numeral [?]:',nn,file=sys.stderr)
