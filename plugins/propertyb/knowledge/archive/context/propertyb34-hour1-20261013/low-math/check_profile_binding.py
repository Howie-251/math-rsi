from pathlib import Path
import json
from fractions import Fraction
root=Path(__file__).resolve().parent
names=['LOW_DEGREE_SIX_VERIFIED.json','SEVEN_MANY_VERIFIED.json','SEVEN_TWO_VERIFIED.json','SEVEN_ONE_VERIFIED.json','EIGHT_VERIFIED.json','TWENTYONE_FIVE_VERIFIED.json']
result=[]
for name in names:
 data=json.loads((root/name).read_text());rows=data.get('cases',data.get('witnesses'))
 for idx,row in enumerate(rows):
  ds=row['ds'];counts={int(t):c for t,c in row['counts'].items()};pos=row['pos']
  assert sum(counts.values())==34,(name,idx,'edge_count')
  assert all(c>=0 and t<(1<<len(ds)) and t.bit_count()<=5 for t,c in counts.items())
  assert len(pos)==len(ds) and len(set(pos))==len(pos)
  assert all(sum(c for t,c in counts.items() if t&(1<<i))==d for i,d in enumerate(ds)),(name,idx,'degrees')
  assert sum(Fraction(r['bound']) for r in row['rows'])==Fraction(row['bound'])<1
 result.append(dict(file=name,witness_count=len(rows),edges=34,degree_and_position_binding=True,row_sum_and_strict_bound=True))
(root/'PROFILE_BINDING_CHECK.json').write_text(json.dumps(dict(scope='Actual dimensions/degrees/counts of retained strict local witnesses',files=result,total_records=sum(r['witness_count'] for r in result)),indent=2)+'\n')
print(json.dumps(result));print('total',sum(r['witness_count'] for r in result))
