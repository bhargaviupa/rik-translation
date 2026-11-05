"""Worksheet for repairing [?] in a volume .md from a machine-read page HTML (the base text).
python3 tools/rv/repair_worksheet.py --md FILE.md --html FILE.html --first-line A --last-line B [--out sheet.txt]
For each line with [?]: its printed page (nearest page marker above), the md context, and the references of the matching type found in the HTML
on that page and its neighbours, with the HTML words before them (transliterated) and a context score. Report only; nothing is changed."""
import re,sys,os,argparse
sys.path.insert(0,os.path.dirname(__file__)); sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..','..','publish','tools','translit'))
import html_pages
from kannada_to_deva import kn2deva
from indic_transliteration import sanscript
from rapidfuzz import fuzz
KD=str.maketrans('೦೧೨೩೪೫೬೭೮೯','0123456789')
TYPES=[('Pā.',r'ಪಾ\.?\s*ಸೂ\.?|ಪಾ\.'),('Uṇ.',r'ಉ\.?\s*ಸೂ\.?|ಉಣಾ\.?'),('Ni.',r'ನಿ\.'),('Kā.',r'ಕಾ\.'),('Ṛ.',r'ಋ\.?\s*ಸಂ\.?'),('Dhā.',r'ಧಾ\.'),('Bṛ. De.',r'ಬೃ\.?\s*ದೇ\.?')]
REF=r'[೦-೯]+(?:\s*[-.]\s*[೦-೯]+)*'
def iast(kn): return sanscript.transliterate(kn2deva(kn),sanscript.DEVANAGARI,sanscript.IAST).lower()
_FM=str.maketrans({'ā':'a','ī':'i','ū':'u','ṛ':'r','ṝ':'r','ṅ':'n','ñ':'n','ṇ':'n','ṭ':'t','ḍ':'d','ś':'s','ṣ':'s','ṃ':'m','ḥ':'h','ḷ':'l'})
def fold(s): return re.sub(r'[^a-z]','',s.lower().translate(_FM))
def html_refs(text):
    out=[]
    for tname,pat in TYPES:
        for m in re.finditer(r'(?:'+pat+r')\s*\(?\s*('+REF+')',text):
            before=text[max(0,m.start()-160):m.start()]; out.append((tname,re.sub(r'\s*[-.]\s*','-',m.group(1).translate(KD)),fold(iast(before))))
    return out
def page_marks(lines):
    cur=None; res=[]
    for l in lines:
        for m in re.finditer(r'\((?:p|pp)\. (\d+)|### Page (\d+) \(PDF|printed p\. (\d+)',l):
            cur=int([g for g in m.groups() if g][0])
        res.append(cur)
    return res
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--md'); ap.add_argument('--html'); ap.add_argument('--first-line',type=int); ap.add_argument('--last-line',type=int); ap.add_argument('--out'); a=ap.parse_args()
    L=open(a.md,encoding='utf8').read().split('\n'); pm=page_marks(L); P=html_pages.pages(a.html); out=[]
    cache={}
    def refs(p):
        if p not in cache: cache[p]=html_refs(P.get(p,''))
        return cache[p]
    for i in range(a.first_line-1,min(a.last_line,len(L))):
        l=L[i]
        if '[?]' not in l: continue
        p=pm[i]; out.append(f'### line {i+1}  (page marker {p})\n{l[:400]}')
        for m in re.finditer(r'\[\?\]',l):
            pre=l[max(0,m.start()-110):m.start()]; typ=None
            for tname,_ in TYPES:
                k=pre.rfind(tname); 
                if k>=0 and (typ is None or k>typ[1]): typ=(tname,k)
            if typ and p:
                cands=[]
                for q in (p-1,p,p+1):
                    for tn,val,bef in refs(q):
                        if tn==typ[0]: cands.append((fuzz.partial_ratio(fold(pre[-80:]),bef[-120:]) if bef else 0,q,val))
                cands.sort(reverse=True)
                out.append(f'   [?] after "...{pre[-50:]}"  type {typ[0]}  candidates (score, page, value): {cands[:4]}')
            else: out.append(f'   [?] after "...{pre[-60:]}"  (no reference type; page {p})')
        out.append('')
    s='\n'.join(out); open(a.out,'w',encoding='utf8').write(s) if a.out else print(s)
main()
