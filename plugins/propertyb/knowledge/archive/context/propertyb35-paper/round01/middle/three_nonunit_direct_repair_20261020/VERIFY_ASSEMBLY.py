"""Independent fixed-certificate replay + complete trace/attachment receipts; no search."""
from pathlib import Path
from itertools import permutations,combinations_with_replacement
from collections import Counter
from fractions import Fraction
from math import comb
import json,sys,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4];sys.path.insert(0,str(ROOT/'computations'));sys.dont_write_bytecode=True
from independent_structure_bounds import independent_rows
st=time.process_time();base=json.loads((P/'RESULT.json').read_text());tails=json.loads((P/'TAIL_RESULT.json').read_text());five=json.loads((P/'FIVE_LOCK_FULL83.json').read_text());six=json.loads((P/'SIX_LOCK_COMMON_STAR47.json').read_text())
def C(n,k):return comb(n,k) if 0<=k<=n else 0
def E(t,r):return 0 if t=='P' else C(11,r-5)+C(11,r) if t==0 else C(11+t,r)
def U(tt,a,r):return a*C(12,r-4)+(31-a)*C(12,r)-max(a-1,0)*C(8,r-8)+sum(E(t,r) for t in tt)
# Recheck only saved safe-prefix certificates, not optimize new thresholds.
table={tuple(z['types']):z for z in base['residual_types']};assert len(table)==35
for tt,z in table.items():
 a,r,u,D=z['fixed_prefix_certificate'];assert a==z['first_failure_k']-1
 assert U(tt,a,r)==u and C(16,r)==D and u<D
 assert C(12,r-4)-C(12,r)-C(8,r-8)>=0 and C(12,r-4)>=C(12,r)
# Independently expand each stored representative under actual S5 and prove disjoint full coverage.
seen=set();perms=list(permutations(range(5)))
for row in base['orbits']:
 tr=tuple(row['traces']);image={tuple(sorted(sum(1<<p[v] for v in range(5) if T>>v&1) for T in tr)) for p in perms}
 assert len(image)==row['labels'] and not seen&image;seen|=image
allowed=[m for m in range(32) if m.bit_count() in (0,2,3,4)]
assert seen==set(combinations_with_replacement(allowed,3)) and len(seen)==3276 and len(base['orbits'])==91
order=['P',0,2,3,4]
def comps(n,k):
 if k==1:yield (n,);return
 for x in range(n+1):
  for tail in comps(n-x,k-1):yield (x,)+tail
actual_keys=set();generic_count=0;closed=0
for row in base['orbits']:
 tr=tuple(row['traces']);tt=[tuple(sorted(('P' if T>>v&1 else T.bit_count() for T in tr),key=order.index)) for v in range(5)]
 ks=[table[t]['first_failure_k'] for t in tt];assert ks==row['k_by_v']
 if sum(ks)>31:closed+=1;continue
 h=[sum(T>>v&1 for T in tr) for v in range(5)]
 for delta in comps(31-sum(ks),5):
  a=tuple(x+y for x,y in zip(ks,delta));generic_count+=1
  # All these small candidates must actually fail every r/v in the simple bound.
  assert all(U(t,x,r)>=C(16,r) for t,x in zip(tt,a) for r in range(17))
  ds=[1+x+y for x,y in zip(a,h)]
  if min(ds)>=6 and ds.count(6)<=1 and sum(max(x-9,0) for x in ds)<=4:actual_keys.add((tr,a))
assert closed==68 and generic_count==119 and len(actual_keys)==83
five_by={(tuple(z['traces']),tuple(z['attachments'])):z for z in five['cases']};assert set(five_by)==actual_keys
strict5=[z for z in five['cases'] if z['best']['strict']];remaining=[z for z in five['cases'] if not z['best']['strict']];assert len(strict5)==79 and len(remaining)==4
# Independent numerical engine: expand actual edge indices. No proposal engine imported.
def replay(ns,pos,saved,rows):
 stubs=[frozenset(v+1 for v in range(len(pos)) if m>>v&1) for m,n in ns.items() for _ in range(n)];assert len(stubs)==35
 rr=independent_rows(21,tuple(pos),stubs)
 for x,y in zip(rr,rows):
  assert x['k']==y['k'] and all(x[t]==Fraction(y[t]) for t in ('A','B','C'))
 value=sum((min(x['A'],x['B'],x['C']) for x in rr),Fraction());assert value==Fraction(saved)<1
 return value
values5=[]
for z in strict5:
 ns=Counter({31:1});ns.update(z['traces'])
 for v,n in enumerate(z['attachments']):ns[1<<v]+=n
 assert dict(ns)=={int(m):n for m,n in z['counts'].items()}
 values5.append(replay(ns,z['best']['positions'],z['best']['bound'],z['rows']))
# Direct necessary actual common-star domain, from the four remaining sources.
expected=set()
for sid,z in zip('ABCD',remaining):
 tr=tuple(z['traces']);a=tuple(z['attachments']);assert (sid,tr,a) in [(j['source'],tuple(j['traces']),tuple(j['attachments'])) for j in six['cases']]
 for v in ([1,2] if sid=='D' else range(5)):
  s=[1]*5;s[v]+=1;expected.add((sid,0,tuple(s)))
 if sid=='C':
  for T in (7,25):
   low=[int(not(T>>v&1) or v==0) for v in range(5)]
   for delta in comps(2,5):expected.add((sid,T,tuple(x+y for x,y in zip(low,delta))))
assert expected=={(z['source'],z['picked_multi'],tuple(z['picked_singletons'])) for z in six['cases']} and len(expected)==47
values6=[]
for z in six['cases']:
 old=Counter({31:1});old.update(z['traces'])
 for v,n in enumerate(z['attachments']):old[1<<v]+=n
 pick=Counter({1<<v:n for v,n in enumerate(z['picked_singletons']) if n})
 if z['picked_multi']:pick[z['picked_multi']]+=1
 assert sum(pick.values())==6 and all(n<=old[m] for m,n in pick.items())
 ns=Counter()
 for m,n in old.items():
  if n-pick.get(m,0):ns[2*m]=n-pick.get(m,0)
  if pick.get(m,0):ns[2*m+1]=pick[m]
 assert dict(ns)=={int(m):n for m,n in z['counts'].items()} and all(sum(n for m,n in ns.items() if m>>v&1)==d for v,d in enumerate(z['selected_degrees']))
 values6.append(replay(ns,z['best']['positions'],z['best']['bound'],z['independent_rows']))
out={'status':'PASS_FIXED_CERTIFICATES_AND_COMPLETE_LOCAL_COVERAGE','imports_not_reproved':'universal q<=2 repair; six-unit8-pool theorem; conditional-permutation-to-original-coloring lemma; paper proof of actual role/common-star restrictions','trace_orbits':91,'labeled_trace_triples':3276,'safe_prefix_certificates':35,'threshold_closed_orbits':68,'generic_failed_attachments':119,'actual_necessary_attachments':83,'strict_five_lock_certificates':79,'remaining_five_lock_keys':4,'six_lock_common_star_keys':47,'strict_six_lock_certificates':47,'maximum_five_lock_bound':str(max(values5)),'maximum_six_lock_bound':str(max(values6)),'independent_original_edge_indices_each':35,'ordered_distinct_pairs_each':1190,'replayed_probability_rows':21*(79+47),'cpu_seconds':time.process_time()-st}
(P/'ASSEMBLY_VERIFY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
