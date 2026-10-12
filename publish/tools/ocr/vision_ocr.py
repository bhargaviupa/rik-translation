#!/usr/bin/env python3
"""OCR page images with Google Cloud Vision (document text detection).

Usage:
  export VISION_API_KEY=...            # an API key restricted to the Cloud Vision API
  python3 vision_ocr.py INPUT_DIR OUT_DIR [--hints kn,hi]

INPUT_DIR holds .jpg/.png page images (e.g. made with:
  pdftoppm -gray -r 300 -jpeg -jpegopt quality=85 -f 30 -l 33 Rig_Vol8_alt.pdf pages/p )
For each image writes OUT_DIR/<name>.txt (plain text) and OUT_DIR/<name>.json (full response,
with per-symbol confidences, useful for checking digits). Needs: pip install requests
Cost: first 1,000 pages/month free, then about US$1.50 per 1,000 pages.
"""
import base64, json, os, sys, time, glob
import requests

def main():
    if len(sys.argv) < 3: sys.exit(__doc__)
    src, out = sys.argv[1], sys.argv[2]
    hints = ['kn', 'hi']
    if '--hints' in sys.argv: hints = sys.argv[sys.argv.index('--hints')+1].split(',')
    key = os.environ.get('VISION_API_KEY') or sys.exit('set VISION_API_KEY')
    os.makedirs(out, exist_ok=True)
    files = sorted(glob.glob(os.path.join(src, '*.jpg')) + glob.glob(os.path.join(src, '*.png')))
    url = 'https://vision.googleapis.com/v1/images:annotate?key=' + key
    for f in files:
        base = os.path.splitext(os.path.basename(f))[0]
        if os.path.exists(os.path.join(out, base + '.txt')): continue
        body = {'requests': [{'image': {'content': base64.b64encode(open(f, 'rb').read()).decode()},
                              'features': [{'type': 'DOCUMENT_TEXT_DETECTION'}],
                              'imageContext': {'languageHints': hints}}]}
        for attempt in range(4):
            r = requests.post(url, json=body, timeout=120)
            if r.status_code == 200: break
            time.sleep(2 ** attempt)
        else:
            print('FAILED', f, r.status_code, r.text[:200]); continue
        resp = r.json()['responses'][0]
        text = resp.get('fullTextAnnotation', {}).get('text', '')
        open(os.path.join(out, base + '.txt'), 'w', encoding='utf-8').write(text)
        json.dump(resp, open(os.path.join(out, base + '.json'), 'w', encoding='utf-8'), ensure_ascii=False)
        print('ok', base, len(text))

if __name__ == '__main__':
    main()
