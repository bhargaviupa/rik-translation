#!/usr/bin/env python3
"""Which printed pages of a volume's prose carry Sāyaṇa's Bhāṣya-bhūmikā, and where in the Wikisource export (refs/wikisource/export/Rigveda_Devanagari_M00.md)?

  python3 tools/rv/bhumika_map.py N [--min-score 85]     writes volN/review/second_pass/bhumika_map.tsv and prints the page ranges

For every printed page of volN's Kannada book, the longest Sanskrit lines (blockquote `>` lines and prose lines that hold a danda, Kannada script) are converted to Devanagari and
aligned (letters only, rapidfuzz) with the export. Columns: page, lines tried, best score, export page (पृष्ठम् N) and first paragraph reference (0.P.N.k).
A page with no line scoring at least --min-score is 'no match'. Nothing is changed."""
import re,sys,os,csv
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE); sys.path.insert(0,os.path.join(HERE,'..','..','publish','tools','translit'))
from rapidfuzz import fuzz
from kannada_to_deva import kn2deva
def norm(s): return re.sub(r'[^क-हा-ौअ-औ]','',re.sub('[॑-॒॔॑]','',s))
def main():
    a=sys.argv[1:]
    if not a: sys.exit(__doc__)
    vol=a[0]; minsc=float(a[a.index('--min-score')+1]) if '--min-score' in a else 85
    T=open('refs/wikisource/export/Rigveda_Devanagari_M00.md',encoding='utf8').read()
    ref=[];text=[];pos=0;page=None
    for ln in T.split('\n'):
        m=re.match(r'### पृष्ठम् (\d+)',ln)
        if m: page=m.group(1); continue
        m=re.match(r'\[(0\.\d+\.\d+\.\d+)\] (.*)',ln)
        if m:
            n=norm(m.group(2)); ref.append((pos,pos+len(n),m.group(1),page)); text.append(n); pos+=len(n)
    full=''.join(text)
    kn=open(f'vol{vol}/Rigveda_Samhita_Vol{vol}_Kannada_Text.md',encoding='utf8').read()
    parts=re.split(r'(?m)^<!-- printed (\d+)(?::[^\n]*)? -->\n',kn); rows=[]
    import bisect; starts=[r[0] for r in ref]
    for i in range(1,len(parts),2):
        pg=int(parts[i]); lines=[l.lstrip('> ').strip() for l in parts[i+1].split('\n') if l.startswith('>') or ('।' in l or '॥' in l)]
        lines=sorted((norm(kn2deva(l)) for l in lines),key=len,reverse=True)[:3]; lines=[l for l in lines if len(l)>=25]
        best=(0,None)
        for l in lines:
            r=fuzz.partial_ratio_alignment(l,full,score_cutoff=minsc)
            if r and r.score>best[0]: best=(r.score,r.dest_start)
        if best[1] is None: rows.append((pg,len(lines),'',' ','')); continue
        k=bisect.bisect_right(starts,best[1])-1; rows.append((pg,len(lines),f'{best[0]:.0f}',ref[k][3],ref[k][2]))
    out=f'vol{vol}/review/second_pass/bhumika_map.tsv'
    with open(out,'w',encoding='utf8') as f:
        f.write('page\tlines_tried\tscore\texport_page\tfirst_ref\n'); [f.write('\t'.join(map(str,r))+'\n') for r in rows]
    hit=[r for r in rows if r[2]]; print(len(rows),'pages;',len(hit),'with a match; written',out)
    # ranges of consecutive matched pages
    cur=None
    for r in rows:
        if r[2]:
            if cur and r[0]-cur[1]<=3: cur[1]=r[0]; cur[3]=max(cur[3],int(r[3])); cur[4]=min(cur[4],int(r[3]))
            else:
                if cur: print(f'  Vol pp. {cur[0]}–{cur[1]} ↔ export पृष्ठम् {cur[4]}–{cur[3]}')
                cur=[r[0],r[0],0,int(r[3]),int(r[3])]
    if cur: print(f'  Vol pp. {cur[0]}–{cur[1]} ↔ export पृष्ठम् {cur[4]}–{cur[3]}')
main()
