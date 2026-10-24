"""One review page for every located numeral group: crop, proposed reading (editable), current file reading.
python3 review_html.py ITEMS.csv TESS.csv SHAPE.csv OUT.html [TITLE]   (items/tess/shape may be comma-joined lists)"""
import sys,os,csv,re,io,glob,base64,subprocess,difflib,json,html
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..','verify11'))
from cfg import WORK,SCAN,EN
from PIL import Image
def load(arg): return [r for f in arg.split(',') for r in csv.DictReader(open(f))]
items=load(sys.argv[1]); T={r['id']:r for r in load(sys.argv[2])}; S={r['id']:r for r in load(sys.argv[3])}
OUT=sys.argv[4]; TITLE=sys.argv[5] if len(sys.argv)>5 else 'Vol 11 numerals'
dig=lambda s:re.sub(r'\D','',s)
DEV=str.maketrans('०१२३४५६७८९','0123456789')
t=open(EN,encoding='utf8').read(); pages={}
for s in re.split(r'\n(?=### Printed p\. )',t):
    m=re.match(r'### Printed p\. (\S+)\s+\(.*?PDF (\d+)',s)
    if m: pages[m.group(2)]=pages.get(m.group(2),'')+s
NUM=re.compile(r'(?<![\w.])(\d{1,4}(?:\s*-\s*(?:\d{1,4}\??|\d*\[\?\]|\?+)){0,3})(\s*\[\?\])?')
def file_nums(pdf):
    out=[]
    for m in NUM.finditer(pages.get(pdf,'').translate(DEV)):
        if re.search(r'[A-Za-zāīū]\s*$',pages[pdf][max(0,m.start()-1):m.start()]): pass
        v=re.sub(r'\s','',m.group(1)); out.append((v+(' [?]' if m.group(2) else ''),pages[pdf][max(0,m.start()-45):m.end()+5].replace('\n',' ')))
    return out
TOK=json.load(open(WORK+'numerals.json'))
KD='೦೧೨೩೪೫೬೭೮೯'
def is_numeral(iid):
    p,i=iid.split('_'); t=TOK[p][int(i)]['tess']
    core=re.sub(r'[()\[\].,;:।॥|\'"`]','',t)
    nd=sum(ch in KD for ch in core)
    return bool(re.search(f'[{KD}]-[{KD}]',core)) or (nd>=1 and nd>=0.75*len(core))
def propose(b,c):
    if b.endswith('2') and dig(b)[:-1]==dig(c) and dig(c): b=b[:-1]      # ')' read as a trailing 2
    if dig(b) and dig(b)==dig(c):
        return (b if b.count('-')>=c.count('-') else c),'agree'
    return (b or c),'split'
rows=[];cur=None;byp={}
for it in items:
    byp.setdefault(it['pdf'],[]).append(it)
for pdf in sorted(byp,key=int):
    fn=file_nums(pdf); used=set()
    for f in glob.glob(WORK+'h-*.pgm'): os.remove(f)
    subprocess.run(['pdftoppm','-f',pdf,'-l',pdf,'-r','600','-gray',SCAN,WORK+'h'],check=True)
    pg=Image.open(glob.glob(WORK+'h-*.pgm')[0])
    for it in byp[pdf]:
        b=T.get(it['id'],{}).get('tess',''); c=S.get(it['id'],{}).get('shape','')
        if not is_numeral(it['id']): continue
        prop,st=propose(b,c)
        if not dig(prop) and not os.environ.get('NOMACH'): continue
        if os.environ.get('NOMACH'): prop=c
        best=(None,0)
        for k,(v,ctx) in enumerate(fn):
            if k in used: continue
            r=difflib.SequenceMatcher(None,dig(v),dig(prop)).ratio()
            if r>best[1]: best=(k,r)
        fv=fctx=''
        if best[0] is not None and best[1]>=0.6:
            used.add(best[0]); fv,fctx=fn[best[0]]
            if '?' not in fv and st=='split' and dig(fv) in (dig(b),dig(c)): prop=fv; st='file'   # one machine + file agree
            if dig(fv)==dig(prop) and '?' not in fv: prop=fv.replace(' [?]','')   # keep the file's separators
        if os.environ.get('NOMACH'):              # no machine pair: prefill the file reading where one matches, else the shape reading
            prop=fv.replace(' [?]','') if fv and '?' not in fv else c; cls='n'
        else: cls='l' if st=='file' else 'g' if st=='agree' and fv and dig(fv)==dig(prop) and '?' not in fv else ('b' if st=='agree' else 'y')
        x0,y0,x1,y1=map(int,it['box600'].split()); cr=pg.crop((x0,y0,x1,y1)).convert('L')
        cr=cr.resize((max(1,cr.width*3//5),max(1,cr.height*3//5)),Image.LANCZOS).point(lambda v:255 if v>150 else 0).convert('1')
        bf=io.BytesIO(); cr.save(bf,'PNG',optimize=True)
        rows.append(dict(id=it['id'],pdf=pdf,img=base64.b64encode(bf.getvalue()).decode(),prop=prop,file=fv,ctx=fctx,cls=cls,b=b,c=c))
    print(pdf,len(byp[pdf]),flush=True)
json.dump([{k:v for k,v in r.items() if k!='img'} for r in rows],open(OUT.replace('.html','.json'),'w'),ensure_ascii=False,indent=0)
body=[];lastp=None
for r in rows:
    if r['pdf']!=lastp:
        body.append(f'<h3 id="p{r["pdf"]}">PDF {r["pdf"]} · printed {int(r["pdf"])-18}</h3>'); lastp=r['pdf']
    body.append(f'<div class="r {r["cls"]}"><span class="n">{r["id"]}</span><img src="data:image/png;base64,{r["img"]}" alt="">'
                f'<input data-id="{r["id"]}" data-orig="{html.escape(r["prop"])}" value="{html.escape(r["prop"])}" autocomplete="off">'
                f'<span class="f" title="{html.escape(r["ctx"])}">file: {html.escape(r["file"]) or "—"}</span></div>')
n={k:sum(r['cls']==k for r in rows) for k in 'glby'}
page=f'''<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{TITLE}</title>
<style>
:root{{--bg:#fff;--fg:#111;--line:#e3e3e3;--box:#f7f7f7;--g:#e8f6ea;--l:#f1faf0;--b:#e6effc;--y:#fff4cc;--mut:#666}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#1b1b1b;--fg:#eee;--line:#3a3a3a;--box:#262626;--g:#1e3323;--l:#232c24;--b:#1d2a40;--y:#3d3517;--mut:#aaa}}}}
:root[data-theme="dark"]{{--bg:#1b1b1b;--fg:#eee;--line:#3a3a3a;--box:#262626;--g:#1e3323;--l:#232c24;--b:#1d2a40;--y:#3d3517;--mut:#aaa}}
body{{background:var(--bg);color:var(--fg);font:15px system-ui,sans-serif;margin:0 auto;max-width:900px;padding:16px}}
.bar{{position:sticky;top:0;background:var(--bg);padding:8px 0;border-bottom:1px solid var(--line);z-index:2}}
.r{{display:flex;align-items:center;gap:10px;padding:4px 6px;border-bottom:1px solid var(--line);flex-wrap:wrap}}
.r.g{{background:var(--g)}} .r.l{{background:var(--l)}} .r.b{{background:var(--b)}} .r.y{{background:var(--y)}} .r.ed{{outline:2px solid #d33}}
.n{{width:4.2em;color:var(--mut);font-size:12px}}
img{{background:#fff;max-width:100%;height:auto;border-radius:3px}}
input{{font-size:17px;padding:4px 6px;width:9em;background:var(--box);color:var(--fg);border:1px solid var(--line);border-radius:5px}}
.f{{color:var(--mut);font-size:13px}}
textarea{{width:100%;height:12em;font:14px monospace;background:var(--box);color:var(--fg)}}
button,select{{font-size:15px;padding:5px 10px}}
</style></head><body>
<h2>{TITLE}</h2>
<p>{'<b>No confidence colours on this page:</b> each box is pre-filled with the current file reading where one was matched, otherwise with the shape reading — please check every row. ' if os.environ.get('NOMACH') else ''}Each row: the numeral as printed, the proposed reading (edit it if wrong), and what the files say now.
<b style="background:var(--g)">green</b> both machine readers agree and match the file ({n['g']});
<b style="background:var(--l)">light green</b> one machine reader agrees with the file ({n['l']});
<b style="background:var(--b)">blue</b> both machine readers agree, the file differs or has [?] ({n['b']});
<b style="background:var(--y)">yellow</b> the machine readers disagree — please check ({n['y']}).
Use <b>?</b> for a digit you cannot decide, <b>x</b> if the crop is not a reference numeral. Edits are kept in this browser.</p>
<div class="bar"><select id="flt"><option value="all">show all</option><option value="by">blue + yellow only</option><option value="y">yellow only</option><option value="ed">my edits</option></select>
<button id="cp">Copy my edits</button> <span id="st"></span></div>
{''.join(body)}
<h3>My edits</h3><p>Copy this and paste it into the chat (only rows you changed are listed).</p>
<textarea id="out" readonly></textarea>
<script>
const ins=[...document.querySelectorAll('input[data-id]')],out=document.getElementById('out'),K='numerals:{TITLE}';
function upd(){{const e={{}};ins.forEach(i=>{{const ch=i.value.trim()!==i.dataset.orig;i.parentNode.classList.toggle('ed',ch);if(ch)e[i.dataset.id]=i.value.trim()}});
 out.value=Object.entries(e).map(([k,v])=>k+': '+v).join('\\n');try{{localStorage.setItem(K,JSON.stringify(e))}}catch(x){{}}}}
try{{const e=JSON.parse(localStorage.getItem(K)||'{{}}');ins.forEach(i=>{{if(e[i.dataset.id]!==undefined)i.value=e[i.dataset.id]}})}}catch(x){{}}
ins.forEach(i=>i.addEventListener('input',upd));upd();
document.getElementById('flt').onchange=ev=>{{const v=ev.target.value;document.querySelectorAll('.r').forEach(r=>{{
 r.style.display=(v=='all'||(v=='by'&&(r.classList.contains('b')||r.classList.contains('y')))||(v=='y'&&r.classList.contains('y'))||(v=='ed'&&r.classList.contains('ed')))?'':'none'}})}};
document.getElementById('cp').onclick=async()=>{{out.select();try{{await navigator.clipboard.writeText(out.value);document.getElementById('st').textContent='Copied.'}}catch(e){{document.execCommand('copy');document.getElementById('st').textContent='Selected — press Ctrl/Cmd+C.'}}}};
</script></body></html>'''
open(OUT,'w').write(page); print('rows',len(rows),n,os.path.getsize(OUT)//1024,'KB')
