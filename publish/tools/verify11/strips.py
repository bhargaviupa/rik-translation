"""Render PDF page N of the scan at 260 dpi, trim margins, cut into S horizontal strips -> WORK/pN_1.png ...
python3 strips.py N [S=3]   (view each strip; zoom with tiles.py where a glyph is unclear)"""
import sys,subprocess,json,glob
from PIL import Image
from cfg import WORK,SCAN
n=int(sys.argv[1]); S=int(sys.argv[2]) if len(sys.argv)>2 else 3
subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','260','-gray',SCAN,f'{WORK}s{n}'],check=True)
f=glob.glob(f'{WORK}s{n}-*.pgm')[0]
a=Image.open(f).convert('L'); W,H=a.size
bw=a.point(lambda p:0 if p>170 else 255); x0,y0,x1,y1=bw.getbbox()
x0=max(0,x0-10);y0=max(0,y0-10);x1=min(W,x1+10);y1=min(H,y1+10)
h=(y1-y0)/S; meta=[]
for i in range(S):
    ya=int(y0+i*h-(30 if i else 0)); yb=int(min(y1,y0+(i+1)*h+30))
    a.crop((x0,ya,x1,yb)).save(f'{WORK}p{n}_{i+1}.png'); meta.append((x0,ya))
json.dump(meta,open(f'{WORK}p{n}.json','w')); print(n,x1-x0,y1-y0)
