"""Compare blind scan transcriptions (one file per printed page, Kannada script) with a machine-read page HTML/markdown, word by word.
python3 tools/rv/compare_html_scan.py --html FILE --dir OUTDIR --pages 5 14 18 [--sheet sheet.tsv]
Each OUTDIR/printedN.txt is read; '=== PAGE N ===' lines, [?] marks and spacing/punctuation variants are normalised away. Output: per-page and total word counts,
identical words, differing spots (classified: one-character difference, longer difference, insertion/deletion) and a sheet of every differing spot for human adjudication.
Nothing here says which side is right: a difference is an error in the HTML, in the scan reading, or in both."""
import re,sys,os,argparse,difflib
sys.path.insert(0,os.path.dirname(__file__)); import html_pages
def norm_text(t):
    t=re.sub(r'=== PAGE [^=]*===','',t); t=t.replace('[?]',' '); t=re.sub(r'[*>#_`]',' ',t)
    t=re.sub(r'-\s*\n\s*','',t)                     # line-end hyphenation joined
    t=t.replace('||','॥').replace('|','।').replace('s','ಽ') if False else t.replace('||','॥').replace('|','।')
    t=re.sub(r'[॥।\.,;:()\[\]“”"\'‘’—–\-]',' ',t)    # punctuation is not compared
    t=re.sub(r'\s+',' ',t).strip(); return t.split()
def lev(a,b):
    p=list(range(len(b)+1))
    for i,x in enumerate(a,1):
        c=[i]
        for j,y in enumerate(b,1): c.append(min(p[j]+1,c[j-1]+1,p[j-1]+(x!=y)))
        p=c
    return p[-1]
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--html',nargs='+'); ap.add_argument('--dir'); ap.add_argument('--pages',nargs='+',type=int); ap.add_argument('--sheet'); a=ap.parse_args()
    P={}
    for _f in a.html: P.update(html_pages.load(_f))
    tot=dict(h=0,s=0,eq=0,one=0,more=0,ins=0,dele=0); rows=[]; per=[]
    for pg in a.pages:
        f=os.path.join(a.dir,f'printed{pg}.txt')
        if not os.path.exists(f): print('missing',f); continue
        s=norm_text(open(f,encoding='utf8').read()); h=norm_text(P.get(pg,''))
        sm=difflib.SequenceMatcher(None,h,s,autojunk=False); eq=one=more=ins=dele=0
        for t,i1,i2,j1,j2 in sm.get_opcodes():
            if t=='equal': eq+=i2-i1; continue
            hw,sw=' '.join(h[i1:i2]),' '.join(s[j1:j2]); ctx=' '.join(h[max(0,i1-3):i1])
            if t=='replace':
                kind='one-character' if lev(hw.replace(' ',''),sw.replace(' ',''))<=1 else ('two-three characters' if lev(hw.replace(' ',''),sw.replace(' ',''))<=3 else 'longer')
                if kind=='one-character': one+=1
                else: more+=1
            elif t=='insert': kind='only in scan reading'; ins+=1
            else: kind='only in HTML'; dele+=1
            rows.append((pg,kind,ctx,hw,sw))
        per.append((pg,len(h),len(s),eq,one,more,ins,dele))
        for k,v in zip(('h','s','eq','one','more','ins','dele'),(len(h),len(s),eq,one,more,ins,dele)): tot[k]+=v
    print('page | HTML words | scan words | identical | 1-char diffs | longer diffs | only-scan | only-HTML')
    for r in per: print(' | '.join(map(str,r)))
    print('TOTAL',tot,f"identical share of HTML words {100*tot['eq']/max(1,tot['h']):.1f}%")
    if a.sheet:
        with open(a.sheet,'w',encoding='utf8') as o:
            o.write('page\tkind\tbefore(HTML)\tHTML\tscan_reading\tuser_verdict(HTML/SCAN/BOTH/NEITHER)\n')
            for r in rows: o.write('\t'.join(map(str,r))+'\t\n')
        print('sheet:',a.sheet,len(rows),'rows')

def chars_mode():
    """character-level comparison: spaces/markup/punctuation removed on both sides; one row per differing spot with context"""
    ap=argparse.ArgumentParser(); ap.add_argument('--html',nargs='+'); ap.add_argument('--dir'); ap.add_argument('--pages',nargs='+',type=int); ap.add_argument('--sheet'); ap.add_argument('--chars',action='store_true'); a=ap.parse_args()
    P={}
    for _f in a.html: P.update(html_pages.load(_f))
    KN='[\u0C80-\u0CFF]'; tot=dict(h=0,eq=0); rows=[]; per=[]
    for pg in a.pages:
        f=os.path.join(a.dir,f'printed{pg}.txt')
        s=''.join(norm_text(open(f,encoding='utf8').read())); h=''.join(norm_text(P.get(pg,'')))
        s=re.sub('[A-Za-z0-9]','',s); h=re.sub('[A-Za-z0-9]','',h)         # Latin text and Latin digits are not compared here
        sm=difflib.SequenceMatcher(None,h,s,autojunk=False); eq=0; spots=[0,0,0,0]
        for t,i1,i2,j1,j2 in sm.get_opcodes():
            if t=='equal': eq+=i2-i1; continue
            d=max(i2-i1,j2-j1); k=0 if (t=='replace' and i2-i1==1 and j2-j1==1) else (1 if d<=3 else 2 if d<=12 else 3); spots[k]+=1
            rows.append((pg,['1 char for 1 char','2-3 chars','4-12 chars','longer than 12 chars (probably layout/ordering, not letters)'][k],h[max(0,i1-8):i1]+' [ '+h[i1:i2]+' ] '+h[i2:i2+6],h[i1:i2],s[j1:j2]))
        per.append((pg,len(h),len(s),eq,*spots)); tot['h']+=len(h); tot['eq']+=eq
    print('page | HTML chars | scan chars | identical chars | 1-for-1 spots | 2-3 char spots | 4-12 char spots | >12 char spots')
    for r in per: print(' | '.join(map(str,r)))
    S=[sum(r[i] for r in per) for i in (4,5,6,7)]
    print('TOTAL HTML chars',tot['h'],'identical chars',tot['eq'],f"= {100*tot['eq']/tot['h']:.1f}%",'| spots 1-for-1 / 2-3 / 4-12 / >12 =',S,'| spots per 1000 HTML chars: %.1f'%(1000*sum(S[:3])/tot['h']))
    if a.sheet:
        with open(a.sheet,'w',encoding='utf8') as o:
            o.write('page\tsize\tHTML context [ differing part ]\tHTML\tscan_reading\tuser_verdict(HTML/SCAN/BOTH/NEITHER)\n')
            for r in rows: o.write('\t'.join(map(str,r))+'\t\n')
        print('sheet',a.sheet,len(rows),'rows')
if __name__=='__main__':
    if '--chars' in sys.argv: chars_mode()
    else: main()
