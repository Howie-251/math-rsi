from pathlib import Path
from itertools import combinations,permutations
from collections import Counter
import hashlib,json
R=Path(__file__).resolve().parent
maps=[tuple(sum(((x>>i)&1)<<p[i] for i in range(5)) for x in range(32)) for p in permutations(range(5))]
cache={}
def canon(M,J,U):
 anchor=min(M or U);raw=tuple(tuple(sorted(x^anchor for x in xs)) for xs in (M,J,U))
 if raw not in cache:
  m,j,u=raw;cache[raw]=min(tuple(tuple(sorted(t[x^s] for x in xs)) for xs in (m,j,u)) for s in (m or u) for t in maps)
 return cache[raw]
def project(x,d):return (x&((1<<d)-1))|((x>>(d+1))<<d)
counts=Counter();hashes={};reports=[]
for v in (1,7,31):
 name=f'SIXTEEN_POST12_FORCED_remaining_v{v}_covered.bin';raw=(R/name).read_bytes();assert len(raw)%15==0;hashes[name]=hashlib.sha256(raw).hexdigest();covered=Counter()
 for off in range(0,len(raw),15):
  Z,W=raw[off:off+7],raw[off+7:off+15];seen=set()
  for d in range(6):
   A=lambda x:(x>>d&1)==(v>>d&1)
   za=[x for x in Z if A(x)];wa=[x for x in W if A(x)];s=len(za)+1-len(wa)
   if s>=2:
    if not wa:continue
    pool=za;minor=[x for x in Z if not A(x)];major=[x for x in W if not A(x)]
   elif s<=-2:s=-s;pool=[x for x in wa if x!=(1<<d)];minor=[x for x in W if not A(x)];major=[x for x in Z if not A(x)]
   else:continue
   h=len(minor)+len(major)+s
   if h not in (12,14):continue
   for S in combinations(pool,s):
    M=[project(x,d) for x in minor];U=[project(x,d) for x in S];J=[project(x,d) for x in major]+U
    assert len(set(M+J))==h
    seen.add((h,s,canon(M,J,U)))
  counts.update(seen);covered.update({h for h,u,g in seen})
  if seen:covered['any']+=1
 reports.append({'v':v,'input':len(raw)//15,'covered_by_h':dict(covered)})
rows=[]
for i,((h,u,g),ct) in enumerate(sorted(counts.items(),key=lambda x:(-x[1],x[0]))):
 rows.append({'index':i,'holes':h,'omit_count':u,'type':f'H{h}_U{u}','minority':g[0],'majority':g[1],'omitted':g[2],'actual_records':ct})
(R/'SIXTEEN_NEW_TYPES_profile.json').write_text(json.dumps({'status':'CONDITIONAL_PRODUCER_ONLY','input_hashes':hashes,'reports':reports,'rows':rows},indent=2)+'\n')
print('orbits',len(rows),'types',sorted({r['type'] for r in rows}),'reports',reports)
