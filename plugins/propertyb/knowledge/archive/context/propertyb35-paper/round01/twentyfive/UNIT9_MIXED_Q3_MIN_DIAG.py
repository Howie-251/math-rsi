"""Bounded diagnostic: do saved fixed choices lose actual min on the 27 pilot residuals?
No new layouts or DP; evaluate the existing <=8 layouts per pilot family.
"""
from pathlib import Path
from fractions import Fraction as Q
import sys,json,time
P=Path(__file__).resolve().parent
sys.dont_write_bytecode=True
sys.path[:0]=[str(P)]
from UNIT9_MIXED_Q3_QUADRATIC import counts,FixedBranch
from multilock import json_value,Profile,rows,total_bound
from pure_quota import certificate
st=time.perf_counter();source=json.loads((P/'UNIT9_MIXED_AFFINE.json').read_text())
fs={f['base']:(f,next(c for c in f['cases'] if c['q']==3)) for f in source['families'] if f['feasible'] and any(c['q']==3 for c in f['cases'])}
pilot=json.loads((P/'UNIT9_MIXED_Q3_QUADRATIC_PILOT.json').read_text());out=[]
for entry in pilot['families']:
 if not entry['residual_masks']:continue
 f,c=fs[entry['base']]
 evaluators=[FixedBranch(f,c,p['positions'],p['choices']) for p in entry['polynomials']]
 residual=[];covered=[]
 for mask in entry['residual_masks']:
  vv=[ev.evaluate(mask,True)[1] for ev in evaluators];best=min(vv);j=vv.index(best)
  if best<1:
   pos=entry['polynomials'][j]['positions'];p=Profile(25,5,pos,counts(f,c,mask))
   losses={pos[i]:certificate(p,i)['loss'] for i in range(9)}
   rr=rows(p,deductions=losses);assert total_bound(rr)==best
   covered.append(dict(mask=mask,bound=best,polynomial_index=j,independent_ordered_pair_replay=True))
  else:residual.append(dict(mask=mask,bound=best))
 out.append(dict(base=entry['base'],min_switch_covers=covered,residual=residual))
summary=dict(scope=__doc__,initial_residual=27,additional_strict=sum(len(e['min_switch_covers']) for e in out),remaining=sum(len(e['residual']) for e in out),elapsed_seconds=time.perf_counter()-st)
(P/'UNIT9_MIXED_Q3_MIN_DIAG.json').write_text(json.dumps(json_value(dict(summary=summary,families=out)),indent=2)+'\n');print(json.dumps(json_value(summary),indent=2))
