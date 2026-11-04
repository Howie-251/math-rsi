"""Diagnostic: compare stored N14 positive unions against exact small T44 unions."""
from pathlib import Path
from itertools import permutations
import json,numpy as np,sys
P=Path(__file__).resolve().parent
E=[(a,b) for a in range(16) for b in range(a+1,16) if (a^b).bit_count()==1];idx={e:i for i,e in enumerate(E)}
def edge(a,b):return (min(a,b),max(a,b))
unions=[];mates=[];holepairs=[]
for hole in (() if '--exact-n14' in sys.argv else (3,15)):
 raw=(P/f'q4_n14_rich_{hole}.bin').read_bytes();pos=0
 while pos<len(raw):
  m=raw[pos:pos+16];n=raw[pos+16];pos+=17;F={edge(x,m[x]) for x in range(16) if m[x]!=255};mask=0
  for j in range(n):
   cyc=raw[pos:pos+15];pos+=15
   for i,a in enumerate(cyc):
    e=edge(a,cyc[(i+1)%15])
    if e not in F:mask|=1<<idx[e]
  unions.append(mask);mates.append(list(m));holepairs.append(hole)
 assert pos==len(raw)
if '--exact-n14' in sys.argv:
 exact=(P/'Q5_T63_n14_exact_inputs.bin').read_bytes()
 unions=list(np.frombuffer((P/'Q5_T63_n14_exact_unions.bin').read_bytes(),dtype='<u4'))
 mates=[list(exact[i:i+16]) for i in range(0,len(exact),18)]
 holepairs=[next(j for j in range(1,16) if m[j]==255) for m in mates]
u,uniqueidx=np.unique(np.array(unions,dtype=np.uint32),return_index=True)
low=json.loads((P/'Q5_T63_t44_rich_samples.json').read_text())['low']
low.sort(key=lambda x:x['union_mask'].bit_count())
hits=[]
for row in low:
 for perm in permutations(range(4)):
  base=[sum(((x>>perm[i])&1)<<i for i in range(4)) for x in range(16)]
  for shift in range(16):
   if shift.bit_count()%2!=1:continue
   tr=[x^shift for x in base];mask=0
   for i,(a,b) in enumerate(E):
    if row['union_mask']>>i&1:mask|=1<<idx[edge(tr[a],tr[b])]
   where=np.flatnonzero((u&mask)==0)
   if len(where):
    k=int(uniqueidx[where[0]]);newmate=[255]*16
    for a,b in enumerate(row['mate']):
     if b!=255:newmate[tr[a]]=tr[b]
    hits.append({'N14_mate':mates[k],'N14_holes':[0,holepairs[k]],'N14_stored_union':int(unions[k]),
     'T44_mate':newmate,'T44_omitted':[tr[x] for x in row['omitted']],
     'T44_union':mask,'T44_sample_record':row['record']})
    break
  if hits:break
 if hits:break
out={'status':'DIAGNOSTIC_ONLY','T44_low_samples_compared_until_hit':row['record'],
 'N14_records':len(unions),'disjoint_stored_union_candidates':hits,
 'conclusion':'Stored union disjointness is not a nonexistence proof; further N14 exploration required.'}
(P/('Q5_T63_zero_gluing_exact_probe.json' if '--exact-n14' in sys.argv else 'Q5_T63_zero_gluing_probe.json')).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
