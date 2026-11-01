import importlib.util,json,itertools,time
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent;ROOT=P.parents[2]
spec=importlib.util.spec_from_file_location('c',ROOT/'propertyB_small_k/propertyB_m6_certificate.py');c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c);c.M=66
start=time.process_time();rows=[];selection=[];adaptive=[]
def bound(v,ds,blocks,pos):
 ell={b:1 for b in blocks}
 for j,d in enumerate(ds):ell[1<<j]=d-sum(bool(b&(1<<j)) for b in blocks)
 ell[0]=66-sum(ell.values())
 if min(ell.values())<0:return None
 return c.profile_bound(v,pos,{t:n for t,n in ell.items() if n})
def unlocked(v):
 q=max(0,c.ceilings(990-c.C(v,2),10));g=66*65-2*q
 return sum(min(F(396,v)*F(c.C(h-1,5),c.C(v-1,5)),F(396,v)*F(c.C(v-h,5),c.C(v-1,5)),g*F(c.C(h-1,5)*c.C(v-h,5),v*c.C(v-1,5)*c.C(v-6,5))) for h in range(1,v+1))
def add(v,kind,ds,blocks,u,pos,source):
 r=dict(v=v,kind=kind,degrees=ds,blocks=blocks,U=str(u),strict=u<1,positions=pos,source=source);rows.append(r);return r
vdom=[v for v in range(11,100) if v*c.ceilings(v-1,5)<=396 and 66*F(c.C(v//2,6)+c.C(v-v//2,6),c.C(v,6))>=1]
for v in vdom:
 u=unlocked(v);add(v,'zero',[],[],u,[],'complete vertex domain')
 # Full min-degree adaptive one/two/conditional-three selection.
 if u<1:continue
 d0=c.ceilings(v-1,5)
 for d in range(d0,396//v+1):
  u=c.one(v,d);r=add(v,'one',[d],[],u,[v//2],'minimum degree')
  if u<1:continue
  n=2*(v-1)-5*d
  if n<=0:
   adaptive.append(dict(v=v,d=d,status='unit_partner_selection_gap',unit_pool_lower=n));continue
  B=d+(396-v*d)//n
  for e in range(d,B+1):
   vals=[(bound(v,[d,e],[3],p),p) for p in [(v//2,v//2+1),(v//2,v//2-1)]]
   u,pos=min(vals);r=add(v,'two',[d,e],[3],u,pos,'adaptive unit partner')
   if u<1:continue
   t=v-2-(5*d-(v-1))-(5*e-(v-1))
   if t<=0:
    adaptive.append(dict(v=v,d=d,e=e,status='third_unit_selection_gap',unit_common_pool_lower=t,two_U=str(u)));continue
   R=396-v*d-(e-d);Fmax=d+R//t
   failed=[]
   for f in range(d,Fmax+1):
    for blocks in ([3,5,6],[7]):
     ds=sorted([d,e,f]);p=(v//2-1,v//2,v//2+1);u=bound(v,ds,blocks,p)
     if u is None:continue
     add(v,'conditional_three',ds,blocks,u,p,'adaptive conditional third unit lock')
     if u>=1:failed.append(dict(f=f,blocks=blocks,U=str(u)))
   adaptive.append(dict(v=v,d=d,e=e,status='conditional_three_probability_gap' if failed else 'conditional_three_pass',F=Fmax,t=t,failures=failed))
# Uniform selection lemma, minimum threshold D for 3 or 4 units; all resulting profiles.
patterns4=[[3,5,6,9,10,12],[7,9,10,12],[11,5,6,12],[13,3,6,10],[14,3,5,9],[15]]
for v in vdom:
 if unlocked(v)<1:continue
 d0=c.ceilings(v-1,5)
 for s in (3,4):
  valid=[]
  for D in range(d0,67):
   Z=(D+1)*v-396;T=5*(D+1)-v+2
   if Z>0 and 20*Z>(s-1)*T*T:valid.append(D)
  if not valid:
   selection.append(dict(v=v,s=s,status='continuous_selection_gap'));continue
  D=min(valid);nrows=0;fails=[]
  # Stay bounded: >2500 types are not a cheap pilot.
  if c.C(D-d0+s,s)*(2 if s==3 else 6)>2500:
   selection.append(dict(v=v,s=s,D=D,status='table_not_attempted_size'));continue
  pats=([3,5,6],[7]) if s==3 else patterns4
  pos=tuple(range(v//2-1,v//2-1+s))
  for ds in itertools.combinations_with_replacement(range(d0,D+1),s):
   for blocks in pats:
    u=bound(v,ds,blocks,pos);nrows+=1
    add(v,'uniform'+str(s),ds,blocks,u,pos,'continuous low-degree selection')
    if u>=1:fails.append(dict(degrees=ds,blocks=blocks,U=str(u)))
  selection.append(dict(v=v,s=s,D=D,profiles=nrows,failures=fails,status='probability_gap' if fails else 'pass'))
res=dict(M=66,total_degree=396,vertex_domain=vdom,min_degree_domain={v:list(range(c.ceilings(v-1,5),396//v+1)) for v in vdom},balanced_max_through26=str(max(66*F(c.C(v//2,6)+c.C(v-v//2,6),c.C(v,6)) for v in range(11,27))),rows=rows,adaptive=adaptive,uniform=selection,cpu_seconds=time.process_time()-start)
(P/'RESULTS.json').write_text(json.dumps(res,indent=2))
print(json.dumps({k:v for k,v in res.items() if k not in ('rows','adaptive')},indent=2));print('adaptive unresolved',json.dumps([r for r in adaptive if r['status']!='conditional_three_pass'],indent=2))
