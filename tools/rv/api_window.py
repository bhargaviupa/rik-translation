#!/usr/bin/env python3
"""Prepare ONE window of chosen pages afresh from the supplied text and translate it by one direct API request (not a batch).

  python3 tools/rv/api_window.py VOL P1,P2,... [--model claude-sonnet-5-5] [--effort medium] [--no-send]
        e.g.  python3 tools/rv/api_window.py 23 372,373      (pages that a source repair made appear, or a window whose source changed)
  Prepares vol/work/wPPPP (PPPP = the first page; as `batch.py prep` does, but for exactly these pages), sends it with the same brief and
  repairs as api_batch (apply_answer), logs the cost in volN/parts/batch_costs.md.  It does NOT commit and does NOT touch the volume files.
  When the window belongs after the progress note, `batch.py done` / `collect` commits it; when it belongs INSIDE the finished text, insert it
  as a logged repair (docs/LESSONS).  Key: RIK_API_KEY."""
import os, sys, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rvlib, batch, api_batch
ROOT = rvlib.ROOT
def main():
    a = sys.argv[1:]
    if len(a) < 2: sys.exit(__doc__)
    vol, pages = a[0], [int(x) for x in a[1].split(',')]
    opt = lambda k, d: a[a.index(k) + 1] if k in a else d
    model, effort = opt('--model', 'claude-sonnet-5-5'), opt('--effort', 'medium')
    cfg = rvlib.Cfg(vol)
    batch.next_pages = lambda cfg_, dp, dpdf, src: [(p, cfg_.printed_to_pdf(p)) for p in pages]
    batch.cmd_prep([vol], quiet=True, after=pages[0] - 1)
    w = os.path.join(cfg.work, f'w{pages[0]:04d}')
    for f in ('kn.md.orig', 'pages.json.orig', 'answer.txt', 'gate_failure.txt'):
        if os.path.exists(os.path.join(w, f)): os.remove(os.path.join(w, f))
    if '--no-send' in a: print('prepared', w); return
    cl = api_batch.client()
    with cl.messages.stream(**api_batch.params(w, model, effort)) as s: msg = s.get_final_message()
    text = ''.join(b.text for b in msg.content if b.type == 'text'); open(os.path.join(w, 'answer.txt'), 'w', encoding='utf8').write(text)
    pi, po = api_batch.PRICES.get(model, (0, 0)); usd = (msg.usage.input_tokens * pi + msg.usage.output_tokens * po) / 1e6
    prob = api_batch.apply_answer(w, text)
    cost = os.path.join(ROOT, f'vol{cfg.vol}', 'parts', 'batch_costs.md')
    open(cost, 'a', encoding='utf8').write(f"| w{pages[0]:04d} (pp. {pages[0]}-{pages[-1]}, direct request) | {model} | in {msg.usage.input_tokens}, out {msg.usage.output_tokens} | ${usd:.3f} |\n")
    print(f'{w}: stop_reason {msg.stop_reason}, cost ${usd:.3f}, problems: {prob}')
if __name__ == '__main__': main()
