"""CaseB single-G forced interfaces only, degree spectrum6^2,8^2,7^21.
New low-point single stars, selected positive-trace pairs and the two global
D=1 eight-degree points; no free mixed external-point domain is enumerated.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction as Q
import json,sys,time
P=Path(__file__).resolve().parent;root=P.parents[3];sys.dont_write_bytecode=True;sys.path[:0]=[str(root/'context/propertyb34/round01/high-math'),str(root/'computations'),str(root/'computations/propertyb33/round01')]
from subset_position_dp import SubsetEngine
from multilock import json_value
cat=json.loads((P/'GROUP5_CATALOGUE.json').read_text());old=json.loads((P/'K5_SINGLE_COMPONENT_REPLAY.json').read_text());selection=json.loads((P/'MIXED_ONE_SIX_K5_SELECTION_CHECK.json').read_text());st=time.perf_counter();cases={}
def put(ident,ds,p,r=None,q=None,caller=None):
 mu={int(t):n for t,n in cat['representatives'][ident]['counts'].items()};x={t:1 for t in p};x[0]=ds[5]-len(p);ns={};q=q or {}
 if r is None:
  for t,n in mu.items():
   a=x.get(t,0)
   if not 0<=a<=n:return
   if n-a:ns[t]=n-a
   if a:ns[t+32]=a
 else:
  y={t:1 for t in r};y[0]=ds[6]-len(r)
  for t,n in mu.items():
   a=x.get(t,0);b=y.get(t,0);c=q.get(t,0);cells=[n-a-b+c,a-c,b-c,c]
   if min(cells)<0:return
   for mask,v in enumerate(cells):
    if v:ns[t+32*mask]=v
 assert sum(ns.values())==35 and all(t.bit_count()<=5 for t in ns)
 assert all(sum(n for t,n in ns.items() if t>>i&1)==d for i,d in enumerate(ds))
 for i in range(len(ds)):
  for j in range(i+1,len(ds)):
   lam=sum(n for t,n in ns.items() if t>>i&1 and t>>j&1);assert lam==(sum(q.values()) if (i,j)==(5,6) else 2 if j<5 else 1)
   if ds[i]==6 or ds[j]==6:assert lam==1
 key=(ident,tuple(ds),tuple(sorted(ns.items())));cases[key]=dict(id=ident,degrees=ds,P=p,Q=r,joint=q,caller=caller,counts=ns)
def parts(ident,T):
 mu={int(t):n for t,n in cat['representatives'][ident]['counts'].items()};comp=31^T;out=[]
 if mu.get(comp):out.append((T,comp))
 ss=[1<<i for i in range(5) if comp>>i&1]
 if all(mu.get(t) for t in ss):out.append(tuple([T]+ss))
 return out
def allpairs(ident,T,d,e,ps,caller):
 mu={int(t):n for t,n in cat['representatives'][ident]['counts'].items()}
 for pp,rr in product(ps,repeat=2):
  p={t:1 for t in pp};r={t:1 for t in rr};p[0]=d-len(pp);r[0]=e-len(rr);common=sorted(set(p)&set(r));ranges=[[1] if t==T else range(max(0,p[t]+r[t]-mu[t]),min(p[t],r[t])+1) for t in common]
  for vv in product(*ranges):
   q={t:n for t,n in zip(common,vv) if n};lam=sum(q.values());upper=9 if d==e==8 else 5
   if not (lam==1 if d==6 else 1<=lam<=upper):continue
   put(ident,[7]*5+[d,e],pp,rr,q,caller)
# If all two strict-triple edges lack a seven-degree endpoint, all four special
# points are used, hence a six-degree endpoint exists on one of these traces.
for ident in [11,13,17]:
 f=next(f for f in selection['old_sixlock_classes_transferred'] if f['id']==ident)
 for T in f['strict_three_traces']:
  for pp in parts(ident,T):put(ident,[7]*5+[6],pp,caller='old_strict_triple_six_endpoint')
# For forced-star classes, six endpoints are impossible and an orbit of two
# triple edges has four distinct endpoints; two eights cannot occupy all four.
for ident in [1,5,8,10]:
 T=next(f['T'] for f in old['families'] if f['id']==ident);allpairs(ident,T,7,8,parts(ident,T),'triple_orbit_at_least_one_seven')
# Four triple edges let us avoid both eights; remaining new endpoints use6.
for ident in [7,9]:
 T=next(f['T'] for f in old['families'] if f['id']==ident)
 for d,e in [(6,6),(6,7)]:allpairs(ident,T,d,e,parts(ident,T),'four_triple_edges_avoid_both_eights')
# Two triple edges always allow a pair other than8/8.
T=22
for d,e in [(6,8),(7,8)]:allpairs(26,T,d,e,parts(26,T),'two_triple_edges_avoid_double_eight')
# Global D=1 special points might be the two eights, with either V type.
mu={int(t):n for t,n in cat['representatives'][12]['counts'].items()}
for pp,rr in product([(5,26),(3,28)],repeat=2):
 p={t:1 for t in pp};r={t:1 for t in rr};p[0]=r[0]=6;common=sorted(set(p)&set(r));ranges=[range(max(0,p[t]+r[t]-mu[t]),min(p[t],r[t])+1) for t in common]
 for vv in product(*ranges):
  q={t:n for t,n in zip(common,vv) if n}
  if 1<=sum(q.values())<=9:put(12,[7]*5+[8,8],pp,rr,q,'global_D_one_eights')
allpairs(24,28,8,8,[(1,2,28),(3,28)],'unique_triple_double_eight')
out=[]
for z in cases.values():
 eng=SubsetEngine(25,len(z['degrees']),z['counts']);w=eng.verify(eng.solve());raw=sum(min(r['A'],r['B'],r['C']) for r in w['rows']);out.append(dict(**{k:v for k,v in z.items() if k!='counts'},raw_ABC_bound=raw,**w))
ids=sorted({z['id'] for z in out});summary=dict(scope=__doc__,cases=len(out),raw_strict=sum(z['raw_ABC_bound']<1 for z in out),corrected_strict=sum(z['bound']<1 for z in out),maximum_raw=max(z['raw_ABC_bound'] for z in out),by_type=[dict(id=i,cases=sum(z['id']==i for z in out),raw_strict=sum(z['id']==i and z['raw_ABC_bound']<1 for z in out),maximum_raw=max(z['raw_ABC_bound'] for z in out if z['id']==i)) for i in ids],elapsed_seconds=time.perf_counter()-st)
(P/'MIXED_TWO_SIX_K5_B_PILOT.json').write_text(json.dumps(json_value(dict(summary=summary,results=out)),indent=2)+'\n');print(json.dumps(json_value(summary),indent=2))
