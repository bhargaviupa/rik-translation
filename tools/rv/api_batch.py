#!/usr/bin/env python3
"""Translate windows through the Anthropic Message Batches API (half price, no agent, no dispatcher turns).

  python3 tools/rv/api_batch.py plan    VOL [--windows K] [--model claude-sonnet-5-5] [--effort medium]
        prepares the next K windows ahead (work/wPPPP/, as `batch.py prep` does), builds one request per window
        (system = the translator brief, cached; user = the window's TASK.md + its pictures), counts the input tokens
        with the API's token counter (free) and prints the cost estimate.  Nothing is sent.
  python3 tools/rv/api_batch.py submit  VOL          sends the planned requests as ONE batch (this spends money); id in work/api_batch.json
  python3 tools/rv/api_batch.py status  VOL          batch state
  python3 tools/rv/api_batch.py collect VOL          fetches the results: writes each window's en.md (and applies the Kannada-file repairs the model
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
Give <kn_fix> only when the structure of kn.md is wrong (a verse standing as plain lines must become a `> ` block under its standard label; Kannada prose must not be inside a block; a wrong or garbled label; a missed running head needs `<!-- printed N -->` + the head line). Letters and digits are never changed in a fix. Block numbers [[bN]] in your <en> must be those of kn.md AFTER your fixes are applied (blocks counted from 1 in order of appearance). If a picture is attached, it is the `[figure: …]` of kn.md: if it only repeats a verse block that kn.md already has, remove the figure line with a fix and say so in an italic note; otherwise write its verse into kn.md with a fix, letter by letter in Kannada script.

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
    if st.get('batch_id'): sys.exit(f"a batch is already recorded ({st['batch_id']}): collect it, or delete work/api_batch.json")
    reqs = [Request(custom_id=os.path.basename(x['win']), params=MessageCreateParamsNonStreaming(**params(os.path.join(ROOT, x['win']), st['model'], st['effort']))) for x in st['windows']]
    b = client().messages.batches.create(requests=reqs); st['batch_id'] = b.id; save_state(cfg, st)
    print('submitted', b.id, b.processing_status, len(reqs), 'requests')
def cmd_status(a):
    cfg = rvlib.Cfg(a[0]); st = load_state(cfg)
    b = client().messages.batches.retrieve(st['batch_id']); c = b.request_counts
    print(b.id, b.processing_status, f'processing {c.processing} succeeded {c.succeeded} errored {c.errored} canceled {c.canceled} expired {c.expired}')
    return b.processing_status
def apply_answer(w, text):
    """write en.md and apply the kn.md repairs; returns a list of problems"""
    prob = []; m = re.search(r'<en>\s*\n?(.*?)\n?\s*</en>', text, re.S)
    if not m: return ['no <en> … </en> in the answer']
    kp = os.path.join(w, 'kn.md'); kn = open(kp, encoding='utf8').read()
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
    open(os.path.join(w, 'en.md'), 'w', encoding='utf8').write(m.group(1).strip() + '\n')
    return prob
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
    for x in st['windows']:                                    # gates and commit, strictly in page order
        if x.get('done'): continue
        if not x.get('collected') or (x.get('problem') and 'kn_fix adds' not in x['problem']): print(f"STOP at {x['win']}: {x.get('problem') or 'not collected'}"); break
        r = subprocess.run(['python3', 'tools/rv/batch.py', 'done', str(cfg.vol), x['win'], '--note', f"pp. {x['first']}-{x['last']} (batch API)"], capture_output=True, text=True, cwd=ROOT)
        out = (r.stdout + r.stderr).strip(); print(x['win'], '->', out.split('\n')[-1][:200])
        if r.returncode: open(os.path.join(ROOT, x['win'], 'gate_failure.txt'), 'w', encoding='utf8').write(out); print(f"STOP at {x['win']}: gates failed (see {x['win']}/gate_failure.txt); repair en.md / kn.md there, run batch.py done, then collect again"); break
        x['done'] = True; save_state(cfg, st)
    save_state(cfg, st)
CMDS = dict(plan=cmd_plan, submit=cmd_submit, status=cmd_status, collect=cmd_collect)
if __name__ == '__main__':
    if len(sys.argv) < 3 or sys.argv[1] not in CMDS: sys.exit(__doc__)
    CMDS[sys.argv[1]](sys.argv[2:])
