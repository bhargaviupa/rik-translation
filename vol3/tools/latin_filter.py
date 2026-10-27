"""Drop located 'numeral' boxes that are really Latin type (the printed English translation at the foot of the
Bhumika pages, which Tesseract's Kannada model reads as digits). A box is dropped when it overlaps a word on a line that Tesseract eng reads as
at least 3 confident (>= MINCONF) English words of >= 3 letters, no digits (Kannada ೦/೧ read as 'o'/'n' do not count).
python3 latin_filter.py FIRST LAST [JOBS]   (global PDF pages; rewrites WORK/numerals.json in place, keeps a .bak)"""
import sys,os,re,csv,io,json,shutil,subprocess,tempfile
from concurrent.futures import ProcessPoolExecutor
sys.path.insert(0,os.path.dirname(__file__))
from cfg import WORK,part_of
MINCONF=80
ENV=dict(os.environ,OMP_THREAD_LIMIT='1')
def latin_words(g):
    path,n=part_of(g); d=tempfile.mkdtemp(dir=WORK)
    subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','300','-gray',path,d+'/p'],check=True)   # same dpi as locate.py
    img=d+'/'+os.listdir(d)[0]
    tsv=subprocess.run(['tesseract',img,'-','-l','eng','--psm','3','tsv'],capture_output=True,text=True,env=ENV).stdout
    subprocess.run(['rm','-rf',d]); lines={}
    for r in csv.DictReader(io.StringIO(tsv),delimiter='\t',quoting=csv.QUOTE_NONE):
        w=(r.get('text') or '').strip()
        try: c=float(r['conf']); key=(r['block_num'],r['par_num'],r['line_num'])
        except (ValueError,TypeError,KeyError): continue
        if not w: continue
        bb=[int(r['left']),int(r['top']),int(r['width']),int(r['height'])]
        good=c>=MINCONF and len(re.findall('[A-Za-z]',w))>=3 and not re.search(r'\d',w) and not re.fullmatch(r'[noOuUcCe\-–.,;:()]+',w)
        lines.setdefault(key,[]).append((good,bb))
    out=[]
    for ws in lines.values():   # an English line: at least 3 confident English words on it; then every word box on it counts
        if sum(g for g,_ in ws)>=3: out+= [bb for _,bb in ws]
    return g,out
def overlap(a,b):
    ax,ay,aw,ah=a; bx,by,bw,bh=b
    ix=max(0,min(ax+aw,bx+bw)-max(ax,bx)); iy=max(0,min(ay+ah,by+bh)-max(ay,by))
    return ix*iy>0.3*min(aw*ah,bw*bh)
if __name__=='__main__':
    a,b=int(sys.argv[1]),int(sys.argv[2]); jobs=int(sys.argv[3]) if len(sys.argv)>3 else 4
    N=WORK+'numerals.json'; shutil.copy(N,N+'.bak'); T=json.load(open(N)); dropped=0
    with ProcessPoolExecutor(jobs) as ex:
        for g,words in ex.map(latin_words,range(a,b+1)):
            k=str(g); keep=[t for t in T.get(k,[]) if not any(overlap(t['box'],w) for w in words)]
            dropped+=len(T.get(k,[]))-len(keep); T[k]=keep
    json.dump(T,open(N,'w'),ensure_ascii=False); print('dropped',dropped)
