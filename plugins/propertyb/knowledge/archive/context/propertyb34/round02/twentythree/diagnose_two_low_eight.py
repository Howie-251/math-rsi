from pathlib import Path
exec((Path(__file__).with_name('diagnose_two_low_projection.py')).read_text().split('start=time.monotonic();summary=[]')[0])
from itertools import combinations
@lru_cache(None)
def copowers(key,n):
 ns=dict(key);ls=[(a,b,sum(v for t,v in ns.items()if t>>a&1 and t>>b&1))for a,b in combinations(range(n),2)]
 return tuple(sum(v**p for a,b,v in ls if int(a<2)+int(b<2)==r)for r in range(3)for p in [1,2,3,4])
@lru_cache(None)
def rooted(key,n):
 ns=dict(key)
 return tuple(sum(sum(v for t,v in ns.items()if t>>i&1 and (t&3).bit_count()==a and (t>>2).bit_count()==b)**p for i in range(n)if (i<2)==low) for low in [False,True]for a in range(3)for b in range(n-1)for p in [2,3])
@lru_cache(None)
def pairspectrum(key,n):
 ns=dict(key);sums={}
 for t,v in ns.items():
  for u,w in ns.items():
   k=((t&3).bit_count(),(t>>2).bit_count(),(u&3).bit_count(),(u>>2).bit_count(),(t&u&3).bit_count(),((t&u)>>2).bit_count())
   sums[k]=sums.get(k,0)+v*w
 return tuple(sorted(sums.items()))
n=5;ds=[6,6,7,7,7]
old=json.loads((SRC/'FEW_LOW23_2_3.json').read_text());oldrows=[r for r in old['results']if F(r['final_bound'])>=1]
keys=[tuple(sorted((int(t),v)for t,v in r['counts'].items()if v))for r in oldrows]
inv={moments(k,n,2)for k in keys};extras=[]
features=[copowers,rooted,pairspectrum];validsets=[{(moments(k,n,2),fn(k,n))for k in keys}for fn in features];left=[0]*3
for r in oldrows:
 ns={int(t):v for t,v in r['counts'].items()}
 for row in extensions(ns,n,23,new_degree=7,max_extra=6,old_degrees=ds,codegree_caps=[1,1,3,3,3]):
  ps=[tuple(sorted((t,v)for t,v in project(row,tuple(i for i in range(n+1)if i!=x)).items()if v))for x in range(2,n+1)]
  if not all(moments(p,n,2)in inv for p in ps):continue
  for j,fn in enumerate(features):
   left[j]+=all((moments(p,n,2),fn(p,n))in validsets[j]for p in ps)
print(dict(moment_survivors=180,exact=172,feature_survivors=dict(zip([fn.__name__ for fn in features],left))))
(HERE/'TWO_LOW_EIGHT_DIAGNOSIS.json').write_text(json.dumps(dict(moment_survivors=180,exact=172,feature_survivors=dict(zip([fn.__name__ for fn in features],left))),indent=2)+'\n')
