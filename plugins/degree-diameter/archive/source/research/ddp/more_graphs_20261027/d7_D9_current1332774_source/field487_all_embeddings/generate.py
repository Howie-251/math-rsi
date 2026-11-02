"""Stream the complete hit edge set; no distances or hashes are computed."""
from pathlib import Path
import argparse,json,sys
p=argparse.ArgumentParser();p.add_argument('--recipe',default=str(Path(__file__).with_name('HIT_RECIPE.json')));p.add_argument('--output');args=p.parse_args()
r=json.loads(Path(args.recipe).read_text());N=r['normal_modulus'];M=r['phase_modulus'];a=r['action'];darts=r['all_darts_normal_phase'];n=N*M
f=Path(args.output).open('w') if args.output else sys.stdout
f.write(f'{n} {n*7//2}\n')
for phase in range(M):
 shifts=[pow(a,phase,N)*b%N for b,j in darts];bases=[((phase+j)%M)*N for b,j in darts]
 for x in range(N):
  u=phase*N+x
  for s,base in zip(shifts,bases):
   v=base+(x+s)%N
   if u<v:f.write(f'{u} {v}\n')
if args.output:f.close()
