"""Complete second-high extensions of four actual six-degree locks at v=23."""
from pathlib import Path
from fractions import Fraction as Q
from time import perf_counter
import json,sys
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'high-math'))
from subset_position_dp import SubsetEngine
from extend_low import extensions,project
from extend_mixed22 import canonical
from joint_layout_lp import solve_profile,Engine,json_value
from verify_joint_layout import verify

def main():
 start=perf_counter();source=json.loads((HERE/'MIXED_LOW_23_4.json').read_text())
 bad=[r for r in source['results'] if Q(r['final_bound'])>=1]
 keys={d:{canonical({int(t):n for t,n in r['counts'].items()},r['degrees']) for r in bad if r['degrees'][-1]==d} for d in (7,8)}
 groups={};raw=filtered=0
 for w in bad:
  ds=w['degrees'];ns={int(t):n for t,n in w['counts'].items()}
  for degree in (7,8):
   if degree<ds[-1]:continue
   newds=ds+[degree]
   for z in extensions(ns,5,23,new_degree=degree,max_extra=4*degree-22,old_degrees=ds,codegree_caps=[1]*4+[min(ds[-1],degree)]):
    raw+=1
    if canonical(project(z,(0,1,2,3,5)),[6]*4+[degree]) not in keys[degree]:continue
    filtered+=1;key=(tuple(newds),canonical(z,newds))
    if key not in groups:groups[key]=len(groups)
 print('raw',raw,'filtered',filtered,'groups',len(groups),flush=True)
 out=[];eng=Engine(23,6)
 for (ds,key),gid in groups.items():
  ns=dict(key);sub=SubsetEngine(23,6,ns);r=sub.solve();w=dict(r,graph='v23-fourlow-twohigh',group=gid,counts=ns,degrees=list(ds))
  if r['bound']>=1:
   w['joint']=solve_profile(eng,w);w['final_bound']=w['joint'].get('bound',9)
   if Q(w['final_bound'])<1:w['independent']=verify(w['joint'],23,6,ds)
  else:sub.verify(r);w['final_bound']=r['bound'];w['independent_ABC']=True
  out.append(w);print(gid,ds,w['final_bound'],flush=True)
  if perf_counter()-start>180:break
 (HERE/'TWO_HIGH_23_4.json').write_text(json.dumps(json_value(dict(scope=__doc__,raw=raw,filtered=filtered,groups=len(groups),complete=len(out)==len(groups),results=out,elapsed_seconds=perf_counter()-start)),indent=2)+'\n')
if __name__=='__main__':main()
