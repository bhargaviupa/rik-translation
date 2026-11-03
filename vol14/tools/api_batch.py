"""Translate the next N pages of Vol 14 through the Anthropic API (no tool loop).
python3 vol14/tools/api_batch.py [--pages 3] [--model claude-sonnet-5-5] [--budget 90] [--dry] [--no-commit] [--loops K]
Key: env RIK_API_KEY. Position is taken from the trailing progress note ('Done through printed p. N (PDF M)').
Per batch: render strips (page.py), numeral rows (numerals_for.py), call the API (system prompt cached), write chunk to /tmp,
add_iast.py, append_en.py, log doubts to vol14/review/api_doubts.tsv, cost to vol14/parts/api_costs.jsonl, git commit.
Stops on any error, on a missing CHUNK, if cumulative cost would exceed --budget (USD), or if the chunk lacks an IAST line for a Devanagari block."""
import os,sys,re,json,subprocess,base64,time,argparse
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..')); V=os.path.join(ROOT,'vol14')
EN=os.path.join(ROOT,'Rigveda_Samhita_Vol14_English_Translation.md')
COST=os.path.join(V,'parts','api_costs.jsonl'); DOUBTS=os.path.join(V,'review','api_doubts.tsv')
PRICE=dict(inp=3.0,out=15.0)   # USD per million tokens; ASSUMED Sonnet-class list price, adjust with --price-in/--price-out
def sh(c,**k): return subprocess.run(c,shell=True,capture_output=True,text=True,cwd=ROOT,**k)
def printed(g): return g-18-(1 if g>=224 else 0)-(1 if g>=336 else 0)
def position():
    s=open(EN,encoding='utf8').read(); i=s.rfind('**Progress note:**'); note=s[i:]
    m=re.search(r'through printed p\. (\d+) \(PDF (\d+)\)',note); assert m,'no position in note'
    return int(m.group(2)),note,s
def spent():
    return sum(json.loads(l)['usd'] for l in open(COST)) if os.path.exists(COST) else 0.0
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--pages',type=int,default=3); ap.add_argument('--model',default='claude-sonnet-5-5')
    ap.add_argument('--budget',type=float,default=90); ap.add_argument('--dry',action='store_true'); ap.add_argument('--no-commit',action='store_true')
    ap.add_argument('--loops',type=int,default=1); ap.add_argument('--price-in',type=float,default=PRICE['inp']); ap.add_argument('--price-out',type=float,default=PRICE['out'])
    ap.add_argument('--max-tokens',type=int,default=30000); a=ap.parse_args()
    import anthropic
    cl=anthropic.Anthropic(api_key=os.environ['RIK_API_KEY'])
    sysprompt=''.join(open(os.path.join(ROOT,f)).read()+'\n\n=========\n\n' for f in ['CLAUDE.md','vol14/vol14_runbook.md'])+open(os.path.join(V,'API_PROMPT.md')).read()
    for _ in range(a.loops):
        done,note,s=position(); pages=[done+1+k for k in range(a.pages)]
        if any(p in (223,335) for p in pages): print('duplicate page in range; handle by hand',pages); return 2
        if spent()>=a.budget: print('budget reached',spent()); return 3
        user=[]; 
        out=sh(f'python3 vol14/tools/numerals_for.py {" ".join(map(str,pages))}').stdout
        for p in pages:
            r=sh(f'python3 vol14/tools/page.py {p} /tmp/api_pg_{p}').stdout.split('\n')
            fs=[l.split()[0] for l in r if l.strip()]
            for k,f in enumerate(fs):
                user.append({'type':'text','text':f'PDF page {p} (printed {printed(p)}), strip {k+1} of {len(fs)}:'})
                user.append({'type':'image','source':{'type':'base64','media_type':'image/png','data':base64.b64encode(open(f,'rb').read()).decode()}})
        tail='\n'.join(s[:s.rfind('**Progress note:**')].split('\n')[-150:])
        user.append({'type':'text','text':f'NUMERAL FILE ROWS:\n{out}\n\nPREVIOUS PROGRESS NOTE:\n{note}\n\nEND OF OUTPUT SO FAR (last ~150 lines):\n{tail}\n\nTranslate PDF pages {pages[0]}-{pages[-1]} (printed {printed(pages[0])}-{printed(pages[-1])}) now, in the required output format.'})
        if a.dry:
            n=sum(1 for u in user if u['type']=='image'); print('DRY: pages',pages,'images',n,'text chars',sum(len(u.get('text','')) for u in user),'system chars',len(sysprompt)); return 0
        t=time.time(); txt=''
        with cl.messages.stream(model=a.model,max_tokens=a.max_tokens,system=[{'type':'text','text':sysprompt,'cache_control':{'type':'ephemeral'}}],messages=[{'role':'user','content':user}]) as st:
            for x in st.text_stream: txt+=x
            u=st.get_final_message().usage
        cw=u.cache_creation_input_tokens or 0; cr=u.cache_read_input_tokens or 0
        usd=((u.input_tokens+1.25*cw+0.1*cr)*a.price_in+u.output_tokens*a.price_out)/1e6
        open(COST,'a').write(json.dumps(dict(pages=pages,model=a.model,inp=u.input_tokens,cache_write=cw,cache_read=cr,out=u.output_tokens,usd=round(usd,4),sec=round(time.time()-t)))+'\n')
        print(f'pages {pages}: in {u.input_tokens} cw {cw} cr {cr} out {u.output_tokens} -> ${usd:.3f}  total ${spent():.2f}')
        m=re.search(r'=====CHUNK=====\n(.*?)\n=====NOTE=====\n(.*?)\n=====DOUBTS=====\n?(.*)\Z',txt,re.S)
        if not m: open('/tmp/api_raw.txt','w').write(txt); print('bad format; raw saved /tmp/api_raw.txt'); return 4
        chunk,nt,db=m.group(1).strip(),m.group(2).strip().replace('**Progress note:**','').strip(),m.group(3).strip()
        cf=f'/tmp/api_chunk_{pages[0]}.md'; open(cf,'w',encoding='utf8').write(chunk+'\n')
        sh(f'python3 publish/tools/translit/add_iast.py {cf}'); chunk=open(cf,encoding='utf8').read()
        nd=len(re.findall(r'^> .*[ऀ-ॿ]',chunk,re.M)); ni=len(re.findall(r'^> \*',chunk,re.M))
        print('Devanagari blockquote lines',nd,'IAST lines',ni)
        if not all(f'(PDF {p})' in chunk for p in pages): print('missing page marker; chunk kept at',cf); return 5
        r=subprocess.run(['python3','vol14/tools/append_en.py',nt],input=chunk,capture_output=True,text=True,cwd=ROOT); print(r.stdout.strip(),r.stderr.strip()[-300:])
        if r.returncode: return 6
        if db:
            with open(DOUBTS,'a',encoding='utf8') as f:
                for l in db.split('\n'):
                    if l.strip(): f.write(l.strip()+'\n')
        if not a.no_commit:
            sh(f'git add -A && git commit -qm "Vol 14 (API): printed pp. {printed(pages[0])}–{printed(pages[-1])}" -m "Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>" -m "Claude-Session: https://claude.ai/code/session_01CtcBQVMSeD9UwVaoeH9aHo" && git push -q origin HEAD')
    return 0
sys.exit(main())
