#!/usr/bin/env python3
"""Pilot of the title structure (chapter - level 1 - level 2 - level 3) on a few pages of both books of a volume (user, Nov 26 2026:
"the levels part needs pilot first").

  python3 publish/pilot_levels.py N        reads volN/data/headings_pilot.tsv, writes volN/review/pilot_levels_Kan.pdf and _Eng.pdf

The mapping file names, for each title, its level, its line in the Kannada text and in the English file, and the wording to print
(level 'drop' = a heading of the English that the original does not have: it is not printed as a heading).  The excerpt runs from the first
page mark before the first title to the last page mark after the last one.  Nothing in the volume's files is changed: this only shows
how the levels would look, with the same print step and styles as the books (publish/printfix.py, style_footer.css: .lv1 .lv2 .lv3)."""
import re, sys, csv, pathlib, subprocess
PUB = pathlib.Path(__file__).resolve().parent; ROOT = PUB.parent
sys.path.insert(0, str(PUB)); import printfix
MARK = {'chapter': '## {t} {{.chapter}}', '1': '### {t} {{.lv1}}', '2': '#### {t} {{.lv2}}', '3': '##### {t} {{.lv3}}'}
def pandoc(md): return subprocess.run(['pandoc', '-f', 'markdown-yaml_metadata_block-smart+pipe_tables', '-t', 'html5', '--wrap=none'], input=md, capture_output=True, text=True, check=True).stdout
def excerpt(L, lines, page_rx):
    a = max(i for i in range(min(lines)) if re.match(page_rx, L[i])); b = min((i for i in range(max(lines), len(L)) if re.match(page_rx, L[i])), default=len(L))
    return a, b
def main():
    vol = int(sys.argv[1]); d = ROOT / f'vol{vol}'
    rows = list(csv.DictReader(open(d / 'data' / 'headings_pilot.tsv', encoding='utf8'), delimiter='\t'))
    kn = next(p for p in (d / f'Rigveda_Samhita_Vol{vol}_Kannada_Text.md', d / 'kannada' / f'Rigveda_Samhita_Vol{vol}_Kannada_Text.md') if p.exists())
    for lang, f, col, tcol, page_rx in (('kn', kn, 'kn_line', 'kn_title', r'<!-- printed \d+ -->'), ('en', d / f'Rigveda_Samhita_Vol{vol}_English_Translation.md', 'en_line', 'en_title', r'#+ \[?Pages? \d+')):
        L = f.read_text(encoding='utf8').split('\n'); use = [r for r in rows if r[col]]
        a, b = excerpt(L, [int(r[col]) - 1 for r in use], page_rx); new = {}
        for r in use:
            i = int(r[col]) - 1
            if r['level'] == 'drop': new[i] = [re.sub(r'\s*—.*$', '', L[i]) if re.match(page_rx, L[i]) else '']; continue
            new.setdefault(i, []).append(MARK[r['level']].format(t=r[tcol]))
            if r['level'] == 'chapter': new[i + 1] = new.get(i + 1, []) if not L[i + 1].strip() else []; nxt = next(k for k in range(i + 1, i + 4) if L[k].strip()); new[nxt] = []     # the title line is in the heading
        out = []
        for i in range(a, b):
            if i in new: out += [x for h in new[i] for x in ('', h, '')]
            elif lang == 'kn' and re.fullmatch(r'\*\[.*\]\*', L[i].strip()): continue
            else: out.append(L[i])
        md = '\n'.join(out)
        if lang == 'kn': md = re.sub(r'<!-- printed (\d+) -->', lambda m: f'<div class="pgmark" id="p{m.group(1)}" data-p="Kannada edition p. {m.group(1)}"></div>\n', md)
        body = pandoc(md)
        css = ''.join(f'<link rel="stylesheet" href="{x}">' for x in ('style.css', 'style_vol1.css', 'style_volbook.css') + (('style_volbook_kan.css',) if lang == 'kn' else ()) + ('style_footer.css',))
        title = f'Ṛgveda-saṃhitā, Volume {vol} — pilot of the title levels ' + ('(Kannada text)' if lang == 'kn' else '(English translation)')
        doc = f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><title>{title}</title>{css}</head><body>\n{body}\n</body></html>'
        doc = printfix.fix(doc, quiet=True, stamp_it=False)
        from weasyprint import HTML
        pdf = d / 'review' / f'pilot_levels_{"Kan" if lang == "kn" else "Eng"}.pdf'
        HTML(string=doc, base_url=str(PUB)).write_pdf(pdf); print('wrote', pdf.relative_to(ROOT))
if __name__ == '__main__': main()
