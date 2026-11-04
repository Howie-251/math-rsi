import itertools,json
from pathlib import Path
R=Path(__file__).resolve().parent
rows=json.loads((R/'q4_balanced_two_avoided_generation.json').read_text())['rows']
out=[]
for row in rows:
 r,y=row['avoided']; raw=(R/f'q4_balanced_two_avoided_{r}_{y}.bin').read_bytes()
 neg=[raw[i:i+16] for i in range(0,len(raw),30) if raw[i+16]==255]
 for p0 in itertools.permutations(range(3)):
  p=p0+(3,)
  def tr(v):return sum(((v>>j)&1)<<p[j] for j in range(4))
  for m in neg:
   q=[-1]*16
   for a in range(16):
    if m[a]!=255:q[tr(a)]=tr(m[a])
   out.append((tr(r),tr(y),*q))
out=sorted(set(out))
(R/'t15_r3_small_negative_inputs.txt').write_text('\n'.join(' '.join(map(str,t)) for t in out)+'\n')
print(len(out))
