"""Add Vedic accent marks to the Saṃhitā blocks of the Vol 14 translation from the accented reference text vol14/refs/rv_mandala2_accented.txt.
Only accent marks (U+0951, U+0952) are added; the printed spelling of our text is never changed (checked: stripping the marks gives back exactly the original block).
A block is matched to a reference Ṛk by similarity of its unaccented skeleton; below the threshold nothing is changed and the block is reported.
CLI: python3 vol14/tools/accents.py FILE [--write] [--from-line N]     (report, or rewrite FILE)
API: apply_text(text, state=None) -> (new_text, report)  where state['ptr'] keeps the Ṛk pointer between calls."""
import re,os,sys,difflib
REF=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','..','vol14','refs','rv_mandala2_accented.txt')   # moved here from vol14/tools (Nov 13 2026); the reference file stays in vol14/refs
AC='॒॑'
def load():
    rik=[];cur=[]
    for l in open(REF,encoding='utf8'):
        if l.startswith('#') or not l.strip(): continue
        m=re.search(r'॥\s*२\.(\d{3})\.(\d{2})',l)
        if m:
            cur.append(l[:m.start()].strip()); rik.append(((int(m.group(1)),int(m.group(2))),cur)); cur=[]
        else: cur.append(l.strip())
    return rik
NAS={'ङ':'क','ञ':'च','ण':'ट','न':'त','म':'प'}   # nasal -> class initial; used only for canonical comparison
def strip_ac(s): return re.sub('['+AC+'\u1cd0-\u1cf4\ua8e0-\ua8f1]','',re.sub('[१३](?=['+AC+'])','',s))
def canon(s):
    s=strip_ac(s).replace('[?]','').replace('\u200c','').replace('\u200d','')
    s=re.sub(r'[।॥\d०-९\s\-–]','',s)
    s=re.sub(r'[ङञणनम]्(?=[क-ह])','ं',s)       # nasal conjunct ~ anusvāra
    s=s.replace('ँ','ं')
    return s
def transfer(ours,ref):
    """insert the accent marks of `ref` into `ours` by aligning their characters; return new string"""
    # reference chars with attached accents
    rb=[];ra=[]
    for n,ch in enumerate(ref):
        if ch in AC and rb: ra[-1]+=ch
        elif ch in '१३' and n+1<len(ref) and ref[n+1] in AC and rb: ra[-1]+=ch   # svarita notation 'य१॒': the digit belongs to the accent cluster
        elif ch in '‌‍' : continue
        else: rb.append(ch); ra.append('')
    ob=list(ours)
    sm=difflib.SequenceMatcher(None,ob,rb,autojunk=False); out=[];
    ins=[ '' for _ in ob]
    for tag,i1,i2,j1,j2 in sm.get_opcodes():
        if tag=='equal':
            for k in range(i2-i1): ins[i1+k]+=ra[j1+k]
        elif tag=='replace' or tag=='delete':
            a=''.join(ra[j1:j2])
            if a and i2>i1: ins[i2-1]+=a
        elif tag=='insert':
            a=''.join(ra[j1:j2])
            if a and i1>0: ins[i1-1]+=a
    res=''.join(c+ins[k] for k,c in enumerate(ob))
    # accents after visarga/anusvāra (project rule): move a mark that follows a vowel sign before ः / ं to after it
    res=re.sub('(?<![१३])(['+AC+'])([ःं])',r'\2\1',res)
    return res
RIK=None
def flat():
    out=[]
    for rid,lines in load():
        for l in lines: out.append((rid,l))
    return out
def apply_text(text,state=None,verbose=False):
    """line-wise: every line of a Saṃhitā block is matched to a reference line (searched forward from the pointer)"""
    global RIK
    if RIK is None: RIK=flat()
    state=state if state is not None else {}
    ptr=state.get('ptr',0); L=text.split('\n'); rep=[]; i=0
    cr=[canon(x[1]) for x in RIK]
    while i<len(L):
        if '॥ संहितापाठः ॥' in L[i]:
            j=i+1
            while j<len(L) and (not L[j].strip() or L[j].startswith('#') or L[j].strip()=='---' or (L[j].startswith('*') and not L[j].startswith('> '))): j+=1
            k=j
            while k<len(L) and L[k].startswith('> ') and not L[k].startswith('> *'): k+=1
            for m in range(j,k):
                ours=L[m][2:]
                if any(ch in AC for ch in ours): continue
                sk=canon(ours); best=None
                for q in range(max(0,ptr-1),min(len(RIK),ptr+10)):
                    r=difflib.SequenceMatcher(None,sk,cr[q],autojunk=False).ratio()
                    if best is None or r>best[0]: best=(r,q)
                if best is None or best[0]<0.85:       # window missed: search the whole reference (pointer had fallen behind)
                    gb=None
                    for q in range(len(RIK)):
                        if abs(len(cr[q])-len(sk))>0.4*max(len(sk),1): continue
                        r=difflib.SequenceMatcher(None,sk,cr[q],autojunk=False).ratio()
                        if gb is None or r>gb[0]: gb=(r,q)
                    if gb and gb[0]>=0.9: best=gb
                if best is None or best[0]<0.85: rep.append(('NOMATCH',round(best[0],2) if best else 0,ours[:40])); continue
                r,q=best; rid='%d.%d'%RIK[q][0]
                new=transfer(ours,RIK[q][1])
                if strip_ac(new)!=ours: rep.append(('ABORT',rid,ours[:40])); continue
                if canon(ours)!=cr[q]: rep.append(('DIFF',rid,round(r,3),ours[:40]))
                L[m]='> '+new; ptr=q+1; rep.append(('OK',rid))
            i=k
        else: i+=1
    state['ptr']=ptr
    return '\n'.join(L),rep
def ptr_from_file(text):
    """index into the flat reference list just after the last accented Saṃhitā line already in `text`"""
    global RIK
    if RIK is None: RIK=flat()
    cr=[canon(x[1]) for x in RIK]
    for l in reversed(text.split('\n')):
        if l.startswith('> ') and not l.startswith('> *') and any(c in AC for c in l):
            sk=canon(l[2:]); q=max(range(len(RIK)),key=lambda i:difflib.SequenceMatcher(None,sk,cr[i],autojunk=False).ratio()); return q+1
    return 0
def diff_rows(rep,text):
    """lines whose spelling differs from the reference beyond final-m/anusvāra style: (rik, ours, ref, [(ours,ref)...])"""
    RIKl=RIK; cr=[canon(x[1]) for x in RIKl]; rows=[]
    for r in rep:
        if r[0]!='DIFF': continue
        c=[l[2:] for l in text.split('\n') if l.startswith('> '+r[3][:20])]
        if not c: continue
        ours=c[0]; a=canon(ours); q=[i for i,x in enumerate(RIKl) if '%d.%d'%x[0]==r[1]]
        best=max(q,key=lambda i:difflib.SequenceMatcher(None,a,cr[i],autojunk=False).ratio()); b=cr[best]
        d=[(a[i1:i2],b[j1:j2]) for tag,i1,i2,j1,j2 in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes() if tag!='equal']
        d=[x for x in d if x!=('ं','म्')]
        if d: rows.append(('2.'+r[1],ours,RIKl[best][1],d))
    return rows
if __name__=='__main__':
    f=sys.argv[1]; s=open(f,encoding='utf8').read()
    n=int(sys.argv[sys.argv.index('--from-line')+1]) if '--from-line' in sys.argv else 0
    head='\n'.join(s.split('\n')[:n]); tail='\n'.join(s.split('\n')[n:])
    new,rep=apply_text(tail)
    import collections; print(collections.Counter(r[0] for r in rep))
    for r in rep:
        if r[0]!='OK': print(r)
    if '--write' in sys.argv: open(f,'w',encoding='utf8').write((head+'\n' if n else '')+new)
