#!/usr/bin/env python3
"""Translate windows through the Anthropic Message Batches API (half price, no agent, no dispatcher turns).

  python3 tools/rv/api_batch.py plan    VOL [--windows K] [--model claude-sonnet-5-5] [--effort medium]
        prepares the next K windows ahead (work/wPPPP/, as `batch.py prep` does), builds one request per window
        (system = the translator brief, cached; user = the window's TASK.md + its pictures), counts the input tokens
        with the API's token counter (free) and prints the cost estimate.  Nothing is sent.
  python3 tools/rv/api_batch.py submit  VOL          sends the planned requests as ONE batch (this spends money); id in work/api_batch.json
  python3 tools/rv/api_batch.py status  VOL          batch state
  python3 tools/rv/api_batch.py collect VOL [--retries N]   fetches the results: writes each window's en.md (and applies the Kannada-file repairs the model
        asked for), logs real usage and cost per window in volN/parts/batch_costs.md, then runs `batch.py done` window after window IN PAGE ORDER
        and stops at the first window whose gates fail (fix it by hand or with an agent, then `collect` again: finished windows are skipped).

Key: environment variable RIK_API_KEY (or ANTHROPIC_API_KEY); it is never printed.  Prices per million tokens (input, output) are in PRICES
below: check them against the price list before trusting an estimate.  Batch = 50 % of both.
The model has no tools.  It answers with <en> … </en> (the en.md of the window) and optionally <kn_fix> … </kn_fix>: a JSON list of
{"old": "...", "new": "..."} exact, unique replacements in kn.md (structure repairs only, letters unchanged)."""
import os, re, sys, json, time, base64, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rvlib, batch
ROOT = rvlib.ROOT
PRICES = {'claude-sonnet-5-5': (2.0, 10.0), 'claude-opus-5-5': (4.0, 20.0), 'claude-haiku-5-5': (0.10, 0.50)}   # USD per MTok, list price (Nov 2026)
HEADER = """You translate one window (about six printed pages) of a 1950s Kannada edition of the Ṛgveda (Sāyaṇa's Sanskrit commentary with a Kannada commentary) into English for a scholarly edition.
You have NO tools here: ignore every instruction below about reading files or running commands. The user message is the window's TASK.md (it contains kn.md with the Sanskrit blocks numbered «bN»).
Answer with exactly this and nothing else:
<en>
…the complete en.md of the window, as the brief describes…
</en>
<kn_fix>
[{"old": "exact text that occurs once in kn.md", "new": "replacement"}]
</kn_fix>
Give <kn_fix> only when the structure of kn.md is wrong (a verse standing as plain lines must become a `> ` block under its standard label; Kannada prose must not be inside a block; a wrong or garbled label; a missed running head needs `<!-- printed N -->` + the head line). Letters and digits are never changed in a fix. A page that prints no number of its own, or whose head the script missed, gets its marker by a fix; write its `### Printed p. N` heading in <en>. Block numbers [[bN]] in your <en> must be those of kn.md AFTER your fixes are applied (blocks counted from 1 in order of appearance). If a picture is attached, it is the `[figure: …]` of kn.md: if it only repeats a verse block that kn.md already has, remove the figure line with a fix (no remark in <en>); otherwise write its verse into kn.md with a fix, letter by letter in Kannada script.

The translator brief follows.

"""

def client():
    import anthropic
    key = os.environ.get('RIK_API_KEY') or os.environ.get('ANTHROPIC_API_KEY')
    if not key: sys.exit('no API key in the environment (RIK_API_KEY)')
    return anthropic.Anthropic(api_key=key)
def state_file(cfg): return os.path.join(cfg.work, 'api_batch.json')
def load_state(cfg): return json.load(open(state_file(cfg))) if os.path.exists(state_file(cfg)) else {}
def save_state(cfg, st): os.makedirs(cfg.work, exist_ok=True); json.dump(st, open(state_file(cfg), 'w'), indent=1)
def system_blocks():
    brief = open(os.path.join(ROOT, 'tools', 'rv', 'BRIEF.md'), encoding='utf8').read()
    return [{'type': 'text', 'text': HEADER + brief, 'cache_control': {'type': 'ephemeral'}}]
def user_content(w):
    task = open(os.path.join(w, 'TASK.md'), encoding='utf8').read(); content = []
    for f in re.findall(r'\[figure: ([^\]]+)\]', task):
        p = os.path.join(ROOT, f.strip())
        if os.path.exists(p):
            mt = 'image/png' if p.lower().endswith('.png') else 'image/jpeg'
            content.append({'type': 'image', 'source': {'type': 'base64', 'media_type': mt, 'data': base64.standard_b64encode(open(p, 'rb').read()).decode()}})
    content.append({'type': 'text', 'text': task})
    return content
def params(w, model, effort):
    return dict(model=model, max_tokens=32000, system=system_blocks(), output_config={'effort': effort},
                messages=[{'role': 'user', 'content': user_content(w)}])

def cmd_plan(a):
    cfg = rvlib.Cfg(a[0]); opt = lambda k, d: a[a.index(k) + 1] if k in a else d
    k = int(opt('--windows', 5)); model = opt('--model', 'claude-sonnet-5-5'); effort = opt('--effort', 'medium')
    old = load_state(cfg)
    if old.get('batch_id') and not all(x.get('done') for x in old.get('windows', [])): sys.exit('the previous batch is not finished: run collect (and repair the window it stopped at) before planning more')
    if old.get('batch_id'): os.rename(state_file(cfg), state_file(cfg).replace('.json', f"_{old['windows'][0]['first']:04d}.json"))
    pr, f = batch.audit(cfg, expect_clean=False)
    if pr: sys.exit('audit fails, fix first: ' + '; '.join(pr))
    after = f['page']; wins = []; cl = client(); tot = 0
    for _ in range(k):
        try: w, pages, notes = batch.cmd_prep([a[0]], quiet=True, after=after)
        except SystemExit as e: print('no further window:', e); break
        p = params(w, model, effort)
        n = cl.messages.count_tokens(model=model, system=p['system'], messages=p['messages']).input_tokens
        wins.append(dict(win=os.path.relpath(w, ROOT), first=pages[0][0], last=pages[-1][0], input_tokens=n)); tot += n; after = pages[-1][0]
        print(f"{wins[-1]['win']}  pp. {pages[0][0]}-{pages[-1][0]}  {n} input tokens  {len(notes)} script notes")
    pi, po = PRICES.get(model, (0, 0)); npages = sum(x['last'] - x['first'] + 1 for x in wins)
    out_lo, out_hi = tot * 0.5, tot * 1.2          # output (English + the model's reasoning) is not known before the run: a range, to be replaced by measurement
    print(f"\n{len(wins)} windows, about {npages} pages, {tot} input tokens ({round(tot / max(npages, 1))} per page), model {model}, effort {effort}")
    print(f"batch cost estimate: input ${tot * pi / 2e6:.2f} + output ${out_lo * po / 2e6:.2f} to ${out_hi * po / 2e6:.2f}  (output assumed 0.5-1.2 x input; the pilot measures it)")
    save_state(cfg, dict(model=model, effort=effort, windows=wins, batch_id=None))
def cmd_submit(a):
    from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
    from anthropic.types.messages.batch_create_params import Request
    cfg = rvlib.Cfg(a[0]); st = load_state(cfg)
    if not st.get('windows'): sys.exit('run plan first')
    if st.get('batch_id'): sys.exit(f"a batch is already recorded ({st['batch_id']}): collect it first (plan writes a new state once every window of it is done)")
    reqs = [Request(custom_id=os.path.basename(x['win']), params=MessageCreateParamsNonStreaming(**params(os.path.join(ROOT, x['win']), st['model'], st['effort']))) for x in st['windows']]
    b = client().messages.batches.create(requests=reqs); st['batch_id'] = b.id; save_state(cfg, st)
    print('submitted', b.id, b.processing_status, len(reqs), 'requests')
def cmd_status(a):
    cfg = rvlib.Cfg(a[0]); st = load_state(cfg)
    b = client().messages.batches.retrieve(st['batch_id']); c = b.request_counts
    print(b.id, b.processing_status, f'processing {c.processing} succeeded {c.succeeded} errored {c.errored} canceled {c.canceled} expired {c.expired}')
    return b.processing_status
_SKIP = r'[\s\u200c\u200d\-–—|>।]'
def autofix_inline(w, en, kn):
    """An inline ⟦…⟧ segment that is not in kn.md letter for letter (the model retyped it, often 'correcting' a misread letter of the supplied text)
    is replaced by the same words as kn.md has them, when one run of whole words there is clearly the same passage (similarity >= 0.85).
    The supplied text stays the base; every replacement is logged (the model's form may be the better reading: a list for the editor).
    Returns (en, [(model's form, kn.md form, score)])."""
    import convert, difflib
    norm = lambda t: re.sub(_SKIP, '', t)
    flat = convert.kn_flat(kn); words = flat.split(' '); nk = norm(flat) + norm(kn); log = []
    def best(seg):
        q = norm(seg); n = len(seg.split())
        if len(q) < 4: return None
        top = (0, None)
        for k in {max(1, n - 1), n, n + 1}:
            for i in range(0, len(words) - k + 1):
                c = ' '.join(words[i:i + k]); cn = norm(c)
                if abs(len(cn) - len(q)) > 2 or (cn[:1] != q[:1] and cn[-1:] != q[-1:]): continue
                r = difflib.SequenceMatcher(None, q, cn).ratio()
                if r > top[0]: top = (r, c)
        return top if top[0] >= 0.85 else None
    def rep(m):
        seg = m.group(1)
        if '~~' in seg or not re.search('[\u0C80-\u0CFF]', seg) or norm(seg) in nk: return m.group(0)
        b = best(seg)
        if not b: return m.group(0)
        log.append((seg, b[1].strip('।॥ '), round(b[0], 2))); return '⟦' + b[1].strip('।॥ ') + '⟧'
    return re.sub(r'⟦([^⟧]+)⟧', rep, en), log
def soften(en, kn, w):
    """What a script can settle is settled here, so that a window is not sent to the model twice for it (user, Nov 11 2026: too many retries):
      * a `## Sūkta N (Maṇḍala M)` heading that the volume already has, or that stands twice in the window, is dropped (kept once);
      * a `⟦START~~END⟧` quotation that cannot be located even approximately is given by its first and last words with … between, and marked **NOTE**;
      * a reference that is not in kn.md in that form: accepted when its numbers are those of a printed reference in another punctuation
        (2-3-13 for the printed 2-3 13) or part of one; otherwise kept as written and marked **NOTE**.
    Returns the changed en and a list of what was done (also written to WIN/softened.tsv)."""
    import convert, numerals
    log = []; vol = re.search(r'vol(\d+)', w).group(1)
    have = set(re.findall(r'(?m)^## Sūkta \d+ \(Maṇḍala \d+\)', open(os.path.join(ROOT, f'vol{vol}', f'Rigveda_Samhita_Vol{vol}_English_Translation.md'), encoding='utf8').read()))
    out = []
    for l in en.split('\n'):
        h = re.fullmatch(r'## Sūkta \d+ \(Maṇḍala \d+\)\s*', l)
        if h and l.strip() in have: log.append(('heading dropped (already written)', l.strip())); continue
        if h: have.add(l.strip())
        out.append(l)
    en = '\n'.join(out)
    # translator remarks and old marks that the reader's text must not carry
    n0 = len(en); en = re.sub(r'(?m)^\*\[[^\]\n]*\]\*[ \t]*\n', '', en); en = re.sub(r'[ \t]*\*\[[^\]\n]*\]\*', '', en)
    en = re.sub(r'[ \t]*\((?:[^()\n]*?\b(?:as supplied|as printed|so printed)\b[^()\n]*)\)', '', en, flags=re.I)
    en = re.sub(r'(?mi)^\*?Running head[^\n]*\n', '', en)
    if len(en) != n0: log.append(('translator remarks removed', f'{n0 - len(en)} characters'))
    for old, why in ((r'\[\?\]', 'marked [?] by the translator'), (r'\[sic\]', 'marked [sic] by the translator'), (r'(?<![IVXLCDM])XXX(?![IVXLCDM])', 'placeholder left by the translator')):
        en, k = re.subn(old, '**NOTE**{' + why + '}', en)
        if k: log.append((why, str(k)))
    en, k = re.subn(r'\*\*NOTE\*\*(?!\{)', '**NOTE**{no question given by the translator}', en)
    if k: log.append(('NOTE without a question', str(k)))
    # Sanskrit blocks: each exactly once, alone on its line; a block the translation did not place is put after the block before it
    nb = len(convert.kn_blocks(kn)); L = en.split('\n'); seen = set(); out = []
    for l in L:
        m = re.search(r'\[\[b(\d+)\]\]', l)
        if not m: out.append(l); continue
        n = int(m.group(1)); rest = (l[:m.start()] + l[m.end():]).strip()
        if n < 1 or n > nb or n in seen: log.append(('block reference dropped (no such block, or placed twice)', m.group(0))); 
        else: seen.add(n); out.append(f'[[b{n}]]')
        if rest: out.append(rest)
    L = out
    for n in range(1, nb + 1):
        if n in seen: continue
        at = next((i for i, l in enumerate(L) if l.strip() == f'[[b{n - 1}]]'), None) if n > 1 else next((i for i, l in enumerate(L) if l.startswith('### Printed p. ')), -1)
        if at is None: at = len(L) - 1
        L[at + 1:at + 1] = ['', '**NOTE**{the Sanskrit block that follows was placed here by script: the translation had not placed it}', '', f'[[b{n}]]', '']
        seen.add(n); log.append(('block placed by script', f'b{n}'))
    en = '\n'.join(L)
    probs = []; en = convert.resolve_markers(en, kn, probs)
    def unres(m):
        a, b = [x.strip() for x in m.group(1).split('~~', 1)]; log.append(('quotation not located: first and last words only', m.group(0)[:80]))
        return f'⟦{a}⟧ … ⟦{b}⟧ **NOTE**{{long quotation not located in the supplied text of these pages: only its first and last words are given}}'
    en = re.sub(r'⟦([^⟧]*~~[^⟧]*)⟧', unres, en)
    knr = re.sub(r'(?<=[೦-೯0-9])_(?=[೦-೯0-9])', '-', kn); knr = kn + '\n' + re.sub(r'(?<=-[೦-೯0-9]) (?=[೦-೯0-9]{1,3}-[೦-೯0-9])', '-', knr)
    kset = set(numerals.refs_kn(knr)) | set(numerals.refs_en(knr)); groups = [k.split('-') for k in kset]
    def part_of(r):
        g = r.split('-'); n = len(g)
        return any(k[i:i + n] == g for k in groups for i in range(len(k) - n + 1)) or any(''.join(k) == ''.join(g) for k in groups)
    parts = re.split(r'(⟦[^⟧]*⟧|⟪[^⟫]*⟫|\*\*NOTE\*\*\{[^{}]*\})', en)
    for i in range(0, len(parts), 2):
        def ref(m):
            r = numerals.norm(m.group()); nxt = parts[i + 1] if i + 1 < len(parts) else ''
            if r in kset or part_of(r): return m.group()
            log.append(('reference marked NOTE', m.group()))
            return m.group() + ' **NOTE**{reference ' + r + ' is not in the supplied text of these pages in this form}'
        parts[i] = numerals.EN_REF.sub(ref, parts[i])
    en = ''.join(parts)
    if log: open(os.path.join(w, 'softened.tsv'), 'w', encoding='utf8').write(''.join(f'{a}\t{b}\n' for a, b in log))
    return en, log
def wrap_bare_kannada(en):
    """Kannada-script words the model left outside ⟦ ⟧ (usually a Sanskrit quotation put in plain quotation marks) are put inside ⟦ ⟧,
    so that the script converts and checks them like every other quotation.  NOTE details and existing segments are left alone."""
    parts = re.split(r'(⟦[^⟧]*⟧|⟪[^⟫]*⟫|\*\*NOTE\*\*\{[^{}]*\})', en)
    KR = '[\u0C80-\u0CFF]'
    for i in range(0, len(parts), 2):
        parts[i] = re.sub('[“"\']?(' + KR + '[\u0C80-\u0CFF\u200c\u200d ।॥\\-—]*' + KR + '|' + KR + ')[”"\']?', lambda m: '⟦' + m.group(1) + '⟧', parts[i])
    return ''.join(parts)
def latin_fallback(en, kn):
    """Last resort for an inline segment that is not in kn.md even approximately (a word taken out of a sandhi, or from another page): it is
    given in transliteration only (italic, made by script from the model's letters) and logged, so that no Sanskrit stands in Devanagari in the
    book that is not in the supplied text, and no paid retry is needed for it."""
    import convert
    sys.path.insert(0, os.path.join(ROOT, 'publish', 'tools', 'translit'))
    from kannada_to_deva import kn2deva
    from add_iast import deva_to_iast
    norm = lambda t: re.sub(_SKIP, '', t); nk = norm(convert.kn_flat(kn)) + norm(kn); log = []
    def rep(m):
        seg = m.group(1)
        if '~~' in seg or not re.search('[\u0C80-\u0CFF]', seg) or norm(seg) in nk: return m.group(0)
        log.append((seg, '(not in the supplied text of this window: given in transliteration only)', '')); return '*' + deva_to_iast(kn2deva(seg)) + '*'
    return re.sub(r'⟦([^⟧]+)⟧', rep, en), log
def apply_answer(w, text):
    """write en.md and apply the kn.md repairs; returns a list of problems"""
    prob = []; m = re.search(r'<en>\s*\n?(.*?)\n?\s*</en>', text, re.S)
    if not m: return ['no <en> … </en> in the answer']
    kp = os.path.join(w, 'kn.md'); pj0 = os.path.join(w, 'pages.json')
    for f in (kp, pj0):                                   # the first answer is applied to the prepared files; a retry starts from them again
        if not os.path.exists(f + '.orig'): open(f + '.orig', 'w', encoding='utf8').write(open(f, encoding='utf8').read())
        else: open(f, 'w', encoding='utf8').write(open(f + '.orig', encoding='utf8').read())
    kn = open(kp, encoding='utf8').read()
    f = re.search(r'<kn_fix>\s*(.*?)\s*</kn_fix>', text, re.S)
    if f and f.group(1).strip() not in ('', '[]'):
        try: fixes = json.loads(f.group(1))
        except Exception as e: fixes = []; prob.append(f'kn_fix is not valid JSON ({e})')
        for x in fixes:
            if kn.count(x.get('old', '\0')) != 1: prob.append(f"kn_fix: old text occurs {kn.count(x.get('old', chr(0)))} times: {str(x.get('old'))[:50]}"); continue
            strip = lambda t: re.sub(r'[\s>*\[\]\-<!]|printed|\d', '', t)          # a structure repair may add markers, labels, quote marks, page numbers: nothing else
            if not set(strip(x['new'])) - set(strip(x['old'])) <= set('ಸಂಹಿತಾಪಾಠಃಪದಸಾಯಣಭಾಷ್ಯಂಪ್ರತಿಪದಾರ್ಥಭಾವಾರ್ಥವಿಶೇಷವಿಷಯಗಳುವ್ಯಾಕರಣಪ್ರಕ್ರಿಯಾEnglish Translation.'): prob.append(f"kn_fix adds letters that are not a label: {x['new'][:50]} (applied; check it)")
            kn = kn.replace(x['old'], x['new']); open(os.path.join(w, 'fixes.tsv'), 'a', encoding='utf8').write(f"kn\t{x['old']}\t{x['new']}\n")
        open(kp, 'w', encoding='utf8').write(kn)
        pj = os.path.join(w, 'pages.json'); pg = json.load(open(pj)); have = {x['printed'] for x in pg}      # a page marker added by a fix joins the window's page list
        for n in re.findall(r'<!-- printed (\d+)', kn):
            if int(n) not in have: pg.append(dict(printed=int(n), pdf=None, file_page=None, numeral_rows=0)); have.add(int(n))
        json.dump(sorted(pg, key=lambda x: x['printed']), open(pj, 'w'), indent=1)
    en, soft = soften(m.group(1).strip() + '\n', kn, w)
    en = wrap_bare_kannada(en)
    en, fixed = autofix_inline(w, en, kn)
    en, latin = latin_fallback(en, kn); fixed += latin
    open(os.path.join(w, 'en.md'), 'w', encoding='utf8').write(en)
    if fixed:
        vol = re.search(r'vol(\d+)', w).group(1); lf = os.path.join(ROOT, f'vol{vol}', 'review', 'inline_readings.tsv'); new = not os.path.exists(lf)
        with open(lf, 'a', encoding='utf8') as f:
            if new: f.write('window\tas the translator wrote it (often the expected Sanskrit)\tas the supplied text has it (used in the book)\tsimilarity\n')
            for a_, b_, r_ in fixed: f.write(f"{os.path.basename(w)}\t{a_}\t{b_}\t{r_}\n")
    return prob
RETRY = """The automatic checks rejected your answer for this window. Their message:

{gate}

Send the COMPLETE corrected answer again in the same format (<en> … </en> and, if needed, <kn_fix> … </kn_fix>; your fixes are applied to the kn.md shown in the task, not to an already fixed copy). Change only what the message requires and keep everything else word for word. Never change what the print says to satisfy a check: an inline ⟦ ⟧ segment must be copied letter for letter from kn.md (if you cannot find the exact words there, write the word in Latin letters instead); a reference is written as kn.md prints it."""
def retry_window(cl, st, x, gate):
    """one direct (not batch) request: the task, the rejected answer and the gate message; returns (text, usd)"""
    w = os.path.join(ROOT, x['win']); p = params(w, st['model'], st['effort'])
    p['messages'] += [{'role': 'assistant', 'content': open(os.path.join(w, 'answer.txt'), encoding='utf8').read()},
                      {'role': 'user', 'content': RETRY.format(gate=gate[-2500:])}]
    with cl.messages.stream(**p) as stream: msg = stream.get_final_message()
    u = msg.usage; pi, po = PRICES.get(st['model'], (0, 0))
    usd = ((u.input_tokens + (getattr(u, 'cache_creation_input_tokens', 0) or 0) * 1.25 + (getattr(u, 'cache_read_input_tokens', 0) or 0) * 0.1) * pi + u.output_tokens * po) / 1e6
    text = ''.join(b.text for b in msg.content if b.type == 'text')
    return (text if msg.stop_reason == 'end_turn' else ''), usd, u
def cmd_collect(a):
    cfg = rvlib.Cfg(a[0]); st = load_state(cfg); cl = client()
    if cl.messages.batches.retrieve(st['batch_id']).processing_status != 'ended': sys.exit('batch not ended yet: run status')
    pi, po = PRICES.get(st['model'], (0, 0)); res = {r.custom_id: r for r in cl.messages.batches.results(st['batch_id'])}
    cost = os.path.join(ROOT, f'vol{cfg.vol}', 'parts', 'batch_costs.md'); total = 0.0
    for x in st['windows']:
        w = os.path.join(ROOT, x['win']); name = os.path.basename(w); r = res.get(name)
        if x.get('collected'): continue
        if r is None or r.result.type != 'succeeded': x['problem'] = f'request {r.result.type if r else "missing"}'; print(name, x['problem']); continue
        msg = r.result.message; u = msg.usage
        text = ''.join(b.text for b in msg.content if b.type == 'text')
        inp = u.input_tokens; cw = getattr(u, 'cache_creation_input_tokens', 0) or 0; cr = getattr(u, 'cache_read_input_tokens', 0) or 0; out = u.output_tokens
        usd = (inp * pi + cw * pi * 1.25 + cr * pi * 0.1 + out * po) / 2e6      # batch: half price; cache write/read multipliers are the usual 1.25 / 0.1 (approximate)
        x.update(collected=True, usd=round(usd, 4), stop=msg.stop_reason, usage=dict(input=inp, cache_write=cw, cache_read=cr, output=out)); total += usd
        open(os.path.join(w, 'answer.txt'), 'w', encoding='utf8').write(text)
        if msg.stop_reason != 'end_turn': x['problem'] = f'stop_reason {msg.stop_reason}'; print(name, x['problem']); continue
        pr = apply_answer(w, text); x['problem'] = '; '.join(pr) if pr else None
        open(cost, 'a', encoding='utf8').write(f"| {name} pp. {x['first']}-{x['last']} | {st['model']} batch API, effort {st['effort']} | 1 request | in {inp} + cache write {cw} + cache read {cr}, out {out} | ${usd:.3f} |\n")
        print(f"{name}: in {inp + cw + cr}, out {out}, ${usd:.3f}" + (f"  PROBLEM: {x['problem']}" if pr else ''))
    save_state(cfg, st)
    if total: print(f'cost of the collected windows: ${total:.2f}')
    from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
    from anthropic.types.messages.batch_create_params import Request
    def gate(x):
        r = subprocess.run(['python3', 'tools/rv/batch.py', 'done', str(cfg.vol), x['win'], '--dry-run'], capture_output=True, text=True, cwd=ROOT)
        return r.returncode == 0, (r.stdout + r.stderr).strip()
    rounds = int(a[a.index('--retries') + 1]) if '--retries' in a else 0      # default: NO retry (user, Nov 11 2026): the scripts settle what they can; a window that still fails is repaired by hand or re-sent on purpose with --retries 1
    for rnd in range(1, rounds + 1):                               # windows whose gates fail go back with the gate message, as ONE batch per round
        if '--no-retry' in a: break
        bad = []
        for x in st['windows']:
            if x.get('done') or not x.get('collected') or (x.get('problem') and 'kn_fix' not in x['problem']): continue
            ok, out = gate(x)
            if not ok: bad.append((x, out)); open(os.path.join(ROOT, x['win'], f'gate_failure_{rnd}.txt'), 'w', encoding='utf8').write(out)
        print(f'round {rnd}: {len(bad)} windows fail their gates' + (': ' + ' '.join(os.path.basename(x["win"]) for x, _ in bad) if bad else ''))
        if not bad: break
        reqs = []
        for x, out in bad:
            w = os.path.join(ROOT, x['win']); p = params(w, st['model'], st['effort'])
            p['messages'] += [{'role': 'assistant', 'content': open(os.path.join(w, 'answer.txt'), encoding='utf8').read()}, {'role': 'user', 'content': RETRY.format(gate=out[-2500:])}]
            reqs.append(Request(custom_id=os.path.basename(w), params=MessageCreateParamsNonStreaming(**p)))
        bt = cl.messages.batches.create(requests=reqs); st.setdefault('retry_batches', []).append(bt.id); save_state(cfg, st)
        while cl.messages.batches.retrieve(bt.id).processing_status != 'ended': time.sleep(30)
        res2 = {r.custom_id: r for r in cl.messages.batches.results(bt.id)}
        for x, out in bad:
            r = res2.get(os.path.basename(x['win']))
            if r is None or r.result.type != 'succeeded' or r.result.message.stop_reason != 'end_turn': continue
            msg = r.result.message; u = msg.usage; text = ''.join(b.text for b in msg.content if b.type == 'text')
            usd = ((u.input_tokens + (getattr(u, 'cache_creation_input_tokens', 0) or 0) * 1.25 + (getattr(u, 'cache_read_input_tokens', 0) or 0) * 0.1) * pi + u.output_tokens * po) / 2e6
            x['retries'] = rnd; x['usd'] = round(x.get('usd', 0) + usd, 4)
            open(cost, 'a', encoding='utf8').write(f"| {os.path.basename(x['win'])} retry {rnd} (gate failure) | {st['model']} batch API | 1 request | in {u.input_tokens}, out {u.output_tokens} | ${usd:.3f} |\n")
            w = os.path.join(ROOT, x['win']); open(os.path.join(w, 'answer.txt'), 'w', encoding='utf8').write(text); pr = apply_answer(w, text); x['problem'] = '; '.join(pr) if pr else None
        save_state(cfg, st)
    for x in st['windows']:                                    # commit, strictly in page order
        if x.get('done'): continue
        if not x.get('collected') or (x.get('problem') and 'kn_fix' not in x['problem']): print(f"STOP at {x['win']}: {x.get('problem') or 'not collected'}"); break
        r = subprocess.run(['python3', 'tools/rv/batch.py', 'done', str(cfg.vol), x['win'], '--note', f"pp. {x['first']}-{x['last']} (batch API)"], capture_output=True, text=True, cwd=ROOT)
        out = (r.stdout + r.stderr).strip(); print(os.path.basename(x['win']), '->', out.split('\n')[-1][:150])
        if r.returncode: open(os.path.join(ROOT, x['win'], 'gate_failure.txt'), 'w', encoding='utf8').write(out); print(f"STOP at {x['win']}: gates still fail (see {x['win']}/gate_failure.txt); repair en.md / kn.md there, run batch.py done, then collect again"); break
        x['done'] = True; save_state(cfg, st)
    save_state(cfg, st)
    print('windows done:', sum(1 for x in st['windows'] if x.get('done')), 'of', len(st['windows']), '| cost of this batch incl. retries: $%.2f' % sum(x.get('usd', 0) for x in st['windows']))
CMDS = dict(plan=cmd_plan, submit=cmd_submit, status=cmd_status, collect=cmd_collect)
if __name__ == '__main__':
    if len(sys.argv) < 3 or sys.argv[1] not in CMDS: sys.exit(__doc__)
    CMDS[sys.argv[1]](sys.argv[2:])
