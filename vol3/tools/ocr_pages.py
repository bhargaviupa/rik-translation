"""OCR (Kannada, 300 dpi, psm 6) of scan pages -> vol3/review/ocr/PDF.json = [[top,left,height,text],...] per text line (page coords at 300 dpi).
python3 ocr_pages.py FIRST LAST   (global PDF pages; needs tesseract-ocr-kan; 4 processes)"""
import sys,os,subprocess,tempfile,json,csv
sys.path.insert(0,os.path.dirname(__file__))
from cfg import WORK,part_of,VOL
from concurrent.futures import ProcessPoolExecutor
OUT=os.path.join(VOL,'review','ocr'); os.makedirs(OUT,exist_ok=True)
ENV=dict(os.environ,OMP_THREAD_LIMIT='1')
def one(g):
    f=os.path.join(OUT,f'{g}.json')
    if os.path.exists(f): return g
    path,n=part_of(g); d=tempfile.mkdtemp(dir=WORK)
    subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','300','-gray','-png','-singlefile',path,d+'/p'],check=True)
    subprocess.run(['tesseract',d+'/p.png',d+'/o','-l','kan','--psm','6','tsv'],capture_output=True,env=ENV)
    rows=list(csv.DictReader(open(d+'/o.tsv',encoding='utf8'),delimiter='\t',quoting=csv.QUOTE_NONE))
    L={}
    for r in rows:
        if r['text'].strip(): L.setdefault((r['block_num'],r['par_num'],r['line_num']),[]).append(r)
    out=[[int(min(int(x['top']) for x in w)),int(min(int(x['left']) for x in w)),int(max(int(x['height']) for x in w)),' '.join(x['text'] for x in w)] for w in L.values()]
    out.sort()
    json.dump(out,open(f,'w',encoding='utf8'),ensure_ascii=False); subprocess.run(['rm','-rf',d]); return g
if __name__=='__main__':
    a,b=int(sys.argv[1]),int(sys.argv[2])
    with ProcessPoolExecutor(4) as ex:
        for g in ex.map(one,range(a,b+1)): pass
