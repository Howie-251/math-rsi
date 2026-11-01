"""Reclassify one already saved actual H/initial state, not a new search."""
from pathlib import Path
import itertools as it,json
P=Path(__file__).resolve().parent
s=json.load(open(P.parent/'twentyfive/CRITICAL_SMALL_BLOCKERS_PILOT.json'))
H=[set(A) for A in s['actual_H']['edges']];G=set(s['actual_H']['G']);V=set(s['actual_H']['points']);R=set(s['found']['initial_red']);L=V-R;g=s['found']['g']
assert len(H)==35 and len({tuple(sorted(A)) for A in H})==35 and all(len(A)==5 for A in H)
assert [A for A in H if A<=R or A<=L]==[G]
assert all(any({a,b}<=A for A in H) for a,b in it.combinations(V,2))
pos=[A-{g} for A in H if g in A and A&R=={g}];neg=[A&L for A in H if g not in A]
small=[B for B in neg if len(B)<=2];F=set.union(*(B for B in small if len(B)==1))
assert pos==[{0,1,12,18}] and F=={0,1,3,12,14,18,23}
assert all(F&B for B in small) # singleton set itself is a complete small cover
# Every singleton must lie in every cover, hence tau exactly |F| without set search.
assert len(F)==7 and pos[0]<=F
D={v:sum(v in A for A in pos)+sum(v in B for B in neg) for v in L}
omit={v:sum(v in A and g in A and A&R!={g} for A in H) for v in L}
deg={v:sum(v in A for A in H) for v in V}
assert all(D[v]==deg[v]-omit[v] for v in L)
# Audit the exact change under forbidden-blue Z on a few explicit nonempty sets.
for Z in ({0},{1},{0,1},{0,1,12,18},F):
 rempos=[A-Z for A in pos];remneg=[B for B in neg if not B&Z]
 for y in L-Z:
  rZ=sum(y in B and bool(B&Z) for B in neg)
  assert sum(y in A for A in rempos)+sum(y in B for B in remneg)==deg[y]-omit[y]-rZ
out={'status':'PASS','scope':'Exact reclassification only, one saved colorable H; no criticality/min-blue initial state assertion.','source':'../twentyfive/CRITICAL_SMALL_BLOCKERS_PILOT.json','g':g,'G':sorted(G),'initial_red':sorted(R),'blue':sorted(L),'positive':[sorted(A) for A in pos],'negative_size_counts':{k:sum(len(B)==k for B in neg) for k in range(1,5)},'small_negative_sets':[sorted(B) for B in small],'common_small_negative_point':sorted(set.intersection(*small)),'distinct_singleton_vertices':sorted(F),'small_negative_transversal_number':len(F),'signed_degree_on_blue':D,'omitted_through_g_occurrences':omit,'signed_degree_on_positive_union':{v:D[v] for v in set.union(*pos)},'total_original_degrees_on_positive_union':{v:deg[v] for v in set.union(*pos)},'all_positive_points_forced_blue_by_singletons':True}
(P/'SAVED_SOURCE_DIAGNOSIS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
