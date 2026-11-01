"""Actual four degree8 vertices in20-point35-edge min8 pair-cover H.
Every real triple view must survive the existing complete55 triple8 certificate catalog.
Recover all four-point exact traces from six pair counts, four triple inclusives and one quadruple inclusive.
"""
from pathlib import Path
from itertools import combinations,product,permutations
import json,sys,time
HERE=Path(__file__).parent;ROOT=HERE.parents[5];sys.dont_write_bytecode=True
start=time.time();old=json.loads((HERE.parents[1]/'20-new-high/DIAGNOSIS.json').read_text())['triples'];allowed={}
for r in old:
 if r['degrees']!=[8,8,8] or r['strict']:continue
 assert max(r['codegrees'])<=3;allowed.setdefault(tuple(r['codegrees']),[]).append(r['triple'])
assert sum(map(len,allowed.values()))==21
pairs=list(combinations(range(4),2));trips=list(combinations(range(4),3));pairm=[sum(1<<i for i in S) for S in pairs];tripm=[sum(1<<i for i in S) for S in trips];seen={};orbits=[];labelled=[];pre_nonnegative=0
for cs in product((1,2,3),repeat=6):
 cdict=dict(zip(pairm,cs));ranges=[allowed.get(tuple(sorted(cdict[sum(1<<i for i in S)] for S in combinations(T,2))),()) for T in trips]
 if any(not rr for rr in ranges):continue
 for ts in product(*ranges):
  for q in range(min(ts)+1):
   pre_nonnegative+=1;I={1<<i:8 for i in range(4)};I.update(cdict);I.update(dict(zip(tripm,ts)));I[15]=q
   ns={T:sum((-1)**(A.bit_count()-T.bit_count())*n for A,n in I.items() if A&T==T) for T in range(1,16)};ns[0]=35-sum(ns.values())
   if min(ns.values())<0:continue
   key=tuple(ns.get(t,0) for t in range(16))
   if key in seen:idx,perm=seen[key]
   else:
    idx=len(orbits);orbits.append(dict(id=idx,degrees=[8]*4,counts=ns,pairs=cs,triples=ts,quadruple=q,pair_energy=sum(cs),labelled_count=0))
    for perm in permutations(range(4)):
     moved={sum(1<<perm[i] for i in range(4) if t>>i&1):n for t,n in ns.items()};seen[tuple(moved.get(t,0) for t in range(16))]=(idx,perm)
    idx,perm=seen[key]
   orbits[idx]['labelled_count']+=1;labelled.append(dict(counts=ns,orbit=idx,from_representative_permutation=perm))
result=dict(scope=__doc__,surviving_triple_count=21,allowed_triple_parameters={str(k):v for k,v in allowed.items()},inclusive_candidates=pre_nonnegative,labelled_count=len(labelled),orbit_count=len(orbits),orbits=orbits,labelled=labelled,elapsed_seconds=time.time()-start)
(HERE/'DOMAIN.json').write_text(json.dumps(result,indent=2)+'\n');print({k:v for k,v in result.items() if k not in ('orbits','labelled','allowed_triple_parameters')})
