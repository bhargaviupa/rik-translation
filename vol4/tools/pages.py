"""Vol 4: global PDF page <-> printed page, and the file text of each printed page."""
import re,os,sys
sys.path.insert(0,os.path.dirname(__file__))
from cfg import EN
ROMAN=['i','ii','iii','iv','v','vi','vii','viii','ix','x','xi','xii','xiii','xiv','xv','xvi','xvii','xviii','xix','xx']
FRONT={}; PRINTED_AS={}
# Vol 4 BETTER SCAN (7 parts, 701 PDF pages), page map checked by pnum.py OCR of the header numbers (Oct 28, noisy; majority vote per 50 pages):
# printed = PDF - 14 for about PDF 1-101, printed = PDF - 15 from about PDF 105 on: ONE EXTRA PAGE (duplicate or inserted) lies between
# PDF 101 and 105 -- find it by eye (header montage) and record it in DUP below. Printed p. 608 (the last page of the old scan) should then be
# PDF 623; PDF 624-701 (78 pages) are UNEXPLAINED (OCR finds no header numbers there): look at them first (contact sheet), they may be an index,
# blank/duplicate pages or part of the next volume. Front matter: PDF 1-14 (old scan: Kannada title page 1, dedication 3, board 5, portrait 6,
# preface 7-10 -- not translated by design). Printed page numbers are Latin digits.
DUP={}      # fill in: {duplicate PDF page: the page it repeats}
MISSING={}  # printed pages absent from the better scan (read them from ../Rig_Vol4.pdf, printed = PDF - 14 there)
def printed(g):
    if g in FRONT: return FRONT[g]
    if g in DUP: return printed(DUP[g])
    if 15<=g<=101: return str(g-14)   # PROVISIONAL
    if 105<=g<=623: return str(g-15)  # PROVISIONAL
    return None
def label(g):
    p=printed(g)
    return 'unnumbered' if p is None else f"p. {PRINTED_AS[g]} (= {p}, as printed)" if g in PRINTED_AS else f"p. {p}"
HEAD=re.compile(r'^### (?:Pages? ([0-9ivxlc]+)(?:\s*[–-]\s*([0-9ivxlc]+))?\b|Sūkta \d+ — Rik .*\(printed pp?\. (\d+)(?:[–-](\d+))?\)).*$',re.M)
# (Oct 27: the superseded first version of pp. 452-517 was removed and the REDO put in its place; the REDO-style
# heading pattern above is kept only in case such headings reappear.)
def _key(s): return ROMAN.index(s)-100 if s in ROMAN else int(s) if s.isdigit() else None
def sections():
    """list of (file, first, last, start, end) for every '### Page N' section, in file order"""
    out=[]
    for f in (EN,):
        t=open(f,encoding='utf8').read(); ms=list(HEAD.finditer(t))
        for i,m in enumerate(ms):
            g1,g2=(m.group(1),m.group(2)) if m.group(1) else (m.group(3),m.group(4))
            a=_key(g1); b=_key(g2) if g2 else a
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
