#!/usr/bin/env python3
"""Translate a front-matter piece of a volume (its preface / Pīṭhike) that stands before the first numbered page, so that no window covers it.

  python3 tools/rv/api_front.py VOL FIRST_LINE LAST_LINE NAME [--model claude-sonnet-5-5] [--effort medium]
        e.g.  python3 tools/rv/api_front.py 17 129 395 preface
  One direct request (not a batch: a single small job).  Writes volN/work/NAME/kn.md (the Kannada, cleaned as html_to_kn does, with
  `<!-- printed iii -->` at the roman page numbers the text shows), en.md (the model's answer) and en_final.md (Devanagari + IAST by script,
  **NOTE** details split off into notes.json).  It checks, like the window gates: no Kannada script and no remarks left in the English, every
  inline ⟦ ⟧ segment present in kn.md (retyped ones are put back from kn.md and logged).  It does NOT touch the volume files: put the result
  in place with  --install  (English file: after the title lines, before the first printed page; Kannada file likewise; notes to review/notes.tsv)
  when no window job is running.
Key: RIK_API_KEY.  Cost is printed."""
import os, re, sys, json, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rvlib, batch, convert, html_to_kn, api_batch, check_inline
ROOT = rvlib.ROOT
TASK = """This is the volume's own preface (ಪೀಠಿಕೆ) by the translator-editor of the Kannada edition, printed before the contents on pages with roman numbers. Translate ALL of it into English, paragraph by paragraph, completely: it is prose (no Ṛk sections, no Sanskrit blocks, no [[bN]]).
Format of <en>: start with the line `## Preface (Pīṭhike)`; put `### Printed p. iii` (and so on) exactly where kn.md has `<!-- printed iii -->`; then plain paragraphs. Sanskrit words and quotations are copied from kn.md inside ⟦ ⟧ as the brief says; references in Latin letters and digits; the date line and the signature at the end are translated too. No <kn_fix> is needed. Everything else in the brief applies (no remarks of yours; **NOTE**{…} where a decision is needed; no Kannada script in the English).

kn.md of the preface:

"""
def main():
    a = sys.argv[1:]; cfg = rvlib.Cfg(a[0]); lo, hi, name = int(a[1]), int(a[2]), a[3]; opt = lambda k, d: a[a.index(k) + 1] if k in a else d
    model = opt('--model', 'claude-sonnet-5-5'); effort = opt('--effort', 'medium')
    w = os.path.join(cfg.work, name); os.makedirs(w, exist_ok=True)
    if '--install' in a: return install(cfg, w, name)
    src = os.path.join(ROOT, cfg.source[0].split('@')[0]); L = open(src, encoding='utf8').read().split('\n')[lo - 1:hi]; out = []
    for l in L:
        l = html_to_kn.clean_line(l);
        if not l or l == '---': continue
        m = re.fullmatch(r'#*\s*([ivxl]+)\s*', l)
        if m: out += ['', f'<!-- printed {m.group(1)} -->', '']; continue
        out.append(re.sub(r'^#+\s*', '', l))
    kn = '\n'.join(html_to_kn.join_hyphens(out)) + '\n'; open(os.path.join(w, 'kn.md'), 'w', encoding='utf8').write(kn)
    rebuild = '--rebuild' in a   # redo the checks and en_final.md from a hand-repaired en.md, no API call
    if rebuild:
        en = open(os.path.join(w, 'en.md'), encoding='utf8').read(); fixed = []; u = None; usd = 0.0
    else:
        cl = api_batch.client()
        p = dict(model=model, max_tokens=32000, system=api_batch.system_blocks(), output_config={'effort': effort}, messages=[{'role': 'user', 'content': TASK + kn}])
        with cl.messages.stream(**p) as stream: msg = stream.get_final_message()
        u = msg.usage; pi, po = api_batch.PRICES.get(model, (0, 0)); usd = (u.input_tokens * pi + u.output_tokens * po) / 1e6
        text = ''.join(b.text for b in msg.content if b.type == 'text'); open(os.path.join(w, 'answer.txt'), 'w', encoding='utf8').write(text)
        m = re.search(r'<en>\s*\n?(.*?)\n?\s*</en>', text, re.S)
        if msg.stop_reason != 'end_turn' or not m: sys.exit(f'no usable answer (stop_reason {msg.stop_reason}); cost ${usd:.3f}')
        en, fixed = api_batch.autofix_inline(w, m.group(1).strip() + '\n', kn); open(os.path.join(w, 'en.md'), 'w', encoding='utf8').write(en)
    en2, notes = batch.split_notes(en); json.dump(notes, open(os.path.join(w, 'notes.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    t, prob = convert.expand(en2, kn); fp = os.path.join(w, 'en_final.md'); open(fp, 'w', encoding='utf8').write(t)
    subprocess.run(['python3', 'publish/tools/translit/add_iast.py', fp], cwd=ROOT, check=True); t = open(fp, encoding='utf8').read()
    bad = check_inline.mismatches(w); kk = re.findall('[ಀ-೿]+', t)
    prob += [f'inline segment not in kn.md: {x[:50]}' for x in bad] + ([f'{len(kk)} Kannada-script words left, e.g. {kk[0]}'] if kk else [])
    if re.search(r'\[\?\]|\[sic\]|(?i:\bas supplied|\bas printed|running head)|\*\[', en2): prob.append('a translator remark is left in the text')
    cost = os.path.join(ROOT, f'vol{cfg.vol}', 'parts', 'batch_costs.md')
    if not rebuild: open(cost, 'a', encoding='utf8').write(f"| {name} (front matter, source lines {lo}-{hi}) | {model} direct | 1 request | in {u.input_tokens}, out {u.output_tokens} | ${usd:.3f} |\n")
    print(f'{name}: kn {len(kn)} chars, en {len(en)} chars, {len(notes)} NOTE, {len(fixed)} segments put back from kn.md, cost ${usd:.3f}')
    print('PROBLEMS:\n - ' + '\n - '.join(prob) if prob else 'checks: PASS  (not installed: run again with --install when no window job is running)')
def install(cfg, w, name):
    en = open(cfg.en, encoding='utf8').read(); kn = open(cfg.kn, encoding='utf8').read()
    t = open(os.path.join(w, 'en_final.md'), encoding='utf8').read().strip(); k = open(os.path.join(w, 'kn.md'), encoding='utf8').read().strip()
    if '## Preface' in en: sys.exit('the English file already has a preface')
    i = en.index('### Printed p. ') if '### Printed p. ' in en else en.index('---\n\n**Progress note:**'); j = kn.index('<!-- printed ') if '<!-- printed ' in kn else len(kn.rstrip('\n')) + 1
    open(cfg.en, 'w', encoding='utf8').write(en[:i] + t + '\n\n' + en[i:]); open(cfg.kn, 'w', encoding='utf8').write(kn[:j] + ('\n' if j == len(kn.rstrip('\n')) + 1 else '') + '## ಪೀಠಿಕೆ\n\n' + k.replace('<!-- printed ', '<!-- roman ') + '\n\n' + kn[j:])
    nf = os.path.join(ROOT, f'vol{cfg.vol}', 'review', 'notes.tsv'); notes = json.load(open(os.path.join(w, 'notes.json'), encoding='utf8'))
    if notes:
        L = open(nf, encoding='utf8').read().rstrip('\n').split('\n') if os.path.exists(nf) else ['window\tprinted page\tquestion (what needs a decision or a second look)\twords before the mark in the English text\tdecision']
        L[1:1] = [f"{name}\t{pg or ''}\t{det}\t{ctx}\t" for pg, det, ctx in notes]; open(nf, 'w', encoding='utf8').write('\n'.join(L) + '\n')
    open(os.path.join(ROOT, f'vol{cfg.vol}', 'review', 'repair_log.md'), 'a', encoding='utf8').write(f"- front matter: the volume's {name} (translated by tools/rv/api_front.py) inserted before printed p. 1 in the English and the Kannada file; {len(notes)} NOTE rows added at the top of review/notes.tsv.\n")
    print('installed; now run: python3 tools/rv/batch.py audit', cfg.vol)
if __name__ == '__main__':
    if len(sys.argv) < 5: sys.exit(__doc__)
    main()
