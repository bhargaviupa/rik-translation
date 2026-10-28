"""Volume 4 pass: scan parts and paths.
Better scan: vol4/scans/04 RigvedaSamhithaVolume04 1..7.pdf = 701 PDF pages (part 1 has 101, the others 100). The existing text was written from the old scan ../../Rig_Vol4.pdf (622 pages, printed = PDF - 14).
The page map of the better scan is checked with pnum.py (see vol4_state.md) and recorded in pages.py."""
import os
VOL=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))   # the vol4/ folder
ROOT=os.path.dirname(VOL)                                         # repository root
PARTS=[  # (path, first global PDF page); better scan in 7 parts (101+6x100 = 701 pages)
    ('vol4/scans/04 RigvedaSamhithaVolume04 1.pdf',1),
    ('vol4/scans/04 RigvedaSamhithaVolume04 2.pdf',102),
    ('vol4/scans/04 RigvedaSamhithaVolume04 3.pdf',202),
    ('vol4/scans/04 RigvedaSamhithaVolume04 4.pdf',302),
    ('vol4/scans/04 RigvedaSamhithaVolume04 5.pdf',402),
    ('vol4/scans/04 RigvedaSamhithaVolume04 6.pdf',502),
    ('vol4/scans/04 RigvedaSamhithaVolume04 7.pdf',602),
]
LAST=701
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
