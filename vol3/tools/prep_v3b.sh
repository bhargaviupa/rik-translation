#!/bin/bash
# prep_v3b.sh "HEADING PREFIX" PDF... : print the section (no IAST lines) and render 6 strips per page at 400 dpi
cd /home/user/rik-translation/vol3
F=Rigveda_Samhita_Vol3_English_Translation.md
a=$(grep -n -F "$1" $F | head -1 | cut -d: -f1)
awk -v a=$a 'NR>a && /^(### Pages|## )/{exit} NR>=a' $F | grep -v '^> \*'
shift; cd tools
for g in "$@"; do for i in 0 1 2 3 4 5; do python3 zoomreg_v3b.py $g 0 $(python3 -c "print($i/6-0.01 if $i else 0)") 1 $(python3 -c "print(min(1,($i+1)/6+0.01))") /tmp/v3num/p${g}_$i.png 1 >/dev/null; done; done
