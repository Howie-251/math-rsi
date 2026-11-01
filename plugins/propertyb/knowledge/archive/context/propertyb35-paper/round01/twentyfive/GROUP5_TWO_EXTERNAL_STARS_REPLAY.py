"""Independent exact rational replay of 223 distinct seven-lock witnesses.
No DP/probability/quota modules imported. All local pair domains are rebuilt.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations_with_replacement
from collections import Counter
from math import comb
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter();N=18
cat=json.loads((P/'GROUP5_CATALOGUE.json').read_text())
six=json.loads((P/'GROUP5_EXTERNAL_STAR_COMPLETE.json').read_text())
pilot=json.loads((P/'GROUP5_TWO_EXTERNAL_STARS_PILOT.json').read_text())
old=json.loads((P/'GROUP5_TWO_EXTERNAL_STARS_COMPLETE.json').read_text())
new=json.loads((P/'GROUP5_TWO_EXTERNAL_STARS_ALL_TRACES.json').read_text())
def build(mu,p,r,T):
 ns=Counter()
 for t,c in mu.items():
  a=int(t in p) if t else 7-len(p);b=int(t in r) if t else 7-len(r);q=int(t==T)
  vv=[c-a-b+q,a-q,b-q,q]
  if min(vv)<0:return None
  for mask,n in zip([t,t+32,t+64,t+96],vv):ns[mask]+=n
 ns={t:c for t,c in ns.items() if c}
 assert sum(ns.values())==35 and all(t.bit_count()<=5 for t in ns)
 assert all(sum(c for t,c in ns.items() if t>>i&1)==7 for i in range(7))
 assert all(sum(c for t,c in ns.items() if t>>i&1 and t>>j&1)==(2 if j<5 else 1) for i in range(7) for j in range(i+1,7))
 assert sum(c for t,c in ns.items() if t&96==96)==1 and ns.get(T+96)==1
 return ns
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
 ns={int(t):c for t,c in z['counts'].items()};pos=z['positions'];mu={int(t):c for t,c in cat['representatives'][z['id']]['counts'].items()}
 rebuilt=build(mu,tuple(z['P']),tuple(z['Q']),z['T']);assert rebuilt==ns
 assert len(pos)==7 and len(set(pos))==7 and all(1<=x<=25 for x in pos)
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

def key(z):return z['id'],z['T'],tuple(sorted(z['P'])),tuple(sorted(z['Q']))
bykey={key(z):z for z in old['results']}
for z in new['results']:
 if key(z) in bykey:assert bykey[key(z)]['counts']==z['counts']
 bykey[key(z)]=z
records=[]
for k,z in sorted(bykey.items()):records.append(dict(id=z['id'],T=z['T'],P=z['P'],Q=z['Q'],bound=str(replay(z))))
assert len(records)==223
# Domain equality is recomputed from the old complete six-lock residuals.
domains=[]
for f in pilot['domain']:
 ident=f['id'];mu={int(t):c for t,c in cat['representatives'][ident]['counts'].items()}
 ps=[tuple(p) for p in next(g['residual_partitions'] for g in six['families'] if g['id']==ident)]
 Ts=[t for t in [1,2,4,8,16] if mu.get(t,0)] if ident in [1,5,9,10] else [f['chosen_T']]
 for T in Ts:
  eligible=[p for p in ps if T in p]
  expected={(ident,T,tuple(sorted(p)),tuple(sorted(r))) for p,r in combinations_with_replacement(eligible,2) if build(mu,p,r,T) is not None}
  actual={k for k in bykey if k[:2]==(ident,T)}
  assert actual==expected
  domains.append(dict(id=ident,T=T,eligible_partitions=len(eligible),pair_cases=len(expected)))
assert sum(z['pair_cases'] for z in domains)==223
# Arc consistency: effective self-loops P=Q are deliberately included.
pruning=[]
for f in pilot['domain']:
 ident=f['id'];mu={int(t):c for t,c in cat['representatives'][ident]['counts'].items()};rr=[z for z in records if z['id']==ident]
 active={tuple(sorted(p)) for p in next(g['residual_partitions'] for g in six['families'] if g['id']==ident)};initial=len(active);rounds=[]
 Ts=sorted({z['T'] for z in rr})
 while True:
  why={}
  for T in Ts:
   supported=set()
   for z in rr:
    p=tuple(sorted(z['P']));r=tuple(sorted(z['Q']))
    if z['T']==T and Q(z['bound'])>=1 and p in active and r in active:supported|={p,r}
   for p in active:
    if T in p and p not in supported:why.setdefault(p,[]).append(T)
  rounds.append(dict(active=len(active),removed=[dict(partition=list(p),unsupported_singletons=why[p]) for p in sorted(why)]))
  if not why:break
  active-=set(why)
 missing=sorted(t for t,c in mu.items() if t and c and not any(t in p for p in active))
 pruning.append(dict(id=ident,initial_partitions=initial,rounds=rounds,remaining_partitions=[list(p) for p in sorted(active)],missing_required_traces=missing,eliminated=bool(missing)))
assert [z['id'] for z in pruning if z['eliminated']]==[5,7,8,10,18]
out=dict(scope=__doc__,passed=True,cases=len(records),strict=sum(Q(z['bound'])<1 for z in records),residual=sum(Q(z['bound'])>=1 for z in records),domains=domains,arc_pruning=pruning,remaining_no_full_G_ids=[z['id'] for z in pruning if not z['eliminated']],results=records,elapsed_seconds=time.perf_counter()-st)
(P/'GROUP5_TWO_EXTERNAL_STARS_REPLAY.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['passed','cases','strict','residual','remaining_no_full_G_ids','elapsed_seconds']},indent=2))
print([(z['id'],z['initial_partitions'],len(z['remaining_partitions']),z['missing_required_traces']) for z in pruning])
