"""Build review HTML pages from review/doubts_v13.json: crop of scan + note + answer box. python3 make_review_html.py [batch=60]"""
import sys,os,json,base64,io,html
sys.path.insert(0,os.path.dirname(__file__))
from view import render
R=os.path.join(os.path.dirname(__file__),'..','review'); OUT=os.path.join(R,'html'); os.makedirs(OUT,exist_ok=True)
D=json.load(open(os.path.join(R,'doubts_v13.json'),encoding='utf-8')); B=int(sys.argv[1]) if len(sys.argv)>1 else 60
for i,d in enumerate(D): d['id']=i+1
D.sort(key=lambda d:(d['pdf'],d['crop'][0])); 
imgs={}
def crop(d):
    g=d['pdf']
    if g not in imgs: imgs.clear(); imgs[g]=render(g,110)
    im=imgs[g]; W,H=im.size; y0,y1,x0,x1=d['crop']
    c=im.crop((int(W*x0),max(0,int(H*(y0-.005))),int(W*x1),int(H*(y1+.005))))
    b=io.BytesIO(); c.convert('L').save(b,'JPEG',quality=60); return base64.b64encode(b.getvalue()).decode()
CSS="""<style>:root{--bg:#fff;--fg:#111;--line:#ddd;--box:#f6f6f6;--mut:#666}@media (prefers-color-scheme:dark){:root{--bg:#1b1b1b;--fg:#eee;--line:#3a3a3a;--box:#262626;--mut:#aaa}}
body{background:var(--bg);color:var(--fg);font:15px system-ui,sans-serif;margin:0 auto;max-width:900px;padding:12px 16px}
.bar{position:sticky;top:0;background:var(--bg);padding:8px 0;border-bottom:1px solid var(--line);z-index:2}
.c{border-bottom:1px solid var(--line);padding:10px 0}.h{color:var(--mut);font-size:13px}img{max-width:100%;background:#fff;border-radius:3px;margin:6px 0}
textarea{width:100%;height:3.2em;font:15px system-ui;background:var(--box);color:var(--fg);border:1px solid var(--line);border-radius:5px}button{font-size:15px;padding:5px 10px}</style>"""
n=0
for k in range(0,len(D),B):
    ch=D[k:k+B]; a,b=ch[0]['printed'],ch[-1]['printed']; name=f'Vol13_doubts_p{a}-{b}'
    rows=[]
    for d in ch:
        rows.append(f'<div class="c" id="d{d["id"]}"><div class="h"><b>#{d["id"]}</b> · printed p. {d["printed"]} (PDF {d["pdf"]}) · {html.escape(d["note"])}</div><img loading="lazy" src="data:image/jpeg;base64,{crop(d)}"><textarea data-id="{d["id"]}" placeholder="Correct reading / answer (leave blank if the text is right)">{html.escape(d.get("answer",""))}</textarea></div>')
    js="""<script>const K='v13_'+document.title;const T=[...document.querySelectorAll('textarea')];
try{const s=JSON.parse(localStorage[K]||'{}');T.forEach(t=>{if(s[t.dataset.id])t.value=s[t.dataset.id]})}catch(e){}
T.forEach(t=>t.oninput=()=>{try{const s={};T.forEach(x=>{if(x.value.trim())s[x.dataset.id]=x.value});localStorage[K]=JSON.stringify(s)}catch(e){}});
function dl(){const s={};T.forEach(x=>{if(x.value.trim())s[x.dataset.id]=x.value});const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([JSON.stringify(s,null,1)],{type:'application/json'}));a.download=document.title+'_answers.json';a.click()}</script>"""
    open(f'{OUT}/{name}.html','w',encoding='utf-8').write(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{name}</title>{CSS}</head><body><div class="bar"><b>{name}</b> — {len(ch)} items (#{ch[0]["id"]}…). Type answers only where the text is wrong or you can read a doubtful numeral. <button onclick="dl()">Download answers (JSON)</button></div>{"".join(rows)}{js}</body></html>')
    n+=1; print(name,flush=True)
