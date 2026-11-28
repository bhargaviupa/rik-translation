#!/usr/bin/env python3
"""Draft skeleton of the English edition's OWN preface (REQUIREMENTS A2 'Preface to the English edition', F15; PUBLICATION_TODO U6).

    python3 tools/rv/own_preface.py N [N...] [--force]

Writes volN/own_preface.json: facts of the volume taken from pubcfg.json and the English file (range, adhyāyas, number of sūktas,
printed pages), the fixed paragraph on the source edition, and slots `{{...}}` for what only the editor can say (themes of the
volume, why and for whom, thanks, signature).  `publish/volbook.py` sets it after the contents of the English book; a paragraph
that still holds a `{{slot}}` is shown as a placeholder (review copy), so no slot can reach a release by accident (see
`publish/pdf_check.py`).  An existing file is never overwritten without --force: the text is the editor's.
The paragraph on how the translation was made is only a pointer: the truthful account (including the AI assistant, H1.5) is
the 'Note on this translation' (H2.4), whose wording the user decides.
"""
import json, re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
ORD = {1:'first',2:'second',3:'third',4:'fourth',5:'fifth',6:'sixth',7:'seventh',8:'eighth',9:'ninth',10:'tenth'}

def facts(n):
    cfg = json.loads((ROOT / f'vol{n}/pubcfg.json').read_text())
    en = ROOT / cfg.get('english_md', f'vol{n}/Rigveda_Samhita_Vol{n}_English_Translation.md')
    txt = en.read_text(encoding='utf-8') if en.exists() else ''
    suk = len(re.findall(r'^## S[ūu]kta\b', txt, re.M))
    pm = re.findall(r'Done through printed p\.\s*(\d+)', txt)
    pages = int(pm[-1]) if pm else None
    return cfg, suk, pages

def draft(n):
    cfg, suk, pages = facts(n)
    rng = cfg.get('range_line', '{{range of the volume}}').replace('&amp;', '&')
    adh = cfg.get('adhyaya_line', '')
    p = []
    p.append(f"This volume holds {rng}" + (f" ({adh})" if adh else '') + '.'
             + (f" It runs to {suk} sūktas" if suk else '') + (f" on {pages} printed pages of the Kannada edition." if suk and pages else ('.' if suk else '')))
    p.append("{{Themes of the volume: the ṛṣis and families, the deities, the hymns the reader should not miss — two or three paragraphs, the editor's own.}}")
    p.append("The translation follows the Kannada edition of the Ṛgveda-saṃhitā with the Sāyaṇa-bhāṣya, edited and translated by Asthāna Mahāvidvān H. P. Venkata Rao "
             f"(Śrī Jayacāmarājendra Vedaratna-mālā, {cfg.get('year', '')}). What is reproduced from that edition, what is translated, "
             "and how the English was made are stated in the Note on this translation, which follows.")
    p.append("{{Why this English edition was made, and for whom: the editor's own reasons and the readers in mind.}}")
    p.append("{{Thanks: to the scholars, readers and families who made the work possible (wording to be decided; see REQUIREMENTS F8).}}")
    return {"vol": n, "title": "Preface to the English Edition", "paragraphs": p, "dateline": ["{{place and date}}"], "signature": ["{{signature}}"]}

if __name__ == '__main__':
    force = '--force' in sys.argv
    vols = [int(a) for a in sys.argv[1:] if a.isdigit()]
    if not vols: sys.exit(__doc__)
    for n in vols:
        out = ROOT / f'vol{n}/own_preface.json'
        if out.exists() and not force:
            print(f'vol{n}: {out.name} exists, kept (use --force to replace)'); continue
        try: d = draft(n)
        except FileNotFoundError: print(f'vol{n}: no pubcfg.json, skipped'); continue
        out.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8'); print(f'vol{n}: wrote {out}')
