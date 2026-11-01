"""Independent rational replay of all 245 stored six-lock witnesses.
No probability/DP/pure-quota implementation is imported. Actual-input degree,
projection and star identities and the 51-partition domain are reconstructed.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
from collections import Counter
from math import comb
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter();src=json.loads((P/'GROUP5_EXTERNAL_STAR_COMPLETE.json').read_text());pilot=json.loads((P/'GROUP5_EXTERNAL_STAR_PILOT.json').read_text());cat=json.loads((P/'GROUP5_CATALOGUE.json').read_text());N=19

def C(n,k):return comb(n,k) if 0<=k<=n else 0
# Independent set-partition generation by joining each next element to an
# existing block or forming a new block, compared as unordered block families.
parts={frozenset()}
for i in range(5):
 nxt=set()
 for pp in parts:
  nxt.add(pp|{1<<i})
  for t in pp:nxt.add((pp-{t})|{t|(1<<i)})
 parts=nxt
parts.discard(frozenset({31}));assert len(parts)==51

def replay(z):
 ns={int(t):c for t,c in z['counts'].items()};pos=z['positions'];part=set(z['partition']);mu={int(t):c for t,c in cat['representatives'][z['id']]['counts'].items()}
 assert frozenset(part) in parts
 rebuilt=Counter()
 for t,c in ns.items():rebuilt[t&31]+=c
 assert dict(rebuilt)==mu and sum(ns.values())==35
 assert {t&31 for t in ns if t&32 and t&31}==part
 assert all(ns[t|32]==1 for t in part) and ns.get(32,0)==7-len(part)
 assert all(sum(c for t,c in ns.items() if t>>i&1)==7 for i in range(6))
 assert all(sum(c for t,c in ns.items() if t>>i&1 and t>>j&1)==(2 if j<5 else 1) for i in range(6) for j in range(i+1,6))
 total=Q(0);certs=[]
 for k in range(1,26):
  left=sum(1<<i for i,p in enumerate(pos) if p<k);right=sum(1<<i for i,p in enumerate(pos) if p>k);pivot=next((1<<i for i,p in enumerate(pos) if p==k),0);a=k-1-left.bit_count();b=25-k-right.bit_count()
  def ew(t,side,slots):
   r=5-t.bit_count()
   if pivot:
    if not t&pivot or (t^pivot)&~side:return Q(0)
    return Q(C(slots,r),C(N,r))
   if not r or t&~side:return Q(0)
   return Q(r*C(slots,r-1),N*C(N-1,r-1))
  def pw(t,u):
   r=5-t.bit_count();q=5-u.bit_count()
   if pivot:
    if t&u!=pivot or (t^pivot)&~left or (u^pivot)&~right or r+q>N:return Q(0)
    return Q(C(a,r)*C(b,q),C(N,r)*C(N-r,q))
   if not r or not q or t&u or t&~left or u&~right or r+q-1>N:return Q(0)
   return Q(C(a,r-1)*C(b,q-1),N*C(N-1,r-1)*C(N-r,q-1))
  A=sum(c*ew(t,left,a) for t,c in ns.items());B=sum(c*ew(t,right,b) for t,c in ns.items())
  rawC=sum(c*(d-(t==u))*pw(t,u) for t,c in ns.items() for u,d in ns.items());loss=Q(0)
  if pivot:
   ts=sorted(t for t in ns if t&pivot);slots=[]
   for j,t in enumerate(ts):
    for u in ts[j:]:
     cap=C(ns[t],2) if t==u else ns[t]*ns[u]
     if cap:slots.append([pw(t,u)+pw(u,t),cap,t==u==pivot])
   pure=max(0,(4*ns.get(pivot,0)-N+2)//3);assert pure<=2
   rem=pure
   for slot in slots:
    if slot[2]:take=min(rem,slot[1]);rem-=take;slot[1]-=take;loss+=take*slot[0]
   assert rem==0
   rem=2-pure
   for weight,cap,flag in sorted(slots):
    take=min(rem,cap);loss+=take*weight;rem-=take
   assert rem==0
   i=pivot.bit_length()-1;cc=z['certificates'][i];assert cc['q_total']==2 and cc['q_pure']==pure and Q(cc['loss'])==loss
   certs.append(dict(center=i,q_total=2,q_pure=pure,loss=str(loss)))
  row=z['rows'][k-1];assert Q(row['A'])==A and Q(row['B'])==B and Q(row['C'])==rawC
  assert Q(row['deduction'])==loss and Q(row['corrected_C'])==rawC-loss
  v=min(A,B,rawC-loss);assert v==Q(row['bound']);total+=v
 assert total==Q(z['bound'])
 return total
results=[]
for z in src['results']:results.append(dict(id=z['id'],partition=z['partition'],bound=str(replay(z))))
# Exact domain equality: every admissible external partition is present once.
for f in pilot['domain']:
 mu={int(t):c for t,c in f['mu'].items()};expected={p for p in parts if all(mu.get(t,0)>0 for t in p) and mu.get(0,0)>=7-len(p)}
 actual=[frozenset(z['partition']) for z in src['results'] if z['id']==f['id']]
 assert len(actual)==len(set(actual)) and set(actual)==expected
# Read a required G trace missing from every residual partition. Then a real
# edge of that trace supplies an outside point whose partition is strict.
eliminated=[];remaining=[]
for f in src['families']:
 mu={int(t):c for t,c in cat['representatives'][f['id']]['counts'].items()};rr=[z for z in results if z['id']==f['id']];res=[z['partition'] for z in rr if Q(z['bound'])>=1]
 missing=sorted(t for t,c in mu.items() if t and t!=31 and c and all(t not in p for p in res))
 if missing:
  t=missing[0];witness=[z for z in rr if t in z['partition']];assert witness and all(Q(z['bound'])<1 for z in witness)
  eliminated.append(dict(id=f['id'],required_trace=t,trace_vertices=[i for i in range(5) if t>>i&1],trace_multiplicity=mu[t],strict_partitions_containing_trace=[z['partition'] for z in witness],worst_bound_over_trace=str(max(Q(z['bound']) for z in witness)),all_missing_required_traces=missing))
 else:remaining.append(f['id'])
assert 12 in remaining
f12=next(f for f in src['families'] if f['id']==12)
mu12={int(t):c for t,c in cat['representatives'][12]['counts'].items()}
nu12={t:(5-t.bit_count())*c for t,c in mu12.items() if t}
for pp in f12['residual_partitions']:
 assert sum(t.bit_count()>=2 for t in pp)<=1+int(6 in pp)
nonsingle12=sum(c for t,c in nu12.items() if t.bit_count()>=2)
assert nonsingle12==25 and nu12[6]==3 and 25>20+3
partition_separator=dict(id=12,inequality='For every residual partition P, nonsingle_blocks(P) <= 1 + 1_{6 in P}',left_actual=25,right_actual=23,nu_6=3,residual_partitions=f12['residual_partitions'])
remaining.remove(12)
old=json.loads((P/'GROUP5_PARTITIONS.json').read_text())['results'];positive=[]
for i in remaining:
 ff=next(f for f in src['families'] if f['id']==i);allowed={frozenset(pp) for pp in ff['residual_partitions']};w=next(r for r in old if r['id']==i)
 assert all(frozenset(z['blocks']) in allowed for z in w['partition_multiset'])
 marginal=Counter();count=0
 for z in w['partition_multiset']:
  count+=z['multiplicity']
  for t in z['blocks']:marginal[t]+=z['multiplicity']
 assert count==20 and dict(marginal)=={int(t):c for t,c in w['nu'].items()}
 positive.append(dict(id=i,partition_multiset=w['partition_multiset'],twenty_partitions_and_all_trace_marginals_replayed=True))
extra=json.loads((P/'GROUP5_EXTERNAL_STAR_FULL_EDGE_PILOT.json').read_text())
extra_bound=replay(extra);assert extra_bound<1 and extra['partition']==[1,30]
full_ids=[r['id'] for r in cat['representatives'] if r['counts'].get('31',0)]
assert full_ids==[23,24,25,26]
all_remaining=remaining+[23,24,26]
assert all(not any(int(t).bit_count()==4 and c for t,c in cat['representatives'][i]['counts'].items()) for i in all_remaining)
out=dict(scope=__doc__,passed=True,domain_complete=True,cases=len(results),strict=sum(Q(z['bound'])<1 for z in results),residual=sum(Q(z['bound'])>=1 for z in results),actual_caller_eliminated_families=eliminated,additional_partition_separator=partition_separator,remaining_no_full_G_ids=remaining,remaining_partition_relaxation_witnesses=positive,extra_full_G_case=dict(id=25,partition=extra['partition'],required_trace=30,bound=str(extra_bound),all_rows_and_quotas_replayed=True),remaining_all_group_ids=all_remaining,remaining_groups_have_no_four_trace=True,results=results,elapsed_seconds=time.perf_counter()-st)
(P/'GROUP5_EXTERNAL_STAR_REPLAY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['passed','domain_complete','cases','strict','residual','remaining_no_full_G_ids','extra_full_G_case','remaining_all_group_ids','remaining_groups_have_no_four_trace','elapsed_seconds']},indent=2));print('trace-eliminated',[(e['id'],e['required_trace'],e['worst_bound_over_trace']) for e in eliminated]);print('separator-eliminated',12)
