"""Independent ABC verification for new useful high-codegree middle branches."""
from pathlib import Path
from fractions import Fraction
import json,runpy
HERE=Path(__file__).resolve().parent
ns=runpy.run_path(str(HERE/'middle_diagnostic.py'))
Profile,rows,total_bound,certificate,json_value,independent_rows=[ns[k] for k in ['Profile','rows','total_bound','certificate','json_value','independent_rows']]
out=[]
for kind,source in [('pair','MIDDLE_DOUBLE_RESULTS.json'),('triple','MIDDLE_TRIPLE_RESULTS.json')]:
 for x in json.loads((HERE/source).read_text())['cases']:
  v=x['v'];th=3 if v==22 else 4
  if kind=='pair' and not (x['degrees']==[7,7] and x['codegree']>th):continue
  if kind=='triple' and max(x['pairs'])!=th:continue
  p=Profile(v,5,x['positions'],{int(t):n for t,n in x['counts'].items() if n})
  cs=[certificate(p,i) for i in range(len(p.positions))]
  rr=rows(p,deductions={p.positions[i]:cs[i]['loss'] for i in range(len(p.positions))})
  assert total_bound(rr)==Fraction(x['bound'])<1
  stubs=[frozenset(i+1 for i in range(len(p.positions)) if t&(1<<i)) for t,n in p.counts.items() for _ in range(n)]
  for a,b in zip(rr,independent_rows(v,p.positions,stubs)):assert all(a[k]==b[k] for k in ['A','B','C'])
  out.append(dict(kind=kind,**x,independent_ABC=True))
(HERE/'MIDDLE_THRESHOLDS_VERIFIED.json').write_text(json.dumps(json_value(dict(scope='actual selectability is the separate threshold lemma; exact witnesses and independent ABC checked here',profiles=out)),indent=2)+'\n')
print('Verified',len(out),'retained profiles')
