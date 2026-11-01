"""Second stdlib replay of every savedsource / owncolour / originaltrace role."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json,time
HERE=Path(__file__).resolve().parent;start=time.process_time()
source=HERE.parent/'positive_occ_three/nine_positive_joint_negative_budget_20261020/budget21_difference/P6_REMAINING.jsonl'
original={json.dumps([r['inventory'],r['nine'],r['higher'],r['J']],separators=(',',':')):r for r in map(json.loads,source.open())}
rows=list(map(json.loads,(HERE/'ALL79_MENUS.jsonl').open()));seen=set();columns=0;tenkeys=set();provenkeys=set()
for r in rows:
 key=json.dumps(r['source_key'],separators=(',',':'));assert key in original and key not in seen;seen.add(key)
 raw=original[key];T=[31]+[sum(1<<v for v in t) for t in raw['higher']]
 for p,n in zip(combinations(range(6),2),raw['J']):T.extend([sum(1<<v for v in p)]*n)
 ds=[8+int(v==raw['nine']) for v in range(6)];u=[ds[v]-sum(m>>v&1 for m in T) for v in range(6)]
 for v,n in enumerate(u):T.extend([1<<v]*n)
 assert len(T)==35 and T==r['trace_masks']==raw['trace_masks']
 assert sum(5-m.bit_count() for m in T)==126
 blueexpected={b for b in range(1,64) if b&31 and (~b)&31};actualblue=set()
 for c in r['menus']:
  b=sum(1<<v for v in c['blue']);assert b not in actualblue;actualblue.add(b)
  counts={'P':Counter(),'N':Counter()};roles=[];inc=0
  for i,m in enumerate(T):
   sign='P' if m&b==m else ('N' if m&b==0 else 'proper');k=5-m.bit_count();roles.append([i,sign,k])
   if sign!='proper':counts[sign][k]+=1;inc+=k
   columns+=1
  assert roles==c['roles'] and inc==c['signed_total_occurrence']<=126
  sig=tuple(counts['P'][k] for k in (4,3,2,1))+tuple(counts['N'][k] for k in (1,2,3,4))
  assert sig==tuple(c['signature'][:8]) and c['signed_point_occurrence_upper_bound']==[7]*18
  if c['provisional_exact10_match']:
   assert sig[:6]==(10,0,0,0,0,0) and sig[6]<=2 and sig[7]<=18;tenkeys.add(key)
  if c['proved_gate']:provenkeys.add(key)
 assert actualblue==blueexpected and len(actualblue)==60
assert seen==set(original) and len(rows)==79 and not provenkeys and len(tenkeys)==59
conditional=list(map(json.loads,(HERE/'PROVISIONAL_TEN_MATCHES.jsonl').open()))
assert {json.dumps(r['source_key'],separators=(',',':')) for r in conditional}==tenkeys
remaining=list(map(json.loads,(HERE/'CONDITIONAL_REMAINING.jsonl').open()))
assert {json.dumps(r['source_key'],separators=(',',':')) for r in remaining}==seen-tenkeys
out={'status':'PASS','source_keys_complete':79,'own_P_colourings':4740,'original_trace_roles_checked':columns,'provisional10_sources':59,'conditional_remaining':20,'proved_gate_new_sources':0,'exterior_exact_degrees_invented':False,'signed_D7_reason':'Everyactual exteriorvertex has degree7; eachactiveoriginaledge yields atmostone signedindex because its nonempty Ptrace is already monochromeonecolour or mixedsafe.','cpu_seconds':time.process_time()-start}
(HERE/'VERIFY_MENUS.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
