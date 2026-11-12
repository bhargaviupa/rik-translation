"""Split a machine-read page HTML (one <header> per page, Kannada script) into printed pages.
python3 tools/rv/html_pages.py FILE.html            list pages (printed number, size)
import: pages(path) -> {printed_page: text}  (page = text from one running head to the next; a running head contains the book title and the page number at either end)"""
import re,html,sys
KD=str.maketrans('೦೧೨೩೪೫೬೭೮೯','0123456789')
ANOMALIES=[]
def pages(path,heads=None,title=('ಸಾಯಣಭಾಷ್ಯಸಹಿತಾ','ಋಗ್ವೇದಸಂಹಿತಾ','ಸಾಯಣಭಾಷ್ಯಭೂಮಿಕೆ','ಸಾಯಣಭಾವ್ಯಸಹಿತಾ')):
    """HTML form. Head numbers are noisy (OCR: '750' for 790, '79]' for 791): numbers that disagree with their neighbours are replaced by the
    offset-median rule (as in pages_md); a head with no number takes the previous number + 1."""
    t=open(path,encoding='utf8',errors='replace').read(); b=t[t.find('<body'):]
    parts=re.split(r'<header[^>]*>(.*?)</header>',b,flags=re.S); items=[]
    for i in range(1,len(parts),2):
        h=html.unescape(re.sub(r'<[^>]+>','',parts[i])).strip(); body=parts[i+1]
        isp=any(x in h for x in title) or bool(re.search(r'(^[0-9]{1,4}\s+\S)|(\S\s+-?\s*[0-9]{1,4}$)',h) and len(h)>=8 and not re.search('ಪಾರಃ|ಪಾಠಃ|ಪಾದಃ',h))
        m=re.findall(r'(?<![0-9೦-೯])[0-9]{1,4}(?![0-9೦-೯])',h) if isp else []
        items.append([h,body,isp,int(m[0]) if m else None])
    num=[k for k,it in enumerate(items) if it[2] and it[3] is not None]
    off=[items[k][3]-j for j,k in enumerate(num)]; fixed={}
    for j,k in enumerate(num):
        nb=[off[x] for x in range(max(0,j-3),min(len(num),j+4)) if x!=j]
        if off[j] in nb or not nb: fixed[k]=items[k][3]
        else: w=sorted(nb); fixed[k]=j+w[len(w)//2]; ANOMALIES.append((k,items[k][3],fixed[k],items[k][0][:50]))
    out={}; cur=None; last=0
    for k,(h,body,isp,n) in enumerate(items):
        if isp:
            cur=fixed[k] if k in fixed else last+1; last=cur; out.setdefault(cur,[])
            if heads is not None: heads.setdefault(cur,h)
        txt=html.unescape(re.sub(r'<[^>]+>','',re.sub(r'<br\s*/?>|</(p|div|h\d|li|aside)>','\n',body)))
        if cur is not None: out[cur].append((h if not isp else '')+'\n'+txt if not isp else txt)
    return {k:re.sub(r'\n\s*\n+','\n','\n'.join(v)).strip() for k,v in out.items()}

def _head_number(h):
    h=h.translate(KD)                                   # Kannada digits in a head count like Latin ones (Vol 16)
    m=re.match(r'^[#\s]*([0-9][0-9:)]{0,4})(?=\s)',h) or re.search(r'\s([0-9]{1,4})\s*$',h)
    if not m: return None
    d=re.sub(r'[^0-9]','',m.group(1)); return int(d) if d else None
VOL1_HEAD=re.compile(r'(?:[0-9]{1,4}\s+(?:ಋಗ್ವೇದ|ಹುಗ್ಗೇದ|ಮಗ್ವೇದ|ಋಗ್ಗೇದ)\S{0,8}|(?:ಪೂರ್ವಪೀಠಿಕೆ|ಸಾಯಣಭಾಷ್ಯಭೂಮಿಕೆ|ಸಾಯಣಭಾಷ್ಯ ?ಭೂಮಿಕೆ)\s+[0-9]{1,4})')
def pages_md(path,heads=None):
    """same for the markdown form: a running-head line (title + page number at its start or end) starts a page; image lines are dropped.
    The head numbers are noisy (OCR): a number that disagrees with its neighbours is replaced by the one the sequence implies (median of the offset
    number - index over the 3 heads on each side) and listed in ANOMALIES. A jump forward that the neighbours share (unnumbered pages carry no head) is kept
    and listed too: a page without a head merges into the page before it."""
    lines=open(path,encoding='utf8',errors='replace').read().split('\n'); H=[]
    body0=next((i for i,l in enumerate(lines) if l.strip()=='<!-- body -->'),-1)   # optional marker: running heads above it (front matter, roman pages) are not page heads
    for ln,l in enumerate(lines):
        h=l.strip()
        if ln<body0: continue
        if l.startswith('![') or 'base64,' in l or not h or len(h)>=110: continue
        m0=re.fullmatch(r'<!-- page (\d+) -->',h)          # explicit marker put into the supplied file for a page that prints no running head (e.g. p. 1 of a volume); recorded in volN/STATUS.md
        if m0: H.append([ln,int(m0.group(1)),'']); continue
        if VOL1_HEAD.fullmatch(h):                          # Vol 1 heads: 'ಪೂರ್ವಪೀಠಿಕೆ 3', '4 ಋಗ್ವೇದಭಾಷ್ಯದ' (and OCR variants of the second word)
            n=_head_number(h)
            if n is not None: H.append([ln,n,h]); continue
        if any(x in h for x in ('ಸಾಯಣಭಾಷ್ಯಸಹಿತಾ','ಋಗ್ವೇದಸಂಹಿತಾ','ಸಾಯಣಭಾಷ್ಯಭೂಮಿಕೆ','ಭಾಷ್ಯಸಹಿತಾ','ಗ್ವೇದಸಂಹಿತಾ')):
            n=_head_number(h)
            if n is not None: H.append([ln,n,h])
    off=[n-i for i,(ln,n,h) in enumerate(H)]; del ANOMALIES[:]; fixed=[]
    for i,(ln,n,h) in enumerate(H):
        nb=[off[j] for j in range(max(0,i-3),min(len(H),i+4)) if j!=i]
        if off[i] in nb or not nb: t=n                      # a neighbour shares this offset: the number is consistent
        else:
            w=sorted(nb); t=i+w[len(w)//2]                  # isolated: take the offset of its neighbours
            ANOMALIES.append((ln+1,n,t,h[:50]))
        fixed.append(t)
    for i in range(1,len(H)):
        if fixed[i]>fixed[i-1]+1 and fixed[i]==H[i][1]: ANOMALIES.append((H[i][0]+1,H[i][1],H[i][1],'skip from %d (page without a running head, merged into the page before?)'%fixed[i-1]))
    out={}; cur=None; hi={ln:(k,fixed[k]) for k,(ln,n,h) in enumerate(H)}
    for ln,l in enumerate(lines):
        if ln in hi:
            cur=hi[ln][1]; out.setdefault(cur,[])
            if heads is not None: heads.setdefault(cur,H[hi[ln][0]][2])
            continue
        if l.startswith('![') or 'base64,' in l: continue
        if cur is not None: out[cur].append(re.sub(r'^#+\s*','',l))
    return {k:re.sub(r'\n\s*\n+','\n','\n'.join(v)).strip() for k,v in out.items()}
def load(path,heads=None): return pages_md(path,heads) if path.endswith('.md') else pages(path,heads)
def load_many(specs,heads=None):
    """specs: 'file' or 'file@LO-HI' (printed pages taken from that file); returns {printed page: text}"""
    P={}
    for sp in specs:
        lo,hi=0,10**6
        if '@' in sp: sp,r=sp.split('@'); lo,hi=map(int,r.split('-'))
        h={}; d=load(sp,h)
        for k,v in d.items():
            if lo<=k<=hi: P[k]=v; (heads.__setitem__(k,h.get(k,'')) if heads is not None else None)
    return P
if __name__=='__main__':
    p=load(sys.argv[1]); print(len(p),'pages; printed',min(p),'-',max(p)); print('missing numbers:',[k for k in range(min(p),max(p)+1) if k not in p])
    print('anomalies (line, number read, number used, head):'); [print('  ',a) for a in ANOMALIES]
