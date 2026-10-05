#!/usr/bin/env python3
"""Clean the Volume 1 working draft for publication.  Reads the closed .md, writes
work/vol1_clean.md and an audit log work/vol1_audit.md listing everything removed/converted."""
import re, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "Rigveda_Samhita_Vol1_English_Translation.md"
OUT = pathlib.Path(__file__).resolve().parent / "work"
OUT.mkdir(exist_ok=True)

CHAPTER_H2 = re.compile(r'^## (Chapter |Purva-peethike|Preface|Table of Contents|Sayana\'s Bhashya-bhumika|Sayana\'s Commentary with|Title Page)')

GAPS = ROOT / "Rigveda_Samhita_Vol1_Gaps_English_Translation.md"
NUMW = {'6': 'Six', '7': 'Seven', '8': 'Eight'}
GAP_B_NOTICE = ('<div class="edition-note">\n\n**Editorial notice.** The source prints this alphabetical index of the Ṛgveda’s ṛṣis with, '
    'for every entry, the hymn references (maṇḍala–sūkta–ṛc, in Kannada numerals) and, in square brackets, the total number of verses seen by that ṛṣi. '
    'In this edition the names, descriptions and bracketed verse-counts are given in full; the hymn references are not reproduced, because at the scan quality '
    'available they could not be read with the certainty that a reference table requires. The cross-reference lines, printed in mirrored pairs (“A B … B A”), '
    'are compressed: each ṛṣi is listed once, with the ṛṣis paired with him or her.\n\n</div>')

def load_gap(letter):
    """Blocks of one gap section of the supplementary translation, normalised for the Volume 1 build."""
    txt = GAPS.read_text(encoding='utf-8')
    txt = re.sub(r'(?<!\n)\n(?=#{1,6} )', '\n\n', txt)
    m = re.search(r'(?m)^# GAP ' + letter + r' — .*$', txt)
    nxt = re.search(r'(?m)^# GAP [A-D] — .*$', txt[m.end():])
    sec = txt[m.end(): m.end() + nxt.start()] if nxt else txt[m.end():]
    blocks = [b.strip('\n') for b in re.split(r'\n\s*\n', sec) if b.strip()]
    res, skipping = [], False
    for b in blocks:
        first = b.split('\n', 1)[0]
        if b.strip() == '---' or first.startswith('**Progress note'):
            continue
        if first.startswith('[End of printed p. 167') or first.startswith('(the page ends here; the earlier draft resumes') or first.startswith('[End of printed p.'):
            continue
        if letter == 'B' and first.startswith('# Chapter Eleven'):
            break                                   # the draft already carries Chapter Eleven from p. 205
        if letter == 'B' and first.startswith('**Editorial note on this section'):
            res.append(GAP_B_NOTICE); skipping = True; continue
        if skipping:
            if first.startswith('### Page'): skipping = False
            else: continue
        mp = re.match(r'^### Page (\d+)(?: — (.*))?$', first)
        if mp:
            res.append(f'<div class="pgmark">original p. {mp.group(1)}</div>')
            if mp.group(2): res.append('### ' + mp.group(2).strip())
            rest = b.split('\n', 1)[1] if '\n' in b else ''
            if rest.strip(): res.append(rest)
            continue
        mc = re.match(r'^#{1,2} Chapter (\d+|\w+) — (.*)$', first)
        if mc:
            num = NUMW.get(mc.group(1), mc.group(1))
            h = f'## Chapter {num} — {mc.group(2)}'
            k = len(res)
            while k > 0 and (res[k - 1].startswith('<div class="pgmark">') or re.match(r'^\*\*[\u0C80-\u0CFF]', res[k - 1])):
                k -= 1                                # chapter heading before the page mark / Kannada title line that open it
            res.insert(k, h)
            continue
        if first.startswith('### ') and not first.startswith('####'):
            b = '#' + b                              # ### -> ####
        elif first.startswith('## '):
            b = '#' + b                              # ## -> ###
        res.append(b)
    return res

audit = []
def log(kind, lineno, text):
    audit.append(f"- **{kind}** (draft line {lineno}): {text[:220].replace(chr(10), ' ')}{'…' if len(text) > 220 else ''}")

def clean():
    text = SRC.read_text(encoding='utf-8')
    text = re.sub(r'(?<!\n)\n(?=#{1,6} )', '\n\n', text)
    text = re.sub(r'(?m)^(#{1,6} .*)\n(?!\n)', r'\1\n\n', text)   # and a blank line after
    lines = text.split('\n')
    # blocks with their starting line numbers
    blocks, cur, start = [], [], 1
    for i, l in enumerate(lines, 1):
        if l.strip() == '':
            if cur: blocks.append((start, '\n'.join(cur))); cur = []
        else:
            if not cur: start = i
            cur.append(l)
    if cur: blocks.append((start, '\n'.join(cur)))

    out, skip_section, skip_rishi = [], False, False
    seen_preface = False
    for ln, blk in blocks:
        first = blk.split('\n', 1)[0]
        # 0. everything before the Preface is draft header / image notes
        if not seen_preface:
            if first.startswith('## Preface'):
                seen_preface = True
            else:
                log('removed (draft header / front-matter description)', ln, blk); continue
        if first.startswith("## Page 191 — The Rigveda's Rishis"):
            skip_rishi = True; log('removed (draft sample of the rishi index; replaced by the full index)', ln, first); continue
        if skip_rishi and not first.startswith('> **⚠'):
            log('removed (draft sample of the rishi index)', ln, blk); continue
        # 1. whole sections that are working messages
        if first.startswith('## ') and re.search(r'🎉|✅', first):
            skip_section = True; log('removed section (working milestone)', ln, first); continue
        if skip_section:
            if first.startswith('# ') or first.startswith('## ') and not re.search(r'🎉|✅', first):
                skip_section = False
            else:
                log('removed (inside milestone section)', ln, blk); continue
        if blk.strip() == '---':
            continue
        # 2. progress / milestone paragraphs
        if re.match(r'\*\*(Progress|🎉|Target for next session|Recommendation for future sessions|PDF page 622|⚠ IMPORTANT STRUCTURAL FLAG)', first):
            log('removed (progress / working flag)', ln, blk); continue
        if first.startswith('*(This marks the completion of the entire Rigveda-Bhashya-Bhumika'):
            log('removed (working note)', ln, blk); continue
        if re.match(r'\*\*(Pacing note|The genuine highlight of this batch|Also completed this batch|This batch (is different|completed|established))', first) or first.startswith('*This page continues Sāyaṇa'):
            body = blk.replace('\n', ' ').replace('This batch', 'This section').replace('this batch', 'this section').replace("this batch's", "this section's")
            out.append('*(' + body.strip('*') + ')*'); log('converted to note (session summary)', ln, blk); continue
        if re.match(r'\*\*(Honesty note|What made this)', first):
            out.append('*(' + blk.replace('\n', ' ') + ')*'); log('converted to note (session remark)', ln, blk); continue
        if re.match(r'^\*\((To be continued|No outstanding issues flagged|Known reading issues|paragraph continues onto the next page|No separately boxed|This page.s Kannada prose has been rendered in full above; no separately boxed)', blk):
            log('removed (working marker)', ln, blk); continue
        # 2b. explicit rewording of scan-duplication notes (no scan-file coordinates in the book)
        dup = re.match(r'^\*\(PDF pages? (\d+)(?:–(\d+))? (?:are exact-content duplicates of|largely re-scan|re-scans?) ', blk)
        if dup:
            pp = re.search(r'printed pages? ([\d–]+)', blk).group(1)
            res = re.search(r'resumes below at PDF page \d+ \(printed page (\d+)\)', blk).group(1)
            new = f'*(The source scan repeats printed page{"s" if "–" in pp else ""} {pp}, already translated above; the duplicate{"s" if "–" in pp else ""} {"are" if "–" in pp else "is"} not translated again. The translation resumes at printed page {res}.)*'
            log('reworded (scan duplication)', ln, blk); out.append(new); continue
        if first.startswith('*("ಸಾಯಣಭಾಷ್ಯಸಹಿತ'):
            blk = re.sub(r' Begins PDF page \d+ / printed page \d+ of the source\.', '', blk)
        # 3. blockquote notes
        if first.startswith('> **✅'):
            body = re.sub(r'^> ?', '', blk, flags=re.M); body = re.sub(r'^\*\*✅ Gap filled:\*\*\s*', '', body)
            out.append('*(' + body.replace('\n', ' ') + ')*'); log('converted to note (gap filled)', ln, body); continue
        if first.startswith('> **⚠'):
            body = re.sub(r'^> ?', '', blk, flags=re.M)
            gk = ('A' if 'printed page 94' in first else 'C' if 'printed page 260' in first else 'D' if 'printed page 287' in first else 'B' if 'alphabetical rishi-index' in first else None)
            if gk:
                gb = load_gap(gk); out.extend(gb); log(f'inserted translation of omitted portion (Gap {gk})', ln, f'{len(gb)} blocks from the supplementary translation'); skip_rishi = False; continue
            if 'deliberate skip' in first or 'alphabetical rishi-index' in first:
                body = re.sub(r'^\*\*⚠ Note on a deliberate skip:\*\*', '**Editorial notice — omitted portion.**', body)
                body = re.sub(r'^\*\*⚠ Note on the alphabetical rishi-index[^*]*\*\*', '**Editorial notice — omitted portion.** The alphabetical index of rishis (printed pages 191–205 of the original)', body)
                body = body.replace("At the user's request, translation now jumps", 'In this edition the translation passes').replace("At the user's request, translation jumps", 'In this edition the translation passes')
                body = body.replace("At the user's request, this", 'In this edition this')
                body = re.sub(r'PDF pages? \d+(?:–\d+)? \((printed pages? [\d–]+)([^)]*)\)', r'\1\2', body)
                body = body.replace('****', '**')
                out.append('<div class="edition-note">\n\n' + body + '\n\n</div>'); log('converted to editorial notice', ln, body); continue
            if 'Known issues' in first:
                log('removed (draft QA log: known issues)', ln, body); continue
            body = re.sub(r'^\*\*⚠ Note on[^*]*:\*\*\s*', '', body)
            out.append('*(' + body.replace('\n', ' ') + ')*'); log('converted to note (scan/sequence note)', ln, body); continue
        # 4. bracketed image descriptions / preface reading note -> notes
        if re.match(r'^\*\[.*\]\*$', blk, flags=re.S):
            out.append('*(' + blk[2:-2] + ')*'); log('converted to note (image description)', ln, blk); continue
        if re.match(r'^\*Note: This is a careful first-pass', blk):
            out.append('*(' + blk.strip('*') + ')*'); log('converted to note (reading note)', ln, blk); continue
        # 5. page headings -> markers
        m = re.match(r'^#{2,3} \[?Page ([0-9ivxlc]+)\]?(?: — (.*))?$', first)
        if m:
            pg, title = m.group(1), m.group(2)
            out.append(f'<div class="pgmark">original p. {pg}</div>')
            if title: out.append(('### ' + title))
            rest = blk.split('\n', 1)[1] if '\n' in blk else ''
            if rest.strip(): out.append(rest)
            continue
        ren = [(r'^## Chapter Fourteen — Commentators on the Atharvaveda', '## Chapter Sixteen — Commentators on the Atharvaveda'),
               (r'^## Chapter \[Fifteen\?\] — Authors of the Padapatha', '## Chapter Seventeen — Authors of the Padapatha'),
               (r'^## Chapter Seventeen — Ancient Efforts', '## Chapter Eighteen — Ancient Efforts'),
               (r'^## Chapter Eighteen — Modern Efforts', '## Chapter Nineteen — Modern Efforts'),
               (r'^## Chapter \[Nineteen\] — The Method', '## Chapter Twenty — The Method')]
        for pat, rep in ren:
            if re.match(pat, first):
                blk = re.sub(pat, rep, blk, count=1); log('renumbered chapter to match the original contents table', ln, first); break
        if blk.startswith('*(The chapter number on this page is not fully legible'):
            log('removed (chapter-number caution; resolved by the contents table)', ln, blk); continue
        # 6. heading levels: only genuine chapter headings stay level 2
        if first.startswith('## ') and not CHAPTER_H2.match(first):
            blk = '### ' + blk[3:]
        # 7. chapter titles with uncertain numerals
        blk = re.sub(r'^## Chapter \[([\w-]+)\??\] — ', lambda m: f'## Chapter {m.group(1)} — ', blk)
        blk = re.sub(r'^## Preface .*$', '## Preface (ಮುನ್ನುಡಿ)', blk, flags=re.M)
        out.append(blk)
    SUBS = [("reproduced here in full as it appears, per the user's explicit request to retain both the Sanskrit and this English rendering together", "reproduced here in full as it appears in the source, together with the Sanskrit"),
            ("**The debate reaches its genuine resolution in this batch.**", "**The debate reaches its genuine resolution here.**"),
            ("(see previous session's notes for the earlier stages)", "(see the earlier stages above)"),
            ("**This closes out what has been, across several sessions, a substantial introductory apparatus for Sukta 2**", "**This closes what has been a substantial introductory apparatus for Sukta 2**")]
    for k, b0 in enumerate(out):
        for a, z in SUBS:
            if a in b0:
                out[k] = b0 = b0.replace(a, z); log('reworded (working-session phrase)', 0, a)
    # 7b. structure: Part markers, merged chapter titles, Sūkta headings
    fixed = []
    i = 0
    while i < len(out):
        b = out[i]
        if re.match(r'^## Chapter \w+$', b) and i + 1 < len(out) and out[i + 1].startswith('### '):
            fixed.append(b + ' — ' + out[i + 1][4:].strip()); i += 2; continue
        if b.startswith('## Purva-peethike (Introduction)'):
            fixed.append('# PART I: Pūrva-pīṭhikā — the Introduction'); fixed.append('## Introduction (Pūrva-pīṭhikā)'); i += 1; continue
        if b.startswith('### The First Mantra of the Rigveda'):
            fixed.append('## The First Sūkta (Ṛgveda 1.1) — agnim īḷe purohitam'); fixed.append(b); i += 1; continue
        if b.startswith('# ॥ द्वितीयं सूक्तम् ॥') and i + 1 < len(out) and out[i + 1].startswith('### The Second'):
            fixed.append('## The Second Sūkta (Ṛgveda 1.2) — vāyav ā yāhi'); i += 2; continue
        dup = re.match(r'^\*\(PDF pages? \d+', b)
        if dup:
            pp = re.search(r'printed pages? ([\d–]+)', b).group(1)
            res = re.search(r'resumes below at PDF page \d+ \(printed page (\d+)\)', b).group(1)
            pl = '–' in pp
            new = f'*(The source scan repeats printed page{"s" if pl else ""} {pp}, already translated above; the duplicate{"s" if pl else ""} {"are" if pl else "is"} not translated again. The translation resumes at printed page {res}.)*'
            log('reworded (scan duplication)', 0, b); fixed.append(new); i += 1; continue
        fixed.append(b); i += 1
    out = fixed
    # 8. the unfinished mantra index is dropped and replaced by a notice
    cut = next((i for i, b in enumerate(out) if b.startswith('# ॥ ऋग्वेदमन्त्राणां')), None)
    if cut is not None:
        for b in out[cut:]: log('removed (unfinished mantra index appendix)', 0, b)
        out = out[:cut]
        out.append('<div class="edition-note">\n\n**Editorial notice — omitted portion.** The original volume ends with a long alphabetical index of the mantras of the Rigveda (Varṇānukrama-sūcī). It has not been translated or reproduced in this edition.\n\n</div>')
    md = '\n\n'.join(out) + '\n'
    (OUT / 'vol1_clean.md').write_text(md, encoding='utf-8')
    (OUT / 'vol1_audit.md').write_text('# Volume 1 cleaning audit\n\n' + '\n'.join(audit) + '\n', encoding='utf-8')
    print(len(blocks), 'blocks in;', len(out), 'out;', len(audit), 'audit entries')

if __name__ == '__main__':
    clean()
