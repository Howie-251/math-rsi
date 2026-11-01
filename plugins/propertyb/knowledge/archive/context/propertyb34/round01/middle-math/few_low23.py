"""Local exact domains: one/two six-degree locks and common-unit seven-degree locks at v23."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations,product
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

def main(low,h):
 start=perf_counter();s=low+h;ds=[6]*low+[7]*h;groups={};raw=filtered=0
 if s==3:
  for a,b,c in product(range(1,4),repeat=3):
   ls={(0,1):a,(0,2):b,(1,2):c}
   if any(lam!=1 for (i,j),lam in ls.items() if (i<low)!=(j<low)):continue
   for t in range(min(a,b,c)+1):
    ns={7:t,3:a-t,5:b-t,6:c-t}
    for i,d in enumerate(ds):ns[1<<i]=d-sum(n for mask,n in ns.items() if mask&(1<<i))
    ns[0]=34-sum(ns.values())
    if min(ns.values())<0:continue
    raw+=1;key=canonical(ns,ds)
    if key not in groups:groups[key]=len(groups)
  filtered=raw
 else:
  source=json.loads((HERE/f'FEW_LOW23_{low}_{h-1}.json').read_text());assert source['complete']
  oldds=ds[:-1];bad=[r for r in source['results'] if Q(r['final_bound'])>=1]
  keys={canonical({int(t):n for t,n in w['counts'].items()},oldds) for w in bad}
  for w in bad:
   ns={int(t):n for t,n in w['counts'].items()}
   for z in extensions(ns,s-1,23,new_degree=7,max_extra=6,old_degrees=oldds,codegree_caps=[1]*low+[3]*(h-1)):
    raw+=1
    if any(canonical(project(z,tuple(range(low))+hs),oldds) not in keys for hs in combinations(range(low,s),h-1)):continue
    filtered+=1;key=canonical(z,ds)
    if key not in groups:groups[key]=len(groups)
 print('low/high',low,h,'raw',raw,'filtered',filtered,'groups',len(groups),flush=True)
 out=[];eng=Engine(23,s)
 for key,gid in groups.items():
  ns=dict(key);sub=SubsetEngine(23,s,ns);r=sub.solve();w=dict(r,graph=f'v23-{low}low-{h}seven',group=gid,counts=ns,degrees=ds)
  if r['bound']>=1:
   w['joint']=solve_profile(eng,w);w['final_bound']=w['joint'].get('bound',9)
   if Q(w['final_bound'])<1:w['independent']=verify(w['joint'],23,s,ds)
  else:sub.verify(r);w['final_bound']=r['bound'];w['independent_ABC']=True
  out.append(w)
  if gid%50==0:print(gid,w['final_bound'],'elapsed',perf_counter()-start,flush=True)
  if perf_counter()-start>180:break
 (HERE/f'FEW_LOW23_{low}_{h}.json').write_text(json.dumps(json_value(dict(scope=__doc__,degrees=ds,raw=raw,filtered=filtered,groups=len(groups),complete=len(out)==len(groups),results=out,elapsed_seconds=perf_counter()-start)),indent=2)+'\n')
 print('done',len(out),'bad',sum(Q(w['final_bound'])>=1 for w in out),flush=True)
if __name__=='__main__':main(*map(int,sys.argv[1:]))
