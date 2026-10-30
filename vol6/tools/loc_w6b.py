"""w6b helper: LOCATE lines on a printed page (OCR used only to find line positions, never for readings).
python3 loc_w6b.py PRINTED [REGEX]  -> 'y0-y1 x0-x1: ocr-text' as WHOLE-page fractions for OCR lines matching REGEX."""
import sys,os,re,subprocess,csv,io
sys.path.insert(0,os.path.dirname(__file__))
from cfg import WORK,OFFSET
from view import render
pg=int(sys.argv[1]); rx=re.compile(sys.argv[2] if len(sys.argv)>2 else '.')
c=os.path.join(WORK,f'loc_{pg}.png')
if not os.path.exists(c): render(pg+OFFSET,200).save(c)
from PIL import Image
W,H=Image.open(c).size
t=subprocess.run(['tesseract',c,'-','-l','kan+eng','tsv'],capture_output=True,text=True).stdout
L={}
for r in csv.DictReader(io.StringIO(t),delimiter='\t',quoting=csv.QUOTE_NONE):
    if r['level']!='5' or not r['text'].strip(): continue
    k=(r['block_num'],r['par_num'],r['line_num']); x,y,w,h=map(int,(r['left'],r['top'],r['width'],r['height']))
    a=L.setdefault(k,[x,y,x+w,y+h,[]]); a[0]=min(a[0],x);a[1]=min(a[1],y);a[2]=max(a[2],x+w);a[3]=max(a[3],y+h);a[4].append(r['text'])
for a in sorted(L.values(),key=lambda a:a[1]):
    s=' '.join(a[4])
    if rx.search(s): print(f'{a[1]/H:.3f}-{a[3]/H:.3f} {a[0]/W:.2f}-{a[2]/W:.2f}: {s[:70]}')
