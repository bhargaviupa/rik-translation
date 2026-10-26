"""Volume 1 numeral pass: scan parts of the better (~575 dpi) scan and paths.
Global PDF page = page number in the user's full 143 MB scan; each part holds a run of it."""
import os
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..','..','..'))
PARTS=[  # (path, first global PDF page)
    ('kannada/01 Rigveda Samhitha Volume 1 1.pdf',1),
    ('kannada/01 Rigveda Samhitha Volume 1 2.pdf',101),
    ('kannada/01 Rigveda Samhitha Volume 1 3.pdf',201),
    ('kannada/01 Rigveda Samhitha Volume 1 4,pdf.pdf',301),
    ('kannada/01 Rigveda Samhitha Volume 1 5.pdf',401),
    ('kannada/01 Rigveda Samhitha Volume 1 6.pdf',501),
    ('kannada/01 Rigveda Samhitha Volume 1 7.pdf',601),
    ('kannada/01 Rigveda Samhitha Volume 1 8.pdf',701),
    ('kannada/01 Rigveda Samhitha Volume 1 9.pdf',801),
    ('kannada/01 Rigveda Samhitha Volume 1 10.pdf',876),
]
EN=os.path.join(ROOT,'Rigveda_Samhita_Vol1_English_Translation.md')
GAPS=os.path.join(ROOT,'Rigveda_Samhita_Vol1_Gaps_English_Translation.md')
WORK=os.environ.get('V1WORK','/tmp/v1num/')
os.makedirs(WORK,exist_ok=True)
def part_of(g):
    """global PDF page -> (part path, page within part)"""
    for i,(p,first) in enumerate(PARTS):
        last=PARTS[i+1][1]-1 if i+1<len(PARTS) else 10**6
        if first<=g<=last: return os.path.join(ROOT,p),g-first+1
    raise KeyError(g)
