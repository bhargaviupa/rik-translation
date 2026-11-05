"""Render pages for reading, or zoom into a box.
python3 tools/rv/page.py VOL PDFPAGE OUTPREFIX [--dpi 400] [--strips N]          -> OUTPREFIX_0.png ... (top to bottom, full width)
python3 tools/rv/page.py VOL PDFPAGE OUTPREFIX --strip K --box X0 Y0 X1 Y1 [--dpi 600]   -> OUTPREFIX_z.png
The box is in the pixel coordinates of strip K as DISPLAYED to you (if the viewer reports a scale factor, multiply by it first).
Make the box a generous full line; check the zoom shows the intended word before reading it."""
import sys,os
sys.path.insert(0,os.path.dirname(__file__)); import rvlib
a=sys.argv[1:]
if len(a)<3: sys.exit(__doc__)
vol,g,out=int(a[0]),int(a[1]),a[2]; opt=lambda k,d:type(d)(a[a.index(k)+1]) if k in a else d
cfg=rvlib.Cfg(vol)
if '--strip' in a:
    k=int(a[a.index('--strip')+1]); b=[float(x) for x in a[a.index('--box')+1:a.index('--box')+5]]
    print(*rvlib.zoom(cfg,g,out,k,b,zdpi=opt('--dpi',600)))
else:
    for f,sz,d in rvlib.strips(cfg,g,out,dpi=opt('--dpi',400),n=opt('--strips',None)): print(f,sz,f'{d} dpi')
