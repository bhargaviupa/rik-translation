import subprocess,re,sys
import os; R=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
def g(*a): return subprocess.run(['git','-C',R]+list(a),capture_output=True,text=True).stdout
g('fetch','-q','origin')
F={'3':'vol3/Rigveda_Samhita_Vol3_English_Translation.md','4':'Rigveda_Samhita_Vol4_English_Translation.md','5':'Rigveda_Samhita_Vol5_English_Translation.md'}
for b in ['vol3','vol4-a','vol4-b','vol5-a','vol5-b','vol5-c']:
    r='origin/claude/pass2-'+b
    if not g('rev-parse','-q','--verify',r).strip(): print(b,'NO BRANCH'); continue
    v=b[3]; f=F[v]; base=g('merge-base','origin/main',r).strip()
    n=g('rev-list','--count',base+'..'+r).strip()
    files=g('diff','--name-only',base,r).split()
    d=g('diff','-U0',base,r,'--',f)
    hunks=[(int(m.group(1)),int(m.group(2) or 1)) for m in re.finditer(r'^@@ -(\d+)(?:,(\d+))? ',d,re.M)]
    lo=min([h[0] for h in hunks],default=0); hi=max([h[0]+h[1] for h in hunks],default=0)
    old=g('show',f'{base}:{f}'); new=g('show',f'{r}:{f}')
    q0,q1=old.count('[?]'),new.count('[?]')
    msgs=g('log','--format=%s',base+'..'+r)
    ocr='OCR' in msgs or any('ocr' in x.lower() for x in files)
    part=[x for x in files if '/parts/' in x]
    ph=g('show',f'{r}:{part[0]}').splitlines()[:1] if part else ['-']
    blank='blank' in (g('show',f'{r}:{part[0]}').lower() if part else '')
    other=[x for x in files if x!=f and '/parts/' not in x and '/review/edits_' not in x]
    print(f"{b}: {n} commits | lines {lo}-{hi} of old file | size {len(old)}->{len(new)} | [?] {q0}->{q1} | OCR:{ocr} blank:{blank} | other files:{other[:6]} | part1: {ph[0][:70]}")
