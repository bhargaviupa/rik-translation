"""w5g: locate 'ref ಮತ್ತು ref' groups (the print's 'and' = ಮತ್ತು) on a PDF page of the better scan, crop each at DPI and stack.
Locating only (tesseract kan used for positions, never for readings).
python3 andq_w5g.py PDFPAGE OUT.png [dpi=450] [WORDS=ಮತ್ತು,ರಿಂದ]  -> prints index/box list"""
import sys,os,subprocess,tempfile,re
sys.path.insert(0,os.path.dirname(__file__))
from view import render
from PIL import Image,ImageDraw
g,OUT=int(sys.argv[1]),sys.argv[2]; dpi=int(sys.argv[3]) if len(sys.argv)>3 else 450
WIN=(float(sys.argv[4]),float(sys.argv[5])) if len(sys.argv)>5 else None   # y window (fractions): loose mode, any digit nearby
im=render(g,300); f=tempfile.mktemp(suffix='.png',dir=os.environ.get('V5WORK','/tmp')); im.save(f)
tsv=subprocess.run(['tesseract',f,'-','-l','kan','--psm','4','tsv'],capture_output=True,text=True).stdout.splitlines()[1:]
W=[]
for r in tsv:
    c=r.split('\t')
    if len(c)>=12 and c[11].strip(): W.append((int(c[2]),int(c[3]),int(c[6]),int(c[7]),int(c[8]),int(c[9]),c[11]))
hits=[]
for i,w in enumerate(W):
    if re.search('ಮತ್ತು|ರಿಂದ',w[6]):
        # require a digit-bearing word within 3 words before, same line
        prev=[v for v in W[max(0,i-2):i] if re.search('[೦-೯]\\W?[-–_.]\\W?[೦-೯]',v[6]) and abs(v[3]-w[3])<30]
        nxt=[v for v in W[i+1:i+3] if re.search('[೦-೯]',v[6]) and abs(v[3]-w[3])<30]
        if WIN:
            loose=[v for v in W[max(0,i-4):i+4] if re.search('[೦-೯]',v[6]) and abs(v[3]-w[3])<30]
            if loose and WIN[0]<=w[3]/im.size[1]<=WIN[1]: hits.append(w)
        elif prev and nxt: hits.append(w)
big=render(g,dpi); k=dpi/300; crops=[]
for n,w in enumerate(hits,1):
    x0=max(0,int((w[2]-330)*k)); x1=min(big.size[0],int((w[2]+w[4]+330)*k)); y0=int((w[3]-14)*k); y1=int((w[3]+w[5]+14)*k)
    crops.append((n,big.crop((x0,y0,x1,y1))))
    print(n,round(w[3]/im.size[1],3),w[6])
if crops:
    Wd=max(c.size[0] for n,c in crops)+50; img=Image.new('L',(Wd,sum(c.size[1]+8 for n,c in crops)),255); d=ImageDraw.Draw(img); y=0
    for n,c in crops: img.paste(c,(50,y)); d.text((2,y+c.size[1]//3),str(n),fill=0); y+=c.size[1]+8
    img.save(OUT); print(img.size)
