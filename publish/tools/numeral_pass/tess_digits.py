"""Method B: Tesseract on each numeral crop, digits-only whitelist, several preprocessings; majority vote.
python3 tess_digits.py ITEMS.csv OUT.csv   (ITEMS has pdf, box600)"""
import sys,os,csv,glob,subprocess,collections
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..','verify11'))
from cfg import WORK,SCAN
from PIL import Image,ImageFilter,ImageOps
KD='೦೧೨೩೪೫೬೭೮೯'; TR=str.maketrans(KD,'0123456789')
def ocr(im):
    im.save(WORK+'td.png')
    r=subprocess.run(['tesseract',WORK+'td.png','-','-l','kan','--psm','7','-c','tessedit_char_whitelist='+KD+'-'],capture_output=True,text=True).stdout
    return ''.join(c for c in r.translate(TR) if c.isdigit() or c=='-').strip('-')
rows=list(csv.DictReader(open(sys.argv[1]))); out=[]; cur=None
for r in rows:
    p=int(r['pdf'])
    if p!=cur:
        for f in glob.glob(WORK+'g-*.pgm'): os.remove(f)
        subprocess.run(['pdftoppm','-f',str(p),'-l',str(p),'-r','600','-gray',SCAN,WORK+'g'],check=True)
        page=Image.open(glob.glob(WORK+'g-*.pgm')[0]); cur=p
    x0,y0,x1,y1=map(int,r['box600'].split()); c=page.crop((x0+40,y0,x1-40,y1)).convert('L')
    h=c.resize((c.width//2,c.height//2),Image.LANCZOS)
    vs=[ocr(ImageOps.expand(h,20,255)),
        ocr(ImageOps.expand(c.resize((c.width*2//5,c.height*2//5),Image.LANCZOS),16,255)),
        ocr(ImageOps.expand(c.resize((c.width*3//5,c.height*3//5),Image.LANCZOS),24,255))]
    v=collections.Counter(vs).most_common(1)[0]
    out.append(dict(id=r['id'],tess=v[0],agree=v[1],votes='|'.join(vs)))
    print(r['id'],vs,flush=True)
w=csv.DictWriter(open(sys.argv[2],'w',newline=''),fieldnames=['id','tess','agree','votes']); w.writeheader(); w.writerows(out)
