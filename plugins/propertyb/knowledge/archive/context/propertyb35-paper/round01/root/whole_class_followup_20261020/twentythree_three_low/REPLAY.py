from pathlib import Path
from collections import Counter
from math import comb
from time import process_time
import json
P=Path(__file__).resolve().parent
stars=json.loads((P.parent/'twentythree_internal_map/independent/RESULT.json').read_text())['direct_counts']
def C(n,k):return comb(n,k) if 0<=k<=n else 0
def single(q,c,r):return C(18-r,q-r if c=='B' else q)
def D(q,c,m):
 tab=([0,0,45,126,234,600,1125] if q==8 and c=='R' else [0,0,1,3,6,30,75] if q==8 else [0,0,10,29,56,180,400])
 step=45 if q==8 and c=='R' else 1 if q==8 else 10
 return tab[min(m,6)]+max(0,m-6)*step
def fail(q,t):
 if t=='w0':return max(v[str(q)] for n,v in stars.items() if n.startswith('w0'))
 if t.startswith('w1_'):return max(stars['w1_'+s+'_'+t[-1]][str(q)] for s in ('34','44'))
 return stars[t][str(q)]
start=process_time();summaries=[]
for U,name in [(7,'RESULT.json'),(8,'RESULT_U8_R13.json'),(9,'RESULT_U9_R13.json')]:
 r=json.loads((P/name).read_text());r13=[];r12=[]
 for row in r['rows']:
  tr=row['traces'];d=row['d'];free=set(row['free']);colors={int(k):v for k,v in row['fixed'].items()};q=row['quota'];inc=Counter(z for e in tr for z in e)
  singles=[5-inc[z] for z in range(3)]+[U-1-inc[3],d-1-inc[4]]
  pure=21-U+sum(len(e)-1 for e in tr)-d
  assert min(singles)>=0 and pure>=0
  count=sum(singles[z] for z in colors)+pure+sum(not(free&set(e)) for e in tr)
  assert count==34-5*len(free)
  total=pure*(single(q,'R',5)+single(q,'B',5));counts=Counter()
  for z,c in colors.items():total+=singles[z]*single(q,c,4);counts[c]+=singles[z]
  for e in tr:
   if free&set(e):continue
   cs={colors[z] for z in e}
   if len(cs)==1:total+=single(q,next(iter(cs)),5-len(e))
  total+=sum(fail(q,t) for t in row['types']);total-=sum(D(q,c,n) for c,n in counts.items())
  assert total==row['total'] and C(18,q)==row['space']
  if row['r13']:r13.append(row)
  if U==7 and all(sum(sum(v<3 for v in e)-1 for e in tr if z in e)<=1 for z in range(3)):r12.append(row)
 tight=max(r13,key=lambda v:v['total']/v['space'])
 summaries.append({'U':U,'rows':len(r['rows']),'r13_keys':len(r13),'r13_min_margin':min(v['space']-v['total'] for v in r13),'r13_tight_ratio':[tight['total'],tight['space']],'r13_tight_witness':tight,'r12_compatible_keys':len(r12),'r12_compatible_residual':[v for v in r12 if v['total']>=v['space']]})
 if U==7:(P/'R12_RESIDUAL.json').write_text(json.dumps(summaries[-1]['r12_compatible_residual'],indent=2)+'\n')
out={'status':'PASS','summaries':summaries,'cpu_seconds':process_time()-start}
(P/'REPLAY_RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
