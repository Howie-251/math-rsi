"""Add the actual fifth six-degree point to the unique four-low/three-high residue."""
from pathlib import Path
from fractions import Fraction as Q
from time import perf_counter
import json,sys
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'high-math'))
from subset_position_dp import SubsetEngine
from extend_low import extensions
from extend_mixed22 import canonical
from joint_layout_lp import solve_profile,Engine,json_value
from verify_joint_layout import verify

def main():
 start=perf_counter();source=json.loads((HERE/'MORE_HIGH_23_4_3.json').read_text());assert source['complete']
 bad=[r for r in source['results'] if Q(r['final_bound'])>=1];assert len(bad)==1
 w=bad[0];ds=w['degrees'];newds=ds+[6];ns={int(t):n for t,n in w['counts'].items()};groups={};raw=0
 for z in extensions(ns,7,23,new_degree=6,max_extra=2,old_degrees=ds,codegree_caps=[1]*4+[3]*3):
  raw+=1;key=canonical(z,newds)
  if key not in groups:groups[key]=len(groups)
 print('raw',raw,'groups',len(groups),flush=True);out=[];eng=Engine(23,8)
 for key,gid in groups.items():
  ns=dict(key);sub=SubsetEngine(23,8,ns);r=sub.solve();w=dict(r,graph='v23-five-low-three-high',group=gid,counts=ns,degrees=newds)
  if r['bound']>=1:
   w['joint']=solve_profile(eng,w);w['final_bound']=w['joint'].get('bound',9)
   if Q(w['final_bound'])<1:w['independent']=verify(w['joint'],23,8,newds)
  else:sub.verify(r);w['final_bound']=r['bound'];w['independent_ABC']=True
  out.append(w);print(gid,w['final_bound'],flush=True)
 (HERE/'FIFTH_LOW_23.json').write_text(json.dumps(json_value(dict(scope=__doc__,raw=raw,groups=len(groups),complete=True,results=out,elapsed_seconds=perf_counter()-start)),indent=2)+'\n')
if __name__=='__main__':main()
