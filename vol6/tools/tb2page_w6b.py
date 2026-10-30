"""w6b helper: convert y0/y1/x0/x1 of a doubts JSON from text-block fractions to whole-page fractions (what doubts_v6.py crops).
python3 tb2page_w6b.py IN.json OUT.json   (entries with "pagefrac": true are left as they are)"""
import sys,os,json
sys.path.insert(0,os.path.dirname(__file__))
from cfg import OFFSET
from view import textbox,render
D=json.load(open(sys.argv[1],encoding='utf8'))
for d in D:
    if d.pop('pagefrac',False): continue
    im=render(d['page']+OFFSET,40); W,H=im.size; x0,t0,x1,t1=textbox(im); w=x1-x0; h=t1-t0
    d['y0']=round(max(0,(t0+d['y0']*h)/H-0.005),4); d['y1']=round(min(1,(t0+d['y1']*h)/H+0.005),4)
    d['x0']=round(max(0,(x0+d.get('x0',0)*w)/W-0.02),4); d['x1']=round(min(1,(x0+d.get('x1',1)*w)/W+0.02),4)
json.dump(D,open(sys.argv[2],'w',encoding='utf8'),ensure_ascii=False,indent=1)
