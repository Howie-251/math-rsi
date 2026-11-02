"""Stream a literal edge list from the complete accepted parameter object."""
import argparse,json
from pathlib import Path
parser=argparse.ArgumentParser()
parser.add_argument('--parameters',type=Path,default=Path(__file__).with_name('HIT.json'))
parser.add_argument('--output',type=Path,required=True)
args=parser.parse_args()
p=json.loads(args.parameters.read_text());q=p['field'];m=p['phase_modulus'];beta=p['beta']
assert q==49663 and m==93 and pow(beta,93,q)==1 and pow(beta,31,q)!=1 and pow(beta,3,q)!=1
phases=p['all_phases'];normals=p['all_normals'];n=q*m
shifts=[[pow(beta,j,q)*b%q for b in normals] for j in range(m)]
nextbase=[[((j+k)%m)*q for k in phases] for j in range(m)]
with args.output.open('w') as f:
    f.write(f'{n} {4*n}\n');count=0
    for u in range(n):
        j,x=divmod(u,q)
        for d in range(8):
            y=x+shifts[j][d]
            if y>=q:y-=q
            v=nextbase[j][d]+y
            if u<v:f.write(f'{u} {v}\n');count+=1
    assert count==4*n
