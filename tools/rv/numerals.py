"""The user's numeral file (xlsx) for a volume: rows per page, and the checks used by batch.py.

  python3 tools/rv/numerals.py VOL PDFPAGE [PDFPAGE ...]        rows for those PDF pages (file page from volcfg 'numerals.file_page')
  python3 tools/rv/numerals.py check VOL WINDOWDIR              compare the window's Kannada and English references with the file

Columns are found by header name (page / line / kannada / english|equivalent / context|raw); if the headers are not recognised the old layout is assumed:
Page | Line | Kannada pattern | English digits | Raw context. A new Kannada-numerals column is picked up automatically if its header contains 'kannada'.
Only references with separators (6-1-163, 4.5.6) are in the file; plain numbers are never checked here."""
import os,re,sys,glob,json
sys.path.insert(0,os.path.dirname(__file__)); import rvlib
KD=str.maketrans('೦೧೨೩೪೫೬೭೮೯','0123456789')
KN_REF=re.compile(r'[೦-೯]+(?:\s*[-.:–]\s*[೦-೯]+)+')
EN_REF=re.compile(r'(?<![\d.])\d+(?:[-.]\d+)+(?![\d])')
def norm(s): return re.sub(r'\s*[-.:–]\s*','-',s.translate(KD).strip())
def load(cfg):
    import openpyxl; rows=[]
    for f in cfg.numeral_files():
        ws=openpyxl.load_workbook(f,read_only=True).active; it=ws.iter_rows(values_only=True); hdr=next(it)
        h=[str(x or '').lower() for x in hdr]; col={}
        for i,x in enumerate(h):
            for key,pat in (('page','page'),('line','line'),('kn','kannada'),('en','english|equivalent'),('ctx','context|raw')):
                if key not in col and re.search(pat,x): col[key]=i
        if not {'page','en'}<=set(col): col={'page':0,'line':1,'kn':2,'en':3,'ctx':4}
        for r in it:
            if r[col['page']] is None: continue
            g=lambda k:r[col[k]] if k in col and col[k]<len(r) else None
            try: pg=int(g('page'))
            except Exception: continue
            en=norm(str(g('en') or '')) or norm(str(g('kn') or ''))
            rows.append(dict(page=pg,line=g('line'),kn=str(g('kn') or ''),en=en,ctx=str(g('ctx') or ''),file=os.path.basename(f)))
    return rows
def rows_for(cfg,rows,pdf): fp=cfg.file_page(pdf); return [r for r in rows if r['page']==fp]
def lev(a,b):
    p=list(range(len(b)+1))
    for i,x in enumerate(a,1):
        c=[i]
        for j,y in enumerate(b,1): c.append(min(p[j]+1,c[j-1]+1,p[j-1]+(x!=y)))
        p=c
    return p[-1]
def refs_kn(t): return [norm(m.group()) for m in KN_REF.finditer(t)]
def refs_en(t): return [norm(m.group()) for m in EN_REF.finditer(t)]
def check(cfg,pdfs,kn_text,en_text,rows=None):
    """returns dict: match, near (probable misreads), missing (file rows not in the Kannada text), extra_kn (refs the file does not list),
    twin_bad (English refs with no Kannada counterpart), twin_info (Kannada refs not found in English)"""
    rows=rows if rows is not None else load(cfg); fr=[r for p in pdfs for r in rows_for(cfg,rows,p)]
    kn=refs_kn(kn_text); en=refs_en(en_text); left=list(kn); res=dict(match=[],near=[],missing=[],extra_kn=[],twin_bad=[],twin_info=[])
    for r in fr:
        if not r['en']: continue
        if r['en'] in left: left.remove(r['en']); res['match'].append(r['en']); continue
        c=[(lev(r['en'],k),k) for k in left]; c=[x for x in c if x[0]<=2 and abs(len(x[1])-len(r['en']))<=1]
        if c: d,k=min(c); left.remove(k); res['near'].append((r['en'],k,r['page'],r['line']))
        else: res['missing'].append((r['en'],r['page'],r['line'],r['ctx'][:60]))
    res['extra_kn']=left
    kset=set(kn)|set(refs_en(kn_text))   # Latin-digit references printed inside English quotations of the Kannada text are their own twins (fix Nov 9 2026)
    res['twin_bad']=[e for e in en if e not in kset]; eset=set(en); res['twin_info']=[k for k in kn if k not in eset]
    return res
def report(res):
    L=[f"file references matched exactly in the Kannada text: {len(res['match'])}"]
    L.append(f"NEAR (file value differs from the Kannada text by 1-2 characters; one of them is a misread, fix it or justify): {len(res['near'])}")
    L+= [f"   file {a}  |  Kannada text {b}   (file page {p}, line {l})" for a,b,p,l in res['near']]
    L.append(f"file rows with no counterpart in the Kannada text (omitted or badly misread): {len(res['missing'])}")
    L+= [f"   {a}  (file page {p}, line {l})  context: {c}" for a,p,l,c in res['missing']]
    L.append(f"Kannada references the file does not list (information): {len(res['extra_kn'])} {res['extra_kn'][:12]}")
    L.append(f"English references with NO Kannada counterpart (twin mismatch): {len(res['twin_bad'])} {res['twin_bad']}")
    L.append(f"Kannada references not found in the English (information): {len(res['twin_info'])} {res['twin_info'][:12]}")
    return '\n'.join(L)
def ok(res): return not res['near'] and not res['twin_bad'] and not res['missing']
if __name__=='__main__':
    a=sys.argv[1:]
    if a and a[0]=='check':
        cfg=rvlib.Cfg(a[1]); w=a[2]; pg=json.load(open(os.path.join(w,'pages.json')))
        kn=open(os.path.join(w,'kn.md'),encoding='utf8').read(); en=open(os.path.join(w,'en.md'),encoding='utf8').read()
        r=check(cfg,[p['pdf'] for p in pg],kn,en); print(report(r)); sys.exit(0 if ok(r) else 1)
    cfg=rvlib.Cfg(a[0]); rows=load(cfg)
    for g in map(int,a[1:]):
        rs=rows_for(cfg,rows,g); print(f'== PDF {g} (printed {cfg.printed(g)}, file page {cfg.file_page(g)}): {len(rs)} rows')
        for r in rs: print(f"  line {r['line']} | {r['kn']} | {r['en']} | {r['ctx'][:100]}")
