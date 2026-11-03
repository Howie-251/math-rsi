from pathlib import Path
from collections import Counter
from itertools import product
import json,time
P=Path(__file__).resolve().parent;started=time.process_time();d=json.loads((P.parent/'chart4_quotient_probe/RESULT.json').read_text());A=d['matrices'];b=d['vectors'];inv=[1,0,3,2]
def mv(T,x):return [sum(a*z for a,z in zip(row,x))%3 for row in T]
def mm(T,U):return [[sum(T[i][k]*U[k][j] for k in range(4))%3 for j in range(4)] for i in range(4)]
def rank(cols):
 m=[list(row) for row in zip(*cols)];r=0
 for j in range(4):
  p=next((i for i in range(r,4) if m[i][j]),None)
  if p is None:continue
  m[r],m[p]=m[p],m[r];s=1 if m[r][j]==1 else 2;m[r]=[s*x%3 for x in m[r]]
  for i in range(4):
   if i!=r:
    f=m[i][j];m[i]=[(x-f*y)%3 for x,y in zip(m[i],m[r])]
  r+=1
 return r
I=[[int(i==j) for j in range(4)] for i in range(4)]
for t in range(4):assert mm(A[inv[t]],A[t])==I and mv(A[inv[t]],b[t])==b[inv[t]]
records=[]
for word in product(range(4),repeat=4):
 if any(word[j+1]==inv[word[j]] for j in range(3)):continue
 cols=[]
 for t in word:cols=[mv(A[t],v) for v in cols]+[b[t]]
 rr=rank(cols);assert rr==4;records.append(dict(word=word,rank=rr))
assert len(records)==108
out=dict(status='QUOTIENT108_RANK4_AND_INVERSES_CONFIRMED',field=3,dimension=4,words=108,rank_histogram=dict(Counter(r['rank'] for r in records)),inverse_identities=True,source='sibling chart4_quotient_probe/RESULT.json',old_length5_words_rechecked=0,CPU_seconds=time.process_time()-started)
(P/'quotient_check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
