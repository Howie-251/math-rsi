"""Integer checks of the mixedr1 actual-selection interfaces, no probability
search. Confirms old strict traces, exact three-trace automorphism orbits,
forced nonempty stars excluding the six-point, and type12's two violators.
"""
from pathlib import Path
from itertools import permutations
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter();cat=json.loads((P/'GROUP5_CATALOGUE.json').read_text());old=json.loads((P/'GROUP5_EXTERNAL_STAR_REPLAY.json').read_text());one=json.loads((P/'K5_SINGLE_COMPONENT_REPLAY.json').read_text());assert old['passed'] and one['passed']
transfer=[]
for f in old['actual_caller_eliminated_families']:
 mu={int(t):n for t,n in cat['representatives'][f['id']]['counts'].items()};strict=f['all_missing_required_traces'];pair=[t for t in strict if t.bit_count()==2];triples=[t for t in strict if t.bit_count()==3];assert pair or sum(mu[t] for t in triples)>=2
 transfer.append(dict(id=f['id'],strict_pair_traces=pair,strict_three_traces=triples,strict_three_trace_edge_count=sum(mu[t] for t in triples)))
orbits=[]
for ident in [1,5,7,8,9,10,18,26]:
 mu={int(t):n for t,n in cat['representatives'][ident]['counts'].items()};T=next(f['T'] for f in one['families'] if f['id']==ident);orb=set()
 for perm in permutations(range(5)):
  tab=[sum(1<<perm[j] for j in range(5) if t>>j&1) for t in range(32)]
  if {tab[t]:n for t,n in mu.items()}==mu:orb.add(tab[T])
 n=sum(mu[t] for t in orb);assert n>=2
 comp=31^T;single=[1<<j for j in range(5) if comp>>j&1];ps=[]
 if mu.get(comp,0):ps.append([T,comp])
 if all(mu.get(t,0) for t in single):ps.append([T]+single)
 unique=sum(mu[t]==1 for t in ps[0] if t!=T) if len(ps)==1 else None
 if ident in [1,5,8,10]:assert len(ps)==1 and unique>=1
 if ident in [7,9,18]:assert n>=3
 orbits.append(dict(id=ident,selected_T=T,orbit=sorted(orb),orbit_edge_count=n,possible_nonempty_stars_containing_T=ps,additional_shared_unique_blocks_if_forced=unique))
parts={()}
for j in range(5):
 nxt=set()
 for pp in parts:
  nxt.add(tuple(sorted(pp+(1<<j,))))
  for k,t in enumerate(pp):nxt.add(tuple(sorted(pp[:k]+pp[k+1:]+(t|(1<<j),))))
 parts=nxt
parts.remove((31,));mu12={int(t):n for t,n in cat['representatives'][12]['counts'].items()};allowed=[p for p in parts if all(mu12.get(t,0) for t in p)];violators=[]
for pp in allowed:
 d=sum(t.bit_count()>=2 for t in pp)-1-int(6 in pp);assert d<=1
 if d==1:violators.append(pp)
assert set(violators)=={(5,26),(3,28)} and all(mu12[t]==1 for pp in violators for t in pp)
nu={t:(5-t.bit_count())*n for t,n in mu12.items() if t};assert sum(n for t,n in nu.items() if t.bit_count()>=2)-20-nu[6]==2
out=dict(scope=__doc__,passed=True,old_sixlock_classes_transferred=transfer,triple_orbits=orbits,type12=dict(violating_partitions=sorted(violators),global_D_sum=2,special_same_partition_forbidden_by_six_unit=True),elapsed_seconds=time.perf_counter()-st)
(P/'MIXED_ONE_SIX_K5_SELECTION_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(dict(passed=True,transferred_classes=[x['id'] for x in transfer],orbit_sizes=[(x['id'],x['orbit_edge_count']) for x in orbits],type12=out['type12'],elapsed_seconds=out['elapsed_seconds']),indent=2))
