"""Transcribe scanned pages of the Kannada Rigveda commentary into a Kannada-script markdown file (Kannada-first reading).

  python3 publish/tools/kannada/scan_to_kannada.py --pdf vol11/scans/Rig_Vol11.pdf --first 171 --last 175 --offset 18 --out /tmp/test_kn.md [--dry]

--pdf/--first/--last   a scan PDF and a range of PDF pages (one API call per page)
--offset K             printed page = PDF page - K (marker lines use it; use --offset 0 and read printed numbers if unknown)
--out FILE             appended to, one block per page; pages already in FILE (marker present) are skipped, so a run can be resumed
--dry                  render the pages and print the estimated input size and cost; no API call, no key needed
Key: env RIK_API_KEY (never put it in a file). No extended thinking is requested. Cost log: FILE.costs.jsonl (one line per page).
Stops at once on any API error, on a reply without the marker, or when the cumulative cost would pass --budget (USD).
Prices are ASSUMED ($3 / $15 per million input / output tokens, cache write x1.25, cache read x0.1): change with --price-in/--price-out.
The output follows the layout of vol11/Rigveda_Samhita_Vol11_Kannada_Text.md: page marker, header line in italics, section labels in italics,
bold headwords, Sanskrit blocks as '> ' lines, doubtful readings as [?]. The second step (resolving [?] by zoom) is a separate tool."""
import os,sys,re,json,base64,subprocess,tempfile,argparse,time,glob
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..','..'))
CROP=os.path.join(ROOT,'publish','tools','pageprep','crop_pages.py')
SYSTEM='''You transcribe pages of a 1949 Kannada book (a commentary on the Rigveda: Sayana's Sanskrit bhashya printed in Kannada script, plus a Kannada-language explanation) into Kannada-script text, exactly as printed. You receive one page as horizontal strips in order (top to bottom).

RULES (strict)
1. Letter by letter, as printed. NEVER complete, correct or normalise a word or number from memory or from what you think it should be, even for familiar Sanskrit or verses. Write what the print shows.
2. A letter, word or digit you cannot read with confidence: write your best reading and put [?] directly after the word (or after the digit group); if nothing is readable write [?] alone. Never guess silently. A wrong confident reading is worse than [?].
3. In this typeface plain ma and ya are drawn with a hook that looks like the vowel sign u (e.g. ಮುರುತಃ = marutah). Do not read it as u. A small subscript stroke inside Pada lines is the compound-division mark.
4. Numerals: copy the Kannada digits as printed (೦-೯); references have 2-5 numbers joined by hyphens; keep the separators. Digits 2/3/7 look alike: round open loop = 2, hooked ಇ/ಖ-like = 3, flat-footed ಒ-like = 7; 3/5, 6/7, 2/9, 8/9 are also easily confused. If unsure, [?].
5. Keep the printed order and paragraph structure. Do not translate, do not add Devanagari, IAST or English, do not summarise.

OUTPUT FORMAT (markdown, nothing before the first line)
<!-- PDF {PDF} · printed {PRINTED} -->
*[running head as printed, in brackets]*   (omit if the page has none)
Then the page content in order: section labels in italics (e.g. *ಸಾಯಣಭಾಷ್ಯಂ*, *ಪ್ರತಿಪದಾರ್ಥ*, *ಭಾವಾರ್ಥ*, *ವಿಶೇಷವಿಷಯಗಳು*, *ವ್ಯಾಕರಣಪ್ರಕ್ರಿಯಾ*) as printed; bold (**...**) for printed bold headwords; every block of Sanskrit (Samhita, Pada, Sayana's bhashya, Sanskrit quotations) as '> ' lines, one line per printed line, keeping the printed hyphenation at line ends; Kannada prose as paragraphs; references in parentheses as printed; a small-type grammar note as a paragraph in italics. If a page is blank, a figure, a duplicate or cut off, say so in one italic line and do not invent text.'''
def render(pdf,page,dpi,strips,tmp):
    r=subprocess.run(['python3',CROP,pdf,str(page),str(page),tmp,'--dpi',str(dpi),'--strips',str(strips),'--quality','85'],capture_output=True,text=True)
    fs=sorted(glob.glob(os.path.join(tmp,f'p{page}_*.jpg')))
    if not fs: fs=sorted(glob.glob(os.path.join(tmp,f'p{page}.jpg')))
    if not fs: sys.exit(f'render failed for page {page}: {r.stderr[-300:]}')
    return fs
def spent(cf): return sum(json.loads(l)['usd'] for l in open(cf)) if os.path.exists(cf) else 0.0
def printed_label(p,off): return str(p-off) if p-off>0 else f'front-matter (PDF {p})'
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--pdf',required=True); ap.add_argument('--first',type=int,required=True); ap.add_argument('--last',type=int,required=True)
    ap.add_argument('--offset',type=int,default=0); ap.add_argument('--out',required=True); ap.add_argument('--dry',action='store_true')
    ap.add_argument('--model',default='claude-sonnet-5-5'); ap.add_argument('--dpi',type=int,default=300); ap.add_argument('--strips',type=int,default=3)
    ap.add_argument('--budget',type=float,default=20.0); ap.add_argument('--price-in',type=float,default=3.0); ap.add_argument('--price-out',type=float,default=15.0)
    ap.add_argument('--max-tokens',type=int,default=8000); a=ap.parse_args()
    out=a.out; cf=out+'.costs.jsonl'; have=open(out,encoding='utf8').read() if os.path.exists(out) else ''
    if not a.dry:
        import anthropic; cl=anthropic.Anthropic(api_key=os.environ['RIK_API_KEY'])
    tot_img=0; tot_pix=0
    for p in range(a.first,a.last+1):
        if re.search(rf'<!-- PDF {p} ·',have): print(f'PDF {p}: already in {out}, skipped'); continue
        if spent(cf)>=a.budget: print('budget reached',round(spent(cf),2)); return 3
        with tempfile.TemporaryDirectory() as tmp:
            fs=render(a.pdf,p,a.dpi,a.strips,tmp)
            from PIL import Image
            pix=sum(Image.open(f).width*Image.open(f).height for f in fs)
            if a.dry:
                tot_img+=len(fs); tot_pix+=pix; print(f'PDF {p}: {len(fs)} strips, {pix/1e6:.2f} Mpx, ~{int(pix/750)} input tokens (image estimate w*h/750)'); continue
            user=[]
            for k,f in enumerate(fs):
                user.append({'type':'text','text':f'PDF page {p}, strip {k+1} of {len(fs)}:'})
                user.append({'type':'image','source':{'type':'base64','media_type':'image/jpeg','data':base64.b64encode(open(f,'rb').read()).decode()}})
            user.append({'type':'text','text':f'Transcribe this page now. The first line must be: <!-- PDF {p} · printed {printed_label(p,a.offset)} -->'})
        t=time.time(); txt=''
        with cl.messages.stream(model=a.model,max_tokens=a.max_tokens,system=[{'type':'text','text':SYSTEM,'cache_control':{'type':'ephemeral'}}],messages=[{'role':'user','content':user}]) as st:
            for x in st.text_stream: txt+=x
            u=st.get_final_message().usage
        cw=u.cache_creation_input_tokens or 0; cr=u.cache_read_input_tokens or 0
        usd=((u.input_tokens+1.25*cw+0.1*cr)*a.price_in+u.output_tokens*a.price_out)/1e6
        open(cf,'a').write(json.dumps(dict(page=p,model=a.model,inp=u.input_tokens,cache_write=cw,cache_read=cr,out=u.output_tokens,chars=len(re.findall('[ಀ-೿]',txt)),usd=round(usd,4),sec=round(time.time()-t)))+'\n')
        print(f'PDF {p}: in {u.input_tokens} cw {cw} cr {cr} out {u.output_tokens} -> ${usd:.4f}  total ${spent(cf):.2f}  Kannada chars {len(re.findall(chr(0x0C80)+"-"+chr(0x0CFF),txt)) if False else len(re.findall("[ಀ-೿]",txt))}  [?] {txt.count("[?]")}')
        if not txt.lstrip().startswith(f'<!-- PDF {p} ·'): open(out+f'.bad_{p}.txt','w',encoding='utf8').write(txt); print('reply lacks the page marker; raw saved, stopping'); return 4
        with open(out,'a',encoding='utf8') as f: f.write(txt.strip()+'\n\n')
        have+=txt
    if a.dry:
        n=a.last-a.first+1; est_in=tot_pix/750
        print(f'DRY SUMMARY: {n} pages, {tot_img} strips, ~{int(est_in)} image tokens ({int(est_in/n)}/page) + ~700 system tokens (cached after page 1)')
        print(f'  assumed output 1,500-6,000 tokens/page => ${(est_in/n*a.price_in+1500*a.price_out)/1e6:.3f} - ${(est_in/n*a.price_in+6000*a.price_out)/1e6:.3f} per page; real figures come from the first live run (FILE.costs.jsonl)')
    return 0
sys.exit(main())
