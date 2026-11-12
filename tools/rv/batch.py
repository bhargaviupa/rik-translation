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
  python3 tools/rv/batch.py done VOL WIN --note TEXT [--max-doubts N] [--dry-run]    ONE command for the translator: build + check + inline/placeholder gates + commit + push
                                                          + self-verification (git log, pushed, one progress note); prints <= 12 lines. --dry-run: gates only, nothing appended
  python3 tools/rv/batch.py next VOL [--tokens T] [--tools K] [--min M]             ONE command for the dispatcher: audit the last window, log its cost, prep the next, print the message to send
  python3 tools/rv/batch.py audit VOL                     repository invariants of the two volume files (script, no model): one progress note, no XXX, markers, pushed
  python3 tools/rv/batch.py view VOL WIN                  kn.md with its Sanskrit blocks numbered «bN» (after a fix of kn.md the numbers may have moved)
Position = the trailing '**Progress note:** Done through printed p. N' of the English file. Nothing is appended unless `check` passes."""
import os,re,sys,json,glob,subprocess,shutil
sys.path.insert(0,os.path.dirname(__file__))
import rvlib,numerals,convert,labels,html_to_kn,check_inline
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
def subheads(t):
    """Reader's layout (user, Nov 11 2026): every part of a Ṛk under its own sub-heading, blocks set apart by blank lines, the lines of the verse
    (Saṃhitā, Pada and their transliteration) kept one under the other.  Done at the end of the build; en.md is written as before."""
    out=[]; sec=None
    L=t.split('\n')
    for i,l in enumerate(L):
        m=re.fullmatch(r'\*\*([^*]+)\*\*\s*',l)
        if m and (m.group(1).startswith(('॥','प्रतिपदार्थ','भावार्थ','विशेषविषय','Printed English','Grammar','English translation','Anuvāda','Particulars'))):
            name=m.group(1).strip(); sec=name
            name={'॥ संहितापाठः ॥':'॥ संहितापाठः ॥ (Saṃhitā-pāṭha)','॥ पदपाठः ॥':'॥ पदपाठः ॥ (Pada-pāṭha)','॥ सायणभाष्यम् ॥':'॥ सायणभाष्यम् ॥ (Sāyaṇa-bhāṣya)',
                  'विशेषविषयगळु (Viśeṣaviṣayagaḷu)':'विशेषविषयगळु (Special Topics)'}.get(name,name)
            if out and out[-1].strip(): out.append('')
            out+=['##### '+name,'']; continue
        m=re.match(r'\*\(?Gist[.:)]*\*:?\s*(.*)',l)
        if m:
            if out and out[-1].strip(): out.append('')
            out+=['##### Gist of the bhāṣya','']
            if m.group(1).strip(): out.append(m.group(1).strip())
            sec='gist'; continue
        if l.startswith('#'): sec=None if l.startswith(('#### ','## ')) else sec
        if l.startswith('> '):
            if out and out[-1].strip() and not out[-1].startswith('>'): out.append('')
            verse=sec in ('॥ संहितापाठः ॥','॥ पदपाठः ॥'); nxt=L[i+1] if i+1<len(L) else ''
            out.append(l.rstrip()+('  ' if verse and nxt.startswith('> ') else ''))      # two spaces = line break inside the verse
            if not nxt.startswith('>') and nxt.strip(): out.append('')
            continue
        out.append(l)
    return re.sub(r'\n{3,}','\n\n','\n'.join(out))
def nextrk(L,i):
    """number of the next `#### Ṛk` heading after line i (None when a `## ` heading comes first)"""
    for k in range(i+1,len(L)):
        if L[k].startswith('## '): return None
        m=re.match(r'#### Ṛk (\d+)',L[k])
        if m: return int(m.group(1))
    return None
def rk_headings(t):
    """Every Saṃhitā block stands under its own `#### Ṛk N` heading (lesson 53: in Vol 17 the model left 61 of 441 out, wrote some after the
    Saṃhitā label, some without or with the wrong number, and repeated some on the next page).  Returns (text, list of what was changed).
    N: the verse number the Saṃhitā or the Pada block ends with; a heading that disagrees with it is changed only when the block's number
    continues the sequence (so a misprinted number in the block does not spoil a right heading); no number in the blocks -> the number after the
    one before in the same sūkta; a heading repeated inside a Ṛk gets ' (continued)'."""
    t=re.sub(r'(?m)^#{1,6} *(Ṛk\b)',r'#### \1',t)                      # a Ṛk heading written at another level
    L=t.split('\n'); D=str.maketrans('०१२३४५६७८९','0123456789'); ch=[]
    SAM='##### ॥ संहितापाठः ॥'; isrk=lambda l:l.startswith('#### Ṛk') and '(contin' not in l
    i=0
    while i<len(L):                                   # heading written after the Saṃhitā label: put it before
        if L[i].startswith(SAM):
            k=i+1
            while k<len(L) and not L[k].strip(): k+=1
            if k<len(L) and isrk(L[k]): L[i],L[k]=L[k],L[i]; ch.append(('order',L[i]))
        i+=1
    def num(i):
        b=[]; k=i+1
        while k<len(L) and (not L[k].strip() or L[k].startswith('> ')):
            if L[k].startswith('> *'): break
            if L[k].startswith('> '): b.append(L[k])
            k+=1
        m=re.search(r'॥\s*([०-९]+)\s*॥?\s*$',re.sub('[॒॑]','',b[-1] if b else '')); return int(m.group(1).translate(D)) if m else None
    sams=[i for i,l in enumerate(L) if l.startswith(SAM)]; ins={}; prev=None; own=set()
    for x,i in enumerate(sams):
        end=sams[x+1] if x+1<len(sams) else len(L); n=num(i)
        for k in range(i+1,end):
            if L[k].startswith('## ') or isrk(L[k]): break
            if L[k].startswith('##### ॥ पदपाठः ॥'): n=n or num(k); break
        h=None; k=i-1
        while k>=0 and not L[k].startswith(('##### ','## ','####')): k-=1
        if k>=0 and isrk(L[k]): h=k
        k=i-1
        while k>=0 and not L[k].startswith('## '):
            if L[k].startswith(SAM): break
            k-=1
        if k<0 or L[k].startswith('## '): prev=None                     # first Ṛk of a sūkta (or of the text)
        if k>=0 and L[k].startswith('## Sūkta') and n is None: n=1
        if h is None:
            n=n or (prev+1 if prev else None); ins[i]='#### Ṛk'+(f' {n}' if n else ''); ch.append(('added',n))
        else:
            own.add(h); m=re.search(r'\d+',L[h]); hn=int(m.group()) if m else None
            if hn is None: n=n or (prev+1 if prev else None)
            elif n is None or (n!=hn and not (prev and n==prev+1)): n=hn
            if n!=hn: ch.append(('number',f'{L[h]} -> {n}')); L[h]=f'#### Ṛk {n}'
        prev=n
    out=[]; cur=None
    for i,l in enumerate(L):
        if l.startswith('## '): cur=None
        if i in ins: out+=[ins[i],'']; m=re.search(r'\d+',ins[i]); cur=int(m.group()) if m else None
        elif isrk(l):
            m=re.search(r'\d+',l); n=int(m.group()) if m else None
            if i in own: cur=n
            elif n is not None and n==cur: l=l.rstrip()+' (continued)'; ch.append(('continued',n))
            elif n is not None and cur is not None and n!=cur and nextrk(L,i)==n: l=f'#### Ṛk {cur} (continued)'; ch.append(('continued',cur))      # the model wrote the NEXT Ṛk's number on the tail of this one (Vol 18 p. 310): the real heading follows
            if len(out)>=2 and isrk(out[-2]) and not out[-1].strip() and (out[-2]==l or not re.search(r'\d',l)): ch.append(('double',l)); continue
        out.append(l)
    return '\n'.join(out),ch
NOTE_RE=re.compile(r'\*\*NOTE\*\*\{([^{}]*)\}')
def note_style(cfg): return cfg.d.get('note_style')=='NOTE'
def split_notes(en):
    """'**NOTE**{detail}' in en.md -> ('**NOTE**' in the text, [(printed page, detail, words before it)]).  The reader's text carries only the mark;
    the detail goes to volN/review/notes.tsv (user decision, Nov 11 2026: no translator remarks in the English text)."""
    notes=[]; page=[None]; out=[]
    for l in en.split('\n'):
        m=re.match(r'### Printed p\. (\d+)',l)
        if m: page[0]=int(m.group(1))
        def r(mm):
            notes.append((page[0],re.sub(r'\s+',' ',mm.group(1)).strip(),re.sub(r'\s+',' ',NOTE_RE.sub('',l[:mm.start()]))[-60:])); return '**NOTE**'
        out.append(NOTE_RE.sub(r,l))
    return '\n'.join(out),notes
PLACEHOLDER=re.compile(r'(?<![IVXLCDM])XXX(?![IVXLCDM])')   # the placeholder, not a printed roman numeral such as 'Vol. XXXII' (Vol 12 p. 536: a translator rewrote the numeral to pass)
def numbered(kn):
    """kn.md with «bN» before the first line of every Sanskrit block (the numbers [[bN]] refers to)"""
    out=[];n=0;inb=False
    for l in kn.split('\n'):
        isb=l.startswith('> ') and not l.startswith('> *')
        if isb and not inb: n+=1; out.append(f'«b{n}»')
        inb=isb; out.append(l)
    return '\n'.join(out),n
def mandalas(cfg): return cfg.d.get('mandalas') or [cfg.mandala,cfg.mandala+1]
def cmd_prep(a,quiet=False,after=None):
    """after=P: prepare the window that follows printed p. P whatever the progress note says (batch runs prepare many windows ahead; no English context then)"""
    cfg=rvlib.Cfg(a[0]); heads={}; src=cfg.source_pages(heads)
    if src is None: sys.exit('volcfg.json has no "source": this workflow needs the supplied text (use the older scan workflow only for volumes without one)')
    dp,dpdf=position(cfg)
    if after is not None: dp,dpdf=after,None
    pages=next_pages(cfg,dp,dpdf,src); w=os.path.join(cfg.work,f'w{pages[0][0]:04d}'); os.makedirs(w,exist_ok=True)
    specs=[os.path.join(ROOT,x.split('@')[0])+('@'+x.split('@')[1] if '@' in x else '') for x in cfg.source]
    kn,sec=html_to_kn.kn_pages(specs,[p for p,_ in pages],None,mandalas(cfg))        # section/verse at the window start: found by the script itself (no state file)
    notes=list(html_to_kn.LOG); extra=list(html_to_kn.EXTRA)
    pages=sorted(set(pages)|{(p,None) for p in extra},key=lambda x:x[0])
    wr(os.path.join(w,'kn.md'),kn); wr(os.path.join(w,'section_end.txt'),sec or ''); wr(os.path.join(w,'section_start.txt'),html_to_kn.START[0] or '')
    rows=numerals.load(cfg) if cfg.numeral_files() else []; info=[]; nrows=[]
    for pr,g in pages:
        rs=numerals.rows_for(cfg,rows,g) if g and rows else []
        info.append(dict(printed=pr,pdf=g if rows else None,file_page=cfg.file_page(g) if g and rows else None,numeral_rows=len(rs)))
        nrows.append(f'== printed {pr}: {len(rs)} rows\n'+'\n'.join(f"  line {r['line']} | {r['kn']} | {r['en']} | {r['ctx'][:100]}" for r in rs))
    wr(os.path.join(w,'pages.json'),json.dumps(info,indent=1))
    if rows: wr(os.path.join(w,'numerals.txt'),'\n'.join(nrows)+'\n')                 # only when the user supplied a numeral file
    rel=os.path.relpath(w,ROOT); en=rd(cfg.en); i=en.rfind('**Progress note:**'); body=en[:i].rstrip('\n').rstrip('-').rstrip('\n') if i>=0 else en
    tail='…'+body[-900:] if after is None else '(prepared ahead: the English of the pages before this window is not available; the Kannada lines below show where the text stands)'; prev=[p for p in sorted(src) if p<pages[0][0]][-1:]
    pk=''
    if prev:
        t,_=html_to_kn.kn_pages(specs,prev,None,mandalas(cfg),warm=6); pk='\n'.join([l for l in t.split('\n') if l.strip()][-5:]); html_to_kn.LOG[:]=notes
    view,nb=numbered(kn); med=sorted(len(v) for v in src.values())[len(src)//2]
    long_=[p for p,_ in pages if p in src and len(src[p])>1.7*med]
    if long_: notes.append(f'pages much longer than usual ({long_}): a running head may be missing inside (insert "<!-- printed N -->" + the head line in kn.md, "### Printed p. N" in en.md, and append the page to pages.json)')
    task=f"""# Window {rel}: printed pp. {pages[0][0]}-{pages[-1][0]} of Vol {cfg.vol}   (rules: tools/rv/BRIEF.md)

Write `{rel}/en.md`, then run:  python3 tools/rv/batch.py done {cfg.vol} {rel} --note "what the window covers"
Page headings needed in en.md: {', '.join(f'### Printed p. {p}' for p,_ in pages)}.  Sanskrit blocks to place: [[b1]] … [[b{nb}]] (each exactly once, alone on its line).

## What the script already did to kn.md (check it; mention garbled labels / inserted markers only if something is still wrong)
{chr(10).join('- '+n for n in notes) or '- nothing special'}

## Context, already translated — do NOT translate again (end of the English file, then the last Kannada lines before this window)
{tail}

{pk}

## kn.md of this window («bN» = number of the Sanskrit block that follows; the marks are not in kn.md itself)
{view}
"""
    wr(os.path.join(w,'TASK.md'),task); wr(os.path.join(w,'PROMPT.txt'),f'Read {rel}/TASK.md and do the window (rules: tools/rv/BRIEF.md).\n')
    miss=[p for p,_ in pages if p not in src and p not in extra]
    if not quiet:
        print(w); print('pages:',[p for p,_ in pages],'| blocks:',nb,'| script notes:',len(notes))
        if miss: print('WARNING: not in the supplied text:',miss)
    return w,pages,notes
def cmd_build(a):
    cfg=rvlib.Cfg(a[0]); w=a[1]; kn=rd(os.path.join(w,'kn.md')); en=rd(os.path.join(w,'en.md'))
    if re.search(r'^> \*',en,re.M): sys.exit("FAIL: IAST typed by hand in en.md ('> *' lines): IAST is added by script")
    if cfg.d.get('layout')=='subheads' and not os.environ.get('RV_REBUILD'):      # a sūkta heading the volume already has (written where Sāyaṇa's introduction began, in an earlier window) is not written again
        have=set(re.findall(r'(?m)^## Sūkta \d+ \(Maṇḍala \d+\)',rd(cfg.en))); keep=[]
        for l in en.split('\n'):
            h=l.strip() if re.fullmatch(r'## Sūkta \d+ \(Maṇḍala \d+\)\s*',l) else None
            if h and h in have: print('heading dropped (the volume has it already):',h); continue
            if h: have.add(h)
            keep.append(l)
        en='\n'.join(keep); wr(os.path.join(w,'en.md'),en)
    notes=[]
    if note_style(cfg): en,notes=split_notes(en)
    wr(os.path.join(w,'notes.json'),json.dumps(notes,ensure_ascii=False,indent=1))
    sp=os.path.join(w,'section_start.txt'); start=(rd(sp).strip() or None) if os.path.exists(sp) else None
    text,prob=convert.expand(en,kn,plain=tuple(cfg.d.get('no_iast_blocks',[])),start=start)
    if convert.RESTORED: print('labels put in or normalised by script:'); print('\n'.join(' - '+x for x in convert.RESTORED)); wr(os.path.join(w,'labels_restored.txt'),'\n'.join(convert.RESTORED)+'\n')
    wr(os.path.join(w,'markers_fuzzy.tsv'),''.join(f'{a_}\t{b_}\n' for a_,b_ in convert.FUZZY))      # quotation markers resolved approximately (for a spot check)
    if prob: print('PROBLEMS:'); print('\n'.join(' - '+p for p in prob)); sys.exit(1)
    p=os.path.join(w,'en_final.md'); wr(p,text)
    r=sh(f'python3 publish/tools/translit/add_iast.py "{p}"'); print('add_iast:',(r.stdout+r.stderr).strip()[-200:])
    t=labels.normalise(rd(p)).replace(convert.NOIAST,'> ')
    if cfg.d.get('layout')=='subheads': t,_=rk_headings(subheads(t))
    lab=cfg.d.get('printed_english_label')                 # the heading of the English printed in the edition (volcfg), e.g. 'English translation (H. H. Wilson)'
    if lab: t=re.sub(r'(?m)^(\*\*|##### )Printed English( translation)?(\*\*)?\s*$',lambda m:('##### '+lab) if m.group(1).startswith('#') else '**'+lab+'**',t)
    wr(p,t)
    r=sh(f'python3 publish/tools/accents/accent_volume.py {cfg.vol} --file "{p}" --write'); print('accents:',[l for l in (r.stdout+r.stderr).split('\n') if l.startswith('Vol') or 'not matched' in l or 'Error' in l or 'Trace' in l])
    rep=os.path.join(ROOT,f'vol{cfg.vol}','review','accent_report.tsv')                     # the accent step rewrites its report every time: keep a cumulative copy (Vol 16 lesson 35)
    if os.path.exists(rep):
        rows=[l for l in rd(rep).split('\n')[1:] if l.strip()]; cum=rep.replace('.tsv','_cumulative.tsv'); tag=os.path.basename(w.rstrip('/'))
        old=[l for l in (rd(cum).split('\n') if os.path.exists(cum) else []) if l.strip() and not l.startswith(tag+'\t')]
        wr(cum,'\n'.join(old+[tag+'\t'+r for r in rows])+'\n')
    wr(os.path.join(w,'kn_final.md'),convert.kn_final(kn)); print('built',p,os.path.join(w,'kn_final.md'))
def doubts(text): return [(i,l.strip()[:110]) for i,l in enumerate(text.split('\n'),1) if '[?]' in l]
def cmd_check(a):
    cfg=rvlib.Cfg(a[0]); w=a[1]; mx=int(a[a.index('--max-doubts')+1]) if '--max-doubts' in a else 0
    pg=json.load(open(os.path.join(w,'pages.json'))); kn=rd(os.path.join(w,'kn.md')); en=rd(os.path.join(w,'en.md')); fail=[]
    fe=os.path.join(w,'en_final.md')
    if not os.path.exists(fe): sys.exit('run build first')
    enf=rd(fe)
    for p in pg:
        if not re.search(rf"<!-- printed {p['printed']}[ :]",kn) and not (p.get('pdf') and re.search(rf"<!-- PDF {p['pdf']} ·",kn)): fail.append(f"kn.md has no page marker for printed p. {p['printed']}")
        if not re.search(rf"### Printed p\. {p['printed']}\b",en): fail.append(f"en.md has no heading '### Printed p. {p['printed']}'")
    if note_style(cfg):
        raw=en; en=split_notes(en)[0]
        if raw.count('**NOTE**')!=len(NOTE_RE.findall(raw)): fail.append('a **NOTE** without its {detail}: write **NOTE**{what is doubtful, with the Kannada words}')
        for pat,msg in ((r'\[\?\]|\[sic\]','[?] / [sic] are not used any more: mark the place **NOTE**{detail}'),
                        (r'(?m)^\*\[|\*\[[^\]]*\]\*','translator remarks in italic brackets *[…]* are not written into the English text: drop them, or use **NOTE**{detail} where a decision is needed'),
                        (r'(?i)\bas supplied|\bas printed|running head','no remarks such as "as supplied" / "Running head" in the English text (the Kannada file keeps the heads and stray lines)')):
            if re.search(pat,en): fail.append(msg)
        kk=re.findall('[ಀ-೿]+',enf)
        if kk: fail.append(f'{len(kk)} Kannada-script words left in the English text (e.g. {kk[0]}): Sanskrit goes inside ⟦ ⟧ (the script converts it), a reference abbreviation is written in Latin letters (BRIEF.md table), a Kannada word is translated; Kannada letters may stand only inside **NOTE**{{…}}')
    dk,de=doubts(kn),doubts(enf)
    if len(dk)+len(de)>mx: fail.append(f'[?] left: {len(dk)} in kn.md, {len(de)} in en.md (allowed {mx})')
    knr=re.sub(r'(?<=[೦-೯0-9])_(?=[೦-೯0-9])','-',kn); knr=re.sub(r'(?<=-[೦-೯0-9]) (?=[೦-೯0-9]{1,3}-[೦-೯0-9])','-',knr)   # … and a space for it inside a reference (೧೦-೫ ೪-೧೪)          # the machine reader sometimes gives '_' for the hyphen of a reference (ನಿ. ೧೦_೮): same reference for the twin check
    pdfs=[p['pdf'] for p in pg if p.get('pdf')]; knr=kn+'\n'+knr      # both forms count as twins (the loosened form must never hide a reference that matched as printed)
    res=numerals.check(cfg,pdfs,knr,en) if cfg.numeral_files() else numerals.check(cfg,[],knr,en,rows=[])
    print(numerals.report(res))
    if res['near']: fail.append(f"{len(res['near'])} numerals differ from the numeral file by 1-2 characters (the file is the reference: correct kn.md, or tell the user)")
    if note_style(cfg):                                  # a reference that carries a **NOTE** about itself is settled (the editor decides), and so is one whose numbers are a printed reference in other punctuation
        det=' '.join(d for _,d,_ in split_notes(raw)[1]); groups=[k.split('-') for k in set(numerals.refs_kn(knr))|set(numerals.refs_en(knr))]
        sub=lambda r:(lambda g:any(k[i:i+len(g)]==g for k in groups for i in range(len(k)-len(g)+1)) or any(''.join(k)==''.join(g) for k in groups))(r.split('-'))
        res['twin_bad']=[r for r in res['twin_bad'] if ('reference '+r) not in det and not sub(r)]
    if res['twin_bad']: fail.append(f"English references without Kannada twin: {res['twin_bad']}")
    if res['missing']: fail.append(f"{len(res['missing'])} numeral-file rows have no counterpart in the Kannada text")
    if re.search(r'\[\[b\d+\]\]',enf): fail.append('unresolved [[bN]] in en_final.md')
    if '⟪' in enf or '⟫' in enf: fail.append('unbalanced ⟪ ⟫ in en.md')
    if cfg.d.get('grammar')=='sanskrit' and re.search(r'\*\*Grammar\*\*',en) and '⟪' not in en: fail.append('the Grammar section is written in Sanskrit inside ⟪ ⟫ (Kannada script), one word per line: see BRIEF.md')
    if re.search('['+chr(0x0900)+'-'+chr(0x0963)+chr(0x0966)+'-'+chr(0x097F)+']',convert.kn_final(kn)): fail.append('Devanagari in kn.md (the Kannada file is Kannada script only; danda marks are allowed)')
    bad=check_inline.mismatches(w)
    if bad: fail.append(f'{len(bad)} inline ⟦…⟧ segment(s) are not in kn.md (copy them from kn.md, never retype): '+' | '.join(x[:40] for x in bad[:6]))
    if PLACEHOLDER.search(en) or PLACEHOLDER.search(enf): fail.append('placeholder XXX left in en.md')
    dv=re.findall('[ऄ-ह][ऀ-ॣ]*',en)
    if dv: fail.append(f'Devanagari typed in en.md ({len(dv)} places, e.g. {dv[0]}): Sanskrit is copied from kn.md in Kannada script inside ⟦ ⟧; the script converts')
    if re.search(r'⟧\s*\(\*(?!\*)[^)]*(?<!\*)\*\)',en): fail.append('hand IAST "(*…*)" after a ⟦ ⟧ segment in en.md: the build adds the IAST itself (Vol 16: 116 doubled pairs)')
    if re.search(r'\(\*([^)]{2,})\*\) \(\*\1\*\)',enf): fail.append('doubled IAST "(*x*) (*x*)" in en_final.md')
    for sec in re.findall(r'\*\*Pratipadārtha\*\*\n(.*?)(?=\n\*\*|\n#|\Z)',en,re.S):
        if sec.count('—')>=3 and '⟦' not in sec: fail.append('a Pratipadārtha has no ⟦ ⟧ headwords (the Sanskrit words are copied from kn.md inside ⟦ ⟧, not written in Latin letters)'); break
    acc=[l[:60] for l in enf.split('\n') if l.startswith('> ') and re.search('([१३])[॒॑]+\\1|्[॒॑]|[॒॑][ा-ौ]',l)]
    if acc: print('ACCENT WARNING (doubled pluta digit / mark at a virama or before a vowel sign; logged, do not hand-edit):',acc[:3]); open(os.path.join(ROOT,f'vol{cfg.vol}','review','accent_flags.tsv'),'a',encoding='utf8').write(''.join(f"{os.path.basename(w)}\t{x}\n" for x in acc))
    if re.search(r'⟦\s*⟧|⟦\s*\(\*\s*\*\)\s*⟧',enf): fail.append('empty inline segment ⟦ ⟧ in en.md')
    if re.search(r'\*\*Progress note',en): fail.append('en.md must not contain a Progress note (the script writes it)')
    if '[figure' in kn: fail.append('kn.md still has a [figure: …] line: read the picture, write the block into kn.md, remove the line (BRIEF.md)')
    for m in re.findall(r'<!-- printed (\d+)',kn):
        if int(m) not in [p['printed'] for p in pg]: fail.append(f'kn.md has a marker for printed p. {m} that is not in pages.json (append it there and add "### Printed p. {m}" to en.md)')
    hs=re.findall(r'(?m)^## Sūkta \d+ \(Maṇḍala \d+\)',enf); done_en=rd(cfg.en)
    for h in sorted(set(hs)):
        if hs.count(h)>1 or (h in done_en and not os.environ.get('RV_REBUILD')): fail.append(f'the heading "{h}" would stand twice (it is written once, where the sūkta begins)')
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
    if re.match(r'\s*Done through',note): sys.exit('FAIL: the note must not start with "Done through" (the script writes the position)')
    r=sh(f'python3 tools/rv/batch.py check {cfg.vol} "{w}" --max-doubts {mx}'); print(r.stdout[-1500:])
    if r.returncode: sys.exit('check failed: nothing appended')
    if cfg.branch and '--no-git' not in a:
        cur=sh('git rev-parse --abbrev-ref HEAD').stdout.strip()
        if cur!=cfg.branch and cur not in cfg.d.get('branches',[]) and not os.environ.get('ALLOW_OTHER_BRANCH'): sys.exit(f'STOP: on branch {cur!r}, Vol {cfg.vol} belongs on {cfg.branch!r}')
    pg=json.load(open(os.path.join(w,'pages.json'))); last=max(pg,key=lambda x:x['printed']); pg=sorted(pg,key=lambda x:x['printed']); enf=rd(os.path.join(w,'en_final.md')).rstrip('\n'); knf=rd(os.path.join(w,'kn_final.md')).strip()   # last = highest printed page, even if a merged head was appended to pages.json out of order (Vol 12 w0159)
    s=rd(cfg.en); n0=len(s); i=s.rfind('**Progress note:**')
    if i>=0:
        assert i>len(s)-20000,'progress note not near the end'; s=s[:i].rstrip('\n').rstrip('-').rstrip('\n')
    pdf=f" (PDF {last['pdf']})" if last.get('pdf') else ''
    s=s+'\n\n'+enf+f"\n\n---\n\n**Progress note:** Done through printed p. {last['printed']}{pdf}. {note}\n"
    s=mandala_heading(s,cfg,knf)
    if cfg.d.get('layout')=='subheads': s,_=rk_headings(s)      # whole file: a Ṛk that continues over the window boundary gets '(continued)' (Vol 18 w0076, w0101)
    k=rd(cfg.kn); assert not re.search(rf"<!-- printed {pg[0]['printed']}[ :]",k),'Kannada file already has this window'      # checked BEFORE the English is written
    assert s.count('**Progress note:**')==1 and len(s)>=n0-2000; wr(cfg.en,s)
    wr(cfg.kn,k.rstrip('\n')+'\n\n'+knf+'\n')
    sec=rd(os.path.join(w,'section_end.txt')).strip() if os.path.exists(os.path.join(w,'section_end.txt')) else ''
    os.makedirs(cfg.work,exist_ok=True); wr(state_path(cfg),json.dumps({'section':sec or None,'printed':last['printed']}))
    rng=f"printed pp. {pg[0]['printed']}-{last['printed']}"
    nj=os.path.join(w,'notes.json')
    if note_style(cfg) and os.path.exists(nj):
        nt=json.load(open(nj,encoding='utf8')); nf=os.path.join(ROOT,f'vol{cfg.vol}','review','notes.tsv'); os.makedirs(os.path.dirname(nf),exist_ok=True)
        new=not os.path.exists(nf)
        with open(nf,'a',encoding='utf8') as f:
            if new: f.write('window\tprinted page\tquestion (what needs a decision or a second look)\twords before the mark in the English text\tdecision\n')
            for pgn,det,ctx in nt: f.write(f"{os.path.basename(w.rstrip('/'))}\t{pgn}\t{det}\t{ctx}\t\n")
    dl=[(rng,'kn',i,t) for i,t in doubts(rd(os.path.join(w,'kn.md')))]+[(rng,'en',i,t) for i,t in doubts(enf)]
    if dl:
        os.makedirs(os.path.join(ROOT,f'vol{cfg.vol}','review'),exist_ok=True)
        with open(os.path.join(ROOT,f'vol{cfg.vol}','review','doubts.tsv'),'a',encoding='utf8') as f:
            for x in dl: f.write('\t'.join(map(str,x))+'\n')
    print('appended to',os.path.relpath(cfg.en,ROOT),'and',os.path.relpath(cfg.kn,ROOT),f'; {len(dl)} doubts logged')
    if '--no-git' not in a:
        co=os.environ.get('RV_COAUTHOR') or cfg.d.get('coauthor') or 'Claude <noreply@anthropic.com>'
        r=sh(f'git add "vol{cfg.vol}" && git commit -qm "Vol {cfg.vol}: {rng}" -m "Co-Authored-By: {co}" && git push -q origin HEAD'); print('git:',(r.stdout+r.stderr).strip()[-200:] or 'pushed')

def audit(cfg,expect_clean=True):
    """invariants of the volume files and of git; returns (problems, facts)"""
    en=rd(cfg.en); kn=rd(cfg.kn); pr=[]; dp,_=position(cfg)
    if en.count('**Progress note:**')!=1: pr.append(f"{en.count('**Progress note:**')} progress notes in the English file (must be 1)")
    if PLACEHOLDER.search(en): pr.append('XXX in the English file')
    hs=re.findall(r'(?m)^## Sūkta \d+ \(Maṇḍala \d+\)',en); dup=sorted({h for h in hs if hs.count(h)>1})
    if dup: pr.append('sūkta heading more than once: '+', '.join(dup))
    if re.search(r'⟦\s*⟧|⟦\s*\(\*\s*\*\)\s*⟧',en): pr.append('empty ⟦ ⟧ in the English file')
    if re.search('['+chr(0x0900)+'-'+chr(0x0963)+chr(0x0966)+'-'+chr(0x097F)+']',kn): pr.append('Devanagari in the Kannada file')
    pe=[int(x) for x in re.findall(r'^### Printed p\. (\d+)',en,re.M)]; pk=[int(x) for x in re.findall(r'<!-- printed (\d+)',kn)]
    if set(pe)!=set(pk): pr.append(f'page marks differ between the files: only English {sorted(set(pe)-set(pk))[:8]}, only Kannada {sorted(set(pk)-set(pe))[:8]}')
    if pe and max(pe)!=dp: pr.append(f'progress note says p. {dp} but the last page heading is p. {max(pe)}')
    q=lambda t:t.count('[?]')-t.count('`[?]`')
    if q(en)!=q(kn): pr.append(f"[?] counts differ: English {q(en)}, Kannada {q(kn)}")
    if note_style(cfg):
        nf=os.path.join(ROOT,f'vol{cfg.vol}','review','notes.tsv'); rows=max(0,len([l for l in rd(nf).split('\n') if l.strip()])-1) if os.path.exists(nf) else 0
        if en.count('**NOTE**')!=rows: pr.append(f"{en.count('**NOTE**')} **NOTE** marks in the English file but {rows} rows in review/notes.tsv")
    if cfg.d.get('layout')=='subheads':
        miss=len(rk_headings(en)[1])
        a_,b_=kn.count('*ಸಂಹಿತಾಪಾಠಃ*'),len(re.findall(r'(?m)^##### ॥ संहितापाठः ॥',en))
        if a_!=b_: pr.append(f'{a_} Saṃhitā labels in the Kannada file but {b_} Saṃhitā sub-headings in the English file (a verse placed without its labels?)')
        odd=[h for h in re.findall(r'(?m)^## .*',en) if not h.startswith(('## Sūkta','## Maṇḍala','## Preface'))]
        if odd: pr.append('chapter-level heading that is neither a sūkta, a maṇḍala nor the preface: '+'; '.join(odd[:4]))
        if miss: pr.append(f'{miss} Ṛk headings missing, misplaced, unnumbered or repeated (python3 tools/rv/batch.py rkheads {cfg.vol})')
    st=sh('git status -sb').stdout.split('\n'); dirty=[l for l in st[1:] if l.strip() and f'vol{cfg.vol}/' in l and '/work/' not in l]
    if expect_clean and dirty: pr.append('uncommitted changes: '+'; '.join(dirty[:4]))
    if 'ahead' in st[0]: pr.append('commits not pushed: '+st[0])
    return pr,dict(page=dp,pages=len(pe),doubts=q(en),head=sh('git log -1 --oneline').stdout.strip())
def mandala_heading(s,cfg,kn=''):
    """The windows do not write `## Maṇḍala M` (Vol 17 and Vol 18, lesson 52): put it before a new maṇḍala's introduction (a `## …` heading that is not a
    sūkta/maṇḍala/preface heading, standing after the last `## Sūkta` of the previous maṇḍala; the heading is lowered to `###`), or else before `## Sūkta 1 (Maṇḍala M)`.
    M comes from `mandalas` in volcfg.json (the maṇḍala after the last one seen).  Nothing happens when `## Maṇḍala M` is there."""
    ms=cfg.d.get('mandalas') or []
    for m in ms[1:]:
        if f'\n## Maṇḍala {m}\n' in s: continue
        i=s.find(f'\n## Sūkta 1 (Maṇḍala {m})\n')
        prev=ms[ms.index(m)-1]; j=s.rfind(f'\n## Sūkta ')
        odd=None
        if f'(Maṇḍala {prev})' in s[j:j+80] or i<0:
            mm=re.search(r'(?m)^## (?!Sūkta|Maṇḍala|Preface)([^\n]+)$',s[j+1:]) if j>=0 else None
            if mm and i<0 and f'(Maṇḍala {prev})' in s[j:j+80] and 'ಮಂಡಲವು ಸಮಾಪ್ತ' in kn: odd=j+1+mm.start()      # only in a window whose Kannada says the maṇḍala ends
        if odd is not None:
            s=s[:odd]+f'## Maṇḍala {m}\n\n### '+s[odd+3:]
        elif i>=0: s=s[:i+1]+f'## Maṇḍala {m}\n\n'+s[i+1:]
    return s
def cmd_audit(a):
    cfg=rvlib.Cfg(a[0]); pr,f=audit(cfg); print(f"Vol {cfg.vol}: done through printed p. {f['page']} ({f['pages']} page headings, {f['doubts']} [?]); HEAD {f['head']}")
    print('AUDIT FAIL:\n - '+'\n - '.join(pr) if pr else 'AUDIT PASS'); sys.exit(1 if pr else 0)
def cmd_rkheads(a):
    """repair of the volume file: Ṛk headings left out, misplaced, unnumbered or repeated by the translator (logged in review/repair_log.md)"""
    cfg=rvlib.Cfg(a[0]); t,ch=rk_headings(rd(cfg.en))
    if not ch: print('nothing to change'); return
    import collections; c=collections.Counter(k for k,_ in ch)
    for k,v in ch:
        if k!='added': print(k,v)
    print('added:',[v for k,v in ch if k=='added'])
    if '--dry-run' in a: return
    wr(cfg.en,t); open(os.path.join(ROOT,f'vol{cfg.vol}','review','repair_log.md'),'a',encoding='utf8').write(f"- Ṛk headings (`batch.py rkheads`): {c['added']} put in where a Saṃhitā block stood without `#### Ṛk N` (number from the verse number at the end of the Saṃhitā or Pada block, else by sequence); {c['order']} moved before the Saṃhitā label; {c['number']} given or corrected a number: {'; '.join(v for k,v in ch if k=='number')}; {c['continued']} repeated headings marked '(continued)'. No other text changed.\n")
    print(dict(c))
def cmd_view(a): print(numbered(rd(os.path.join(a[1],'kn.md')))[0])
def cmd_done(a):
    """build + check (+ inline and placeholder gates) + commit + push + self-verification: the translator's single command"""
    cfg=rvlib.Cfg(a[0]); w=a[1].rstrip('/'); note=a[a.index('--note')+1] if '--note' in a else ''; mx=a[a.index('--max-doubts')+1] if '--max-doubts' in a else '0'
    if not note and '--dry-run' not in a: sys.exit('give --note "what the window covers"')
    r=sh(f'python3 tools/rv/batch.py build {cfg.vol} "{w}"')
    if r.returncode: print('BUILD FAIL\n'+(r.stdout+r.stderr).strip()[-1500:]); sys.exit(1)
    acc=[l for l in r.stdout.split('\n') if l.startswith('accents:')]
    r=sh(f'python3 tools/rv/batch.py check {cfg.vol} "{w}" --max-doubts {mx}')
    if r.returncode: print('CHECK '+r.stdout[r.stdout.rfind('FAIL'):].strip()[:1800]+'\nNothing was appended. Fix en.md / kn.md (batch.py fix …) and run done again.'); sys.exit(1)
    print('gates: PASS |',(acc[0][:160] if acc else 'accents: n/a'))
    if '--dry-run' in a: print('dry run: nothing appended'); return
    extra=' --no-git' if '--no-git' in a else ''
    r=sh(f'python3 tools/rv/batch.py commit {cfg.vol} "{w}" --note "{note.replace(chr(34),chr(39))}" --max-doubts {mx}{extra}')
    out=(r.stdout+r.stderr).strip()
    if r.returncode or 'appended to' not in out: print('COMMIT FAIL\n'+out[-1200:]); sys.exit(1)
    pr,f=audit(cfg,expect_clean=not extra); pg=json.load(open(os.path.join(w,'pages.json'))); last=max(p['printed'] for p in pg)
    if f['page']!=last: pr.append(f"progress note is at p. {f['page']}, window ends at p. {last}")
    if not extra and f'Vol {cfg.vol}: printed pp.' not in f['head']: pr.append('HEAD is not this window\'s commit: '+f['head'])
    print(f"DONE through printed p. {f['page']} | {f['head']} | {'pushed' if not extra else 'no git'}")
    if pr: print('VERIFY FAIL:\n - '+'\n - '.join(pr)); sys.exit(1)
    print('VERIFIED: one progress note, no XXX, no empty ⟦⟧, page marks equal in both files, pushed. Report in <= 4 lines.')
def cmd_next(a):
    """dispatcher: audit, log the cost of the window just done, prep the next window, print the message for the translator"""
    cfg=rvlib.Cfg(a[0]); opt=lambda k:a[a.index(k)+1] if k in a else 'n/a'
    pr,f=audit(cfg,expect_clean=False)
    if pr: print('AUDIT FAIL (fix before the next window):\n - '+'\n - '.join(pr)); sys.exit(1)
    cost=os.path.join(ROOT,f'vol{cfg.vol}','parts','batch_costs.md'); os.makedirs(os.path.dirname(cost),exist_ok=True)
    if '--tokens' in a or '--tools' in a or '--min' in a:
        open(cost,'a',encoding='utf8').write(f"| through p. {f['page']} | {opt('--model') if '--model' in a else 'sonnet'} | {opt('--tools')} | {opt('--tokens')} | {opt('--min')} |\n")   # committed with the next window (commit adds volN/)
    try: w,pages,notes=cmd_prep([a[0]],quiet=True)
    except SystemExit as e: print(f"Vol {cfg.vol}: done through printed p. {f['page']}; no further window: {e}"); return
    rel=os.path.relpath(w,ROOT)
    print(f"audit PASS | done through p. {f['page']} | {f['doubts']} [?] | next window {rel} (pp. {pages[0][0]}-{pages[-1][0]}, {len(notes)} script notes)")
    print(f'MESSAGE: Window {rel}: read {rel}/TASK.md, write {rel}/en.md, run `python3 tools/rv/batch.py done {cfg.vol} {rel} --note "…"` until it prints VERIFIED; report in <= 4 lines (last line of `done`, hand-fixes, doubts).')
CMDS=dict(new=cmd_new,prep=cmd_prep,build=cmd_build,check=cmd_check,zoomlist=cmd_zoomlist,fix=cmd_fix,commit=cmd_commit,done=cmd_done,next=cmd_next,audit=cmd_audit,view=cmd_view,rkheads=cmd_rkheads)
if __name__=='__main__':
    if len(sys.argv)<3 or sys.argv[1] not in CMDS: sys.exit(__doc__)
    CMDS[sys.argv[1]](sys.argv[2:])
