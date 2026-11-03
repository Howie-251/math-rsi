import resource
resource.setrlimit(resource.RLIMIT_CPU,(14,14))
from pathlib import Path
from collections import deque,Counter
from itertools import combinations
import json,time
out=Path(__file__).resolve().parent;start=time.process_time()
def enc(x,y,z,j):return x%3+3*(y%3)+9*(z%3)+27*(j%4)
def dec(a):return a%3,a//3%3,a//9%3,a//27
E=[dec(i) for i in range(108)]
def rot(x,y,j):return [(x,y),(-y,x),(-x,-y),(y,-x)][j%4]
def mul(g,h):
 x,y,z,j=E[g];u,v,t,k=E[h];u,v=rot(u,v,j);return enc(x+u,y+v,z+(-1 if j%2 else 1)*t,j+k)
T=[[mul(g,h) for h in range(108)] for g in range(108)];inverse=[]
for g,(x,y,z,j) in enumerate(E):
 u,v=rot(-x,-y,-j);h=enc(u,v,-(-1 if j%2 else 1)*z,-j);assert T[g][h]==T[h][g]==0;assert T[0][g]==T[g][0]==g;inverse.append(h)
H=[g for g in range(1,108) if inverse[g]==g];P=[(g,inverse[g]) for g in range(1,108) if g<inverse[g]];assert len(H)==9 and len(P)==49
C=[]
for p,q in combinations(P,2):C.append(('two_pairs',tuple(sorted(p+q))))
for p in P:
 for h in combinations(H,2):C.append(('one_pair_two_involutions',tuple(sorted(p+h))))
for h in combinations(H,4):C.append(('four_involutions',h))
assert len(C)==len({s for t,s in C})==3066
(out/'GROUP_TABLE.json').write_text(json.dumps({'encoding':'x+3y+9z+27j','elements':E,'inverse':inverse,'table':T})+'\n')
(out/'ORBIT_COUNTS.json').write_text(json.dumps({'action':'inversion permutation,notgraphAut','identity_singleton':1,'nonidentity_selfinverse':9,'twoelement_inverse_orbits':49,'involution_ids':H,'inverse_pair_ids':P,'types':dict(Counter(t for t,s in C))},indent=2)+'\n')
def qgate(S,iv):
 phases=[E[s][3] for s in S];raw=[1,0,0,0];dp=[0]*16
 for k,p in enumerate(phases):dp[p*4+k]+=1
 for depth in range(1,5):
  for p in range(4):raw[p]+=sum(dp[p*4:p*4+4])
  if depth==4:break
  nxt=[0]*16
  for p in range(4):
   total=sum(dp[p*4:p*4+4])
   for k,j in enumerate(phases):nxt[((p+j)%4)*4+k]+=total-dp[p*4+iv[k]]
  dp=nxt
 assert sum(raw)==161
 return raw
def closure(S):
 seen={0};stack=[0]
 while stack:
  u=stack.pop()
  for s in S:
   v=T[u][s]
   if v not in seen:seen.add(v);stack.append(v)
 return len(seen)
def R4(S):
 d=[-1]*108;d[0]=0;q=deque([0])
 while q:
  u=q.popleft()
  if d[u]==4:continue
  for s in S:
   v=T[u][s]
   if d[v]<0:d[v]=d[u]+1;q.append(v)
 hist=Counter(x for x in d if x>=0);return d,[hist[k] for k in range(max(hist)+1)]
stats=Counter();types=Counter();hit=None
with (out/'CASES.jsonl').open('w') as log:
 for i,(typ,S) in enumerate(C):
  assert len(S)==len(set(S))==4 and all(inverse[s] in S for s in S)
  iv=[S.index(inverse[s]) for s in S];raw=qgate(S,iv);stats['processed']+=1;types[typ]+=1
  row={'ordinal':i,'type':typ,'generator_ids':S,'generator_coordinates':[E[s] for s in S],'inverse_label_indices':iv,'phase_rawcounts':raw,'minimum_phase_raw':min(raw),'actual108_profiled':False,'actual108_connected':None,'actual108_R4missing':None,'actual_global_D':None}
  if min(raw)<27:stats['phase_raw_gate_rejects']+=1;row['status']='STRICT_C4_RAW_GATE_REJECT'
  else:
   stats['phase_gate_passes']+=1;reach=closure(S);stats['actual108_profiles']+=1;row.update({'actual108_profiled':True,'closure_size':reach,'actual108_connected':reach==108})
   if reach!=108:stats['actual108_disconnected']+=1;row['status']='ACTUAL108_DISCONNECTED'
   else:
    stats['actual108_connected']+=1;d,hist=R4(S);stats['actual108_R4checks']+=1;missing=d.count(-1);row.update({'actual108_R4missing':missing,'R4_histogram':hist})
    if not missing:assert max(d)==4;row.update({'status':'HIT_D4','actual_global_D':4});hit=row
    else:row.update({'status':'ACTUAL108_R4_FAIL','first_missing_id':d.index(-1)});stats['actual108_R4fail']+=1
  log.write(json.dumps(row)+'\n');log.flush()
  if i%64==0 or hit:(out/'checkpoint.json').write_text(json.dumps({'status':'HIT_STOP' if hit else 'RUNNING','next_cursor':i+1,'stats':dict(stats)})+'\n')
  if hit:
   edges=sorted({tuple(sorted((u,T[u][s]))) for u in range(108) for s in S});assert len(edges)==216 and all(u!=v for u,v in edges)
   (out/'graph108.edges').write_text('108 216\n'+''.join(f'{u} {v}\n' for u,v in edges));(out/'HIT.json').write_text(json.dumps(hit,indent=2)+'\n');(out/'GENERATORS.json').write_text(json.dumps({'ids':S,'coordinates':[E[s] for s in S],'inverse_ids':[inverse[s] for s in S],'encoding':'x+3*y+9*z+27*j'},indent=2)+'\n');break
r={'status':'HIT_STOP_REMAINDER_UNTESTED' if hit else 'COMPLETE_ALL3066_NO_HIT','prediction':'SUPPORTED_PRODUCER_HIT_PENDING_PARENT' if hit else 'REFUTED_COMPLETE','total_sets':3066,'processed':stats['processed'],'untested':3066-stats['processed'],'stats':dict(stats),'processed_by_type':dict(types),'expected_by_type':{'two_pairs':1176,'one_pair_two_involutions':1764,'four_involutions':126},'group_order':108,'degree':4,'target_D':4,'savedL':104,'hits':int(hit is not None),'actual_global_D':4 if hit else None,'ordinary_bad_unordered_pairs':None,'CPU_seconds':time.process_time()-start,'quotient':'C4only;notGplusC12','source_BFS':0,'othergroups':0}
(out/'WORKER_RESULT.json').write_text(json.dumps(r,indent=2)+'\n');(out/'checkpoint.json').write_text(json.dumps({'status':r['status'],'next_cursor':r['processed'],'untested':r['untested'],'stats':dict(stats)})+'\n');print(json.dumps(r),flush=True)
