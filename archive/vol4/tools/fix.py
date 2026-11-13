"""fix.py BATCH.json LEDGER_ROWS.json -- exact replacements [[old,new,count],...] on the main file (refuses mismatches); appends ledger rows [[page,rk,category,marked,old,new,note],...]"""
import sys,json,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from cfg import EN
t=open(EN,encoding='utf8').read(); n0=len(t)
R=json.load(open(sys.argv[1]))
bad=0
for a,b,c in R:
    k=t.count(a)
    if k!=c: print('MISMATCH',k,'!=',c,repr(a[:80])); bad+=1; continue
    t=t.replace(a,b)
if bad: sys.exit('nothing written')
assert len(t)>n0-3000
open(EN,'w',encoding='utf8').write(t)
L='/tmp/v4num/ledger.tsv'; n=sum(1 for _ in open(L,encoding='utf8'))-1
with open(L,'a',encoding='utf8') as f:
    for r in json.load(open(sys.argv[2])):
        n+=1; f.write(str(n)+'\t'+'\t'.join(r)+'\n')
print('applied',len(R),'edits; ledger rows now',n)
