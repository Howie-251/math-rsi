"""New a7 triangle anomaly on nine locks: seven unit core, same partner i.
Start only from the three seven-core families not already strict, and root i
up to their exact automorphism groups. Quotient the first star, then the joint
inventory by that star's stabilizer. No whole H is enumerated.
"""
from pathlib import Path
from itertools import permutations,product
from collections import Counter
from fractions import Fraction as Q
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter();src=json.loads((P/'UNIT7_SCREEN.json').read_text());roots=[(0,0),(19,0),(19,4),(21,0),(21,2)]
def star(mu,i):
 ts=sorted(t for t,c in mu.items() if t and t.bit_count()<=4);target=tuple(2 if j==i else 1 for j in range(7));out=set()
 def visit(rem,picked,start=0):
  if not any(rem):
   if sum(picked.values())<=7 and 7-sum(picked.values())<=mu.get(0,0):out.add(tuple(sorted(picked.items())))
   return
  j=next(j for j,v in enumerate(rem) if v)
  for t in ts:
   if t<start or not t>>j&1 or picked.get(t,0)>=mu[t] or any(t>>k&1 and not rem[k] for k in range(7)):continue
   rr=tuple(v-int(t>>k&1) for k,v in enumerate(rem));pp=dict(picked);pp[t]=pp.get(t,0)+1
   visit(rr,pp,t if rr[j] else 0)
 visit(target,{})
 return sorted(out)
def group(mu,i,big):
 inside={j for j in range(7) if big>>j&1};cells=[sorted(inside-{i}),sorted(set(range(7))-inside-{i})];out=[]
 for orders in product(*(permutations(c) for c in cells)):
  m=list(range(7))
  for c,o in zip(cells,orders):
   for a,b in zip(c,o):m[a]=b
  tab=[sum(1<<m[j] for j in range(7) if t>>j&1) for t in range(128)]
  assert all(mu.get(tab[t],0)==n for t,n in mu.items())
  out.append(tab)
 return out
def act(star,tab):return tuple(sorted((tab[t],n) for t,n in star))
def split(mu,p,r,q):
 ns={}
 for t,n in mu.items():
  a=p.get(t,0);b=r.get(t,0);c=q.get(t,0);vv=[n-a-b+c,a-c,b-c,c]
  if min(vv)<0:return None
  for j,v in enumerate(vv):
   if v:ns[t+128*j]=v
 if any(t.bit_count()>5 for t in ns):return None
 return ns
out=[]
for base,i in roots:
 rr=next(z for z in src['results'] if z['base']==base);mu={int(t):c for t,c in rr['counts'].items()};big=next(iter(rr['large']),0);gs=group(mu,i,big);stars=star(mu,i);orbits={min(act(p,g) for g in gs) for p in stars};cases={};raw=0
 for ps in sorted(orbits):
  p=dict(ps);p[0]=7-sum(p.values());stab=[g for g in gs if act(ps,g)==ps]
  for rs in stars:
   r=dict(rs);r[0]=7-sum(r.values());common=sorted(set(p)&set(r));options=[range(max(0,p[t]+r[t]-mu.get(t,0)),min(p[t],r[t])+1) for t in common]
   for values in product(*options):
    q={t:n for t,n in zip(common,values) if n};lam=sum(q.values())
    if not 2<=lam<=4:continue
    ns=split(mu,p,r,q)
    if ns is None:continue
    assert sum(ns.values())==35 and all(sum(n for t,n in ns.items() if t>>j&1)==7 for j in range(9))
    for a in range(9):
     for b in range(a+1,9):
      val=sum(n for t,n in ns.items() if t>>a&1 and t>>b&1);want=lam if (a,b)==(7,8) else (2 if a==i and b>=7 else 1);assert val==want
    raw+=1
    # Keep x fixed while applying the first star stabilizer to G labels.
    key=None;bestg=None
    for g in stab:
     kk=tuple(sorted(((t&384)|g[t&127],n) for t,n in ns.items()))
     if key is None or kk<key:key=kk;bestg=g
    if key not in cases:
     g=bestg;cases[key]=dict(base=base,partner=i,codegree=lam,P=dict(act(ps,g)),Q=dict(act(rs,g)),joint={g[t]:n for t,n in q.items()},counts=dict(key))
 ff=list(cases.values());out.append(dict(base=base,partner=i,core_counts=mu,core_big=big,automorphisms=len(gs),stars=len(stars),first_star_orbits=len(orbits),pre_stabilizer_cases=raw,cases=ff));print(base,i,'stars',len(stars),'Porbits',len(orbits),'raw',raw,'joint',len(ff),flush=True)
summary=dict(scope=__doc__,rooted_cores=len(roots),joint_cases=sum(len(z['cases']) for z in out),elapsed_seconds=time.perf_counter()-st)
(P/'A7_TRIANGLE_DOMAIN.json').write_text(json.dumps(dict(summary=summary,results=out),indent=2)+'\n');print(json.dumps(summary,indent=2))
