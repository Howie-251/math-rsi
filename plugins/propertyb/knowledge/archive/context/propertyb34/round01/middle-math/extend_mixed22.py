"""Add an actual seven or common-low-unit eight to the residual mixed quad domain."""
from pathlib import Path
from itertools import permutations,combinations,product
from functools import lru_cache
from fractions import Fraction as Q
from time import perf_counter
import sys,json
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'high-math'))
from subset_position_dp import SubsetEngine
from extend_low import extensions,project
from joint_layout_lp import solve_profile,Engine,json_value
from verify_joint_layout import verify

@lru_cache(maxsize=32)
def role_permutations(ds):
 roles=[tuple(i for i,d in enumerate(ds) if d==degree) for degree in sorted(set(ds))]
 out=[]
 for blocks in product(*(permutations(role) for role in roles)):
  p=list(range(len(ds)))
  for role,block in zip(roles,blocks):
   for i,j in zip(role,block):p[i]=j
  out.append(tuple(p))
 return tuple(out)

def canonical(ns,ds):
 s=len(ds)
 return min(tuple(sorted((sum(1<<p[i] for i in range(s) if t&(1<<i)),n) for t,n in ns.items() if n)) for p in role_permutations(tuple(ds)))

def main(low,newdegree):
 start=perf_counter();ds=[6]*low+[7]*(4-low);newds=ds+[newdegree]
 source=json.loads((HERE/f'MIXED_QUAD_FULL_22_{low}.json').read_text());bad=[r for r in source['results'] if Q(r['final_bound'])>=1]
 badkeys={canonical({int(t):n for t,n in r['counts'].items()},ds) for r in bad};groups={};raw=filtered=0
 caps=([4]*low+[3]*(4-low)) if newdegree==7 else ([1]*low+[7]*(4-low))
 for w in bad:
  ns={int(t):n for t,n in w['counts'].items()}
  for z in extensions(ns,4,22,new_degree=newdegree,max_extra=4*newdegree-21,old_degrees=ds,codegree_caps=caps):
   raw+=1
   if newdegree==7 and any(canonical(project(z,tuple(range(low))+highs),ds) not in badkeys for highs in combinations(range(low,5),4-low)):continue
   filtered+=1;key=canonical(z,newds)
   if key not in groups:groups[key]=len(groups)
 print('low',low,'newdegree',newdegree,'raw',raw,'filtered',filtered,'groups',len(groups),flush=True);out=[];eng=Engine(22,5)
 for key,gid in groups.items():
  ns=dict(key);sub=SubsetEngine(22,5,ns);r=sub.solve();w=dict(r,graph=f'v22-low{low}-new{newdegree}',group=gid,counts=ns,degrees=newds)
  if r['bound']>=1:
   w['joint']=solve_profile(eng,w);w['final_bound']=w['joint'].get('bound',9)
   if Q(w['final_bound'])<1:w['independent']=verify(w['joint'],22,5,newds)
  else:sub.verify(r);w['final_bound']=r['bound'];w['independent_ABC']=True
  out.append(w)
  if Q(w['final_bound'])>=1:print('remaining',gid,w['final_bound'],flush=True)
  if perf_counter()-start>150:break
 (HERE/f'EXTEND_MIXED22_{low}_{newdegree}.json').write_text(json.dumps(json_value(dict(scope=__doc__,degrees=newds,raw=raw,filtered=filtered,groups=len(groups),complete=len(out)==len(groups),results=out,elapsed_seconds=perf_counter()-start)),indent=2)+'\n')
 print('done',len(out),'bad',sum(Q(w['final_bound'])>=1 for w in out),'seconds',perf_counter()-start,flush=True)
if __name__=='__main__':main(int(sys.argv[1]),int(sys.argv[2]))
