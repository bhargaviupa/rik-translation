"""Compare readings of the gold items: A file text (old visual method), B Tesseract, C shape classifier, D eye; and user gold if given.
python3 compare.py  (reads docs/numeral_gold/*.csv and WORK/all_*.csv) -> docs/numeral_gold/comparison.csv + summary"""
import csv,re,os,sys,difflib,collections
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..','verify11'))
from cfg import WORK,EN
G='docs/numeral_gold/'
items=list(csv.DictReader(open(G+'gold_items.csv')))
B={r['id']:r['tess'] for r in csv.DictReader(open(G+'method_tess.csv'))}
D={r['id']:r['eye'] for r in csv.DictReader(open(G+'method_eye.csv'))}
allit={(r['pdf'],r['box600']):r['id'] for r in csv.DictReader(open(WORK+'all_items.csv'))}
shape={r['id']:r for r in csv.DictReader(open(WORK+'all_shape.csv'))}
U={}
if os.path.exists(G+'answers.csv'):
    U={r['id']:r['your_reading'].strip() for r in csv.DictReader(open(G+'answers.csv')) if r['your_reading'].strip()}
t=open(EN,encoding='utf8').read(); pages={}
for s in re.split(r'\n(?=### Printed p\. )',t):
    m=re.match(r'### Printed p\. (\S+)\s+\(.*?PDF (\d+)',s)
    if m: pages[m.group(2)]=pages.get(m.group(2),'')+s
DEV=str.maketrans('०१२३४५६७८९','0123456789')
NUM=re.compile(r'(?<![\w.])(\d{1,4}(?:\s*-\s*[\d?]{1,4}|\s*-\s*\[\?\]){0,3})(\s*\[\?\])?')
def fileread(pdf,ref):
    best=('',0,False)
    for m in NUM.finditer(pages.get(pdf,'').translate(DEV)):
        v=re.sub(r'\s','',m.group(1)); r=difflib.SequenceMatcher(None,v,ref).ratio()
        if r>best[1]: best=(v,r,bool(m.group(2)) or '?' in v)
    return best
rows=[]
for it in items:
    i=it['id']; c=shape.get(allit.get((it['pdf'],it['box600'])),{}).get('shape','')
    b=B[i]; d=D[i]
    cons=b if b==c==d else (b if b==c else (c if c==d else (b if b==d else '')))
    a,ar,af=fileread(it['pdf'],cons or b)
    if ar<0.6: a='(not found)'
    rows.append(dict(id=i,pdf=it['pdf'],A_file=a+(' [?]' if af and ar>=0.6 else ''),B_tess=b,C_shape=c,D_eye=d,
        consensus=cons,n_agree=sum(x==cons for x in (b,c,d)) if cons else 0,user=U.get(i,'')))
w=csv.DictWriter(open(G+'comparison.csv','w',newline=''),fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
ref_name='user' if U else 'consensus(>=2 of B,C,D)'
print('reference:',ref_name)
def score(key):
    ok=n=0; pair=collections.Counter(); pairn=collections.Counter()
    for r in rows:
        ref=r['user'] if U else (r['consensus'] if r['n_agree']>=2 else '')
        if not ref or '?' in ref: continue
        got=r[key].replace(' [?]','')
        n+=1; ok+=got==ref
        for P in ('35','67','29','89'):
            if any(ch in ref for ch in P):
                pairn[P]+=1; pair[P]+=got==ref
    return ok,n,{P:f'{pair[P]}/{pairn[P]}' for P in ('35','67','29','89')}
for k in ('A_file','B_tess','C_shape','D_eye'):
    ok,n,p=score(k); print(f'{k:8} {ok}/{n} = {ok/max(n,1):.0%}  per pair (items containing 3/5, 6/7, 2/9, 8/9):',p)
print('B=C=D unanimous:',sum(r['n_agree']==3 for r in rows),' two of three:',sum(r['n_agree']==2 for r in rows),' no majority:',sum(r['n_agree']<2 for r in rows))
