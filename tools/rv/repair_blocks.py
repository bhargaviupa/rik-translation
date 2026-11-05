"""Repair '[?]' in Devanagari block lines of an English volume file from the user's supplied machine-read text.
  python3 tools/rv/repair_blocks.py --md FILE.md --src "file.html@LO-HI" --first P --last Q [--apply] [--tsv log.tsv]
For every '> ' Devanagari line with '[?]' between printed pages P..Q: the supplied page text (page, previous and next page) is converted
(Kannada -> Devanagari) and the best-matching word window found; the doubtful word is aligned with the supplied word. Equal -> the '[?]' is dropped;
different -> the supplied word is put in (logged for the user's decision); no counterpart -> the line is left. Nothing is changed without --apply."""
import re,sys,os,argparse,difflib
sys.path.insert(0,os.path.dirname(__file__)); sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..','..','publish','tools','translit'))
import html_pages; from html_to_kn import clean_line
from kannada_to_deva import kn2deva
from rapidfuzz import fuzz
ACC=dict.fromkeys([0x951,0x952,0x953,0x954,0x1CDA,0x1CF4],None)
def norm(w):
    w=re.sub(r'\[\?\]','',w).translate(ACC)
    return re.sub(r'[^ऄ-हा-्क़-ॣ]','',w.replace('ऽ',''))
KN=re.compile('[ಀ-೿]')
def pool(P,p):
    toks=[]
    for q in (p-1,p,p+1):
        for raw in P.get(q,'').split('\n'):
            l=clean_line(raw)
            if not l: continue
            d=kn2deva(l) if KN.search(l) else l
            toks+= [t for t in d.split() if norm(t)]
    return toks
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--md'); ap.add_argument('--src',action='append'); ap.add_argument('--first',type=int); ap.add_argument('--last',type=int)
    ap.add_argument('--apply',action='store_true'); ap.add_argument('--tsv'); a=ap.parse_args()
    P=html_pages.load_many(a.src); L=open(a.md,encoding='utf8').read().split('\n'); page=None; cache={}; log=[]; stat={'confirmed':0,'changed':0,'left':0,'nomatch':0}
    for i,l in enumerate(L):
        m=re.match(r'### Printed p\. (\d+)',l)
        if m: page=int(m.group(1))
        if page is None or not(a.first<=page<=a.last) or not l.startswith('> ') or l.startswith('> *') or '[?]' not in l: continue
        old=l[2:].split(); n_old=[norm(t) for t in old]
        if page not in cache: cache[page]=pool(P,page)
        pl=cache[page]; npl=[norm(t) for t in pl]
        core=[t for t in n_old if t]; cs=''.join(core); best=(0,0,0)
        for k in (len(core)-1,len(core),len(core)+1,len(core)+2):
            if k<2: continue
            for s in range(0,max(0,len(npl)-k)+1):
                sc=fuzz.ratio(cs,''.join(npl[s:s+k]))
                if sc>best[0]: best=(sc,s,k)
        sc,s,k=best
        if sc<72: stat['nomatch']+=1; log.append((i+1,page,'nomatch',round(sc),l[2:80],'')); continue
        win=pl[s:s+k]; nw=npl[s:s+k]
        sm=difflib.SequenceMatcher(None,n_old,nw,autojunk=False); ops=sm.get_opcodes()
        new=list(old); edits=[]
        for j,t in enumerate(old):
            if '[?]' not in t: continue
            # the doubtful word: this token if it has text besides [?], else the previous token
            jj=j if norm(t) else j-1
            if jj<0: continue
            op=next((o for o in ops if o[1]<=jj<o[2] or (o[0]=='insert' and o[1]==jj)),None)
            if op is None: continue
            tag,i1,i2,j1,j2=op
            if tag=='equal': edits.append((j,jj,'confirmed',None))
            elif tag=='replace' and (i2-i1)<=2 and (j2-j1)<=3: edits.append((j,jj,'changed',(i1,i2,win[j1:j2])))
            else: edits.append((j,jj,'left',None))
        for j,jj,st,rep in edits:
            stat[st]+=1
            log.append((i+1,page,st,round(sc),' '.join(old[(rep[0] if rep else jj):(rep[1] if rep else jj+1)]), ' '.join(rep[2]) if rep else ''))
        if a.apply:
            for j,jj,st,rep in sorted(edits,key=lambda e:-e[0]):
                if st=='confirmed':
                    new[j]=new[j].replace('[?]','').strip() or None
                elif st=='changed':
                    i1,i2,w=rep; new[i1:i2]=[' '.join(w)]+[None]*0; 
                    # remove the [?] token that followed (index shifted): handled by cleanup below
            new=[t for t in new if t]
            out=' '.join(t for t in new)
            if any(e[2]=='changed' for e in edits): out=re.sub(r'\s*\[\?\]','',out,count=0) if all(e[2]!='left' for e in edits) else out
            L[i]='> '+out
    print(stat)
    if a.tsv: open(a.tsv,'w',encoding='utf8').write('\n'.join('\t'.join(map(str,r)) for r in log)+'\n')
    if a.apply: open(a.md,'w',encoding='utf8').write('\n'.join(L))
    return log
if __name__=='__main__': main()
