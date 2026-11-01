from pathlib import Path
from math import comb
from fractions import Fraction
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;start=time.process_time();data=json.loads((P/'RESULT.json').read_text())
def C(n,k):return comb(n,k) if 0<=k<=n else 0
# Cache linear coefficients. Same-anchor event-tree deduction on both colors.
coeff={r:(C(13,r-4),C(13,r),C(9,r-8),C(9,r),C(17,r)) for r in range(18)}
def risk(tr,a,red,r):
 R,B,J,K,D=coeff[r]
 U=sum(x*(R if red>>v&1 else B)-max(x-1,0)*(J if red>>v&1 else K) for v,x in enumerate(a))
 for m in tr:
  j=m.bit_count();k=(red&m).bit_count()
  if not j:U+=C(12,r-5)+C(12,r)
  elif k==j:U+=C(12+j,r-5+j)
  elif not k:U+=C(12+j,r)
 return U,D
rows=[]
for row in data['rows']:
 if not row['actual_necessary_profiles']:continue
 remaining=[];closed=[]
 for z in row['actual_necessary_profiles']:
  best=min((Fraction(U,D),red,r,U,D) for red in range(1,16) for r in range(18) for U,D in [risk(row['traces'],z['attachments'],red,r)])
  ratio,red,r,U,D=best
  entry={**z,'best_bound':str(ratio),'best_red_mask':red,'best_outside_red':r,'best_U':U,'best_D':D}
  (closed if ratio<1 else remaining).append(entry)
 rows.append({'traces':row['traces'],'sizes':row['sizes'],'closed':closed,'remaining':remaining})
result={'scope':'All proper F-colorings up to complement (15 masks),18 outside-red counts; universal same-anchor red/blue event-tree deduction; exact n22. Necessary profiles only. No positions/search.','input_profiles':data['actual_necessary_profiles'],'closed':sum(len(r['closed']) for r in rows),'remaining':sum(len(r['remaining']) for r in rows),'remaining_trace_orbits':sum(bool(r['remaining']) for r in rows),'rows':rows,'cpu_seconds':time.process_time()-start}
(P/'F_COLOR_RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print({k:v for k,v in result.items() if k!='rows'})
print('first remaining',next((r['traces'],r['remaining'][0]) for r in rows if r['remaining']))
