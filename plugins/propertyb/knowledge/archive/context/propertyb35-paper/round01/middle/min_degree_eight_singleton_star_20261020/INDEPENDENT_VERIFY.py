from pathlib import Path
from collections import Counter
from itertools import combinations_with_replacement,permutations,product
from fractions import Fraction
from math import comb
import json,time,sys
P=Path(__file__).resolve().parent; ROOT=P.parents[4];sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'computations'))
from independent_structure_bounds import independent_rows
st=time.process_time();old=P.parent/'three_nonunit_direct_repair_20261020';base=json.loads((old/'RESULT.json').read_text());five=json.loads((old/'FIVE_LOCK_FULL83.json').read_text());saved=json.loads((P/'RESULT.json').read_text())
def C(n,k):return comb(n,k) if 0<=k<=n else 0
def ex(t,r):return 0 if t=='P' else C(11,r-5)+C(11,r) if t==0 else C(11+t,r)
def U(tt,a,r):return a*C(12,r-4)+(31-a)*C(12,r)-max(a-1,0)*C(8,r-8)+sum(ex(t,r) for t in tt)
tab={tuple(z['types']):z for z in base['residual_types']};order=['P',0,2,3,4]
seen=set();actual=set();closed=0
for z in base['orbits']:
 tr=tuple(z['traces']);orb={tuple(sorted(sum(1<<p[v] for v in range(5) if m>>v&1) for m in tr)) for p in permutations(range(5))}
 assert not seen&orb and len(orb)==z['labels'];seen|=orb
 tt=[tuple(sorted(('P' if m>>v&1 else m.bit_count() for m in tr),key=order.index)) for v in range(5)]
 lower=[tab[t]['first_failure_k'] for t in tt]
 for t,k in zip(tt,lower):
  a,r,u,D=tab[t]['fixed_prefix_certificate'];assert a==k-1 and U(t,a,r)==u<D==C(16,r)
  assert C(12,r-4)-C(12,r)-C(8,r-8)>=0 and C(12,r-4)>=C(12,r)
 if sum(lower)>31:closed+=1;continue
 # independent Cartesian bounded residual enumeration (budget is at most2 here)
 h=[sum(m>>v&1 for m in tr) for v in range(5)]
 for ds in product(range(31-sum(lower)+1),repeat=5):
  if sum(ds)!=31-sum(lower):continue
  a=tuple(x+y for x,y in zip(lower,ds));deg=[1+x+y for x,y in zip(a,h)]
  if min(deg)<8 or sum(max(x-9,0) for x in deg)>4:continue
  assert all(U(t,x,r)>=C(16,r) for t,x in zip(tt,a) for r in range(17))
  actual.add((tr,a))
allowed=[m for m in range(32) if m.bit_count() in (0,2,3,4)]
assert seen==set(combinations_with_replacement(allowed,3)) and len(seen)==3276 and len(base['orbits'])==91
oldfive={(tuple(z['traces']),tuple(z['attachments'])):z for z in five['cases']}
assert len(actual)==25 and actual=={k for k,z in oldfive.items() if min(z['selected_degrees'])>=8}
values=[];replayed5=0
for key in actual:
 z=oldfive[key]
 if not z['best']['strict']:continue
 ns=Counter({31:1});ns.update(z['traces'])
 for v,n in enumerate(z['attachments']):ns[1<<v]+=n
 types=[frozenset(v+1 for v in range(5) if m>>v&1) for m,n in ns.items() for _ in range(n)]
 rr=independent_rows(21,tuple(z['best']['positions']),types)
 value=sum((min(r['A'],r['B'],r['C']) for r in rr),Fraction())
 assert value==Fraction(z['best']['bound'])<1;replayed5+=1
for z in saved['cases']:
 # Direct35 indexed original edges, selecting singleton edge indices rather than mass-count splitting.
 tr=z['traces'];a=z['attachments'];s=tuple(z['singleton_star'])
 original=[(31,False)]+[(t,False) for t in tr]
 original.extend((1<<v,j<s[v]) for v,n in enumerate(a) for j in range(n))
 assert len(original)==35 and sum(flag for m,flag in original)==8
 masks=[(m<<1)|int(flag) for m,flag in original]
 assert Counter(masks)==Counter({int(k):v for k,v in z['counts'].items()})
 types=[frozenset(v+1 for v in range(6) if m>>v&1) for m in masks]
 rr=independent_rows(21,tuple(z['best']['positions']),types)
 value=sum((min(r['A'],r['B'],r['C']) for r in rr),Fraction())
 assert value==Fraction(z['best']['bound'])<1
 z['independent_35_index_rows']=[{'k':r['k'],'A':str(r['A']),'B':str(r['B']),'C':str(r['C']),'minimum':str(min(r['A'],r['B'],r['C']))} for r in rr]
 values.append(value)
expected={(sid,s) for sid in ('C','D') for s in product(range(1,5),repeat=5) if sum(s)==8}
assert expected=={(z['source'],tuple(z['singleton_star'])) for z in saved['cases']} and len(expected)==70
(P/'INDEPENDENT_ROWS.json').write_text(json.dumps({'cases':saved['cases']},indent=2)+'\n')
out={'status':'PASS','scope':'Independent full3276 trace-label coverage viaS5; generic safe-prefix certificates and direct minFdegree8/high-excess filter; all23 saved strict5lock and70 original35-index6lock injection replays. No layout search. Mathematical universal q<=2 and original permutation-coloring lemma remain declared imports.','trace_labels':len(seen),'trace_orbits':len(base['orbits']),'threshold_closed_orbits':closed,'min_degree8_tail_keys':len(actual),'strict5lock_replayed':replayed5,'singleton_degree8_star_cases':len(values),'strict6lock_replayed':sum(v<1 for v in values),'maximum6lock':str(max(values)),'nonstrict':[],'positions_domain':21,'locks':6,'free_vertices':15,'free_injections_denominator':1307674368000,'original_indices':35,'ordered_distinct_pairs':1190,'probability_rows':21*(replayed5+len(values)),'cpu_seconds':time.process_time()-st}
(P/'INDEPENDENT_VERIFY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
