"""Complete local four-degree-six profile domains at v=22,23; no whole H scan."""
from pathlib import Path
from itertools import product,permutations,combinations
from fractions import Fraction as Q
from time import perf_counter
import sys,json,argparse
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[3]
sys.path[:0]=[str(ROOT/'context/propertyb34-hour1-20261013/low-math'),str(HERE.parent/'high-math')]
from quad_general import profiles
from subset_position_dp import SubsetEngine
from joint_layout_lp import solve_profile,Engine,json_value
from weighted_overlap_lp import overlap_inventory

def main(v):
 start=perf_counter();s=4;ps=list(permutations(range(s)));pairs=list(combinations(range(s),2));groups={};originals=[]
 def canonical(ns):
  return min(tuple(sorted((sum(1<<p[i] for i in range(s) if t&(1<<i)),n) for t,n in ns.items() if n)) for p in ps)
 for ls in product(range(1,27-v),repeat=6):
  if any(sum(c-1 for ij,c in zip(pairs,ls) if i in ij)>25-v for i in range(s)):continue
  for ns,t4,t3 in profiles((6,)*4,ls):
   ns={t:n for t,n in ns.items() if n};key=canonical(ns)
   if key not in groups:groups[key]=len(groups)
   originals.append(dict(codegrees=ls,quadruple=t4,triples=t3,group=groups[key]))
 print('v',v,'labelled',len(originals),'groups',len(groups),flush=True)
 eng=Engine(v,s);out=[]
 for key,gid in groups.items():
  ns=dict(key);sub=SubsetEngine(v,s,ns);r=sub.solve();w=dict(r,graph=f'v{v}-four6',group=gid,counts=ns)
  if Q(r['bound'])>=1:w['joint']=solve_profile(eng,w)
  if Q(w.get('joint',w).get('bound',9))>=1:w['overlap']=solve_profile(eng,w,quota_builder=overlap_inventory)
  best=w.get('overlap',w.get('joint',w));w['final_bound']=best.get('bound',9)
  if Q(r['bound'])<1:sub.verify(r);w['independent_ABC']=True
  out.append(w);print(gid,'bound',w['final_bound'],flush=True)
  if perf_counter()-start>150:break
 (HERE/f'FOUR_LOW_{v}.json').write_text(json.dumps(json_value(dict(scope=__doc__,v=v,complete=len(out)==len(groups),labelled=len(originals),groups=len(groups),bindings=originals,results=out,elapsed_seconds=perf_counter()-start)),indent=2)+'\n')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('v',type=int);main(ap.parse_args().v)
