#!/usr/bin/env python3
"""Sanskrit for a second-pass edit, made by script from the Kannada (a reader never types Devanagari or IAST).

  python3 tools/rv/sp_sanskrit.py "KANNADA TEXT COPIED FROM THE KANNADA BOOK"     prints the Devanagari and the IAST
  python3 tools/rv/sp_sanskrit.py --check VOL PAGE "DEVANAGARI"                   True/False: found in the Kannada of pages PAGE-1..PAGE+1 (letters only)
sp_apply.py uses the same check as a gate on every English edit whose new text holds Devanagari."""
import sys,os,re
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE); sys.path.insert(0,os.path.join(HERE,'..','..','publish','tools','translit'))
from kannada_to_deva import kn2deva
from deva_to_kannada import deva2kn
import add_iast
_IV={'ಅ':'','ಆ':'ಾ','ಇ':'ಿ','ಈ':'ೀ','ಉ':'ು','ಊ':'ೂ','ಋ':'ೃ','ಎ':'ೆ','ಏ':'ೇ','ಐ':'ೈ','ಒ':'ೊ','ಓ':'ೋ','ಔ':'ೌ'}
def join_words(k):
    """the English has word-split forms (tad apekṣitau, with spaces or hyphens): consonant+virama+space+independent vowel = the joined sandhi form of the print"""
    return re.sub('್[\\s\\-]*([ಅ-ಔ])',lambda m:_IV.get(m.group(1),m.group(0)) if m.group(1) in _IV else m.group(0),k)
def gate(kn_pages, page, deva, minlen=6):
    """kn_pages: {page: kannada text}; every chunk (split at dandas, commas, semicolons, colons) of at least minlen Kannada letters must stand in the Kannada of pages page-1..page+1. Returns the list of chunks that do not."""
    import recheck as R
    hay=R.norm_kn(''.join(kn_pages.get(x,'') for x in (page-1,page,page+1))); bad=[]
    for ch in re.split(r'[।॥|,;:]',deva):
        n=R.norm_kn(join_words(deva2kn(ch)))
        if len(n)>=minlen and n not in hay: bad.append(ch.strip())
    return bad
if __name__=='__main__':
    a=sys.argv[1:]
    if a and a[0]=='--check':
        import recheck as R
        vol,page,dv=a[1],int(a[2]),a[3]; kn,_=R.read_kn(f'vol{vol}/Rigveda_Samhita_Vol{vol}_Kannada_Text.md'); b=gate(kn,page,dv); print(not b, b)
    elif a:
        d=kn2deva(a[0]); print(d); print(add_iast.deva_to_iast(d))
    else: sys.exit(__doc__)
