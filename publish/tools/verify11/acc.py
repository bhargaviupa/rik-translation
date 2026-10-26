"""Add Vedic accents to Saṃhitā lines of the English file.
apply(["accented line", ...]): each accented line must equal an existing '> ' Devanagari line once the marks are removed;
it replaces that line and regenerates the IAST line below it.  ॒ (U+0952) anudātta = underline in print; ॑ (U+0951) svarita = stroke above; unmarked = udātta."""
import sys,re,os
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..','translit'))
from add_iast import deva_to_iast
from cfg import EN as E
A=re.compile('[॒॑]')
def apply(lines):
    L=open(E,encoding='utf8').read().split('\n')
    for new in lines:
        plain=A.sub('',new)
        hits=[i for i,l in enumerate(L) if l.startswith('> ') and not l.startswith('> *') and A.sub('',l[2:])==plain]
        assert hits,('no match',plain)
        i=hits[0]; L[i]='> '+new; ip=deva_to_iast(plain).replace('̱','').replace('̭','')
        for j in range(i+1,min(i+12,len(L))):
            if L[j].startswith('> *') and A.sub('',L[j])[3:-1].replace('̱','').replace('̭','')==ip:
                L[j]='> *'+deva_to_iast(new)+'*'; break
        else: print('IAST line not found for',plain[:30])
    open(E,'w',encoding='utf8').write('\n'.join(L))
