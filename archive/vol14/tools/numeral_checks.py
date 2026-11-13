"""Consistency checks on the Vol 14 translation (read-only). python3 vol14/tools/numeral_checks.py [--cite M1_HTML]
1. Ṛk headings: within a sūkta they must run 1,2,3...; heading vs the numeral printed in the Saṃhitā block.
2. Varga numbers in the page-header notes must not decrease within an adhyāya.
3. (--cite) Ṛgveda citations 'M-S-R' that sit next to a quoted verse: quote matched against the accented references (M1 from the user's HTML, M2 from vol14/refs); reports quotes whose best-matching verse differs from the cited number."""
import re,sys,os,html,difflib,collections
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
EN=os.path.join(ROOT,'vol14','Rigveda_Samhita_Vol14_scan_English_Translation.md')
s=open(EN,encoding='utf8').read(); L=s.split('\n')
DEV=str.maketrans('०१२३४५६७८९','0123456789')
# 1. Ṛk numbering
out=[]; prev=None; pn=None
for i,l in enumerate(L):
    m=re.match(r'####+ Ṛk (\d+)\b',l)
    if m:
        n=int(m.group(1))
        if prev is not None and n!=1 and n!=prev+1: out.append((i+1,'Ṛk sequence',f'heading Ṛk {n} after Ṛk {prev}'))
        if prev is not None and n==prev and n!=1: out.append((i+1,'Ṛk repeated',f'Ṛk {n}'))
        prev=n
        # numeral printed in the Saṃhitā block that follows
        for j in range(i+1,min(i+14,len(L))):
            if L[j].startswith('> ') and not L[j].startswith('> *'):
                k=j
                while k<len(L) and L[k].startswith('> ') and not L[k].startswith('> *'): k+=1
                blk=' '.join(x[2:] for x in L[j:k]); mm=re.search(r'॥\s*([०-९]+)\s*॥',blk)
                if mm and int(mm.group(1).translate(DEV))!=n: out.append((j+1,'Ṛk numeral vs heading',f'heading {n}, block prints {mm.group(1).translate(DEV)}'))
                break
# 2. Varga
vg=[];pg=None
for i,l in enumerate(L):
    m=re.match(r'### Printed p\. (\d+) \(PDF (\d+)',l)
    if m: pg=(int(m.group(1)),int(m.group(2))); continue
    if pg and pg[0]>=375:
        for mm in re.finditer(r'(?:\bVa\.|\bV\.|Varga)\s*(\d+)',l[:400]):
            if 'Header' in l[:60] or 'header' in l[:60]: vg.append((pg,i+1,int(mm.group(1)))); break
lastv=None
for pg,i,v in vg:
    if lastv is not None and (v<lastv[0] and v>1):
        out.append((i,'Varga decreases',f'p.{pg[0]} Varga {v} after {lastv[0]} (p.{lastv[1]})'))
    if lastv is not None and v>lastv[0]+1: out.append((i,'Varga jumps',f'p.{pg[0]} Varga {v} after {lastv[0]} (p.{lastv[1]})'))
    lastv=(v,pg[0])
for r in out: print(r)
print(len(out),'findings in checks 1-2; Varga header readings found:',len(vg))

# 3. citations into Maṇḍala 1 and 2, checked against the quoted verse text
if '--cite' in sys.argv:
    sys.path.insert(0,os.path.join(ROOT,'vol14','tools')); import accents as A
    m1=open(sys.argv[sys.argv.index('--cite')+1],encoding='utf8',errors='replace').read()
    m1=html.unescape(re.sub(r'<[^>]+>','',re.sub(r'<br>|</p>','\n',m1,flags=re.I))).split('\n')
    verses={}
    def add(lines,pref):
        buf=[]
        for l in lines:
            l=l.strip()
            if not l: continue
            m=re.search(r'॥\s*([०-९0-9]+)\.([०-९0-9]{3})\.([०-९0-9]{2})\s*$',l)
            if m:
                t=l[:m.start()].strip(); buf.append(t); key=tuple(int(x.translate(DEV)) for x in m.groups())
                verses[key]=A.canon(' '.join(buf)); buf=[]
            elif re.search('[ऀ-ॿ]',l) and not l.startswith('॥ ऋग्वेदः'): buf.append(l)
    add(m1,1); add(open(os.path.join(ROOT,'vol14','refs','rv_mandala2_accented.txt'),encoding='utf8').read().split('\n'),2)
    print('reference verses loaded',len(verses))
    G=collections.defaultdict(set)
    for k,v in verses.items():
        for i in range(len(v)-5): G[v[i:i+6]].add(k)
    def best(q):
        q=A.canon(q); 
        if len(q)<14: return None
        cnt=collections.Counter(); 
        for i in range(0,len(q)-5): 
            for k in G.get(q[i:i+6],()): cnt[k]+=1
        res=[]
        for k,c in cnt.most_common(6):
            sm=difflib.SequenceMatcher(None,q,verses[k],autojunk=False); b=sm.find_longest_match(0,len(q),0,len(verses[k])).size
            res.append((b/len(q),k))
        return max(res) if res else None
    rows=[]; n=0
    for i,l in enumerate(L):
        for m in re.finditer(r'Ṛ(?:g)?\. ?Saṃ\. ?(\d+)-(\d+)-(\d+)',l):
            M,S,R=map(int,m.groups())
            if M not in (1,2): continue
            quote=None
            # quote in the blockquote that follows a 'Cited' line
            if l.lstrip().startswith('*Cited'):
                for j in range(i+1,min(i+5,len(L))):
                    if L[j].startswith('> ') and not L[j].startswith('> *'): quote=L[j][2:]; break
            if quote is None:
                pre=l[max(0,m.start()-160):m.start()]; d=re.findall(r'[ऀ-ॿ][ऀ-ॿ\s।॥\-]{12,}',pre)
                if d: quote=d[-1]
            if not quote: continue
            b=best(quote); n+=1
            if b is None: continue
            sc,k=b
            if sc>=0.75 and k!=(M,S,R): rows.append((i+1,f'cited {M}-{S}-{R}; quote best matches {k[0]}-{k[1]}-{k[2]} (score {sc:.2f})',quote[:50]))
            elif sc<0.5: rows.append((i+1,f'cited {M}-{S}-{R}; quote matches nothing well (best {k[0]}-{k[1]}-{k[2]}, {sc:.2f})',quote[:50]))
    print('citations with a usable quote',n,'| findings',len(rows))
    for r in rows: print(r)
