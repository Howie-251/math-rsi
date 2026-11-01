import importlib.util,json,itertools,time
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent; ROOT=P.parents[2]
s=importlib.util.spec_from_file_location('av',ROOT/'context/propertyb-m6-66-20261029/avoided/verify.py');av=importlib.util.module_from_spec(s);s.loader.exec_module(av);c=av.c;c.M=66
start=time.process_time();rows=[];branches=[]
def ell_for(ds,blocks):
 ell={b:1 for b in blocks}
 for j,d in enumerate(ds):ell[1<<j]=d-sum(bool(b&(1<<j)) for b in blocks)
 ell[0]=66-sum(ell.values());return {t:n for t,n in ell.items() if n}
def bound(v,pos,ell):
 dels={pos[j]:av.deletion(v,pos,ell,j) for j in range(len(pos))};total=F(0)
 for h in range(1,v+1):
  A=sum(n*c.endpoint(v,pos,h,T,True) for T,n in ell.items());B=sum(n*c.endpoint(v,pos,h,T,False) for T,n in ell.items());Q=sum(n*(m-(T==U))*c.weight(v,pos,h,T,U) for T,n in ell.items() for U,m in ell.items());total+=min(A,B,Q-dels.get(h,F(0)))
 return total
def best(v,ds,blocks):
 ans=None
 for shift in (0,-1,1,-2):
  pos=tuple(range(v//2-1+shift,v//2-1+shift+len(ds)))
  for perm in sorted(set(itertools.permutations(ds))):
   ell=ell_for(perm,blocks);u=bound(v,pos,ell)
   row=dict(v=v,degrees=ds,blocks=blocks,assigned=perm,positions=pos,U=str(u),strict=u<1)
   if ans is None or u<F(ans['U']):ans=row
   if u<1:return row
 return ans
for v in range(34,39):
 for d in range(c.ceilings(v-1,5),396//v+1):
  n=2*(v-1)-5*d;emax=d+(396-v*d)//n
  for e in range(d,emax+1):
   r=best(v,[d,e],[3]);rows.append(r)
   if r['strict']:branches.append(dict(v=v,d=d,e=e,status='two_pass'));continue
   t=n-1-(5*e-(v-1))
   if t<=0:branches.append(dict(v=v,d=d,e=e,status='pool_gap',t=t));continue
   # y is chosen minimum-degree in the actual unit-neighbor pool of x.
   budget=396-v*d-n*(e-d)
   fmax=e+budget//t
   fails=[];count=0
   for f in range(e,fmax+1):
    for blocks in ([3,5,6],[7]):
     r=best(v,[d,e,f],blocks);rows.append(r);count+=1
     if not r['strict']:fails.append(r)
   branches.append(dict(v=v,d=d,e=e,n=n,t=t,fmax=fmax,budget=budget,status='three_gap' if fails else 'three_pass',count=count,failures=fails))
result=dict(rows=rows,branches=branches,cpu_seconds=time.process_time()-start,stats=av.stats)
(P/'ADAPTIVE.json').write_text(json.dumps(result,indent=2))
for v in range(34,39):
 print('v',v,'branches',sum(b['v']==v for b in branches),'gaps',[(b['d'],b['e'],b.get('fmax'),b['status'],len(b.get('failures',[]))) for b in branches if b['v']==v and b['status'] not in ('two_pass','three_pass')])
print('CPU',result['cpu_seconds'])
