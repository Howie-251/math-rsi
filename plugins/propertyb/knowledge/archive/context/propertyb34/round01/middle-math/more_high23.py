"""Add another common-unit 7/8-degree lock, retaining every residual high-deletion projection."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
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

def main(h):
 start=perf_counter();source=json.loads((HERE/('TWO_HIGH_23_4.json' if h==2 else f'MORE_HIGH_23_4_{h}.json')).read_text());assert source['complete']
 bad=[r for r in source['results'] if Q(r['final_bound'])>=1]
 keys={(tuple(w['degrees']),canonical({int(t):n for t,n in w['counts'].items()},w['degrees'])) for w in bad}
 groups={};raw=filtered=0;s=4+h
 for w in bad:
  ds=w['degrees'];ns={int(t):n for t,n in w['counts'].items()}
  for degree in (7,8):
   if degree<ds[-1]:continue
   newds=ds+[degree];caps=[1]*4+[2 if degree==d==8 else 1 for d in ds[4:]]
   for z in extensions(ns,s,23,new_degree=degree,max_extra=4*degree-22,old_degrees=ds,codegree_caps=caps):
    raw+=1
    if any((tuple(newds[i] for i in keep),canonical(project(z,keep),[newds[i] for i in keep])) not in keys for hs in combinations(range(4,s+1),h) for keep in [tuple(range(4))+hs]):continue
    filtered+=1;key=(tuple(newds),canonical(z,newds))
    if key not in groups:groups[key]=len(groups)
 print('h',h+1,'raw',raw,'filtered',filtered,'groups',len(groups),flush=True);out=[];eng=Engine(23,s+1)
 for (ds,key),gid in groups.items():
  ns=dict(key);sub=SubsetEngine(23,s+1,ns);r=sub.solve();w=dict(r,graph=f'v23-fourlow-{h+1}high',group=gid,counts=ns,degrees=list(ds))
  if r['bound']>=1:
   w['joint']=solve_profile(eng,w);w['final_bound']=w['joint'].get('bound',9)
   if Q(w['final_bound'])<1:w['independent']=verify(w['joint'],23,s+1,ds)
  else:sub.verify(r);w['final_bound']=r['bound'];w['independent_ABC']=True
  out.append(w);print(gid,ds,w['final_bound'],flush=True)
  if perf_counter()-start>180:break
 (HERE/f'MORE_HIGH_23_4_{h+1}.json').write_text(json.dumps(json_value(dict(scope=__doc__,raw=raw,filtered=filtered,groups=len(groups),complete=len(out)==len(groups),results=out,elapsed_seconds=perf_counter()-start)),indent=2)+'\n')
if __name__=='__main__':main(int(sys.argv[1]))
