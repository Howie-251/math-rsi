"""Only sixedges boundary: cap333444, E6, maxpointfreq2, M3<=3.
Complete6label integer graph domain; no negative layout or originalH enumeration.
"""
from pathlib import Path
from itertools import combinations,combinations_with_replacement,permutations,product
from collections import Counter
from math import comb
import json,time
HERE=Path(__file__).resolve().parent;start=time.process_time();EDGES=list(combinations(range(6),2));EI={e:i for i,e in enumerate(EDGES)};CAP=[3]*3+[4]*3
PERMS=[p+q for p in permutations(range(3)) for q in permutations(range(3,6))]
PIM=[[EI[tuple(sorted((p[a],p[b])))] for a,b in EDGES] for p in PERMS]
def image(g,pm):
 out=[0]*15
 for i,j in enumerate(pm):out[j]=g[i]
 return tuple(out)
def match(lst):
 if not lst:yield [];return
 a=lst[0]
 for b in lst[1:]:
  for rest in match([v for v in lst if v not in (a,b)]):yield [(a,b)]+rest
MATCH=list(match(list(range(6))));MIDX=[[EI[e] for e in mm] for mm in MATCH]
TWO=[(i,j) for i,e in enumerate(EDGES) for j,f in enumerate(EDGES) if i<j and not set(e)&set(f)]
assert len(MATCH)==15 and len(TWO)==45
orbits={};allkeys=set();m0=set();raw=0
for ids in combinations_with_replacement(range(15),6):
 g=[0]*15;deg=[0]*6
 for i in ids:g[i]+=1;a,b=EDGES[i];deg[a]+=1;deg[b]+=1
 if any(d>c for d,c in zip(deg,CAP)):continue
 m3=sum(g[i]*g[j]*g[k] for i,j,k in MIDX)
 if m3>3:continue
 m2=sum(g[i]*g[j] for i,j in TWO);g=tuple(g);allkeys.add(g)
 canon=min(image(g,pm) for pm in PIM);orbits.setdefault(canon,0);orbits[canon]+=1
 if m2==0:m0.add(g)
 raw+=1
rows=[];bad=[]
for g,osize in sorted(orbits.items()):
 deg=[sum(g[i] for i,e in enumerate(EDGES) if v in e) for v in range(6)]
 masks=[];points={}
 for e,w in zip(EDGES,g):points[e]=list(range(len(masks),len(masks)+w));masks.extend([sum(1<<v for v in e)]*w)
 for v in range(6):masks.extend([1<<v]*(CAP[v]-deg[v]))
 N=len(masks);assert N==15
 triples=[frozenset(p) for mm in MATCH for p in product(*(points[e] for e in mm))];m3=len(triples)
 c4=sum((-1)**s.bit_count()*comb(sum(not m&s for m in masks),4) for s in range(64) if sum(not m&s for m in masks)>=4)
 covered=0
 for t in range(1,1<<m3):
  U=set.union(set(),*[set(q) for i,q in enumerate(triples) if t>>i&1]);a=len(U)
  if a<=4:covered+=(-1)**(t.bit_count()+1)*comb(N-a,4-a)
 d4=c4-covered;m2=sum(g[i]*g[j] for i,j in TWO);bound=23-4*m3
 r={'graph':g,'orbit_size':osize,'degree':deg,'C3':m3,'C4':c4,'minimalC4':d4,'bound':bound,'margin':d4-bound,'M2':m2}
 if not m2:r['analytic_double_triangle_C5']=324;r['analytic_block_bound_T3_B13']=88
 elif d4<=bound:bad.append(r)
 rows.append(r)
# Actual group orbit images must partition the complete independentraw graph set.
assert sum(orbits.values())==len(allkeys)==raw
images=set()
for g,size in orbits.items():
 orb={image(g,pm) for pm in PIM};assert len(orb)==size and not orb&images;images|=orb
assert images==allkeys
out={'status':'COMPLETE_ALL_BOUNDARY_STRICT' if not bad else 'COMPLETE_WITH_NONGATED_BOUNDARIES',
 'capacity':CAP,'E':6,'M3_max':3,'raw6edge_multisets':38760,'labelled_necessary_graphs':raw,'size_preserving_orbits':len(rows),'M2zero_labelled':len(m0),
 'rows':rows,'nongated_rows':bad,'scope':__doc__,'cpu_seconds':time.process_time()-start}
(HERE/'E6_PROFILE.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k not in ('rows',)})
