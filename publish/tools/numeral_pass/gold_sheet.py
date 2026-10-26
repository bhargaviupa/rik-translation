"""Pick ~N numeral groups from WORK/numerals.json and make numbered contact sheets (no readings shown).
python3 gold_sheet.py N OUTDIR  -> OUTDIR/sheet_K.png, OUTDIR/gold_items.csv (id,pdf,box600,tess)"""
import sys,json,os,random,subprocess,glob,csv
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..','verify11'))
from cfg import WORK,SCAN
from PIL import Image,ImageDraw,ImageFont
N=int(sys.argv[1]); OUT=sys.argv[2]; os.makedirs(OUT,exist_ok=True)
D=json.load(open(WORK+'numerals.json')); random.seed(11)
HARD='೩೫೬೭೨೯೮'
cand=[]
for p,toks in D.items():
    for t in toks:
        s=t['tess']; nd=sum(c in '೦೧೨೩೪೫೬೭೮೯' for c in s)
        if '-' in s and nd>=3: cand.append((int(p),t,sum(c in HARD for c in s)))
# per page at most 2, weight by hard digits
random.shuffle(cand); cand.sort(key=lambda x:-x[2]); seen={}; pick=[]
for p,t,h in cand:
    if seen.get(p,0)>=2: continue
    seen[p]=seen.get(p,0)+1; pick.append((p,t))
    if len(pick)>=N: break
pick.sort(key=lambda x:(x[0],x[1]['box'][1],x[1]['box'][0]))
font=ImageFont.truetype(glob.glob('/usr/share/fonts/**/DejaVuSans-Bold.ttf',recursive=True)[0],34)
crops=[]; cur=None
for i,(p,t) in enumerate(pick,1):
    if cur!=p:
        for f in glob.glob(WORK+'g-*.pgm'): os.remove(f)
        subprocess.run(['pdftoppm','-f',str(p),'-l',str(p),'-r','600','-gray',SCAN,WORK+'g'],check=True)
        page=Image.open(glob.glob(WORK+'g-*.pgm')[0]); cur=p
    x,y,w,h=[v*2 for v in t['box']]; pad=24
    box=(x-pad-40,y-pad,x+w+pad+40,y+h+pad)   # a little context on both sides
    crops.append((i,p,box,t['tess'],page.crop(box)))
per=25
for k in range(0,len(crops),per):
    part=crops[k:k+per]; cw=max(c[4].size[0] for c in part)+130; rh=[c[4].size[1]+20 for c in part]
    sheet=Image.new('L',(cw*1,sum(rh)),255); d=ImageDraw.Draw(sheet); y=0
    for (i,p,box,tess,im),h in zip(part,rh):
        d.text((8,y+h//2-20),str(i),fill=0,font=font); sheet.paste(im,(120,y+10)); d.line((0,y+h-1,cw,y+h-1),fill=180); y+=h
    sheet.save(f'{OUT}/sheet_{k//per+1}.png')
with open(f'{OUT}/gold_items.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['id','pdf','printed','box600','tess_whole_page'])
    for i,p,box,tess,_ in crops: w.writerow([i,p,p-18,' '.join(map(str,box)),tess])
print(len(crops))
