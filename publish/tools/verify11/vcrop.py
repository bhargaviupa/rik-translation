"""Crop a page region (fractions of page) at 400 dpi and split into left/right halves -> WORK/<tag>L.png, <tag>R.png
Used for Saṃhitā verse blocks when adding accents.  python3 vcrop.py PDFPAGE y0 y1 x0 x1 tag   e.g. 72 0.62 0.86 0.19 0.90 d72"""
import sys,subprocess,glob
from PIL import Image
from cfg import WORK,SCAN
n=int(sys.argv[1]); y0,y1,x0,x1=map(float,sys.argv[2:6]); tag=sys.argv[6]
subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','400','-gray',SCAN,f'{WORK}hi{n}'],check=True)
a=Image.open(glob.glob(f'{WORK}hi{n}-*.pgm')[0]); W,H=a.size
c=a.crop((int(W*x0),int(H*y0),int(W*x1),int(H*y1))); w,h=c.size; m=w//2
c.crop((0,0,m+60,h)).save(f'{WORK}{tag}L.png'); c.crop((m-60,0,w,h)).save(f'{WORK}{tag}R.png'); print(c.size)
