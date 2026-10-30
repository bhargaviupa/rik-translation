# w5d: tight zooms: z_w5d.sh PDF "line:x0:x1 line:x0:x1 ..." [dpi=600] -> /tmp/claude-0/sp/Z.png (stacked)
export V5WORK=/tmp/claude-0/sp/w/; P=$1; D=${3:-600}; i=0; rm -f /tmp/claude-0/sp/zz*.png
for s in $2; do IFS=: read l a b <<< "$s"; i=$((i+1)); python3 vol5/tools/ltile_w5c.py $P /tmp/claude-0/sp/zz$i.png $l $l $D 1 $a $b >/dev/null; done
python3 - <<'P'
from PIL import Image; import glob
fs=sorted(glob.glob('/tmp/claude-0/sp/zz*.png'),key=lambda f:int(f[19:-4].replace('zz','') or 0) if False else int(f.split('zz')[1][:-4])); I=[Image.open(f) for f in fs]
W=max(i.size[0] for i in I); out=Image.new('L',(W,sum(i.size[1]+10 for i in I)),255); y=0
for i in I: out.paste(i,(0,y)); y+=i.size[1]+10
out.save('/tmp/claude-0/sp/Z.png'); print(out.size)
P
