#!/usr/bin/env python3
"""English + Kannada Pīṭhike for a volume WITHOUT volcfg.json (legacy Vols 3-6, 10): one direct API request, then install.

  python3 tools/rv/en_front.py VOL FIRST_LINE LAST_LINE --source FILE [--html] [--install] [--before 'LINE-PREFIX']

Same method as tools/rv/api_front.py (same task text, checks and cost note); the Kannada comes from tools/rv/kn_front.py's cleaning.
--html: the supplied file is HTML (Vol 10): tags are stripped first.  Without --install nothing in the volume files changes
(work in volN/review/preface/).  --install puts '## Preface (Pīṭhike)' into the English file before the first line that starts with
--before (default '## ') and '## ಪೀಠಿಕೆ' into the Kannada file before its first `<!-- printed` mark; NOTE details go to
volN/review/preface_notes.tsv; the repair is logged in volN/review/repair_log.md.  Key: RIK_API_KEY."""
import os, re, sys, json, subprocess, html as H
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rvlib, batch, convert, html_to_kn, api_batch, check_inline, api_front
ROOT = rvlib.ROOT
a = sys.argv[1:]
if len(a) < 3: sys.exit(__doc__)
vol = int(a[0]); lo, hi = int(a[1]), int(a[2]); opt = lambda k, d=None: a[a.index(k) + 1] if k in a else d
src = os.path.join(ROOT, opt('--source')); w = os.path.join(ROOT, f'vol{vol}', 'review', 'preface'); os.makedirs(w, exist_ok=True)
EN = os.path.join(ROOT, f'vol{vol}', f'Rigveda_Samhita_Vol{vol}_English_Translation.md'); KN = os.path.join(ROOT, f'vol{vol}', f'Rigveda_Samhita_Vol{vol}_Kannada_Text.md')
if '--install' not in a:
    out = []
    for l in open(src, encoding='utf8').read().split('\n')[lo - 1:hi]:
        if '--html' in a: l = H.unescape(re.sub(r'<[^>]+>', '', l))
        l = html_to_kn.clean_line(l)
        if not l or l == '---': continue
        m = re.fullmatch(r'#*\s*([ivxl]+)\s*', l)
        if m: out += ['', f'<!-- printed {m.group(1)} -->', '']; continue
        out.append(re.sub(r'^#+\s*', '', l))
    kn = '\n'.join(html_to_kn.join_hyphens(out)).strip() + '\n'; open(os.path.join(w, 'kn.md'), 'w', encoding='utf8').write(kn)
    cl = api_batch.client(); model = 'claude-sonnet-5-5'
    p = dict(model=model, max_tokens=32000, system=api_batch.system_blocks(), output_config={'effort': 'medium'}, messages=[{'role': 'user', 'content': api_front.TASK + kn}])
    with cl.messages.stream(**p) as s: msg = s.get_final_message()
    u = msg.usage; pi, po = api_batch.PRICES.get(model, (0, 0)); usd = (u.input_tokens * pi + u.output_tokens * po) / 1e6
    text = ''.join(b.text for b in msg.content if b.type == 'text'); open(os.path.join(w, 'answer.txt'), 'w', encoding='utf8').write(text)
    m = re.search(r'<en>\s*\n?(.*?)\n?\s*</en>', text, re.S)
    if msg.stop_reason != 'end_turn' or not m: sys.exit(f'no usable answer ({msg.stop_reason}); cost ${usd:.3f}')
    en, fixed = api_batch.autofix_inline(w, m.group(1).strip() + '\n', kn); open(os.path.join(w, 'en.md'), 'w', encoding='utf8').write(en)
    en2, notes = batch.split_notes(en); json.dump(notes, open(os.path.join(w, 'notes.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    t, prob = convert.expand(en2, kn); fp = os.path.join(w, 'en_final.md'); open(fp, 'w', encoding='utf8').write(t)
    subprocess.run(['python3', 'publish/tools/translit/add_iast.py', fp, '--inline-only'], cwd=ROOT, check=True); t = open(fp, encoding='utf8').read()
    bad = check_inline.mismatches(w); kk = re.findall('[ಀ-೿]+', t)
    prob += [f'inline segment not in kn.md: {x[:50]}' for x in bad] + ([f'{len(kk)} Kannada-script words left, e.g. {kk[0]}'] if kk else [])
    if re.search(r'\[\?\]|\[sic\]|(?i:\bas supplied|\bas printed|running head)|\*\[', en2): prob.append('a translator remark is left in the text')
    open(os.path.join(ROOT, f'vol{vol}', 'review', 'preface_cost.md'), 'a', encoding='utf8').write(f"| Pīṭhike, source lines {lo}-{hi} | {model} direct | in {u.input_tokens}, out {u.output_tokens} | ${usd:.3f} |\n")
    print(f'vol{vol}: kn {len(kn)} chars, en {len(en)} chars, {len(notes)} NOTE, cost ${usd:.3f}'); print('PROBLEMS:\n - ' + '\n - '.join(prob) if prob else 'checks: PASS')
else:
    en = open(EN, encoding='utf8').read(); kn = open(KN, encoding='utf8').read()
    t = open(os.path.join(w, 'en_final.md'), encoding='utf8').read().strip(); k = open(os.path.join(w, 'kn.md'), encoding='utf8').read().strip()
    if '## Preface' in en or '## ಪೀಠಿಕೆ' in kn: sys.exit('a preface is already in one of the files')
    lines = en.split('\n'); pre = opt('--before', '## ')
    i = next(n for n, l in enumerate(lines) if n > 0 and l.startswith(pre)); j = kn.index('<!-- printed ') if '<!-- printed ' in kn else len(kn)
    open(EN, 'w', encoding='utf8').write('\n'.join(lines[:i]) + '\n' + t + '\n\n' + '\n'.join(lines[i:]))
    open(KN, 'w', encoding='utf8').write(kn[:j] + '## ಪೀಠಿಕೆ\n\n' + k.replace('<!-- printed ', '<!-- roman ') + '\n\n' + kn[j:])
    notes = json.load(open(os.path.join(w, 'notes.json'), encoding='utf8'))
    if notes: open(os.path.join(ROOT, f'vol{vol}', 'review', 'preface_notes.tsv'), 'w', encoding='utf8').write('\n'.join(f"{pg or ''}\t{det}\t{ctx}" for pg, det, ctx in notes) + '\n')
    open(os.path.join(ROOT, f'vol{vol}', 'review', 'repair_log.md'), 'a', encoding='utf8').write(f"- 2026-11-28 front matter: the editor's Pīṭhike (from the supplied text, translated by tools/rv/en_front.py) inserted in the English file (before '{pre}') and in the Kannada file; {len(notes)} NOTE details in review/preface_notes.tsv.\n")
    print('installed')
