"""rv — one tool for every volume (docs/DESIGN.md §9).   python3 -m rv VERB VOL [options]

  structure VOL --mandalas 3,4    cut the volume into units from its Kannada text and the reference verses; structure report
  import VOL                      lay the volume's existing English into the units; alignment report
  print VOL [--pdf]               working copy (.md) and review copy printed from the units, in the final format
Built so far: Phase A of DESIGN §12 (these three verbs).  Nothing here changes a volume's existing files."""
import sys
def main():
    a = sys.argv[1:]
    if len(a) < 2: sys.exit(__doc__)
    verb, vol = a[0], int(a[1]); opt = lambda k, d=None: a[a.index(k) + 1] if k in a else d
    if verb == 'structure':
        from . import structure; structure.build(vol, [int(x) for x in opt('--mandalas').split(',')])
    elif verb == 'import':
        from . import importer; importer.run(vol)
    elif verb == 'print':
        from . import printer; printer.run(vol, pdf='--pdf' in a)
    else: sys.exit(__doc__)
main()
