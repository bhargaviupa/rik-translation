"""For PDF pages FIRST..LAST: the user's readings in print order (all crops of the page; edited ones marked *)
and the page section text with its numeral groups bracketed.  python3 pagework.py REVIEW.json EDITS.txt FIRST LAST"""
import sys,os,re,json
sys.path.insert(0,os.path.dirname(__file__))
from pages import page_sections,text_of,label
R=json.load(open(sys.argv[1])); E={}
for l in open(sys.argv[2],encoding='utf8').read().splitlines():
    if ':' in l: k,v=l.split(':',1); E[k.strip()]=v.strip()
a,b=int(sys.argv[3]),int(sys.argv[4])
for g in range(a,b+1):
    rows=[r for r in R if r['pdf']==g]
    if not any(r['id'] in E for r in rows): continue
    print(f'\n######## PDF {g} · printed {label(g)}')
    print('  '.join(f"{r['id'].split('_')[1]}{'*' if r['id'] in E else ''}={E.get(r['id'],r['prop']) or '∅'}" for r in rows))
    for (f,_,_,s,e) in page_sections(g):
        t=text_of(f)[s:e]
        t=re.sub(r'\*[^*\n]{0,200}\*','',t) if os.environ.get('NOIAST') else t
        lines=[l for l in t.split('\n') if re.search(r'\d|[०-९]',l)]
        for l in lines: print('   |',l[:600])
