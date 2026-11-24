#!/usr/bin/env python3
"""Reading sheet for S2 of a legacy volume's second pass: python3 tools/rv/second_pass_page.py VOL A-B [--out FILE]
For printed pages A..B writes the supplied Kannada of every page, then the English segments (from second_pass_sieve's sieve_segments.tsv) whose first page is in A..B,
with their line numbers in the English file. Saṃhitā/Pada/bhāṣya blocks of the English are shown as '[block not read]' (rule 2 of the prompt). Report only."""
import sys,os,re,csv
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import recheck as R
vol,rng=sys.argv[1],sys.argv[2]; a,b=map(int,rng.split('-')); d=f'vol{vol}'
out=sys.argv[sys.argv.index('--out')+1] if '--out' in sys.argv else None
KN,_=R.read_kn(f'{d}/Rigveda_Samhita_Vol{vol}_Kannada_Text.md')
EN=open(f'{d}/Rigveda_Samhita_Vol{vol}_English_Translation.md',encoding='utf8').read().split('\n')
segs=list(csv.DictReader(open(f'{d}/review/second_pass/sieve_segments.tsv'),delimiter='\t'))
o=[f'# Reading sheet Vol {vol}, printed pp. {a}-{b}\n','## SUPPLIED KANNADA\n']
for p in range(a-1,b+2):
    o.append(f'<<< printed {p} >>>\n'+(KN.get(p,'(not in the supplied text: stands in the neighbour page)').strip())+'\n')
o.append('## ENGLISH (line numbers of the English file in front)\n')
skip=False
for s in segs:
    if not(a<=int(s['page'])<=b): continue
    o.append(f"--- segment from page {s['page']}, lines {s['first_line']}-{s['last_line']}, sieve: refs only in English [{s['refs_list']}] numbers only in English [{s['nums_list']}] quotations not found {s['quote_not_found']}")
    for i in range(int(s['first_line'])-1,int(s['last_line'])):
        l=EN[i]; m=re.match(r'\*\*([^*]+)\*\*',l)
        if m: skip=m.group(1).startswith(('Saṃhitā','Pada-pāṭha','Sāyaṇa-bhāṣya'))
        elif l.startswith('#') or l.startswith('**Translation:**') or l.startswith('**Grammatical') or l=='---': skip=False
        o.append(f'{i+1}: '+('[block not read]' if skip and not m else l))
t='\n'.join(o)+'\n'
if out: open(out,'w',encoding='utf8').write(t); print(len(t),'chars ->',out)
else: print(t)
