"""Volume 5 pass: paths. Scan = Rig_Vol5.pdf at the repository root (724 PDF pages; printed = PDF - 16)."""
import os
VOL=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))   # the vol5/ folder
ROOT=os.path.dirname(VOL)
SCAN=os.environ.get('V5SCAN',os.path.join(ROOT,'Rig_Vol5.pdf'))
EN=os.path.join(ROOT,'Rigveda_Samhita_Vol5_English_Translation.md')
REVIEW=os.path.join(VOL,'review')
WORK=os.environ.get('V5WORK','/tmp/v5num/')
os.makedirs(WORK,exist_ok=True)
OFFSET=16   # printed = PDF - 16 (check against the page headers)
