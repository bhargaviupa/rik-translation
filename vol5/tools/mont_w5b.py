"""w5b: stack several tight crops of one PDF page into one image.
python3 mont_w5b.py PDF OUT DPI y0,y1,x0,x1 [y0,y1,x0,x1 ...]"""
import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from view import render
from PIL import Image
g,OUT,dpi=int(sys.argv[1]),sys.argv[2],int(sys.argv[3])
im=render(g,dpi).convert('L');W,H=im.size;cs=[]
for s in sys.argv[4:]:
    y0,y1,x0,x1=map(float,s.split(','));cs.append(im.crop((int(W*x0),int(H*y0),int(W*x1),int(H*y1))))
o=Image.new('L',(max(c.width for c in cs),sum(c.height+6 for c in cs)),255);y=0
for c in cs:o.paste(c,(0,y));y+=c.height+6
o.save(OUT)
