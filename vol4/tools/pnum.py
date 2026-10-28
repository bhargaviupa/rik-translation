"""OCR the Latin page number in the top corners of each page: pnum.py FIRST LAST -> WORK/pnum.json"""
import sys,os,subprocess,tempfile,json,re
sys.path.insert(0,os.path.dirname(__file__))
from cfg import WORK,part_of
from header_montage import textbox
from PIL import Image
from concurrent.futures import ProcessPoolExecutor
ENV=dict(os.environ,OMP_THREAD_LIMIT='1')
def one(g):
    path,n=part_of(g); d=tempfile.mkdtemp(dir=WORK)
    subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','200','-gray',path,d+'/p'],check=True)
    im=Image.open(d+'/'+os.listdir(d)[0]).convert('L'); bb=textbox(im)
    w=bb[2]-bb[0]; hh=int(w*0.06); cw=int(w*0.16); out=[]
    for box in ((bb[0],bb[1],bb[0]+cw,bb[1]+hh),(bb[2]-cw,bb[1],bb[2],bb[1]+hh)):
        im.crop(box).save(d+'/c.png')
        t=subprocess.run(['tesseract',d+'/c.png','-','--psm','7','-c','tessedit_char_whitelist=0123456789'],capture_output=True,text=True,env=ENV).stdout
        out.append(re.sub(r'\D','',t))
    subprocess.run(['rm','-rf',d]); return g,out
if __name__=='__main__':
    a,b=int(sys.argv[1]),int(sys.argv[2]); P=WORK+'pnum.json'
    R=json.load(open(P)) if os.path.exists(P) else {}
    with ProcessPoolExecutor(4) as ex:
        for g,o in ex.map(one,range(a,b+1)): R[str(g)]=o
    json.dump(R,open(P,'w'))
