"""Conditional r8=5 only: all fifteen external points have degree9.
For each49 core representative, pair energy C>=14 gives an actual external y with total core codegree
S<=floor((160-2C)/15)<=8. Promote the same old trace slots, full-six0 and every full-five<=1.
Only domain generation/counting; no unconditional six8 assumption or position DP.
"""
from pathlib import Path
from itertools import permutations
import json,time,sys
HERE=Path(__file__).parent;sys.dont_write_bytecode=True;start=time.time();source=json.loads((HERE.parent/'five_join/FIVE_REMAINDERS.json').read_text())['cases'];seen={};orbits=[];prefix_labelled=[];stats=[];complete=True
for core in source:
 ns0={int(t):n for t,n in core['counts'].items()};C=sum(n*t.bit_count()*(t.bit_count()-1)//2 for t,n in ns0.items());budget=(160-2*C)//15;assert budget in (7,8);ts=sorted((t for t,n in ns0.items() if t and t!=31 and n),key=lambda t:(-t.bit_count(),t));before=len(prefix_labelled);p={31:0};lam=[0]*5
 def visit(j,used_weight,used_edges):
  global complete
  if j==len(ts):
   if min(lam)<1:return
   p0=9-used_edges
   if not 0<=p0<=ns0[0]:return
   ns={0:ns0[0]-p0,32:p0}
   for t,n in ns0.items():
    if not t:continue
    q=p.get(t,0);ns[t]=n-q;ns[t|32]=q
   kk=tuple(ns.get(t,0) for t in range(64))
   if kk in seen:idx,perm=seen[kk]
   else:
    idx=len(orbits);orbits.append(dict(id=idx,degrees=[8]*5+[9],counts=ns,source_core_id=core['id'],source_core_counts=ns0,pair_energy=C,association_budget=budget,total_association=used_weight,mixed_incidence=used_edges,promoted=p.copy(),promoted_empty=p0,low_codegrees=lam.copy(),prefix_labelled_count=0))
    for perm in permutations(range(5)):
     def move(t):return(t&32)|sum(1<<perm[i] for i in range(5) if t>>i&1)
     moved={move(t):n for t,n in ns.items()};seen[tuple(moved.get(t,0) for t in range(64))]=(idx,perm)
    idx,perm=seen[kk]
   orbits[idx]['prefix_labelled_count']+=1;prefix_labelled.append(dict(counts=ns,source_core_id=core['id'],orbit=idx,from_representative_low_permutation=perm));return
  t=ts[j];w=t.bit_count();cap=min(ns0[t],(budget-used_weight)//w,1 if w==4 else 9)
  for a in range(cap+1):
   if any(lam[i]+a>budget-4 for i in range(5) if t>>i&1):continue
   p[t]=a
   for i in range(5):lam[i]+=a*(t>>i&1)
   visit(j+1,used_weight+a*w,used_edges+a)
   for i in range(5):lam[i]-=a*(t>>i&1)
  p.pop(t,None)
 visit(0,0,0);stats.append(dict(core_id=core['id'],pair_energy=C,association_budget=budget,prefix_promotions=len(prefix_labelled)-before));print(core['id'],'C',C,'Sbound',budget,'prefix',len(prefix_labelled)-before,'orbits_total',len(orbits),'seconds',time.time()-start,flush=True)
 if time.time()-start>25:complete=False;break
result=dict(scope=__doc__,complete=complete,source_core_count=len(source),processed_core_count=len(stats),prefix_labelled_count=len(prefix_labelled),orbit_count=len(orbits),core_stats=stats,orbits=orbits,prefix_labelled=prefix_labelled,elapsed_seconds=time.time()-start)
(HERE/'DOMAIN.json').write_text(json.dumps(result,indent=2)+'\n');print('complete',complete,'prefix',len(prefix_labelled),'orbits',len(orbits),'seconds',time.time()-start)
