import re,json,glob,collections,hashlib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import match as M
CONS=re.compile(r'[ಕ-ಹ]')
sk=lambda s:''.join(CONS.findall(s))
# text blocks: every distinct block body >=300 chars in any file (keep source info)
U=M.U; blocks={}
srcs={f:open(f).read() for f in glob.glob(U+'*.md')}
for i,l in enumerate(open(U+'a19c48aa-vol22_chunks.jsonl')): srcs[f'chunk{i}']=json.loads(l)['markdown']
srcs['extra']=open('chunk_extra.md').read()
for f,t in srcs.items():
    ms=list(M.PAT.finditer(t))
    for i,m in enumerate(ms):
        lab=int(next(g for g in m.groups() if g)); e=ms[i+1].start() if i+1<len(ms) else len(t)
        body=t[m.end():e].replace('\n---\n','\n').strip()
        if len(body)<300: continue
        h=hashlib.md5(body.encode()).hexdigest()
        b=blocks.setdefault(h,{'label':lab,'files':set(),'body':body}); b['files'].add(f[-12:-3])
B=list(blocks.values()); print(len(B),'distinct text blocks')
pdf=[open(f'pdfocr/full{n}.txt').read() for n in range(1,627)]
docs=[sk(b['body']) for b in B]+[sk(t) for t in pdf]
vec=TfidfVectorizer(analyzer='char',ngram_range=(3,4),sublinear_tf=True,min_df=2,max_df=0.5)
X=vec.fit_transform(docs); XB=X[:len(B)]; XP=X[len(B):]
S=(XB@XP.T).toarray()                      # blocks x pdf pages
np.save('S.npy',S)
json.dump([{'body':b['body'],'label':b['label'],'files':sorted(b['files']),'len':len(b['body'])} for b in B],open('blocks_meta.json','w'))
best_pdf=S.argmax(1); best_sc=S.max(1)
print('block best-sim: median %.2f; >=0.5: %d; 0.3-0.5: %d; <0.3: %d'%(np.median(best_sc),(best_sc>=.5).sum(),((best_sc>=.3)&(best_sc<.5)).sum(),(best_sc<.3).sum()))
# per PDF page: best block
pb=S.argmax(0); ps=S.max(0)
print('pdf pages with a block sim>=0.5: %d, 0.3-0.5: %d, <0.3: %d'%((ps>=.5).sum(),((ps>=.3)&(ps<.5)).sum(),(ps<.3).sum()))
