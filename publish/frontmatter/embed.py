"""The embedder: puts the common front and back pages of publish/frontmatter/order.json into the finished HTML of a volume's English book.

Called as the last step of publish/printfix.fix(), for every builder (build.py, build_vol1/2/45.py, volbook.py).  It does nothing unless
order.json has "embed": true (the user's master switch; REQUIREMENTS A2a).  `embed(doc, force=True)` ignores the switch (tests only).

What it does, in this order:
  1. takes out the bodies that printfix.mark_slots marked (<section data-slot="contents|abbreviations|original_preface">), without their
     headings (class slot-head: the frame brings its own);
  2. removes the sections the builders print as front matter (cover, title page, copyright, king, guru, present day, board of scholars, scans,
     the builders' own list of abbreviations): the pages of order.json take their place;
  3. builds the front: the enabled rows of order.json in order; a fragment gets its tokens, its recto/verso class, and (kind slot) its body;
     a slot the volume has no body for is skipped (its page is not printed; the hand-over names it);
  4. inserts <div class="fm-bodystart" data-orig=""></div> in front of the text (row "body": opens a right page, clears the footer name,
     arabic 1) and puts the rows after it (the closing page) behind the text.
Tokens: {{vol}} {{vol_roman}} {{range_line}} {{adhyaya_line}} {{imprint}} {{year}} from volN/pubcfg.json (vol from volN/volcfg.json where there is
no pubcfg.json; a field that does not exist prints "[… to be supplied]"), {{assets}} = publish/assets, {{release.X}} from publish/release.json
(empty: "[to be supplied]").  The report of what was done goes to stdout and to the module variable `last_report`."""
import re, json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
PUB = HERE.parent; ROOT = PUB.parent
last_report = {}
OLD_FRONT = ('cover', 'titlepage', 'copyright', 'portrait', 'portrait pair', 'scan', 'scan small', 'board', 'abbr')       # classes of the builders' own front sections

def _roman(n):
    out = ''
    for v, r in ((10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')):
        while n >= v: out += r; n -= v
    return out
def _match_end(doc, start, tag='section'):
    depth = 0
    for m in re.finditer(r'<(/?)' + tag + r'\b[^>]*>', doc[start:]):
        depth += -1 if m.group(1) else 1
        if depth == 0: return start + m.end()
    return None
def _tokens(vol):
    cfg = {}
    for f in (ROOT / f'vol{vol}' / 'volcfg.json', ROOT / f'vol{vol}' / 'pubcfg.json'):          # pubcfg wins
        if f.exists(): cfg.update(json.loads(f.read_text(encoding='utf8')))
    rel = json.loads((PUB / 'release.json').read_text(encoding='utf8')) if (PUB / 'release.json').exists() else {}
    t = {'vol': str(cfg.get('vol', vol)), 'vol_roman': _roman(int(cfg.get('vol', vol))), 'assets': (PUB / 'assets').as_uri(), 'fm_assets': (HERE / 'assets').as_uri()}
    for k, label in (('range_line', 'range of the volume'), ('adhyaya_line', 'Aṣṭaka and Adhyāya'), ('imprint', 'press of the original'), ('year', 'year'), ('press', 'press')):
        t[k] = str(cfg[k]) if cfg.get(k) else f'[{label} — to be supplied]'
    t['release'] = {k: v for k, v in rel.items() if not k.startswith('_')}
    return t
def _fill(html, tok):
    def rep(m):
        k = m.group(1)
        if k.startswith('release.'): return tok['release'].get(k[8:]) or '[to be supplied]'
        return tok.get(k, m.group(0))
    return re.sub(r'\{\{([\w.]+)\}\}', rep, html)

def _own_preface(vol):
    """The text of row `our_preface`: volN/own_preface.json (made by tools/rv/own_preface.py, written by the editor).  Paragraphs that still hold a
    {{slot}} print as the dashed placeholder (class ph), so an unfinished slot is visible in a review copy.  None = no file: the fragment's own placeholder stays."""
    import html as H
    f = ROOT / f'vol{vol}' / 'own_preface.json'
    if not f.exists(): return None
    d = json.loads(f.read_text(encoding='utf8')); ph = lambda x: '{{' in x
    paras = ''.join(f'<p class="ph">{H.escape(x)}</p>' if ph(x) else f'<p>{H.escape(x)}</p>' for x in d.get('paragraphs', []))
    line = lambda k: '<br>'.join(H.escape(x) for x in d.get(k, []) if not ph(x))
    sign = f'<div class="sign"><div class="dl">{line("dateline")}</div><div class="sg">{line("signature")}</div></div>' if line('dateline') or line('signature') else ''
    return paras + sign

def embed(doc, force=False):
    order = json.loads((HERE / 'order.json').read_text(encoding='utf8'))
    if not (force or order.get('embed')): return doc
    t = re.search(r'<title>[^<]*Volume (\d+)', doc); vol = int(t.group(1)) if t else 0
    tok = _tokens(vol); rep = {'volume': vol, 'slots': {}, 'skipped': [], 'removed': []}
    b0 = doc.index('<body>') + len('<body>'); b1 = doc.rindex('</body>')
    head, body, tail = doc[:b0], doc[b0:b1], doc[b1:]
    # 1. slot bodies
    slots = {}
    for name in ('original_preface', 'contents', 'abbreviations', 'introduction'):
        m = re.search(r'<section\b[^>]*data-slot="' + name + r'"[^>]*>', body)
        if not m: continue
        e = _match_end(body, m.start())
        inner = body[m.end():e - len('</section>')]
        inner = re.sub(r'<(h[1-6]|p)\b[^>]*class="[^"]*\bslot-head\b[^"]*"[^>]*>.*?</\1>', '', inner, flags=re.S)
        slots[name] = inner.strip(); body = body[:m.start()] + body[e:]
    rep['slots'] = {k: len(v) for k, v in slots.items()}
    # 2. the builders' own front sections
    for cls in OLD_FRONT:
        while True:
            m = re.search(r'<section class="' + re.escape(cls) + r'(?: [^"]*)?"[^>]*>', body)
            if not m: break
            e = _match_end(body, m.start())
            if e is None: break
            body = body[:m.start()] + body[e:]; rep['removed'].append(cls)
    # 3. the front, the text, the back
    front, back, seen_body = [], [], False
    for row in order['pages']:
        if not row.get('enabled'): continue
        if row['kind'] == 'volume': seen_body = True; continue
        h = (HERE / row['file']).read_text(encoding='utf8')
        if row['kind'] == 'slot':
            inner = slots.get(row['slot'])
            if not inner: rep['skipped'].append(row['id']); continue
            h = re.sub(r'(<div class="fm-slot"[^>]*>)\s*</div>', lambda m: m.group(1) + inner + '</div>', h, count=1)
        if row['id'] == 'our_preface':             # the editor's own preface of this volume replaces the placeholder block
            own = _own_preface(vol)
            if own: h = re.sub(r'<div class="ph tall">.*?</div>', lambda m: own, h, count=1, flags=re.S)
        cls = {'recto': 'recto ', 'verso': 'verso '}.get(row.get('start'), '')
        h = h.replace('class="fm ', 'class="fm ' + cls, 1)
        (back if seen_body else front).append(_fill(h, tok))
    # the first element of the text: a part/chapter/sūkta heading becomes the 'first' one (named page chapter-first: arabic 1) and the marker then makes no page
    txt = body.strip(); plain = False
    m = re.match(r'(?:\s*<div class="pgmark"[^>]*></div>)*\s*<(h1|h2)\b([^>]*)class="((?:part|book|chapter|sukta)[^"]*)"', txt)
    if m and ' first' not in ' ' + m.group(3):
        txt = txt[:m.start(3)] + m.group(3) + ' first' + txt[m.end(3):]; plain = True
    elif m: plain = True
    body = txt
    mark = '<div class="fm-bodystart' + (' plain' if plain else '') + '" data-orig=""></div>'
    if plain:          # a heading opens the text: it takes the class itself, no empty marker page
        body = re.sub(r'class="((?:part|book|chapter|sukta)[^"]* first)"', r'class="\1 fm-first"', body, count=1); mark = ''
    else:      # the text opens with something else (a title block, a div): that element itself opens the right page, no empty marker page
        m2 = re.match(r'<(div|section|p|h1|h2|h3)\b[^>]*>', body)
        if m2:
            tag = m2.group(0); c = re.search(r'class="([^"]*)"', tag)
            new = tag.replace(c.group(0), 'class="' + c.group(1) + ' fm-first"') if c else tag[:-1] + ' class="fm-first">'
            body = new + body[len(tag):]; mark = ''
    head = head.replace('</head>', f'<link rel="stylesheet" href="{(HERE / "fm.css").as_uri()}"></head>', 1)     # the styles of the pages: named pages front/roman/fmbody, recto/verso, placeholders
    doc = head + '\n'.join(front) + '\n' + mark + '\n' + body.strip() + '\n' + '\n'.join(back) + tail
    global last_report; last_report = rep
    print(f"[embed] vol {vol}: slots {rep['slots']}; skipped {rep['skipped']}; builders' own front sections removed: {len(rep['removed'])} ({', '.join(sorted(set(rep['removed'])))})")
    return doc
