"""Check all witnesses, matching coverage and the full coordinate orbit cover."""
import hashlib,itertools,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def pairings(n):
 r=1
 for k in range(1,n,2):r*=k
 return r
def main():
 permutations=list(itertools.permutations(range(4)))
 transforms=[[sum(((x>>i)&1)<<p[i] for i in range(4)) for x in range(16)] for p in permutations]
 orbit_counts=Counter()
 for b in range(1,16):
  if b.bit_count()%2:continue
  for z in range(16):
   if z.bit_count()%2!=1 or (z^b).bit_count()==1:continue
   for d in range(16):
    if d==z or d.bit_count()%2!=1:continue
    orbit_counts[min((t[b],t[z],t[d]) for t in transforms)]+=1
 listed=[tuple(map(int,l.split())) for l in (ROOT/'q4_balanced_avoid_path_configs.txt').read_text().splitlines() if l.strip()]
 assert len(listed)==len(set(listed))==13 and set(listed)==set(orbit_counts)
 assert sum(orbit_counts.values())==196
 reports=[]
 for b,z,d in sorted(orbit_counts):
  name=f'q4_balanced_avoid_path_{b}_{z}_{d}.bin';raw=(ROOT/name).read_bytes()
  assert len(raw)==31*10395
  holes={0,b,z,d};covered=set(range(16))-holes;seen=bytearray(10395)
  for off in range(0,len(raw),31):
   m=raw[off:off+16];p=raw[off+16:off+31]
   assert {x for x in range(16) if m[x]==255}==holes
   for x in covered:assert m[x] in covered and m[x]!=x and m[m[x]]==x
   rest=sorted(covered);rank=0
   while rest:
    x=rest.pop(0);i=rest.index(m[x]);rank+=i*pairings(len(rest)-1);rest.pop(i)
   assert not seen[rank];seen[rank]=1
   assert len(p)==len(set(p))==15 and set(p)==set(range(1,16))
   assert p[0]==d and p[-1]!=z and p[-1].bit_count()%2==1
   edges={frozenset((x,y)) for x,y in zip(p,p[1:])}
   required={frozenset((x,m[x])) for x in covered}
   assert required<=edges
   for e in edges-required:
    x,y=e;assert (x^y).bit_count()==1
  assert all(seen)
  reports.append({'file':name,'records':10395,'orbit_size':orbit_counts[b,z,d],'sha256':hashlib.sha256(raw).hexdigest()})
 result={'status':'PASS','configurations':196,'orbits':13,'records':13*10395,'files':reports,'full_p6_proved':False}
 (ROOT/'q4_balanced_avoid_path_verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:result[k] for k in ('status','configurations','orbits','records')}))
if __name__=='__main__':main()
