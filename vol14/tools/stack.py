"""Stack several crops (whole-page-block fractions, as view.py) into one image for a single view.
python3 stack.py OUT.png DPI PAGE:y0:y1:x0:x1 [PAGE:y0:y1:x0:x1 ...]   (whole-page fractions; omit x for full width)"""
import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from view import crop
from PIL import Image
if __name__=='__main__':
    out,dpi=sys.argv[1],int(sys.argv[2]); cs=[]
    for a in sys.argv[3:]:
        f=a.split(':'); g=int(f[0]); y0,y1=float(f[1]),float(f[2]); x0,x1=(float(f[3]),float(f[4])) if len(f)>4 else (0,1)
        cs.append(crop(g,dpi,y0,y1,x0,x1))
    W=max(c.width for c in cs); H=sum(c.height+6 for c in cs); im=Image.new('L',(W,H),255); y=0
    for c in cs: im.paste(c,(0,y)); y+=c.height+6
    im.save(out); print(im.size)
