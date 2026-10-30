"""Crop bands of a Vol 6 scan page by fractions of the WHOLE rendered page (as seen in view.py's full view, which is the full page).
python3 pcrop_w6a.py PDFPAGE OUT.png DPI y0,y1[,x0,x1] [y0,y1[,x0,x1] ...]  (bands stacked into one image)"""
import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from view import render
from PIL import Image
g,OUT,dpi=int(sys.argv[1]),sys.argv[2],int(sys.argv[3]); im=render(g,dpi); W,H=im.size; ims=[]
for s in sys.argv[4:]:
    a=[float(v) for v in s.split(',')]; y0,y1=a[0],a[1]; x0,x1=(a[2],a[3]) if len(a)>3 else (0,1)
    ims.append(im.crop((int(W*x0),int(H*y0),int(W*x1),int(H*y1))))
w=max(i.width for i in ims); o=Image.new('L',(w,sum(i.height+6 for i in ims)),255); y=0
for i in ims: o.paste(i,(0,y)); y+=i.height+6
o.save(OUT); print(o.size)
