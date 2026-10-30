# w5d: line tiles of a PDF page: tiles_w5d.sh PDF FROM TO [per=3] [dpi=400] -> /tmp/claude-0/sp/L{n}.png
export V5WORK=/tmp/claude-0/sp/w/; P=$1; A=$2; B=$3; S=${4:-3}; D=${5:-400}; rm -f /tmp/claude-0/sp/L*.png
i=$A; n=1; while [ $i -le $B ]; do j=$((i+S-1)); [ $j -gt $B ] && j=$B
python3 vol5/tools/ltile_w5c.py $P /tmp/claude-0/sp/L$n.png $i $j $D 2 >/dev/null; i=$((j+1)); n=$((n+1)); done; ls /tmp/claude-0/sp/L*.png | wc -l
