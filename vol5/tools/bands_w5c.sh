#!/bin/sh
# w5c: all bands of one PDF page: bands_w5c.sh PDF OUTDIR [from=0] [to=1]  -> OUTDIR/PDF_k.png (step 0.11, height 0.12)
P=$1; D=$2; A=${3:-0}; B=${4:-1}
python3 - "$P" "$D" "$A" "$B" <<'PY'
import sys,subprocess
p,d,a,b=sys.argv[1],sys.argv[2],float(sys.argv[3]),float(sys.argv[4]); k=0
while a<b-0.01:
    k+=1; subprocess.run(['python3','vol5/tools/tiles_w5c.py',p,f'{d}/{p}_{k}.png',f'{a:.3f}',f'{min(b,a+0.12):.3f}'],capture_output=True); a+=0.11
print(k)
PY
