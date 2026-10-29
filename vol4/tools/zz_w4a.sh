#!/bin/sh
# zz_w4a.sh PDF x0 y0 x1 y1 [...] : 450-dpi crops stacked and enlarged x2 -> /tmp/w4a/m3.png
g=$1; shift
python3 "$(dirname "$0")/mz_w4a.py" $g 450 /tmp/w4a/m.png "$@" >/dev/null && python3 -c "
from PIL import Image; im=Image.open('/tmp/w4a/m.png'); im.resize((im.width*2,im.height*2),Image.LANCZOS).save('/tmp/w4a/m3.png'); print(im.size)"
