"""Exact low-edge degree-spectrum audit and integer obstruction to the central AB trace LP."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
import sys,json,time
HERE=Path(__file__).parent;ROOT=HERE.parents[4]
sys.path.insert(0,str(ROOT/'computations'))
from independent_structure_bounds import independent_rows,as_json
from multilock import edge_weight

def partitions(n,cap=None):
 if not n:yield ();return
 for a in range(min(n,cap or n),1-1,-1):
  for tail in partitions(n-a,a):yield(a,)+tail

def main():
 st=time.time();ps=list(partitions(7));assert len(ps)==15;spectra=[]
 for p in ps:
  k=len(p);sq=sum(t*t for t in p);assert sum(p)==7 and 1274+sq<=1323
  if k>=5:assert sq<21 and sq<=(8-k)**2+k-1<=13
  spectra.append(dict(excess_partition=p,positive_vertices=k,degree_square_sum=1274+sq,positive_degree_sum=7*k+7,guaranteed_low_edge_modes=['77777'] if k<=4 else ['77777','77778']))
 assert {tuple(z['excess_partition']) for z in spectra if z['positive_vertices']>=5}=={(3,1,1,1,1),(2,2,1,1,1),(2,1,1,1,1,1),(1,1,1,1,1,1,1)}
 position=(10,11,12,13,14);cases=[]
 for ds in ((7,7,7,7,7),(7,7,7,7,8),(7,7,7,8,8),(7,7,7,7,9)):
  ns={0:39-sum(ds),31:1}|{1<<i:d-1 for i,d in enumerate(ds)}
  assert sum(ns.values())==35 and ns[31]==1 and all(n>=0 for n in ns.values())
  assert all(sum(n for m,n in ns.items() if m>>i&1)==d for i,d in enumerate(ds))
  assert all(sum(n for m,n in ns.items() if m>>i&1 and m>>j&1)>=1 for i in range(5) for j in range(i))
  cross=[sum((5-m.bit_count())*n for m,n in ns.items() if m>>i&1) for i in range(5)];assert min(cross)>=19
  paircap=sum(comb(5-m.bit_count(),2)*n for m,n in ns.items());assert paircap>=comb(19,2)
  outside_inc=sum((5-m.bit_count())*n for m,n in ns.items());assert outside_inc==175-sum(ds)>=19*7
  types=[frozenset(i+1 for i in range(5) if m>>i&1) for m,n in ns.items() for _ in range(n)];rr=independent_rows(24,position,types)
  for r in rr:
   assert r['A']==sum(n*edge_weight(24,5,position,m,r['k'],True) for m,n in ns.items())
   assert r['B']==sum(n*edge_weight(24,5,position,m,r['k'],False) for m,n in ns.items())
  ab=sum((min(r['A'],r['B']) for r in rr),Q());abc=sum((r['bound'] for r in rr),Q());assert ab>1
  cases.append(dict(degrees=ds,counts=ns,positions=position,AB_value=ab,ABC_value_before_link_deduction=abc,rows=rr,selected_external_pair_capacity=cross,outside_pair_capacity=paircap,outside_pair_requirement=comb(19,2),outside_degree_sum=outside_inc,retained_after_stronger_low_edge_selector=sum(ds)<=36))
 out=dict(scope=__doc__,status='PASS',degree_spectra=spectra,stronger_selection='an actual edge of degree sum<=36 always exists',AB_LP_scope='integer primal feasible obstruction for the one stated central layout; no LP optimization or all-layout claim',cases=cases,elapsed_seconds=time.time()-st)
 (HERE/'AUDIT.json').write_text(json.dumps(as_json(out),indent=2)+'\n');print('PASS spectra',len(ps),'AB integer witnesses',[(r['degrees'],str(r['AB_value'])) for r in cases],'seconds',time.time()-st)
if __name__=='__main__':main()
