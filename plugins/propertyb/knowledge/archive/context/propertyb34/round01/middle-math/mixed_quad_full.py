"""Complete degree-budget four-lock diagnostics for v22 with one/two sixes."""
from pathlib import Path
from itertools import product,permutations,combinations
from fractions import Fraction as Q
from time import perf_counter
import sys,json
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[3]
sys.path[:0]=[str(ROOT/'context/propertyb34-hour1-20261013/low-math'),str(HERE.parent/'high-math')]
from quad_general import profiles
from subset_position_dp import SubsetEngine
from joint_layout_lp import solve_profile,Engine,json_value
from verify_joint_layout import verify

def main(low):
 start=perf_counter();v=22;ds=(6,)*low+(7,)*(4-low);pairs=list(combinations(range(4),2));groups={};raw=0
 perms=[p for p in permutations(range(4)) if all(ds[i]==ds[p[i]] for i in range(4))]
 def canonical(ns):return min(tuple(sorted((sum(1<<p[i] for i in range(4) if t&(1<<i)),n) for t,n in ns.items() if n)) for p in perms)
 ranges=[range(1,5 if min(ds[i],ds[j])==6 else 4) for i,j in pairs]
 for ls in product(*ranges):
  if any(sum(c-1 for ij,c in zip(pairs,ls) if i in ij)>4*ds[i]-21 for i in range(4)):continue
  for ns,*_ in profiles(ds,ls):
   raw+=1;key=canonical(ns)
   if key not in groups:groups[key]=len(groups)
 print('ds',ds,'raw',raw,'groups',len(groups),flush=True);out=[];eng=Engine(v,4)
 for key,gid in groups.items():
  ns=dict(key);sub=SubsetEngine(v,4,ns);r=sub.solve();w=dict(r,graph='v22-'+''.join(map(str,ds)),group=gid,counts=ns)
  if r['bound']>=1:
   w['joint']=solve_profile(eng,w);w['final_bound']=w['joint'].get('bound',9)
   if Q(w['final_bound'])<1:w['independent']=verify(w['joint'],v,4,ds)
  else:sub.verify(r);w['final_bound']=r['bound'];w['independent_ABC']=True
  out.append(w)
  if Q(w['final_bound'])>=1:print('remaining',gid,w['final_bound'],flush=True)
  if perf_counter()-start>150:break
 (HERE/f'MIXED_QUAD_FULL_22_{low}.json').write_text(json.dumps(json_value(dict(scope=__doc__,degrees=ds,raw=raw,groups=len(groups),complete=len(out)==len(groups),results=out,elapsed_seconds=perf_counter()-start)),indent=2)+'\n')
 print('completed',len(out),'remaining',sum(Q(w['final_bound'])>=1 for w in out),'seconds',perf_counter()-start,flush=True)
if __name__=='__main__':main(int(sys.argv[1]))
