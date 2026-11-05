"""Shared library for the Vol 15+ pipeline (Claude Code sessions): per-volume config, page map, rendering, numeral-file rows.

Everything volume-specific lives in volN/volcfg.json (create it with `python3 tools/rv/batch.py new N`):
{
 "vol": 15, "mandala": 2, "branch": "claude/vol15",
 "source": ["vol15/html/rig_15_1.html@1-100", "vol15/html/rig_15_2.md@101-200"],   the supplied machine-read text (file@FIRST-LAST printed pages); the base text from Vol 15 on
 "scan": {"glob": "vol15/scans/15 *.pdf"},               optional now (only for a spot check)              parts in page order (number before .pdf orders them); or {"files": [...]}
 "printed": [[1, 20]],                                   printed page = PDF - k for PDF >= from_pdf (list of [from_pdf, k]; add a pair at every change)
 "skip_pdf": [],                                         PDF pages that duplicate the previous page (no content); never given to a translator
 "numerals": {"glob": "vol15/numerals/*.xlsx", "file_page": [[1, 0]]},   file page = PDF - delta for PDF >= from_pdf
 "out": {"kn": "vol15/Rigveda_Samhita_Vol15_Kannada_Text.md", "en": "vol15/Rigveda_Samhita_Vol15_English_Translation.md"},
 "work": "vol15/work", "window": 3
}
"""
import os,re,sys,glob,json,subprocess,tempfile
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
LIM=1950   # the viewer shows images up to ~2000 px wide without shrinking them
def cfg_path(vol): return os.path.join(ROOT,f'vol{vol}','volcfg.json')
class Cfg:
    def __init__(s,vol,path=None):
        s.vol=int(vol); s.path=path or cfg_path(vol)
        if not os.path.exists(s.path): sys.exit(f'no config {s.path}: run  python3 tools/rv/batch.py new {vol}')
        d=json.load(open(s.path,encoding='utf8')); s.d=d
        s.printed_map=sorted(d.get('printed',[[1,0]])); s.skip=set(d.get('skip_pdf',[])); s.window=d.get('window',3)
        s.branch=d.get('branch'); s.mandala=d.get('mandala',1); s.source=d.get('source',[])
        s.kn=os.path.join(ROOT,d['out']['kn']); s.en=os.path.join(ROOT,d['out']['en']); s.work=os.path.join(ROOT,d.get('work',f'vol{vol}/work'))
        s._parts=None
    def parts(s):
        if s._parts is None:
            sc=s.d['scan']; fs=[os.path.join(ROOT,f) for f in sc['files']] if 'files' in sc else sorted(glob.glob(os.path.join(ROOT,sc['glob'])),key=lambda p:int(re.findall(r'(\d+)\.pdf$',p)[0]))
            out=[];g=1
            for p in fs:
                n=int(re.search(r'Pages:\s+(\d+)',subprocess.run(['pdfinfo',p],capture_output=True,text=True).stdout).group(1)); out.append((p,g,g+n-1)); g+=n
            s._parts=out
        return s._parts
    def part_of(s,g):
        for p,a,b in s.parts():
            if a<=g<=b: return p,g-a+1
        raise KeyError(f'PDF {g} is beyond the scan parts (last {s.parts()[-1][2] if s.parts() else 0})')
    def printed(s,g):
        k=0
        for f,kk in s.printed_map:
            if g>=f: k=kk
        return g-k
    def file_page(s,g):
        k=0
        for f,kk in s.d.get('numerals',{}).get('file_page',[[1,0]]):
            if g>=f: k=kk
        return g-k
    def source_pages(s,heads=None):
        """{printed page: text} from the supplied HTML/markdown files (None if no source is configured)"""
        if not s.source: return None
        import html_pages
        return html_pages.load_many([os.path.join(ROOT,x) if '@' not in x else os.path.join(ROOT,x.split('@')[0])+'@'+x.split('@')[1] for x in s.source],heads)
    def printed_to_pdf(s,p):
        for f,k in sorted(s.printed_map,reverse=True):
            g=p+k
            if g>=f and s.printed(g)==p: return g
        return None
    def numeral_files(s):
        n=s.d.get('numerals',{}); return sorted(glob.glob(os.path.join(ROOT,n['glob']))) if 'glob' in n else []
def render(cfg,g,dpi):
    from PIL import Image
    p,n=cfg.part_of(g); d=tempfile.mkdtemp()
    subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r',str(dpi),'-gray','-png',p,d+'/p'],check=True)
    f=os.listdir(d)[0]; im=Image.open(d+'/'+f).convert('L'); im.load(); subprocess.run(['rm','-rf',d]); return im
def _ink(im):
    import numpy as np; return np.array(im)<140
def trim(im,pad=12):
    import numpy as np; ys,xs=np.where(_ink(im))
    if len(xs)==0: return im,(0,0)
    x0,x1=int(np.percentile(xs,.1)),int(np.percentile(xs,99.9)); y0,y1=int(np.percentile(ys,.1)),int(np.percentile(ys,99.9))
    b=(max(0,x0-pad),max(0,y0-pad),min(im.width,x1+pad),min(im.height,y1+pad)); return im.crop(b),(b[0],b[1])
def best_dpi(cfg,g,want):
    w=trim(render(cfg,g,100))[0].width; return max(100,min(want,int(LIM*100/w)))
def cuts(im,n):
    import numpy as np
    blank=_ink(im).sum(axis=1)<=1; runs=[];s=None
    for y,b in enumerate(blank):
        if b and s is None: s=y
        if not b and s is not None:
            if y-s>=10: runs.append((s,y))
            s=None
    cs=[]
    for k in range(1,n):
        t=im.height*k//n
        if not runs: cs.append(t); continue
        r=min(runs,key=lambda r:abs((r[0]+r[1])/2-t)); cs.append((r[0]+r[1])//2)
    return [0]+sorted(set(cs))+[im.height]
def strips(cfg,g,out,dpi=400,n=None):
    """render PDF page g, trimmed, cut into full-width strips at gaps between lines; returns [(path,size)]"""
    d=best_dpi(cfg,g,dpi); im,_=trim(render(cfg,g,d)); n=n or max(1,-(-im.height//LIM)); ys=cuts(im,n) if n>1 else [0,im.height]
    res=[]
    for k in range(len(ys)-1):
        s=im.crop((0,ys[k],im.width,ys[k+1])); f=f'{out}_{k}.png'; s.save(f); res.append((f,s.size,d))
    return res
def zoom(cfg,g,out,k,box,zdpi=600,dpi=400):
    """re-render box (x0,y0,x1,y1) of strip k, in the pixel coordinates of the strip image as displayed, at zdpi"""
    d=best_dpi(cfg,g,dpi); full=render(cfg,g,d); im,off=trim(full); n=max(1,-(-im.height//LIM)); ys=cuts(im,n) if n>1 else [0,im.height]
    X0,Y0,X1,Y1=box; sy=ys[k]; q=zdpi/d
    bx=(X0+off[0],Y0+sy+off[1],X1+off[0],Y1+sy+off[1]); big=render(cfg,g,zdpi); c=big.crop(tuple(int(v*q) for v in bx)); c.save(out+'_z.png'); return out+'_z.png',c.size
