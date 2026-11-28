#!/usr/bin/env python3
"""Fit the printed-contents settings of a volume's pubcfg.json from its own supplied text (Nov 28 2026) and check the parsed contents.

  python3 publish/contents_kan.py N [N …] [--write] [--force]

For each volume: finds, in the files of volcfg `source`, the one that holds the printed contents (heading ವಿಷಯಾನುಕ್ರಮಣಿಕೆ … closing line
'ವಿಷಯಾನುಕ್ರಮಣಿಕೆ ಸಮಾಪ್ತವು'), parses it with publish/tools/frontmatter/contents_parse.py and reports: blocks, sūktas, items without a page, page range,
pages that are not in the Kannada Text file (no `<!-- printed N -->`), pages that go backwards.  --write sets `supplied_md` and `contents`
{start, end, heading} in volN/pubcfg.json (an existing `contents` is kept unless --force).  The heading's middle line is taken from the supplied
text only where it prints one ('ಋಗ್ವೇದಸಂಹಿತೆಯ … ಭಾಗದ' within 3 lines above the heading); otherwise it is left empty, not composed.
A page number wrong in the print stays as printed; the report lists the suspect ones (`contents_target_overrides` is for a link target only)."""
import re, sys, json, pathlib
PUB = pathlib.Path(__file__).resolve().parent; ROOT = PUB.parent
sys.path.insert(0, str(PUB / 'tools' / 'frontmatter')); import contents_parse
START, END = 'ವಿಷಯಾನುಕ್ರಮಣಿಕೆ', 'ವಿಷಯಾನುಕ್ರಮಣಿಕೆ ಸಮಾಪ್ತವು'
KD = str.maketrans('೦೧೨೩೪೫೬೭೮೯', '0123456789')
def main(a):
    force = '--force' in a; write = '--write' in a
    for v in [int(x) for x in a if x.isdigit()]:
        vcp = ROOT / f'vol{v}' / 'volcfg.json'; p = ROOT / f'vol{v}' / 'pubcfg.json'
        vc = json.loads(vcp.read_text(encoding='utf8')) if vcp.exists() else {'source': [str(f.relative_to(ROOT)) for f in sorted((ROOT / f'vol{v}' / 'html').glob('*.md')) if not re.search(r'front_transcribed|filled|machine_read|part2|marked|ordered|review|merged', f.name)]}   # older volumes have no volcfg.json: the supplied files of volN/html/
        cfg = json.loads(p.read_text(encoding='utf8')) if p.exists() else None
        if cfg is None: print(f'vol{v}: no pubcfg.json'); continue
        src = None
        for s in vc['source']:
            f = s.split('@')[0]; L = (ROOT / f).read_text(encoding='utf8', errors='replace').split('\n')
            if any(END in l for l in L) and any(START in l and END not in l for l in L): src, lines = f, L; break
        if not src: print(f'vol{v}: no file with the contents heading and the closing line'); continue
        try: blocks = contents_parse.parse(lines, START, END, {})
        except Exception as ex: print(f'vol{v}: parse failed ({type(ex).__name__})'); continue
        idx = [i for i, l in enumerate(lines) if START in l and END not in l]; s = idx[1] if len(idx) > 1 else idx[0]
        mid = next((re.sub(r'[#|*\s]+$|^[#|*\s]+', '', l) for l in lines[max(0, s - 3):s] if re.search(r'ಋಗ್ವೇದಸಂಹಿತೆಯ.*ಭಾಗದ', l)), '')
        kn = (ROOT / f'vol{v}' / f'Rigveda_Samhita_Vol{v}_Kannada_Text.md').read_text(encoding='utf8')
        marks = {int(x) for x in re.findall(r'(?m)^<!-- printed (\d+) -->$', kn)}
        items = [b for b in blocks if b['t'] == 'item']; pages = [b['page'] for b in items if b['page']]
        nopage = [b['text'][:30] for b in items if not b['page']]
        absent = sorted({x for x in pages if x not in marks}); back = [(pages[i - 1], pages[i]) for i in range(1, len(pages)) if pages[i] < pages[i - 1]]
        sk = sum(1 for b in blocks if b['t'] == 'sukta')
        print(f'vol{v}: {src.split("/")[-1]}  blocks {len(blocks)}, sūktas {sk}, items {len(items)} (no page: {len(nopage)}), pages {min(pages) if pages else "-"}–{max(pages) if pages else "-"}, '
              f'not in the Kannada file {absent[:6] or "none"}, going backwards {len(back)} {back[:3]}, middle heading line: {"printed" if mid else "none"}')
        if write:
            if cfg.get('contents') and not force: print(f'   contents already set (kept)'); continue
            cfg['supplied_md'] = src
            cfg['contents'] = {'start': START, 'end': END, 'heading': ['॥ ಶ್ರೀಃ ॥', mid, 'ವಿಷಯಾನುಕ್ರಮಣಿಕೆ']}
            p.write_text(json.dumps(cfg, ensure_ascii=False, indent=1) + '\n', encoding='utf8'); print('   pubcfg.json: contents set')
if __name__ == '__main__': main(sys.argv[1:])
