"""Producer replay of every retained actual Q6 projection, no transfer gate."""
from pathlib import Path
from itertools import permutations
from collections import Counter
import json,hashlib
R=Path(__file__).resolve().parent
path=R/'Q5_T17_RANK_candidate_first_coverage.json';a=json.loads(path.read_text())
target_major=tuple(a['orbit']['majority']);target_omit=tuple(a['orbit']['omitted'])
perms=list(permutations(range(5)));seen=set();counts=Counter()
def project(x,d):return (x&((1<<d)-1))|((x>>(d+1))<<d)
for w in a['witnesses']:
 v=w['v'];i=w['input_index'];d=w['outer_cut'];assert (v,i) not in seen;seen.add((v,i));counts[v]+=1
 raw=(R/f'Q5_T26_RANK_batch_remaining_v{v}.bin').read_bytes()[9*i:9*i+9]
 z=set(raw[:4]);odd=set(raw[4:]);s=set(w['sources']);assert v not in odd
 assert len(z)==4 and len(odd)==5 and all((x^y).bit_count()!=1 for x in z for y in odd)
 side=lambda x:((x^v)>>d)&1==0
 za={x for x in z if side(x)};wa={x for x in odd if side(x)}
 if (len(za),len(wa))==(3,1):assert s==za;minor=next(iter(z-za));inc=odd-wa
 else:assert (len(za),len(wa))==(0,4) and s<=wa and len(s)==3 and (1<<d) not in s;minor=next(iter(odd-wa));inc=z-za
 assert minor==w['minority'];omit=tuple(sorted(project((x^(1<<d))^minor,d) for x in s));major=tuple(sorted({project(x^minor,d) for x in inc}|set(omit)))
 assert omit==tuple(w['omitted']) and major==tuple(w['majority'])
 for j,p in enumerate(perms):
  image=lambda x:sum(((x>>k)&1)<<p[k] for k in range(5))
  if tuple(sorted(map(image,major)))==target_major and tuple(sorted(map(image,omit)))==target_omit:
   w['local_permutation_index']=j;w['local_bit_permutation']=p;break
 else:raise AssertionError('marked projection not in fixed orbit')
assert len(seen)==882 and dict(counts)=={1:180,7:342,31:360}
remainders=[]
for v in (1,7,31):
 raw=(R/f'Q5_T26_RANK_batch_remaining_v{v}.bin').read_bytes();new=b''.join(raw[k:k+9] for k in range(0,len(raw),9) if (v,k//9) not in seen)
 n=f'Q5_T17_RANK_candidate_first_remaining_v{v}.bin';(R/n).write_bytes(new)
 remainders.append({'v':v,'input':len(raw)//9,'removed':counts[v],'candidate_remaining':len(new)//9,'file':n,'sha256':hashlib.sha256(new).hexdigest()})
a['status']='PRODUCER_REPLAY_PASS_LOCAL_RANK_AND_IMPORT_REVIEW_PENDING';a['candidate_remainders']=remainders;a['witnesses_replayed']=882
path.write_text(json.dumps(a,indent=2)+'\n',encoding='utf-8')
print(json.dumps(remainders,indent=2))
