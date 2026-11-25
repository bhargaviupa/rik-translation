#!/bin/sh
# usage: tools/rv/second_pass_prep.sh VOL A B SHEET   -- refresh the sieve segments (English changed) and write the reading sheet for pages A-B
python3 tools/rv/second_pass_sieve.py "$1" >/dev/null && python3 tools/rv/second_pass_page.py "$1" "$2-$3" --out "$4"
