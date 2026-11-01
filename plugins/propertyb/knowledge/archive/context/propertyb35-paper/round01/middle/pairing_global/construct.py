"""Explicit colorable pair-covering H24 with35 simple5-edges, delta7, no matching hits20 edges.
The upper bound is certified by a two-vertex weighted-matching dual, not whole-H enumeration.
"""
from pathlib import Path
from itertools import combinations
from fractions import Fraction as Q
from collections import Counter
import json,random,time
HERE=Path(__file__).parent

def main():
 st=time.time();points=[(x,y) for x in range(5) for y in range(5) if (x,y)!=(0,0)];index={p:i for i,p in enumerate(points)};a=(0,1);b=(1,0);lines=[]
 for x in range(5):lines.append(tuple((x,y) for y in range(5)))
 for m in range(5):
  for c in range(5):lines.append(tuple((x,(m*x+c)%5) for x in range(5)))
 base=[];through=[]
 for L in lines:
  if (0,0) not in L:base.append(tuple(sorted(index[p] for p in L)))
  else:
   B=[p for p in L if p!=(0,0)];fill=b if a in B else a;E=tuple(sorted(index[p] for p in B+[fill]));base.append(E);through.append(dict(block=[index[p] for p in B],fill=index[fill],edge=E))
 other=[p for p in points if p not in (a,b)];extra=[tuple(sorted(index[p] for p in other[i:i+5])) for i in range(0,20,5)];extra.append(tuple(sorted(index[p] for p in other[20:]+other[:3])));edges=base+extra;assert len(set(edges))==35 and all(len(set(E))==5 for E in edges)
 degrees=[sum(i in E for E in edges) for i in range(24)];assert sorted(degrees)==[7]*20+[8]*3+[11];pairs=list(combinations(range(24),2));lam={p:sum(set(p)<=set(E) for E in base) for p in pairs};assert min(lam.values())==1
 dual=[int(p in (a,b)) for p in points];weights={p:c-1 for p,c in lam.items()};assert sum(dual)==2 and all(w>=0 and w<=dual[i]+dual[j] for (i,j),w in weights.items());assert weights[tuple(sorted((index[a],index[b])))]==2
 # Direct deterministic search for a coloring of this one explicit control H.
 rng=random.Random(20261020)
 for attempt in range(1,10001):
  mask=rng.getrandbits(24)
  if all(any(mask>>i&1 for i in E) and any(not(mask>>i&1) for i in E) for E in edges):break
 else:raise AssertionError('No color found within control-only trial bound')
 colors=[int(mask>>i&1) for i in range(24)];assert all({colors[i] for i in E}=={0,1} for E in edges)
 result=dict(scope=__doc__,vertices=24,points=points,base_edges=base,extra_edges=extra,edges=edges,deleted_point=[0,0],center_a=index[a],center_b=index[b],modified_blocks=through,degrees=degrees,degree_spectrum={str(d):n for d,n in Counter(degrees).items()},pair_covered=True,base_pair_codegrees=[dict(pair=p,lambda_base=lam[p],repeat_weight=weights[p]) for p in pairs],weighted_matching_vertex_dual=dual,repeat_matching_upper_bound=2,max_matching_size=12,base_hit_upper_bound=14,total_hit_upper_bound=19,proper_coloring=colors,coloring_trial=attempt,universal_random_matching_expectations={22:str(Q(35)*(Q(10,21)-Q(15,21*19))),23:str(Q(35)*(Q(10,23)-Q(15,23*21))),24:str(Q(35)*(Q(10,23)-Q(15,23*21)))},elapsed_seconds=time.time()-st)
 (HERE/'COUNTEREXAMPLE.json').write_text(json.dumps(result,indent=2)+'\n');print({k:v for k,v in result.items() if k in ('vertices','degree_spectrum','total_hit_upper_bound','coloring_trial','universal_random_matching_expectations','elapsed_seconds')})
if __name__=='__main__':main()
