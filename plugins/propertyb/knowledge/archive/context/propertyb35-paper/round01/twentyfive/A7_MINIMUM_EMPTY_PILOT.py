"""At most six pilots only from191 retained old fixed-layout residuals.
No new domain or third outside point. Samples worst bound by codegree and
whether each private swap preserves the minimum empty potential.
"""
from pathlib import Path
from fractions import Fraction as Q
import json,sys,time
P=Path(__file__).resolve().parent;root=P.parents[3];sys.dont_write_bytecode=True
sys.path[:0]=[str(root/'context/propertyb34/round01/high-math'),str(root/'computations'),str(root/'computations/propertyb33/round01')]
from subset_position_dp import SubsetEngine
from multilock import json_value
src=json.loads((P/'A7_TRIANGLE_DOMAIN.json').read_text());fil=json.loads((P/'A7_MINIMUM_EMPTY_FILTER.json').read_text());zs=next(z['cases'] for z in src['results'] if z['base']==19 and z['partner']==4);ff=next(z for z in fil['results'] if z['partner']==4);res=[z for z in ff['retained_cases'] if z['was_fixed_residual']];chosen={};st=time.perf_counter()
for lam in [2,3,4]:
 z=max((z for z in res if zs[z['case_index']]['codegree']==lam),key=lambda z:Q(z['minimum_raw']));chosen[z['case_index']]=z
for pp in [(0,0),(1,0),(0,1)]:
 z=max((z for z in res if (z['P']['a']+z['P']['q_out'],z['Q']['a']+z['Q']['q_out'])==pp),key=lambda z:Q(z['minimum_raw']));chosen[z['case_index']]=z
out=[]
for idx,r in chosen.items():
 zz=zs[idx];ns={int(t):n for t,n in zz['counts'].items()};tm=time.perf_counter();eng=SubsetEngine(25,9,ns);w=eng.verify(eng.solve());raw=sum(min(rr['A'],rr['B'],rr['C']) for rr in w['rows']);out.append(dict(case_index=idx,base=19,partner=4,codegree=zz['codegree'],P=zz['P'],Q=zz['Q'],joint=zz['joint'],previous_fixed=r['minimum_raw'],raw_ABC_bound=raw,seconds=time.perf_counter()-tm,**w));print(idx,zz['codegree'],r['minimum_raw'],w['bound'],raw,flush=True)
summary=dict(scope=__doc__,cases=len(out),strict=sum(z['bound']<1 for z in out),raw_strict=sum(z['raw_ABC_bound']<1 for z in out),elapsed_seconds=time.perf_counter()-st)
(P/'A7_MINIMUM_EMPTY_PILOT.json').write_text(json.dumps(json_value(dict(summary=summary,results=out)),indent=2)+'\n');print(json.dumps(summary,indent=2))
