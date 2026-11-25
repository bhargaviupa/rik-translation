#!/bin/sh
# usage: tools/rv/second_pass_merge.sh VOL A B NEXT_A NEXT_B SHEET -- append batch_A-B.tsv to findings.tsv, apply, prepare the next sheet
D=vol$1/review/second_pass
tail -n +2 $D/batch_$2-$3.tsv >> $D/findings.tsv && python3 tools/rv/second_pass_apply.py $1 && tools/rv/second_pass_prep.sh $1 $4 $5 $6
