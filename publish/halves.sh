#!/bin/bash
# halves.sh N : two 200-dpi halves of scan-B page for printed page N (PDF = N+14)
n=$1; p=$((n+14))
pdftoppm -jpeg -r 200 -f $p -l $p -x 100 -y 150 -W 1520 -H 830 /home/user/scanB/Rig_Vol2_B.pdf /tmp/cmp/h${n}a
pdftoppm -jpeg -r 200 -f $p -l $p -x 100 -y 950 -W 1520 -H 830 /home/user/scanB/Rig_Vol2_B.pdf /tmp/cmp/h${n}b
