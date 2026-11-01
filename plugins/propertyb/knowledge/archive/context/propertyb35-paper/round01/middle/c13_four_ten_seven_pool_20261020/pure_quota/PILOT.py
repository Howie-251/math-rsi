"""Independent pure-link2 correction of the frozen first zero-quota failure."""
from pathlib import Path
from fractions import Fraction
import json,sys,time
P=Path(__file__).resolve().parent;ROOT=P.parents[5];st=time.process_time()
sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'computations'))
from independent_structure_bounds import independent_rows,injection_probability
frozen=json.loads((P.parent/'RESULT.json').read_text());z=frozen['nonstrict'][0]
ns={int(m):n for m,n in z['counts'].items()};assert ns[1]==5
masks=[m for m,n in ns.items() for _ in range(n)];assert len(masks)==35
types=[frozenset(v+1 for v in range(5) if m>>v&1) for m in masks]
cases=[]
for slot in (1,10,11,12):
 pos=(slot,8,9,20,21);ir=independent_rows(21,pos,types)
 zero=sum((min(r['A'],r['B'],r['C']) for r in ir),Fraction())
 total=Fraction();rr=[]
 for row in ir:
  W=injection_probability(16,row['a'],row['b'],4,4,False) if row['k']==slot else Fraction()
  loss=4*W;Cnew=row['C']-loss;assert Cnew>=0
  old=min(row['A'],row['B'],row['C']);new=min(row['A'],row['B'],Cnew);total+=new
  rr.append(dict(k=row['k'],A=str(row['A']),B=str(row['B']),Czero=str(row['C']),W=str(W),quota_unordered=2 if row['k']==slot else 0,loss=str(loss),Cnew=str(Cnew),old_min=str(old),new_min=str(new)))
 cases.append(dict(positions=pos,zero_bound=str(zero),pure_bound=str(total),strict=total<1,changed_pivot=next(r for r in rr if r['k']==slot),rows=rr))
best=min(cases,key=lambda z:Fraction(z['pure_bound']))
out=dict(status='PURE2_FIRST_FAILURE_STRICT' if best['strict'] else 'PURE2_FIRST_FAILURE_NONSTRICT',scope=__doc__,N=16,pure_edges=5,pure_bad_unordered_quota=2,c_pair=z['c_pair'],c0=z['c0'],all_fixed=cases,best=best,cpu_seconds=time.process_time()-st)
(P/'PILOT_RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print('STATUS',out['status'],'CPU',out['cpu_seconds'])
for c in cases:print(c['positions'],'zero',c['zero_bound'],'pure',c['pure_bound'],'pivot',c['changed_pivot'])
