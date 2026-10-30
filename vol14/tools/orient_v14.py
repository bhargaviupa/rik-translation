"""Orientation + page-number inventory for the Vol 14 scan (locating aid only; no readings).
For each global PDF page: OCR (kan, psm 4) of the page at 100 dpi in both orientations (0 and 180 degrees); keep the one with more recognised Kannada letters.
Writes vol14/review/orient_v14.json: {page: {"rot": 0|180, "n0": count, "n180": count}}.
python3 vol14/tools/orient_v14.py [FIRST LAST] [JOBS]"""
import sys,os,re,json,subprocess,tempfile
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0,os.path.dirname(__file__))
import cfg
from PIL import Image
a=int(sys.argv[1]) if len(sys.argv)>2 else 1; b=int(sys.argv[2]) if len(sys.argv)>2 else cfg.PARTS[-1][2]
J=int(sys.argv[3]) if len(sys.argv)>3 else 4
K=re.compile('[ಀ-೿]')
def one(g):
    p,n=cfg.part_of(g); d=tempfile.mkdtemp()
    subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','100','-gray',p,d+'/p'],check=True)
    f=os.path.join(d,os.listdir(d)[0]); im=Image.open(f).convert('L'); res={}
    for rot in (0,180):
        im2=im if rot==0 else im.rotate(180); im2.save(d+'/r.png')
        t=subprocess.run(['tesseract',d+'/r.png','-','-l','kan','--psm','4'],capture_output=True,text=True).stdout
        res[rot]=len(K.findall(t))
    subprocess.run(['rm','-rf',d])
    return g,{'rot':0 if res[0]>=res[180] else 180,'n0':res[0],'n180':res[180]}
out={}
with ThreadPoolExecutor(J) as ex:
    for g,r in ex.map(one,range(a,b+1)): out[g]=r
os.makedirs(cfg.REVIEW,exist_ok=True)
json.dump(out,open(os.path.join(cfg.REVIEW,'orient_v14.json'),'w'),indent=0)
print(sum(1 for r in out.values() if r['rot']==180),'of',len(out),'pages look upside down')
