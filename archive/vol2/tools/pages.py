"""Vol 2: global PDF page <-> printed page, and the file text of each printed page (both English files)."""
import re,os,sys
sys.path.insert(0,os.path.dirname(__file__))
from cfg import EN
ROMAN=['i','ii','iii','iv','v','vi','vii','viii','ix','x','xi','xii','xiii','xiv','xv','xvi','xvii','xviii','xix','xx']
FRONT={}; PRINTED_AS={}
# printed = PDF - 14; printed pp. 224-225 are not in the scan (PDF 237 = 223, PDF 238 = 226);
# PDF 290-291 repeat printed pp. 276-277 (= PDF 288-289). PDF 822 = printed 808, the last page.
DUP={290:288,291:289}
def printed(g):
    if g in FRONT: return FRONT[g]
    if g in DUP: return printed(DUP[g])
    if 15<=g<=237: return str(g-14)
    if 238<=g<=289: return str(g-12)
    if 292<=g<=822: return str(g-14)
    return None
def label(g):
    p=printed(g)
    return 'unnumbered' if p is None else f"p. {PRINTED_AS[g]} (= {p}, as printed)" if g in PRINTED_AS else f"p. {p}"
HEAD=re.compile(r'^### Pages? ([0-9ivxlc]+)(?:\s*[–-]\s*([0-9ivxlc]+))?\b.*$',re.M)
def _key(s): return ROMAN.index(s)-100 if s in ROMAN else int(s) if s.isdigit() else None
def sections():
    """list of (file, first, last, start, end) for every '### Page N' section, in file order"""
    out=[]
    for f in (EN,):
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
    if hits: return hits
    prev=[s for s in _S if s[2]<k and k-s[2]<=2 and s[0]==EN]
    return prev[-1:] if prev else []
