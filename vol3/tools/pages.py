"""Vol 3: global PDF page <-> printed page, and the file text of each printed page."""
import re,os,sys
sys.path.insert(0,os.path.dirname(__file__))
from cfg import EN
ROMAN=['i','ii','iii','iv','v','vi','vii','viii','ix','x','xi','xii','xiii','xiv','xv','xvi','xvii','xviii','xix','xx']
FRONT={}; PRINTED_AS={}
# Better scan (7 parts, 660 PDF pages), checked from the page headers: PDF 15 = printed 1 (invocation page),
# printed = PDF - 14 for PDF 15-500 (PDF 500 = p. 486); printed p. 487 is NOT in the scan; PDF 501 repeats p. 488
# (= PDF 502); printed = PDF - 14 for PDF 502-659 (PDF 659 = p. 645); printed p. 646 is NOT in the scan;
# PDF 660 = p. 647, the last page. The two missing pages are in scans/Rig_Vol3.pdf (its PDF 502 and 661; printed = PDF - 15 there).
DUP={501:502}
MISSING={'487':('scans/Rig_Vol3.pdf',502),'646':('scans/Rig_Vol3.pdf',661)}
def printed(g):
    if g in FRONT: return FRONT[g]
    if g in DUP: return printed(DUP[g])
    if 15<=g<=500: return str(g-14)
    if 502<=g<=659: return str(g-14)
    if g==660: return '647'
    return None
def label(g):
    p=printed(g)
    return 'unnumbered' if p is None else f"p. {PRINTED_AS[g]} (= {p}, as printed)" if g in PRINTED_AS else f"p. {p}"
HEAD=re.compile(r'^### (?:Pages? ([0-9ivxlc]+)(?:\s*[–-]\s*([0-9ivxlc]+))?\b|Sūkta \d+ — Rik .*\(printed pp?\. (\d+)(?:[–-](\d+))?\)).*$',re.M)
SUPERSEDED=('### Pages 452–454 — Sūkta 29, Rik 6','## ॥ ಮೂವತ್ತೊಂದನೆಯ ಸೂಕ್ತವು ॥')   # unverified text, replaced by the REDO block
def _key(s): return ROMAN.index(s)-100 if s in ROMAN else int(s) if s.isdigit() else None
def sections():
    """list of (file, first, last, start, end) for every '### Page N' section, in file order"""
    out=[]
    for f in (EN,):
        t=open(f,encoding='utf8').read(); ms=list(HEAD.finditer(t))
        sa=t.index(SUPERSEDED[0]); sb=t.index(SUPERSEDED[1])
        for i,m in enumerate(ms):
            if sa<=m.start()<sb: continue
            g1,g2=(m.group(1),m.group(2)) if m.group(1) else (m.group(3),m.group(4))
            a=_key(g1); b=_key(g2) if g2 else a
            if a is None: continue
            end=min([x.start() for x in ms[i+1:i+2]]+[sa] if m.start()<sa else [x.start() for x in ms[i+1:i+2]]+[len(t)])
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
