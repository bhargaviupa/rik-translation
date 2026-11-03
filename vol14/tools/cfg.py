"""Volume 14: paths. Scan = vol14/scans/ ("14 rigveda samhita volume 14 N.pdf", parts in page order); global PDF page = page in the full scan (parts in order). OFFSET and the page map are to be set from the header strips (see vol14_runbook.md).""" 
import os,re,glob,subprocess
VOL=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))   # the vol14/ folder
ROOT=os.path.dirname(VOL)
EN=os.path.join(ROOT,'Rigveda_Samhita_Vol14_English_Translation.md')
REVIEW=os.path.join(VOL,'review')
WORK=os.environ.get('V14WORK','/tmp/v14num/')
os.makedirs(WORK,exist_ok=True)
OFFSET=18   # printed = PDF - 18 (title page PDF 19 = printed 1; contents PDF 11-18 = roman; checked on all of part 1, PDF 20-121 = printed 2-103)
def _parts():
    fs=sorted(glob.glob(os.path.join(VOL,'scans','14 [Rr]igveda*.pdf')),key=lambda p:int(re.findall(r'(\d+)\.pdf$',p)[0]))
    out=[];g=1
    for p in fs:
        n=int(re.search(r'Pages:\s+(\d+)',subprocess.run(['pdfinfo',p],capture_output=True,text=True).stdout).group(1))
        out.append((p,g,g+n-1)); g+=n
    return out
PARTS=_parts()
def part_of(g):
    """global PDF page -> (pdf path, page within that pdf)"""
    for p,a,b in PARTS:
        if a<=g<=b: return p,g-a+1
    raise KeyError(f'PDF {g} is beyond the uploaded scan parts (last {PARTS[-1][2]}): upload the next part or stop')
