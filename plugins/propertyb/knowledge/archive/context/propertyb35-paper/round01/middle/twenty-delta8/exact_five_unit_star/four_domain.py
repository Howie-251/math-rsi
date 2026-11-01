"""Shared four-unit-neighbor recovery from the same48 actual three-view residuals.
True permutations preserve neighbor degrees and fix center; no unit assumptions beyond selected actual points.
"""
from common import *
from itertools import product,permutations
start=time.time();rs=json.loads((HERE/'THREE_REMAINDERS.json').read_text())['cases'];allowed={}
for r in rs:
 k=(tuple(r['neighbor_degrees']),tuple(tuple(B) for B in r['partition']),tuple(r['neighbor_codegrees']));allowed.setdefault(k,[]).append(r['neighbor_triple'])
two=json.loads((HERE/'UNIT_TWO.json').read_text())['cases'];res2={(tuple(r['neighbor_degrees']),r['neighbor_codegree'],tuple(tuple(B) for B in r['partition'])) for r in two if not r['strict']};out=[];allviews=[];stats=[];seen={}
for ds in ((8,8,9,9),(8,9,9,9),(9,9,9,9)):
 before=len(out);labels=0;pairs=list(combinations(range(4),2));triples=list(combinations(range(4),3));perms=[p for p in permutations(range(4)) if all(ds[i]==ds[p[i]] for i in range(4))]
 for part in parts(4):
  opts=[]
  for i,j in pairs:
   same=any(i in B and j in B for B in part);p=((0,1),) if same else ((0,),(1,));opts.append([c for dd,c,q in res2 if dd==(ds[i],ds[j]) and q==p])
  for ps in product(*opts):
   cp=dict(zip(pairs,ps));toptions=[]
   for S in triples:
    ren={i:j for j,i in enumerate(S)};pp=tuple(sorted(tuple(ren[i] for i in B if i in S) for B in part if any(i in S for i in B)));key=(tuple(ds[i] for i in S),pp,tuple(cp[(i,j)] for i,j in combinations(S,2)));toptions.append(allowed.get(key,[]))
   if any(not a for a in toptions):continue
   for tt in product(*toptions):
    for q in range(min(tt)+1):
     hi={sum(1<<i for i in S):t for S,t in zip(triples,tt)};hi[15]=q;ns=recover(8,ds,ps,part,hi)
     if ns is None:continue
     labels+=1;kk=(ds,tuple(ns.get(t,0) for t in range(32)))
     if kk not in seen:
      idx=len(out);out.append(dict(id=idx,neighbor_degrees=ds,neighbor_codegrees=ps,partition=part,neighbor_triples=tt,neighbor_quadruple=q,counts=ns))
      for p in perms:
       move=lambda t:(t&1)|sum(1<<(p[i]+1) for i in range(4) if t>>(i+1)&1);vv={move(t):n for t,n in ns.items()};seen[(ds,tuple(vv.get(t,0) for t in range(32)))]=(idx,p)
     idx,p=seen[kk];allviews.append(dict(counts=ns,neighbor_degrees=ds,orbit=idx,from_representative_neighbor_permutation=p))
 stats.append(dict(neighbor_degrees=ds,labelled_count=labels,orbit_count=len(out)-before));print(stats[-1],'seconds',time.time()-start,flush=True)
(HERE/'FOUR_DOMAIN.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=True,orbits=out,labelled=allviews,stats=stats,orbit_count=len(out),labelled_count=len(allviews),elapsed_seconds=time.time()-start)),indent=2)+'\n')
