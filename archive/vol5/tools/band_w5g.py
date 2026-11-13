"""w5g: stack horizontal bands of PDF pages for viewing. Specs: PDFPAGE:y0:y1:x0:x1 (fractions of the WHOLE page).
python3 band_w5g.py OUT.png DPI spec [spec ...]"""
import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from view import render
from PIL import Image,ImageDraw
OUT,dpi=sys.argv[1],int(sys.argv[2]); cr=[]
for s in sys.argv[3:]:
    g,y0,y1,x0,x1=s.split(':'); im=render(int(g),dpi); W,H=im.size
    cr.append((s,im.crop((int(float(x0)*W),int(float(y0)*H),int(float(x1)*W),int(float(y1)*H)))))
Wd=max(c.size[0] for s,c in cr)+16; o=Image.new('L',(Wd,sum(c.size[1]+8 for s,c in cr)),255); d=ImageDraw.Draw(o); y=0
for k,(s,c) in enumerate(cr,1): o.paste(c,(16,y)); d.text((1,y+c.size[1]//3),str(k),fill=0); y+=c.size[1]+8
o.save(OUT); print(o.size)
