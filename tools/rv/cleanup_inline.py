#!/usr/bin/env python3
"""Remove translator remarks that stand INSIDE a line of a legacy volume's English (Vol 5, Nov 27 2026, user: "inline marks - go ahead").
  python3 tools/rv/cleanup_inline.py VOL [--write]
Two operations, outside the first 80 lines (front matter) and never touching `[sic ...]`, `[?]`, `[accent ?]`, `**GLOSS**`, grammatical tails (*(The tail ...)*), Devanagari:
  1. PHRASE: ", as printed" / " as printed here" / "[as printed]" / ", as read" / ", re-read at N dpi" ... inside a reference or word are deleted, the reference stays.
  2. WHOLE: a parenthetical (...) / *(...)* / [...] that is ONLY a process remark (starts with as printed / as read / re-read / printed so / gloss(es) mine / mine, tentative / identification only /
     numerals re-read / I ... / the print says ... / the Devanagari as printed ...) is taken out with the space before it.
Dry run prints each change as before -> after (short windows); --write applies and appends the removed texts to VOL/review/removed_remarks.tsv (kind 'inline')."""
import re,sys
vol=sys.argv[1]; write='--write' in sys.argv; d=f'vol{vol}'
E=f'{d}/Rigveda_Samhita_Vol{vol}_English_Translation.md'; L=open(E,encoding='utf8').read().split('\n')
SKIP=re.compile(r'\[sic|\[\?\]|\[accent|\*\*GLOSS')
PHR=[re.compile(p) for p in (r',? as printed here(?=[);\]])', r';? ?as printed here', r',? as printed(?= ?[);\]"”,])', r' \[as printed\]', r',? as read(?=[);\]])', r',? re-read at [\d–-]+ dpi', r'; no number\b(?=\))')]
START=r'(?:as printed|as read|re-?read|Re-?read|printed so|The Devanagari as printed|gloss(?:es)? mine|Gloss mine|\*Gloss mine|mine,? (?:and )?tentative|the mine|identification only|Numerals re-read|numerals in small|the Ṛgveda and Brāhmaṇa numerals|I give|I have|I read|I take|I as|sic, as printed|The citation is as printed|The Kannada word after the parenthesis|The Taittirīya text in the print|The print here says|Printed "|\(?The tail is now|eight Riks are quoted|Tai\. Saṃ\. 2-1-1-1; p\. 232|the print says \*madhyama|the print cites|as I read|Grammar, noted briefly|the print\'s examples)'
INNER=r'(?:[^()\[\]\n]|\([^()\n]*\)|\[[^\[\]\n]*\])*'
WH=[re.compile(r'\s*\*\(\s*'+START+INNER+r'\)\*'),re.compile(r'\s*\(\s*'+START+INNER+r'\)'),re.compile(r'\s*\[\s*'+START+r'(?:[^\[\]\n])*\]')]
rows=[]; out=[]
for i,l in enumerate(L,1):
    new=l
    if i>80 and not re.match(r'\s*\*\(The (?:grammatical )?tail|\s*\*\(Grammatical tail|\s*\*\(continued',l):
        for rx in PHR:
            new=rx.sub(lambda m:(rows.append((i,'phrase: '+m.group().strip())) or ''),new) if not SKIP.search(new) else new
        for rx in WH:
            def f(m):
                s=m.group()
                if SKIP.search(s) or re.search(r'[ऀ-ॿ]',s): return s
                rows.append((i,'whole: '+s.strip())); return ''
            new=rx.sub(f,new)
        if new!=l: new=re.sub(r'(?<=\S)  +',' ',new); new=re.sub(r'\s+([.;,:])',r'\1',new) if re.search(r'\s[.;,:]',new) and not re.search(r'\s[.;,:]',l) else new
    out.append(new)
print(len(rows),'changes',('(dry run)' if not write else 'written'))
for i,s in rows[:140]: print(f'L{i}: {s[:140]}')
if write:
    open(E,'w',encoding='utf8').write('\n'.join(out))
    with open(f'{d}/review/removed_remarks.tsv','a',encoding='utf8') as f:
        for i,s in rows: f.write(f'inline\t\t{i}\t{s}\t\t\n')
