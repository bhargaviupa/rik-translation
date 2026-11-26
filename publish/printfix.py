"""Fixes applied to the finished HTML of every print build, just before the PDF is made (build.py and its build_vol*.py, volbook.py).

label_paragraphs: a paragraph that consists ONLY of one bold run (a label such as "**Third: the slaying of Vritrasura.**") is set as a centred
line; one that consists only of one italic run is a small grey line in volbook.  The stylesheets used to pick these with
`p > strong:only-child` / `p > em:only-child`, which also matches a paragraph of running text that merely contains one bold or italic run
(CSS does not count the text around it): "**(1)** At the beginning of the book …" came out as a centred "(1)" on a line of its own, while
"**(2)** *The Bhashya-bhumika* …" (two runs) did not (Vol 1, PDF p. 19; user, Nov 26 2026).  The paragraphs are now marked here by class
(`only-strong`, `only-em`) and the stylesheets select the class."""
import re
_ONLY = re.compile(r'<p>\s*<(strong|em)>((?:(?!</?\1>).)*)</\1>\s*</p>', re.S)
def label_paragraphs(doc):
    return _ONLY.sub(lambda m: f'<p class="only-{m.group(1)}"><{m.group(1)}>{m.group(2)}</{m.group(1)}></p>', doc)

_OLSTART = re.compile(r'<ol([^>]*?) start="(\d+)"([^>]*)>')
_SPLIT = re.compile(r'</ol>(\s*<(?:div|h3) class="(?:pgmark|pg)"[^>]*>[^<]*(?:<span>[^<]*</span>)?\s*</(?:div|h3)>\s*)<ol ')
def lists(doc):
    """A numbered list that goes on after a page mark: WeasyPrint ignores <ol start="7"> and began again at 1 (Vol 1 PDF p. 22, the
    bibliography); the start is set as a counter, and the two halves lose the gap between them."""
    doc = _SPLIT.sub(lambda m: '</ol>' + m.group(1) + '<ol class="cont" ', doc)
    return _OLSTART.sub(lambda m: f'<ol{m.group(1)} start="{m.group(2)}" style="counter-reset: list-item {int(m.group(2)) - 1}"{m.group(3)}>', doc)

# ---- contents pages: ONE format in every volume and builder (user, Nov 26 2026): a table  No. | Contents | Page
def contents_table(rows, note='Page numbers are the pages of this book.', head=('No.', 'Contents', 'Page')):
    """rows: dicts {kind: 'row'|'head', no, html, href (link target, page of THIS book printed by CSS) or page (text printed as it is), pre (html put
    in front of the row's text, e.g. an invisible page mark)}.  Styling: style_footer.css, table.contents."""
    out = ['<table class="contents"><thead><tr><th class="no">%s</th><th>%s</th><th class="pg">%s</th></tr></thead><tbody>' % head]
    for r in rows:
        if r.get('kind') == 'head':
            out.append(f'<tr class="hd"><td colspan="3">{r.get("pre", "")}{r["html"]}</td></tr>'); continue
        pg = f'<a class="pgref" href="{r["href"]}"></a>' if r.get('href') else (r.get('page') or '')
        out.append(f'<tr><td class="no">{r.get("no") or ""}</td><td class="tx">{r.get("pre", "")}{r["html"]}</td><td class="pg">{pg}</td></tr>')
    out.append('</tbody></table>' + (f'<p class="cnote">{note}</p>' if note else ''))
    return '\n'.join(out)

_SEC = re.compile(r'(<h[23][^>]*>(?:(?!</h[23]>).)*Table of Contents(?:(?!</h[23]>).)*</h[23]>)(.*?)(?=<h[12][ >])', re.S)
_ENTRY = re.compile(r'^(.*?)(?:\s*—\s*|\s+)pp?\.\s*([0-9ivxlc]+)(?:[–-][0-9ivxlc]+)?\.?\s*(\[[^\]]*\])?\s*$', re.S)
_LEAD = re.compile(r'^\s*<strong>\s*(?:Chapter\s+)?(\d+|[A-Z][a-z]+(?:-[a-z]+)?)\s*—\s*(.*?)</strong>\s*', re.S)
def contents_sections(doc):
    """Old builders: a section of the body headed '… Table of Contents' (the original's contents pages, translated) is set as the table.
    An entry is a paragraph ending in '— p. N'; '**Chapter 4 — Title** text' gives the number.  The page printed is the page of THIS book
    (link to the mark of the original's page N), as REQUIREMENTS C9 asks; where that page has no mark, the cell is empty."""
    ids = set(re.findall(r'<div class="pgmark" id="(p[0-9ivxlc]+)"', doc))
    def sec(m):
        rows, pre, end, nlast = [], '', 0, 0        # the table ends with the last entry that has a page; what follows (a key to abbreviations …) stays as it is
        for part in re.finditer(r'<div class="pgmark"[^>]*></div>|<p[^>]*>(.*?)</p>|<(h3|h4)[^>]*>(.*?)</\2>|<(ul|ol|blockquote|table)\b.*?</\4>', m.group(2), flags=re.S):
            t = part.group(0)
            if t.startswith('<div'): pre += t; continue
            if part.group(2): rows.append({'kind': 'head', 'html': '<strong>' + part.group(3) + '</strong>', 'pre': pre}); pre = ''; continue
            if part.group(4): rows.append({'kind': 'head', 'html': t, 'pre': pre}); pre = ''; continue
            inner = part.group(1); e = _ENTRY.match(inner); body = e.group(1) if e else inner; no = ''
            lead = _LEAD.match(body)
            if lead: no = lead.group(1); body = '<strong>' + lead.group(2) + '</strong> ' + body[lead.end():]
            elif e and not body.lstrip().startswith('<strong>'):
                # an entry that opens with the name of a section which is a heading later in the book ("The counter-view (uttara-paksha): …"):
                # the opening words up to the colon or dash are set in bold (user, Nov 26 2026)
                hd = re.match(r'^(\s*[^<:—]{3,70}?(?::|\s—))(\s)', body)
                if hd: body = '<strong>' + hd.group(1).rstrip(' —') + ('' if hd.group(1).rstrip().endswith(':') else ' —') + '</strong>' + hd.group(2) + body[hd.end():]
            row = {'no': no, 'html': body + ((' ' + e.group(3)) if e and e.group(3) else ''), 'pre': pre}; pre = ''
            if e and ('p' + e.group(2)) in ids: row['href'] = '#p' + e.group(2)
            rows.append(row)
            if e: end, nlast = part.end(), len(rows)
        if sum(1 for r in rows if r.get('href')) < 3: return m.group(0)          # not a contents list after all
        return m.group(1) + contents_table(rows[:nlast]) + m.group(2)[end:]
    return _SEC.sub(sec, doc)
_HEAD = re.compile(r'<(h1|h2) class="(part|book|chapter)([^"]*)"([^>]*)>(.*?)</\1>', re.S)
_ORIG = re.compile(r'^(.*\S)\s*\(([^()]*)\)\s*$', re.S)
def headings(doc):
    """Part and chapter headings (user, Nov 26 2026): (1) cut properly into two lines, the number or kind on the first ("PART I",
    "Chapter One", "Table of Contents"), the title under it, never broken by chance in the middle of the title; (2) a part heading, and the
    headings "Introduction (…)" / "Preface (…)", show the English name only: the original's name in the trailing parenthesis goes to the
    footer (data-orig -> style_footer.css)."""
    def rep(m):
        tag, cls, more, attrs, inner = m.groups(); orig = ''
        text = inner.strip()
        o = _ORIG.match(text)
        if o and '<' not in o.group(2) and (cls in ('part', 'book') or re.match(r'(Introduction|Preface)\b', text)):
            text, orig = o.group(1), o.group(2)
        cut = re.match(r'((?:PART|Part|BOOK|Book) [^:<]{1,12}):\s*(.+)$', text, re.S) or re.match(r'(Chapter [\w-]+)\s*(?:—|\.)\s*(.+)$', text, re.S) \
              or re.match(r'([^<—]{3,40}?)\s+—\s+(.+)$', text, re.S)
        body = f'<span class="ht1">{cut.group(1)}</span><span class="ht2">{cut.group(2)}</span>' if cut else text
        d = f' data-orig="{orig}"' if orig else (' data-orig=""' if cls in ('part', 'book') else '')
        return f'<{tag} class="{cls}{more}"{attrs}{d}>{body}</{tag}>'
    return _HEAD.sub(rep, doc)
_TURN = re.compile(r'<p>((?:(?!</p>).)*?)\s*</p>\s*<div class="pgmark"([^>]*)></div>\s*<p>((?:(?!</p>).)*?)</p>', re.S)
def join_page_turns(doc):
    """A sentence that runs over a page turn of the original was two paragraphs with the page heading between them ("…in this manner..." /
    "...the greatness of these texts").  With the page mark out of the body they are one paragraph again (user, Nov 26 2026): joined where the
    first ends in an ellipsis or without closing punctuation AND the second begins with an ellipsis or a small letter.  The page mark stays
    inside the paragraph as an invisible span, so the footer still changes at the right place."""
    n = 0
    def rep(m):
        nonlocal n
        a, attrs, b = m.group(1), m.group(2), m.group(3)
        ta, tb = re.sub(r'<[^>]+>', '', a).rstrip(), re.sub(r'<[^>]+>', '', b).lstrip()
        open_a = bool(re.search(r'(\.\.\.|…)$', ta)) or bool(re.search(r'[A-Za-zāīūṛṃḥśṣṇṭḍñ,;—-]$', ta))
        cont_b = bool(re.match(r'(\.\.\.|…)', tb)) or bool(re.match(r'[a-zāīūṛśṣ]', tb))
        if not (open_a and cont_b) or not ta or not tb: return m.group(0)
        if not (re.search(r'(\.\.\.|…)$', ta) or re.match(r'(\.\.\.|…)', tb)) and not re.match(r'[a-z]', tb): return m.group(0)
        n += 1
        a2 = re.sub(r'\s*(\.\.\.|…)\s*((?:</[a-z]+>)*)\s*$', r'\2', a); b2 = re.sub(r'^((?:<[a-z]+[^>]*>)*)\s*(\.\.\.|…)\s*', r'\1', b)
        return f'<p>{a2} <span class="pgmark"{attrs}></span>{b2}</p>'
    prev = None
    while prev != doc: prev = doc; doc = _TURN.sub(rep, doc)          # a paragraph can run over more than one page turn
    return doc

_DV = re.compile('[ऀ-ॿ]')
_DVRUN = re.compile('[ऀ-ॿ᳐-᳿꣠-ꣿ][ऀ-ॿ᳐-᳿꣠-ꣿ‌‍\\s।॥|,;.:\'’\\-–—0-9()]*[ऀ-ॿ᳐-᳿꣠-ꣿ।॥]|[ऀ-ॿ]')
_IASTCH = re.compile('[āīūṛṝḷṃḥśṣṇṭḍñṅĀĪŪṚŚṢ]')
_BQ = re.compile(r'<blockquote(?![^>]*samhita)[^>]*>.*?</blockquote>', re.S)
def sanskrit(doc):
    """Sanskrit set smaller, transliteration on its own line (user, Nov 26 2026: fewer pages).  In every blockquote: a run of Devanagari is
    wrapped in <span class="dv">, an italic run that is transliteration gets class "iast" and begins a new line.  Sizes: style_footer.css.
    The spaced Saṃhitā verse of volbook (blockquote.samhita) is left as it is."""
    def bq(m):
        parts = re.split(r'(<[^>]+>)', m.group(0)); out = []; in_em = False
        for k, t in enumerate(parts):
            if t.startswith('<'):
                if t == '<em>':
                    nxt = parts[k + 1] if k + 1 < len(parts) else ''
                    if not _DV.search(nxt) and (_IASTCH.search(nxt) or re.search(r'\|\s*$|‖', nxt)):
                        prev = ''.join(out[-3:]).rstrip()
                        br = '' if re.search(r'(<p>|<br ?/?>|<blockquote[^>]*>)$', prev) else '<br>'
                        out.append(br + '<em class="iast">'); continue
                out.append(t)
            else:
                out.append(_DVRUN.sub(lambda r: f'<span class="dv">{r.group(0)}</span>', t))
        return ''.join(out)
    return _BQ.sub(bq, doc)

_STRONG = re.compile(r'<strong>((?:(?!</?strong>).)*)</strong>', re.S)
def plain_sentences(doc):
    """Bold is for headings and labels.  The scan-period sessions also set whole sentences in bold as emphasis of their own (Vol 1: about 930);
    in print such a sentence is plain text (user, Nov 26 2026).  A bold run counts as a sentence when it has 8 words or more, or 5 or more and
    ends like a sentence; short bold runs (labels, run-in heads, single terms) are left."""
    def rep(m):
        t = re.sub(r'<[^>]+>', '', m.group(1)).strip(); w = len(t.split())
        if w >= 8 or (w >= 5 and re.search(r'[.?!]["”’)]*$', t)): return m.group(1)
        return m.group(0)
    return _STRONG.sub(rep, doc)

def fix(doc):
    return sanskrit(headings(lists(contents_sections(join_page_turns(label_paragraphs(plain_sentences(doc)))))))
