#!/usr/bin/env python3
"""Kannada text of a PROSE volume (or prose part) from the supplied machine-read files, page by page, with `<!-- printed N -->` marks.

  python3 tools/rv/prose_kn.py OUT.md "file.md@1-224" "file.html@225-573" "file.md@575-720" [--front file.md]

Same cleaning as html_to_kn.py (clean_line: '||'/'|' -> danda, Telugu digits, avagraha, the user's reference-abbreviation reading; stray lines kept as italic
notes; line-end hyphen joins; Devanagari inside Kannada rewritten letter for letter) but NO Ṛk-section structure (no Saṃhitā/Pada labels): for the
Ṛk-structured part of a volume use html_to_kn.py. Used for Vol 1 and Vol 2 (preface, introduction, Bhāṣya-bhūmikā). Pages missing between the first and
last page are written as `<!-- printed N: NOT IN THE SUPPLIED TEXT -->`. --front: lines of that file above its `<!-- body -->` marker are written first, as one
block (roman-numbered pages are not split); embedded images are replaced by `[figure]` lines."""
import re,sys,os
sys.path.insert(0,os.path.dirname(__file__))
import html_pages as HP, html_to_kn as K
def clean_page(printed,head,text):
    out=[f'<!-- printed {printed} -->']
    if head: out.append('*['+K.clean_line(head)+']*')
    out.append('')
    for l in text.split('\n'):
        l=K.clean_line(l)
        if not l: out.append(''); continue
        if l.startswith('![') or 'base64,' in l: out.append('[figure]'); continue
        l,dv=K.deva_to_kn_line(l)
        if K.stray(l): out.append(f'*[stray line as supplied: {l}]*'); continue
        out.append(l)
    return '\n'.join(K.join_hyphens(out))+'\n'
def front(path):
    L=open(path,encoding='utf8',errors='replace').read().split('\n')
    end=next((i for i,l in enumerate(L) if l.strip()=='<!-- body -->'),len(L)); out=['<!-- front matter (roman-numbered pages, not split) -->','']
    for l in L[1:end]:
        if l.startswith('![') or 'base64,' in l: out.append('[figure]'); continue
        c=K.clean_line(l)
        out.append(c if c or not l.strip() else '')
    return re.sub(r'\n{3,}','\n\n','\n'.join(out))+'\n'
if __name__=='__main__':
    a=sys.argv[1:]; fr=a[a.index('--front')+1] if '--front' in a else None
    if fr: a=[x for i,x in enumerate(a) if x!='--front' and a[i-1]!='--front']
    out,specs=a[0],a[1:]; H={}; P=HP.load_many(specs,H); lo,hi=min(P),max(P)
    md=[front(fr)] if fr else []
    for p in range(lo,hi+1):
        md.append(clean_page(p,H.get(p,''),P[p]) if p in P else f'<!-- printed {p}: NOT IN THE SUPPLIED TEXT -->\n')
    open(out,'w',encoding='utf8').write('\n'.join(md))
    print(f'{len(P)} pages, printed {lo}-{hi}; missing: {[p for p in range(lo,hi+1) if p not in P]}')
