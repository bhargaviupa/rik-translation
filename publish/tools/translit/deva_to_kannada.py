#!/usr/bin/env python3
"""Convert Devanagari text to Kannada script (codepoint-aligned blocks).
Usage: deva_to_kannada.py FILE   (prints converted text)   or import deva2kn(str).
Only Devanagari characters are mapped; danda/double danda and everything else are kept."""
import sys, re

_VARGA = {'ङ': 'कखगघङ', 'ञ': 'चछजझञ', 'ण': 'टठडढण', 'न': 'तथदधन', 'म': 'पफबभम'}

def _anusvara(s):
    # homorganic nasal + virama + stop of its own class -> anusvara (the print writes anusvara there)
    return re.sub('([ङञणनम])\u094d([कखगघचछजझटठडढतथदधपफबभ])',
                  lambda m: ('\u0902' + m.group(2)) if m.group(2) in _VARGA[m.group(1)] else m.group(0), s)

def deva2kn(s, anusvara=True):
    if anusvara: s = _anusvara(s)
    out = []
    for ch in s:
        o = ord(ch)
        if 0x0901 <= o <= 0x094D or 0x0950 == o or 0x0958 <= o <= 0x095F:
            if o == 0x0950: out.append('ಓಂ'); continue
            if 0x0958 <= o <= 0x095F: out.append(ch); continue
            out.append(chr(o + 0x380))        # block offset DEVA 0900 -> KANNADA 0C80
        elif 0x0960 <= o <= 0x0963:           # vocalic RR/LL and vowel signs
            out.append(chr(o + 0x380))
        elif 0x0966 <= o <= 0x096F:           # digits
            out.append(chr(o - 0x0966 + 0x0CE6))
        elif o == 0x093D: out.append('ಽ')     # avagraha
        else: out.append(ch)
    return ''.join(out)

if __name__ == '__main__':
    sys.stdout.write(deva2kn(open(sys.argv[1], encoding='utf8').read()))
