"""Link every open [?] of the main file to a line of the OCR text of its page(s).
python3 qlocate.py [FIRSTLINE LASTLINE]  -> /tmp/v3num/qloc.json
For each [?]: nearest preceding sūtra/word (italic IAST or Devanagari), converted to Kannada, fuzzy-matched against OCR lines of the Ṛk's pages;
prints nothing big. Output rows: {line, pdf, cand_text, top, left, h, score, ctx}."""
import sys,os,re,json,difflib
sys.path.insert(0,os.path.dirname(__file__))
from cfg import EN,VOL
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate as T
L=open(EN,encoding='utf8').read().split('\n')
OCR={}
def ocr(g):
    if g not in OCR:
        f=os.path.join(VOL,'review','ocr',f'{g}.json'); OCR[g]=json.load(open(f,encoding='utf8')) if os.path.exists(f) else []
    return OCR[g]
HEAD=re.compile(r'^### Pages? (\d+)(?:\s*[–-]\s*(\d+))?')
def pages(h):
    m=HEAD.match(h)
    if not m: return None
    a=int(m.group(1)); b=int(m.group(2)) if m.group(2) else a
    return list(range(a+14,b+15))
def kn(s):
    s=re.sub(r'[*_`|"\'()\[\]]','',s)
    try: return T(s,sanscript.IAST,sanscript.KANNADA) if re.search('[a-zA-Zāīūṛṣśṭḍṇṅñ]',s) else T(s,sanscript.DEVANAGARI,sanscript.KANNADA)
    except Exception: return ''
def norm(k): return re.sub(r'[^ಀ-೿]','',k)
def key_before(l,i):
    seg=l[max(0,i-260):i]
    c=re.findall(r'\*([^*]{4,60})\*|"([^"]{4,60})"|([ऀ-ॿ][ऀ-ॿ ॥।]{3,50})',seg)
    c=[a or b or d for a,b,d in c if (a or b or d)]
    return c[-1] if c else ''
if __name__=='__main__':
    lo=int(sys.argv[1]) if len(sys.argv)>1 else 1; hi=int(sys.argv[2]) if len(sys.argv)>2 else len(L)
    head='';pg=None;out=[]
    for n,l in enumerate(L,1):
        if l.startswith('### '): head=l; pg=pages(l)
        if n<lo or n>hi: continue
        for m in re.finditer(r'\[\?\]',l):
            ctx=l[max(0,m.start()-80):m.end()+30]
            k=key_before(l,m.start()); kk=norm(kn(k))[:14]
            best=None
            for g in (pg or []):
                for top,left,h,t in ocr(g):
                    nt=norm(t)
                    if kk and len(kk)>=4:
                        sc=difflib.SequenceMatcher(None,kk,nt).find_longest_match(0,len(kk),0,len(nt)).size/len(kk)
                        if best is None or sc>best[0]: best=(sc,g,top,left,h,t)
            out.append(dict(line=n,pdf=best[1] if best else None,score=round(best[0],2) if best else 0,top=best[2] if best else None,left=best[3] if best else None,h=best[4] if best else None,cand=best[5] if best else '',key=k,ctx=ctx,head=head[4:50]))
    json.dump(out,open('/tmp/v3num/qloc.json','w'),ensure_ascii=False)
    import collections
    print(len(out),'[?]; matched>=0.7:',sum(1 for o in out if o['score']>=0.7),'; no pages:',sum(1 for o in out if o['pdf'] is None))
