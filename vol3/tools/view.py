"""Render the text block of a global PDF page of the better scan for viewing.
python3 view.py PDF OUT.png [DPI] [y0 y1]   (y0/y1: fractions of the text block height)"""
import sys,os,subprocess,tempfile
sys.path.insert(0,os.path.dirname(__file__))
from cfg import WORK,part_of
from PIL import Image,ImageOps,ImageFilter
def textbox(im):
    b=ImageOps.invert(im).point(lambda v:255 if v>100 else 0).filter(ImageFilter.MedianFilter(3)); w,h=b.size; px=b.load()
    rows=[y for y in range(h) if sum(px[x,y]>0 for x in range(0,w,2))>w*0.004]
    cols=[x for x in range(w) if sum(px[x,y]>0 for y in range(0,h,2))>h*0.004]
    return (cols[0],rows[0],cols[-1],rows[-1]) if rows and cols else (0,0,w,h)
if __name__=='__main__':
    g,OUT=int(sys.argv[1]),sys.argv[2]; dpi=int(sys.argv[3]) if len(sys.argv)>3 else 130
    y0,y1=(float(sys.argv[4]),float(sys.argv[5])) if len(sys.argv)>5 else (0,1)
    path,n=part_of(g)
    def render(r):
        d=tempfile.mkdtemp(dir=WORK); subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r',str(r),'-gray',path,d+'/p'],check=True)
        im=Image.open(d+'/'+os.listdir(d)[0]).convert('L'); subprocess.run(['rm','-rf',d]); return im
    k=dpi/40; x0,t0,x1,t1=[int(v*k) for v in textbox(render(40))]   # text box from a fixed 40 dpi render, so fractions agree at any dpi
    im=render(dpi)
    H=t1-t0; im.crop((max(0,x0-8),t0+int(H*y0)-8,x1+8,t0+int(H*y1)+8)).save(OUT); print(im.size)
