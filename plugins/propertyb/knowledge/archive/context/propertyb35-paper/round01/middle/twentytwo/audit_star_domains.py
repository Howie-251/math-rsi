"""Independent RGS-partition/Mobius check of the 13 and379 actual unit-star domains.
Expanded-edge injection replay of the six strict all-unit neighbour triples.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations,product
from math import comb
import sys,json,time
HERE=Path(__file__).parent;ROOT=HERE.parents[4]
sys.dont_write_bytecode=True
sys.path.insert(0,str(ROOT/'computations'))
from independent_structure_bounds import independent_rows,injection_probability

def partitions(n):
 for a in product(range(n),repeat=n):
  if a[0]!=0:continue
  if any(a[i]>max(a[:i])+1 for i in range(1,n)):continue
  yield [sum(1<<i for i,b in enumerate(a) if b==j) for j in range(max(a)+1)]
def inverse(center,s,ps,blocks,hi):
 I={1<<i:8 for i in range(s)}
 I.update({(1<<a)|(1<<b):c for (a,b),c in zip(combinations(range(s),2),ps)});I.update(hi)
 ns={1:center-len(blocks),**{1+(B<<1):1 for B in blocks}}
 for t in range(1,1<<s):
  z=Q()
  for u in range(1,1<<s):
   if u&t!=t:continue
   incidence=I[u]-sum(u&B==u for B in blocks)
   z+=(-1)**(u.bit_count()-t.bit_count())*incidence
  assert z.denominator==1
  if z<0:return None
  ns[t<<1]=int(z)
 ns[0]=35-sum(ns.values())
 if ns[0]<0:return None
 return {t:n for t,n in ns.items() if n}
def key(ns):return tuple(sorted((int(t),n) for t,n in ns.items() if n))
def audit():
 start=time.time();old3=json.loads((HERE/'STAR_THREE.json').read_text())['cases'];old4=json.loads((HERE/'STAR_FOUR_DOMAIN.json').read_text())['cases']
 expected3=set()
 for ps in [(1,1,1),(1,1,2)]:
  for blocks in partitions(3):
   for t in range(2):
    ns=inverse(7,3,ps,blocks,{7:t})
    if ns is not None:expected3.add((tuple(ps),key(ns)))
 assert expected3=={(tuple(z['neighbor_codegrees']),key(z['counts'])) for z in old3} and len(expected3)==13
 expected4=set();graphs={}
 for z in old4:graphs[z['graph']]=z['neighbor_codegrees']
 for name,ps in graphs.items():
  for blocks in partitions(4):
   for ts in product(range(4),repeat=4):
    for q in range(4):
     hi=dict(zip((7,11,13,14),ts));hi[15]=q
     ns=inverse(7,4,ps,blocks,hi)
     if ns is not None:expected4.add((name,key(ns)))
 assert expected4=={(z['graph'],key(z['counts'])) for z in old4} and len(expected4)==379
 # Independently compute the six sufficient all-unit-star certificate values.
 checked=[]
 for r in old3:
  if r['neighbor_codegrees']!=[1,1,1]:continue
  ns={int(t):n for t,n in r['counts'].items() if n};pos=tuple(r['positions']);s=4;N=18
  types=[frozenset(i+1 for i in range(s) if t>>i&1) for t,n in ns.items() for _ in range(n)]
  rr=independent_rows(22,pos,types)
  # Loss independently reconstructed from unlabelled inventory and nested quotas.
  deductions={}
  for i,c in enumerate(r['quotas']):
   bit=1<<i;k=pos[i];left=sum(1<<j for j,p in enumerate(pos) if p<k);right=sum(1<<j for j,p in enumerate(pos) if p>k)
   a=k-1-left.bit_count();b=22-k-right.bit_count();ts=sorted(t for t in ns if t&bit);inv=[]
   def w(t,u):
    if t&u!=bit or (t^bit)&~left or (u^bit)&~right:return Q()
    return injection_probability(N,a,b,5-t.bit_count(),5-u.bit_count(),False)
   for j,t in enumerate(ts):
    for u in ts[j:]:
     cap=comb(ns[t],2) if t==u else ns[t]*ns[u]
     if cap:inv.append([w(t,u)+w(u,t),cap,t==u==bit,t,u])
   degree=sum(ns[t] for t in ts);qt=(4*degree-21+2)//3;qp=max(0,(4*ns.get(bit,0)-N+2)//3)
   assert qt==c['q_total'] and qp==c['q_pure'];remaining=qp;loss=Q()
   for z in sorted(inv):
    if z[2]:
     n=min(remaining,z[1]);remaining-=n;z[1]-=n;loss+=n*z[0]
   assert remaining==0
   remaining=max(0,qt-qp)
   for z in sorted(inv):
    n=min(remaining,z[1]);remaining-=n;loss+=n*z[0]
   assert remaining==0 and loss==Q(c['loss']);deductions[k]=loss
  value=sum((min(z['A'],z['B'],z['C']-deductions.get(z['k'],Q())) for z in rr),Q())
  assert value==Q(r['bound'])<1;checked.append(str(value))
 result=dict(status='PASS',scope=__doc__,three_domain=13,four_domain=379,all_unit_certificates=checked,rows_recomputed=6*22,elapsed_seconds=time.time()-start)
 (HERE/'STAR_AUDIT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':audit()
