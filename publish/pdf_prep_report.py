#!/usr/bin/env python3
"""Facts about the state of one or many volumes, for the preparation of their review PDFs (docs/prompts/VOLN_PDF_PREP_PROMPT.md, Step 0).

  python3 publish/pdf_prep_report.py            one table row per volume 1-30
  python3 publish/pdf_prep_report.py N [N …]    the same for the volumes named, with the details (headings before the first Sūkta, builder, what is missing)
  python3 publish/pdf_prep_report.py N --pdf    also runs publish/pdf_check.py on volN/review/*.pdf

Nothing is written, nothing is built.  The prompt takes every fact about a volume from here and never from a table typed into the prompt,
because such a table is out of date as soon as another session merges into main."""
import re, os, sys, json, subprocess, pathlib
PUB = pathlib.Path(__file__).resolve().parent; ROOT = PUB.parent
sys.path.insert(0, str(ROOT / 'tools' / 'rv')); sys.path.insert(0, str(PUB))
KN = re.compile('[ಀ-೿]'); DOTS = re.compile(r'(\.\.\.|…)[*_")\]]*\s*$')
def eng(n): return ROOT / f'vol{n}' / f'Rigveda_Samhita_Vol{n}_English_Translation.md'
def kan(n):
    for p in (ROOT / f'vol{n}' / f'Rigveda_Samhita_Vol{n}_Kannada_Text.md', ROOT / f'vol{n}' / 'kannada' / f'Rigveda_Samhita_Vol{n}_Kannada_Text.md'):
        if p.exists(): return p
def builder(n):
    cfg = ROOT / f'vol{n}' / 'pubcfg.json'
    old = 'build_vol1.py' if n == 1 else 'build_vol2.py' if n == 2 else 'build.py' if n == 3 else 'build_vol45.py' if 4 <= n <= 10 else None
    if cfg.exists():
        if json.loads(cfg.read_text(encoding='utf8')).get('kannada_only'): return (old or '?') + ' (English); volbook.py (Kannada)'
        return 'volbook.py'
    return old or 'none: no pubcfg.json yet'

def facts(n, detail=False):
    f = {'vol': n}; e = eng(n)
    if not e.exists(): f['verdict'] = 'NOT READY: no English file'; return f
    L = e.read_text(encoding='utf8').split('\n'); f['lines'] = len(L)
    f['layout'] = ('Printed p.' if any(l.startswith('### Printed p.') for l in L[:3000]) else 'Page N' if any(re.match(r'#{2,4} \[?Pages? \d', l) for l in L[:3000]) else '?')
    f['sukta'] = sum(bool(re.match(r'#{2,4} S[ūu]kta', l)) for l in L)
    f['rik'] = sum(bool(re.match(r'#{3,5} (Ṛk|Rik|Ṛc)\b', l)) for l in L)
    f['q'] = sum('[?]' in l for l in L); f['sic'] = sum('[sic' in l for l in L)
    f['note'] = sum('**NOTE**' in l for l in L); f['gloss'] = sum('**GLOSS**' in l for l in L)
    f['kn_script'] = sum(bool(KN.search(l)) for l in L); f['dots'] = sum(bool(DOTS.search(l)) for l in L if not l.startswith('#'))
    last = next((l for l in reversed(L) if l.strip()), '')
    m = re.search(r'Done through printed p\. (\d+)(.*)', ' '.join(L[-6:]))
    f['progress'] = (f'to p. {m.group(1)}' + (' (final)' if re.search('final|FINAL|end of volume|colophon', m.group(2), re.I) else '')) if m else 'closed file'
    vc = ROOT / f'vol{n}' / 'volcfg.json'
    if vc.exists() and m:
        src = json.loads(vc.read_text(encoding='utf8')).get('source', ''); src = ' '.join(src) if isinstance(src, list) else str(src); mm = re.search(r'@\d+-(\d+)', src)
        if mm and int(m.group(1)) < int(mm.group(1)): f['progress'] += f' of {mm.group(1)}: UNFINISHED'
    k = kan(n); f['kannada'] = (f'{k.relative_to(ROOT).parent if k.parent.name == "kannada" else "yes"}' if k else 'none')
    if k: f['kn_pages'] = sum(1 for l in k.read_text(encoding='utf8').split('\n') if l.startswith('<!-- printed'))
    f['builder'] = builder(n); f['pubcfg'] = (ROOT / f'vol{n}' / 'pubcfg.json').exists()
    f['assets'] = [x for x in ('frontmatter_en.json', 'contents_en.json') if (ROOT / f'vol{n}' / x).exists()]
    # headings before the first Maṇḍala/Sūkta heading: preface, contents, introduction
    first = next((i for i, l in enumerate(L) if re.match(r'#{1,3} (S[ūu]kta|Maṇḍala|Mandala)\b', l)), len(L))
    heads = [(i + 1, l) for i, l in enumerate(L[:first]) if re.match(r'#{1,4} ', l) and not re.match(r'#{3,4} \[?(Printed )?Pages? ', l) and not re.match(r'#{3,4} Printed p\.', l)]
    f['heads_before_text'] = heads
    f['preface'] = any(re.search(r'p[īi][ṭt]hik|preface|prastāvan', h, re.I) for _, h in heads)
    f['contents'] = any(re.search(r'contents|anukrama', h, re.I) for _, h in heads)
    f['intro'] = any(re.search(r'introduction|pūrva|purva', h, re.I) for _, h in heads)
    try:
        import cleanup_remarks as C
        c = {k_: len([x for x in fn(L) if x != 'last']) for k_, fn in (('session', C.kind_session), ('paren', C.kind_paren), ('ownnote', C.kind_ownnote))}
        f['cleanup'] = c; f['cleanup_total'] = sum(c.values())
    except Exception as ex: f['cleanup'] = f'? {ex}'; f['cleanup_total'] = None
    f['removed_remarks'] = (ROOT / f'vol{n}' / 'review' / 'removed_remarks.tsv').exists()
    bn = json.loads((PUB / 'build_numbers.json').read_text()) if (PUB / 'build_numbers.json').exists() else {}
    f['builds'] = {k_: v for k_, v in bn.items() if k_.startswith(f'vol{n}_')}
    pdfs = sorted((ROOT / f'vol{n}' / 'review').glob(f'vol{n}_full*.pdf')) if (ROOT / f'vol{n}' / 'review').exists() else []
    f['pdfs'] = [p.name for p in pdfs]
    if '--pdf' in sys.argv:
        f['pdf_check'] = [subprocess.run(['python3', str(PUB / 'pdf_check.py'), str(p)], capture_output=True, text=True).stdout.strip() for p in pdfs]
    f['family'] = 'A' if n <= 10 else ('B' if (f['q'] + f['sic']) > f['note'] else 'C')     # A scan-era (old builders); B older text with remarks; C NOTE style
    f['contents_en_json'] = 'contents_en.json' in f['assets']; f['frontmatter_en_json'] = 'frontmatter_en.json' in f['assets']
    why = []
    if 'UNFINISHED' in f['progress']: why.append('translation unfinished')
    elif f['family'] != 'A' and f['progress'].startswith('to p.') and 'final' not in f['progress']: why.append('completeness unclear: the progress note does not say final; read STATUS.md')
    if f['builder'].startswith('none'): why.append('no pubcfg.json (the session writes a minimal one)')
    if f['layout'] == '?': why.append('page-heading layout not recognised')
    f['done'] = f['removed_remarks'] and bool(f['builds'])
    f['verdict'] = 'NOT READY: ' + '; '.join(why) if 'UNFINISHED' in f['progress'] else ('prepared already' if f['done'] else 'ready for the procedure' + (' (' + '; '.join(why) + ')' if why else ''))
    return f
def main():
    args = [int(a) for a in sys.argv[1:] if a.isdigit()]
    vols = args or [n for n in range(1, 31) if (ROOT / f'vol{n}').is_dir()]
    rows = [facts(n) for n in vols]
    if not args:
        print('| Vol | family | English lines | layout | builder | Kannada | state | [?] [sic] | NOTE GLOSS | Kannada-script lines | lines in dots | clean-up (dry run) | preface | contents | intro | prepared | verdict |')
        print('|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|')
        for f in rows:
            if 'lines' not in f: print(f"| {f['vol']} | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | {f['verdict']} |"); continue
            print(f"| {f['vol']} | {f['family']} | {f['lines']} | {f['layout']} | {f['builder']} | {f['kannada']} | {f['progress']} | {f['q']} {f['sic']} | {f['note']} {f['gloss']} | {f['kn_script']} | {f['dots']} | {f['cleanup_total']} | {'yes' if f['preface'] else 'no'} | {'yes' if f['contents'] else ('contents_en.json' if f['contents_en_json'] else 'no')} | {'yes' if f['intro'] else 'no'} | {'yes' if f['done'] else 'no'} | {f['verdict']} |")
    else:
        for f in rows:
            print(f"=== Vol {f['vol']}: {f['verdict']}")
            for k_, v in f.items():
                if k_ in ('vol', 'verdict', 'heads_before_text', 'pdf_check'): continue
                print(f'  {k_}: {v}')
            print('  headings before the text (line: heading):'); [print(f'    {i}: {h[:110]}') for i, h in f.get('heads_before_text', [])[:25]]
            for t in f.get('pdf_check', []): print('  ' + t.replace('\n', '\n  '))
if __name__ == '__main__': main()
