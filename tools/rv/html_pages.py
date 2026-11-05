"""Split a machine-read page HTML (one <header> per page, Kannada script) into printed pages.
python3 tools/rv/html_pages.py FILE.html            list pages (printed number, size)
import: pages(path) -> {printed_page: text}  (page = text from one running head to the next; a running head contains the book title and the page number at either end)"""
import re,html,sys
KD=str.maketrans('೦೧೨೩೪೫೬೭೮೯','0123456789')
def pages(path,heads=None,title=('ಸಾಯಣಭಾಷ್ಯಸಹಿತಾ','ಋಗ್ವೇದಸಂಹಿತಾ','ಸಾಯಣಭಾಷ್ಯಭೂಮಿಕೆ','ಸಾಯಣಭಾವ್ಯಸಹಿತಾ')):
    t=open(path,encoding='utf8',errors='replace').read(); b=t[t.find('<body'):]
    parts=re.split(r'<header[^>]*>(.*?)</header>',b,flags=re.S); out={}; cur=None; last=0
    for i in range(1,len(parts),2):
        h=html.unescape(re.sub(r'<[^>]+>','',parts[i])).strip(); body=parts[i+1]
        isp=any(x in h for x in title) or bool(re.search(r'(^[0-9]{1,4}\s+\S)|(\S\s+-?\s*[0-9]{1,4}$)',h) and len(h)>12 and not re.search('ಪಾರಃ|ಪಾಠಃ|ಪಾದಃ',h))
        if isp:
            m=re.findall(r'(?<![0-9೦-೯])[0-9]{1,4}(?![0-9೦-೯])',h)
            cur=int(m[0]) if m else last+1; last=cur; out.setdefault(cur,[])
            if heads is not None: heads.setdefault(cur,h)
        txt=html.unescape(re.sub(r'<[^>]+>','',re.sub(r'<br\s*/?>|</(p|div|h\d|li|aside)>','\n',body)))
        if cur is not None: out[cur].append((h if not isp else '')+'\n'+txt if not isp else txt)
    return {k:re.sub(r'\n\s*\n+','\n','\n'.join(v)).strip() for k,v in out.items()}

def pages_md(path,heads=None):
    """same for the markdown form: a running-head line (title + page number at either end) starts a page; image lines are dropped"""
    out={}; cur=None
    for l in open(path,encoding='utf8',errors='replace').read().split('\n'):
        if l.startswith('![') or 'base64,' in l: continue
        h=l.strip()
        if h and len(h)<100 and any(x in h for x in ('ಸಾಯಣಭಾಷ್ಯಸಹಿತಾ','ಋಗ್ವೇದಸಂಹಿತಾ','ಸಾಯಣಭಾಷ್ಯಭೂಮಿಕೆ')):
            m=re.findall(r'(?<![0-9೦-೯])[0-9]{1,4}(?![0-9೦-೯])',h)
            if m:
                cur=int(m[0]); out.setdefault(cur,[])
                if heads is not None: heads.setdefault(cur,h)
                continue
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
    p=pages(sys.argv[1]); print(len(p),'pages; printed',min(p),'-',max(p)); print([(k,len(v)) for k,v in sorted(p.items())][:20])
