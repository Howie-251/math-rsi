"""Stream the full edge list of the accepted deterministic parameter object."""
import argparse,json
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--parameters',type=Path,default=Path(__file__).with_name('HIT.json'));p.add_argument('--output',type=Path,required=True);args=p.parse_args()
h=json.loads(args.parameters.read_text());m=h['phase_modulus'];q=h['normal_modulus'];a=h['action'];n=m*q;ph=h['all_phases'];b=h['all_normals'];assert n==2262690 and len(ph)==9
shift=[[pow(a,j,q)*v%q for v in b] for j in range(m)];nextbase=[[((j+k)%m)*q for k in ph] for j in range(m)]
with args.output.open('w') as f:
    f.write(f'{n} {9*n//2}\n');count=0
    for u in range(n):
        j,x=divmod(u,q)
        for d in range(9):
            y=x+shift[j][d]
            if y>=q:y-=q
            v=nextbase[j][d]+y
            if u<v:f.write(f'{u} {v}\n');count+=1
    assert count==9*n//2
