"""Montage of the page-number corners (top-left + top-right of the text block) for eye reading.
python3 header_montage.py FIRST LAST OUT.png"""
import sys,os,subprocess,tempfile
sys.path.insert(0,os.path.dirname(__file__))
from cfg import WORK,part_of
from PIL import Image,ImageOps,ImageDraw,ImageFilter
def textbox(im):
    """text-block box, ignoring specks: rows/cols with enough dark pixels after a median filter"""
    b=ImageOps.invert(im).point(lambda v:255 if v>100 else 0).filter(ImageFilter.MedianFilter(3))
    w,h=b.size; px=b.load()
    rows=[y for y in range(h) if sum(px[x,y]>0 for x in range(0,w,2))>w*0.004]
    cols=[x for x in range(w) if sum(px[x,y]>0 for y in range(0,h,2))>h*0.004]
    return (cols[0],rows[0],cols[-1],rows[-1]) if rows and cols else (0,0,w,h)
if __name__!="__main__": pass
else:
    a,b,OUT=int(sys.argv[1]),int(sys.argv[2]),sys.argv[3]; tiles=[]
    for g in range(a,b+1):
        path,n=part_of(g); d=tempfile.mkdtemp(dir=WORK)
        subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','100','-gray',path,d+'/p'],check=True)
        im=Image.open(d+'/'+os.listdir(d)[0]).convert('L'); subprocess.run(['rm','-rf',d])
        bb=textbox(im)
        w=bb[2]-bb[0]; hh=int(w*0.06); cw=int(w*0.16)
        L=im.crop((bb[0],bb[1],bb[0]+cw,bb[1]+hh)); R=im.crop((bb[2]-cw,bb[1],bb[2],bb[1]+hh))
        t=Image.new('L',(2*cw+44,hh),255); t.paste(L,(40,0)); t.paste(R,(44+cw,0))
        ImageDraw.Draw(t).text((2,2),str(g),fill=0); tiles.append(t)
    cols=4; tw=max(t.width for t in tiles); th=max(t.height for t in tiles)
    m=Image.new('L',(cols*(tw+8),((len(tiles)+cols-1)//cols)*(th+4)),255)
    for i,t in enumerate(tiles): m.paste(t,((i%cols)*(tw+8),(i//cols)*(th+4)))
    m.save(OUT); print(m.size)

