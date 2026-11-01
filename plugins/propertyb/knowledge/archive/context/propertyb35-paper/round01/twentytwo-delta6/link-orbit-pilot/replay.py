"""No optimizer: independent complement-count probability table and exact fractional obstruction replay."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations_with_replacement,permutations
from collections import Counter
from math import comb,factorial
from functools import lru_cache
import json,time,sys
HERE=Path(__file__).resolve().parent
def choose(n,k):return comb(n,k)if 0<=k<=n else 0
@lru_cache(None)
def internal(n,red,edge,mono_red):
 total=Q();variants=set(permutations(red))
 for R in variants:
  score=Q(1)
  for r,e in zip(R,edge):
   numerator=choose(n-e,r-e)if mono_red else choose(n-e,r)
   score*=Q(numerator,choose(n,r))
  total+=score
 return total/len(variants)
def orbitmult(xs):
 z=factorial(len(xs))
 for c in Counter(xs).values():z//=factorial(c)
 return z
def main():
 start=time.process_time();m=json.loads((HERE/'MODEL.json').read_text());input_name=sys.argv[1] if len(sys.argv)>1 else 'FRACTIONAL_OBSTRUCTION.json';z=json.loads((HERE/input_name).read_text())
 colors=[(pc,a,b)for pc in (0,1)for a in combinations_with_replacement(range(4-pc),4)for b in combinations_with_replacement(range(4),2)]
 edges=[(ep,a,b)for ep in (0,1)for a in combinations_with_replacement(range(4),4)for b in combinations_with_replacement(range(5),2)if ep+sum(a)+sum(b)==5]
 assert [[pc,list(a),list(b)]for pc,a,b in colors]==m['colors']
 assert [[ep,list(a),list(b)]for ep,a,b in edges]==m['edges']
 counts={json.dumps(e['edge']):Q(e['count'])for e in z['counts']};ns=[counts.get(json.dumps(e),Q())for e in m['edges']];scores=[]
 for i,(pc,a,b)in enumerate(colors):
  row=[]
  for j,(ep,c,d)in enumerate(edges):
   red=Q(int(not ep or pc))*internal(3,a,c,True)*internal(4,b,d,True)
   blue=Q(int(not ep or not pc))*internal(3,a,c,False)*internal(4,b,d,False)
   row.append(red+blue);assert row[-1]==Q(m['probabilities'][i][j])
  scores.append(sum(p*n for p,n in zip(row,ns)))
 names=['external_edge_count','p_external_degree','A_external_incidence','B_external_incidence','AA_cross_pairs','AB_cross_pairs','BB_cross_pairs','pB_pairs'];marg=[Q()]*len(names)
 for (ep,a,b),n,cap in zip(edges,ns,m['simple_orbit_capacities']):
  assert n>=0
  actualcap=orbitmult(a)*orbitmult(b)
  for e in a:actualcap*=choose(3,e)
  for e in b:actualcap*=choose(4,e)
  assert cap==actualcap and n<=cap
  vals=[1,ep,sum(a),sum(b),sum(a[i]*a[j]for i in range(4)for j in range(i+1,4)),sum(a)*sum(b),b[0]*b[1],ep*sum(b)]
  marg=[v+n*c for v,c in zip(marg,vals)]
 assert all(x>=lo and(hi is None or x<=hi)for x,lo,hi in zip(marg,m['lower'],m['upper']))
 assert [str(x)for x in marg]==z['marginals'] and min(scores)==Q(z['exact_minimum_score'])>1
 out=dict(status='PASS',method=__doc__,color_families=len(colors),edge_orbits=len(edges),probability_cells=len(colors)*len(edges),exact_minimum=str(min(scores)),marginals=dict(zip(names,map(str,marg))),scope='Fractional aggregate type-count relaxation only; no integer witness and no hypergraph realization.',cpu_seconds=time.process_time()-start)
 (HERE/('UNIFORM_REPLAY.json' if input_name=='UNIFORM_OBSTRUCTION.json' else 'REPLAY.json')).write_text(json.dumps(out,indent=2)+'\n');print(out)
if __name__=='__main__':main()
