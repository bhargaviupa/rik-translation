import re,glob,json,sys
from rapidfuzz import fuzz,process
U='/root/.claude/uploads/224fdbbf-d54a-585a-b1af-ff03016dade8/'
W='/tmp/claude-0/-home-user-rik-translation/224fdbbf-d54a-585a-b1af-ff03016dade8/scratchpad/'
KN=re.compile(r'[ಀ-೿]')
def norm(s):
    s=re.sub(r'[‌‍ೕೖ]','',s)
    return ''.join(KN.findall(s))
SKIP=re.compile(r'(ಋಗ್ವೇದಸಂಹಿತಾ|ಸಾಯಣಭಾಷ್ಯಸಹಿತಾ|ಭಾಷ್ಯಸಹಿತಾ|ಮಂ\.|ಅ\. ?[೦-೯]|^\W*[೦-೯0-9]{1,3}\W*$|^\W*(ಪದಪಾಠಃ|ಸಂಹಿತಾಪಾಠಃ|ಸಾಯಣಭಾಷ್ಯ[ಮಂ]?|ಪ್ರತಿಪದಾರ್ಥ|ಭಾವಾರ್ಥ|English Translation|ವಿಶೇಷವಿಷಯಗಳು)\W*$|^\W*[-=]*\W*$)')
PAT=re.compile(r'##\s*Page\s+(\d+)|^page\s+(\d+)\s*$|==Page\s*(\d+)',re.M|re.I)
def start_of(body,n=70):
    keep=[]
    for ln in body.split('\n'):
        l=ln.strip().strip('#*> ')
        if not l or SKIP.search(l) or re.match(r'^\[?Illustration',l): continue
        if not KN.search(l): continue
        keep.append(l)
        if len(norm(' '.join(keep)))>=n: break
    return norm(' '.join(keep))[:n]
def blocks():
    out={}
    srcs={f:open(f).read() for f in glob.glob(U+'*.md')}
    for i,l in enumerate(open(U+'a19c48aa-vol22_chunks.jsonl')): srcs[f'chunk{i}']=json.loads(l)['markdown']
    for f,t in srcs.items():
        ms=list(PAT.finditer(t))
        for i,m in enumerate(ms):
            lab=int(next(g for g in m.groups() if g)); e=ms[i+1].start() if i+1<len(ms) else len(t)
            body=t[m.end():e].replace('\n---\n','\n').strip()
            if len(body)<300: continue
            s=start_of(body)
            if len(s)<25: continue
            key=s[:40]
            cur=out.get(key)
            if cur is None or len(body)>len(cur['body']): out[key]={'label':lab,'files':set(),'body':body,'start':s}
            out[key]['files'].add(f[:8])
    return out
if __name__=='__main__':
    B=blocks(); print(len(B),'distinct page starts')
    ocr=json.load(open(W+'pdfocr/all.json'))
    P={r['pdf']:norm(start_of(r['body'],70)) for r in ocr}
    H={r['pdf']:re.sub(r'\D','',r['head']) for r in ocr}
    res=[]
    pdfs=list(P)
    for key,b in B.items():
        lab=b['label']
        cand=[(p,fuzz.partial_ratio(b['start'][:45],P[p])) for p in pdfs if P[p]]
        cand.sort(key=lambda x:-x[1]); top=cand[:3]
        res.append({'label':lab,'start':b['start'][:40],'top':top,'files':sorted(b['files']),'len':len(b['body'])})
    json.dump(res,open(W+'match.json','w'),ensure_ascii=False)
    print('matched',len(res))
