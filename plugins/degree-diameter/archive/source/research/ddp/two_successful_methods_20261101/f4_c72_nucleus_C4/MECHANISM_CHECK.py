"""Proof-only GF4/conic masks. No controller or fiber graph is constructed."""
import itertools,json,time
from pathlib import Path
D=Path(__file__).resolve().parent;t0=time.process_time()
def mul(a,b):
 z=0
 while b:
  if b&1:z^=a
  b>>=1;a<<=1
  if a&4:a^=7
 return z
def frob(a,s):return mul(a,a) if s else a
def inv(a):return next(b for b in [1,2,3] if mul(a,b)==1)
def smul(a,v):return tuple(mul(a,x) for x in v)
def add(u,v):return tuple(x^y for x,y in zip(u,v))
def span(*vs):
 out=set()
 for cs in itertools.product(range(4),repeat=len(vs)):
  q=(0,0,0)
  for c,v in zip(cs,vs):q=add(q,smul(c,v))
  out.add(q)
 return out
N=(0,1,0);C=[(0,0,1)]+[(1,x,mul(x,x)) for x in range(4)];V=set(itertools.product(range(4),repeat=3));NZ_N={smul(a,N) for a in [1,2,3]}
assert mul(2,2)==3 and mul(2,3)==1
secants=[]
for a,b in itertools.combinations(range(5),2):
 S=span(C[a],C[b]);assert len(S)==16 and not(S&NZ_N);secants.append(S)
for a,b,c in itertools.combinations(range(5),3):assert span(C[a],C[b],C[c])==V
T=[span(N,v) for v in C];assert len({frozenset(S) for S in T})==5 and set.union(*T)==V
for r in range(5):
 other=[span(C[r],C[p]) for p in range(5) if p!=r]
 assert len(set.union(*other))==52 and set.union(*other,T[r])==V
 assert T[r]&set.union(*other)==span(C[r])
configs=[(0,2),(0,3),(1,3)];scalars=[]
for s,a in configs:
 ar=frob(inv(a),s);assert frob(inv(ar),s)==a
 shifts={0,1,2,a,mul(a,frob(2,s))};backshifts={0,1,2,ar,mul(ar,frob(2,s))}
 assert shifts==backshifts==set(range(4))
 scalars.append({'sigma':s,'alpha':a,'inverse_alpha':ar,'shift_coefficients':sorted(shifts),'inverse_shift_coefficients':sorted(backshifts)})
 for p in range(5):
  got={add(v,smul(c,N)) for v in span(C[p]) for c in backshifts}
  assert got==T[p]
 for p,q in itertools.combinations(range(5),2):
  got={add(v,smul(c,N)) for v in span(C[p],C[q]) for c in shifts}
  assert got==V
bad=good=0
for a,b,c in itertools.product(range(5),repeat=3):
 if a==b or b==c:continue
 S=span(C[a],C[b],C[c]);assert (S==V)==(a!=c)
 if a==c:bad+=1;assert not(S&NZ_N)
 else:good+=1
all_bad_union=set.union(*secants);assert all_bad_union==V-NZ_N
r={'status':'PASS_PROOF_ONLY_GF4_CONIC_MASKS','field':'F2[w]/(w^2+w+1); codes0,1,2,3, addXOR','conic':C,'nucleus':N,'conic_pair_checks':10,'conic_distinct_triple_checks':10,'tangent_pencil_planes':5,'tangent_pencil_union':64,'each_adjacent_secant_union':52,'each_adjacent_plus_tangent_union':64,'directed_scalar_cases':scalars,'two_cross_secant_and_shift_cases':30,'nonbacktracking_conic_triples_checked':good+bad,'good_triples':good,'bad_triples':bad,'bad_plane_nucleus_nonzero_intersection':0,'union_all_ten_secant_planes':len(all_bad_union),'excluded_nonzero_nucleus_vectors':sorted(NZ_N),'controller_inputs_read':[],'controller_or_source_graph_constructed':False,'BFS_runs':0,'solver_calls':0,'Lean_calls':0,'candidate_legality_or_novelty_claim':False,'CPU_seconds':time.process_time()-t0,'CPU_budget_seconds':30}
assert r['CPU_seconds']<30
(D/'MECHANISM_CHECK_RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
