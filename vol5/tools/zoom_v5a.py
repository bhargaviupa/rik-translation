"""Zoom on a region given in pixel coordinates of the 130-dpi view made by view.py (same text-block crop).
python3 zoom_v5a.py PDFPAGE OUT.png DPI y0 y1 [x0 x1]   (pixels of the 130-dpi image)"""
import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from view import textbox,render
g,OUT,dpi=int(sys.argv[1]),sys.argv[2],int(sys.argv[3])
y0,y1=float(sys.argv[4]),float(sys.argv[5])
x0p,x1p=(float(sys.argv[6]),float(sys.argv[7])) if len(sys.argv)>7 else (0,1e9)
k=dpi/40; X0,T0,X1,T1=[int(v*k) for v in textbox(render(g,40))]
im=render(g,dpi); s=dpi/130
L=X0-8+int(x0p*s); R=min(X1+8,X0-8+int(x1p*s)); im.crop((max(0,L),T0-8+int(y0*s),R,T0-8+int(y1*s))).save(OUT); print(im.size)
