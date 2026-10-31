"""Volume 6 pass: paths. Scan = the better scan in vol13/scans/ ("13 rigveda samhita volume 13 N.pdf", to be uploaded by the user),
read part by part; global PDF page = page in the user's full scan (parts in order). The page map printed = PDF - 18 is that of the
old scan Rig_Vol13.pdf: check it against the page headers of the better scan before relying on it.
Set V13OLD=1 to use the old scan Rig_Vol13.pdf instead."""
import os,re,glob,subprocess
VOL=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))   # the vol13/ folder
ROOT=os.path.dirname(VOL)
OLD=os.path.join(ROOT,'Rig_Vol13.pdf')
EN=os.path.join(ROOT,'Rigveda_Samhita_Vol13_English_Translation.md')
REVIEW=os.path.join(VOL,'review')
WORK=os.environ.get('V13WORK','/tmp/v13num/')
os.makedirs(WORK,exist_ok=True)
OFFSET=20   # printed = PDF - 20 for PDF 21..677 (PDF 21 = printed 1); front matter PDF 7-19 = roman i-xiii (PDF-6); verified by review/page_map_v13.json
def _parts():
    fs=sorted(glob.glob(os.path.join(VOL,'scans','*[0-9].pdf')),key=lambda p:int(re.findall(r'(\d+)\.pdf$',p)[0]))   # numbered parts only: '4a' is a duplicate rescan of pp. 361-460
    out=[];g=1
    for p in fs:
        n=int(re.search(r'Pages:\s+(\d+)',subprocess.run(['pdfinfo',p],capture_output=True,text=True).stdout).group(1))
        out.append((p,g,g+n-1)); g+=n
    return out
PARTS=[] if os.environ.get('V13OLD') else _parts()
def part_of(g):
    """global PDF page -> (pdf path, page within that pdf)"""
    if not PARTS: return OLD,g
    for p,a,b in PARTS:
        if a<=g<=b: return p,g-a+1
    raise KeyError(f'PDF {g} is beyond the uploaded scan parts (last {PARTS[-1][2]}): upload the next part or stop')
SCAN=OLD   # kept for old callers

_ORI=None
def flipped(g):
    """True if PDF page g is stored upside down (from review/orient_v13.json, written by orient_v13.py, then spot-checked)."""
    global _ORI
    if _ORI is None:
        import json
        f=os.path.join(REVIEW,'orient_v13.json')
        _ORI={int(k):v['rot']==180 for k,v in json.load(open(f)).items()} if os.path.exists(f) else {}
        # manual overrides after visual checks: review/orient_fix_v13.json {page: 0|180}
        f2=os.path.join(REVIEW,'orient_fix_v13.json')
        if os.path.exists(f2): _ORI.update({int(k):v==180 for k,v in json.load(open(f2)).items()})
    return _ORI.get(g,False)
