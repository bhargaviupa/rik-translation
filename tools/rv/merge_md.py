#!/usr/bin/env python3
"""Merge the user's machine-read markdown files of one volume into ONE file, losslessly.

  python3 tools/rv/merge_md.py OUT.md IN1.md IN2.md [...] [--write] [--first FIRST --last LAST (printed pages to compare, default: all)]

The files are concatenated in the order given. The converter's first line ('Markdown source') of the 2nd, 3rd … file is dropped; nothing else
changes. Before writing, the printed-page split (tools/rv/html_pages.pages_md) of every input and of the merged text are compared: the
pages that each input contributes must be identical (text) in the merged file, and no page may appear that no input has. Any difference
refuses to write. After merging: point volN/volcfg.json `source` at the merged file (`OUT.md@FIRST-LAST`) and `supplied_md` in pubcfg.json,
then `git rm` the inputs (history keeps them). When two inputs overlap in page numbers the later one wins in the comparison."""
import re, sys, pathlib
root = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(root / 'tools' / 'rv'))
import html_pages as H
args = [a for a in sys.argv[1:] if not a.startswith('--')]
out, ins = pathlib.Path(args[0]), [pathlib.Path(a) for a in args[1:]]
texts = [p.read_text(encoding='utf8') for p in ins]
parts = [texts[0].rstrip('\n')] + [re.sub(r'\A(Markdown source\n)+', '', t).rstrip('\n') for t in texts[1:]]
merged = '\n\n'.join(parts) + '\n'
tmp = out.with_suffix('.tmp.md'); tmp.write_text(merged, encoding='utf8')
try:
    pm = H.pages_md(str(tmp))
    expect = {}
    for p in ins:
        for k, v in H.pages_md(str(p)).items(): expect[k] = v
    # a page that is cut by the seam may legitimately differ only by whitespace
    diff = [k for k in expect if k not in pm or pm[k].strip() != expect[k].strip()]
    extra = [k for k in pm if k not in expect]
    print(f'{len(ins)} files, {len(expect)} pages in inputs, {len(pm)} in merged; different: {diff[:10]} ({len(diff)}); only in merged: {extra[:10]}')
    if diff or extra: sys.exit('REFUSED: the merged file does not split into the same pages')
    if '--write' in sys.argv: out.write_text(merged, encoding='utf8'); print('wrote', out)
finally:
    tmp.unlink(missing_ok=True)
