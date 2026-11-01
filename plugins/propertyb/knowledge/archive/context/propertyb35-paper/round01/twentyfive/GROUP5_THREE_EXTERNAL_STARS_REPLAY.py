"""Independent exact domain and rational replay for the eight-lock closure.
Enumerates ordered partition triples, then quotients explicitly. Uses direct
8-cell inclusion-exclusion, not the domain generator or DP/probability code.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from collections import Counter
from math import comb
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter();N=17
cat=json.loads((P/'GROUP5_CATALOGUE.json').read_text())
seven=json.loads((P/'GROUP5_TWO_EXTERNAL_STARS_REPLAY.json').read_text());assert seven['passed']
source=json.loads((P/'GROUP5_THREE_EXTERNAL_STARS_DOMAIN.json').read_text())
complete=json.loads((P/'GROUP5_THREE_EXTERNAL_STARS_COMPLETE.json').read_text())
def direct(mu,ps,T,mode,U):
 ns={}
 for t,n in mu.items():
  a,b,c=[int(t in pp) if t else 7-len(pp) for pp in ps]
  triple=int(t==T);ab=triple+int(mode=='211' and t==U);ac=bc=triple
  cells=[n-a-b-c+ab+ac+bc-triple,a-ab-ac+triple,b-ab-bc+triple,ab-triple,c-ac-bc+triple,ac-triple,bc-triple,triple]
  if min(cells)<0:return None
  for mask,ncell in enumerate(cells):
   if ncell:ns[t+32*mask]=ncell
 if any(t.bit_count()>5 for t in ns):return None
 assert sum(ns.values())==35
 assert all(sum(c for t,c in ns.items() if t>>i&1)==7 for i in range(8))
 for i in range(8):
  for j in range(i+1,8):
   want=2 if j<5 or mode=='211' and (i,j)==(5,6) else 1
   assert sum(c for t,c in ns.items() if t>>i&1 and t>>j&1)==want
 assert ns.get(T+224)==1 and sum(c for t,c in ns.items() if t&224==224)==1
 projected=Counter()
 for t,c in ns.items():projected[t&31]+=c
 assert dict(projected)==mu
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
 rebuilt=direct(mu,[tuple(pp) for pp in z['partitions']],z['T'],z['mode'],z['U']);assert rebuilt==ns
 assert len(pos)==8 and len(set(pos))==8 and all(1<=x<=25 for x in pos)
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

def signature(z):
 ps=tuple(tuple(sorted(pp)) for pp in z['partitions'])
 return z['id'],z['T'],z['mode'],ps,z['U']
expected={};domain_statistics=[]
for ident in [1,9]:
 mu={int(t):c for t,c in cat['representatives'][ident]['counts'].items()}
 active=[frozenset(p) for r in seven['arc_pruning'] if r['id']==ident for p in r['remaining_partitions']]
 for T in [t for t in [1,2,4,8,16] if mu.get(t,0)]:
  pp=[p for p in active if T in p]
  pairs={frozenset([frozenset(z['P']),frozenset(z['Q'])]) for z in seven['results'] if z['id']==ident and z['T']==T and Q(z['bound'])>=1}
  subtotal=Counter()
  for a,b,c in product(pp,repeat=3):
   if all(frozenset([x,y]) in pairs for x,y in [(a,b),(a,c),(b,c)]):
    ps=tuple(sorted([tuple(sorted(x)) for x in [a,b,c]]));ns=direct(mu,ps,T,'111',None)
    if ns is not None:expected[(ident,T,'111',ps,None)]=ns
   if all(frozenset([x,c]) in pairs for x in [a,b]):
    ab=sorted([tuple(sorted(a)),tuple(sorted(b))]);ps=tuple(ab+[tuple(sorted(c))])
    for U in {0}|(a&b):
     if U&T or U.bit_count()>3:continue
     ns=direct(mu,ps,T,'211',U)
     if ns is not None:expected[(ident,T,'211',ps,U)]=ns
  subtotal=Counter(k[2] for k in expected if k[:2]==(ident,T));domain_statistics.append(dict(id=ident,T=T,mode111=subtotal['111'],mode211=subtotal['211'],total=sum(subtotal.values())))
actual={signature(z):{int(t):c for t,c in z['counts'].items()} for r in source['results'] for z in r['cases']}
assert len(actual)==source['summary']['cases']==227 and actual==expected
# Independently check the small paper tables and their loopless K3 premise.
paper={
 1:dict(parts=[(1,2,4,24),(1,10,20),(1,12,18)],rows=[('111',0,1,2,None),('211',0,0,1,2),('211',0,0,2,2),('211',0,1,2,0),('211',0,2,1,0),('211',1,1,0,20),('211',1,1,2,20),('211',1,2,0,0)]),
 9:dict(parts=[(1,2,12,16),(1,4,10,16),(1,6,8,16)],rows=[('111',0,1,2,None),('211',0,1,2,0),('211',0,1,2,16),('211',0,2,1,0),('211',0,2,1,16),('211',1,2,0,0),('211',1,2,0,16),('211',2,2,0,8),('211',2,2,1,8)])
}
for ident,tab in paper.items():
 pp=tab['parts'];active={tuple(p) for r in seven['arc_pruning'] if r['id']==ident for p in r['remaining_partitions'] if 1 in p}
 assert active==set(pp)
 edges={frozenset([tuple(sorted(z['P'])),tuple(sorted(z['Q']))]) for z in seven['results'] if z['id']==ident and z['T']==1 and Q(z['bound'])>=1 and tuple(sorted(z['P'])) in active and tuple(sorted(z['Q'])) in active}
 assert edges=={frozenset([pp[i],pp[j]]) for i in range(3) for j in range(i+1,3)}
 table_keys={(ident,1,mode,(pp[a],pp[b],pp[c]),U) for mode,a,b,c,U in tab['rows']}
 assert table_keys=={k for k in expected if k[:2]==(ident,1)}
records=[]
for z in complete['results']:
 assert z['T']==1 and signature(z) in expected
 bound=replay(z)
 assert all(Q(c['loss'])==0 for c in z['certificates'])
 uncorrected=sum(min(Q(r['A']),Q(r['B']),Q(r['C'])) for r in z['rows'])
 assert uncorrected==bound
 records.append(dict(id=z['id'],T=z['T'],mode=z['mode'],partitions=z['partitions'],U=z['U'],bound=str(bound),without_any_quota_deduction=str(uncorrected)))
assert len({signature(z) for z in complete['results']})==17
assert {signature(z) for z in complete['results']}=={k for k in expected if k[1]==1}
assert all(Q(z['bound'])<1 for z in records)
families=[]
for ident in [1,9]:
 zz=[z for z in records if z['id']==ident]
 families.append(dict(id=ident,selected_singleton=1,cases=len(zz),mode111=sum(z['mode']=='111' for z in zz),mode211=sum(z['mode']=='211' for z in zz),all_strict=True,maximum=str(max(Q(z['bound']) for z in zz))))
out=dict(scope=__doc__,passed=True,complete_local_domains=domain_statistics,domain_cases=227,replayed_selected_cases=17,all_selected_strict=True,no_quota_deduction_needed=True,families=families,results=records,elapsed_seconds=time.perf_counter()-st)
(P/'GROUP5_THREE_EXTERNAL_STARS_REPLAY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['passed','domain_cases','replayed_selected_cases','all_selected_strict','families','elapsed_seconds']},indent=2))
