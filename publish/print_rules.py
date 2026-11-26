#!/usr/bin/env python3
"""Print rules of REQUIREMENTS A4a (user's reading of the Vol 1 PDF, Nov 25 2026), applied to a volume's cleaned draft in memory (the .md files are never changed).

    import print_rules; md = print_rules.apply(md)       # used by build_vol1.py; any legacy build can call it

Rules done here (numbers = A4a): 1 no 'original p. N' marks, the sentence they cut is joined; 2 no translator remarks (`*( … )*` blocks and inline remarks, edition-note boxes,
named comments); 3 no 'p. N' leader tails of a translated contents list; 4 bold only for a heading or a short label, never a sentence; 5 Sanskrit alone on its line, the
transliteration on the next; 6 one Devanagari form per citation and one translation line; 8 a single hyphen between a word and its gloss; 9 prose transliteration ch for c.
Counts of what each rule did are printed by `apply(md, report=True)`."""
import re, collections
DEV = re.compile(r'[ऀ-ॿ]')
IAST = re.compile(r'[āīūṛṝḷṃḥṅñṭḍṇśṣĀĪŪṚṢŚ]')
STATS = collections.Counter()

def _dev_frac(s):
    letters = re.sub(r'[\s\W\d_]', '', s)
    return (len(DEV.findall(s)) / len(letters)) if letters else 0

def _blocks(md): return re.split(r'\n{2,}', md.strip('\n'))

def drop_remarks(blocks):
    out = []
    for b in blocks:
        t = b.strip()
        if re.match(r'^\*\(.*\)\*$', t.replace('\n', ' '), re.S) or t.startswith('<div class="edition-note">'):
            STATS['remark blocks dropped'] += 1; continue
        if re.match(r'^\*Opening invocatory verse \(a traditional Sanskrit shloka, not original to this author\):\*$', t):
            STATS['remark blocks dropped'] += 1; continue
        if re.match(r'^\*?The next pages \(17.18 of the PDF\)', t) or re.match(r'^\*\*(Editorial notice|Target for next session)', t):
            STATS['remark blocks dropped'] += 1; continue
        if re.match(r'^\*\*?(Honesty note|Pacing note)', t): STATS['remark blocks dropped'] += 1; continue
        n = len(re.findall(r'(?<!\*)\*\(.+?\)\*(?!\*)', b, flags=re.S))
        if n and not t.startswith(('>', '#', '|')):
            b = re.sub(r'\s*(?<!\*)\*\(.+?\)\*(?!\*)', '', b, flags=re.S); STATS['inline remarks dropped'] += n
            if not b.strip(): continue
        out.append(b)
    return out

def drop_pagemarks(blocks):
    """rule 1: remove 'original p. N' and join a sentence the mark cut"""
    out = []; i = 0
    mark = re.compile(r'^<div class="pgmark">[^<]*</div>$')
    for b in blocks:
        if mark.match(b.strip()):
            STATS['original-page marks removed'] += 1
            if out and out[-1] is not None:
                out.append(None)          # placeholder: decide on the next block
            continue
        if out and out[-1] is None:
            out.pop(); prev = out[-1] if out else ''
            if prev is None: prev = ''
            pt = prev.rstrip()
            cut = bool(pt) and not pt.startswith(('#', '>', '|', '<')) and (not re.search(r'[.!?:;”"\)\]\*]$', pt) or pt.endswith('…'))
            if cut and not b.lstrip().startswith(('#', '>', '|', '<', '*', '-')):
                out[-1] = re.sub(r'\s*…\s*$', '', pt) + ' ' + re.sub(r'^…\s*', '', b.lstrip()); STATS['sentences joined across a page mark'] += 1
                continue
        out.append(b)
    return [b for b in out if b is not None]

def contents_tails(md):
    n = len(re.findall(r'\s*\.{4,}\s*p\.\s*\d+', md))
    STATS['contents leader tails removed'] += n
    return re.sub(r'\s*\.{4,}\s*p\.\s*\d+', '', md)

def unbold(b):
    """rule 4: bold stays for a heading-like whole block or a short label; a sentence is never bold"""
    t = b.strip()
    if t.startswith(('#', '|', '<')): return b
    whole = re.fullmatch(r'\*\*([^*]+)\*\*', t)
    if whole:
        w = whole.group(1)
        if len(w.split()) <= 10 and not re.search(r'[.!?]$', w): return b
        STATS['bold sentences set in roman'] += 1; return w
    def sub(m):
        x = m.group(1)
        if len(x.split()) <= 4 and re.search(r'[:—]$', x.strip()) or (len(x.split()) <= 3 and not re.search(r'[.!?,;]', x)): return m.group(0)
        STATS['bold sentences set in roman'] += 1; return x
    return re.sub(r'\*\*([^*\n]+?)\*\*', sub, b)

def blockquote_fix(b):
    """rules 5, 6: in a Sanskrit blockquote keep one Devanagari form, put the transliteration and the translation on their own lines"""
    lines = [re.sub(r'^>\s?', '', l) for l in b.split('\n')]
    dev = [l for l in lines if l.strip() and _dev_frac(l) > .5]
    if not dev: return b
    keep = []; seen_dev = 0
    for l in lines:
        if l.strip() and _dev_frac(l) > .5:
            seen_dev += 1
            if seen_dev > 1: STATS['duplicate Devanagari lines dropped'] += 1; continue
            l = l.rstrip('* ')
        keep.append(l)
    # translation repeated by the paragraph that follows is handled in apply()
    out = []
    for l in keep:
        if l.strip() == '': continue
        out.append(l)
    return '\n'.join('> ' + l + '\n>' if True else l for l in out).rstrip('\n>').rstrip()

def split_mixed(b):
    """rule 5: a prose line that runs English into a Devanagari run: the run becomes its own quoted line"""
    t = b.strip()
    if t.startswith(('>', '#', '|', '<')) or not DEV.search(b): return [b]
    parts = re.split(r'((?:[ऀ-ॿ॥।][ऀ-ॿ॥।\s\-]*[ऀ-ॿ॥।]))', b)
    if len(parts) < 3: return [b]
    res = []
    for p in parts:
        if not p.strip(): continue
        if DEV.search(p) and _dev_frac(p) > .5 and len(p.split()) >= 2: res.append('> ' + p.strip()); STATS['mixed lines split'] += 1
        else: res.append(p.strip())
    return res

def hyphen_gloss(b):
    t = b.strip()
    if t.startswith(('#', '>', '|', '<')): return b
    n = b.count(' — ')
    STATS['dashes set as a single hyphen'] += n
    return b.replace(' — ', ' - ')

def prose_ch(b):
    """rule 9: in prose words with an IAST diacritic (outside italics): c -> ch, ch -> chh"""
    t = b.strip()
    if t.startswith(('#', '>', '|', '<')): return b
    segs = re.split(r'(\*[^*\n]+\*)', b)
    def word(w):
        if not IAST.search(w): return w
        w2 = re.sub(r'ch', 'chh', w); w2 = re.sub(r'c(?!h)', 'ch', w2).replace('Ch', 'Chh') if False else re.sub(r'(?<![ch])c(?!h)', 'ch', w2)
        if w2 != w: STATS['prose words c→ch'] += 1
        return w2
    for k, s in enumerate(segs):
        if s.startswith('*') and s.endswith('*') and len(s) > 2: continue
        segs[k] = re.sub(r"[\w'’ʼĀ-ſḀ-ỿ]+", lambda m: word(m.group(0)), s)
    return ''.join(segs)

def no_bold(b):
    """user, Nov 26 2026: nothing is bold except the chapter headings (the '# ' and '## ' lines, set in bold by the style sheet)"""
    out = []
    for l in b.split('\n'):
        if re.match(r'^#{1,2} ', l): out.append(l); continue
        n = l.count('**')
        l2 = re.sub(r'\*\*\*(.+?)\*\*\*', r'*\1*', l)
        l2 = re.sub(r'\*\*(.+?)\*\*', r'\1', l2).replace('**', '')
        if l2 != l: STATS['bold marks removed'] += max(1, n // 2)
        out.append(l2)
    return '\n'.join(out)

def apply(md, report=False):
    STATS.clear()
    md = md.replace('**Embedded English translation, as given in the source:**', '**Printed English translation:**')
    md = contents_tails(md)
    blocks = _blocks(md)
    blocks = drop_remarks(blocks)
    blocks = drop_pagemarks(blocks)
    out = []
    for b in blocks:
        if b.lstrip().startswith('>'): out.append(blockquote_fix(b)); continue
        for p in split_mixed(b):
            if p.startswith('> '): out.append(blockquote_fix(p)); continue
            p = unbold(p); p = hyphen_gloss(p); p = prose_ch(p)
            out.append(p)
    # a translation line quoted under a citation and then explained again by 'That is: …' : keep the explanation once
    res = []
    for i, b in enumerate(out):
        if b.startswith('>') and i + 1 < len(out) and re.match(r'^(That is|i\.e\.|That means)\b', out[i + 1].lstrip()):
            lines = b.split('\n'); k = [j for j, l in enumerate(lines) if re.match(r'^>\s*[“"].+[”"]\s*$', l)]
            if k:
                for j in reversed(k): del lines[j]
                b = '\n'.join(lines).rstrip('\n>').rstrip(); STATS['repeated translation lines dropped'] += 1
        res.append(b)
    res = [no_bold(b) for b in res]
    md2 = '\n\n'.join(res) + '\n'
    if report: print(dict(STATS))
    return md2
