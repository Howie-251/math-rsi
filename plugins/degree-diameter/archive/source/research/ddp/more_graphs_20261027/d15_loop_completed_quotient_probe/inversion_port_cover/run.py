from pathlib import Path
from datetime import datetime,timezone
import json,struct,time,resource,subprocess,os
import numpy as np
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[4]
BASE=ROOT/'research/ddp/more_graphs_20261027'
START=time.process_time();r=resource.getrusage(resource.RUSAGE_CHILDREN);CH0=r.ru_utime+r.ru_stime
CAD=ROOT/'.tools/lean-4.24.0-linux/bin/cadical'
assert CAD.exists()
def childcpu():
 r=resource.getrusage(resource.RUSAGE_CHILDREN);return r.ru_utime+r.ru_stime-CH0
specs=[]
for n,D in [(15552,4),(102060,5)]:
 chart=json.loads((BASE/f'd15_loop_completed_quotient_probe/affine_relation_recovery/source{n}_AFFINE_RELATIONS.json').read_text())
 assert all(not any(a['c']) for a in chart['arcs'])
 groups=[]
 for a in sorted((a for a in chart['arcs'] if a['from']==a['to']),key=lambda a:a['from']):
  c=a['from'];off=c*chart['bin_size'];v=a['v'];q1=sum(t*3**i for i,t in enumerate(v));q2=sum((2*t%3)*3**i for i,t in enumerate(v))
  groups.append({'variable':len(groups)+1,'controller':c,'pins':[off],'cost':1,'kind':'ZERO'})
  groups.append({'variable':len(groups)+1,'controller':c,'pins':sorted([off+q1,off+q2]),'cost':2,'kind':'SIGN_PAIR'})
 assert len({p for g in groups for p in g['pins']})==sum(g['cost'] for g in groups)
 specs.append({'n':n,'D':D,'groups':groups,'variables':len(groups)})
pred={'timestamp_UTC':datetime.now(timezone.utc).isoformat(),'status':'FROZEN_BEFORE_GROUP_BALL_UNIONS_OR_SOLVER','rule':'Append one vertex to a selected union of canonical inversion orbits: each self-controller zero point costs1, its designated selfline plus/minus direction pair costs2. Total selected pins <=15. All oldedges retained.','basis':'Recovered charts have allc0, making global fiber inversion an actual source automorphism. Purezero union and5fulltriangles both failed; mixed cost1/cost2 orbits retain exact symmetry without requiring all3points of a triangle.','prediction':'At least one of the two sources admits a full R_(D-1) cover in this symmetry-restricted canonical48/60group domain.','scope':'Only zero and original selfline plus/minus pair perloopcontroller, not all source inversionorbits or all648/810freepins.','sources':specs,'budget':{'aggregate_CPU_seconds':20,'solver_calls_per_source':1,'cadical_internal_seconds':5,'solver_OS_CPU_soft_hard':[7,8],'new_balls':0,'source_BFS':0},'stop':'One complete tinyCNF per source. SAT must pass exact cardinality/freepin/cacheOR check before candidate report; no seed,shift,extraorbit,or time continuation. UNKNOWN remains UNKNOWN.'}
(OUT/'PREDICTION.json').write_text(json.dumps(pred,indent=2)+'\n')
results=[]
for spec in specs:
 n=spec['n'];D=spec['D'];groups=spec['groups'];wanted={v for g in groups for v in g['pins']};balls={}
 if n==15552:
  raw=(BASE/'d15_D4_current15552/single_vertex_R3_cover/R3_MASKS.bin').read_bytes();cnt,nn,W=struct.unpack_from('<III',raw);assert nn==n;off=12
  for _ in range(cnt):
   v=struct.unpack_from('<I',raw,off)[0];off+=4
   if v in wanted:balls[v]=int.from_bytes(raw[off:off+8*W],'little')
   off+=8*W
  assert off==len(raw)
 else:
  p=BASE/'d15_D5_current102060_source/monotone_R4_cover';ids=list(map(int,(p/'eligible.txt').read_text().split()));W=(n+63)//64;raw=(p/'radius4.u64le.bin').read_bytes();assert len(raw)==len(ids)*W*8
  for i,v in enumerate(ids):
   if v in wanted:balls[v]=int.from_bytes(raw[i*8*W:(i+1)*8*W],'little')
 assert len(balls)==len(wanted)
 support=np.zeros(n,dtype=np.uint64)
 for i,g in enumerate(groups):
  mask=0
  for v in g['pins']:mask|=balls[v]
  bits=np.unpackbits(np.frombuffer(mask.to_bytes(8*W,'little'),dtype=np.uint8),bitorder='little')[:n].astype(bool)
  support[bits]|=np.uint64(1)<<np.uint64(i)
 unique=[int(x) for x in np.unique(support)];assert unique[0]>0
 clauses=[]
 for mask in unique:
  row=[]
  while mask:
   bit=mask&-mask;row.append(bit.bit_length());mask^=bit
  clauses.append(row)
 expanded=[g['variable'] for g in groups for _ in range(g['cost'])]
 countvars=len(groups);table=[]
 for _ in expanded:
  row=[]
  for j in range(16):countvars+=1;row.append(countvars)
  table.append(row)
 for i,x in enumerate(expanded):
  clauses.append([-x,table[i][0]])
  if i:
   for j in range(16):clauses.append([-table[i-1][j],table[i][j]])
   for j in range(1,16):clauses.append([-x,-table[i-1][j-1],table[i][j]])
 clauses.append([-table[-1][15]])
 cnf=OUT/f'model_{n}.cnf'
 with cnf.open('w') as f:
  f.write(f'p cnf {countvars} {len(clauses)}\n')
  for row in clauses:f.write(' '.join(map(str,row))+' 0\n')
 dims={'n':n,'D':D,'group_variables':len(groups),'expanded_cardinality_inputs':len(expanded),'unique_cover_rows':len(unique),'variables':countvars,'clauses':len(clauses),'cached_pins':len(wanted)}
 (OUT/f'model_{n}.json').write_text(json.dumps(dims,indent=2)+'\n')
 def limits():resource.setrlimit(resource.RLIMIT_CPU,(7,8));resource.setrlimit(resource.RLIMIT_CORE,(0,0))
 out=OUT/f'solver_{n}.stdout';err=OUT/f'solver_{n}.stderr';before=childcpu();wall=time.monotonic()
 with out.open('w') as so,err.open('w') as se:
  proc=subprocess.Popen([str(CAD),'-t','5',str(cnf)],stdout=so,stderr=se,preexec_fn=limits)
  (OUT/'RUN_HANDLE.json').write_text(json.dumps({'status':'RUNNING','source_n':n,'pid':proc.pid})+'\n')
  try:code=proc.wait(timeout=12)
  except subprocess.TimeoutExpired:proc.kill();code=proc.wait()
 text=out.read_text();selected=[];pins=[];status='UNKNOWN'
 if 's UNSATISFIABLE' in text:status='UNSAT_RESTRICTED_CANONICAL_MODEL'
 elif 's SATISFIABLE' in text:
  vals=[]
  for line in text.splitlines():
   if line.startswith('v '):vals.extend(map(int,line[2:].split()))
  pos={x for x in vals if x>0};selected=[g for g in groups if g['variable'] in pos];pins=sorted(v for g in selected for v in g['pins'])
  assert len(pins)==len(set(pins))==sum(g['cost'] for g in selected)<=15
  chosen=sum(1<<(g['variable']-1) for g in selected);assert all(mask&chosen for mask in unique)
  cover=0
  for v in pins:cover|=balls[v]
  assert cover==(1<<n)-1
  status='SAT_LITERAL_NEIGHBOR_SET_CACHE_VERIFIED'
  (OUT/f'HIT_{n}.json').write_text(json.dumps({'status':status,'source_n':n,'source_D':D,'target_n':n+1,'target_max_degree':15,'full_neighbor_set':pins,'groups':selected,'complete_cached_R_covered':n,'new_graph_exported':False},indent=2)+'\n')
 result={**dims,'status':status,'solver_return_code':code,'solver_CPU_seconds':childcpu()-before,'solver_wall_seconds':time.monotonic()-wall,'selected_pins':pins,'candidate_sets':int(bool(pins)),'new_graphs':0,'new_balls':0,'source_BFS':0}
 results.append(result);print(json.dumps(result),flush=True)
(OUT/'RUN_HANDLE.json').write_text(json.dumps({'status':'TERMINAL','pending':[]})+'\n')
result={'status':'TERMINAL_TWO_CANONICAL_MODELS','sources':results,'aggregate_CPU_seconds':childcpu()+time.process_time()-START,'new_balls':0,'source_BFS':0,'solver_calls':len(results),'new_graphs':0,'pending':[]}
(OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
