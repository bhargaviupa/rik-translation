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
_ORIGNAMES = r'(?:P[ūu]rva-?)?P[īi][ṭt]hik[eāa]|Munnu[ḍd]i|Upodgh[āa]ta|Bh[āa][ṣs]ya-?bh[ūu]mik[āa]|Anukrama[ṇn]ik[āa]|Pari[śs]i[ṣs][ṭt]a'
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
        o2 = re.match(r'^(' + _ORIGNAMES + r')\s*\(([^()<]+)\)\s*$', text) or re.match(r'^(' + _ORIGNAMES + r')\s+—\s+(?:the\s+)?([^<]+)$', text)
        if o2 and not orig: text, orig = o2.group(2)[:1].upper() + o2.group(2)[1:], o2.group(1)      # "Pīṭhike (Introduction)" -> "Introduction", name to the footer
        cut = re.match(r'((?:PART|Part|BOOK|Book) [^:<]{1,12}):\s*(.+)$', text, re.S) or re.match(r'(Chapter [\w-]+)\s*(?:—|\.)\s*(.+)$', text, re.S) \
              or re.match(r'([^<—]{3,40}?)\s+—\s+(.+)$', text, re.S)
        body = f'<span class="ht1">{cut.group(1)}</span><span class="ht2">{cut.group(2)}</span>' if cut else text
        d = f' data-orig="{orig}"' if orig else (' data-orig=""' if cls in ('part', 'book') else '')
        return f'<{tag} class="{cls}{more}"{attrs}{d}>{body}</{tag}>'
    return _HEAD.sub(rep, doc)
_TURN = re.compile(r'<p>((?:(?!</p>).)*?)\s*</p>\s*<(?:div class="pgmark"|h3 class="pg")([^>]*)>(?:<span>[^<]*</span>)?</(?:div|h3)>\s*<p>((?:(?!</p>).)*?)</p>', re.S)
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
        open_a = bool(re.search(r'(\.\.\.|…)$', ta)) or bool(re.search(r'[A-Za-zāīūṛṃḥśṣṇṭḍñ,;—\])-]$', ta))
        cont_b = bool(re.match(r'(\.\.\.|…)', tb)) or bool(re.match(r'[a-zāīūṛśṣ]', tb))
        if ta and tb and re.search('[\u0c80-\u0cff,;]$', ta) and re.match('[\u0c80-\u0cff]', tb):      # Kannada book: the page ends inside a sentence
            n += 1; return f'<p>{a} <span class="pgmark"{attrs}></span>{b}</p>'
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
                        out.append(br + '<em class="iast">'); in_em = True; continue
                if t == '</em>' and in_em:
                    in_em = False; nxt = parts[k + 1] if k + 1 < len(parts) else ''
                    out.append('</em>' + ('<br>' if nxt.strip() else '')); continue                    # the English after it begins a new line too
                out.append(t)
            else:
                out.append(_DVRUN.sub(lambda r: f'<span class="dv">{r.group(0)}</span>', t))
        return ''.join(out)
    return _BQ.sub(bq, doc)

_STRONG = re.compile(r'<strong>((?:(?!</?strong>).)*)</strong>', re.S)
def plain_sentences(doc):
    """Bold is for headings and labels only (user, Nov 26 2026).  The scan-period sessions also set whole sentences, and single words and
    names inside sentences, in bold as emphasis of their own; in print these are plain text.  Kept: a short bold run (fewer than 8 words,
    not a sentence) that OPENS its paragraph, list item or table cell: a label or run-in head."""
    def sentence(t):
        w = len(t.split()); return w >= 8 or (w >= 5 and bool(re.search(r'[.?!]["”’)]*$', t)))
    def block(m):
        open_, inner, close = m.group(1), m.group(2), m.group(3); first = [True]
        def rep(x):
            lead = first[0] and not re.sub(r'<[^>]+>|[\s"“(\[—-]', '', inner[:x.start()]); first[0] = False
            t = re.sub(r'<[^>]+>', '', x.group(1)).strip()
            return x.group(0) if lead and not sentence(t) else x.group(1)
        return open_ + _STRONG.sub(rep, inner) + close
    return re.sub(r'(<(p|li|td)\b[^>]*>)(.*?)(</\2>)', lambda m: block(re.match(r'(.*?>)(.*)(</\w+>)$', m.group(0), re.S)), doc, flags=re.S)


def stamp(doc):
    """Every PDF carries a build number and date in the footer of every page: "REVIEW COPY / build 03 · 26 Nov 2026" (REQUIREMENTS H2.7;
    user, Nov 26 2026: "I prefer you give version number … like build01").  The number counts the builds of that book (volume and
    language, read from the <title>) and is kept in publish/build_numbers.json; two copies can be told apart at a glance and a comment
    quotes "build NN, p. X"."""
    import datetime, json, pathlib
    t = re.search(r'<title>([^<]*)</title>', doc); t = t.group(1) if t else ''
    v = re.search(r'Volume (\d+)', t); key = f'vol{v.group(1) if v else "?"}_{"kan" if "Kannada" in t else "eng"}'
    f = pathlib.Path(__file__).resolve().parent / 'build_numbers.json'
    nums = json.loads(f.read_text(encoding='utf8')) if f.exists() else {}
    nums[key] = nums.get(key, 0) + 1; f.write_text(json.dumps(nums, indent=1, sort_keys=True) + '\n', encoding='utf8')
    when = datetime.datetime.now(datetime.timezone.utc).strftime('%-d %b %Y')
    css = (f'<style>@page {{ @bottom-left {{ content: "REVIEW COPY\\A build {nums[key]:02d}  ·  {when}"; white-space: pre; }} }} @page front {{ @bottom-left {{ content: none; }} }} '
           '@page :first { @bottom-left { content: none; } } @page :blank { @bottom-left { content: none; } }</style>')
    print(f'[build] {key} build {nums[key]:02d}')
    return doc.replace('</head>', css + '</head>', 1)

_PGHEAD = re.compile(r'<(h[2-4])([^>]*)>\s*\[?(?:Printed )?[Pp]ages? ([0-9ivxlc]+)((?:[–-][0-9ivxlc]+)?)\]?\s*(?:(?:—|:)\s*(.*?)|<em>\([^<]*\)</em>|\([^<)]*\))?\s*</\1>', re.S)
def page_headings(doc):
    """Safety net for every builder: a heading of the working file that is only a page of the original ("Page 221 (continued)",
    "Pages 46–47 — The Bashkala Samhita…") never prints.  It becomes the invisible page mark that feeds the footer; a title after the dash
    stays as a heading unless it only says that the text continues."""
    have = set(re.findall(r'<(?:div class="pgmark"|h3 class="pg") id="(p[0-9ivxlc]+)"', doc)); n = 0
    def rep(m):
        nonlocal n
        tag, attrs, pg, rng, title = m.groups()
        if 'class="pg"' in attrs: return m.group(0)                      # volbook's own page mark
        n += 1; pid = 'p' + pg; idattr = '' if pid in have else f' id="{pid}"'; have.add(pid)
        out = f'<div class="pgmark"{idattr} data-p="Kannada edition p{"p" if rng else ""}. {pg}{rng}"></div>'
        if title and not re.search(r'(^|[\s(—,])continued\)?\s*$', re.sub(r'<[^>]+>', '', title), flags=re.I): out += f'<{tag}{attrs}>{title}</{tag}>'
        return out
    doc = _PGHEAD.sub(rep, doc)
    return doc, n

_TOC = re.compile(r'(<section class="toc">\s*<h2>[^<]*</h2>)(?:\s*<p class="tocsub">[^<]*</p>)?\s*<ul[^>]*>(.*?)</ul>', re.S)
def toc_tables(doc):
    """The book's own contents page or index of sūktas, as every builder writes it (a list of links), set as the one contents table."""
    def rep(m):
        rows = []
        for li in re.finditer(r'<li class="([^"]*)">\s*<a href="(#[^"]+)">(.*?)</a>\s*</li>', m.group(2), flags=re.S):
            cls, href, label = li.groups()
            if 'su' in cls.split(): rows.append({'kind': 'head', 'html': f'<a href="{href}"><strong>{label}</strong></a>'}); continue
            nm = re.match(r'(?:.*?·\s*)?(?:Sūkta|Chapter|ಸೂಕ್ತ)\s+([\w೦-೯-]+)\s*(?:[—:.]\s*(.*))?$', re.sub(r'<[^>]+>', '', label), flags=re.S)
            rows.append({'no': nm.group(1) if nm else '', 'html': f'<a href="{href}">{label}</a>', 'href': href + ('" data-rm="1' if 'rm' in cls.split() else '')})
        return m.group(1) + contents_table(rows) if rows else m.group(0)
    return _TOC.sub(rep, doc)

_LAT = re.compile(r'[A-Za-z]{3,}')
def quotations(doc):
    """A quotation from another work, printed with a bar, holds the Sanskrit and its transliteration only (user, Nov 26 2026: "references
    from other books … should not contain the English"; "we don't need English translation in there or other such places").  The English
    rendering of the quotation that stood inside the bar is not printed; it stays in the working file.  A short reference in parentheses
    after the Sanskrit stays.  A bar without Sanskrit (a passage quoted in English) is left as it is."""
    n = 0
    def bq(m):
        nonlocal n
        inner = m.group(2)
        if not _DV.search(inner): return m.group(0)
        keep, out_en = [], []
        for part in re.split(r'(<p\b[^>]*>.*?</p>)', inner, flags=re.S):
            pm = re.match(r'(<p\b[^>]*>)(.*)(</p>)$', part, flags=re.S)
            if not pm: keep.append(part); continue
            body = pm.group(2)
            ends = [x.end() for x in re.finditer(r'</em>|</span>', body) if (x.group(0) == '</span>' or '<em class="iast">' in body[:x.start()])]
            cut = max(ends) if ends else 0
            head, tail = body[:cut], body[cut:]
            ref = re.match(r'(?:\s|<br ?/?>)*(\((?:[^()<]|<[^>]+>){0,70}\))', tail)                       # "(Taittiriya Brahmana 2-1-2-12)" stays with the Sanskrit
            if ref and cut: head += ' ' + ref.group(1); tail = tail[ref.end():]
            t = re.sub(r'^(?:\s|<br ?/?>)+|(?:\s|<br ?/?>)+$', '', tail)
            if cut == 0 and not _DV.search(body) and 'class="iast"' not in body:
                if _LAT.search(re.sub(r'<[^>]+>', '', body)): out_en.append(body); continue             # a paragraph of English only
                keep.append(part); continue
            if t and len(_LAT.findall(re.sub(r'<[^>]+>', '', t))) >= 2 and not _DV.search(t):
                out_en.append(t); head = re.sub(r'(?:\s|<br ?/?>)+$', '', head)
                if head.strip(): keep.append(pm.group(1) + head + pm.group(3))
            else: keep.append(part)
        if not out_en: return m.group(0)
        n += len(out_en)
        return m.group(1) + ''.join(keep) + '</blockquote>'            # the English of the quotation is not printed (it stays in the working file)
    doc = re.sub(r'(<blockquote(?![^>]*samhita)[^>]*>)(.*?)</blockquote>', bq, doc, flags=re.S)
    return doc, n

_KN = re.compile('[ಀ-೿]')
_KNRUN = re.compile('[ಀ-೿][ಀ-೿‌‍\\s।॥.,:;\\-–]*[ಀ-೿।॥.]|[ಀ-೿]')
def no_kannada(doc):
    """No Kannada script in the body of the English book (REQUIREMENTS B2.3; user, Nov 26 2026: "no kannada in main body at all").
    "ಆರನೆಯ ಪ್ರಕರಣ — The Sixth Chapter" keeps the English; "(ಮುನ್ನುಡಿ)" after an English word goes; any other Kannada is given in
    transliteration, italic, so that nothing is lost.  Only for a document whose language is English."""
    if not re.search(r'<html lang="en"', doc[:300]) or not _KN.search(doc): return doc, 0
    import sys, pathlib
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent / 'tools' / 'translit'))
    from kannada_to_deva import kn2deva
    from add_iast import deva_to_iast
    n = 0; digits = str.maketrans('೦೧೨೩೪೫೬೭೮೯', '0123456789')
    def text(t):
        nonlocal n
        if not _KN.search(t): return t
        n += 1
        t = re.sub('[ಀ-೿][ಀ-೿\\s‌‍]*\\s+[—–-]\\s+(?=[A-Z])', '', t)             # Kannada name — English name
        t = re.sub('\\s*\\(\\s*[ಀ-೿][ಀ-೿\\s‌‍.]*\\)', '', t)                        # English (Kannada)
        t = t.translate(digits)
        return _KNRUN.sub(lambda r: '<i>' + deva_to_iast(kn2deva(r.group(0))).strip() + '</i>', t)
    parts = re.split(r'(<[^>]+>)', doc); body = False
    for k, t in enumerate(parts):
        if t.startswith('<'):
            if t.startswith('<body'): body = True
        elif body: parts[k] = text(t)
    return ''.join(parts), n

def wide_tables(doc):
    """A table must fit the page: one with many columns ran off the right edge and was cut (Vol 1; user, Nov 26 2026).  Every table of the
    text gets its number of columns as a class (cols5, cols6 …); style_footer.css sets tables of 5 columns or more in smaller type with
    fixed column widths and lets long words break."""
    n = 0
    def rep(m):
        nonlocal n
        if 'class="contents"' in m.group(1): return m.group(0)
        rows = re.findall(r'<tr\b.*?</tr>', m.group(0), flags=re.S); cols = max((len(re.findall(r'<t[dh]\b', r)) for r in rows), default=0)
        if cols >= 5: n += 1
        tag = m.group(1)
        tag = re.sub(r'class="', f'class="cols{cols} ' + ('wide ' if cols >= 5 else ''), tag, count=1) if 'class="' in tag else tag[:-1] + f' class="cols{cols}{" wide" if cols >= 5 else ""}">'
        return tag + m.group(0)[len(m.group(1)):]
    return re.sub(r'(<table\b[^>]*>).*?</table>', rep, doc, flags=re.S), n

def fix(doc, quiet=False):
    """Every print rule that holds for all volumes (docs/REQUIREMENTS.md, A4 "Print rules"), applied to the finished HTML of any builder.
    Prints one line of counts, so that each build shows what was done."""
    c = {}
    doc = stamp(doc)
    doc, c['page headings out of the body'] = page_headings(doc)
    b0 = doc.count('<strong>'); doc = plain_sentences(doc); c['bold sentences and words set plain'] = b0 - doc.count('<strong>')
    doc = label_paragraphs(doc); c['label paragraphs'] = doc.count('<p class="only-strong">')
    doc = join_page_turns(doc); c['paragraphs joined over a page turn'] = doc.count('<span class="pgmark"')
    doc = toc_tables(contents_sections(doc)); c['contents tables'] = doc.count('<table class="contents">')
    doc = lists(doc); c['lists continued'] = doc.count('<ol class="cont"')
    doc = headings(doc); c['two-line headings'] = doc.count('class="ht1"')
    doc = sanskrit(doc); c['transliterations on their own line'] = doc.count('<em class="iast">')
    doc, c['English of quotations not printed'] = quotations(doc)
    doc, c['Kannada-script places'] = no_kannada(doc)
    doc, c['wide tables fitted'] = wide_tables(doc)
    if not quiet: print('[printfix] ' + '; '.join(f'{k} {v}' for k, v in c.items()))
    return doc
