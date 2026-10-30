import re,sys,html as H
VERIFY='verify' in sys.argv[1]
src,out,lo,hi=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]
t=open(src).read()
blocks=re.findall(r'(<h3 id="p\d+">.*?</h3>|<div class="r [me]">.*?</div>)',t,re.S)
um=re.search(r'<h3>Flagged references with no crop found.*?</ul>',t,re.S).group(0)
rows=sum(1 for b in blocks if b.startswith('<div'))
green=sum(1 for b in blocks if b.startswith('<div class="r m"'))
NORMAL_TXT=f'''<p>Each row is a reference the file has with a <b>?</b> in it: the numeral as printed, a box, and what the file says now.
<b style="background:var(--grn);padding:0 4px">Green rows</b> ({green}): the box holds a machine reading that agrees with the digits the file already has; check it against the crop.
<b style="background:var(--yel);padding:0 4px">Yellow rows</b> ({rows-green}): the box is empty; type the digits you see, like <code>2-14-4</code>.</p>
<ul><li>Correct a box if it does not match the crop. Type <b>x</b> if the crop shows a different reference from "file:". Type <b>?</b> for one digit you cannot decide, e.g. <code>2-1?-4</code>.</li>
<li><b>Your edits save automatically</b> when you leave a box. Nothing to copy or send; tell me when you are done.</li></ul>'''
VERIFY_TXT=f'''<p>Each of the {rows} rows is a reference the worker read from the print and entered in the file: the numeral as printed, a box holding the worker's reading, and the words around it. <b>Change a box only if the reading is wrong</b>; leave it alone if it is right. If the crop shows a different reference, type <b>x</b>; type <b>?</b> for one digit you cannot decide.</p>
<ul><li><b>Your corrections save automatically</b> when you leave a box. Tell me when you are done.</li></ul>'''
page=f'''<title>Pariśiṣṭa {'Check' if VERIFY else 'Refs'} {lo}–{hi}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<style>
:root{{--bg:#fbfaf7;--fg:#1c1b19;--line:#e0ddd5;--box:#f2f0ea;--yel:#fff3cf;--grn:#e8f3e6;--mut:#6a665c;--acc:#2b5d8a;--ok:#2f7d3a}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#171715;--fg:#ecebe6;--line:#3a3935;--box:#252420;--yel:#3a3318;--grn:#1f2c21;--mut:#a7a498;--acc:#8fb8e0;--ok:#7fcf8b;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#171715;--fg:#ecebe6;--line:#3a3935;--box:#252420;--yel:#3a3318;--grn:#1f2c21;--mut:#a7a498;--acc:#8fb8e0;--ok:#7fcf8b;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font:15px/1.45 system-ui,-apple-system,sans-serif;margin:0;padding-block:16px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));max-width:920px;margin-inline:auto}}
h2{{margin:0 0 6px;font-size:20px}} h3{{font-size:15px;margin:18px 0 4px;color:var(--acc)}}
.bar{{position:sticky;top:env(safe-area-inset-top,0px);background:var(--bg);padding:8px 0;border-bottom:1px solid var(--line);z-index:2;display:flex;gap:12px;align-items:center;flex-wrap:wrap}}
.r{{display:flex;align-items:center;gap:10px;padding:6px;border-bottom:1px solid var(--line);flex-wrap:wrap}}
.r.e{{background:var(--yel)}} .r.m{{background:var(--grn)}} .r.ed{{outline:2px solid var(--acc)}}
.n{{width:4.8em;color:var(--mut);font-size:12px}}
img{{background:#fff;max-width:100%;height:auto;border-radius:3px}}
input{{font-size:17px;padding:5px 7px;width:9.5em;background:var(--box);color:var(--fg);border:1px solid var(--line);border-radius:5px}}
.f{{color:var(--mut);font-size:13px;min-width:0;overflow-wrap:anywhere}}
#st{{color:var(--ok);font-size:14px}} textarea{{width:100%;height:9em;font:13px ui-monospace,monospace;background:var(--box);color:var(--fg);border:1px solid var(--line)}}
</style>
<h2>{'Check of the worker readings' if VERIFY else 'Pariśiṣṭa references'}, printed pp. {lo}–{hi}</h2>
{VERIFY_TXT if VERIFY else NORMAL_TXT}
<div class="bar"><span id="st">Connecting…</span><span id="cnt"></span></div>
{''.join(blocks)}
{um}
<h3>My edits (backup: select and copy from here if saving is unavailable)</h3><textarea id="out"></textarea>
<script>
const ins=[...document.querySelectorAll('input[data-id]')],by={{}};ins.forEach(i=>by[i.dataset.id]=i);
const out=document.getElementById('out'),st=document.getElementById('st'),cnt=document.getElementById('cnt');
let db=null;
function mark(i){{i.parentNode.classList.toggle('ed',i.value.trim()!==i.dataset.orig)}}
function tally(){{const e=ins.filter(i=>i.value.trim()!==i.dataset.orig);cnt.textContent=e.length+' changed';out.value=e.map(i=>i.dataset.id+': '+i.value.trim()).join('\\n')}}
const chain=new Map();
function save(i){{
 if(!db)return;const id=i.dataset.id,v=i.value.trim();
 const p=(chain.get(id)||Promise.resolve()).then(async()=>{{
  try{{const d=db.doc('edits/'+id);
   if(v===i.dataset.orig){{await d.delete()}}else{{await d.set({{v:v,at:Date.now()}})}}
   st.textContent='Saved '+new Date().toLocaleTimeString()}}catch(e){{st.textContent='Not saved ('+(e&&e.code||'error')+')'}}
 }});chain.set(id,p);
}}
ins.forEach(i=>{{i.addEventListener('input',()=>{{mark(i);tally()}});i.addEventListener('change',()=>save(i))}});
tally();
(async()=>{{
 try{{db=await claude.use('db')}}catch(e){{db=null}}
 if(!db){{st.textContent='Saving is unavailable here: copy from the box at the bottom.';return}}
 st.textContent='Ready';
 db.collection('edits').onSnapshot(s=>{{
  s.docs.forEach(d=>{{const i=by[d.id],x=d.data();if(i&&x&&document.activeElement!==i&&i.value.trim()!==x.v){{i.value=x.v;mark(i)}}}});
  tally();
 }},e=>{{st.textContent='Live updates stopped ('+(e&&e.code||'error')+')'}});
}})();
</script>'''
open(out,'w').write(page); print(len(page)//1024,'KB rows',rows,'green',green)
