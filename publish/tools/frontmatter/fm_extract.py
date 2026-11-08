#!/usr/bin/env python3
"""Turn a user-supplied front-matter PDF (cover, title page, portraits, board, preface, contents ...) into page images
for the print builds.

  python3 publish/tools/frontmatter/fm_extract.py UPLOAD.pdf --vol 15 [--dpi 130] [--roles cover,title,portrait,permission,board,preface1,preface2,contents1,...]

Writes publish/assets/volN/fm_01.jpg ... (grayscale JPEG, trimmed of white margins) and publish/assets/volN/frontmatter.json:
  {"pages": [{"n": 1, "file": "fm_01.jpg", "role": "cover", "w": ..., "h": ...}, ...]}
Roles are free labels (they are only read by publish/volbook.py through volN/pubcfg.json); without --roles they are 'pN'.
"""
import argparse, json, pathlib, subprocess, sys, tempfile
from PIL import Image, ImageChops

def trim(im, pad=12):
    g = im.convert('L')
    bbox = ImageChops.invert(g).point(lambda v: 255 if v > 40 else 0).getbbox()
    if not bbox: return im
    x0, y0, x1, y1 = bbox
    return im.crop((max(0, x0 - pad), max(0, y0 - pad), min(im.width, x1 + pad), min(im.height, y1 + pad)))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('pdf'); ap.add_argument('--vol', type=int, required=True)
    ap.add_argument('--dpi', type=int, default=130); ap.add_argument('--roles', default='')
    ap.add_argument('--no-trim', action='store_true')
    a = ap.parse_args()
    root = pathlib.Path(__file__).resolve().parents[3]
    out = root / 'publish' / 'assets' / f'vol{a.vol}'; out.mkdir(parents=True, exist_ok=True)
    roles = [r for r in a.roles.split(',') if r]
    with tempfile.TemporaryDirectory() as td:
        subprocess.run(['pdftoppm', '-r', str(a.dpi), '-gray', '-png', a.pdf, f'{td}/p'], check=True)
        files = sorted(pathlib.Path(td).glob('p-*.png'))
        pages = []
        for i, f in enumerate(files, 1):
            im = Image.open(f)
            if not a.no_trim: im = trim(im)
            name = f'fm_{i:02d}.jpg'
            im.convert('L').save(out / name, quality=88)
            pages.append({'n': i, 'file': name, 'role': roles[i - 1] if i <= len(roles) else f'p{i}', 'w': im.width, 'h': im.height})
    (out / 'frontmatter.json').write_text(json.dumps({'source': pathlib.Path(a.pdf).name, 'pages': pages}, indent=1, ensure_ascii=False), encoding='utf8')
    print(f'{len(pages)} pages -> {out.relative_to(root)}')
    for p in pages: print(p['n'], p['role'], p['file'], p['w'], 'x', p['h'])

if __name__ == '__main__':
    main()
