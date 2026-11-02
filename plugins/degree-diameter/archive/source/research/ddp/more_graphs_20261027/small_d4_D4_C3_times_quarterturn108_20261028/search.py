import resource
resource.setrlimit(resource.RLIMIT_CPU,(14,14))
from pathlib import Path
from itertools import combinations
from collections import deque,Counter
import json,time
out=Path(__file__).resolve().parent;started=time.process_time()
def enc(x,y,z,j):return x%3+3*(y%3)+9*(z%3)+27*(j%4)
def dec(i):return (i%3,i//3%3,i//9%3,i//27)
def rotate(x,y,j):return [(x,y),(-y,x),(-x,-y),(y,-x)][j%4]
elements=[dec(i) for i in range(108)]
def multiply(g,h):
 x,y,z,j=elements[g];u,v,t,k=elements[h];u,v=rotate(u,v,j);return enc(x+u,y+v,z+t,j+k)
table=[[multiply(g,h) for h in range(108)] for g in range(108)]
inverses=[]
for g,(x,y,z,j) in enumerate(elements):
 u,v=rotate(-x,-y,-j);q=enc(u,v,-z,-j);assert table[g][q]==table[q][g]==0;assert table[0][g]==table[g][0]==g;inverses.append(q)
invol=[g for g in range(1,108) if inverses[g]==g];pairs=[(g,inverses[g]) for g in range(1,108) if g<inverses[g]]
assert len(invol)==9 and len(pairs)==49
candidates=[]
for p,q in combinations(pairs,2):candidates.append(('two_pairs',tuple(sorted(p+q))))
for p in pairs:
 for h in combinations(invol,2):candidates.append(('one_pair_two_involutions',tuple(sorted(p+h))))
for h in combinations(invol,4):candidates.append(('four_involutions',h))
assert len(candidates)==3066 and len({s for _,s in candidates})==3066
control=tuple(sorted((enc(0,0,1,1),enc(0,0,-1,-1),enc(1,0,0,0),enc(-1,0,0,0))))
assert any(s==control for _,s in candidates)
candidates=[('two_pairs',control)]+[(t,s) for t,s in candidates if s!=control]
(out/'GROUP_TABLE.json').write_text(json.dumps({'encoding':'x+3*y+9*z+27*j','elements':elements,'inverse':inverses,'table':table})+'\n')
(out/'ORBIT_COUNTS.json').write_text(json.dumps({'orbit_action':'inversion permutationg->g^-1 ongroup elements,notanAutgraphsearch','identity_singleton':1,'nonidentity_self_inverse_singletons':9,'two_element_inverse_orbits':49,'self_inverse_ids':invol,'inverse_pair_ids':pairs,'connection_set_types':dict(Counter(t for t,s in candidates))},indent=2)+'\n')
qmul=[[((a%3+b%3)%3)+3*((a//3+b//3)%4) for b in range(12)] for a in range(12)]
project=[z+3*j for x,y,z,j in elements]
def qprofile(S,inv):
 gs=[project[g] for g in S];d=[-1]*12;d[0]=0;queue=deque([0])
 while queue:
  u=queue.popleft()
  for g in gs:
   v=qmul[u][g]
   if d[v]<0:d[v]=d[u]+1;queue.append(v)
 raw=[0]*12;raw[0]=1;dp=[0]*48
 for k,g in enumerate(gs):dp[g*4+k]+=1
 for depth in range(1,5):
  for q in range(12):raw[q]+=sum(dp[q*4:q*4+4])
  if depth==4:break
  nxt=[0]*48
  for q in range(12):
   total=sum(dp[q*4:q*4+4])
   if total:
    for k,g in enumerate(gs):nxt[qmul[q][g]*4+k]+=total-dp[q*4+inv[k]]
  dp=nxt
 assert sum(raw)==161
 return {'projected_labels':gs,'connected':all(x>=0 for x in d),'R4missing':sum(x<0 or x>4 for x in d),'minimum_raw':min(raw),'first_minimum_slot':raw.index(min(raw)),'rawcounts':raw,'exact_quotient_D':max(d) if all(x>=0 for x in d) else None}
def closure(S):
 seen={0};stack=[0]
 while stack:
  u=stack.pop()
  for s in S:
   v=table[u][s]
   if v not in seen:seen.add(v);stack.append(v)
 return len(seen)
def radius(S,full=False):
 d=[-1]*108;d[0]=0;queue=deque([0])
 while queue:
  u=queue.popleft()
  if not full and d[u]==4:continue
  for s in S:
   v=table[u][s]
   if d[v]<0:d[v]=d[u]+1;queue.append(v)
 hist=Counter(x for x in d if x>=0);return d,[hist[k] for k in range(max(hist)+1)]
stats=Counter();types=Counter();hit=None
with (out/'CASES.jsonl').open('w') as log:
 for ordinal,(typ,S) in enumerate(candidates):
  assert len(set(S))==4 and 0 not in S and all(inverses[s] in S for s in S)
  inv=[S.index(inverses[s]) for s in S];q=qprofile(S,inv);stats['processed']+=1;types[typ]+=1
  row={'ordinal':ordinal,'type':typ,'generator_ids':S,'generator_coordinates':[elements[s] for s in S],'inverse_label_indices':inv,'quotient':q,'actual108_connectivity_profiled':False,'actual108_connected':None,'actual108_R4_missing':None,'actual_global_D':None}
  iscontrol=S==control;dp=None;hist=None
  if iscontrol:
   dp,hist=radius(S,True);stats['control_full_BFS']+=1;stats['actual108_profiles']+=1;stats['actual108_connected_profiled']+=all(x>=0 for x in dp);stats['actual108_R4checks']+=1
   row.update({'actual108_connectivity_profiled':True,'actual108_connected':all(x>=0 for x in dp),'actual108_R4_missing':sum(x<0 or x>4 for x in dp),'actual_global_D':max(dp),'exact_histogram':hist,'status':'CONTROL_EXACT_PROFILE'})
   (out/'CONTROL_RESULT.json').write_text(json.dumps(row,indent=2)+'\n')
  if q['R4missing'] or q['minimum_raw']<9:
   stats['quotient_gate_rejects']+=1;stats['quotient_R4_rejects']+=q['R4missing']>0;stats['quotient_raw_below9_rejects']+=q['minimum_raw']<9;stats['quotient_disconnected_implies_full_disconnected']+=not q['connected']
   if not iscontrol:row['status']='STRICT_QUOTIENT_GATE_REJECT';stats['quotient_only_rejects_without108_profile']+=1
  else:
   stats['quotient_gate_passes']+=1
   if not iscontrol:
    reach=closure(S);stats['actual108_profiles']+=1;row['actual108_connectivity_profiled']=True;row['actual108_connected']=reach==108;row['closure_size']=reach
    if reach!=108:stats['actual108_disconnected_profiled']+=1;row['status']='ACTUAL108_DISCONNECTED'
    else:
     stats['actual108_connected_profiled']+=1;dp,hist=radius(S);stats['actual108_R4checks']+=1;row['actual108_R4_missing']=sum(x<0 for x in dp)
     if all(x>=0 for x in dp):
      assert max(dp)==4;row.update({'status':'HIT_D4','actual_global_D':4,'R4_histogram':hist});hit=row
     else:row.update({'status':'ACTUAL108_R4_FAIL','first_missing_id':dp.index(-1),'R4_histogram':hist});stats['actual108_R4_fail']+=1
  if iscontrol and row['actual108_R4_missing']>0:stats['control_R4_fail']+=1
  log.write(json.dumps(row)+'\n');log.flush()
  if ordinal%64==0 or hit:(out/'checkpoint.json').write_text(json.dumps({'status':'HIT_STOP' if hit else 'RUNNING','next_cursor':ordinal+1,'processed':stats['processed'],'total':3066,'stats':dict(stats)})+'\n')
  if hit:
   edges=sorted({tuple(sorted((u,table[u][s]))) for u in range(108) for s in S});assert len(edges)==216 and all(u!=v for u,v in edges)
   (out/'graph108.edges').write_text('108 216\n'+''.join(f'{u} {v}\n' for u,v in edges));(out/'HIT.json').write_text(json.dumps(hit,indent=2)+'\n');(out/'GENERATORS.json').write_text(json.dumps({'ids':S,'coordinates':[elements[s] for s in S],'inverse_ids':[inverses[s] for s in S],'encoding':'x+3*y+9*z+27*j'},indent=2)+'\n');break
res={'status':'HIT_STOP_REMAINDER_UNTESTED' if hit else 'COMPLETE_ALL3066_NO_HIT','prediction':'SUPPORTED_PRODUCER_HIT_PENDING_PARENT' if hit else 'REFUTED_COMPLETE','total_sets':3066,'processed':stats['processed'],'untested':3066-stats['processed'],'stats':dict(stats),'processed_by_type':dict(types),'expected_by_type':{'two_pairs':1176,'one_pair_two_involutions':1764,'four_involutions':126},'group_order':108,'target_degree':4,'target_D':4,'savedL':104,'hits':int(hit is not None),'actual_global_D':4 if hit else None,'ordinary_bad_unordered_pairs':None,'CPU_seconds':time.process_time()-started,'source_BFS':0,'othergroups':0,'case_order':'controlfirst,thenlexcategories','scope':'This fixedgroup all4element inverseclosednonidentitysets; quotientrejection is notanactual108diametermeasurement.'}
(out/'WORKER_RESULT.json').write_text(json.dumps(res,indent=2)+'\n');(out/'checkpoint.json').write_text(json.dumps({'status':res['status'],'next_cursor':res['processed'],'untested':res['untested'],'stats':dict(stats)})+'\n');print(json.dumps(res),flush=True)
