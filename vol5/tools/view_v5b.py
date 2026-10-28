"""v5b viewer: render a PDF page of the Vol 5 scan and crop by fractions of the WHOLE page (no text-block detection,
which clips some pages). python3 view_v5b.py PDFPAGE OUT.png [DPI] [y0 y1] [x0 x1]"""
import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from view import render
g,OUT=int(sys.argv[1]),sys.argv[2]; dpi=int(sys.argv[3]) if len(sys.argv)>3 else 130
y0,y1=(float(sys.argv[4]),float(sys.argv[5])) if len(sys.argv)>5 else (0,1)
x0,x1=(float(sys.argv[6]),float(sys.argv[7])) if len(sys.argv)>7 else (0.05,0.97)
im=render(g,dpi); W,H=im.size
im.crop((int(W*x0),int(H*y0),int(W*x1),int(H*y1))).save(OUT); print(im.size)
