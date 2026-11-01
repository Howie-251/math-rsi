"""Inspect existing exact domains; no probability/layout search."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import permutations,product
import json,sys,time
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).resolve().parent;SRC=ROOT/'context/propertyb34/round01/middle-math'
sys.dont_write_bytecode=True;sys.path.insert(0,str(SRC))
import ast
for name, wanted in [('extend_low.py',{'extensions','project'}),('extend_mixed22.py',{'role_permutations','canonical'})]:
 tree=ast.parse((SRC/name).read_text());tree.body=[node for node in tree.body if isinstance(node,ast.FunctionDef) and node.name in wanted]
 exec(compile(tree,str(SRC/name),'exec'))
@lru_cache(None)
def moments(key,s,powers):
 ns=dict(key)
 return tuple(sum(v**p for t,v in ns.items()if (t&3).bit_count()==a and (t>>2).bit_count()==b)for a in range(3)for b in range(s-1)for p in range(1,powers+1))
start=time.monotonic();summary=[]
for h in [3,4,5]:
 old=json.loads((SRC/f'FEW_LOW23_2_{h-1}.json').read_text());oldrows=[r for r in old['results']if F(r['final_bound'])>=1];n=h+1;ds=[6,6]+[7]*(h-1)
 goodkeys={canonical({int(t):v for t,v in r['counts'].items()},ds)for r in oldrows}
 invariant=[{moments(tuple(sorted((int(t),v)for t,v in r['counts'].items()if v)),n,p)for r in oldrows}for p in [1,2,3]]
 counts=[0,0,0];extra=[0,0,0];raw=0;exact=0
 for r in oldrows:
  ns={int(t):v for t,v in r['counts'].items()}
  for row in extensions(ns,n,23,new_degree=7,max_extra=6,old_degrees=ds,codegree_caps=[1,1]+[3]*(n-2)):
   raw+=1;projections=[project(row,tuple(i for i in range(n+1)if i!=x))for x in range(2,n+1)]
   exactok=all(canonical(pro,ds)in goodkeys for pro in projections);exact+=exactok
   for j,p in enumerate([1,2,3]):
    valid=all(moments(tuple(sorted((t,v)for t,v in pro.items()if v)),n,p)in invariant[j]for pro in projections)
    counts[j]+=valid;extra[j]+=valid and not exactok
 summary.append(dict(new_highs=h,raw=raw,exact=exact,role_moment_survivors=counts,extra_over_exact=extra));print(summary[-1],flush=True)
(HERE/'TWO_LOW_PROJECTION_DIAGNOSIS.json').write_text(json.dumps(dict(results=summary,elapsed=time.monotonic()-start,scope='existing exact domain and necessary moment filters; no new probability certificate'),indent=2)+'\n')
