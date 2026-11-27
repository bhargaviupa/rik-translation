import subprocess,sys,json,os
from multiprocessing import Pool
os.environ['OMP_THREAD_LIMIT']='1'
P='/root/.claude/uploads/224fdbbf-d54a-585a-b1af-ff03016dade8/9d58eccd-Rig_Vol22.pdf'
W='/tmp/claude-0/-home-user-rik-translation/224fdbbf-d54a-585a-b1af-ff03016dade8/scratchpad/pdfocr/'
def one(n):
    out=W+f'full{n}.txt'
    if os.path.exists(out): return n
    base=W+f'f{n}'
    subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','250','-gray','-png','-singlefile',P,base],check=True,capture_output=True)
    t=subprocess.run(['tesseract',base+'.png','-','-l','kan','--psm','4'],capture_output=True,text=True).stdout
    os.remove(base+'.png'); open(out,'w').write(t); return n
if __name__=='__main__':
    with Pool(4) as p:
        for i,n in enumerate(p.imap_unordered(one,range(1,627))):
            if i%50==0: print(i,flush=True)
    print('DONE')
