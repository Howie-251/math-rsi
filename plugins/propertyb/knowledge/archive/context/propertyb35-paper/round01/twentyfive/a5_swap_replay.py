"""Literal vertex-set / before-and-after-color replay of all 345 swap coefficients.
Checks the compressed multiplicities without using the closed K formula.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import permutations
from functools import lru_cache
from math import comb
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter()
source=json.loads((P/'A5_SWAP_PILOT.json').read_text())['pair_types']
orb=[((1,2,2,3,4),Q(6,23)),((1,2,3,3,3),Q(10,23)),((1,3,3,3,3),Q(3,23)),((2,2,2,3,3),Q(4,23))]
@lru_cache(None)
def event(key):
    if any(c+d>5 for c,d in key):return Q()
    ans=Q()
    for pattern,w in orb:
      ps=set(permutations(pattern))
      z=Q()
      for r in ps:
        v=Q(1)
        for ri,(c,d) in zip(r,key):
          if not 0<=ri-c<=5-c-d:v=Q();break
          v*=Q(comb(5-c-d,ri-c),comb(5,ri))
        z+=v
      ans+=w*z/len(ps)
    return ans

def fixed_probability(required):
    counts=[]
    for j in range(5):
      red=sum(color==1 and x//5==j for x,color in required.items())
      blue=sum(color==0 and x//5==j for x,color in required.items())
      counts.append((red,blue))
    return event(tuple(sorted(counts)))

def directed(e,g):
    total=Q()
    for x in e:
      for y in range(x//5*5,x//5*5+5):
        if y in e or ((x in g)==(y in g)):continue
        for original_color in (0,1):
          for target_color in (0,1):
            req={z:original_color for z in e};req[y]=1-original_color
            ok=True
            for z in g:
              oldcolor=(1-target_color) if z in (x,y) else target_color
              if z in req and req[z]!=oldcolor:ok=False;break
              req[z]=oldcolor
            if ok:total+=fixed_probability(req)
    return total
checked=0
for row in source:
    e=set();g=set()
    for j,(a,b,t) in enumerate(row['groups']):
      common={j*5+x for x in range(t)}
      ee={j*5+x for x in range(t,a)}
      gg={j*5+x for x in range(a,a+b-t)}
      e|=common|ee;g|=common|gg
    assert len(e)==len(g)==5 and e!=g
    val=directed(e,g)+directed(g,e)
    assert val==Q(row['coefficient']),(row,val)
    checked+=1
out=dict(scope=__doc__,pair_patterns=checked,all_equal=True,probability_cache=str(event.cache_info()),elapsed_seconds=time.perf_counter()-st)
(P/'A5_SWAP_REPLAY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
