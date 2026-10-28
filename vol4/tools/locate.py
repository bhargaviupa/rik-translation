"""Find numeral groups (positions only) and the printed page number on Vol 4 scan pages.
python3 locate.py FIRST LAST [JOBS]  (global PDF pages) -> WORK/numerals.json, WORK/headers.json
Tesseract is used only for word boxes and the header digits, never as the numeral reader."""
import sys,os,re,csv,io,json,subprocess,tempfile
from concurrent.futures import ProcessPoolExecutor
sys.path.insert(0,os.path.dirname(__file__))
from cfg import WORK,part_of
from PIL import Image,ImageOps
KD='೦೧೨೩೪೫೬೭೮೯'
ENV=dict(os.environ,OMP_THREAD_LIMIT='1')
def keep(t):
    core=re.sub(r'[()\[\].,;:।॥|\'"`]','',t); nd=sum(c in KD for c in core)
    return bool(re.search(f'[{KD}]\\s*-\\s*[{KD}]',core)) or (nd>=1 and nd>=0.75*len(core))
def one(g):
    path,n=part_of(g); d=tempfile.mkdtemp(dir=WORK)
    subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','300','-gray',path,d+'/p'],check=True)
    img=d+'/'+os.listdir(d)[0]
    try:
        tsv=subprocess.run(['timeout','60','tesseract',img,'-','-l','kan','--psm','4','tsv'],capture_output=True,text=True,env=ENV).stdout
    except Exception: tsv=''
    toks=[]
    for r in csv.DictReader(io.StringIO(tsv),delimiter='\t',quoting=csv.QUOTE_NONE):
        t=(r['text'] or '').strip()
        if t and keep(t):
            toks.append(dict(box=[int(r['left']),int(r['top']),int(r['width']),int(r['height'])],tess=t,
                             line=f"{r['block_num']}.{r['par_num']}.{r['line_num']}"))
    # printed page number: top strip of the text block, Latin digits / roman
    im=Image.open(img).convert('L'); bb=ImageOps.invert(im).point(lambda v:255 if v>80 else 0).getbbox() or (0,0)+im.size
    strip=im.crop((bb[0],bb[1],bb[2],bb[1]+int((bb[2]-bb[0])*0.07))); sp=d+'/h.png'; strip.save(sp)
    h=subprocess.run(['timeout','30','tesseract',sp,'-','-l','eng','--psm','6'],capture_output=True,text=True,env=ENV).stdout
    subprocess.run(['rm','-rf',d])
    return g,toks,h.strip()
if __name__=='__main__':
    a,b=int(sys.argv[1]),int(sys.argv[2]); jobs=int(sys.argv[3]) if len(sys.argv)>3 else 4
    N=WORK+'numerals.json'; H=WORK+'headers.json'
    out=json.load(open(N)) if os.path.exists(N) else {}; hd=json.load(open(H)) if os.path.exists(H) else {}
    with ProcessPoolExecutor(jobs) as ex:
        for g,toks,h in ex.map(one,range(a,b+1)):
            out[str(g)]=toks; hd[str(g)]=h; print(g,len(toks),repr(h[:40]),flush=True)
    json.dump(out,open(N,'w'),ensure_ascii=False); json.dump(hd,open(H,'w'),ensure_ascii=False,indent=0)
