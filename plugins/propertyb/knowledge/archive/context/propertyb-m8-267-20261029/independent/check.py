"""Independent k8 injection probabilities, recursive component DP, full domains."""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial,comb
from functools import lru_cache
from itertools import combinations,combinations_with_replacement
import json,time
P=Path(__file__).resolve().parent;BASE=P.parent
K,M,DEG=8,266,2128

def ceil(a,b):return -(-a//b)
@lru_cache(None)
def fall(n,r):return factorial(n)//factorial(n-r)if 0<=r<=n else 0
@lru_cache(None)
def prob(v,pos,h,T,U=-1):
 N=v-len(pos);left=sum(t<h for t in range(1,v+1)if t not in pos);right=N-left-(h not in pos)
 lo=sum(1<<j for j,p in enumerate(pos)if p<h);hi=sum(1<<j for j,p in enumerate(pos)if p>h);bit=(1<<pos.index(h))if h in pos else 0;a=K-T.bit_count()
 if U<0:
  result=[]
  for cap,mask in((left,lo),(right,hi)):
   if bit:value=Q(fall(cap,a),fall(N,a))if T&bit and not T&~(mask|bit)else Q(0)
   else:value=Q(a*fall(cap,a-1),fall(N,a))if a>0 and not T&~mask else Q(0)
   result.append(value)
  return tuple(result)
 b=K-U.bit_count()
 if bit:
  if T&U!=bit or T&~(lo|bit)or U&~(hi|bit)or a+b>N:return Q(0)
  return Q(fall(left,a)*fall(right,b),fall(N,a+b))
 if T&~lo or U&~hi or min(a,b)==0 or a+b-1>N:return Q(0)
 return Q(fall(left,a-1)*fall(right,b-1),fall(N,a+b-1))

@lru_cache(None)
def min_support(f,q):
 if f==0:return 0
 best=7*f
 for t in range(1,f+1):
  for e in range(t-1,min(comb(t,2),q)+1):
   support=7 if t==1 else max(8,7*ceil(t*t,t+2*e),7*ceil(2*t-e-1,2),15 if comb(t,2)-e>t//2 else 0)
   best=min(best,support+min_support(f-t,q-e))
 return best
@lru_cache(None)
def quota(f,N):
 q=0
 while min_support(f,q)>N:q+=1
 return q

def deduction(v,pos,ell,j,component):
 typ=[T for T,n in ell.items()if n and T>>j&1];cells=[]
 for a,T in enumerate(typ):
  for U in typ[a:]:
   capacity=comb(ell[T],2)if T==U else ell[T]*ell[U]
   if capacity:cells.append((prob(v,pos,pos[j],T,U)+prob(v,pos,pos[j],U,T),capacity,T|U))
 costs=[];Rs=range(1<<len(pos))if component else(0,)
 for R in Rs:
  if R>>j&1:continue
  f=sum(n for T,n in ell.items()if T>>j&1 and not T&R);N=v-1-R.bit_count();need=quota(f,N)if component else max(0,ceil(7*f-N,6));cost=Q(0)
  for w,cap,U in sorted(cells):
   if U&R:continue
   take=min(need,cap);cost+=take*w;need-=take
  assert need==0
  costs.append(cost)
 return max(costs)

def bound(v,pos,ell,component):
 pos=tuple(pos);D={pos[j]:deduction(v,pos,ell,j,component)for j in range(len(pos))};out=Q(0)
 for h in range(1,v+1):
  A=sum(n*prob(v,pos,h,T)[0]for T,n in ell.items());B=sum(n*prob(v,pos,h,T)[1]for T,n in ell.items());C=sum(n*(m-(T==U))*prob(v,pos,h,T,U)for T,n in ell.items()for U,m in ell.items())
  assert C>=D.get(h,0);out+=min(A,B,C-D.get(h,0))
 return out

def ell_for(ds,blocks):
 ell={b:1 for b in blocks}
 for j,d in enumerate(ds):ell[1<<j]=d-sum(bool(b>>j&1)for b in blocks)
 ell[0]=M-sum(ell.values());assert min(ell.values())>=0
 return{T:n for T,n in ell.items()if n}

def unit_partitions4():
 # First-uncovered-pair recursion, distinct from authorclique subsetscan.
 pairs=list(combinations(range(4),2));cliques=[(b,tuple(k for k,(a,c)in enumerate(pairs)if b>>a&1 and b>>c&1))for b in range(1,16)if b.bit_count()>=2]
 @lru_cache(None)
 def rec(mask):
  if mask==63:return frozenset({()})
  pivot=next(k for k in range(6)if not mask>>k&1);out=set()
  for b,used in cliques:
   bits=sum(1<<k for k in used)
   if pivot in used and not mask&bits:out.update(tuple(sorted((b,*tail)))for tail in rec(mask|bits))
  return frozenset(out)
 return rec(0)

def main():
 start=time.process_time();data=json.loads((BASE/'CERTIFICATE.json').read_text());rows=data['rows'];expected=set();table={};replay=[]
 for r in rows:
  ds=tuple(r.get('degrees',()));tri=r.get('tri');blocks=tuple(sorted(r.get('blocks',())))
  key=(r['v'],r['kind'],ds,tri,blocks);assert key not in table;table[key]=r
 # Full originalinput necessaryv domain and balancedbound.
 balanced=[]
 for v in range(15,47):
  p=Q(266*(comb(v//2,8)+comb(v-v//2,8)),comb(v,8));assert p<1;balanced.append((v,str(p)))
 assert 120*ceil(119,7)<=DEG and 121*ceil(120,7)>DEG
 for v in range(47,121):assert v*ceil(v-1,7)<=DEG
 for v in range(47,83):expected.add((v,'zero',(),None,()))
 for v in range(83,90):
  for d in range(ceil(v-1,7),DEG//v+1):expected.add((v,'one',(d,),None,()))
 adaptive_parents=[]
 for v in range(90,108):
  for d in range(ceil(v-1,7),DEG//v+1):
   n=2*(v-1)-7*d;assert n>0;B=d+(DEG-v*d)//n
   assert v*d+n*(B+1-d)>DEG
   for e in range(d,B+1):
    key=(v,'two',(d,e),None,())
    if key in table:expected.add(key);continue
    t=n-1-(7*e-v+1);assert t>0;left=DEG-v*d-n*(e-d);F=e+left//t
    assert v*d+n*(e-d)+t*(F+1-e)>DEG
    adaptive_parents.append(dict(v=v,d=d,e=e,common_unit_pool=t,third_upper=F))
    for f in range(e,F+1):
     for tri in(0,1):expected.add((v,'adaptive_three',(d,e,f),tri,()))
 for v in range(108,120):
  Z=21*v-DEG;T=149-v;assert Z>0 and 14*Z>T*T
  for ds in combinations_with_replacement(range(ceil(v-1,7),21),3):
   for tri in(0,1):expected.add((v,'three',ds,tri,()))
 patterns=unit_partitions4();assert len(patterns)==6 and 18*120-DEG==32 and 7*17==119
 for bs in patterns:expected.add((120,'four17',(17,)*4,None,bs))
 assert set(table)==expected,(len(set(table)-expected),len(expected-set(table)))
 for r in rows:
  v=r['v'];kind=r['kind'];ds=r.get('degrees',());pos=tuple(r.get('positions',()))
  if kind=='zero':
   gamma=M*(M-1)-2*max(0,ceil(M*28-comb(v,2),21));u=sum(min(M*prob(v,(),h,0)[0],M*prob(v,(),h,0)[1],gamma*prob(v,(),h,0,0))for h in range(1,v+1));ell={0:M}
  else:
   if kind=='one':ell=ell_for(ds,[])
   elif kind=='two':ell=ell_for(ds,[3])
   elif kind in('three','adaptive_three'):ell=ell_for(ds,[7]if r['tri']else[3,5,6])
   else:ell=ell_for(ds,r['blocks'])
   assert ell=={int(T):n for T,n in r['ell'].items()if n}
   assert len(set(pos))==len(ds)and all(1<=h<=v for h in pos)
   u=bound(v,pos,ell,r['deletion']=='component_max_R')
  assert u==Q(r['U'])<1,(r,u)
  replay.append(dict(v=v,kind=kind,degrees=ds,tri=r.get('tri'),blocks=r.get('blocks'),U=str(u),positions=pos))
  if not any(x['v']==v for x in rows[rows.index(r)+1:]):prob.cache_clear()
 # Everyactual quota argument is rebuilt by another DPand mustmatch.
 for q in data['quotas']:assert quota(q['f'],q['N'])==q['q']
 out=dict(status='PASS_WITH_DECLARED_IMPORTS',review_independence='same-family',acceptance_status='provisional',scope='Complete47..120 actualdegree/partner/tracedomain plus full2094row independentk8 injection replay',k=8,M=266,profiles=len(replay),component_quota_arguments=len(data['quotas']),adaptive_parents=adaptive_parents,balanced=balanced,maximum=str(max(Q(r['U'])for r in replay)),cpu_seconds=time.process_time()-start,rows=replay)
 (P/'CHECK.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items()if k not in('rows','adaptive_parents','balanced')},indent=2))
if __name__=='__main__':main()
