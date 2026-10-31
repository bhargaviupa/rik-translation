"""Contact sheets of header number strips (left + right outer edges of the header band) for reading printed page numbers by eye.
python3 numsheets.py FIRST LAST OUTPREFIX [PER_SHEET=48]   -> OUTPREFIX_<first>.png ; each tile is labelled with the PDF page."""
import sys,os,subprocess,tempfile
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0,os.path.dirname(__file__))
from cfg import part_of
from PIL import Image,ImageDraw
DPI=100; XL=(0.03,0.27); XR=(0.73,0.97); TH=62
import numpy as np
def header_y(im):
    """first sustained ink row below the top margin (locating only)"""
    a=np.array(im)<128; W=a.shape[1]; prof=a[:,int(W*.05):int(W*.95)].sum(1)
    H=len(prof)
    for y in range(int(H*.04),int(H*.45)):
        if prof[y:y+6].min()>=1 and prof[y:y+14].sum()>=40: return y
    return int(H*.15)
def strip(g):
    p,n=part_of(g); d=tempfile.mkdtemp()
    subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r',str(DPI),'-gray',p,d+'/p'],check=True)
    im=Image.open(d+'/'+os.listdir(d)[0]).convert('L'); subprocess.run(['rm','-rf',d])
    W,H=im.size; y=header_y(im); y0=max(0,y-8)
    box=lambda xs:im.crop((int(W*xs[0]),y0,int(W*xs[1]),y0+TH))
    a,b=box(XL),box(XR); t=Image.new('L',(a.width+b.width+4,a.height+12),255); t.paste(a,(0,12)); t.paste(b,(a.width+4,12))
    ImageDraw.Draw(t).text((2,0),str(g),fill=0); return t
if __name__=='__main__':
    a,b,pre=int(sys.argv[1]),int(sys.argv[2]),sys.argv[3]; per=int(sys.argv[4]) if len(sys.argv)>4 else 75
    for s in range(a,b+1,per):
        gs=list(range(s,min(b,s+per-1)+1))
        with ThreadPoolExecutor(4) as ex: ts=list(ex.map(strip,gs))
        w,h=ts[0].size; cols=5; rows=(len(ts)+cols-1)//cols; sh=Image.new('L',(cols*(w+6),rows*(h+6)),255)
        for i,t in enumerate(ts): sh.paste(t,((i%cols)*(w+6),(i//cols)*(h+6)))
        sh.save(f'{pre}_{s}.png'); print(f'{pre}_{s}.png',sh.size)
