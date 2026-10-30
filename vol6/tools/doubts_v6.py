"""HTML page for the doubts a worker could NOT resolve (words, accents, letters, numerals): one row per doubt, a crop of the scan line(s), the file's text, an empty box for the user's reading.
python3 doubts_v6.py DOUBTS.json OUT.html [TITLE]
DOUBTS.json = list of {"page": PRINTED, "y0":0.31,"y1":0.36,"x0":0.0,"x1":1.0 (fractions of the text block as for view.py, optional x), "kind":"word|accent|numeral|other", "file":"the text as now in the file (with [?])", "ctx":"words around it", "note":"what is doubtful" }
The crop is the page band (200 dpi, grayscale; PDF = printed + OFFSET from cfg.py). The user's box is saved by the artifact page; the coordinator applies the readings (exact text in "file" is replaced, uniquely by "ctx")."""
import sys,os,io,re,json,base64,html,subprocess,tempfile
sys.path.insert(0,os.path.dirname(__file__))
from cfg import WORK,part_of,OFFSET
from PIL import Image
src,OUT=sys.argv[1],sys.argv[2]; TITLE=sys.argv[3] if len(sys.argv)>3 else 'Vol 6: doubts the worker could not resolve'
D=json.load(open(src,encoding='utf8')); rows=[]; cache={}
for k,d in enumerate(D):
    p=int(d['page']); g=p+OFFSET
    if g not in cache:
        path,n=part_of(g); t=tempfile.mkdtemp(dir=WORK)
        subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','200','-gray',path,t+'/h'],check=True)
        cache[g]=Image.open(t+'/'+os.listdir(t)[0]).convert('L'); subprocess.run(['rm','-rf',t])
    im=cache[g]; W,H=im.size
    box=(int(d.get('x0',0)*W),int(d['y0']*H),int(d.get('x1',1)*W),int(d['y1']*H))
    cr=im.crop(box)
    if cr.width>1400: cr=cr.resize((1400,max(1,cr.height*1400//cr.width)),Image.LANCZOS)
    bf=io.BytesIO(); cr.save(bf,'PNG',optimize=True)
    rows.append(dict(id=f"{p}_d{k}",printed=p,img=base64.b64encode(bf.getvalue()).decode(),file=d.get('file',''),ctx=d.get('ctx',''),kind=d.get('kind',''),note=d.get('note','')))
json.dump([{k:v for k,v in r.items() if k!='img'} for r in rows],open(OUT.replace('.html','.json'),'w'),ensure_ascii=False,indent=0)
body=[];last=None
for r in rows:
    if r['printed']!=last: body.append(f'<h3 id="p{r["printed"]}">Printed p. {r["printed"]}</h3>'); last=r['printed']
    body.append(f'<div class="r e"><span class="n">{r["id"]}</span><img src="data:image/png;base64,{r["img"]}" alt="">'
      f'<input data-id="{r["id"]}" data-orig="" value="" autocomplete="off" placeholder="your reading">'
      f'<span class="f" title="{html.escape(r["ctx"])}">{html.escape(r["kind"])}: file has <b>{html.escape(r["file"])}</b> &nbsp; {html.escape(r["note"])} <i>({html.escape(r["ctx"])})</i></span></div>')
page=f'''<h2>{html.escape(TITLE)}</h2>
<p>Each row is something the worker could not settle from the print: a crop of the scan band, what the file has now (with <b>?</b> or <b>[?]</b>), and an empty box. Type what you read: the word (Devanagari or Kannada, whichever is easier), the accent as you see it, or the digits like <code>2-14-4</code>. Leave a box empty to keep the file as it is. Type <b>x</b> if the crop does not show the place named.</p>
<ul><li><b>Your edits save automatically</b> when you leave a box. Tell me when you are done.</li></ul>
{''.join(body)}
<h3>Flagged references with no crop found (0)</h3><ul></ul>'''
open(OUT,'w',encoding='utf8').write(page); print('rows',len(rows),os.path.getsize(OUT)//1024,'KB')
