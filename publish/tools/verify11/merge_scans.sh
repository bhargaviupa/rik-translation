#!/bin/sh
# usage: merge_scans.sh scan_1-70.pdf scan_71-140.pdf [more.pdf ...]  -> $VERIFY_WORK/new.pdf
W="${VERIFY_WORK:-$HOME/verify_work}"; mkdir -p "$W"; pdfunite "$@" "$W/new.pdf" && pdfinfo "$W/new.pdf" | grep Pages
