"""No-DP/no-production-formula replay: raw pair-disjoint blocks, orbit keys,35 indices."""
from pathlib import Path
from itertools import combinations,permutations
from fractions import Fraction as Q
import sys,time,json
P=Path(__file__).resolve().parent;ROOT=P.parents[4]
sys.path.insert(0,str(ROOT/'computations'))
from independent_structure_bounds import independent_rows
st=time.process_time();j=json.loads((P/'COMPLETE.json').read_text());assert j['complete']
# Second complete construction: choose/skip every possible >=2 block recursively.
blocks=[tuple(T) for size in [2,3,4] for T in combinations(range(5),size)]
blockpairs=[set(combinations(T,2)) for T in blocks];actual=set()
def visit(i,used,chosen):
 if i==len(blocks):actual.add(tuple(sorted(chosen)));return
 visit(i+1,used,chosen)
 if not used&blockpairs[i]:visit(i+1,used|blockpairs[i],chosen+[sum(1<<v for v in blocks[i])])
visit(0,set(),[]);assert len(actual)==2624
all_orbits=0;checked=0;vals=[];counts=[]
for d in j['domains']:
 ds=d['degrees'];n8=d['eight_count']
 actual_d={pp for pp in actual if all(sum(m.bit_count()-1 for m in pp if m>>i&1)<=4*ds[i]-31 for i in range(5))}
 assert actual_d=={tuple(pp) for pp in d['labelled_keys']}
 group=[g for g in permutations(range(5)) if all(ds[i]==ds[g[i]] for i in range(5))]
 seen=set();rr=[r for r in j['cases'] if r['eight_count']==n8]
 for r in rr:
  pp=tuple(r['packing']);assert pp in actual_d
  image={tuple(sorted(sum(1<<g[i] for i in range(5) if m>>i&1) for m in pp)) for g in group}
  assert len(image)==r['orbit_size'] and image<=actual_d and not image&seen
  seen|=image
  # Recover all original35 trace counts from top five and this exact packing.
  ns={63^(1<<(i+1)):1 for i in range(5)};ns[1]=4
  for m in pp:ns[m<<1]=1
  for i,di in enumerate(ds):ns[1<<(i+1)]=di-4-sum(m>>i&1 for m in pp)
  ns[0]=35-sum(ns.values())
  assert ns=={int(m):n for m,n in r['counts'].items()}
  assert sum(ns.values())==35 and min(ns.values())>=0
  assert [sum(n for m,n in ns.items() if m>>i&1) for i in range(6)]==[9]+ds
  assert r['positions']==[9,10,11,12,13,14] and r['all_deductions_zero']
  stubs=[frozenset(i+1 for i in range(6) if m>>i&1) for m,n in ns.items() for _ in range(n)]
  rows=independent_rows(21,tuple(r['positions']),stubs)
  value=sum(min(rw['A'],rw['B'],rw['C']) for rw in rows)
  assert value==Q(r['bound'])<1
  vals.append(value);checked+=1
 assert seen==actual_d and len(rr)==d['orbit_count'];all_orbits+=len(rr);counts.append([n8,len(actual_d),len(rr)])
assert checked==177 and sum(d[1] for d in counts)==3403
res=dict(status='PASS',complete_domain_key_equality=True,raw_packings=2624,degree_marked_labels=3403,true_degree_orbits=177,counts=counts,fixed_position_profiles=checked,original_stubs_each=35,ordered_distinct_pair_indices_each=1190,independent_rows=21*checked,max=str(max(vals)),all_deductions_zero=True,cpu_seconds=time.process_time()-st)
(P/'VERIFY.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
