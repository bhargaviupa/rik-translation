# w5d: prep a printed page: refs list + 600-dpi paren montage. prep_w5d.sh PRINTED [PDF]
P=$1; G=${2:-$(($1+16))}; rm -f /tmp/claude-0/sp/Q*.png
python3 vol5/tools/refs_w5d.py $P
V5WORK=/tmp/claude-0/sp/w/ python3 vol5/tools/parens_w5d.py $G /tmp/claude-0/sp/Q 600 1150 1400
