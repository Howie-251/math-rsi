"""Complete two-private-point slot splits for four minimum-empty one-six roots.
Two actual seven-degree points share one partner; codegree2..4. Exact mark-
and-partner-preserving quotient, with x fixed, using its first-star stabilizer.
"""
from pathlib import Path
from itertools import product
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter();src=json.loads((P/'MIXED_ONE_SIX_MINIMUM_STARS.json').read_text())
def act(p,g):return tuple(sorted((g[t],n) for t,n in p))
out=[]
for f in src['results']:
 mu={int(t):n for t,n in f['core_counts'].items()};base=f['base'];i=f['partner'];gs=f['group'];stars=[tuple(sorted((int(t),n) for t,n in z['nonempty_star'].items())) for z in f['stars']];first=sorted({min(act(p,g) for g in gs) for p in stars});cases={};raw=0
 for ps in first:
  p=dict(ps);p[0]=7-sum(p.values());stab=[g for g in gs if act(ps,g)==ps]
  for rs in stars:
   r=dict(rs);r[0]=7-sum(r.values());common=sorted(set(p)&set(r));options=[range(max(0,p[t]+r[t]-mu.get(t,0)),min(p[t],r[t])+1) for t in common]
   for values in product(*options):
    q={t:n for t,n in zip(common,values) if n};lam=sum(q.values())
    if not 2<=lam<=4:continue
    ns={};ok=True
    for t,n in mu.items():
     a=p.get(t,0);b=r.get(t,0);c=q.get(t,0);vv=[n-a-b+c,a-c,b-c,c]
     if min(vv)<0:ok=False;break
     for j,v in enumerate(vv):
      if v:ns[t+128*j]=v
    if not ok or any(t.bit_count()>5 for t in ns):continue
    assert sum(ns.values())==35
    assert all(sum(n for t,n in ns.items() if t>>j&1)==(6 if j==6 else 7) for j in range(9))
    for a in range(9):
     for b in range(a+1,9):
      codeg=sum(n for t,n in ns.items() if t>>a&1 and t>>b&1);want=lam if (a,b)==(7,8) else 2 if a==i and b>=7 else 1;assert codeg==want
    raw+=1;key=None;best=None
    for g in stab:
     kk=tuple(sorted(((t&384)|g[t&127],n) for t,n in ns.items()))
     if key is None or kk<key:key=kk;best=g
    if key not in cases:cases[key]=dict(base=base,low=6,partner=i,codegree=lam,P=dict(act(ps,best)),Q=dict(act(rs,best)),joint={best[t]:n for t,n in q.items()},counts=dict(key))
 ff=list(cases.values());out.append(dict(base=base,partner=i,low=6,core_counts=mu,single_stars=len(stars),first_star_orbits=len(first),pre_stabilizer_cases=raw,cases=ff));print(base,i,len(stars),len(first),raw,len(ff),flush=True)
result=dict(scope=__doc__,complete=True,roots=4,joint_cases=sum(len(f['cases']) for f in out),results=out,elapsed_seconds=time.perf_counter()-st)
(P/'MIXED_ONE_SIX_MINIMUM_PAIRS.json').write_text(json.dumps(result,indent=2)+'\n');print('seconds',result['elapsed_seconds'])
