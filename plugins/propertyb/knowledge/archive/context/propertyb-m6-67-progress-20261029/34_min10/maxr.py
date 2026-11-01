from pathlib import Path
import importlib.util,json,itertools,time
from fractions import Fraction as F
P=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('d',P.parent/'small31_33/diagnose.py');d=importlib.util.module_from_spec(s);s.loader.exec_module(d);c=d.c

def deletion(v,pos,ell,j):
 types=[T for T,n in ell.items()if n and T>>j&1];cells=[]
 for i,T in enumerate(types):
  for U in types[i:]:
   cap=c.C(ell[T],2)if T==U else ell[T]*ell[U]
   if cap:cells.append((c.weight(v,pos,pos[j],T,U)+c.weight(v,pos,pos[j],U,T),cap,T|U))
 best=F(0)
 for R in range(1<<len(pos)):
  if R>>j&1:continue
  f=sum(n for T,n in ell.items()if T>>j&1 and not T&R);q=d.quota(v-R.bit_count(),f);cost=F(0)
  for w,cap,U in sorted(cells):
   if U&R:continue
   z=min(q,cap);q-=z;cost+=z*w
  assert q==0
  best=max(best,cost)
 return best
c.bad_pair_deletion=deletion
if __name__=='__main__':
 start=time.process_time();rows=[]
 old=json.loads((P.parent/'root/NONUNIT_LOW_PROBE.json').read_text())
 for r in old['rows']:
  if r['strict']:continue
  ell={int(T):n for T,n in r['ell'].items()if n};best=None
  for pos in itertools.combinations(range(10,23),3):
   for order in ((0,1,2),(1,0,2),(1,2,0)):
    ps=tuple(pos[order.index(j)]for j in range(3));u=c.profile_bound(34,ps,ell)
    if best is None or u<best[0]:best=(u,ps)
    if u<1:break
   if best[0]<1:break
  rows.append(r|dict(U=str(best[0]),pos=best[1],strict=best[0]<1));print(rows[-1],flush=True)
 out=dict(rows=rows,cpu_seconds=time.process_time()-start);(P/'MAXR.json').write_text(json.dumps(out,indent=2));print('CPU',out['cpu_seconds'])
