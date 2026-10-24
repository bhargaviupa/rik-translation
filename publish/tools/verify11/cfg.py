"""Shared paths. Override with env vars if your layout differs.
VERIFY_WORK : scratch folder for rendered images (default ~/verify_work)
SCAN        : merged better-scan PDF, PDF page N == Vol 11 PDF page N (default $VERIFY_WORK/new.pdf)
"""
import os
REPO=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..','..'))+'/'
WORK=os.path.expanduser(os.environ.get('VERIFY_WORK','~/verify_work'))+'/'
SCAN=os.environ.get('SCAN',WORK+'new.pdf')
EN=REPO+'Rigveda_Samhita_Vol11_English_Translation.md'
KN=REPO+'Rigveda_Samhita_Vol11_Kannada_Text.md'
os.makedirs(WORK,exist_ok=True)
