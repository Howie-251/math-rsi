"""Four actual minimum-empty private-star roots (z=6 fixed).
Complete8-incidence set partitions, then sharp exchange necessities.
No probability call, additional vertex or whole-hypergraph enumeration.
"""
from pathlib import Path
from itertools import permutations,product
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter();src=json.loads((P/'MIXED_ONE_SIX_UNIT7_SCREEN.json').read_text());roots=[(16,0),(16,2),(19,0),(19,4)]
parts={()}
for k in range(8):
 nxt=set()
 for pp in parts:
  nxt.add(tuple(sorted(pp+(1<<k,))))
  for j,t in enumerate(pp):nxt.add(tuple(sorted(pp[:j]+pp[j+1:]+(t|(1<<k),))))
 parts=nxt
assert len(parts)==4140

def sharp(base,i,p):
 qout=[t for t,n in p.items() if t.bit_count()==2 and not t>>i&1 for _ in range(n)];big=[t for t,n in p.items() if t.bit_count()==3 for _ in range(n)]
 if base==16:
  if i==0:return not big and not qout
  own=76;other=112;a=p.get(own,0);b=p.get(other,0)
  return b==0 and len(qout)+a<=1 and (a or not qout or qout[0] in [65,66])
 if i==0:return not big and not qout
 a=p.get(112,0)
 return a+len(qout)<=1 and (a or not qout or qout[0] in [65,66,68,72])
def action(star,g):return tuple(sorted((g[t],n) for t,n in star))
results=[]
for base,i in roots:
 z=next(z for z in src['results'] if z['base']==base and z['low']==6);mu={int(t):n for t,n in z['counts'].items() if n};stars=set();labels=list(range(7))+[i]
 for pp in parts:
  p=Counter();ok=True
  for t in pp:
   vs=[labels[k] for k in range(8) if t>>k&1]
   if len(vs)!=len(set(vs)):ok=False;break
   mask=sum(1<<v for v in vs)
   if mask.bit_count()>4 or not mu.get(mask):ok=False;break
   p[mask]+=1
  if ok and all(n<=mu[t] for t,n in p.items()) and 0<=7-len(pp)<=mu.get(0,0):stars.add(tuple(sorted(p.items())))
 keep=[];patterns=Counter()
 for ps in sorted(stars):
  p=dict(ps);r=7-sum(p.values());s=p.get(1<<i,0);new=Counter()
  for t,n in mu.items():
   u=t&~(1<<i);v=p.get(t,0) if t else r;new[u]+=n-v;new[u|(1<<i)]+=v
  new={t:n for t,n in new.items() if n};empty=new.get(0,0);large=sorted(t for t,n in new.items() for _ in range(n) if t.bit_count()>=3)
  allowed=(empty==6 and len(large)==2 and all(t.bit_count()==3 and t>>6&1 for t in large)) or (empty==7 and len(large)==1 and large[0].bit_count()==3 and large[0]>>6&1) or (empty==8 and not large)
  minimal=empty>=(6 if base==16 else 7)
  assert (allowed and minimal)==sharp(base,i,p),(base,i,p,empty,large)
  if not sharp(base,i,p):continue
  assert empty==mu[0]-r+mu[1<<i]-s
  qout=sum(n for t,n in p.items() if t.bit_count()==2 and not t>>i&1);own=p.get(76 if base==16 and i==2 else 112,0);patterns[(r,s,qout,own,empty)]+=1
  keep.append(dict(nonempty_star=p,empty_degree=r,single_partner=s,pair_out=qout,on_own_triple=own,new_empty=empty,new_large=large))
 free=[j for j in range(7) if j not in [6,i]];group=[]
 for order in permutations(free):
  m=list(range(7))
  for a,b in zip(free,order):m[a]=b
  g=[sum(1<<m[j] for j in range(7) if t>>j&1) for t in range(128)]
  if all(mu.get(g[t],0)==mu.get(t,0) for t in range(128)):group.append(g)
 keys=[tuple(sorted(z['nonempty_star'].items())) for z in keep];orbits={min(action(p,g) for g in group) for p in keys}
 f=dict(base=base,low=6,partner=i,core_counts=mu,original_stars=len(stars),retained_stars=len(keep),automorphisms=len(group),first_star_orbits=len(orbits),group=group,stars=keep,patterns=[dict(empty_degree=k[0],single_partner=k[1],pair_out=k[2],on_own_triple=k[3],new_empty=k[4],multiplicity=n) for k,n in sorted(patterns.items())]);results.append(f);print(base,i,len(stars),len(keep),len(group),len(orbits),flush=True)
out=dict(scope=__doc__,passed=True,complete_partition_domain=True,partitions=4140,roots=4,results=results,elapsed_seconds=time.perf_counter()-st)
(P/'MIXED_ONE_SIX_MINIMUM_STARS.json').write_text(json.dumps(out,indent=2)+'\n');print('seconds',out['elapsed_seconds'])
