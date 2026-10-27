"""For PDF pages FIRST..LAST: the user's readings in print order (all rows; '*' = edited) and the numeral groups of the
page section in file order, including placeholders like '4-?? [?]' and '1?th [?]', with short context.
python3 qmap.py REVIEW.json EDITS.txt FIRST LAST"""
import sys,os,re,json
sys.path.insert(0,os.path.dirname(__file__))
from pages import page_sections,text_of,label
R=json.load(open(sys.argv[1])); E={}
for l in open(sys.argv[2],encoding='utf8').read().splitlines():
    if ':' in l: k,v=l.split(':',1); E[k.strip()]=v.strip()
a,b=int(sys.argv[3]),int(sys.argv[4])
NUM=re.compile(r'(?<![\w*])((?:\d|\?)[\d?]*(?:\s*[-–.,]\s*(?:\d|\?)[\d?]*)*(?:st|nd|rd|th)?)(\s*\[\?\])?')
for g in range(a,b+1):
    rows=[r for r in R if r['pdf']==g]
    if not any(r['id'] in E for r in rows): continue
    print(f'\n######## PDF {g} · printed {label(g)}')
    print('  '+'  '.join(f"{r['id'].split('_')[1]}{'*' if r['id'] in E else ''}={E.get(r['id'],r['prop']) or '∅'}" for r in rows))
    for (f,_,_,s,e) in page_sections(g):
        t=text_of(f)[s:e]
        for ln in t.split('\n'):
            if ln.startswith('> *') or ln.startswith('#'): continue
            for m in NUM.finditer(ln):
                v=m.group(1)
                if not re.search(r'\d',v) and '?' not in v: continue
                if v in ('?',) : continue
                print(f"   {v+(m.group(2) or ''):16} …{ln[max(0,m.start()-45):m.start()]}")
