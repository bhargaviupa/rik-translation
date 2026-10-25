"""Vol 1: global PDF page <-> printed page, and the file text of each printed page (both English files)."""
import re,os,sys
sys.path.insert(0,os.path.dirname(__file__))
from cfg import EN,GAPS
ROMAN=['i','ii','iii','iv','v','vi','vii','viii','ix','x','xi','xii','xiii','xiv','xv','xvi','xvii','xviii','xix','xx']
# PDF 1-5 unnumbered (title, dedication, photos); 14 prints "xi" for ix; 17 (xiii) prints no number
FRONT={6:'i',7:'ii',8:'iii',9:'iv',10:'v',11:'vi',12:'vii',13:'viii',14:'ix',15:'x',16:'xi',17:'xiii',18:'xiv',19:'xv',
       20:'xvi',21:'xvii',22:'xviii',23:'xix',24:'xx'}
PRINTED_AS={14:'xi'}
DUP={g:g+8 for g in range(41,49)}   # PDF 41-48 repeat printed pp. 25-32 (= PDF 49-56); printed pp. 17-24 are not in this scan
def printed(g):
    if g in FRONT: return FRONT[g]
    if g in DUP: return str(DUP[g]-24)
    if 25<=g<=383: return str(g-24)
    if g in (384,385): return str(g-26)          # duplicate scan of printed pp. 358-359 (= PDF 382-383)
    if 386<=g<=397: return str(g-26)
    if 398<=g<=400: return str(g-24)             # printed pp. 372-373 are not in the scan
    return None
def label(g):
    p=printed(g)
    return 'unnumbered' if p is None else f"p. {PRINTED_AS[g]} (= {p}, as printed)" if g in PRINTED_AS else f"p. {p}"
HEAD=re.compile(r'^### Pages? ([0-9ivxlc]+)(?:\s*[–-]\s*([0-9ivxlc]+))?\b.*$',re.M)
def _key(s): return ROMAN.index(s)-100 if s in ROMAN else int(s) if s.isdigit() else None
def sections():
    """list of (file, first, last, start, end) for every '### Page N' section, in file order"""
    out=[]
    for f in (EN,GAPS):
        t=open(f,encoding='utf8').read(); ms=list(HEAD.finditer(t))
        for i,m in enumerate(ms):
            a=_key(m.group(1)); b=_key(m.group(2)) if m.group(2) else a
            if a is None: continue
            end=ms[i+1].start() if i+1<len(ms) else len(t)
            out.append((f,a,b if b is not None else a,m.start(),end))
    return out
_S=None; _T={}
def text_of(f):
    if f not in _T: _T[f]=open(f,encoding='utf8').read()
    return _T[f]
def page_sections(g):
    """sections holding printed page of global PDF g; if none, the preceding section (pages merged into it).
    The front-matter section headed 'xi (bibliography, continued)' is printed ix (PDF 14)."""
    global _S
    if _S is None: _S=sections()
    p=printed(g)
    if p is None: return []
    k=_key(p)
    hits=[s for s in _S if s[1]<=k<=s[2]]
    if g==14: hits=[s for s in _S if 'xi (bibliography' in text_of(s[0])[s[3]:s[3]+60]]
    if g==16: hits=[s for s in _S if 'xi (closing' in text_of(s[0])[s[3]:s[3]+60]]
    if hits: return hits
    prev=[s for s in _S if s[2]<k and k-s[2]<=2 and s[0]==EN]
    return prev[-1:] if prev else []
