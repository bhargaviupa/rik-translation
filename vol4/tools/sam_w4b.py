"""sam_w4b.py "HEADING PREFIX" "deva line 1" "deva line 2" ... -- set the accented Saṃhitā block of a Ṛk (bold Devanagari lines + italic IAST
lines, keeping the file's existing word spacing of the IAST), drop '; accents not reproduced' from its label, add the accent note.
IAST: accent.iast() output, re-spaced to the existing unaccented IAST line (letters compared without accents)."""
import sys,os,unicodedata
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from cfg import EN
from accent import iast
def strip(s): return ''.join(c for c in unicodedata.normalize('NFD',s) if c not in '́̀')
pre=sys.argv[1]; dv=sys.argv[2:]
L=open(EN,encoding='utf-8').read().split('\n'); n0=sum(map(len,L))
h=next(i for i,l in enumerate(L) if l.startswith(pre))
s=next(i for i in range(h,h+10) if L[i].startswith('**Saṃhitā-pāṭha**'))
L[s]=L[s].replace('; accents not reproduced','')
a=next(i for i in range(s,s+5) if L[i].startswith('> **'))
assert all(L[a+k].startswith('> **') for k in range(len(dv))) and not L[a+len(dv)].startswith('>')
fl=lambda d:(d.replace(' [accent ?]',''),' [accent ?]' if '[accent ?]' in d else '')
for k,d in enumerate(dv):
    d0,f=fl(d); L[a+k]=f'> **{d0}**{f}'
b=next(i for i in range(a+len(dv),a+len(dv)+4) if L[i].startswith('*'))
for k,d in enumerate(dv):
    d0,f=fl(d); acc=iast(d0); old=L[b+k].strip('*')
    # respace: walk the accented string, copying old's spaces
    a2=acc.replace(' ',''); out=''; j=0
    for ch in old:
        if ch==' ': out+=' '; continue
        # consume chars of a2 whose stripped form matches ch (accents attach after base)
        seg=''
        while j<len(a2) and (not seg or unicodedata.combining(unicodedata.normalize('NFD',a2[j])[0])):
            seg+=a2[j]; j+=1
            if strip(seg)==unicodedata.normalize('NFC',ch) or strip(seg)==strip(ch): break
        while j<len(a2) and unicodedata.normalize('NFD',a2[j])[0] in '́̀': seg+=a2[j]; j+=1
        assert strip(seg)==strip(ch),(old,acc,ch,seg)
        out+=seg
    assert j==len(a2),(old,acc)
    L[b+k]=f'*{out}*{f}'
e=b+len(dv)
if not any('Saṃhitā accents as printed' in L[i] for i in range(e,e+3)):
    L[e:e]=['','*(Saṃhitā accents as printed; Pada unaccented.)*']
for i in range(a,e+3): print(L[i])
assert sum(map(len,L))>=n0
open(EN,'w',encoding='utf-8').write('\n'.join(L))
