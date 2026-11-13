"""Automatic numeral check (Vol 2 method, text-compared): for each PDF page, the references (N-N, N-N-N, Ni./Pā./U. numbers) in the file's page section(s)
versus those in the page's Kannada OCR text (review/ocr). Prints, per page, refs in the file but not in OCR ('file-only': probably misread/old) and OCR refs
absent from the file ('ocr-only': omitted or misread by OCR).  python3 refcheck.py FIRST LAST [--json OUT]"""
import sys,os,re,json
sys.path.insert(0,os.path.dirname(__file__))
from cfg import VOL
from pages import sections,text_of,printed
DD={chr(0x0966+i):str(i) for i in range(10)}; KD={chr(0x0CE6+i):str(i) for i in range(10)}
def A(s): return ''.join(DD.get(c,KD.get(c,c)) for c in s)
REF=re.compile(r'(?<![0-9])(\d{1,3})\s?[-–]\s?(\d{1,3})(?:\s?[-–]\s?(\d{1,3}))?(?:\s?[-–]\s?(\d{1,3}))?(?![0-9])')
def refs(s):
    s=A(s); out=[]
    for m in REF.finditer(s): out.append('-'.join(g for g in m.groups() if g))
    return out
def ocr_refs(g):
    f=os.path.join(VOL,'review','ocr',f'{g}.json')
    if not os.path.exists(f): return None
    t=' '.join(x[3] for x in json.load(open(f,encoding='utf8')))
    t=re.sub(r'(?<=[೦-೯])\s*[.–—_]\s*(?=[೦-೯])','-',t)
    return refs(t)
def ok(k):
    p=[int(x) for x in k.split('-')]
    return not (len(p)==2 and p[0]>40 and p[1]>40) and max(p)<10000
if __name__=='__main__':
    lo,hi=int(sys.argv[1]),int(sys.argv[2]); res=[]  # printed pages
    from collections import Counter
    for f,x,y,st,en in sections():
        if y<lo or x>hi or x<=0: continue
        txt=open(f,encoding='utf8').read()[st:en]
        fo=Counter(r for r in refs(txt) if ok(r)); oo=Counter()
        miss=0
        for p in range(x,y+1):
            o=ocr_refs(p+14)
            if o is None: miss+=1; continue
            oo.update(r for r in o if ok(r))
        if miss: continue
        fonly=sorted(k for k in fo if k not in oo); oonly=sorted(k for k in oo if k not in fo)
        res.append(dict(pages=[x,y],start=st,file_only=fonly,ocr_only=oonly,nfile=sum(fo.values()),nocr=sum(oo.values())))
    json.dump(res,open('/tmp/v3num/refcheck.json','w'),ensure_ascii=False)
    print(len(res),'sections; file-only refs',sum(len(v['file_only']) for v in res),'; ocr-only refs',sum(len(v['ocr_only']) for v in res),'; file refs total',sum(v['nfile'] for v in res))
