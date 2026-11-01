"""Complete four-lock domain: three degree-six locks and one degree-seven lock at v22."""
from pathlib import Path
from itertools import product,combinations
from fractions import Fraction as Q
from time import perf_counter
import sys,json
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[3]
sys.path[:0]=[str(ROOT/'context/propertyb34-hour1-20261013/low-math'),str(HERE.parent/'high-math')]
from quad_general import profiles
from mixed_low import canon
from subset_position_dp import SubsetEngine
from joint_layout_lp import solve_profile,Engine,json_value
from verify_joint_layout import verify
start=perf_counter();v=22;ds=(6,6,6,7);pairs=list(combinations(range(4),2));groups={};raw=0
for ls in product(range(1,5),repeat=6):
 if any(sum(c-1 for ij,c in zip(pairs,ls) if i in ij)>4*ds[i]-21 for i in range(4)):continue
 for ns,*_ in profiles(ds,ls):
  raw+=1;key=canon(ns,3)
  if key not in groups:groups[key]=len(groups)
print('raw',raw,'groups',len(groups),flush=True);out=[];eng=Engine(v,4)
for key,gid in groups.items():
 ns=dict(key);sub=SubsetEngine(v,4,ns);r=sub.solve();w=dict(r,graph='v22-three6-seven',group=gid,counts=ns)
 if r['bound']>=1:
  w['joint']=solve_profile(eng,w);w['final_bound']=w['joint'].get('bound',9)
  if Q(w['final_bound'])<1:w['independent']=verify(w['joint'],v,4,ds)
 else:sub.verify(r);w['final_bound']=r['bound'];w['independent_ABC']=True
 out.append(w)
 if Q(w['final_bound'])>=1:print('remaining',gid,w['final_bound'],flush=True)
 if perf_counter()-start>150:break
(HERE/'THREE_LOW_FULL_22.json').write_text(json.dumps(json_value(dict(scope=__doc__,raw=raw,groups=len(groups),complete=len(out)==len(groups),results=out,elapsed_seconds=perf_counter()-start)),indent=2)+'\n')
print('completed',len(out),'remaining',sum(Q(w['final_bound'])>=1 for w in out),'seconds',perf_counter()-start,flush=True)
