from itertools import combinations,permutations
from collections import Counter
from pathlib import Path
import json
P=Path(__file__).resolve().parent
E=[x for x in range(1,32) if x.bit_count()%2==0]; O=[x for x in range(32) if x.bit_count()%2]
perms=list(permutations(range(5)))
trans=[[sum(((x>>i)&1)<<p[i] for i in range(5)) for x in range(32)] for p in perms]
def key(z,w): return min((tuple(sorted(t[x] for x in z)),tuple(sorted(t[x] for x in w))) for t in trans)
rows=[];hist=Counter();orbits={}
for z in combinations(E,4):
 allowed=[w for w in O if all((w^x).bit_count()!=1 for x in z)]
 for w in combinations(allowed,3):
  ds=[1+sum(not(x>>i&1) for x in z)-sum(not(x>>i&1) for x in w) for i in range(5)]
  cuts=[i for i,d in enumerate(ds) if d in (1,2,3)]
  row={'Z':z,'W':w,'deltas':ds,'good_cuts':cuts}
  rows.append(row);hist[tuple(sorted(ds))]+=1
  if not cuts:
   k=key(z,w); orbits.setdefault(k,[]).append(row)
result={'normalized_forbidden':0,'total':len(rows),'good':sum(bool(r['good_cuts']) for r in rows),'residual':sum(len(v) for v in orbits.values()),'histogram':[(k,v) for k,v in sorted(hist.items())], 'residual_orbits':[{'Z':k[0],'W':k[1],'size':len(v),'deltas':v[0]['deltas'],'members':v} for k,v in sorted(orbits.items())]}
(P/'A8_geometry_census.json').write_text(json.dumps(result,indent=2))
print(json.dumps({k:v for k,v in result.items() if k!='residual_orbits'}));print([(r['Z'],r['W'],r['size'],r['deltas']) for r in result['residual_orbits']])
