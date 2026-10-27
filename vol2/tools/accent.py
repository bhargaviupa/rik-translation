"""Accented Saṃhitā lines: Devanagari with ॒ (anudātta) / ॑ (svarita) as printed -> IAST with acute on the udātta.
The udātta is marked only where the print's marks show it directly: an unmarked syllable right
before a ॑ syllable or right after a ॒ syllable (a line-initial or run-internal udātta is left unmarked).  python3 accent.py 'DEVANAGARI LINE' ...  (prints the IAST)"""
import sys,os,re,unicodedata
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..','..','publish','tools','translit'))
from add_iast import deva_to_iast
U,S='॒','॑'
VOW=set('अआइईउऊऋॠऌएऐओऔ'); MAT=set('ािीुूृॄॢेैोौ'); VIR='्'
def nuclei(d):
    """accent of each vowel nucleus in order: '', 'U' or 'S'"""
    out=[]; i=0
    while i<len(d):
        c=d[i]
        if c in VOW: out.append('')
        elif 'क'<=c<='ह' or c in 'ळ':
            nx=d[i+1] if i+1<len(d) else ''
            if nx=='़': i+=1; nx=d[i+1] if i+1<len(d) else ''
            if nx!=VIR and nx not in MAT: out.append('')
        elif c in MAT: out.append('')
        elif c in (U,S) and out: out[-1]=out[-1] or ('U' if c==U else 'S')
        i+=1
    return out
ACUTE={'a':'á','ā':'ā́','i':'í','ī':'ī́','u':'ú','ū':'ū́','ṛ':'ṛ́','ṝ':'ṝ́','e':'é','o':'ó'}
def iast(d):
    acc=nuclei(d); n=len(acc)
    ud=[acc[k]=='' and ((k+1<n and acc[k+1]=='S') or (k>0 and acc[k-1]=='U')) for k in range(n)]
    plain=deva_to_iast(d.replace(U,'').replace(S,''))
    out=[]; k=0; i=0; s=plain
    while i<len(s):
        two=s[i:i+2]
        if two in ('ai','au'):
            out.append(('á'+two[1]) if k<n and ud[k] else two); k+=1; i+=2; continue
        c=s[i]
        if c in ACUTE:
            out.append(ACUTE[c] if k<n and ud[k] else c); k+=1
        else: out.append(c)
        i+=1
    if k!=n: out.append(f' [syllables {k}/{n}?]')
    return unicodedata.normalize('NFC',''.join(out)).replace('‖','||')
if __name__=='__main__':
    for a in sys.argv[1:]: print(iast(a))
