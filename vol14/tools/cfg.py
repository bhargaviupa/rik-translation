"""Volume 14: paths. Scan = vol14/scans/ ("14 rigveda samhita volume 14 N.pdf", parts in page order); global PDF page = page in the full scan (parts in order). OFFSET and the page map are to be set from the header strips (see vol14_runbook.md). Set V14OLD=1 to use the old 300-dpi scan Rig_Vol14.pdf (if present).""" 
import os,re,glob,subprocess
VOL=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))   # the vol14/ folder
ROOT=os.path.dirname(VOL)
OLD=os.path.join(ROOT,'Rig_Vol14.pdf')
EN=os.path.join(ROOT,'Rigveda_Samhita_Vol14_English_Translation.md')
REVIEW=os.path.join(VOL,'review')
WORK=os.environ.get('V14WORK','/tmp/v14num/')
os.makedirs(WORK,exist_ok=True)
OFFSET=0   # TO BE SET from the page map (printed = PDF - OFFSET)
def _parts():
    fs=sorted(glob.glob(os.path.join(VOL,'scans','*.pdf')),key=lambda p:int(re.findall(r'(\d+)\.pdf$',p)[0]))
    out=[];g=1
    for p in fs:
        n=int(re.search(r'Pages:\s+(\d+)',subprocess.run(['pdfinfo',p],capture_output=True,text=True).stdout).group(1))
        out.append((p,g,g+n-1)); g+=n
    return out
PARTS=[] if os.environ.get('V14OLD') else _parts()
def part_of(g):
    """global PDF page -> (pdf path, page within that pdf)"""
    if not PARTS: return OLD,g
    for p,a,b in PARTS:
        if a<=g<=b: return p,g-a+1
    raise KeyError(f'PDF {g} is beyond the uploaded scan parts (last {PARTS[-1][2]}): upload the next part or stop')
SCAN=OLD   # kept for old callers

_ORI=None
def flipped(g):
    """True if PDF page g is stored upside down (from review/orient_v14.json, written by orient_v14.py, then spot-checked)."""
    global _ORI
    if _ORI is None:
        import json
        f=os.path.join(REVIEW,'orient_v14.json')
        _ORI={int(k):v['rot']==180 for k,v in json.load(open(f)).items()} if os.path.exists(f) else {}
        # manual overrides after visual checks: review/orient_fix_v14.json {page: 0|180}
        f2=os.path.join(REVIEW,'orient_fix_v14.json')
        if os.path.exists(f2): _ORI.update({int(k):v==180 for k,v in json.load(open(f2)).items()})
    return _ORI.get(g,False)
