"""Find numeral groups on scan pages with Tesseract word boxes (positions only; the reading is one vote).
python3 locate.py FIRST LAST  -> WORK/numerals.json  {pdf: [{box:[x,y,w,h] @300dpi, tess, conf, line}]}"""
import sys,subprocess,json,os,re,csv,io
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..','verify11'))
from cfg import WORK,SCAN
KD='೦೧೨೩೪೫೬೭೮೯'
out=json.load(open(WORK+'numerals.json')) if os.path.exists(WORK+'numerals.json') else {}
for n in range(int(sys.argv[1]),int(sys.argv[2])+1):
    b=f'{WORK}t/l{n}'; os.makedirs(WORK+'t',exist_ok=True)
    subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','300','-gray',SCAN,b],check=True)
    img=[f for f in os.listdir(WORK+'t') if f.startswith(f'l{n}-')][0]
    tsv=subprocess.run(['tesseract',WORK+'t/'+img,'-','-l','kan','--psm','4','tsv'],capture_output=True,text=True).stdout
    os.remove(WORK+'t/'+img)
    toks=[]
    for r in csv.DictReader(io.StringIO(tsv),delimiter='\t',quoting=csv.QUOTE_NONE):
        t=r['text'] or ''
        if sum(c in KD for c in t)>=1 and re.search(f'[{KD}]',t):
            toks.append(dict(box=[int(r['left']),int(r['top']),int(r['width']),int(r['height'])],tess=t,conf=float(r['conf']),
                             line=f"{r['block_num']}.{r['par_num']}.{r['line_num']}"))
    out[str(n)]=toks; print(n,len(toks),flush=True)
json.dump(out,open(WORK+'numerals.json','w'),ensure_ascii=False)
