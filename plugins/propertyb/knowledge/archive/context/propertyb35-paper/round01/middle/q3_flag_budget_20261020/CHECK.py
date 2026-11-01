"""Independent flag receipt and explicit degree-slot reconstruction, all frozen5813 keys."""
from pathlib import Path
from functools import lru_cache
from itertools import combinations
import json,time
P=Path(__file__).resolve().parent;st=time.process_time();base=P.parent/'a2_a3_joint_moment_frontier_20261020'
source=json.loads((P/'SOURCE_AUDIT.json').read_text());tail=json.loads((P.parent/'three_nonunit_direct_repair_20261020/TAIL_RESULT.json').read_text());expected=[]
for row in tail['rows']:
 T=row['traces'];pairs={}
 for pair in combinations(range(5),2):
  mask=sum(1<<i for i in pair);pairs[pair]=sum((T[i]&mask)==mask and (T[j]&mask)==mask for i,j in combinations(range(3),2))
 f=sum(pairs.values())
 for a in row['A2_A3_local_necessary_tail']:
  expected.append({'traces':T,'attachments':a['attachments'],'degrees':a['original_F_degrees'],'flag':f})
assert expected==source['all83_flag_keys'] and len(expected)==83
zero=[z for z in expected if z['flag']==0];assert len(zero)==1
assert zero[0]['traces']==[3,13,22] and zero[0]['degrees']==[9,9,10,8,8]
def f(s):
 a,b=divmod(s,5);groups=[a+(i<b) for i in range(5)]
 return sum(groups[i]*groups[j] for i,j in combinations(range(5),2))
@lru_cache(None)
def bound(E,z):
 vals=[]
 for m in range(36):
  if m>z:continue
  q=[3]*m+[4]*(35-m);left=2*E-sum(q)
  if left<0 or left>25*(35-m):continue
  for i in range(m,35):take=min(left,25);q[i]+=take;left-=take
  assert left==0 and sum(q)==2*E and all(3<=v<=29 for v in q) and q.count(3)==m
  vals.append(sum(f(34-v) for v in q))
 return max(vals,default=-1)
old=json.loads((base/'CONDITIONAL_CRITICAL_SURVIVORS.json').read_text());jobs=json.loads((base/'RESULT.json').read_text())['jobs'];ds={j['unique_degree_key']:j['degrees'] for j in jobs};report=json.loads((P/'RESULT.json').read_text())
def key(z):return(z['unique_degree_key'],tuple(z['n']),z['tau'])
outputs=[]
for mode in report['modes']:
 expected={}
 for row in old:
  degree=ds[row['unique_degree_key']];n=row['n'];resources=[2*n[2],10*degree.count(10),4*degree.count(8),(9*degree.count(9))//2]
  z=3*row['tau']+(resources[0] if mode['mode']=='pair_resource_only' else min(resources))
  Pcap=bound(595-n[1],z)
  if Pcap<0:continue
  budget=min(row['P'],Pcap);rem=budget;C=[0]*5
  for j in range(4,-1,-1):C[j]=min(rem,row['C_caps'][j]);rem-=C[j]
  L2=sum(w*c for w,c in zip((36,120,330,792,1716),C))+6864*n[1]
  if L2>=5445440:expected[key(row)]=(resources,z,Pcap,budget,C,L2)
 saved=json.loads((P/('SURVIVORS_'+mode['mode']+'.json')).read_text());assert len(saved)==len(expected)==mode['survivors'] and set(expected)=={key(z) for z in saved}
 for row in saved:
  assert expected[key(row)]==(row['zero_flag_resources'],row['q3_upper'],row['q3_box_bound'],row['P'],row['C'],row['twice_L'])
 for job in mode['jobs']:assert sum(s['unique_degree_key']==job['unique_degree_key'] for s in saved)==job['survivors']
 outputs.append({'mode':mode['mode'],'same_full_keys':True,'survivors':len(saved),'all16_spectra_nonempty':all(j['survivors'] for j in mode['jobs'])})
out={'status':'PASS','scope':__doc__,'source83_tail_key_equality':True,'unique_zero_flag_key':zero[0],'frozen_input_keys':len(old),'modes':outputs,'cpu_seconds':time.process_time()-st};(P/'CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
