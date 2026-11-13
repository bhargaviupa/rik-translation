"""Align the file's references (document order) with the OCR references (page/line order) of each section; 1:1 'replace' pairs = a file ref whose
OCR neighbour sits in the same place of the sequence.  Output /tmp/v3num/refalign.json: pairs {line? , pages, file, ocr, pdf, top, x} for crop checking.
python3 refalign.py FIRST LAST (printed pages)"""
import sys,os,re,json,difflib
sys.path.insert(0,os.path.dirname(__file__))
from cfg import VOL
from pages import sections
from refcheck import refs,ok,A
def ocr_occ(g):
    f=os.path.join(VOL,'review','ocr',f'{g}.json')
    if not os.path.exists(f): return None
    out=[]
    for top,left,h,t in json.load(open(f,encoding='utf8')):
        t2=re.sub(r'(?<=[೦-೯])\s*[.–—_]\s*(?=[೦-೯])','-',t)
        for m in re.finditer(r'(?<![೦-೯0-9])[೦-೯]{1,3}\s?[-–]\s?[೦-೯]{1,3}(?:\s?[-–]\s?[೦-೯]{1,3}){0,2}(?![೦-೯0-9])',t2):
            r=refs(m.group(0))
            if r and ok(r[0]): out.append((r[0],g,top,left+int(2000*m.start()/max(1,len(t2))),t[:0]))
    return out
if __name__=='__main__':
    lo,hi=int(sys.argv[1]),int(sys.argv[2]); pairs=[];stats=[0,0,0]
    for f,x,y,st,en in sections():
        if y<lo or x>hi or x<=0: continue
        txt=open(f,encoding='utf8').read()[st:en]
        fr=[r for r in refs(txt) if ok(r)]
        occ=[]
        miss=False
        for p in range(x,y+1):
            o=ocr_occ(p+14)
            if o is None: miss=True;break
            occ+=o
        if miss: continue
        a=fr; b=[o[0] for o in occ]
        sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
        for tag,i1,i2,j1,j2 in sm.get_opcodes():
            if tag=='replace' and (i2-i1)==(j2-j1):
                for k in range(i2-i1):
                    o=occ[j1+k]; pairs.append(dict(pages=[x,y],file=a[i1+k],ocr=o[0],pdf=o[1],top=o[2],x=o[3]))
            stats[0 if tag=='equal' else 1 if tag=='replace' else 2]+=i2-i1
    json.dump(pairs,open('/tmp/v3num/refalign.json','w'),ensure_ascii=False)
    print('file refs equal:',stats[0],'| replaced (any):',stats[1],'| file-only (delete/other):',stats[2],'| 1:1 aligned pairs:',len(pairs))
