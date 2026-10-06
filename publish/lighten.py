"""Print/Word-only lightening of bold in Volume 2 (the closed .md is never changed).
Keep bold for: (a) a block/line that is only a bold label; (b) a leading label like **Translation:**;
(c) the first bold span of a gloss line that starts with a headword followed by a dash (e.g. '**चित्रभानो (citrabhāno)** — ...').
All other inline bold becomes plain text."""
import re
BOLD = re.compile(r'\*\*([^*\n]+?)\*\*')
LEAD = re.compile(r'^((?:>\s*)*(?:[-*]\s+|\d+\.\s+|\(\d+\)\s+)?)')
def _line(l):
    if '**' not in l: return l
    st = l.strip()
    if re.fullmatch(r'(?:>\s*)?\*\*[^*]+\*\*:?\s*', st): return l           # whole line is a label
    m = LEAD.match(l); pre, rest = m.group(1), l[m.end():]
    if re.match(r'\*\*(Translation|English Translation|Gloss)[^*]*\*\*', rest):  # label then text
        mm = BOLD.match(rest); return pre + mm.group(0) + BOLD.sub(lambda x: x.group(1), rest[mm.end():])
    mm = BOLD.match(rest)
    if mm and (mm.group(1).rstrip().endswith(':') or re.match(r'\s*(—|–|-|:)\s', rest[mm.end():])):                  # leading headword + dash
        return pre + mm.group(0) + BOLD.sub(lambda x: x.group(1), rest[mm.end():])
    return pre + BOLD.sub(lambda x: x.group(1), rest)
def lighten(md):
    out = []
    for l in md.split('\n'):
        if l.startswith('#') or l.startswith('|') or l.startswith('<'): out.append(l); continue   # headings, tables, html untouched
        out.append(_line(l))
    return '\n'.join(out)
if __name__ == '__main__':
    import sys, pathlib
    s = pathlib.Path(sys.argv[1]).read_text(encoding='utf-8'); t = lighten(s)
    n0 = len(BOLD.findall(s)); n1 = len(BOLD.findall(t)); print(n0, '->', n1)
