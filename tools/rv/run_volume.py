#!/usr/bin/env python3
"""NOT YET RUN END TO END (Nov 10 2026: the cloud session's permission rules refused starting headless agents from a script; the headless call itself was tested once by hand).
Script dispatcher: translate a volume window after window with headless Sonnet runs (no model is used for dispatching).

  python3 tools/rv/run_volume.py VOL [--max N] [--model sonnet] [--timeout 1200]

Per window:  batch.py next (audit by script, cost line, prep)  ->  `claude -p` (one fresh run: read BRIEF.md + TASK.md, write en.md, batch.py done)
             ->  the script checks that the progress note moved to the window's last page  ->  next window.
Exact usage of every run (input / cache write / cache read / output tokens, cost, turns, seconds) goes to volN/parts/batch_costs.md
and volN/work/run_log.jsonl.  Stops on: audit failure, a window that fails twice, end of the supplied text, --max, or a file volN/work/STOP.
Run it in the background and read the tail of volN/work/run_volume.log; never start two for one volume (lock file volN/work/RUNNING)."""
import os, re, sys, json, time, subprocess
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
PROMPT = """You are the translator agent for one window of Vol {vol} of the Rigveda translation in {root} (the branch is already checked out; never switch branches or touch git yourself).

1. In ONE message read tools/rv/BRIEF.md and {win}/TASK.md. Follow BRIEF.md exactly.
2. Write {win}/en.md in one go. Translate every paragraph completely; never shorten or summarise because of the length. Use ⟦first words~~last words⟧ for long Sanskrit quotations (copy the first and last words exactly from kn.md).
3. Run `python3 tools/rv/batch.py done {vol} {win} --note "…"` until it prints VERIFIED.{retry}
Use as few tool calls as possible. Final answer in <= 4 lines: the DONE line of `done`, hand-fixes, doubts, anything recurring."""
RETRY = "\nA previous run of this window stopped before VERIFIED: {win}/en.md may already exist. Read it, finish or repair it, and run `done`."

def sh(cmd, timeout=None):
    return subprocess.run(cmd, shell=isinstance(cmd, str), capture_output=True, text=True, cwd=ROOT, timeout=timeout)
def page(vol):
    s = open(os.path.join(ROOT, f'vol{vol}', f'Rigveda_Samhita_Vol{vol}_English_Translation.md'), encoding='utf8').read()
    m = re.search(r'Done through printed p\. (\d+)', s[s.rfind('**Progress note:**'):]); return int(m.group(1))
def log(vol, msg):
    line = time.strftime('%H:%M:%S ') + msg; print(line, flush=True)
    open(os.path.join(ROOT, f'vol{vol}', 'work', 'run_volume.log'), 'a', encoding='utf8').write(line + '\n')

def main():
    a = sys.argv[1:]; vol = int(a[0]); opt = lambda k, d: a[a.index(k) + 1] if k in a else d
    mx = int(opt('--max', 10 ** 6)); model = opt('--model', 'sonnet'); tmo = int(opt('--timeout', 1200))
    work = os.path.join(ROOT, f'vol{vol}', 'work'); os.makedirs(work, exist_ok=True)
    lock = os.path.join(work, 'RUNNING'); stop = os.path.join(work, 'STOP')
    if os.path.exists(lock): sys.exit(f'{lock} exists: another run_volume is active (delete the file if it is stale)')
    open(lock, 'w').write(str(os.getpid())); flags = ''; n = 0; tot = 0; t00 = time.time()
    try:
        while n < mx:
            if os.path.exists(stop): log(vol, 'STOP file found'); break
            r = sh(f'python3 tools/rv/batch.py next {vol}{flags}'); out = r.stdout.strip()
            m = re.search(r'next window (\S+) \(pp\. (\d+)-(\d+)', out)
            if r.returncode or not m: log(vol, 'stopped: ' + out[-400:].replace('\n', ' | ')); break
            win, last = m.group(1), int(m.group(3)); ok = False
            for attempt in (1, 2):
                prompt = PROMPT.format(vol=vol, root=ROOT, win=win, retry=RETRY.format(win=win) if attempt == 2 else '')
                t0 = time.time()
                try:
                    r = sh(['claude', '-p', prompt, '--model', model, '--output-format', 'json', '--permission-mode', 'acceptEdits',
                            '--allowedTools', 'Bash', 'Read', 'Write', 'Edit'], timeout=tmo)
                    j = json.loads(r.stdout) if r.stdout.strip().startswith('{') else {}
                except subprocess.TimeoutExpired:
                    j = {'result': 'TIMEOUT'}
                u = j.get('usage', {}); sec = round(time.time() - t0)
                tok = dict(inp=u.get('input_tokens', 0), cw=u.get('cache_creation_input_tokens', 0), cr=u.get('cache_read_input_tokens', 0), out=u.get('output_tokens', 0))
                total = sum(tok.values()); tot += total; done = page(vol)
                rec = dict(win=win, attempt=attempt, sec=sec, turns=j.get('num_turns'), usd=j.get('total_cost_usd'), **tok, total=total, page=done,
                           report=(j.get('result') or '')[:600])
                open(os.path.join(work, 'run_log.jsonl'), 'a', encoding='utf8').write(json.dumps(rec, ensure_ascii=False) + '\n')
                ok = done >= last
                log(vol, f"{win} attempt {attempt}: {'OK' if ok else 'NOT DONE'} p. {done} | {total} tokens (out {tok['out']}, cache read {tok['cr']}) | {j.get('num_turns')} turns | {sec}s | ${j.get('total_cost_usd')}")
                flags = f" --tokens \"{total} (in {tok['inp']}, cache write {tok['cw']}, cache read {tok['cr']}, out {tok['out']}; ${round(j.get('total_cost_usd') or 0, 3)})\" --tools {j.get('num_turns')} --min {round(sec / 60, 1)} --model {model}"
                if ok: break
            if not ok: log(vol, f'stopped: {win} failed twice (see run_log.jsonl)'); break
            n += 1
        log(vol, f'run ended: {n} windows, {tot} tokens, {round((time.time() - t00) / 60)} min, done through p. {page(vol)}')
    finally:
        os.remove(lock)

if __name__ == '__main__':
    if len(sys.argv) < 2: sys.exit(__doc__)
    main()
