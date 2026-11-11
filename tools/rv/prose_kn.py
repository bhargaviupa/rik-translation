#!/usr/bin/env python3
"""Kannada text of a PROSE volume (or prose part) from the supplied machine-read files, page by page, with `<!-- printed N -->` marks.

  python3 tools/rv/prose_kn.py OUT.md "file.md@1-224" "file.html@225-573" "file.md@575-720" [--front file.md] [--rk-from N]

Same cleaning as html_to_kn.py (clean_line: '||'/'|' -> danda, Telugu digits, avagraha, the user's reference-abbreviation reading; stray lines kept as italic
notes; line-end hyphen joins; Devanagari inside Kannada rewritten letter for letter) but NO Ṛk-section structure (no Saṃhitā/Pada labels): for the
Ṛk-structured part of a volume use html_to_kn.py. Used for Vol 1 and Vol 2 (preface, introduction, Bhāṣya-bhūmikā). Pages missing between the first and
last page are written as `<!-- printed N: NOT IN THE SUPPLIED TEXT -->`. --front: lines of that file above its `<!-- body -->` marker are written first, as one
block; --rk-from N: pages N.. are made by html_to_kn.kn_pages (Mandala 1) (roman-numbered pages are not split); embedded images are replaced by `[figure]` lines."""
import re,sys,os
sys.path.insert(0,os.path.dirname(__file__))
import html_pages as HP, html_to_kn as K
HEADER='# ಋಗ್ವೇದ ಸಂಹಿತಾ — ಸಂಪುಟ 1 (Kannada text)\n*The Kannada text of the printed pages, made by script from the supplied machine-read text (tools/rv/prose_kn.py for the prose pages, tools/rv/html_to_kn.py from the first Ṛk page). `[?]` marks a doubtful reading.*\n\n---\n'
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
    rk=int(a[a.index('--rk-from')+1]) if '--rk-from' in a else None
    if rk: a=[x for i,x in enumerate(a) if x!='--rk-from' and a[i-1]!='--rk-from']
    out,specs=a[0],a[1:]; H={}; P=HP.load_many(specs,H); lo,hi=min(P),max(P)
    md=[HEADER] if rk else []
    if fr: md.append(front(fr))
    for p in range(lo,(rk or hi+1)):
        md.append(clean_page(p,H.get(p,''),P[p]) if p in P else f'<!-- printed {p}: NOT IN THE SUPPLIED TEXT -->\n')
    if rk:        # Ṛk-structured part: the same pass as the other volumes (labels, blocks, verse numbers)
        t,_=K.kn_pages(specs,list(range(rk,hi+1)),None,[1]); md.append(t)
    open(out,'w',encoding='utf8').write('\n'.join(md))
    print(f'{len(P)} pages, printed {lo}-{hi}; missing: {[p for p in range(lo,hi+1) if p not in P]}')
