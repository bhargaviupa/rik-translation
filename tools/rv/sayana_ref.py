#!/usr/bin/env python3
"""Reference text of Sāyaṇa's bhāṣya for one sūkta, from vishvasa.github.io, to settle misread words.

    python3 tools/rv/sayana_ref.py M S          # e.g. 1 138: every Sāyaṇa block of the sūkta, in order
    python3 tools/rv/sayana_ref.py M S N        # only block N (0 = the introduction when the page has one)

Prints ONLY the sections headed सायण-भाष्यम् (the page also carries other people's translations, which the
translator must not see or use). It is another edition: spelling, sandhi and nasals differ from the
supplied text, and it may differ in wording. It serves to identify what a damaged passage of the supplied
text was meant to say; the supplied text stays the base (CLAUDE.md rule 2). Words in **…** on the page are
the words of the Ṛk; the marks are dropped here. The page is kept in /tmp for the session.
"""
import html, pathlib, re, subprocess, sys

URL = 'https://vishvasa.github.io/vedAH_Rk/shAkalam/saMhitA/sarva-prastutiH/{m:02d}/{s:03d}/'


def blocks(m, s):
    cache = pathlib.Path(f'/tmp/sayana_ref/{m:02d}_{s:03d}.html')
    if not cache.exists() or cache.stat().st_size < 2000:
        cache.parent.mkdir(parents=True, exist_ok=True)
        r = subprocess.run(['curl', '-sS', '-L', '-m', '60', '-o', str(cache), '-w', '%{http_code}', URL.format(m=m, s=s)],
                           capture_output=True, text=True)
        if r.stdout.strip() != '200':
            cache.unlink(missing_ok=True)
            sys.exit(f'could not open the reference page ({r.stdout.strip() or r.stderr.strip()}): {URL.format(m=m, s=s)}')
    t = cache.read_text(encoding='utf-8')
    t = t[t.find('<body'):]
    out = []
    for mm in re.finditer(r'<details[^>]*>\s*<summary>\s*सायण-भाष्यम्\s*</summary>(.*?)</details>', t, flags=re.S):
        x = re.split(r'<hr\s*/?>', mm.group(1))[0]      # after a rule the page adds his comment on the same mantra in another Veda
        x = re.sub(r'<br\s*/?>|</p>', '\n', x)
        x = html.unescape(re.sub(r'<[^>]+>', '', x))
        out.append(re.sub(r'[ \t]+', ' ', re.sub(r'\n\s*\n+', '\n', x)).strip())
    return out


def main():
    if len(sys.argv) < 3: sys.exit(__doc__)
    m, s = int(sys.argv[1]), int(sys.argv[2])
    bl = blocks(m, s)
    if not bl: sys.exit('no सायण-भाष्यम् section on the page')
    print(f'# Sāyaṇa, reference text, {m}.{s}: {len(bl)} blocks (source: {URL.format(m=m, s=s)})')
    print('# If the count is the number of Ṛks + 1, block 0 is the introduction and block N belongs to Ṛk N;')
    print('# if it equals the number of Ṛks, block 0 belongs to Ṛk 1. Match by the opening words to be sure.\n')
    want = int(sys.argv[3]) if len(sys.argv) > 3 else None
    for i, b in enumerate(bl):
        if want is None or want == i: print(f'## block {i}\n{b}\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())
