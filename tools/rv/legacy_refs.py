"""Second reading of a re-translated volume against the old (scan-based) translation: per printed page, the numerals/references
(book.chapter.verse, verse numbers, sūtra numbers) found only in the old or only in the new English text; digits normalised
(Kannada/Devanagari -> ASCII).  Report only; nothing is changed.   python3 tools/rv/legacy_refs.py OLD.md NEW.md OUT.tsv"""
import re, sys, collections
DIG = {**{ord('೦') + i: str(i) for i in range(10)}, **{ord('०') + i: str(i) for i in range(10)}}
REF = re.compile(r'(?<![\d.])\d+(?:[-.]\d+)+(?![\d])')
def pages(path):
    out = collections.defaultdict(list); cur = None
    for l in open(path, encoding='utf8').read().split('\n'):
        m = re.match(r'### Printed p\. (\d+)', l)
        if m: cur = int(m.group(1)); continue
        if cur is not None: out[cur].append(l)
    return out
def refs(lines):
    t = re.sub(r'\*\*NOTE\*\*(\{[^}]*\})?', '', '\n'.join(lines)).translate(DIG)
    return collections.Counter(x.replace('.', '-') for x in REF.findall(t))
old, new = pages(sys.argv[1]), pages(sys.argv[2]); rows = 0
with open(sys.argv[3], 'w', encoding='utf8') as f:
    f.write('page\tonly_in_old\tonly_in_new\n')
    for p in sorted(set(old) | set(new)):
        a, b = refs(old.get(p, [])), refs(new.get(p, [])); oa, ob = sorted((a - b).elements()), sorted((b - a).elements())
        if oa or ob: f.write(f'{p}\t{" ".join(oa)}\t{" ".join(ob)}\n'); rows += 1
print(f'{rows} pages with differing references of {len(set(old) | set(new))}; written to {sys.argv[3]}')
