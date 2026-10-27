"""Vol 2 review page: every located numeral group as a crop of the ~575 dpi scan, an editable box pre-filled with the
file's reading where one aligns (page order), else empty; 'file: …' beside it.
python3 build_review.py FIRST LAST OUT.html [TITLE]  (global PDF pages) -> OUT.html + OUT.json (rows without images)"""
import sys,os,re,io,json,base64,html,difflib,subprocess,tempfile
sys.path.insert(0,os.path.dirname(__file__))
from cfg import WORK,part_of
from pages import printed,label,page_sections,text_of
from PIL import Image
a,b,OUT=int(sys.argv[1]),int(sys.argv[2]),sys.argv[3]; TITLE=sys.argv[4] if len(sys.argv)>4 else f'Vol 2 numerals, PDF {a}-{b}'
SKIP={290,291}   # PDF 290-291 repeat printed pp. 276-277
TOK=json.load(open(WORK+'numerals.json'))
KD='೦೧೨೩೪೫೬೭೮೯'; K2A=str.maketrans(KD+'०१२३४५६७८९','0123456789'*2)
dig=lambda s:re.sub(r'\D','',s.translate(K2A))
SEG=r'(?:\d{1,4}|\[\?\])'
GRP=re.compile(r'(?<![\w.\-,])((?:\d{1,3}(?:,\d{3})+|\d{1,4})(?:\s*[-.–]\s*'+SEG+r'){0,4})(\s*\[\?\])?(?![\w])')
def file_groups(g):
    out=[]
    for (f,_,_,s,e) in page_sections(g):
        t=text_of(f)[s:e]; t=t[t.index('\n')+1:] if '\n' in t else t   # not the '### Page N' heading
        tt=t.translate(K2A)
        for m in GRP.finditer(tt):
            v=m.group(1).rstrip('.-–')
            if not v: continue
            out.append(dict(v=t[m.start(1):m.start(1)+len(v)],flag=bool(m.group(2)) or '[?]' in v,ctx=t[max(0,m.start()-50):m.end()+8].replace('\n',' ')))
    return out
def sim(x,y):
    dx,dy=dig(x),dig(y)
    if not dx or not dy: return 0
    r=difflib.SequenceMatcher(None,dx,dy).ratio()
    return r if abs(len(dx)-len(dy))<=2 else r*0.6
def align(cv,fg):
    """global alignment of crop guesses (Tesseract digits: an alignment hint only) with file groups"""
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
S600=576/300
rows=[]; done={}   # section -> index of the last file group matched on an earlier page of a multi-page section
for g in range(a,b+1):
    toks=TOK.get(str(g),[])
    if not toks or g in SKIP or printed(g) is None: continue
    sk=tuple((s[0],s[3]) for s in page_sections(g)); fg=file_groups(g); off=done.get(sk,-1)+1; fg=fg[off:]
    pairs=align([t['tess'] for t in toks],fg)
    if pairs: done[sk]=off+max(pairs.values())
    path,n=part_of(g); d=tempfile.mkdtemp(dir=WORK)
    subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','576','-gray',path,d+'/h'],check=True)
    pg=Image.open(d+'/'+os.listdir(d)[0]); subprocess.run(['rm','-rf',d])
    for i,t in enumerate(toks):
        core=re.sub(r'[^'+KD+'-]','',t['tess']); nd=sum(c in KD for c in core)
        # a bare single digit is most often a letter (ಳ read as ೪, ಂ as ೦): keep it only with ( ) . around it or a file match
        if nd==1 and not re.search(r'[().]',t['tess']) and not (i in pairs and sim(t['tess'],fg[pairs[i]]['v'])==1): continue
        x,y,w,h=t['box']; pad=int(h*1.6); lpad=int(h*2.6)
        cr=pg.crop((int((x-lpad)*S600),int((y-h*0.25)*S600),int((x+w+pad)*S600),int((y+h*1.25)*S600))).convert('L')
        cr=cr.resize((max(1,cr.width*3//5),max(1,cr.height*3//5)),Image.LANCZOS).point(lambda v:255 if v>150 else 0).convert('1')
        bf=io.BytesIO(); cr.save(bf,'PNG',optimize=True)
        fv=ctx=''
        if i in pairs: f=fg[pairs[i]]; fv=f['v']+(' [?]' if f['flag'] and '[?]' not in f['v'] else ''); ctx=f['ctx']
        prop='' if (not fv or '?' in fv) else fv
        rows.append(dict(id=f'{g}_{i}',pdf=g,img=base64.b64encode(bf.getvalue()).decode(),prop=prop,file=fv,ctx=ctx,
                         tess=t['tess'],box=t['box'],line=t['line']))
    print(g,len(toks),len(fg),len(pairs),flush=True)
json.dump([{k:v for k,v in r.items() if k!='img'} for r in rows],open(OUT.replace('.html','.json'),'w'),ensure_ascii=False,indent=0)
body=[];lastp=None
for r in rows:
    if r['pdf']!=lastp:
        path,n=part_of(r['pdf'])
        body.append(f'<h3 id="p{r["pdf"]}">PDF {r["pdf"]} (part {os.path.basename(path)[-5]}, p. {n}) · printed {label(r["pdf"])}</h3>'); lastp=r['pdf']
    cls='m' if r['prop'] else 'e'
    body.append(f'<div class="r {cls}"><span class="n">{r["id"]}</span><img src="data:image/png;base64,{r["img"]}" alt="">'
                f'<input data-id="{r["id"]}" data-orig="{html.escape(r["prop"])}" value="{html.escape(r["prop"])}" autocomplete="off" inputmode="text">'
                f'<span class="f" title="{html.escape(r["ctx"])}">file: {html.escape(r["file"]) or "—"}</span></div>')
nm=sum(1 for r in rows if r['prop']); ne=len(rows)-nm
page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(TITLE)}</title>
<style>
:root{{--bg:#fff;--fg:#111;--line:#e3e3e3;--box:#f7f7f7;--m:#eef6ee;--e:#fff6d6;--mut:#666}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#1b1b1b;--fg:#eee;--line:#3a3a3a;--box:#262626;--m:#1f2c21;--e:#3a3318;--mut:#aaa}}}}
:root[data-theme="dark"]{{--bg:#1b1b1b;--fg:#eee;--line:#3a3a3a;--box:#262626;--m:#1f2c21;--e:#3a3318;--mut:#aaa}}
body{{background:var(--bg);color:var(--fg);font:15px system-ui,sans-serif;margin:0 auto;max-width:900px;padding:16px}}
.bar{{position:sticky;top:0;background:var(--bg);padding:8px 0;border-bottom:1px solid var(--line);z-index:2}}
.r{{display:flex;align-items:center;gap:10px;padding:4px 6px;border-bottom:1px solid var(--line);flex-wrap:wrap}}
.r.m{{background:var(--m)}} .r.e{{background:var(--e)}} .r.ed{{outline:2px solid #d33}}
.n{{width:4.6em;color:var(--mut);font-size:12px}}
img{{background:#fff;max-width:100%;height:auto;border-radius:3px}}
input{{font-size:17px;padding:4px 6px;width:9em;background:var(--box);color:var(--fg);border:1px solid var(--line);border-radius:5px}}
.f{{color:var(--mut);font-size:13px;max-width:100%;overflow-wrap:anywhere}}
textarea{{width:100%;height:12em;font:14px monospace;background:var(--box);color:var(--fg)}}
button,select{{font-size:15px;padding:5px 10px}}
</style></head><body>
<h2>{html.escape(TITLE)}</h2>
<p>Each row: the numeral as printed (crop of the 600 dpi scan), a box, and what the English files say now.
<b style="background:var(--m)">green rows</b> ({nm}): the box holds the file's reading, matched by page order — check it against the crop.
<b style="background:var(--e)">yellow rows</b> ({ne}): no confident file reading (none matched, or the file has [?]) — type what the crop shows.</p>
<ul><li>Correct a box if it does not match the image.</li>
<li><b>Empty the box</b> if the crop is not a reference numeral.</li>
<li>Use <b>?</b> for a digit you cannot decide.</li>
<li>Edits are saved only in this browser. To send them: click in the text box at the bottom, press Cmd+A, Cmd+C, and paste into the chat. (The Copy button may not work in Safari; uploading this file back does not carry the edits.)</li></ul>
<div class="bar"><select id="flt"><option value="all">show all</option><option value="e">yellow only</option><option value="m">green only</option><option value="ed">my edits</option></select>
<button id="cp">Copy my edits</button> <span id="st"></span></div>
{''.join(body)}
<h3>My edits</h3><p>Only rows you changed are listed (an emptied box shows as <code>ID: </code>).</p>
<textarea id="out" readonly></textarea>
<script>
const ins=[...document.querySelectorAll('input[data-id]')],out=document.getElementById('out'),K='v2numerals:{html.escape(TITLE)}';
function upd(){{const e={{}};ins.forEach(i=>{{const ch=i.value.trim()!==i.dataset.orig;i.parentNode.classList.toggle('ed',ch);if(ch)e[i.dataset.id]=i.value.trim()}});
 out.value=Object.entries(e).map(([k,v])=>k+': '+v).join('\\n');try{{localStorage.setItem(K,JSON.stringify(e))}}catch(x){{}}}}
try{{const e=JSON.parse(localStorage.getItem(K)||'{{}}');ins.forEach(i=>{{if(e[i.dataset.id]!==undefined)i.value=e[i.dataset.id]}})}}catch(x){{}}
ins.forEach(i=>i.addEventListener('input',upd));upd();
document.getElementById('flt').onchange=ev=>{{const v=ev.target.value;document.querySelectorAll('.r').forEach(r=>{{
 r.style.display=(v=='all'||r.classList.contains(v))?'':'none'}})}};
document.getElementById('cp').onclick=async()=>{{out.select();try{{await navigator.clipboard.writeText(out.value);document.getElementById('st').textContent='Copied.'}}catch(e){{document.execCommand('copy');document.getElementById('st').textContent='Selected — press Cmd+C.'}}}};
</script></body></html>'''
open(OUT,'w').write(page); print('rows',len(rows),'prefilled',nm,'empty',ne,os.path.getsize(OUT)//1024,'KB')
