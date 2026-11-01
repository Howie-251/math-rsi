"""Second edge-recursion domain; conditional inclusion-exclusion for all extensions."""
from itertools import combinations,permutations
from pathlib import Path
from collections import Counter
from math import comb
import json,time
HERE=Path(__file__).resolve().parent;start=time.process_time()
j=json.loads((HERE/'CENSUS_PROFILE.json').read_text());E=tuple(map(tuple,j['edge_order']));IX={e:i for i,e in enumerate(E)}
match=tuple(map(tuple,j['perfect_matchings']));earlier=[[] for _ in E]
for m in match:
 a,b,c=sorted(m);earlier[c].append((a,b))
# Recover every label member of the supplied S6 orbits independently.
expected=set()
for r in j['rows']:
 g=r['vector'];orb=set()
 for p in permutations(range(6)):
  h=[0]*15
  for e,v in zip(E,g):h[IX[tuple(sorted((p[e[0]],p[e[1]])))]]=v
  orb.add(tuple(h))
 assert len(orb)==r['orbit_size'] and not(expected&orb)
 expected|=orb
# Independent edge-at-a-time recursion, accumulating M3 only when its third
# edge is assigned. No star/row traversal or S6 skipping in this recursion.
g=[0]*15;d=[0]*6;count=0

def rec(k,e,m):
 global count
 if e+sum(4-x for x in d)//2<7:return
 if k==15:
  if e>=7:
   assert tuple(g) in expected
   count+=1
  return
 a,b=E[k];inc=sum(g[i]*g[l] for i,l in earlier[k])
 for v in range(min(4-d[a],4-d[b],12-e)+1):
  if m+v*inc>13:break
  g[k]=v;d[a]+=v;d[b]+=v
  rec(k+1,e+v,m+v*inc)
  d[a]-=v;d[b]-=v
 g[k]=0
rec(0,0,0)
assert count==len(expected)==j['labelled_eligible_scanned']==417328

subs=[]
for missing in range(64):
 out=[];s=missing
 while True:
  out.append(s)
  if not s:break
  s=(s-1)&missing
 subs.append(out)

def nchoose(n,k):return comb(n,k) if n>=k else 0
for r in j['rows']:
 A=list(map(set,r['sets']));U=sorted(set().union(*A));masks=[sum(1<<a for a in range(6) if v in A[a]) for v in U]
 avoid=[sum(not(m&S) for m in masks) for S in range(64)]
 counts=[sum((-1)**s.bit_count()*nchoose(avoid[s],k) for s in range(64)) for k in (3,4)]
 assert counts==[r['C3'],r['C4']]
 # If a specified q-set covers mask C, all q specified points avoid every
 # subset of missing labels; hence the conditional IE count uses avoid[S]-q.
 ext={}
 for q,k in ((2,1),(2,2),(3,1)):
  ext[q,k]=[sum((-1)**s.bit_count()*nchoose(avoid[s]-q,k) for s in subs[63^cov]) for cov in range(64)]
 p3=sorted((ext[2,1][masks[a]|masks[b]] for a,b in combinations(range(len(U)),2)),reverse=True)
 p4=sorted((ext[2,2][masks[a]|masks[b]] for a,b in combinations(range(len(U)),2)),reverse=True)
 h3=max(ext[3,1][masks[a]|masks[b]|masks[c]] for a,b,c in combinations(range(len(U)),3))
 assert [sum(p3[:u]) for u in range(4)]==r['C3_pair_prefix_sums']
 assert [sum(p4[:u]) for u in range(4)]==r['C4_pair_prefix_sums'] and h3==r['C4_max_triple_extension']
 for row in r['maximal_b_parameter_rows']:
  u,t,v,b=[row[x] for x in ('u','t','v','b')]
  assert row['C3_blocker']==sum(p3[:u])+t-u+v
  assert row['C4_blocker']==sum(p4[:u])+(t-u+v)*h3+b-v
out={'status':'PASS','independent_edge_domain_count':count,'S6_orbits':len(j['rows']),
 'all_global_C3_C4_and_conditional_pair_triple_IE_checked':True,
 'scope':'Second complete graph generator and independent conditional-IE extension counts; no negative layout or H search.',
 'cpu_seconds':time.process_time()-start}
(HERE/'INDEPENDENT_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
