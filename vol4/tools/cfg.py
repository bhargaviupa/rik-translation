"""Volume 4 pass: scan and paths.
Vol 4 has one scan, ../../Rig_Vol4.pdf (622 PDF pages; printed = PDF - 14); no better multi-part scan yet.
If one is supplied later, put the parts in vol4/scans/ and list them in PARTS (path, first global PDF page)."""
import os
VOL=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))   # the vol4/ folder
ROOT=os.path.dirname(VOL)                                         # repository root
PARTS=[  # (path, first global PDF page)
    ('Rig_Vol4.pdf',1),
]
LAST=622
EN=os.path.join(ROOT,'Rigveda_Samhita_Vol4_English_Translation.md')   # stays at the repository root (publish/build_vol45.py reads it there)
REVIEW=os.path.join(VOL,'review')
WORK=os.environ.get('V4WORK','/tmp/v4num/')
os.makedirs(WORK,exist_ok=True)
def part_of(g):
    """global PDF page -> (part path, page within part)"""
    for i,(p,first) in enumerate(PARTS):
        last=PARTS[i+1][1]-1 if i+1<len(PARTS) else LAST
        if first<=g<=last: return os.path.join(ROOT,p),g-first+1
    raise KeyError(g)
