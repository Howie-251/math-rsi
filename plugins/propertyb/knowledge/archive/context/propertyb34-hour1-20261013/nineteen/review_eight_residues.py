"""Check only the stated residual implications, not the profile classification."""
from pathlib import Path
from itertools import combinations
import json
ROOT=Path(__file__).resolve().parents[3]
rows=json.loads((ROOT/'context/propertyb34-hour1-20261013/low-math/EIGHT_VERIFIED.json').read_text())['residual']
pairs=list(combinations(range(4),2))
allowed={(0,0,0,0):'empty',(0,0,1,1):'one edge',(1,1,2,2):'P4',(1,1,1,3):'claw',(2,2,2,2):'C4'}
result=[]
for row in rows:
 counts={int(k):v for k,v in row['counts'].items()}
 common=lambda mask:sum(n for m,n in counts.items() if m&mask==mask)
 actual_lambdas=[common((1<<i)|(1<<j)) for i,j in pairs]
 assert actual_lambdas==row['lambdas']
 triples=[common(m) for m in (7,11,13,14)]
 assert triples==row['common_triples'] and common(15)==row['common_quad']
 if 3 in actual_lambdas:
  assert triples==[0]*4 and common(15)==0
  result.append({'index':row['index'],'case':'codegree-three, all common triples zero'})
 else:
  assert all(x in (1,2) for x in actual_lambdas)
  deg=tuple(sorted(sum(actual_lambdas[k]==1 for k,p in enumerate(pairs) if i in p) for i in range(4)))
  assert deg in allowed
  shape=allowed[deg]
  assert common(15)==int(shape=='C4')
  result.append({'index':row['index'],'unit_graph':shape,'common_quad':common(15)})
out={'scope':'16 supplied residual representatives only; no re-verification of complete local classification, probability tables, or global theorem','status':'PASS','rows':result}
Path(__file__).with_name('EIGHT_RESIDUE_REVIEW.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: 16 supplied residual representatives, exact/common traces and induced-graph implications')
