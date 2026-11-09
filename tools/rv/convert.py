"""Kannada-first conversion for one window (3 pages).

kn.md  = the Kannada transcription written by the translator from the page images (Sanskrit blocks as '> ' lines; inline Sanskrit may be marked ⟦ಅಗ್ನಿಂ⟧).
en.md  = the English-file chunk written by the translator: English, labels, headings, and for every Sanskrit block a line  [[bN]]  (N = number of the
         '> ' block in kn.md, counted from 1 in order of appearance); inline Sanskrit is written in Kannada script inside ⟦ ⟧ (copied from kn.md).
The script never retypes Sanskrit: [[bN]] is replaced by the Devanagari conversion of block N, ⟦kannada⟧ by ⟦devanagari⟧; IAST is added later by add_iast.py.
"""
import re,sys,os
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..','..','publish','tools','translit'))
from kannada_to_deva import kn2deva
KNC=re.compile('[ಀ-೿]')
def kn_blocks(kn_text):
    """list of blocks (each a list of text lines without '> ') in order of appearance"""
    blocks=[];cur=None
    for l in kn_text.split('\n'):
        if l.startswith('> ') and not l.startswith('> *'):
            if cur is None: cur=[]; blocks.append(cur)
            cur.append(l[2:])
        else: cur=None
    return blocks
def expand(en_text,kn_text):
    """returns (text, problems)"""
    blocks=kn_blocks(kn_text); used=set(); prob=[]; out=[]
    # a quotation may be broken over several lines in en.md: join it first (add_iast.py and the line-wise conversion below work on single lines)
    en_text=re.sub(r'⟦([^⟧]*)⟧',lambda m:'⟦'+re.sub(r'\s*\n\s*',' ',m.group(1)).strip()+'⟧',en_text)
    for l in en_text.split('\n'):
        m=re.fullmatch(r'\s*\[\[b(\d+)\]\]\s*',l)
        if m:
            n=int(m.group(1))
            if not 1<=n<=len(blocks): prob.append(f'[[b{n}]] does not exist (kn.md has {len(blocks)} blocks)'); out.append(l); continue
            if n in used: prob.append(f'[[b{n}]] used twice')
            used.add(n); out+=['> '+kn2deva(x) for x in blocks[n-1]]
        else:
            if re.search(r'\[\[b\d+\]\]',l): prob.append('[[bN]] must stand alone on its line: '+l[:60])
            out.append(re.sub(r'⟦([^⟧]*)⟧',lambda m:'⟦'+kn2deva(m.group(1))+'⟧' if KNC.search(m.group(1)) else m.group(0),l))
    unused=[i for i in range(1,len(blocks)+1) if i not in used]
    if unused: prob.append('Sanskrit blocks of kn.md not placed in en.md (never omit a block silently): '+', '.join(f'b{i}: '+blocks[i-1][0][:30] for i in unused))
    return '\n'.join(out),prob
def kn_final(kn_text):
    """drop the inline markers; a Devanagari avagraha typed by mistake becomes the Kannada one (U+0CBD)"""
    return kn_text.replace('⟦','').replace('⟧','').replace(chr(0x093D),chr(0x0CBD))
