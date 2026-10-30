"""LOCATING ONLY: scan PDF pages for the Sukta heading block (token containing 'ಸಂಖ್ಯೆ' = 'rik-samkhye' line). Writes review/sukta_blocks_v13.json {pdfpage: y_fraction}. Readings come from viewing the crops.
python3 findsukta.py FIRST LAST [JOBS]"""
import sys,os,json,csv,io,subprocess,tempfile
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0,os.path.dirname(__file__))
import cfg
from PIL import Image
def one(g):
    p,n=cfg.part_of(g); d=tempfile.mkdtemp()
    subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','100','-gray',p,d+'/p'],check=True)
    f=d+'/'+os.listdir(d)[0]; H=Image.open(f).size[1]
    t=subprocess.run(['tesseract',f,'-','-l','kan','--psm','6','tsv'],capture_output=True,text=True).stdout
    subprocess.run(['rm','-rf',d])
    rows=list(csv.DictReader(io.StringIO(t),delimiter='\t',quoting=csv.QUOTE_NONE))
    ys=[round(int(r['top'])/H,3) for r in rows if r.get('text') and 'ಸಂಖ್ಯೆ' in r['text'] and int(r['top'])/H>0.12]
    return g,ys
a,b=int(sys.argv[1]),int(sys.argv[2]); J=int(sys.argv[3]) if len(sys.argv)>3 else 4
out={}
with ThreadPoolExecutor(J) as ex:
    for g,ys in ex.map(one,range(a,b+1)):
        if ys: out[g]=ys
json.dump(out,open(os.path.join(cfg.REVIEW,'sukta_blocks_v13.json'),'w'),indent=0); print(out)
