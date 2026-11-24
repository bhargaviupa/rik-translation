#!/usr/bin/env python3
"""Readable Markdown of the complete Devanagari text of the Wikisource index (Saṃhitā, Pada, Sāyaṇa-bhāṣya), one file per maṇḍala.

    python3 tools/rv/ws_export.py        # writes refs/wikisource/export/Rigveda_Devanagari_M00.md … M10.md  (needs the index)

Per sūkta: the ṛṣi / devatā / chandas note, Sāyaṇa's introduction (reference M.S.0.P), then for each Ṛk the accented Saṃhitā, the accented
Pada (plain where the page has none) and Sāyaṇa's paragraphs on that Ṛk, each paragraph tagged with its reference M.S.R.P. M00 is Sāyaṇa's
Ṛgveda-bhāṣya-bhūmikā in four parts (R = printed page of the compilation edition). Devanagari only, as the index has it: nothing is corrected
(see docs/WIKISOURCE_NOTES.md); no transliteration or English. Regenerate after rebuilding the index: python3 tools/rv/ws_index.py build.
"""
import pathlib, sqlite3, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
DB = ROOT / 'refs' / 'wikisource' / 'index' / 'ws.sqlite'
OUT = ROOT / 'refs' / 'wikisource' / 'export'


def verse(t):
    return '  \n'.join(x.strip() for x in t.split('\n') if x.strip())


def main():
    if not DB.exists(): sys.exit('no index: run  python3 tools/rv/ws_index.py build')
    OUT.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(DB)
    total = 0
    for m in range(0, 11):
        L = [f'# ऋग्वेदः — मण्डल {m}' if m else '# सायणाचार्यकृता ऋग्वेदभाष्यभूमिका (वेदभाष्यभूमिकासङ्ग्रहः)', '',
             '*Text of sa.wikisource.org as indexed in this repository (refs/wikisource/index; see docs/WIKISOURCE_NOTES.md). '
             'Devanagari only; nothing corrected. References in square brackets: M.S.R.P = maṇḍala, sūkta, Ṛk, paragraph of Sāyaṇa (R = 0: his introduction to the sūkta).*', '']
        for s, rishi, note, layout in con.execute('select s, rishi, note, layout from sukta where m=? order by s', (m,)).fetchall():
            if m:
                L += [f'## सूक्तं {m}.{s}', '', f'*{rishi} · {note}*'.replace('  ', ' '), '']
            else:
                L += [f'## भाग {s}', '']
            ritems = {r: (a, p) for r, a, p in con.execute("select r, coalesce(nullif(samhita_acc,''), samhita), coalesce(nullif(pada_acc,''), pada) from rik where m=? and s=?", (m, s))}
            paras = {}
            for r, p, d in con.execute('select r, p, deva from para where m=? and s=? order by r, p', (m, s)):
                paras.setdefault(r, []).append((p, d))
            for r in sorted(set(ritems) | set(paras)):
                if m == 0:
                    L += [f'### पृष्ठम् {r}', '']
                elif r == 0:
                    L += ['### सायणभाष्योपक्रमः', '']
                else:
                    a, p = ritems.get(r, ('', ''))
                    L += [f'### ऋक् {m}.{s}.{r}', '']
                    if a: L += ['**संहिता**', '', verse(a), '']
                    if p: L += ['**पदपाठः**', '', verse(p), '']
                    if paras.get(r): L += ['**सायणभाष्यम्**', '']
                for p, d in paras.get(r, []):
                    L += [f'[{m}.{s}.{r}.{p}] {d.strip()}', '']
        (OUT / f'Rigveda_Devanagari_M{m:02d}.md').write_text('\n'.join(L) + '\n', encoding='utf-8')
        total += len(L)
        print(f'M{m:02d}: {len(L)} lines')
    print(f'written to {OUT.relative_to(ROOT)}: {sum(f.stat().st_size for f in OUT.glob("*.md")) / 1e6:.1f} MB')


if __name__ == '__main__':
    main()
