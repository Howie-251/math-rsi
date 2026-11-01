"""Unique7 center n21/M35: select at least4 actual unit8; reuse existing n21 gates/domain/pilots.
Only remaining fresh three-neighbor inventories get fixed DP; one bounded24-order joint per failure.
"""
from pathlib import Path
from itertools import combinations,product
from fractions import Fraction as Q
import json,sys,time
HERE=Path(__file__).parent;ROOT=HERE.parents[4];sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb35-paper/round01/twentyone-delta5'),str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations'),str(ROOT/'context/propertyb34/round01/middle-math'),str(ROOT/'context/propertyb34-hour1-20261013/high-math')]
from star_low import parts,recover
from subset_position_dp import SubsetEngine
from joint_layout_lp import solve_profile
from fast_position_dp import Engine
from multilock import json_value

def kk(ns):return tuple(ns.get(t,ns.get(str(t),0)) for t in range(16))
def main():
 st=time.time();src=HERE.parents[1]/'twentyone-high';rs=[r for r in json.loads((src/'STAR_THREE_DOMAIN.json').read_text())['cases'] if r['center_degree']==7 and r['neighbor_degrees']==[8]*3];cache={kk(r['counts']):r for r in json.loads((src/'STAR_THREE_PILOT.json').read_text())['cases'] if r['center_degree']==7 and r['neighbor_degrees']==[8]*3};out=[]
 for i,r in enumerate(rs):
  if kk(r['counts']) in cache:z=dict(cache[kk(r['counts'])]);z['bound']=Q(z['bound'])
  else:en=SubsetEngine(21,4,r['counts']);z=en.verify(en.solve())
  z.update(r);z.update(id=i,strict=z['bound']<1,partition=r['center_partition']);out.append(z)
 (HERE/'THREE_DP.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=True,pilot_reused=len(cache),cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('fixed',sum(r['strict'] for r in out),'of',len(out),'seconds',time.time()-st,flush=True)
 js=[];eng=Engine(21,4)
 for r in out:
  if r['strict']:continue
  j=solve_profile(eng,dict(r,counts={t:n for t,n in r['counts'].items() if n},graph='n21unit8',group=r['id']),permutation_limit=24);j['source_id']=r['id'];js.append(j);print('joint',r['id'],j.get('bound',j.get('status')),flush=True)
 (HERE/'THREE_JOINT.json').write_text(json.dumps(json_value(dict(results=js,elapsed_seconds=time.time()-st)),indent=2)+'\n');good={j['source_id'] for j in js if Q(j.get('bound','2'))<1};rr=[r for r in out if not r['strict'] and r['id'] not in good];(HERE/'THREE_REMAINDERS.json').write_text(json.dumps(json_value(dict(count=len(rr),cases=rr,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('jointstrict',len(good),'res',len(rr),'seconds',time.time()-st)
if __name__=='__main__':main()
