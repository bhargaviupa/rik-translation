"""Auto-confirm numerals: a '[?]' directly after a number (e.g. 'Ni. 2-23 [?]', '७-१८ [?]') is removed when the OCR text of the Ṛk's pages
contains the same number in Kannada digits (OCR is independent of the old reading). Others are listed for a crop.
python3 qconfirm.py [--apply] [FIRSTLINE LASTLINE]"""
import sys,os,re,json
sys.path.insert(0,os.path.dirname(__file__))
from cfg import EN,VOL
from qlocate import L,pages,ocr
ap='--apply' in sys.argv; a=[x for x in sys.argv[1:] if not x.startswith('--')]
lo=int(a[0]) if a else 1; hi=int(a[1]) if len(a)>1 else len(L)
KD={str(i):chr(0x0CE6+i) for i in range(10)}; DD={chr(0x0966+i):str(i) for i in range(10)}
def to_ascii(s): return ''.join(DD.get(c,c) for c in s)
def to_kn(s): return ''.join(KD.get(c,c) for c in s)
NUM=re.compile(r'((?:[0-9०-९]+)(?:\s?[-–.]\s?[0-9०-९]+){1,3})\s*\[\?\]')
def ocrnums(pg):
    S=''
    for g in pg:
        for top,left,h,t in ocr(g): S+=' '+t
    return re.sub(r'[\s.–—_‑−\-]+','-',S)
head='';pg=None;conf=[];rest=[];cache={}
new=list(L)
for n,l in enumerate(L,1):
    if l.startswith('### '): head=l; pg=pages(l)
    if n<lo or n>hi or '[?]' not in l: continue
    for m in NUM.finditer(l):
        num=to_ascii(m.group(1)); parts=re.findall(r'\d+',num); key='-'.join(to_kn(p) for p in parts)
        if pg and head not in cache: cache[head]=ocrnums(pg)
        hit=bool(pg) and len(re.sub(r'\D','',num))>=3 and bool(re.search(r'(?<![\u0CE6-\u0CEF])'+re.escape(key)+r'(?![\u0CE6-\u0CEF])',cache.get(head,'')))
        (conf if hit else rest).append((n,m.group(0),key))
print('number+[?] :',len(conf)+len(rest),'| confirmed by OCR:',len(conf),'| need a crop:',len(rest),'| all [?] in range:',sum(L[i].count('[?]') for i in range(lo-1,min(hi,len(L)))))
if ap:
    for n,s,key in conf:
        l=new[n-1]; new[n-1]=l.replace(s,re.sub(r'\s*\[\?\]','',s)+'',1) if s in l else l
    open(EN,'w',encoding='utf8').write('\n'.join(new)); print('applied',len(conf))
json.dump(dict(conf=conf,rest=rest),open('/tmp/v3num/qconf.json','w'),ensure_ascii=False)
