"""Independent187 checked fixed bounds with exactly the pure-link quota, no others."""
from pathlib import Path
from fractions import Fraction
import sys,json,time
P=Path(__file__).resolve().parent;ROOT=P.parents[5];st=time.process_time()
sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'computations'))
from independent_structure_bounds import independent_rows,injection_probability
saved=json.loads((P/'RESULT.json').read_text());domain=json.loads((P.parent/'WORST_SOURCE_DOMAIN.json').read_text())
allowed={(tuple(z['c_pair']),z['c0']) for z in domain['cases']};assert len(allowed)==470
cases=[]
def replay(z,pos):
 ns={int(m):n for m,n in z['counts'].items()};masks=[m for m,n in ns.items() for _ in range(n)];assert len(masks)==35
 types=[frozenset(v+1 for v in range(5) if m>>v&1) for m in masks]
 ir=independent_rows(21,tuple(pos),types);pure=ns.get(1,0);assert pure<=5
 quota=max(0,(4*pure-16+2)//3);assert quota==(2 if pure==5 else 0)
 total=Fraction();rows=[]
 for r in ir:
  W=injection_probability(16,r['a'],r['b'],4,4,False) if r['k']==pos[0] else Fraction()
  loss=2*quota*W;C=r['C']-loss;assert C>=0
  minimum=min(r['A'],r['B'],C);total+=minimum
  rows.append(dict(k=r['k'],A=str(r['A']),B=str(r['B']),Czero=str(r['C']),pure_unordered=quota if r['k']==pos[0] else 0,W=str(W),loss=str(loss),Cnew=str(C),minimum=str(minimum)))
 return dict(positions=pos,bound=str(total),strict=total<1,pure_unordered_quota=quota,expanded35_masks=masks,rows=rows)
for z in saved['cases']:
 assert (tuple(z['c_pair']),z['c0']) in allowed
 out=replay(z,z['positions']);assert Fraction(out['bound'])==Fraction(z['bound']) and out['strict']==z['strict']
 cases.append(dict(c_pair=z['c_pair'],c0=z['c0'],inclusive_z_to_K=z['inclusive_z_to_K'],**out))
last=saved['nonstrict'][0];all_last=[]
for c in last['all_fixed']:
 rr=replay(last,c['positions']);assert Fraction(rr['bound'])==Fraction(c['bound']);all_last.append(rr)
assert len(cases)==187 and sum(z['strict'] for z in cases)==186
out=dict(status='PASS_PURE2_ONLY187_CHECKED_PREFIX',scope=__doc__,checked=187,strict=186,nonstrict=1,remaining283_not_evaluated=True,other_five_sources_not_evaluated=True,all_best_bounds_equal=True,pure_quota_no_other_deduction=True,cases=cases,first_nonstrict_all_four_slots=all_last,cpu_seconds=time.process_time()-st)
(P/'VERIFY_PREFIX.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k not in ('cases','first_nonstrict_all_four_slots')})
