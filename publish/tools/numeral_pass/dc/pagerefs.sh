#!/bin/bash
# usage: pagerefs.sh FIRSTPDF LASTPDF OUTDIR  -> OUTDIR/refs_<pdf>.png : enlarged crop of each reference + classifier reading (second opinion only)
cd "$(dirname "$0")/../../../.."
python3 publish/tools/numeral_pass/dc/refs.py Rig_Vol10.pdf $1 $2 $3/refs.json ${CLF:-/tmp/knum/out/clf.pkl} --crops $3/c >/dev/null
python3 - "$3" <<'PY'
import json,sys,cv2,numpy as np
d=sys.argv[1];r=json.load(open(d+'/refs.json'))
for pg,L in r.items():
    rows=[]
    for x in L:
        if x['conf']<0.5 or len(x['ref'])<3: continue
        im=cv2.imread(f"{d}/c/p{pg}_{x['x']}_{x['y']}.png",0)
        if im is None: continue
        im=cv2.resize(im,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)[:60,:460]
        c=np.full((82,470),255,np.uint8);c[:im.shape[0],:im.shape[1]]=im
        alt=''.join(str(t[0]) if t[1]>.8 else '?' for t in x['digits'])
        cv2.putText(c,f"y{x['y']}: {x['ref']}  (conf {x['conf']})",(2,78),cv2.FONT_HERSHEY_SIMPLEX,.5,0,1);rows.append(c)
    if rows: cv2.imwrite(f"{d}/refs_{pg}.png",np.vstack(rows))
PY
