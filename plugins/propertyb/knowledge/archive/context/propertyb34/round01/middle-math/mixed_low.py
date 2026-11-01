"""Actual-selection candidates: v22 three sixes plus a unit 7/8, v23 six-low residue plus near-unit 7/8."""
from pathlib import Path
from itertools import product,permutations
from fractions import Fraction as Q
from time import perf_counter
import sys,json
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[3]
sys.path[:0]=[str(ROOT/'context/propertyb34-hour1-20261013/low-math'),str(HERE.parent/'high-math')]
from quad_general import profiles
from subset_position_dp import SubsetEngine
from extend_low import extensions
from joint_layout_lp import solve_profile,Engine,json_value
from verify_joint_layout import verify

def canon(ns,s):
 return min(tuple(sorted((sum(1<<p[i] for i in range(s+1) if t&(1<<i)),n) for t,n in ns.items() if n)) for pp in permutations(range(s)) for p in [pp+(s,)])

def run(v,low_count=None):
 start=perf_counter();out=[];stats=[]
 for degree in [7,8]:
  groups={};raw=0
  if v==22:
   s=3
   for a,b,c in product(range(1,5),repeat=3):
    if max(a+b,a+c,b+c)>5:continue
    for ns,*_ in profiles((6,6,6,degree),(a,b,1,c,1,1)):
     raw+=1;key=canon(ns,s)
     if key not in groups:groups[key]=len(groups)
  else:
   s=low_count or 6;source=json.loads((HERE/('FOUR_LOW_23.json' if s==4 else f'EXTEND_LOW_23_{s}.json')).read_text());bad=[r for r in source['results'] if Q(r['final_bound'])>=1]
   for original in bad:
    ns={int(t):n for t,n in original['counts'].items()}
    for z in extensions(ns,s,v,new_degree=degree,max_extra=int(s==6)):
     raw+=1;key=canon(z,s)
     if key not in groups:groups[key]=len(groups)
  print(v,degree,'raw',raw,'groups',len(groups),flush=True);stats.append(dict(degree=degree,raw=raw,groups=len(groups)))
  eng=Engine(v,s+1)
  for key,gid in groups.items():
   ns=dict(key);sub=SubsetEngine(v,s+1,ns);r=sub.solve();w=dict(r,graph=f'v{v}-{s}low-{degree}',group=gid,counts=ns,degrees=[6]*s+[degree])
   if r['bound']>=1:
    w['joint']=solve_profile(eng,w);w['final_bound']=w['joint'].get('bound',9)
    if Q(w['final_bound'])<1:w['independent']=verify(w['joint'],v,s+1,w['degrees'])
   else:
    sub.verify(r);w['final_bound']=r['bound'];w['independent_ABC']=True
   out.append(w);print(degree,gid,w['final_bound'],'seconds',perf_counter()-start,flush=True)
   if perf_counter()-start>180:break
  if perf_counter()-start>180:break
 (HERE/f'MIXED_LOW_{v}{"_"+str(low_count) if low_count else ""}.json').write_text(json.dumps(json_value(dict(scope=__doc__,v=v,stats=stats,complete=len(stats)==2 and len(out)==sum(x['groups'] for x in stats),results=out,elapsed_seconds=perf_counter()-start)),indent=2)+'\n')
if __name__=='__main__':run(int(sys.argv[1]),int(sys.argv[2]) if len(sys.argv)>2 else None)
