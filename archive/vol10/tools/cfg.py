"""Volume 10: paths. Scan = vol10/scans/ ("10 Rigveda Samhitha Volume 10 N.pdf", parts in page order; if none is uploaded the old scan scans/Rig_Vol10.pdf is used). Global PDF page = page in the full scan (parts in order). OFFSET: printed = PDF - OFFSET (CLAUDE.md says 21, TO BE RE-CHECKED from the header strips of the scan actually used)."""
import os,re,glob,subprocess
VOL=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))   # the vol10/ folder
ROOT=os.path.dirname(VOL)
OLD=os.path.join(VOL,'scans','Rig_Vol10.pdf')
EN=os.path.join(VOL,'Rigveda_Samhita_Vol10_English_Translation.md')
REVIEW=os.path.join(VOL,'review')
WORK=os.environ.get('V10WORK','/tmp/v10num/')
os.makedirs(WORK,exist_ok=True)
OFFSET=21   # printed = PDF - 21 (Sūkta 122 on printed p. 2 = PDF 23); re-check, and re-check again for a better scan
def _parts():
    fs=sorted(glob.glob(os.path.join(os.environ.get('V10SCANS',os.path.join(VOL,'scans')),'*[0-9].pdf')),key=lambda p:int(re.findall(r'(\d+)\.pdf$',p)[0]))   # numbered parts only
    fs=[p for p in fs if not os.path.basename(p).startswith('Rig_Vol')]   # old scan lives in scans/ too
    out=[];g=1
    for p in fs:
        n=int(re.search(r'Pages:\s+(\d+)',subprocess.run(['pdfinfo',p],capture_output=True,text=True).stdout).group(1))
        out.append((p,g,g+n-1)); g+=n
    return out
PARTS=[] if os.environ.get('V10OLD') else _parts()
def part_of(g):
    """global PDF page -> (pdf path, page within that pdf)"""
    if not PARTS: return OLD,g
    for p,a,b in PARTS:
        if a<=g<=b: return p,g-a+1
    raise KeyError(f'PDF {g} is beyond the uploaded scan parts (last {PARTS[-1][2]}): upload the next part or stop')
SCAN=OLD
def flipped(g):
    """Pages are not checked for orientation; kept so view.py/numsheets.py work."""
    return False
