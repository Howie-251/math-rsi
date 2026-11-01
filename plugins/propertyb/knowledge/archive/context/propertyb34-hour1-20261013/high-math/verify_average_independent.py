"""Independent expanded-stub and falling-injection replay of successful averages."""
from pathlib import Path
from fractions import Fraction
from itertools import permutations
from math import comb
import sys,json,time
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'computations'))
from independent_structure_bounds import independent_rows,injection_probability
from multilock import json_value
start=time.perf_counter();out=[];here=Path(__file__).parent

def verify(x):
 ns={int(t):n for t,n in x['counts'].items()};pos=tuple(x['positions']);s=len(pos);v=24;N=v-s
 trans=lambda t,p:sum(1<<p[i] for i in range(s) if t&(1<<i))
 ps=x.get('used_auto') or list(permutations(range(s)));sums=[[Fraction() for _ in z['slots']] for z in x['centers']];free=Fraction();cache={};count=0
 def w(t,u,j):
  k=pos[j];bit=1<<j;left=sum(1<<i for i in range(s) if pos[i]<k);right=sum(1<<i for i in range(s) if pos[i]>k)
  if t&u!=bit or (t^bit)&~left or (u^bit)&~right:return Fraction()
  a=k-1-left.bit_count();b=v-k-right.bit_count();return injection_probability(N,a,b,5-t.bit_count(),5-u.bit_count(),False)
 for perm in ps:
  count+=1;counts={trans(t,perm):n for t,n in ns.items()};key=tuple(sorted(counts.items()))
  if key not in cache:
   stubs=[frozenset(i+1 for i in range(s) if t&(1<<i)) for t,n in counts.items() for _ in range(n)];cache[key]=independent_rows(v,pos,stubs)
  rs=cache[key];free+=sum((r['bound'] for r in rs if r['k'] not in pos),Fraction())
  for i,z in enumerate(x['centers']):
   j=perm[i];r=rs[pos[j]-1]
   for n,(t,u) in enumerate(z['slots']):
    mt,mu=trans(t,perm),trans(u,perm);loss=w(mt,mu,j)+w(mu,mt,j);assert loss<=r['C'];sums[i][n]+=min(r['A'],r['B'],r['C']-loss)
 assert free/count==Fraction(x['free_average'])
 for z,ss in zip(x['centers'],sums):
  assert [a/count for a in ss]==[Fraction(a) for a in z['averages']]
  assert max(ss)/count==Fraction(z['maximum'])
 b=(free+sum(max(ss) for ss in sums))/count;assert b==Fraction(x['bound'])<1
 return dict(group=x.get('group'),s=s,bound=b,permutations=count,distinct_expanded_type_rows=len(cache),independent_injections=True)

sources=[('SIX_LOW_ACTUAL_AVERAGE.json','results'),('AUTOMORPHISM_AVERAGE.json','results'),('SEVEN_AUTO_AVERAGE.json','results')]
for filename,key in sources:
 for x in json.loads((here/filename).read_text())[key]:
  if Fraction(x['bound'])<1:
   z=verify(x);out.append(dict(source=filename,**z));print(out[-1],flush=True)
p=json.loads((here/'SEVEN_LOW_AVERAGE.json').read_text())
for g in p['groups']:
 if Fraction(g['best']['bound'])<1:
  z=verify(dict(group=g['group'],**g['best']));out.append(dict(source='SEVEN_LOW_AVERAGE.json',**z));print(out[-1],flush=True)
(here/'AVERAGE_INDEPENDENT.json').write_text(json.dumps(json_value(dict(elapsed=time.perf_counter()-start,results=out)),indent=2)+'\n')
