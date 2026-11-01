"""Nine-unit mixed-lock diagnostic on two explicit local type families, not complete classification."""
from pathlib import Path
from itertools import combinations
from fractions import Fraction
import sys,json,time,random
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[3];sys.path[:0]=[str(ROOT/'computations'),str(ROOT/'computations/propertyb33/round01'),str(Path(__file__).parent)]
from multilock import Profile,rows,total_bound,json_value
from pure_quota import certificate
from position_dp import solve
rng=random.Random(341325)

def make_counts(triples,q=5):
 pairsets=[frozenset(p) for b in triples for p in combinations(b,2)];assert len(pairsets)==len(set(pairsets))
 ns={sum(1<<i for i in b):1 for b in triples}
 for p in combinations(range(9),2):
  if frozenset(p) not in pairsets:ns[sum(1<<i for i in p)]=1
 for i in range(9):ns[1<<i]=(6 if i<q else 7)-sum(n for t,n in ns.items() if t&(1<<i))
 ns[0]=34-sum(ns.values());assert min(ns.values())>=0
 return {t:n for t,n in ns.items() if n}

def evaluate(triples,q=5):
 counts=make_counts(triples,q);pos=tuple(range(9,18));p=Profile(25,5,pos,counts);cs=[certificate(p,i) for i in range(9)];rs=rows(p,deductions={pos[i]:cs[i]['loss'] for i in range(9)});b=total_bound(rs)
 z=solve(25,counts,9) if b>=1 else dict(bound=b,positions=pos,counts=counts,certificates=cs,rows=rs)
 return dict(triples=triples,q=q,**z)

start=time.perf_counter();out=[]
ag=[]
for m in range(3):
 for b in range(3):ag.append(tuple(3*x+(m*x+b)%3 for x in range(3)))
for b in range(3):ag.append(tuple(3*b+y for y in range(3)))
for q in (5,6,7,8,9):
 z=evaluate(ag,q);out.append(z);print('ag',q,z['bound'],z['positions'],flush=True)
# Exact local T5 candidate via bounded randomized triple generation; only diagnostics.
tri=list(combinations(range(9),3));seen=set();trials=0
while len(seen)<12 and trials<200000:
 trials+=1;chosen=[];used=set();d=[0]*9
 for b in rng.sample(tri,len(tri)):
  ps={tuple(p) for p in combinations(b,2)}
  if ps&used:continue
  chosen.append(b);used|=ps
  for i in b:d[i]+=1
  if len(chosen)==5:break
 if min(d[:5])<2 or min(d[5:])<1:continue
 key=tuple(sorted(chosen))
 if key in seen:continue
 seen.add(key);z=evaluate(key);out.append(z);print('t5',len(seen),z['bound'],z['positions'],flush=True)
Path(__file__).with_name('V25_NINE_PROBE.json').write_text(json.dumps(json_value(dict(scope=__doc__,elapsed=time.perf_counter()-start,trials=trials,results=out)),indent=2)+'\n')
