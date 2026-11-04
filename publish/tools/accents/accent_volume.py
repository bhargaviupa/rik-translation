"""Add Vedic accent marks (U+0951 svarita, U+0952 anudatta) to the Samhita blocks of one volume, from an accented Mandala HTML.

  python3 publish/tools/accents/accent_volume.py VOL [--html FILE ...] [--write] [--api] [--dry] [--model M] [--budget USD]

VOL           volume number (1-14). File used: volN/Rigveda_Samhita_VolN_English_Translation.md (Vol 14: repo root, until moved).
--html        accented Mandala file(s); default: every refs/mandala/*.html (and .htm/.txt) in the repo. Give two for a volume that crosses a
              Mandala boundary. The HTML is read as text; each verse must end with its number, e.g. "॥ 1.001.01" (Devanagari or Latin digits).
--write       rewrite the volume file in place (otherwise only a report; nothing is changed).
--api         for blocks the script cannot match by itself, ask the Anthropic API (key: env RIK_API_KEY) to add the marks to OUR line,
              using the closest reference line(s) as a guide. A reply is accepted only if removing the marks gives back our line unchanged.
--dry         with --api: show how many lines would be sent and stop.
--budget      stop sending API requests once the cumulative cost of this volume reaches USD (default 5).
Only accent marks are ever added; the printed spelling of the volume is never changed (checked for every line). Already accented
lines are left alone, so the script can be re-run. Reports: volN/review/accent_report.tsv; API cost log: volN/parts/accent_api_costs.jsonl.
The reference file is a volunteer text "for personal study and research; not to be copied or reposted": keep it out of any public repo."""
import os,sys,re,glob,json,time,argparse,difflib,importlib.util
from html.parser import HTMLParser
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..','..'))
spec=importlib.util.spec_from_file_location('acc',os.path.join(ROOT,'vol14','tools','accents.py')); acc=importlib.util.module_from_spec(spec); spec.loader.exec_module(acc)
AC=acc.AC
DEVD=str.maketrans('०१२३४५६७८९','0123456789')
IDRE=re.compile(r'(\d{1,2})\s*\.\s*(\d{1,3})\s*\.\s*(\d{1,3})\s*$')
class _T(HTMLParser):
    BLOCK={'br','p','div','tr','li','h1','h2','h3','h4','h5','h6','table','section','article','pre','dd','dt'}
    def __init__(s): super().__init__(convert_charrefs=True); s.out=[]; s.skip=0
    def handle_starttag(s,t,a):
        if t in('script','style'): s.skip+=1
        if t in s.BLOCK: s.out.append('\n')
    def handle_endtag(s,t):
        if t in('script','style'): s.skip=max(0,s.skip-1)
        if t in s.BLOCK: s.out.append('\n')
    def handle_data(s,d):
        if not s.skip: s.out.append(d)
def read_ref(path):
    """-> list of ((mandala,sukta,rik), line) in file order; one entry per printed half-verse line"""
    raw=open(path,encoding='utf8').read()
    if path.lower().endswith(('.html','.htm')) or re.search(r'<(html|body|div|p)\b',raw[:2000],re.I):
        p=_T(); p.feed(raw); raw=''.join(p.out)
    lines=[re.sub(r'\s+',' ',l.replace(' ',' ')).strip() for l in raw.split('\n')]
    rik=[];cur=[]
    for l in lines:
        if not l or l.startswith('#'): continue
        t=l.translate(DEVD); m=IDRE.search(t)
        if m and ('॥' in l or '||' in l or len(l)>len(m.group(0))+8):
            body=re.sub(r'[॥|\s]*$','',l[:m.start()]).strip()
            if body: cur.append(body)
            rik.append(((int(m.group(1)),int(m.group(2)),int(m.group(3))),cur)); cur=[]
        else: cur.append(l)
    return [(rid,l) for rid,ls in rik for l in ls]
def vol_file(n):
    for p in (f'vol{n}/Rigveda_Samhita_Vol{n}_English_Translation.md',f'Rigveda_Samhita_Vol{n}_English_Translation.md'):
        if os.path.exists(os.path.join(ROOT,p)): return os.path.join(ROOT,p)
    sys.exit(f'no translation file found for Vol {n}')
def find_blocks(L):
    """yield (header_index, [line indexes of '> ' Samhita lines], header_text)"""
    i=0
    while i<len(L):
        if '॥ संहितापाठः ॥' in L[i]:
            j=i+1
            while j<len(L) and (not L[j].strip() or L[j].startswith('#') or L[j].strip()=='---' or (L[j].startswith('*') and not L[j].startswith('> '))): j+=1
            k=j
            while k<len(L) and L[k].startswith('> ') and not L[k].startswith('> *'): k+=1
            yield i,list(range(j,k)),L[i]; i=k
        else: i+=1
def spent(cf):
    return sum(json.loads(l)['usd'] for l in open(cf)) if os.path.exists(cf) else 0.0
def api_fix(cl,model,items,cands,cf,price_in,price_out):
    """items: [(idx, ours)] -> {idx: accented or None}"""
    sysmsg=("You add Vedic accent marks to Rigveda Samhita lines written in Devanagari. For each item you get OUR line and one or two reference "
            "lines (accented, from another edition, spelling may differ slightly). Return OUR line with accent marks added (U+0951 svarita, U+0952 anudatta, "
            "and the digit notation if the reference uses it) and NOTHING else changed: no letter, space, danda or numeral of OUR line may be altered, added or removed. "
            "If you are not sure which reference line applies or cannot place the marks, return OUR line unchanged. "
            'Reply with JSON only: {"1":"line", "2":"line", ...} using the item numbers given.')
    out={}
    for b in range(0,len(items),25):
        part=items[b:b+25]
        body='\n\n'.join(f'ITEM {n+1}\nOUR: {o}\n'+'\n'.join(f'REF: {c}' for c in cands[idx]) for n,(idx,o) in enumerate(part))
        t=time.time()
        r=cl.messages.create(model=model,max_tokens=8000,system=[{'type':'text','text':sysmsg,'cache_control':{'type':'ephemeral'}}],messages=[{'role':'user','content':body}])
        u=r.usage; usd=((u.input_tokens+1.25*(u.cache_creation_input_tokens or 0)+0.1*(u.cache_read_input_tokens or 0))*price_in+u.output_tokens*price_out)/1e6
        os.makedirs(os.path.dirname(cf),exist_ok=True)
        open(cf,'a').write(json.dumps(dict(n=len(part),model=model,inp=u.input_tokens,out=u.output_tokens,usd=round(usd,4),sec=round(time.time()-t)))+'\n')
        txt=''.join(x.text for x in r.content if x.type=='text'); m=re.search(r'\{.*\}',txt,re.S)
        try: js=json.loads(m.group(0)) if m else {}
        except Exception: js={}
        for n,(idx,o) in enumerate(part): out[idx]=js.get(str(n+1))
        print(f'  API batch of {len(part)}: ${usd:.3f}, total ${spent(cf):.2f}')
        if spent(cf)>=BUDGET[0]: print('budget reached; stopping API use'); break
    return out
BUDGET=[5.0]
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('vol',type=int); ap.add_argument('--html',nargs='*'); ap.add_argument('--file',help='translation file to use instead of the default for VOL (testing)'); ap.add_argument('--write',action='store_true')
    ap.add_argument('--api',action='store_true'); ap.add_argument('--dry',action='store_true'); ap.add_argument('--model',default='claude-sonnet-5-5')
    ap.add_argument('--budget',type=float,default=5.0); ap.add_argument('--price-in',type=float,default=3.0); ap.add_argument('--price-out',type=float,default=15.0)
    ap.add_argument('--threshold',type=float,default=0.85); a=ap.parse_args(); BUDGET[0]=a.budget
    files=a.html or sorted(sum((glob.glob(os.path.join(ROOT,'refs','mandala',e)) for e in('*.html','*.htm','*.txt')),[]))
    if not files: sys.exit('no reference file: put the Mandala HTML in refs/mandala/ or pass --html FILE')
    REF=[]
    for f in files:
        r=read_ref(f); print(f'reference {os.path.relpath(f,ROOT)}: {len(r)} lines, {len({x[0] for x in r})} verses')
        if not r:
            raw=open(f,encoding='utf8').read(); t=_T(); t.feed(raw)
            print('No verse numbers like "॥ 1.001.01" found. First text lines of the file:'); print('\n'.join([l.strip() for l in ''.join(t.out).split('\n') if l.strip()][:15])); return 2
        REF+=r
    cr=[acc.canon(x[1]) for x in REF]
    vf=a.file or vol_file(a.vol); text=open(vf,encoding='utf8').read(); L=text.split('\n'); rep=[]; fail=[]; ptr=0
    def best_near(sk,lo,hi):
        b=None
        for q in range(max(0,lo),min(len(REF),hi)):
            s=difflib.SequenceMatcher(None,sk,cr[q],autojunk=False)
            if s.real_quick_ratio()<(b[0] if b else 0) or s.quick_ratio()<(b[0] if b else 0): continue
            r=s.ratio()
            if b is None or r>b[0]: b=(r,q)
        return b
    for hi,idxs,head in find_blocks(L):
        hint=re.search(r'Rik (\d+)\.(\d+)',head)
        for m in idxs:
            ours=L[m][2:]
            if any(ch in AC for ch in ours): continue
            sk=acc.canon(ours)
            if not sk: continue
            b=best_near(sk,ptr-1,ptr+10)
            if (b is None or b[0]<a.threshold) and ptr==0: b=best_near(sk,0,len(REF))      # first block: search everywhere
            if b is None or b[0]<a.threshold:
                near=best_near(sk,ptr-1,ptr+40) or (0,max(ptr,0)); fail.append((m,ours,near)); rep.append(('NOMATCH',m+1,round(near[0],2),ours[:40])); continue
            r,q=b; new=acc.transfer(ours,REF[q][1])
            if acc.strip_ac(new)!=ours: fail.append((m,ours,b)); rep.append(('ABORT',m+1,round(r,2),ours[:40])); continue
            rid='.'.join(map(str,REF[q][0]))
            if hint and REF[q][0][1:]!=(int(hint.group(1)),int(hint.group(2))): rep.append(('IDMISMATCH',m+1,rid,'header says Rik %s.%s'%hint.groups()))
            if acc.canon(ours)!=cr[q]: rep.append(('DIFF',m+1,rid,round(r,3)))
            L[m]='> '+new; ptr=q+1; rep.append(('OK',m+1,rid))
    import collections; c=collections.Counter(x[0] for x in rep); print(f'Vol {a.vol}:',dict(c))
    api_ok=0
    if a.api and fail:
        cf=os.path.join(ROOT,f'vol{a.vol}','parts','accent_api_costs.jsonl')
        if a.dry: print(f'DRY: would send {len(fail)} lines to the API in {-(-len(fail)//25)} request(s); spent so far ${spent(cf):.2f}, budget ${a.budget}'); return 0
        if spent(cf)>=a.budget: print('budget already reached'); return 3
        import anthropic
        cl=anthropic.Anthropic(api_key=os.environ['RIK_API_KEY'])
        cands={m:[REF[q][1] for q in sorted({near[1],near[1]+1} & set(range(len(REF))))] for m,ours,near in fail}
        res=api_fix(cl,a.model,[(m,o) for m,o,_ in fail],cands,cf,a.price_in,a.price_out)
        for m,ours,near in fail:
            new=res.get(m)
            if new and any(ch in AC for ch in new) and acc.strip_ac(new)==ours: L[m]='> '+new; api_ok+=1; rep.append(('API_OK',m+1,'',ours[:40]))
            else: rep.append(('API_REJECTED',m+1,'',ours[:40]))
        print(f'API: accepted {api_ok} of {len(fail)}')
    elif fail: print(f'{len(fail)} lines not matched; re-run with --api to try them through the API (key RIK_API_KEY)')
    rd=os.path.join(ROOT,f'vol{a.vol}','review'); os.makedirs(rd,exist_ok=True)
    with open(os.path.join(rd,'accent_report.tsv'),'w',encoding='utf8') as o:
        for r in rep:
            if r[0]!='OK': o.write('\t'.join(map(str,r))+'\n')
    new='\n'.join(L)
    assert acc.strip_ac(new)==acc.strip_ac(text),'spelling changed - aborting'
    if a.write:
        assert len(new)>=len(text)
        open(vf,'w',encoding='utf8').write(new); print('written',os.path.relpath(vf,ROOT),'; report vol%d/review/accent_report.tsv'%a.vol)
    else: print('report only (use --write to change the file); report vol%d/review/accent_report.tsv'%a.vol)
    return 0
if __name__=='__main__': sys.exit(main())
