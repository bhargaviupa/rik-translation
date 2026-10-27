"""List the large-type lines of a page (Saṃhitā / Pada verses) as page fractions: biglines.py PDF"""
import sys,os,subprocess,tempfile
sys.path.insert(0,os.path.dirname(__file__))
from cfg import part_of,WORK
from PIL import Image,ImageOps
g=int(sys.argv[1]); path,n=part_of(g); d=tempfile.mkdtemp(dir=WORK)
subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','100','-gray',path,d+'/p'],check=True)
im=Image.open(d+'/'+os.listdir(d)[0]); subprocess.run(['rm','-rf',d])
bw=ImageOps.invert(im).point(lambda v:255 if v>110 else 0); px=bw.load(); w,h=bw.size
rows=[sum(px[x,y]>0 for x in range(0,w,2)) for y in range(h)]
lines=[]; y=0
while y<h:
    if rows[y]>2:
        s=y
        while y<h and rows[y]>2: y+=1
        if y-s>=5: lines.append((s,y))
    y+=1
hs=sorted(e-s for s,e in lines); med=hs[len(hs)//2] if hs else 0
for s,e in lines:
    if e-s>=1.5*med: print(f"{s/h:.3f} {e/h:.3f} h={e-s}")
print('median',med,'lines',len(lines))
