"""Page for references with no crop: per printed page, the list of missing references (with edit boxes) and the page as 3 strips.
python3 make_nocrop_page_v5.py REVIEW.json OUT.html LO HI"""
import sys,os,io,json,base64,html,subprocess,tempfile
sys.path.insert(0,os.path.dirname(__file__))
from cfg import WORK,part_of
from PIL import Image
J=json.load(open(sys.argv[1])); OUT=sys.argv[2]; lo,hi=sys.argv[3],sys.argv[4]
um=J['unmatched']; pages=sorted({(u['printed'],u['pdf']) for u in um})
body=[]
for p,g in pages:
    path,n=part_of(g); d=tempfile.mkdtemp(dir=WORK)
    subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','220','-gray',path,d+'/h'],check=True)
    im=Image.open(d+'/'+os.listdir(d)[0]).convert('L'); subprocess.run(['rm','-rf',d])
    W,H=im.size; top=int(H*0.03); bot=int(H*0.98); BH=330; strips=[]
    y=top
    while y<bot:
        cr=im.crop((int(W*0.02),max(0,y-25),int(W*0.98),min(H,y+BH))).point(lambda v:255 if v>150 else 0).convert('1')
        bf=io.BytesIO(); cr.save(bf,'PNG',optimize=True); strips.append(base64.b64encode(bf.getvalue()).decode()); y+=BH-25
    items=''.join(f'<div class="r e"><span class="n">{p}_{u["j"]}</span><input data-id="{p}_{u["j"]}" data-orig="" value="" autocomplete="off" inputmode="text" placeholder="digits"><span class="f"><b>{html.escape(u["file"])}</b> &nbsp; …{html.escape(u["ctx"][:90])}</span></div>' for u in um if u['printed']==p)
    imgs=''.join(f'<div class="scroll"><img src="data:image/png;base64,{s}" alt="band {i+1} of the page"></div>' for i,s in enumerate(strips))
    body.append(f'<h3 id="p{p}">Printed p. {p} (PDF {g})</h3>{items}<details open><summary>The page in {len(strips)} bands (scroll sideways inside a band)</summary>{imgs}</details>')
src=open(os.path.join(os.path.dirname(__file__),'..','review','html','Vol5_Parisishta_p578-600.html')).read() if False else ''
open(OUT,'w').write('\n'.join(body)); print(len(pages),'pages',len(um),'refs',os.path.getsize(OUT)//1024,'KB')
