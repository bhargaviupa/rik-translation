"""Vol 5 Pariśiṣṭa review page (adapted from vol1/tools/build_review.py): for each printed page, the numeral groups the
file marks with ? / [?] are shown as crops of the better scan (576 dpi, binarised), with an editable box (pre-filled only if
the file reading has no ?), and 'file: …' beside it. Tesseract (kan) is used only to LOCATE numeral groups; its digits are
an alignment hint, never the reading. Unmatched flagged file groups are listed at the end of the page and in the JSON.
python3 build_review_v5.py FIRST_PRINTED LAST_PRINTED OUT.html [TITLE]
"""
import sys,os,re,io,json,base64,html,difflib,subprocess,tempfile,csv
sys.path.insert(0,os.path.dirname(__file__))
from cfg import WORK,EN,part_of
from PIL import Image
a,b,OUT=int(sys.argv[1]),int(sys.argv[2]),sys.argv[3]
TITLE=sys.argv[4] if len(sys.argv)>4 else f'Vol 5 Pariśiṣṭa numerals, printed pp. {a}-{b}'
KD='೦೧೨೩೪೫೬೭೮೯'; K2A=str.maketrans(KD+'०१२३४५६७८९','0123456789'*2)
dig=lambda s:re.sub(r'\D','',s.translate(K2A))
T=open(EN,encoding='utf8').read()
SECT={}   # printed page -> (pdf, text)
for s in re.split(r'\n(?=### Printed p\. )',T):
    m=re.match(r'### Printed p\. (\d+)\s+\(PDF (\d+)\)',s)
    if m: SECT[int(m.group(1))]=(int(m.group(2)),s)
SEG=r'(?:\d{1,4}|\[\?\]|\?)'
GRP=re.compile(r'(?<![\w.\-,])((?:\d{1,3}(?:,\d{3})+|\d{1,4}|\?)(?:\s*[-.–]\s*'+SEG+r'){1,4})(\s*\[\?\])?(?![\w])')
def file_groups(text):
    out=[]; t=text[text.index('\n')+1:] if '\n' in text else text
    for m in GRP.finditer(t):
        v=m.group(1)
        out.append(dict(v=v,flag=('?' in v) or bool(m.group(2)),ctx=t[max(0,m.start()-55):m.end()+10].replace('\n',' ')))
    return out
def sim(x,y):
    """x = Tesseract digits (hint), y = file group, possibly with ? wildcards"""
    sx=[q for q in re.split(r'[-.–]',re.sub(r'[()\s]','',x.translate(K2A))) if q!='']
    sy=[q for q in re.split(r'[-.–]',re.sub(r'\s','',y)) if q!='']
    if sx and sy and len(sx)==len(sy):
        tot=0
        for u,v in zip(sx,sy):
            if u==v: tot+=1
            elif v=='?' or v=='[?]': tot+=0.75
            elif '?' in v: tot+=0.5+0.5*difflib.SequenceMatcher(None,re.sub(r'\D','',u),re.sub(r'\D','',v)).ratio()*0.6
            else: tot+=difflib.SequenceMatcher(None,re.sub(r'\D','',u),re.sub(r'\D','',v)).ratio()
        return tot/len(sx)
    dx,dy=dig(x),dig(y)
    if not dx or not dy: return 0.3 if (dx or dy) else 0
    r=difflib.SequenceMatcher(None,dx,dy).ratio()
    return r if abs(len(dx)-len(dy))<=2 else r*0.6
def align(cv,fg):
    n,m=len(cv),len(fg); G=-0.25
    S=[[0.0]*(m+1) for _ in range(n+1)]; P=[[None]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1): S[i][0]=S[i-1][0]+G; P[i][0]='u'
    for j in range(1,m+1): S[0][j]=S[0][j-1]+G; P[0][j]='l'
    for i in range(1,n+1):
        for j in range(1,m+1):
            d=S[i-1][j-1]+(sim(cv[i-1],fg[j-1]['v'])-0.5)*2
            S[i][j],P[i][j]=max((d,'d'),(S[i-1][j]+G,'u'),(S[i][j-1]+G,'l'))
    i,j=n,m; pairs={}
    while i>0 or j>0:
        p=P[i][j]
        if p=='d':
            if sim(cv[i-1],fg[j-1]['v'])>=0.5: pairs[i-1]=j-1
            i,j=i-1,j-1
        elif p=='u': i-=1
        else: j-=1
    return pairs
def locate(g):
    import csv as _c
    path,n=part_of(g); os.makedirs(WORK+'t',exist_ok=True); d=tempfile.mkdtemp(dir=WORK+'t')
    subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','300','-gray',path,d+'/l'],check=True)
    img=os.path.join(d,os.listdir(d)[0])
    tsv=subprocess.run(['tesseract',img,'-','-l','kan','--psm','4','tsv'],capture_output=True,text=True).stdout
    subprocess.run(['rm','-rf',d]); toks=[]
    for r in _c.DictReader(io.StringIO(tsv),delimiter='\t',quoting=_c.QUOTE_NONE):
        t=r['text'] or ''
        if re.search(f'[{KD}]',t):
            toks.append(dict(box=[int(r['left']),int(r['top']),int(r['width']),int(r['height'])],tess=t,conf=float(r['conf']),line=f"{r['block_num']}.{r['par_num']}.{r['line_num']}"))
    return toks
def prefill(tess,fv):
    """Tesseract's digits, offered only when every file segment that is a number agrees and the segment counts are equal"""
    st=[q for q in re.split(r'[-.–]',re.sub(r'[()\s,]','',tess.translate(K2A))) if q!='']
    sf=[q for q in re.split(r'[-.–]',re.sub(r'\s','',fv)) if q!='']
    if not st or len(st)!=len(sf): return ''
    out=[]
    for u,v in zip(st,sf):
        if not u.isdigit() or len(u)>4: return ''
        if v.isdigit() and v!=u: return ''
        if '?' in v and v!='?' and not (len(v)==len(u)): return ''
        out.append(u)
    return '-'.join(out)
S600=576/300
rows=[]; unmatched=[]
for p in range(a,b+1):
    if p not in SECT: continue
    g,text=SECT[p]; fg=file_groups(text)
    if not any(f['flag'] for f in fg): continue
    toks=locate(g); pairs=align([t['tess'] for t in toks],fg)
    inv={j:i for i,j in pairs.items()}
    path,n=part_of(g); d=tempfile.mkdtemp(dir=WORK)
    subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','576','-gray',path,d+'/h'],check=True)
    pg=Image.open(d+'/'+os.listdir(d)[0]); subprocess.run(['rm','-rf',d])
    nflag=0
    # gap fill: between two matched references, if the number of unmatched file groups equals the number of unmatched tokens, pair them in order
    order=sorted(inv.items()); tok_used=set(inv.values()); filled=set()
    segs=[(-1,-1)]+[(jj,ii) for jj,ii in order]+[(len(fg),len(toks))]
    for (ja,ia),(jb,ib) in zip(segs,segs[1:]):
        gf=[x for x in range(ja+1,jb) if x not in inv]; gt=[k for k in range(ia+1,ib) if k not in tok_used]
        if gf and len(gf)==len(gt):
            for x,k in zip(gf,gt): inv[x]=k; filled.add(x)
    mj=sorted(inv)
    for j,f in enumerate(fg):
        if not f['flag']: continue
        nflag+=1
        region=False
        if j not in inv:
            prv=[a for a in mj if a<j]; nxt=[a for a in mj if a>j]
            if os.environ.get('V5REGION')!='1' or not (prv and nxt):
                unmatched.append(dict(printed=p,pdf=g,j=j,file=f['v'],ctx=f['ctx'])); continue
            b1=toks[inv[prv[-1]]]['box']; b2=toks[inv[nxt[0]]]['box']; h=max(b1[3],b2[3]); region=True
            ya=int(min(b1[1],b2[1])-h*0.25); yb=int(max(b1[1],b2[1])+h*1.25)
            if abs(b2[1]-b1[1])<h*1.5:
                boxes=[(b1[0]+b1[2],ya,b2[0],yb)]
            else:
                boxes=[(b1[0]+b1[2],int(b1[1]-h*0.25),2480,int(b1[1]+h*1.25)),(0,int(b2[1]-h*0.25),b2[0],int(b2[1]+h*1.25))]
            parts=[pg.crop((max(0,int(x0*S600)),max(0,int(y0*S600)),max(1,int(x1*S600)),max(1,int(y1*S600)))).convert('L') for x0,y0,x1,y1 in boxes if x1>x0]
            if not parts: unmatched.append(dict(printed=p,pdf=g,j=j,file=f['v'],ctx=f['ctx'])); continue
            W=max(c.width for c in parts); H=sum(c.height+6 for c in parts); cr=Image.new('L',(W,H),255); yy=0
            for c in parts: cr.paste(c,(0,yy)); yy+=c.height+6
            t=dict(tess='',box=[0,0,0,0])
        else:
            i=inv[j]; t=toks[i]; x,y,w,h=t['box']; need=int(h*(0.85*len(re.sub(r'\s','',f['v']))+1.2)); pad=max(int(h*1.6),need-w); lpad=int(h*2.6)
            cr=pg.crop((max(0,int((x-lpad)*S600)),max(0,int((y-h*0.25)*S600)),int((x+w+pad)*S600),int((y+h*1.25)*S600))).convert('L')
        cr=cr.resize((max(1,cr.width*3//5),max(1,cr.height*3//5)),Image.LANCZOS).point(lambda v:255 if v>150 else 0).convert('1')
        bf=io.BytesIO(); cr.save(bf,'PNG',optimize=True)
        rows.append(dict(id=f'{p}_{j}',printed=p,pdf=g,img=base64.b64encode(bf.getvalue()).decode(),file=f['v'],ctx=f['ctx'],tess=t['tess'],prop=('' if region else prefill(t['tess'],f['v'])),box=t['box'],region=region,filled=(j in filled)))
    print(p,'located',len(toks),'file groups',len(fg),'flagged',nflag,'rows so far',len(rows),'unmatched so far',len(unmatched),flush=True)
json.dump(dict(rows=[{k:v for k,v in r.items() if k!='img'} for r in rows],unmatched=unmatched),open(OUT.replace('.html','.json'),'w'),ensure_ascii=False,indent=0)
body=[];lastp=None
for r in rows:
    if r['printed']!=lastp:
        body.append(f'<h3 id="p{r["printed"]}">Printed p. {r["printed"]} (PDF {r["pdf"]})</h3>'); lastp=r['printed']
    cls='m' if r['prop'] else 'e'
    body.append(f'<div class="r {cls}"><span class="n">{r["id"]}</span><img src="data:image/png;base64,{r["img"]}" alt="">'
                f'<input data-id="{r["id"]}" data-orig="{html.escape(r["prop"])}" value="{html.escape(r["prop"])}" autocomplete="off" inputmode="text" placeholder="digits">'
                f'<span class="f" title="{html.escape(r["ctx"])}">file: {html.escape(r["file"])}{" &nbsp; <b>(the strip between the neighbouring references: the reference is inside it)</b>" if r.get("region") else ""} &nbsp; <small>{html.escape(r["ctx"][:70])}</small></span></div>')
um=''.join(f'<li>p. {u["printed"]}: {html.escape(u["file"])} — {html.escape(u["ctx"])}</li>' for u in unmatched)
page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(TITLE)}</title>
<style>
:root{{--bg:#fff;--fg:#111;--line:#e3e3e3;--box:#f7f7f7;--e:#fff6d6;--m:#eef6ee;--mut:#666}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#1b1b1b;--fg:#eee;--line:#3a3a3a;--box:#262626;--e:#3a3318;--m:#1f2c21;--mut:#aaa}}}}
body{{background:var(--bg);color:var(--fg);font:15px system-ui,sans-serif;margin:0 auto;max-width:900px;padding:16px}}
.bar{{position:sticky;top:0;background:var(--bg);padding:8px 0;border-bottom:1px solid var(--line);z-index:2}}
.r{{display:flex;align-items:center;gap:10px;padding:4px 6px;border-bottom:1px solid var(--line);flex-wrap:wrap}}
.r.e{{background:var(--e)}} .r.m{{background:var(--m)}} .r.ed{{outline:2px solid #d33}}
.n{{width:4.6em;color:var(--mut);font-size:12px}}
img{{background:#fff;max-width:100%;height:auto;border-radius:3px}}
input{{font-size:17px;padding:4px 6px;width:9em;background:var(--box);color:var(--fg);border:1px solid var(--line);border-radius:5px}}
.f{{color:var(--mut);font-size:13px;max-width:100%;overflow-wrap:anywhere}}
textarea{{width:100%;height:12em;font:14px monospace;background:var(--box);color:var(--fg)}}
button{{font-size:15px;padding:5px 10px}}
</style></head><body>
<h2>{html.escape(TITLE)}</h2>
<p>Each row is a reference the file has with a <b>?</b> in it: the numeral as printed (crop of the scan), a box, and what the file says now.
<b style="background:var(--m)">Green rows</b> ({sum(1 for r in rows if r['prop'])}): the box holds a machine reading that agrees with the digits the file already has; check it against the crop.
<b style="background:var(--e)">Yellow rows</b> ({sum(1 for r in rows if not r['prop'])}): the box is empty; type the digits you see, like <code>2-14-4</code>.</p>
<ul><li>Correct a box if it does not match the crop. If the crop shows a <b>different reference</b> from the one named in "file:" (wrong crop), type <b>x</b> in the box. Type <b>?</b> for one digit you cannot decide, e.g. <code>2-1?-4</code>.</li>
<li>Edits are saved only in this browser. To send them: click in the box at the bottom, Cmd+A, Cmd+C, paste into the chat.</li></ul>
<div class="bar"><span id="st"></span> <button id="cp">Copy my edits</button> {len(rows)} rows</div>
{''.join(body)}
<h3>Flagged references with no crop found ({len(unmatched)})</h3><ul>{um}</ul>
<h3>My edits</h3><textarea id="out" readonly></textarea>
<script>
const ins=[...document.querySelectorAll('input[data-id]')],out=document.getElementById('out'),K='v5pari:{html.escape(TITLE)}';
function upd(){{const e={{}};ins.forEach(i=>{{const ch=i.value.trim()!==i.dataset.orig;i.parentNode.classList.toggle('ed',ch);if(ch)e[i.dataset.id]=i.value.trim()}});
 out.value=Object.entries(e).map(([k,v])=>k+': '+v).join('\\n');document.getElementById('st').textContent=Object.keys(e).length+' filled';try{{localStorage.setItem(K,JSON.stringify(e))}}catch(x){{}}}}
try{{const e=JSON.parse(localStorage.getItem(K)||'{{}}');ins.forEach(i=>{{if(e[i.dataset.id]!==undefined)i.value=e[i.dataset.id]}})}}catch(x){{}}
ins.forEach(i=>i.addEventListener('input',upd));upd();
document.getElementById('cp').onclick=async()=>{{out.select();try{{await navigator.clipboard.writeText(out.value)}}catch(e){{document.execCommand('copy')}}}};
</script></body></html>'''
open(OUT,'w').write(page); print('rows',len(rows),'unmatched',len(unmatched),os.path.getsize(OUT)//1024,'KB')
