"""Stack line crops from several Vol 6 pages into one image (no OCR).
python3 multi_w6a.py OUT.png DPI PDFPAGE:SPEC[,SPEC...] ...   SPEC as in lines_w6a.py (i[-j][:x0:x1]); a label strip gives the PDF page."""
import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from view import render
from lines_w6a import bands
from PIL import Image,ImageDraw
OUT,dpi=sys.argv[1],int(sys.argv[2]); ims=[]
for a in sys.argv[3:]:
    g,specs=a.split(':',1); g=int(g); B=bands(g); im=render(g,dpi); W,H=im.size
    lab=Image.new('L',(300,22),200); ImageDraw.Draw(lab).text((4,4),f'PDF {g} = p. {g-19}',fill=0); ims.append(lab)
    for sp in specs.split(','):
        p=sp.split(':'); ij=p[0].split('-'); i=int(ij[0]); j=int(ij[-1]); x0,x1=(float(p[1]),float(p[2])) if len(p)>2 else (0,1)
        ims.append(im.crop((int(W*x0),int(H*(B[i][0]-0.006)),int(W*x1),int(H*(B[j][1]+0.006)))))
w=max(i.width for i in ims); o=Image.new('L',(w,sum(i.height+6 for i in ims)),255); y=0
for i in ims: o.paste(i,(0,y)); y+=i.height+6
o.save(OUT); print(o.size)
