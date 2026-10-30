"""Volume 6 pass: paths. Scan = the better scan in vol14/scans/ ("14 rigveda samhita volume 14 N.pdf", to be uploaded by the user),
read part by part; global PDF page = page in the user's full scan (parts in order). The page map printed = PDF - 18 is that of the
old scan Rig_Vol14.pdf: check it against the page headers of the better scan before relying on it.
Set V14OLD=1 to use the old scan Rig_Vol14.pdf instead."""
import os,re,glob,subprocess
VOL=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))   # the vol14/ folder
ROOT=os.path.dirname(VOL)
OLD=os.path.join(ROOT,'Rig_Vol14.pdf')
EN=os.path.join(ROOT,'Rigveda_Samhita_Vol14_English_Translation.md')
REVIEW=os.path.join(VOL,'review')
WORK=os.environ.get('V14WORK','/tmp/v14num/')
os.makedirs(WORK,exist_ok=True)
OFFSET=0   # TO BE SET from the page inventory (printed = PDF - OFFSET)
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
