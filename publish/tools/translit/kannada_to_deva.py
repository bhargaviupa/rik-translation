#!/usr/bin/env python3
"""Convert Kannada-script Sanskrit to Devanagari (inverse of deva_to_kannada.py; codepoint-aligned blocks).
Usage: kannada_to_deva.py FILE (prints converted text) or import kn2deva(str).
Only Kannada characters are mapped; danda, brackets, [?] and Latin text are kept. Kannada ಽ (avagraha) -> ऽ.
Note: the print writes anusvara before a stop of any class; the Devanagari files may show a nasal+virama conjunct instead; compare with canon()."""
import sys
def kn2deva(s):
    out=[]
    for ch in s:
        o=ord(ch)
        if 0x0C82<=o<=0x0CCD or 0x0CE0<=o<=0x0CE3:
            out.append(chr(o-0x380))
        elif 0x0CE6<=o<=0x0CEF: out.append(chr(o-0x0CE6+0x0966))
        elif ch=='ಽ': out.append('ऽ')
        elif ch=='ಓ' and False: pass
        else: out.append(ch)
    return ''.join(out)
if __name__=='__main__':
    sys.stdout.write(kn2deva(open(sys.argv[1],encoding='utf8').read()))
