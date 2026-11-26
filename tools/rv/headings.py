#!/usr/bin/env python3
"""Title structure of a prose volume: chapter - level 1 - level 2 - level 3 (user, Nov 26 2026; REQUIREMENTS A4 print rule 17).

  python3 tools/rv/headings.py N [--outline]     writes volN/data/headings_kn.tsv and volN/data/headings_en.tsv (the books are not changed)

The structure is taken from the ORIGINAL (the Kannada text made from the supplied text), by script:
  title line  a short line (at most 45 letters) after the end of a sentence or an empty line and before a longer line, without daṇḍa or
              reference number.  A numbered line counts only if it is not part of a list (no numbered line next to it).
  chapter     'ಒಂದನೆಯ ಪ್ರಕರಣ' (N-th chapter); the line after it is the chapter's title.
  level 1     a title that stands directly above another title (it heads a group), or one of the topics the original lists for the chapter
              in its own contents pages, unless it is the second of two titles standing together or a sibling of such a one.
  level 2     the title under a level-1 title, its siblings (same last element, e.g. -ಸಂಹಿತಾ), and every other title.
  level 3     a numbered title.
The English headings follow: on each printed page the headings and bold label lines of the English file are paired with the Kannada
titles of that page in order, by their place on the page; a paired English line takes the level of its Kannada title (a bold label line
becomes a heading), an English heading with no Kannada title beside it keeps its place as level 2 and is listed as 'unpaired'.
Both files have a column 'use' (y/n) and 'level' that the editor may change; volN/data/headings_overrides.tsv (line or text, level) is
applied on top at every run, so hand corrections survive.  The print builds read the two files (publish/volbook.py Kannada book;
publish/vol1_clean.py through apply_en)."""
import os, re, sys, collections
from rapidfuzz import fuzz
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CH = re.compile(r'^([^\s#>*|<\[]\S*ನೆಯ ಪ್ರಕರಣ)(?:ವು)?(?![\u0c80-\u0cff])\s*[.—-]*\s*(.*)$')
ATTR = re.compile(r'\s*\{\.[\w-]+\}\s*$')           # '{.headline}' left on a line by the conversion of the supplied file
NUMBERED = re.compile(r'^[(\[]?[\d೦-೯]{1,2}[.)\]]')
def kn_file(vol):
    for p in (f'vol{vol}/Rigveda_Samhita_Vol{vol}_Kannada_Text.md', f'vol{vol}/kannada/Rigveda_Samhita_Vol{vol}_Kannada_Text.md'):
        if os.path.exists(os.path.join(ROOT, p)): return os.path.join(ROOT, p)
def en_files(vol):
    d = os.path.join(ROOT, f'vol{vol}')
    return [os.path.join(d, x) for x in sorted(os.listdir(d)) if x.endswith('English_Translation.md') and '_scan_' not in x]
def norm(s): return re.sub('[^ಀ-೿]', '', s)
def overrides(vol):
    f = os.path.join(ROOT, f'vol{vol}', 'data', 'headings_overrides.tsv'); o = {}
    if os.path.exists(f):
        for l in open(f, encoding='utf8').read().split('\n')[1:]:
            c = l.split('\t')
            if len(c) >= 2 and c[0].strip(): o[c[0].strip()] = c[1].strip()
    return o
def kannada(vol):
    L = open(kn_file(vol), encoding='utf8').read().split('\n')
    first = next(i for i, l in enumerate(L) if l.startswith('<!-- printed 2 -->'))
    topics, cur = {}, None
    for l in L[:first]:
        m = CH.match(l.strip())
        if m and re.search('[—-]', l): cur = norm(m.group(1)); topics[cur] = []; l = m.group(2)
        if cur: topics[cur] += [t.strip(' .0123456789೦೧೨೩೪೫೬೭೮೯') for t in re.split(r'—|--|-(?=[ಀ-೿])|\.\s', l) if len(norm(t)) >= 4]
    rows, page, chap, pstart = [], None, None, first
    for i in range(first, len(L)):
        l = L[i]; t = ATTR.sub('', l.strip())
        m = re.match(r'<!-- printed (\d+) -->', l)
        if m: page = int(m.group(1)); pstart = i; continue
        if not t or t.startswith(('>', '*', '#', '|', '<', '[')): continue
        prev = ATTR.sub('', L[i - 1].strip()); nxt = ATTR.sub('', L[i + 1].strip()) if i + 1 < len(L) else ''
        c = CH.match(t)
        if c and len(t) <= 75 and not re.search(r'[।॥]', t):
            chap = norm(c.group(1)); title = c.group(2).strip() or (nxt if 0 < len(nxt) <= 60 else '')
            t = c.group(1)
            rows.append({'line': i + 1, 'page': page, 'level': 'chapter', 'text': t.rstrip('. '), 'extra': title.rstrip('. '), 'off': i - pstart}); continue
        if rows and rows[-1]['level'] == 'chapter' and rows[-1]['line'] == i and rows[-1]['extra'] and rows[-1]['extra'] == t.rstrip('. '): continue
        if len(t) > 45 or not re.search('[ಀ-೿]', t) or re.search(r'[।॥]|\d-\d|[೦-೯]-[೦-೯]', t) or t.endswith((',', ';', '—', '-')): continue
        if not (not prev or prev.endswith(('.', '?', '।', '॥', ':')) or prev.startswith(('<', '*')) or (rows and rows[-1]['line'] == i)) or (len(nxt) <= len(t) and not (len(nxt) <= 45 and nxt)): continue
        nx2 = L[i + 2].strip() if i + 2 < len(L) else ''
        if re.search(r'[।॥]', nxt) and len(nxt) < 70: continue                                        # first line of a quoted verse
        if re.match(r'^[\d೦-೯]+\s', t) or re.search(r'\s[\d೦-೯]+$', t) or len(t.split()) > 6 or ',' in t: continue   # a running head, a sentence
        if t.endswith(('ಃ', 'ತ್', 'ಮ್')) and not NUMBERED.match(t): continue                              # a line of Sanskrit
        short = lambda x: 0 < len(x) <= 45 and not re.search(r'[।॥.]$', x)
        if not NUMBERED.match(t) and short(prev) and short(nxt): continue                              # inside a list or chart of names
        if not NUMBERED.match(t) and short(nxt) and short(nx2) and not CH.match(prev): continue        # the first of three or more short lines
        if NUMBERED.match(t):
            if NUMBERED.match(prev) or NUMBERED.match(nxt) or len(nxt) < 50: continue                 # an item of a list, not a title
            rows.append({'line': i + 1, 'page': page, 'level': '3', 'text': t, 'extra': '', 'off': i - pstart}); continue
        if len(nxt) <= len(t) and not (rows and rows[-1]['line'] == i): pass
        best = max((fuzz.ratio(norm(t), norm(x)) for x in topics.get(chap, [])), default=0)
        rows.append({'line': i + 1, 'page': page, 'level': '1' if best >= 80 else '2', 'text': t.rstrip('. '), 'extra': 'in the original contents' if best >= 80 else '', 'off': i - pstart, 'chap': chap})
    # groups: a title directly above another title heads it; the one below, and its siblings in the chapter, are level 2
    for a, b in zip(rows, rows[1:]):
        if a['level'] in '12' and b['level'] in '12' and b['line'] - a['line'] == 1 and a['level'] != 'chapter':
            a['level'] = '1'; b['level'] = '2'; b['child'] = True
    sib = collections.defaultdict(set)
    for r in rows:
        if r.get('child'): sib[r.get('chap')].add(norm(r['text'])[-5:])
    for r in rows:
        if r['level'] == '1' and not any(x['line'] == r['line'] + 1 for x in rows) and norm(r['text'])[-5:] in sib[r.get('chap')]: r['level'] = '2'
    ov = overrides(vol)
    for r in rows:
        k = ov.get(f'kn:{r["line"]}') or ov.get('kn:' + r['text'])
        if k: r['level'] = k
    # chapter titles: the line under the chapter line; where that is a sentence or garbled, the title the original's contents give
    ctitle = {}
    for l in L[:first]:
        m = CH.match(l.strip())
        if m and re.search('[—-]', l): ctitle[norm(m.group(1))] = re.sub(r'[\s.\d೦-೯]+$', '', m.group(2).strip())
    last_ch = 0
    for r in rows:
        if r['level'] == 'chapter':
            last_ch = r['line']; e = r['extra']
            if not e or len(e) > 45 or re.search('[A-Za-z~]', e): r['extra'] = ctitle.get(norm(CH.match(r['text']).group(1)), e if len(e) <= 45 else '')
    # the chapters end where the next part of the book begins (no chapter line after it): titles are proposed inside the chapters only
    end = next((i for i in range(last_ch, len(L)) if re.search('ಪೂರ್ವಪೀಠಿಕೆಯು ಸಮಾಪ್ತ|ಪೂರ್ವಪೀಠಿಕೆ ಸಮಾಪ್ತ|ಭಾಷ್ಯಭೂಮಿಕಾ$|ಸಾಯಣಭಾಷ್ಯಭೂಮಿಕೆ$', L[i].strip())), None)
    if end is None:
        nxt = [int(m.group(1)) for m in (re.match(r'<!-- printed (\d+) -->', x) for x in L) if m]
        end = len(L)
    rows = [r for r in rows if r['level'] != 'drop' and (r['level'] == 'chapter' or r['line'] <= end)]
    return rows, L
def english(vol, krows):
    bypage = collections.defaultdict(list)
    for r in krows: bypage[r['page']].append(r)
    out = []
    for f in en_files(vol):
        L = open(f, encoding='utf8').read().split('\n'); name = os.path.basename(f); page, pstart, items = None, 0, []
        plen = {}
        def close(end, nextpage=None):
            nonlocal items
            if page is None: items = []; return
            # the English file does not mark every page: its text up to the next page heading covers the pages page .. nextpage-1
            span = list(range(page, max(page + 1, min(nextpage or page + 1, page + 12))))
            ks = [k for q in span for k in bypage.get(q, []) if k['level'] != 'chapter']; n = max(1, end - pstart)
            kpos = [((span.index(k['page']) + min(k['off'], 39) / 40) / len(span), k) for k in ks]; used = set(); lastk = -1
            for it in items:
                it['pos'] = (it['i'] - pstart) / n
                if it['kind'] == 'chapter': continue
                cand = [(abs(p - it['pos']), j) for j, (p, k) in enumerate(kpos) if j not in used and j > lastk]
                def numok(j):
                    a_ = re.match(r'\s*\(?(\d{1,2})[.)]', it['text']); b_ = re.match(r'\s*\(?([\d೦-೯]{1,2})[.)]', kpos[j][1]['text'])
                    return not (a_ and b_) or int(a_.group(1)) == int(b_.group(1).translate(str.maketrans('೦೧೨೩೪೫೬೭೮೯', '0123456789')))
                cand = [c_ for c_ in cand if numok(c_[1])]                                   # '7. Guṇaviṣṇu' is not '೨. …'
                if cand and min(cand)[0] <= 0.3:
                    j = min(cand)[1]; used.add(j); lastk = j; it['kn'] = kpos[j][1]
            # equal numbers of headings on both sides: pair them in order whatever their place
            heads = [it for it in items if it['kind'] in ('h', 'pt')]
            if len(heads) == len(ks) and ks:
                for it in items: it.pop('kn', None)
                for it, k in zip(heads, ks): it['kn'] = k
            for it in items:
                k = it.get('kn')
                if it['kind'] == 'b' and not k: continue                                  # a bold label with no title beside it stays a label
                lvl = 'chapter' if it['kind'] == 'chapter' else (k['level'] if k else '3')      # no title of the original beside it: kept, as the lowest level
                out.append({'file': name, 'page': page, 'old': L[it['i']], 'level': lvl, 'title': it['text'], 'kn': k['text'] if k else '', 'state': 'paired' if k or it['kind'] == 'chapter' else 'unpaired'})
            items = []
        for i, l in enumerate(L):
            m = re.match(r'(#{2,4}) \[?Pages? (\d+)[^—]*?(?:—\s*(.*))?$', l)                      # any page heading; a title only after a dash
            if m:
                close(i, int(m.group(2))); page = int(m.group(2)); pstart = i
                t = (m.group(3) or '').strip()
                if t and not re.search(r'continued\)?$', t, re.I): items.append({'i': i, 'kind': 'pt', 'text': t})
                continue
            if page is None: continue
            h = re.match(r'(#{1,5}) (.*)', l)
            if h:
                t = h.group(2).strip()
                if h.group(1) == '#' : continue
                items.append({'i': i, 'kind': 'chapter' if re.match(r'Chapter\b', t) and h.group(1) == '##' else 'h', 'text': t}); continue
            b = re.fullmatch(r'\*\*([^*]{3,70})\*\*', l.strip())
            if b and not re.search(r'[.!?]$', b.group(1).strip()) and len(b.group(1).split()) <= 9: items.append({'i': i, 'kind': 'b', 'text': b.group(1).strip().rstrip(':')})
        close(len(L))
    ov = overrides(vol); lastp = max((k['page'] for k in krows if k['level'] != 'chapter'), default=0) + 10
    for r in out:
        k = ov.get('en:' + r['title'])
        if k: r['level'] = k
        r['use'] = 'n' if (r['state'] == 'unpaired' and r['page'] > lastp) or r['level'] == 'drop' else 'y'    # beyond the chapters nothing is proposed
    return out
def write(vol, krows, erows):
    d = os.path.join(ROOT, f'vol{vol}', 'data'); os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, 'headings_kn.tsv'), 'w', encoding='utf8') as o:
        o.write('line\tprinted page\tlevel\ttitle\tchapter title / note\tuse\n')
        for r in krows: o.write(f"{r['line']}\t{r['page']}\t{r['level']}\t{r['text']}\t{r['extra']}\ty\n")
    with open(os.path.join(d, 'headings_en.tsv'), 'w', encoding='utf8') as o:
        o.write('file\tprinted page\tlevel\ttitle\tKannada title beside it\tstate\tuse\told line\n')
        for r in erows: o.write(f"{r['file']}\t{r['page']}\t{r['level']}\t{r['title']}\t{r['kn']}\t{r['state']}\t{r['use']}\t{r['old']}\n")
def apply_kn(text, vol):
    """the Kannada text with its title lines marked as headings by level (print build; the file is not changed): by line number of the
    file as it stands, so this is applied before anything else touches the text"""
    f = os.path.join(ROOT, f'vol{vol}', 'data', 'headings_kn.tsv')
    if not os.path.exists(f): return text, 0
    L = text.split('\n'); n = 0
    for l in open(f, encoding='utf8').read().split('\n')[1:]:
        c = l.split('\t')
        if len(c) < 6 or c[5] != 'y': continue
        i = int(c[0]) - 1
        if i >= len(L) or norm(L[i])[:6] != norm(c[3])[:6]: continue                          # the file has changed since the list was made
        if c[2] == 'chapter':
            j = next((k for k in range(i + 1, min(i + 3, len(L))) if L[k].strip()), None)
            if j is not None and c[4] and norm(L[j])[:6] == norm(c[4])[:6] and not L[j].startswith(('<', '#')): L[j] = ''          # the title line goes into the heading
            L[i] = '\n## ' + c[3] + (' — ' + c[4] if c[4] else '') + '\n'
        else: L[i] = '\n' + '#' * (2 + int(c[2])) + ' ' + c[3] + ' {.lv' + c[2] + '}\n'
        n += 1
    return '\n'.join(L), n
def apply_en(text, vol, filename):
    """the English file's text with its heading lines marked by level (used by the print build; the file itself is not changed)"""
    f = os.path.join(ROOT, f'vol{vol}', 'data', 'headings_en.tsv')
    if not os.path.exists(f): return text, 0
    want = {}
    for l in open(f, encoding='utf8').read().split('\n')[1:]:
        c = l.split('\t')
        if len(c) >= 8 and c[0] == filename and c[6] == 'y' and c[2] in ('1', '2', '3'): want[c[7]] = (c[2], c[3])
    out, n = [], 0
    for l in text.split('\n'):
        w = want.get(l)
        if w:
            n += 1; lvl, title = w
            pm = re.match(r'(#{2,4} \[?Pages? [^—]*?)\s*—', l)
            if pm: out += [pm.group(1).rstrip(), '']                                           # the page heading stays a page heading
            out.append('#' * (2 + int(lvl)) + ' ' + title + ' {.lv' + lvl + '}')
        else: out.append(l)
    return '\n'.join(out), n
def main():
    vol = int(sys.argv[1]); krows, L = kannada(vol); erows = english(vol, krows); write(vol, krows, erows)
    c = collections.Counter(r['level'] for r in krows); e = collections.Counter((r['level'], r['state']) for r in erows)
    print('Kannada titles:', dict(c)); print('English headings:', {f'{k[0]} {k[1]}': v for k, v in sorted(e.items())})
    if '--outline' in sys.argv:
        ind = {'chapter': '', '1': '  ', '2': '    ', '3': '      '}
        for r in krows: print(f"{ind[r['level']]}{'§ ' if r['level']=='chapter' else ''}{r['text']}{' — ' + r['extra'] if r['level']=='chapter' and r['extra'] else ''}  [p.{r['page']} l.{r['line']}]")
if __name__ == '__main__': main()
