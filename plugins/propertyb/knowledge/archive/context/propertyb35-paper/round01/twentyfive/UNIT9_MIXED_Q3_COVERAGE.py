"""Reconcile exact q3 partial coverage: saved quadratic witnesses plus four min replays."""
from pathlib import Path
from fractions import Fraction as Q
import json,sys,time
P=Path(__file__).resolve().parent
sys.dont_write_bytecode=True;sys.path[:0]=[str(P)]
from UNIT9_MIXED_Q3_QUADRATIC import poly_value
st=time.perf_counter();source=json.loads((P/'UNIT9_MIXED_AFFINE.json').read_text())
residual={f['base']:set(c['residual_colors']) for f in source['families'] if f['feasible'] for c in f['cases'] if c['q']==3 and c.get('residual_colors')}
assert len(residual)==131 and sum(map(len,residual.values()))==2956
pilot=json.loads((P/'UNIT9_MIXED_Q3_QUADRATIC_PILOT.json').read_text());diag=json.loads((P/'UNIT9_MIXED_Q3_MIN_DIAG.json').read_text())
covered_poly=covered_min=0;maximum=Q()
for f in pilot['families']:
 remain=residual[f['base']];seen=set()
 for poly in f['polynomials']:
  for mask in poly['covered_masks']:
   assert mask in remain and mask not in seen
   v=poly_value(poly,mask);assert v<1;maximum=max(maximum,v)
   seen.add(mask);covered_poly+=1
 remain-=seen
 assert remain==set(f['residual_masks'])
for f in diag['families']:
 remain=residual[f['base']]
 for item in f['min_switch_covers']:
  assert item['mask'] in remain and Q(item['bound'])<1 and item['independent_ordered_pair_replay']
  remain.remove(item['mask']);covered_min+=1;maximum=max(maximum,Q(item['bound']))
 assert remain=={z['mask'] for z in f['residual']}
out=dict(scope=__doc__,q=3,complete=False,initial_residual_families=131,initial_residual_colors=2956,quadratic_covers=covered_poly,min_switch_covers=covered_min,remaining_families=sum(bool(v) for v in residual.values()),remaining_colors=sum(map(len,residual.values())),maximum_added_certificate=str(maximum),remaining={str(k):sorted(v) for k,v in residual.items() if v},elapsed_seconds=time.perf_counter()-st)
(P/'UNIT9_MIXED_Q3_COVERAGE.json').write_text(json.dumps(out,separators=(',',':'))+'\n');print(json.dumps({k:v for k,v in out.items() if k!='remaining'},indent=2))
