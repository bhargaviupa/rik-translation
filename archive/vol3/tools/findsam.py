"""Find large-type verse lines on a page: findsam.py PDF -> groups of consecutive big lines as page fractions"""
import sys,os,subprocess,tempfile
sys.path.insert(0,os.path.dirname(__file__))
from cfg import part_of,WORK
from PIL import Image,ImageOps
def groups(g):
    path,n=part_of(g); d=tempfile.mkdtemp(dir=WORK)
    subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','150','-gray',path,d+'/p'],check=True)
    im=Image.open(d+'/'+os.listdir(d)[0]); subprocess.run(['rm','-rf',d])
    bw=ImageOps.invert(im).point(lambda v:255 if v>110 else 0); px=bw.load(); w,h=bw.size
    rows=[sum(px[x,y]>0 for x in range(0,w,2)) for y in range(h)]
    thr=w*0.004; lines=[]; y=0
    while y<h:
        if rows[y]>thr:
            s=y
            while y<h and rows[y]>thr: y+=1
            if y-s>=6: lines.append((s,y))
        y+=1
    hs=sorted(e-s for s,e in lines); med=hs[len(hs)//2]
    big=[(s,e) for s,e in lines if e-s>=1.45*med]
    out=[]
    for s,e in big:
        if out and s-out[-1][1]<2.2*med: out[-1][1]=e
        else: out.append([s,e])
    return [(s/h,e/h) for s,e in out],med,h
if __name__=='__main__':
    gs,med,h=groups(int(sys.argv[1])); print(' '.join(f'{a:.3f}-{b:.3f}' for a,b in gs),'med',med)
