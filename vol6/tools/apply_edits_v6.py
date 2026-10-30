"""Apply reviewed Pariśiṣṭa reference readings (ids 'PRINTEDPAGE_GROUPINDEX: value') to the Vol 6 English file.
python3 apply_edits_v6.py EDITS.txt JSON [--write]   JSON = the review JSON of that batch (rows: id, file).
Each edit replaces the file's group (same regex and index as build_review_v6.py). Applied only if the group's current text equals
the row's 'file' value. 'x' = wrong crop -> skipped; empty value -> skipped. A reading that changes a digit segment the file had
(not '?') is applied (the user's reading wins) but listed as CHANGED. Page text is edited from the end backwards."""
import sys,re,json,os
sys.path.insert(0,os.path.dirname(__file__))
from cfg import EN
E=open(sys.argv[1],encoding='utf8').read().splitlines(); J=json.load(open(sys.argv[2])); W='--write' in sys.argv
BASE=sys.argv[sys.argv.index('--base')+1] if '--base' in sys.argv else None   # commit whose text the row indices refer to (use when earlier edits changed the group count)
import difflib,subprocess
rows={r['id']:r for r in J['rows']}
for u in J.get('unmatched',[]):
    if 'j' in u: rows.setdefault(f"{u['printed']}_{u['j']}",dict(file=u['file']))   # references that had no crop (page bands)
SEG=r'(?:\d{1,4}|\[\?\]|\?)'
GRP=re.compile(r'(?<![\w.\-,])((?:\d{1,3}(?:,\d{3})+|\d{1,4}|\?)(?:\s*[-.–]\s*'+SEG+r'){1,4})(\s*\[\?\])?(?![\w])')
T=open(EN,encoding='utf8').read()
edits={}
for l in E:
    if ':' in l:
        k,v=l.split(':',1); edits[k.strip()]=v.strip()
ok=skip=chg=0; per={}
for k,v in edits.items():
    if k not in rows or not v or v.lower()=='x': print('SKIP',k,repr(v)); skip+=1; continue
    p,j=map(int,k.split('_')); per.setdefault(p,[]).append((j,v,rows[k]['file']))
new=T
for p,lst in per.items():
    m=re.search(r'\n### Page %d \(PDF \d+\)'%p,new); s=m.start()+1
    n=re.search(r'\n### Page ',new[s+5:]); e=s+5+n.start() if n else len(new)
    sec=new[s:e]; body_off=sec.index('\n')+1
    gs=[(g.start(1)+body_off,g.end(),g.group(1),g) for g in GRP.finditer(sec[body_off:])]
    # re-anchor offsets to sec
    gs=[(g.start(1)+body_off,g.end()+body_off,g.group(1)) for g in GRP.finditer(sec[body_off:])]
    remap=None
    if BASE:
        ot=subprocess.run(['git','show',BASE+':'+os.path.relpath(EN)],capture_output=True,text=True).stdout
        mo=re.search(r'\n### Page %d \(PDF \d+\)'%p,ot); so=mo.start()+1
        no=re.search(r'\n### Page ',ot[so+5:]); osec=ot[so:so+5+no.start()] if no else ot[so:]
        og=[g.group(1) for g in GRP.finditer(osec[osec.index('\n')+1:])]
        sm=difflib.SequenceMatcher(None,[re.sub(r'\s','',x) for x in og],[re.sub(r'\s','',x[2]) for x in gs],autojunk=False)
        remap={}
        for a,b,n in sm.get_matching_blocks():
            for k in range(n): remap[a+k]=b+k
    for j,v,exp in sorted(lst,reverse=True):
        if remap is not None:
            if j not in remap: print('UNMAPPED',p,j,exp,'(group edited or moved since BASE)'); skip+=1; continue
            jj=remap[j]
        else: jj=j
        a,b,txt=gs[jj]
        if re.sub(r'\s','',txt)!=re.sub(r'\s','',exp): print('MISMATCH',p,j,repr(txt),'expected',repr(exp)); skip+=1; continue
        oldsegs=re.split(r'[-.–]',re.sub(r'\s','',txt)); newsegs=re.split(r'[-.–]',v)
        changed=len(oldsegs)==len(newsegs) and any(o.isdigit() and o!=n for o,n in zip(oldsegs,newsegs))
        tail=sec[b:b+6]; extra=len(re.match(r'\s*\[\?\]',tail).group(0)) if '?' not in v and re.match(r'\s*\[\?\]',tail) else 0
        sec=sec[:a]+v+sec[b+extra:]; ok+=1; chg+=changed
        print(('CHANGED ' if changed else 'ok      ')+f'p.{p} #{j}: {txt} -> {v}'+('  (removed trailing [?])' if extra else ''))
    new=new[:s]+sec+new[e:]
print('applied',ok,'(of which changed a known digit:',chg,') skipped',skip)
if W:
    assert new.count('**Progress note:**')==T.count('**Progress note:**') and len(new)>=len(T)-50
    open(EN,'w',encoding='utf8').write(new); print('written')
