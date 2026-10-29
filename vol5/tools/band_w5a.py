"""Crop by text-block fractions (as printed by lines_w5a.py A=0 at 120 dpi), at a higher dpi.
python3 band_w5a.py PDFPAGE OUT.png DPI v0 v1 [x0 x1]  (x may exceed the text box: -0.05..1.05)"""
import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from view import render,textbox
g,OUT,dpi,v0,v1=int(sys.argv[1]),sys.argv[2],int(sys.argv[3]),float(sys.argv[4]),float(sys.argv[5])
x0f,x1f=(float(sys.argv[6]),float(sys.argv[7])) if len(sys.argv)>7 else (-0.03,1.03)
x0,t0,x1,t1=[int(v*dpi/40) for v in textbox(render(g,40))]; im=render(g,dpi); W=x1-x0; H=t1-t0
im.crop((int(x0+x0f*W),int(t0+v0*H),int(x0+x1f*W),int(t0+v1*H))).save(OUT); print(im.size)
