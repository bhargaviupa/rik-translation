"""Volume 2 numeral pass: scan parts of the better scan and paths.
Global PDF page = page number in the user's full scan; each part holds a run of it."""
import os
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..','..','..'))
PARTS=[  # (path, first global PDF page)
    ('kannada/02 Rigveda Samhitha Volume 02  1.pdf',1),
    ('kannada/02 Rigveda Samhitha Volume 02 2.pdf',151),
    ('kannada/02 Rigveda Samhitha Volume 02 3.pdf',301),
    ('kannada/02 Rigveda Samhitha Volume 02 4.pdf',451),
    ('kannada/02 Rigveda Samhitha Volume 02 5.pdf',601),
]
EN=os.path.join(ROOT,'Rigveda_Samhita_Vol2_English_Translation.md')
WORK=os.environ.get('V2WORK','/tmp/v2num/')
os.makedirs(WORK,exist_ok=True)
def part_of(g):
    """global PDF page -> (part path, page within part)"""
    for i,(p,first) in enumerate(PARTS):
        last=PARTS[i+1][1]-1 if i+1<len(PARTS) else 822
        if first<=g<=last: return os.path.join(ROOT,p),g-first+1
    raise KeyError(g)
