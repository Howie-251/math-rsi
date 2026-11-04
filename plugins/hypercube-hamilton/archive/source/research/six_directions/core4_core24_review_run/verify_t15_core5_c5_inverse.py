"""Independent occupied-bridge c5 bound for core5, from audited raw Q4 tables."""
import json,itertools,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
negatives=None;source=None
for path in sorted(R.glob('q4_balanced_two_avoided_*_*.bin')):
 r,y=map(int,path.stem.removeprefix('q4_balanced_two_avoided_').split('_'))
 for p0 in itertools.permutations(range(3)):
  p=p0+(3,)
  def tr(v):return sum(((v>>j)&1)<<p[j] for j in range(4))
  if (tr(r),tr(y))!=(6,1):continue
  raw=path.read_bytes();assert len(raw)==10395*30
  found=set()
  for i in range(0,len(raw),30):
   if raw[i+16]!=255:continue
   assert raw[i+16:i+30]==bytes([255])*14
   m=raw[i:i+16];found.add(frozenset(tuple(sorted((tr(a),tr(m[a])))) for a in range(16) if a<m[a]<16))
  if negatives is not None:assert found==negatives
  negatives=found;source=path.name
assert len(negatives)==2
candidates=set()
for L in negatives:
 for pair in itertools.combinations(L,2):candidates.add(frozenset(L-set(pair)))
assert len(candidates)==30
rows=[]
for F in sorted(candidates,key=lambda f:sorted(f)):
 covered={a for e in F for a in e};ports=sorted(set(range(16))-{0,7,1}-covered)
 assert len(F)==4 and len(covered)==8 and len(ports)==5 and 6 in ports
 ends=sorted(set(ports)-{6});a,b,c,d=ends
 Qs=[frozenset({(a,b),(c,d)}),frozenset({(a,c),(b,d)}),frozenset({(a,d),(b,c)})]
 bad=[Q for Q in Qs if F|Q in negatives]
 assert len(bad)==1
 rows.append(dict(ports=ports,matching=sorted(F),bad_quotient=sorted(bad[0]),negative_quotient_count=len(bad)))
out=dict(status='PASS',scope='Core5 c5 occupied bridge6: every fixed B partial matching has at most one negative quotient; all nonempty inverse cases enumerated',source_table=source,negative_count=2,inverse_cases=30,max_bad_quotients=1,cases=rows)
(R/'t15_core5_c5_inverse_verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='cases'}))
