"""Volume 3 pass: scan parts of the better scan and paths.
Global PDF page = page number in the user's full scan (7 parts, 660 pages); each part holds a run of it."""
import os
VOL=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))   # the vol3/ folder
ROOT=os.path.dirname(VOL)                                         # repository root
PARTS=[  # (path, first global PDF page)
    ('vol3/scans/03 Rigveda Samhitha Volume 03 1.pdf',1),
    ('vol3/scans/03 Rigveda Samhitha Volume 03 2.pdf',101),
    ('vol3/scans/03 Rigveda Samhitha Volume 03 3.pdf',201),
    ('vol3/scans/03 Rigveda Samhitha Volume 03 4.pdf',301),
    ('vol3/scans/03 Rigveda Samhitha Volume 03 5.pdf',401),
    ('vol3/scans/03 Rigveda Samhitha Volume 03 6.pdf',501),
    ('vol3/scans/03 Rigveda Samhitha Volume 03 7.pdf',581),
]
LAST=660
EN=os.path.join(VOL,'Rigveda_Samhita_Vol3_English_Translation.md')
REVIEW=os.path.join(VOL,'review')
WORK=os.environ.get('V3WORK','/tmp/v3num/')
os.makedirs(WORK,exist_ok=True)
def part_of(g):
    """global PDF page -> (part path, page within part)"""
    for i,(p,first) in enumerate(PARTS):
        last=PARTS[i+1][1]-1 if i+1<len(PARTS) else LAST
        if first<=g<=last: return os.path.join(ROOT,p),g-first+1
    raise KeyError(g)
