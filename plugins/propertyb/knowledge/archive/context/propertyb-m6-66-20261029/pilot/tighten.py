import json
from pathlib import Path
from fractions import Fraction as F
P=Path(__file__).resolve().parent
x=json.loads((P/'baseline.json').read_text());opt=json.loads((P/'positions.json').read_text());maps={(r['v'],r['kind'],tuple(r['degrees']),r['tri']):r for r in opt['rows']}
rows=[]
for r in x['rows']:
 threshold={39:10,40:10,41:9}.get(r['v'],11)
 if r['degrees'] and max(r['degrees'])>threshold and r['kind']=='three':continue
 a=r.copy();b=maps.get((r['v'],r['kind'],tuple(r['degrees']),r['tri']))
 if b and F(b['best_U'])<F(a['U']):
  a.update(U=b['best_U'],approx=b['best_approx'],pass_strict=b['pass_strict'],positions=b['positions'],ordered_degrees=b['ordered_degrees'])
 rows.append(a)
out=dict(scope='complete necessary covering profile domain after sharper degree-threshold selection, with local placement certificates where available',profiles=len(rows),failures=[r for r in rows if not r['pass_strict']],rows=rows,structural_checks=[])
for v,t in [(39,10),(40,10),(41,9)]:
 d0=8;rmin=-(-( (t+1)*v-390)//(t+1-d0))
 for r in range(rmin,v+1):
  upper=(5*(t+1)-(v-1))*r+1950-5*(t+1)*v
  assert upper>=0 and r*r>2*(r+upper)
 out['structural_checks'].append(dict(v=v,degree_threshold=t,rmin=rmin,checked_r_count=v-rmin+1))
(P/'tightened.json').write_text(json.dumps(out,indent=2))
print('profiles',len(rows),'remaining',len(out['failures']))
for v in range(27,44):
 rs=[r for r in rows if r['v']==v]; print(v,len(rs),sum(not r['pass_strict'] for r in rs))
