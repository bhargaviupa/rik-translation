#!/usr/bin/env python3
"""Pilot: read scanned pages of a volume with the model's vision, as a stand-in for the machine-read text (shared tool; Vol 22 first).

  python3 tools/rv/scan_pilot.py plan VOL PDF FIRST LAST [--dpi 200] [--model claude-sonnet-5-5]
        renders PDF pages FIRST..LAST (PDF page numbers) to volN/work/scan_pilot/, counts the input tokens (free) and prints the cost estimate. Nothing is sent.
  python3 tools/rv/scan_pilot.py run VOL PDF FIRST LAST [--dpi 200] [--model ...] [--max-usd 3]
        sends each page (one request per page) and writes volN/work/scan_pilot/pages.md (page marks `<!-- PDF n -->`) and the usage to volN/parts/scan_pilot.md.
  python3 tools/rv/scan_pilot.py compare VOL REF.md
        compares volN/work/scan_pilot/pages.md with a machine-read text of the same pages (words, numerals, Kannada digits): a measured error rate.

The model transcribes, it does not translate: the Saṃhitā, Pada and Sāyaṇa-bhāṣya blocks are NOT read (they come from the Wikisource index); each is replaced by a
line `[[block: samhita|pada|bhashya]]`. Key: RIK_API_KEY (never printed). Scans are not committed (decision of Nov 12 2026)."""
import os, re, sys, json, base64, subprocess, glob, difflib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
PRICES = {'claude-sonnet-5-5': (2.0, 10.0), 'claude-opus-5-5': (4.0, 20.0), 'claude-haiku-5-5': (0.10, 0.50)}   # USD per MTok (input, output), list price Nov 2026: check before trusting
SYSTEM = """You transcribe one scanned page of a 1950s Kannada edition of the Ṛgveda (Sāyaṇa's Sanskrit commentary with a Kannada commentary). You do not translate.
Write the page as plain Markdown, in reading order, in Kannada script exactly as printed:
- First line: the running head exactly as printed (title and page number), as a line of its own.
- Headings (sūkta, Ṛk number, section labels such as ಪ್ರತಿಪದಾರ್ಥ, ಭಾವಾರ್ಥ, ವಿಶೇಷವಿಷಯಗಳು) as printed, one per line.
- The Sanskrit blocks under the labels ಸಂಹಿತಾಪಾಠಃ, ಪದಪಾಠಃ and ಸಾಯಣಭಾಷ್ಯಂ are NOT to be read: replace each block by one line `[[block: samhita]]`, `[[block: pada]]` or `[[block: bhashya]]`, keeping its label line before it. A Sanskrit quotation inside the Kannada commentary is transcribed as printed (Kannada script).
- Numbers and references (sūtra numbers such as ೬-೧-೧೬೩, verse numbers, page numbers) exactly as printed, in Kannada digits. Look-alike digits (೩/೫, ೬/೭, ೮/೯, ೨/೩/೭) must be read with care; where you cannot decide, write the digit you think is most likely and put [?] right after the number.
- A word or letter you cannot read: write [?] in its place. Never complete anything from memory, never correct what the print says, never skip a line; no remarks of your own.
- Footnotes and marginal notes: at the end, after a line `---`, each as printed.
Answer with the transcription only."""
def key():
    k = os.environ.get('RIK_API_KEY') or os.environ.get('ANTHROPIC_API_KEY'); assert k, 'set RIK_API_KEY'; return k
def args():
    a = sys.argv[1:]; kw = {'dpi': 200, 'model': 'claude-sonnet-5-5', 'max_usd': 3.0}; pos = []
    i = 0
    while i < len(a):
        if a[i] in ('--dpi', '--model', '--max-usd'): kw[a[i][2:].replace('-', '_')] = type(kw[a[i][2:].replace('-', '_')])(a[i + 1]); i += 2
        else: pos.append(a[i]); i += 1
    return pos, kw
def render(vol, pdf, first, last, dpi):
    """Each page is rendered at the width of its scan (the PDF page size of some scans is wrong, so -r is not used), cut at the emptiest line near the middle into a top and a
    bottom half, and each half is shrunk to 1568 px wide (the API shrinks anything larger, which would blur the small Kannada print). Returns [(page, [top.jpg, bottom.jpg])]."""
    import numpy as np
    from PIL import Image
    d = os.path.join(ROOT, f'vol{vol}', 'work', 'scan_pilot'); os.makedirs(d, exist_ok=True); out = []
    for pg in range(first, last + 1):
        base = os.path.join(d, f'full{pg:04d}')
        subprocess.run(['pdftoppm', '-f', str(pg), '-l', str(pg), '-scale-to-x', str(dpi * 10 if dpi > 300 else 2304), '-scale-to-y', '-1', '-gray', '-png', pdf, base], check=True)
        f = glob.glob(base + '*.png')[0]; im = Image.open(f).convert('L'); w, h = im.size
        ink = (np.asarray(im) < 128).sum(axis=1).astype(float); k = max(5, h // 230); sm = np.convolve(ink, np.ones(k) / k, mode='same')
        lo, hi = int(h * 0.42), int(h * 0.58); cut = lo + int(np.argmin(sm[lo:hi]))
        halves = []
        for name, box in (('a', (0, 0, w, cut)), ('b', (0, cut, w, h))):
            part = im.crop(box); part = part.resize((1568, max(1, round(part.size[1] * 1568 / part.size[0]))), Image.LANCZOS)
            fn = os.path.join(d, f'p-{pg:04d}{name}.jpg'); part.save(fn, quality=88); halves.append(fn)
        os.remove(f); out.append((pg, halves))
    return out
def content(halves):
    c = [{'type': 'text', 'text': 'The next two images are the TOP half and the BOTTOM half of ONE printed page (cut at an empty line between two lines of print). Transcribe the whole page once, top to bottom.'}]
    for f in halves: c.append({'type': 'image', 'source': {'type': 'base64', 'media_type': 'image/jpeg', 'data': base64.b64encode(open(f, 'rb').read()).decode()}})
    c.append({'type': 'text', 'text': 'Transcribe this page.'}); return c

def plan_or_run(mode, vol, pdf, first, last, kw):
    import anthropic
    c = anthropic.Anthropic(api_key=key()); files = render(vol, pdf, first, last, kw['dpi']); pin, pout = PRICES[kw['model']]
    n_in = 0
    for pg, hv in files:
        n_in += c.messages.count_tokens(model=kw['model'], system=SYSTEM, messages=[{'role': 'user', 'content': content(hv)}]).input_tokens
    est_out = 1800 * len(files)    # a guess: Kannada text is token-heavy; the run measures the real figure
    est = n_in * pin / 1e6 + est_out * pout / 1e6
    print(f'{len(files)} pages (two halves each): {n_in} input tokens (counted), about {est_out} output tokens (guess) → estimated ${est:.2f} (model {kw["model"]}, list price, no batch discount)')
    if mode == 'plan': return
    assert est <= kw['max_usd'], f'estimate ${est:.2f} is above --max-usd {kw["max_usd"]}'
    out = []; tin = tout = 0; d = os.path.dirname(files[0][1][0])
    for pg, hv in files:
        r = c.messages.create(model=kw['model'], max_tokens=6000, system=SYSTEM, messages=[{'role': 'user', 'content': content(hv)}])
        t = ''.join(b.text for b in r.content if b.type == 'text'); tin += r.usage.input_tokens; tout += r.usage.output_tokens
        out.append(f'<!-- PDF {pg} -->\n{t.strip()}\n'); print('page', pg, r.usage.input_tokens, r.usage.output_tokens, flush=True)
    open(os.path.join(d, 'pages.md'), 'w', encoding='utf8').write('\n'.join(out))
    cost = tin * pin / 1e6 + tout * pout / 1e6
    log = os.path.join(ROOT, f'vol{vol}', 'parts', 'scan_pilot.md'); os.makedirs(os.path.dirname(log), exist_ok=True)
    open(log, 'a', encoding='utf8').write(f'| PDF {first}–{last} | {kw["model"]} | {kw["dpi"]} dpi | in {tin} out {tout} | ${cost:.2f} |\n')
    print(f'done: {len(files)} pages, in {tin} out {tout}, cost ${cost:.2f} → vol{vol}/work/scan_pilot/pages.md')
KD = str.maketrans('೦೧೨೩೪೫೬೭೮೯', '0123456789')
def words(t): return re.findall(r'[^\s\[\]<>|()*#`>]+', re.sub(r'<!--.*?-->|\[\[block:[^\]]*\]\]', ' ', t))
def compare(vol, ref):
    pilot = open(os.path.join(ROOT, f'vol{vol}', 'work', 'scan_pilot', 'pages.md'), encoding='utf8').read(); R = open(ref, encoding='utf8').read()
    a, b = words(pilot), words(R); sm = difflib.SequenceMatcher(None, b, a, autojunk=False)
    same = sum(m.size for m in sm.get_matching_blocks()); na = [w for w in a if re.search('[೦-೯]', w)]; nb = [w for w in b if re.search('[೦-೯]', w)]
    sn = difflib.SequenceMatcher(None, nb, na, autojunk=False); samen = sum(m.size for m in sn.get_matching_blocks())
    print(f'words: pilot {len(a)}, reference {len(b)}, matched {same} ({100 * same / max(1, len(b)):.1f}% of the reference words); tokens with Kannada digits: reference {len(nb)}, matched {samen} ({100 * samen / max(1, len(nb)):.1f}%); `[?]` in the pilot: {pilot.count("[?]")}')
if __name__ == '__main__':
    pos, kw = args(); mode = pos[0]
    if mode == 'compare': compare(pos[1], pos[2])
    else: plan_or_run(mode, pos[1], pos[2], int(pos[3]), int(pos[4]), kw)
