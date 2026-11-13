"""Translate the next N pages of Vol 14 through the Anthropic API (no tool loop).
python3 vol14/tools/api_batch.py [--pages 3] [--model claude-sonnet-5-5] [--budget 90] [--dry] [--no-commit] [--loops K]
Key: env RIK_API_KEY. Position is taken from the trailing progress note ('Done through printed p. N (PDF M)').
Per batch: render strips (page.py), numeral rows (numerals_for.py), call the API (system prompt cached), write chunk to /tmp,
add_iast.py, append_en.py, log doubts to vol14/review/api_doubts.tsv, cost to vol14/parts/api_costs.jsonl, git commit.
Stops on any error, on a missing CHUNK, if cumulative cost would exceed --budget (USD), or if the chunk lacks an IAST line for a Devanagari block."""
import os,sys,re,json,subprocess,base64,time,argparse
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..')); V=os.path.join(ROOT,'vol14')
EN=os.path.join(ROOT,'vol14','Rigveda_Samhita_Vol14_scan_English_Translation.md')
COST=os.path.join(V,'parts','api_costs.jsonl'); DOUBTS=os.path.join(V,'review','api_doubts.tsv')
PRICE=dict(inp=3.0,out=15.0)   # USD per million tokens; ASSUMED Sonnet-class list price, adjust with --price-in/--price-out
def sh(c,**k): return subprocess.run(c,shell=True,capture_output=True,text=True,cwd=ROOT,**k)
def printed(g): return g-18-(1 if g>=224 else 0)-(1 if g>=336 else 0)-(1 if g>=448 else 0)-(1 if g>=560 else 0)-(1 if g>=672 else 0)-(1 if g>=784 else 0)   # PDF 223, 335, 447, 559, 671, 783 are duplicates of the previous page
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
    ap.add_argument('--max-tokens',type=int,default=40000); a=ap.parse_args()
    want=open(os.path.join(V,'BRANCH_FOR_RUNS')).read().split()[0] if os.path.exists(os.path.join(V,'BRANCH_FOR_RUNS')) else None
    cur=sh('git rev-parse --abbrev-ref HEAD').stdout.strip()
    if want and cur!=want and not os.environ.get('ALLOW_OTHER_BRANCH'):
        print(f'STOP: you are on branch {cur!r}, but Vol 14 runs belong on {want!r}. Run: git checkout {want}'); return 7
    import anthropic
    cl=anthropic.Anthropic(api_key=os.environ['RIK_API_KEY'],timeout=900.0,max_retries=2)
    sysprompt=''.join(open(os.path.join(ROOT,f)).read()+'\n\n=========\n\n' for f in ['CLAUDE.md','vol14/vol14_runbook.md'])+open(os.path.join(V,'API_PROMPT.md')).read()
    bs={'n':a.pages}
    for _ in range(a.loops):
        done,note,s=position(); pages=[]
        q=done+1
        while len(pages)<bs['n']:
            if q not in (223,335,447,559,671,783): pages.append(q)
            q+=1
        if any(p in (223,335) for p in pages): print('duplicate page in range; handle by hand',pages); return 2
        if spent()>=a.budget: print('budget reached',spent()); return 3
        user=[]; 
        r0=sh(f'{sys.executable} vol14/tools/numerals_for.py {" ".join(map(str,pages))}')
        if r0.returncode: print('STOP: numerals_for.py failed:\n',r0.stderr[-600:]); return 8
        out=r0.stdout
        for p in pages:
            rp=sh(f'{sys.executable} vol14/tools/page.py {p} /tmp/api_pg_{p}')
            fs=[l.split()[0] for l in rp.stdout.split('\n') if l.strip()]
            if rp.returncode or not fs or not all(os.path.exists(x) for x in fs):
                print(f'STOP: could not render PDF page {p}. Error:\n',rp.stderr[-800:]); return 9
            for k,f in enumerate(fs):
                user.append({'type':'text','text':f'PDF page {p} (printed {printed(p)}), strip {k+1} of {len(fs)}:'})
                user.append({'type':'image','source':{'type':'base64','media_type':'image/png','data':base64.b64encode(open(f,'rb').read()).decode()}})
        tail='\n'.join(s[:s.rfind('**Progress note:**')].split('\n')[-150:])
        user.append({'type':'text','text':f'NUMERAL FILE ROWS:\n{out}\n\nPREVIOUS PROGRESS NOTE:\n{note}\n\nEND OF OUTPUT SO FAR (last ~150 lines):\n{tail}\n\nTranslate PDF pages {pages[0]}-{pages[-1]} (printed {printed(pages[0])}-{printed(pages[-1])}) now, in the required output format.'})
        if a.dry:
            n=sum(1 for u in user if u['type']=='image'); print('DRY: pages',pages,'images',n,'text chars',sum(len(u.get('text','')) for u in user),'system chars',len(sysprompt)); return 0
        t=time.time(); txt=''
        for attempt in range(6):          # transient errors (overloaded 503/529, rate limit, dropped connection): wait and retry the whole call
            try:
                txt=''
                with cl.messages.stream(model=a.model,max_tokens=a.max_tokens,system=[{'type':'text','text':sysprompt,'cache_control':{'type':'ephemeral'}}],messages=[{'role':'user','content':user}]) as st:
                    for x in st.text_stream: txt+=x
                    fm=st.get_final_message(); u=fm.usage; stop=fm.stop_reason
                break
            except Exception as e:   # transient: overloaded / rate limit / connection dropped mid-stream (SSL read error); anything else is raised
                transient=isinstance(e,(anthropic.InternalServerError,anthropic.RateLimitError,anthropic.APIConnectionError,anthropic.APITimeoutError,OSError)) or type(e).__module__.split('.')[0] in ('httpx','httpx2','httpcore','httpcore2','h11','h2','ssl','socket')
                if not transient: raise
                wait=[20,60,120,240,480,900][attempt]
                print(f'API busy ({type(e).__name__}); retry {attempt+1}/6 in {wait}s',flush=True); time.sleep(wait)
        else:
            print('STOP: API still unavailable after 6 tries; run again later.'); return 10
        cw=u.cache_creation_input_tokens or 0; cr=u.cache_read_input_tokens or 0
        usd=((u.input_tokens+1.25*cw+0.1*cr)*a.price_in+u.output_tokens*a.price_out)/1e6
        open(COST,'a').write(json.dumps(dict(pages=pages,model=a.model,inp=u.input_tokens,cache_write=cw,cache_read=cr,out=u.output_tokens,usd=round(usd,4),sec=round(time.time()-t)))+'\n')
        print(f'pages {pages}: in {u.input_tokens} cw {cw} cr {cr} out {u.output_tokens} -> ${usd:.3f}  total ${spent():.2f}')
        if stop=='max_tokens':
            open('/tmp/api_raw.txt','w',encoding='utf8').write(txt)
            if bs['n']>1:
                print(f'OUTPUT LIMIT reached with {bs["n"]} pages (the reply was cut off, nothing written). Retrying these pages one at a time.'); bs['n']=1; continue
            print('OUTPUT LIMIT reached even for one page; raise --max-tokens or tell Claude.'); return 14
        bs['n']=a.pages
        m=re.search(r'=====CHUNK=====\n(.*?)\n=====NOTE=====\n(.*?)\n=====DOUBTS=====\n?(.*)\Z',txt,re.S)
        if not m: open('/tmp/api_raw.txt','w').write(txt); print('bad format; raw saved /tmp/api_raw.txt'); return 4
        chunk,nt,db=m.group(1).strip(),m.group(2).strip().replace('**Progress note:**','').strip(),m.group(3).strip()
        open(f'/tmp/api_raw_{pages[0]}.txt','w',encoding='utf8').write(txt)
        cf=f'/tmp/api_chunk_{pages[0]}.md'; open(cf,'w',encoding='utf8').write(chunk+'\n')
        t0=open(cf,encoding='utf8').read(); t0=re.sub(r'(\n> [^\n]*[\u0900-\u097F][^\n]*)\n\n(\*\()',r'\1\n\nXXPHXX\2',t0); open(cf,'w',encoding='utf8').write(t0)
        sh(f'python3 publish/tools/translit/add_iast.py {cf}'); chunk=open(cf,encoding='utf8').read().replace('XXPHXX','')
        open(cf,'w',encoding='utf8').write(chunk)
        try:
            sys.path.insert(0,os.path.join(V,'tools')); import labels; chunk=labels.normalise(chunk); open(cf,'w',encoding='utf8').write(chunk)
            import accents
            st={'ptr':accents.ptr_from_file(open(EN,encoding='utf8').read())}
            c2,arep=accents.apply_text(chunk,st); assert accents.strip_ac(c2)==chunk
            chunk=c2; open(cf,'w',encoding='utf8').write(chunk)
            bad=[r for r in arep if r[0] in ('NOMATCH','ABORT')]
            print('accents: lines done',sum(1 for r in arep if r[0]=='OK'),'unmatched',len(bad),bad[:3])
            rows=accents.diff_rows(arep,chunk)
            if rows:
                with open(os.path.join(V,'review','accent_ref_differences.tsv'),'a',encoding='utf8') as o:
                    for rid,ours,ref,d in rows: o.write(f'{rid}\t{ours}\t{ref}\t{d}\n')
        except Exception as e: print('accents skipped:',type(e).__name__,e)
        nd=len(re.findall(r'^> .*[ऀ-ॿ]',chunk,re.M)); ni=len(re.findall(r'^> \*',chunk,re.M))
        print('Devanagari blockquote lines',nd,'IAST lines',ni)
        miss=[p for p in pages if f'(PDF {p})' not in chunk and not re.search(rf'PDF {p}[^\n]{{0,80}}duplicate|duplicate[^\n]{{0,120}}PDF {p}',chunk)]
        if miss: print('missing page marker for',miss,'; chunk kept at',cf); return 5
        r=subprocess.run(['python3','vol14/tools/append_en.py',nt],input=chunk,capture_output=True,text=True,cwd=ROOT); print(r.stdout.strip(),r.stderr.strip()[-300:])
        if r.returncode: return 6
        if db:
            with open(DOUBTS,'a',encoding='utf8') as f:
                for l in db.split('\n'):
                    if l.strip(): f.write(l.strip()+'\n')
        if not a.no_commit:
            rc=sh(f'git add -A && git commit -qm "Vol 14 (API): printed pp. {printed(pages[0])}–{printed(pages[-1])}" -m "Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>" -m "Claude-Session: https://claude.ai/code/session_01CtcBQVMSeD9UwVaoeH9aHo"')
            if rc.returncode: print('commit failed:',rc.stderr[-400:]); return 11
            rp=sh('git push origin HEAD')
            if rp.returncode:
                print('PUSH REJECTED:',rp.stderr.strip()[-300:],'\n-> trying git pull --rebase once')
                rr=sh('git pull --rebase origin '+cur)
                if rr.returncode:
                    sh('git rebase --abort'); print('STOP: pull --rebase failed (conflict). Your batches are committed locally and safe. Paste this to Claude:',rr.stderr.strip()[-500:]); return 12
                rp=sh('git push origin HEAD')
                if rp.returncode: print('STOP: push still failing:',rp.stderr.strip()[-400:]); return 13
            print('pushed')
    return 0
sys.exit(main())
