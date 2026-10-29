"""samchk_v4a.py FIRST_LINE LAST_LINE -- in the main file's lines FIRST..LAST, compare each accented Saṃhitā block's IAST lines with accent.iast() of its Devanagari (spaces and apostrophes ignored); print mismatches"""
import sys,os,re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from cfg import EN
from accent import iast
L=open(EN,encoding='utf8').read().split('\n'); a,b=int(sys.argv[1])-1,int(sys.argv[2])
norm=lambda s:re.sub(r"[\s'*>’]",'',s).replace('m̐','~').replace('ṃ','m')
i=a
while i<b:
    if 'Saṃhitā accents as printed' in L[i] and L[i].startswith('**Saṃhitā'):
        dv=[];iv=[];j=i+1
        while j<b and not L[j].startswith('**Pada'):
            s=L[j]
            if s.startswith('> ') and re.search('[ऀ-ॿ]',s): dv.append(s[2:])
            elif s.startswith('> *'): iv.append(s[3:].rstrip('*'))
            j+=1
        for d,v in zip(dv,iv):
            if norm(iast(d.replace('[accent ?]','')))!=norm(v.replace('[accent ?]','')): print(i+1,'\n  file:',v,'\n  tool:',iast(d))
        i=j
    i+=1
