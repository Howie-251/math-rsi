from pathlib import Path
from fractions import Fraction as F
from itertools import permutations
import json
ROOT=Path(__file__).resolve().parents[4];SRC=ROOT/'context/propertyb34/round01/middle-math'
def image(t,p):return sum(1<<p[i]for i in range(len(p))if t>>i&1)
def key(ns):return tuple(sorted((t,k)for t,k in ns.items()if k))
def orbit(rows,n):return {key({image(t,p):k for t,k in ns.items()}):q for q,ns in enumerate(rows)for p in permutations(range(n))}
def proj(ns,n,x):
 out={};keep=[i for i in range(n)if i!=x]
 for t,k in ns.items():
  u=sum(1<<j for j,i in enumerate(keep)if t>>i&1);out[u]=out.get(u,0)+k
 return out
def invariant(ns,n,p):
 return tuple(sum(k**power for t,k in ns.items()if t.bit_count()==j)for j in range(n+1)for power in range(1,p+1))
def rooted(ns,n):
 return tuple(sorted(tuple(sum(k for t,k in ns.items()if t>>i&1 and t.bit_count()==j)for j in range(1,n+1))for i in range(n)))
n=4
oldrows=json.loads((SRC/'FOUR_LOW_23.json').read_text())['results'];old=[{int(t):k for t,k in r['counts'].items()if k}for r in oldrows if min(F(r['bound']),F(r.get('joint',r)['bound']))>=1]
rows=json.loads((SRC/'EXTEND_LOW_23_5.json').read_text())['results'];new=[{int(t):k for t,k in r['counts'].items()if k}for r in rows];neworbit=orbit(new,5)
methods={f'moments_{p}':lambda ns,p=p:invariant(ns,n,p)for p in [1,2,3,4,5]}
methods['rooted_plus_card']=lambda ns:(invariant(ns,n,1),rooted(ns,n))
methods['rooted_plus_moments']=lambda ns:(invariant(ns,n,2),rooted(ns,n))
sets={k:{fun(ns)for ns in old}for k,fun in methods.items()};stats={k:dict(surviving=0,outside_new=0)for k in methods}
for ns in old:
 es=[(t,k)for t,k in sorted(ns.items())if t]
 def rec(i,used,lams,total,vs):
  if i<len(es):
   t,k=es[i];cap=min(k,6-used,*[3-lams[j]for j in range(n)if t>>j&1],(n+2-total)//t.bit_count())
   for v in range(cap+1):rec(i+1,used+v,[a+v if t>>j&1 else a for j,a in enumerate(lams)],total+v*t.bit_count(),vs+[v])
   return
  out=dict(ns)
  for(t,k),v in zip(es,vs):out[t]-=v;out[t|(1<<n)]=v
  p0=6-sum(vs);out[0]-=p0;out[1<<n]=p0
  co=[[sum(k for t,k in out.items()if t>>i&1 and t>>j&1)for j in range(n+1)]for i in range(n+1)]
  if any(co[i][j]<1 for i in range(n+1)for j in range(n+1)if i!=j):return
  if any(sum(co[i][j]-1 for j in range(n+1)if i!=j)>2 for i in range(n+1)):return
  for method,fun in methods.items():
   if all(fun(proj(out,n+1,x))in sets[method]for x in range(n+1)):
    stats[method]['surviving']+=1;stats[method]['outside_new']+=key(out)not in neworbit
 rec(0,0,[0]*n,0,[])
print(json.dumps(stats,indent=2))
Path(__file__).with_suffix('.json').write_text(json.dumps(stats,indent=2)+'\n')
