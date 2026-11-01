"""23 vertices, three degree-six locks and common-unit degree-7/8 locks."""
from pathlib import Path
from itertools import product,combinations
from fractions import Fraction as Q
from time import perf_counter
import sys,json
sys.dont_write_bytecode=True
HERE=Path(__file__).parent;ROOT=HERE.resolve().parents[3];MIDDLE=HERE.parent/'middle-math'
sys.path[:0]=[str(HERE),str(MIDDLE),str(ROOT/'context/propertyb34-hour1-20261013/low-math')]
from quad_general import profiles
from subset_position_dp import SubsetEngine
from extend_low import extensions,project
from extend_mixed22 import canonical
from joint_layout_lp import solve_profile,Engine,json_value
from verify_joint_layout import verify

def generate(h):
 groups={};raw=filtered=0
 if h==1:
  for d in (7,8):
   ds=[6,6,6,d]
   for a,b,c in product(range(1,4),repeat=3):
    if max(a+b,a+c,b+c)>4:continue
    for ns,*_ in profiles(tuple(ds),(a,b,1,c,1,1)):
     raw+=1;key=(tuple(ds),canonical(ns,ds));groups.setdefault(key,len(groups));filtered+=1
 else:
  source=json.loads((HERE/f'V23_THREE_LOW_H{h-1}.json').read_text());assert source['complete']
  bad=[z for z in source['results'] if Q(z['final_bound'])>=1]
  keys={(tuple(z['degrees']),canonical({int(t):n for t,n in z['counts'].items()},z['degrees'])) for z in bad}
  caps_by_degree=None
  if h>2:
   pairs=json.loads((HERE/'V23_THREE_LOW_H2.json').read_text())['results'];caps_by_degree={}
   for z in pairs:
    if Q(z['final_bound'])<1:continue
    ds=z['degrees'];ns={int(t):n for t,n in z['counts'].items()};c=sum(n for t,n in ns.items() if t&24==24)
    caps_by_degree[tuple(ds[3:])]=max(c,caps_by_degree.get(tuple(ds[3:]),0))
  for z in bad:
   ns={int(t):n for t,n in z['counts'].items()};ds=z['degrees'];s=len(ds)
   for d in (7,8):
    if d<ds[-1]:continue
    newds=ds+[d]
    if h>=4 and newds.count(7)<2:continue
    caps=[1]*3+[min(x,d) if caps_by_degree is None else caps_by_degree.get((x,d),0) for x in ds[3:]]
    if 0 in caps:continue
    for nc in extensions(ns,s,23,new_degree=d,max_extra=4*d-22,old_degrees=ds,codegree_caps=caps):
     raw+=1
     if any((tuple(newds[i] for i in keep),canonical(project(nc,keep),[newds[i] for i in keep])) not in keys for hs in combinations(range(3,s+1),h-1) for keep in [tuple(range(3))+hs] if sum(newds[i]==7 for i in keep)>=source.get('minimum_sevens',0)):continue
     filtered+=1;key=(tuple(newds),canonical(nc,newds));groups.setdefault(key,len(groups))
 return groups,raw,filtered

if __name__=='__main__':
 h=int(sys.argv[1]);budget=float(sys.argv[2]) if len(sys.argv)>2 else 300;start=perf_counter()
 groups,raw,filtered=generate(h);print('GENERATE',h,raw,filtered,len(groups),perf_counter()-start,flush=True)
 target=HERE/f'V23_THREE_LOW_H{h}.json';cache={}
 if target.exists():
  for z in json.loads(target.read_text())['results']:cache[(tuple(z['degrees']),tuple(sorted((int(t),n) for t,n in z['counts'].items())))]=z
 out=[];engine=Engine(23,3+h)
 for (ds,key),gid in groups.items():
  if (ds,key) in cache:w=cache[ds,key];w['final_bound']=Q(w['final_bound'])
  else:
   ns=dict(key);sub=SubsetEngine(23,3+h,ns);r=sub.solve();w=dict(r,graph=f'v23-three-low-{h}-high',group=gid,counts=ns,degrees=list(ds))
   if r['bound']<1:sub.verify(r);w['final_bound']=r['bound'];w['independent_ABC']=True
   else:
    w['joint']=solve_profile(engine,w);w['final_bound']=w['joint'].get('bound',9)
    if Q(w['final_bound'])<1:w['independent']=verify(w['joint'],23,3+h,ds)
  out.append(w)
  if len(out)%20==0:print('BOUND',h,len(out),sum(Q(z['final_bound'])<1 for z in out),perf_counter()-start,flush=True)
  if len(out)%20==0 or len(out)==len(groups) or perf_counter()-start>budget:
   result=dict(scope=__doc__,high_count=h,minimum_sevens=2 if h>=4 else 0,complete=len(out)==len(groups),raw=raw,filtered=filtered,orbits=len(groups),elapsed=perf_counter()-start,results=out)
   target.write_text(json.dumps(json_value(result),indent=2)+'\n')
  if perf_counter()-start>budget:print('BUDGET_STOP',flush=True);break
