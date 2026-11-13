"""Shared pieces of the `rv` tool (docs/DESIGN.md).  New code beside the old pipeline (tools/rv/, publish/): nothing here writes to a
volume's existing files; everything it makes goes to volN/data/ and volN/review/."""
import os, re, sys, json, importlib.util
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'publish', 'tools', 'translit'))
sys.path.insert(0, os.path.join(ROOT, 'publish', 'tools', 'accents'))
from kannada_to_deva import kn2deva            # noqa: E402
from add_iast import deva_to_iast              # noqa: E402
from deva_to_kannada import deva2kn            # noqa: E402
import accents                                 # noqa: E402

KD = str.maketrans('೦೧೨೩೪೫೬೭೮೯', '0123456789')
DD = str.maketrans('0123456789', '०१२३४५६७८९')
KN = re.compile('[ಀ-೿]')
DEVA = re.compile('[ऀ-ॿ]')
canon = accents.canon                          # letters only, accents off, class nasal ~ anusvāra: for comparing two readings of a verse
strip_ac = accents.strip_ac

def habit(s):
    """canon() and, beyond it, the spelling habits in which the Kannada edition and the reference differ without a different reading:
    final m / anusvāra, avagraha, a doubled consonant, visarga before a sibilant."""
    s = canon(s).replace('ऽ', '').replace('\u200c', '').replace('\u200d', '')
    s = re.sub('म्$', 'ं', s); s = re.sub('म्(?=[क-ह])', 'ं', s)
    s = re.sub('ः(?=[शषस])', '', re.sub('([शषस])्(?=\\1)', '', s))
    return re.sub('([क-ह])्\\1', '\\1', s)

def vol_paths(vol):
    d = os.path.join(ROOT, f'vol{vol}')
    return dict(dir=d, kn=os.path.join(d, f'Rigveda_Samhita_Vol{vol}_Kannada_Text.md'), en=os.path.join(d, f'Rigveda_Samhita_Vol{vol}_English_Translation.md'),
                data=os.path.join(d, 'data'), review=os.path.join(d, 'review'), notes=os.path.join(d, 'review', 'notes.tsv'))

def read_reference(mandalas):
    """{(m, s, r): [accented Devanagari lines]} from refs/mandala (the accented Saṃhitā; requirement B1.2)."""
    spec = importlib.util.spec_from_file_location('accent_volume', os.path.join(ROOT, 'publish', 'tools', 'accents', 'accent_volume.py'))
    av = importlib.util.module_from_spec(spec); argv = sys.argv; sys.argv = ['accent_volume']
    try: spec.loader.exec_module(av)
    finally: sys.argv = argv
    out = {}
    for m in mandalas:
        for rid, line in av.read_ref(os.path.join(ROOT, 'refs', 'mandala', f'rv_mandala{m}.html')): out.setdefault(rid, []).append(line)
    return out

def unit_id(vol, u):
    if u.get('s') is None: return f"{vol}.front.{u['kind']}"
    return f"{vol}.{u['m']}.{u['s']:03d}." + (f"{u['rk']:02d}." if u.get('rk') else '00.') + u['kind']

def load_units(vol):
    p = os.path.join(vol_paths(vol)['data'], 'units.jsonl')
    return [json.loads(l) for l in open(p, encoding='utf8') if l.strip()]

def save_units(vol, units):
    d = vol_paths(vol)['data']; os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, 'units.jsonl'), 'w', encoding='utf8') as f:
        for u in units: f.write(json.dumps(u, ensure_ascii=False) + '\n')
