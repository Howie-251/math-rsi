import itertools,json
from pathlib import Path
R=Path(__file__).resolve().parent;negative=None;sources=[]
for path in R.glob('q4_balanced_two_avoided_*_*.bin'):
 r,y=map(int,path.stem.removeprefix('q4_balanced_two_avoided_').split('_'))
 for pp in itertools.permutations(range(3)):
  p=pp+(3,)
  def tr(v):return sum(((v>>j)&1)<<p[j] for j in range(4))
  if (tr(r),tr(y))!=(10,1):continue
  raw=path.read_bytes();assert len(raw)==10395*30
  found=set()
  for i in range(0,len(raw),30):
   if raw[i+16]!=255:continue
   assert raw[i+16:i+30]==bytes([255])*14
   m=raw[i:i+16];found.add(tuple(sorted(tuple(sorted((tr(a),tr(m[a])))) for a in range(16) if a<m[a]<16)))
  if negative is not None:assert found==negative
  negative=found;sources.append(path.name)
assert len(negative)==1
out=dict(status='PASS',bridge=10,B_omitted=1,negative_count=1,negative_matching=next(iter(negative)),source_tables=sorted(set(sources)))
(R/'t15_core15_table_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
