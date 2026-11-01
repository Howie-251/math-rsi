"""Six-lock completion candidates built from the exact mixed five-lock residues."""
from pathlib import Path
from itertools import permutations,combinations
from fractions import Fraction as Q
from time import perf_counter
import sys,json
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'high-math'))
from subset_position_dp import SubsetEngine
from extend_low import extensions,project
from extend_mixed22 import canonical
from joint_layout_lp import solve_profile,Engine,json_value
from verify_joint_layout import verify

def main(low,oldnew,newdegree):
 start=perf_counter();source=json.loads((HERE/f'EXTEND_MIXED22_{low}_{oldnew}.json').read_text());ds=source['degrees'];bad=[r for r in source['results'] if Q(r['final_bound'])>=1]
 badkeys={canonical({int(t):n for t,n in w['counts'].items()},ds) for w in bad}
 # A second eight in the two-low/two-seven case is chosen unit to the first;
 # a seven added to the two-low/three-seven case is forced unit by every old projection.
 allunit=(oldnew==8 or newdegree==7)
 caps=[1]*5 if allunit else [1]*low+[7]*(5-low)
 newds=ds+[newdegree];groups={};raw=filtered=0
 for w in bad:
  ns={int(t):n for t,n in w['counts'].items()}
  for z in extensions(ns,5,22,new_degree=newdegree,max_extra=4*newdegree-21,old_degrees=ds,codegree_caps=caps):
   raw+=1
   if newdegree==7 and any(canonical(project(z,tuple(range(low))+hs),ds) not in badkeys for hs in combinations(range(low,6),5-low)):continue
   filtered+=1;key=canonical(z,newds)
   if key not in groups:groups[key]=len(groups)
 print(low,oldnew,newdegree,'raw',raw,'filtered',filtered,'groups',len(groups),flush=True);eng=Engine(22,6);out=[]
 for key,gid in groups.items():
  ns=dict(key);sub=SubsetEngine(22,6,ns);r=sub.solve();w=dict(r,graph=f'v22-second-{low}-{oldnew}-{newdegree}',group=gid,counts=ns,degrees=newds)
  if r['bound']>=1:
   w['joint']=solve_profile(eng,w);w['final_bound']=w['joint'].get('bound',9)
   if Q(w['final_bound'])<1:w['independent']=verify(w['joint'],22,6,newds)
  else:sub.verify(r);w['final_bound']=r['bound'];w['independent_ABC']=True
  out.append(w);print(gid,w['final_bound'],flush=True)
  if perf_counter()-start>150:break
 (HERE/f'SECOND_MIXED22_{low}_{oldnew}_{newdegree}.json').write_text(json.dumps(json_value(dict(scope=__doc__,degrees=newds,raw=raw,filtered=filtered,groups=len(groups),complete=len(out)==len(groups),results=out,elapsed_seconds=perf_counter()-start)),indent=2)+'\n')
if __name__=='__main__':main(*map(int,sys.argv[1:]))
