"""Window workflow for Vol 15+ (3 printed pages at a time, Claude Code sessions).  Run from the repository root.
Base text = the supplied machine-read HTML/markdown (volcfg "source"); the scan is optional (spot checks only).

  python3 tools/rv/batch.py new VOL [--mandala M] [--branch B] [--start-page P] [--source "file@1-100" ...]   scaffold volN/
  python3 tools/rv/batch.py prep VOL                      next window: WIN/kn.md (made by script from the text), source text, numeral rows, PROMPT.txt
  (translator checks kn.md, writes WIN/en.md; see tools/rv/TRANSLATOR_RULES.md)
  python3 tools/rv/batch.py build VOL WIN                 [[bN]] / inline Sanskrit -> Devanagari, IAST, labels, accents  ->  WIN/en_final.md, WIN/kn_final.md
  python3 tools/rv/batch.py check VOL WIN [--max-doubts 0] gates: pages present, [?] count, numerals vs the user's file, twins, structure (exit 1 = fix and re-run)
  python3 tools/rv/batch.py zoomlist VOL WIN              every [?] with line and context
  python3 tools/rv/batch.py fix VOL WIN kn|en OLD NEW     exact unique replacement in WIN/kn.md or WIN/en.md (logged); then re-run build + check
  python3 tools/rv/batch.py commit VOL WIN --note TEXT [--max-doubts N] [--no-git]   append to the two volume files (progress note replaced), doubts log, git commit + push
Position = the trailing '**Progress note:** Done through printed p. N' of the English file. Nothing is appended unless `check` passes."""
import os,re,sys,json,glob,subprocess,shutil
sys.path.insert(0,os.path.dirname(__file__))
import rvlib,numerals,convert,labels,html_to_kn
ROOT=rvlib.ROOT
def sh(c,**k): return subprocess.run(c,shell=True,capture_output=True,text=True,cwd=ROOT,**k)
def rd(p): return open(p,encoding='utf8').read()
def wr(p,s): open(p,'w',encoding='utf8').write(s)
def position(cfg):
    s=rd(cfg.en); i=s.rfind('**Progress note:**'); m=re.search(r'Done through printed p\. (\d+)(?: \(PDF (\d+)\))?',s[i:]) if i>=0 else None
    if not m: sys.exit('no "Done through printed p. N" in the progress note of '+cfg.en)
    return int(m.group(1)),(int(m.group(2)) if m.group(2) else None)
def next_pages(cfg,done_printed,done_pdf,src):
    if src is not None:
        ks=[k for k in sorted(src) if k>done_printed]
        if not ks: sys.exit(f'no page after printed p. {done_printed} in the supplied text: supply the next file')
        return [(k,cfg.printed_to_pdf(k)) for k in ks[:cfg.window]]
    pages=[];q=(done_pdf or 0)+1
    while len(pages)<cfg.window:
        if q not in cfg.skip: pages.append((cfg.printed(q),q))
        q+=1
    return pages
def state_path(cfg): return os.path.join(cfg.work,'state.json')
def cmd_new(a):
    vol=int(a[0]); opt=lambda k,d:a[a.index(k)+1] if k in a else d
    d=os.path.join(ROOT,f'vol{vol}')
    for s in ('html','numerals','work','review'): os.makedirs(os.path.join(d,s),exist_ok=True)
    cp=rvlib.cfg_path(vol); start=int(opt('--start-page',1))
    if os.path.exists(cp): sys.exit(cp+' exists')
    src=[a[i+1] for i,x in enumerate(a) if x=='--source']
    cfg={"vol":vol,"mandala":int(opt('--mandala',1)),"branch":opt('--branch',f'claude/vol{vol}'),
         "source":src or [f"vol{vol}/html/rig_{vol}_1.html@1-100"],"scan":{"glob":f"vol{vol}/scans/{vol} *.pdf"},"printed":[[1,0]],"skip_pdf":[],
         "numerals":{"glob":f"vol{vol}/numerals/*.xlsx","file_page":[[1,0]]},
         "out":{"kn":f"vol{vol}/Rigveda_Samhita_Vol{vol}_Kannada_Text.md","en":f"vol{vol}/Rigveda_Samhita_Vol{vol}_English_Translation.md"},
         "work":f"vol{vol}/work","window":3}
    wr(cp,json.dumps(cfg,indent=1,ensure_ascii=False)+'\n')
    en=os.path.join(ROOT,cfg['out']['en']); kn=os.path.join(ROOT,cfg['out']['kn'])
    if not os.path.exists(en): wr(en,f'# Rigveda Samhita — Volume {vol} (Kannada → English translation)\n\n---\n\n**Progress note:** Done through printed p. {start-1}; nothing translated yet.\n')
    if not os.path.exists(kn): wr(kn,f'# ಋಗ್ವೇದ ಸಂಹಿತಾ — ಸಂಪುಟ {vol} (Kannada text)\n*The Kannada text of the printed pages, made by script from the supplied machine-read text (tools/rv/html_to_kn.py) and checked by the translator; the English file is made from it. `[?]` marks a doubtful reading.*\n\n---\n\n')
    print('created',cp,'\nnext: put the supplied HTML/markdown in',f'vol{vol}/html/','and list it under "source" (file@FIRST-LAST printed pages); set "printed" only if you need PDF numbers (numeral file pages), and the numeral file(s) in',f'vol{vol}/numerals/')
def cmd_prep(a):
    cfg=rvlib.Cfg(a[0]); heads={}; src=cfg.source_pages(heads)
    if src is None: sys.exit('volcfg.json has no "source": this workflow needs the supplied text (use the older scan workflow only for volumes without one)')
    dp,dpdf=position(cfg); pages=next_pages(cfg,dp,dpdf,src); w=os.path.join(cfg.work,f'w{pages[0][0]:04d}'); os.makedirs(w,exist_ok=True)
    st=json.load(open(state_path(cfg))) if os.path.exists(state_path(cfg)) else {}
    kn,sec=html_to_kn.kn_pages(cfg.source and [os.path.join(ROOT,x.split('@')[0])+('@'+x.split('@')[1] if '@' in x else '') for x in cfg.source],[p for p,_ in pages],st.get('section'))
    wr(os.path.join(w,'kn.md'),kn); wr(os.path.join(w,'section_end.txt'),sec or '')
    rows=numerals.load(cfg) if cfg.numeral_files() else []; info=[]; nrows=[]
    for pr,g in pages:
        rs=numerals.rows_for(cfg,rows,g) if g else []
        info.append(dict(printed=pr,pdf=g,file_page=cfg.file_page(g) if g else None,numeral_rows=len(rs)))
        nrows.append(f'== printed {pr} (PDF {g}, file page {cfg.file_page(g) if g else "?"}): {len(rs)} rows\n'+'\n'.join(f"  line {r['line']} | {r['kn']} | {r['en']} | {r['ctx'][:100]}" for r in rs))
    wr(os.path.join(w,'pages.json'),json.dumps(info,indent=1)); wr(os.path.join(w,'numerals.txt'),'\n'.join(nrows)+'\n')
    rel=os.path.relpath(w,ROOT)
    wr(os.path.join(w,'PROMPT.txt'),f"""Translate window {rel}: printed pages {pages[0][0]}-{pages[-1][0]} of Vol {cfg.vol}.
Read tools/rv/TRANSLATOR_RULES.md first. The Kannada text of these pages is in {rel}/kn.md (made by script from the supplied machine-read text; letters and numbers are as supplied);
numeral rows of the user's file: {rel}/numerals.txt. Position before this window: done through printed p. {dp}. The end of {os.path.relpath(cfg.en,ROOT)} (last ~80 lines) shows the format.
Write {rel}/en.md (the Kannada text is NOT retyped: Sanskrit blocks are placed with [[bN]]), then run build and check (VOL={cfg.vol}) until check passes, then commit.
""")
    print(w); print(json.dumps(info,indent=1))
    miss=[p for p,_ in pages if p not in src]
    if miss: print('WARNING: not in the supplied text:',miss)
    if cfg.numeral_files() and any(i['numeral_rows']==0 for i in info): print('NOTE: a numeral file is configured but has no rows for some of these pages (check numerals.file_page in volcfg.json)')
def cmd_build(a):
    cfg=rvlib.Cfg(a[0]); w=a[1]; kn=rd(os.path.join(w,'kn.md')); en=rd(os.path.join(w,'en.md'))
    if re.search(r'^> \*',en,re.M): sys.exit("FAIL: IAST typed by hand in en.md ('> *' lines): IAST is added by script")
    text,prob=convert.expand(en,kn)
    if prob: print('PROBLEMS:'); print('\n'.join(' - '+p for p in prob)); sys.exit(1)
    p=os.path.join(w,'en_final.md'); wr(p,text)
    r=sh(f'python3 publish/tools/translit/add_iast.py "{p}"'); print('add_iast:',(r.stdout+r.stderr).strip()[-200:])
    wr(p,labels.normalise(rd(p)))
    r=sh(f'python3 publish/tools/accents/accent_volume.py {cfg.vol} --file "{p}" --write'); print('accents:',[l for l in (r.stdout+r.stderr).split('\n') if l.startswith('Vol') or 'not matched' in l or 'Error' in l or 'Trace' in l])
    wr(os.path.join(w,'kn_final.md'),convert.kn_final(kn)); print('built',p,os.path.join(w,'kn_final.md'))
def doubts(text): return [(i,l.strip()[:110]) for i,l in enumerate(text.split('\n'),1) if '[?]' in l]
def cmd_check(a):
    cfg=rvlib.Cfg(a[0]); w=a[1]; mx=int(a[a.index('--max-doubts')+1]) if '--max-doubts' in a else 0
    pg=json.load(open(os.path.join(w,'pages.json'))); kn=rd(os.path.join(w,'kn.md')); en=rd(os.path.join(w,'en.md')); fail=[]
    fe=os.path.join(w,'en_final.md')
    if not os.path.exists(fe): sys.exit('run build first')
    enf=rd(fe)
    for p in pg:
        if not re.search(rf"<!-- printed {p['printed']}[ :]",kn) and not re.search(rf"<!-- PDF {p['pdf']} ·",kn): fail.append(f"kn.md has no page marker for printed p. {p['printed']}")
        if not re.search(rf"### Printed p\. {p['printed']}\b",en): fail.append(f"en.md has no heading '### Printed p. {p['printed']}'")
    dk,de=doubts(kn),doubts(enf)
    if len(dk)+len(de)>mx: fail.append(f'[?] left: {len(dk)} in kn.md, {len(de)} in en.md (allowed {mx})')
    pdfs=[p['pdf'] for p in pg if p['pdf']]; res=numerals.check(cfg,pdfs,kn,en) if cfg.numeral_files() else numerals.check(cfg,[],kn,en,rows=[])
    print(numerals.report(res))
    if res['near']: fail.append(f"{len(res['near'])} numerals differ from the numeral file by 1-2 characters (the file is the reference: correct kn.md, or tell the user)")
    if res['twin_bad']: fail.append(f"English references without Kannada twin: {res['twin_bad']}")
    if res['missing']: fail.append(f"{len(res['missing'])} numeral-file rows have no counterpart in the Kannada text")
    if re.search(r'\[\[b\d+\]\]',enf): fail.append('unresolved [[bN]] in en_final.md')
    if re.search('['+chr(0x0900)+'-'+chr(0x0963)+chr(0x0966)+'-'+chr(0x097F)+']',convert.kn_final(kn)): fail.append('Devanagari in kn.md (the Kannada file is Kannada script only; danda marks are allowed)')
    nums=[int(x) for x in re.findall(r'^#### Ṛk (\d+)',enf,re.M)]
    if nums and any(b<a_ and b!=1 for a_,b in zip(nums,nums[1:])): fail.append(f'Ṛk headings out of order: {nums}')
    print('\nFAIL:' if fail else '\nPASS')
    for f in fail: print(' -',f)
    sys.exit(1 if fail else 0)
def cmd_zoomlist(a):
    w=a[1]
    for name in ('kn.md','en.md'):
        t=rd(os.path.join(w,name)); page=None
        for i,l in enumerate(t.split('\n'),1):
            m=re.search(r'<!-- printed (\d+)',l) or re.search(r'### Printed p\. (\d+)',l)
            if m: page=m.group(1)
            if '[?]' in l: print(f'{name}:{i}  printed p. {page}  {l.strip()[:140]}')
def cmd_fix(a):
    w,which,old,new=a[1],a[2],a[3],a[4]; p=os.path.join(w,{'kn':'kn.md','en':'en.md'}[which]); t=rd(p)
    if t.count(old)!=1: sys.exit(f'FAIL: old text occurs {t.count(old)} times in {which}.md (must be exactly once; add context)')
    wr(p,t.replace(old,new)); open(os.path.join(w,'fixes.tsv'),'a',encoding='utf8').write(f'{which}\t{old}\t{new}\n'); print('fixed; re-run build and check')
def cmd_commit(a):
    cfg=rvlib.Cfg(a[0]); w=a[1]; note=a[a.index('--note')+1]; mx=a[a.index('--max-doubts')+1] if '--max-doubts' in a else '0'
    r=sh(f'python3 tools/rv/batch.py check {cfg.vol} "{w}" --max-doubts {mx}'); print(r.stdout[-1500:])
    if r.returncode: sys.exit('check failed: nothing appended')
    if cfg.branch and '--no-git' not in a:
        cur=sh('git rev-parse --abbrev-ref HEAD').stdout.strip()
        if cur!=cfg.branch and not os.environ.get('ALLOW_OTHER_BRANCH'): sys.exit(f'STOP: on branch {cur!r}, Vol {cfg.vol} belongs on {cfg.branch!r}')
    pg=json.load(open(os.path.join(w,'pages.json'))); last=max(pg,key=lambda x:x['printed']);   # highest printed page, even if a merged head was appended to pages.json out of order (Vol 12 w0159) enf=rd(os.path.join(w,'en_final.md')).rstrip('\n'); knf=rd(os.path.join(w,'kn_final.md')).strip()
    s=rd(cfg.en); n0=len(s); i=s.rfind('**Progress note:**')
    if i>=0:
        assert i>len(s)-20000,'progress note not near the end'; s=s[:i].rstrip('\n').rstrip('-').rstrip('\n')
    pdf=f" (PDF {last['pdf']})" if last['pdf'] else ''
    s=s+'\n\n'+enf+f"\n\n---\n\n**Progress note:** Done through printed p. {last['printed']}{pdf}. {note}\n"
    assert s.count('**Progress note:**')==1 and len(s)>=n0-2000; wr(cfg.en,s)
    k=rd(cfg.kn); assert not re.search(rf"<!-- printed {pg[0]['printed']}[ :]",k),'Kannada file already has this window'; wr(cfg.kn,k.rstrip('\n')+'\n\n'+knf+'\n')
    sec=rd(os.path.join(w,'section_end.txt')).strip() if os.path.exists(os.path.join(w,'section_end.txt')) else ''
    os.makedirs(cfg.work,exist_ok=True); wr(state_path(cfg),json.dumps({'section':sec or None,'printed':last['printed']}))
    rng=f"printed pp. {pg[0]['printed']}-{last['printed']}"
    dl=[(rng,'kn',i,t) for i,t in doubts(rd(os.path.join(w,'kn.md')))]+[(rng,'en',i,t) for i,t in doubts(enf)]
    if dl:
        os.makedirs(os.path.join(ROOT,f'vol{cfg.vol}','review'),exist_ok=True)
        with open(os.path.join(ROOT,f'vol{cfg.vol}','review','doubts.tsv'),'a',encoding='utf8') as f:
            for x in dl: f.write('\t'.join(map(str,x))+'\n')
    print('appended to',os.path.relpath(cfg.en,ROOT),'and',os.path.relpath(cfg.kn,ROOT),f'; {len(dl)} doubts logged')
    if '--no-git' not in a:
        r=sh(f'git add -A && git commit -qm "Vol {cfg.vol}: {rng}" -m "Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>" && git push -q origin HEAD'); print('git:',(r.stdout+r.stderr).strip()[-200:] or 'pushed')
CMDS=dict(new=cmd_new,prep=cmd_prep,build=cmd_build,check=cmd_check,zoomlist=cmd_zoomlist,fix=cmd_fix,commit=cmd_commit)
if __name__=='__main__':
    if len(sys.argv)<3 or sys.argv[1] not in CMDS: sys.exit(__doc__)
    CMDS[sys.argv[1]](sys.argv[2:])
