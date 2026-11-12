#!/usr/bin/env python3
"""English front matter of a volume (board of scholars, list of abbreviations, contents) from the supplied machine-read text, by direct API requests.

  python3 tools/rv/api_frontmatter.py N --board FIRST LAST --abbr FIRST LAST --contents vol18/contents.json [--model claude-sonnet-5-5]

  --board FIRST LAST     md line numbers (1-based, inclusive) of the board-of-scholars page (after the title pages)
  --abbr  FIRST LAST     md line numbers of the list of abbreviations (heading line first)
  --contents FILE        the JSON written by publish/tools/frontmatter/contents_parse.py (blocks with `src`, `t`, `text`)
Writes volN/frontmatter_en.json (board, abbreviations, contents heading; same schema as vol15/frontmatter_en.json, no `preface`: the volume's own
preface is translated by api_front.py and stands in the English file) and volN/contents_en.json ([{src, en}]).  Three requests, about $0.2 in all.
Sanskrit words of the contents are copied from the source in Kannada script inside ⟦ ⟧ (publish/volbook.py turns them into IAST); no Devanagari or
Kannada script is typed by the model otherwise.  Key: RIK_API_KEY.  The result is a draft for the editor's reading: names and ordinals are checked by
script only for count and order."""
import sys, os, re, json, pathlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rvlib, api_batch
ROOT = rvlib.ROOT

def ask(cl, model, system, user, max_tokens=16000):
    with cl.messages.stream(model=model, max_tokens=max_tokens, system=system, messages=[{'role': 'user', 'content': user}]) as st:
        msg = st.get_final_message()
    if msg.stop_reason != 'end_turn': sys.exit(f'no usable answer (stop_reason {msg.stop_reason})')
    u = msg.usage; pi, po = api_batch.PRICES.get(model, (0, 0))
    text = ''.join(b.text for b in msg.content if b.type == 'text')
    m = re.search(r'```(?:json)?\s*(.*?)```', text, re.S)
    try: data = json.loads(m.group(1) if m else text)
    except Exception as e: sys.exit(f'answer is not JSON ({e}): {text[:300]}')
    return data, (u.input_tokens * pi + u.output_tokens * po) / 1e6

SYS = ("You translate the front matter of a Kannada edition of the Ṛgveda-saṃhitā with Sāyaṇa's commentary (Mysore, 1952) into English. "
       "Answer with ONE JSON value in a ```json block and nothing else. Write names of persons and works in English with IAST diacritics (Venkata Rao, "
       "Gaṅgādhara Śāstri, Āśvalāyana Śrauta-sūtra). Never write Kannada or Devanagari letters unless the task says to copy a quoted Sanskrit phrase inside ⟦ ⟧. "
       "Add no remarks of your own.")

def main():
    a = sys.argv[1:]; vol = int(a[0]); cfg = rvlib.Cfg(str(vol))
    opt = lambda k, n=1: a[a.index(k) + 1: a.index(k) + 1 + n] if k in a else None
    model = (opt('--model') or ['claude-sonnet-5-5'])[0]
    md = pathlib.Path(ROOT, cfg.source[0].split('@')[0]).read_text(encoding='utf8').split('\n')
    cl = api_batch.client(); total = 0.0; fe = {}
    b = opt('--board', 2)
    if b:
        txt = '\n'.join(l for l in md[int(b[0]) - 1:int(b[1])] if l.strip() and l.strip() != '---')
        d, c = ask(cl, model, SYS, 'This is the page of the board of Vedic scholars (the translator-editor first, then the assisting scholars, numbered; the text is machine-read and may '
                   'have small slips). Return {"title_lines": [3 or fewer lines of the board\'s title], "editor_label": "Translator & Editor:", "editor": "…", "list_title": "…", '
                   '"members": ["1. …"] } (one string per scholar: name, then office and place; keep the numbering out of the strings; transliterate the Kannada titles "ಬ್ರ|| ಶ್ರೀ||" as Brahmaśrī).\n\n' + txt)
        fe['board'] = d; total += c
    b = opt('--abbr', 2)
    if b:
        txt = '\n'.join(l for l in md[int(b[0]) - 1:int(b[1])] if l.strip() and l.strip() != '---')
        d, c = ask(cl, model, SYS, 'This is the printed list of abbreviations ("abbreviation—work"). Return {"title": "Explanation of the abbreviations", "intro": "The printed abbreviation, the form used in this translation, and the work.", '
                   '"rows": [[printed abbreviation exactly as in the text, standard Latin form (e.g. "Ṛ. Saṃ."), English name of the work], …], "note": ""} in the order of the text. '
                   'The text is machine-read: if a printed abbreviation is plainly a misreading of a standard one, keep it as printed in the first column and put the standard form in the second.\n\n' + txt)
        fe['abbreviations'] = d; total += c
    f = opt('--contents')
    if f:
        blocks = json.loads(pathlib.Path(ROOT, f[0]).read_text(encoding='utf8'))
        items = [{'src': x['src'], 't': x['t'], 'text': x['text'], **({'no': x['no']} if 'no' in x else {})} for x in blocks]
        out = []
        for i in range(0, len(items), 70):
            chunk = items[i:i + 70]
            d, c = ask(cl, model, SYS,
                       'These are entries of the printed contents (ವಿಷಯಾನುಕ್ರಮಣಿಕೆ) of the volume, in order; t = "center" (a heading), "mandala", "sukta" (a sūkta heading: its Kannada number is in `no`) or "item". '
                       'Return a JSON list [{"src": <same src>, "en": "<English>"}] with one entry per input entry, same order. A sūkta heading becomes "N. The Nth sūkta, beginning ⟦words⟧" '
                       '(N in Arabic figures, the ordinal in words; the opening words of the sūkta are copied from the text in Kannada script inside ⟦ ⟧, exactly, never retyped). Other Sanskrit words quoted in an item are also copied inside ⟦ ⟧. '
                       'Add "note": "…" to an entry only if the Kannada text itself is garbled or an ordinal disagrees with the number.\n\n' + json.dumps(chunk, ensure_ascii=False))
            total += c; out += d
        if [x['src'] for x in out] != [x['src'] for x in items]: sys.exit('the contents answer does not match the input (src order/count)')
        pathlib.Path(ROOT, f'vol{vol}', 'contents_en.json').write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf8')
        fe['contents'] = {'heading': ['॥ Śrīḥ ॥', f'Contents of the {cfg.d.get("vol_ordinal", str(vol) + "th")} Volume of the Ṛgveda-saṃhitā'], 'page_note': 'Page numbers are the pages of this book.'}
    fe['_doc'] = 'English front matter of the volume (api_frontmatter.py; a draft for the editor). Strings may contain {{fn: text}} = a footnote. Read by publish/volbook.py (English PDF).'
    p = pathlib.Path(ROOT, f'vol{vol}', 'frontmatter_en.json')
    old = json.loads(p.read_text(encoding='utf8')) if p.exists() else {}
    old.update(fe); p.write_text(json.dumps(old, ensure_ascii=False, indent=1), encoding='utf8')
    cost = os.path.join(ROOT, f'vol{vol}', 'parts', 'batch_costs.md')
    open(cost, 'a', encoding='utf8').write(f'| front matter (board, abbreviations, contents) | {model} direct | {sum(k in fe for k in ("board", "abbreviations", "contents"))} requests | | ${total:.3f} |\n')
    print(f'written vol{vol}/frontmatter_en.json (+ contents_en.json); cost ${total:.3f}')

if __name__ == '__main__':
    if len(sys.argv) < 3: sys.exit(__doc__)
    main()
