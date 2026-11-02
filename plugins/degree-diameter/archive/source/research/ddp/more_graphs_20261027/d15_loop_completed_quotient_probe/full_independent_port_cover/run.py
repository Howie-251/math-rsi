"""Complete all-free inversion-orbit single-vertex cover; no new balls."""
import os,time,resource
START=time.process_time();WALL=time.monotonic()
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
import json,pathlib,struct,subprocess
import numpy as np
P=pathlib.Path(__file__).resolve().parent;ROOT=pathlib.Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');BASE=ROOT/'research/ddp/more_graphs_20261027'
cr=resource.getrusage(resource.RUSAGE_CHILDREN);C0=cr.ru_utime+cr.ru_stime
pred=json.loads((P/'PREDICTION.json').read_text());assert pred['status']=='FROZEN_BEFORE_FIRST_FULL_INDEPENDENT_SAT_MODELS';assert not(P/'RESULT.json').exists()
carry=pred['budget']['carried_directions_CPU_seconds'];CAD=ROOT/'.tools/lean-4.24.0-linux/bin/cadical';assert CAD.exists()
# Preserve a large inherited hard ceiling so the explicit child42/43 limit can be set.
resource.setrlimit(resource.RLIMIT_CPU,(25,160))
def childcpu():
 r=resource.getrusage(resource.RUSAGE_CHILDREN);return r.ru_utime+r.ru_stime-C0
def used():return carry+time.process_time()-START+childcpu()
def save(name,x):(P/name).write_text(json.dumps(x,indent=2)+'\n')
def readballs(spec):
 n=spec['n'];cache=spec['cache'];W=cache['words_per_ball'];raw=(BASE/cache['file']).read_bytes();ids=[];balls=[]
 if n==15552:
  count,nn,ww=struct.unpack_from('<III',raw);assert (nn,ww)==(n,W);off=12
  for _ in range(count):
   v=struct.unpack_from('<I',raw,off)[0];off+=4;ids.append(v);balls.append(int.from_bytes(raw[off:off+8*W],'little'));off+=8*W
  assert off==len(raw)
 else:
  ids=list(map(int,(BASE/cache['row_labels']).read_text().split()));assert len(raw)==len(ids)*8*W
  balls=[int.from_bytes(raw[i*8*W:(i+1)*8*W],'little') for i in range(len(ids))]
 assert ids==spec['literal_free_ball_row_order']
 FULL=(1<<n)-1
 return ids,[b&FULL for b in balls],W
def export(spec,pins):
 n,m,D=spec['n'],spec['m'],spec['D'];out=P/'candidate';out.mkdir(exist_ok=True);graph=out/f'graph_d15_D{D}_n{n+1}.edges'
 if n==15552:
  source=BASE/'d15_D4_current15552/source15552.header.edges';degrees={v:0 for v in pins};pinset=set(pins);written=0
  with source.open()as old,graph.open('w')as new:
   assert tuple(map(int,next(old).split()))==(n,m);new.write(f'{n+1} {m+len(pins)}\n')
   for line in old:
    if line.strip():
     a,b=map(int,line.split());written+=1
     if a in pinset:degrees[a]+=1
     if b in pinset:degrees[b]+=1
     new.write(line)
   for v in pins:new.write(f'{v} {n}\n')
  assert written==m
 else:
  source=BASE/'d15_D5_current102060_source/monotone_R4_cover/source.csr.u32le.bin';data=np.fromfile(source,dtype='<u4');assert tuple(map(int,data[:2]))==(n,2*m)
  offsets=data[2:n+3];neighbors=data[n+3:];assert len(neighbors)==2*m and int(offsets[-1])==2*m
  degrees={v:int(offsets[v+1]-offsets[v]) for v in pins};written=0
  with graph.open('w')as new:
   new.write(f'{n+1} {m+len(pins)}\n')
   for u in range(n):
    for v in neighbors[int(offsets[u]):int(offsets[u+1])]:
     if u<int(v):new.write(f'{u} {int(v)}\n');written+=1
   for v in pins:new.write(f'{v} {n}\n')
  assert written==m
 assert all(degrees[v]==14 for v in pins)
 return str(graph.relative_to(ROOT)),degrees
results=[];hit=None;calls=0
for n in [15552,102060]:
 if used()>156:break
 spec=json.loads((P.parent/'full_free_directions'/f'source{n}_FREE_DIRECTION_GROUPS.json').read_text());D=spec['D'];original_groups=spec['groups']
 ids,balls,W=readballs(spec);ordered=sorted(ids);rowindex={v:i for i,v in enumerate(ids)}
 assert len(ordered)==spec['free_pin_count'] and len(set(ordered))==len(ordered)
 assert set(ordered)=={v for g in original_groups for v in g['pins']}
 groups=[{'variable':i+1,'pins':[v],'cost':1,'ball_row_indices':[rowindex[v]]} for i,v in enumerate(ordered)]
 G=len(groups);assert G==(648 if n==15552 else 810);pinvar={g['pins'][0]:g['variable'] for g in groups}
 pair_pins=sorted([tuple(sorted(g['pins'])) for g in original_groups if g['cost']==2]);assert len(pair_pins)==(312 if n==15552 else 390)
 q=spec['bin_size'];neg=spec['neg_local_offsets']
 assert all((p//q)*q+neg[p%q]==v for p,v in pair_pins)
 save(f'INPUT_{n}.json',{'n':n,'m':spec['m'],'D':D,'independent_pins_in_variable_order':ordered,'ball_row_indices':[rowindex[v] for v in ordered],'ordered_inversion_pairs':pair_pins,'cache':spec['cache'],'target_rows':'all original n, not folded','previous_invariant_UNSAT_dependency':str((P.parent/'full_inversion_port_cover/RESULT.json').relative_to(ROOT))})
 cols=[]
 for v in ordered:
  mask=balls[rowindex[v]]
  cols.append(np.unpackbits(np.frombuffer(mask.to_bytes(8*W,'little'),dtype=np.uint8),bitorder='little')[:n])
 packed=np.packbits(np.stack(cols).T,axis=1,bitorder='little')
 unique=[int.from_bytes(row.tobytes(),'little') for row in np.unique(packed,axis=0)]
 assert all(unique)
 del cols,packed
 structural=[];countvars=G;table=[]
 for x in range(1,G+1):table.append(list(range(countvars+1,countvars+17)));countvars+=16
 for i,x in enumerate(range(1,G+1)):
  structural.append([-x,table[i][0]])
  if i:
   for j in range(16):structural.append([-table[i-1][j],table[i][j]])
   for j in range(1,16):structural.append([-x,-table[i-1][j-1],table[i][j]])
 structural.append([-table[-1][15]])
 countvars+=1;prefix0=countvars;prefix=[prefix0];structural.append([prefix0])
 for low,high in pair_pins:
  x,y=pinvar[low],pinvar[high];prev=prefix[-1];countvars+=1;cur=countvars;prefix.append(cur)
  structural += [[-cur,prev],[-cur,-x,y],[-cur,x,-y],[-prev,x,y,cur],[-prev,-x,-y,cur],[-prev,x,-y]]
 structural.append([-prefix[-1]])
 cnf=P/f'model_{n}.cnf';cover_literals=0
 with cnf.open('w')as f:
  f.write(f'p cnf {countvars} {len(unique)+len(structural)}\n')
  for mask in unique:
   row=[]
   while mask:
    bit=mask&-mask;v=bit.bit_length();assert 1<=v<=G;row.append(str(v));mask^=bit
   cover_literals+=len(row);f.write(' '.join(row)+' 0\n')
  for row in structural:f.write(' '.join(map(str,row))+' 0\n')
 dims={'source_n':n,'source_m':spec['m'],'source_D':D,'independent_pin_selectors':G,'target_rows_before_dedup':n,'unique_target_rows':len(unique),'cover_literals':cover_literals,'counter_inputs':G,'ordered_inversion_pairs':len(pair_pins),'lex_prefix_variables':len(prefix),'lex_smaller_label_selected_at_first_difference':True,'asymmetry_cut_final_prefix_false':True,'negative_dependency':'previous full-invariant rawUNSAT, no prooflog certification','variables':countvars,'clauses':len(unique)+len(structural),'prep_parent_CPU_seconds':time.process_time()-START,'source_BFS':0,'new_balls':0}
 save(f'MODEL_{n}.json',dims);print('MODEL_READY '+json.dumps(dims),flush=True)
 if time.process_time()-START>24.5 or used()>156:
  results.append({**dims,'status':'UNKNOWN_PREP_OR_AGGREGATE_BUDGET','solver_calls':0});break
 limit=min(60,max(1,int(160-used()-3)))
 def solver_limits():
  resource.setrlimit(resource.RLIMIT_CPU,(min(62,limit+2),min(63,limit+3)));resource.setrlimit(resource.RLIMIT_CORE,(0,0))
 before=childcpu();sw=time.monotonic();out=P/f'solver_{n}.stdout';err=P/f'solver_{n}.stderr'
 with out.open('w')as so,err.open('w')as se:
  proc=subprocess.Popen([str(CAD),'-t',str(limit),str(cnf)],stdout=so,stderr=se,preexec_fn=solver_limits);calls+=1
  save('LIVE_HANDLE.json',{'status':'RUNNING_UNIQUE_FULL_INDEPENDENT_SOURCE_SOLVER','source_n':n,'pid':proc.pid,'CaDiCaL_seconds':limit,'OS_CPU_soft_hard':[min(62,limit+2),min(63,limit+3)],'solver_calls_total':calls});print('SOLVER_RUNNING '+json.dumps({'source_n':n,'pid':proc.pid,'seconds':limit}),flush=True)
  try:code=proc.wait(timeout=limit+10)
  except subprocess.TimeoutExpired:proc.kill();code=proc.wait()
 text=out.read_text();status='UNKNOWN';pins=[];selected=[]
 if 's UNSATISFIABLE' in text:status='SOLVER_UNSAT_FULL_ASYMMETRIC_DOMAIN_UNCERTIFIED'
 elif 's SATISFIABLE' in text:
  values=[]
  for line in text.splitlines():
   if line.startswith('v '):values.extend(map(int,line[2:].split()))
  pos={x for x in values if x>0};selected=[g for g in groups if g['variable'] in pos];pins=sorted(v for g in selected for v in g['pins'])
  assert len(pins)==len(set(pins))==len(selected)<=15
  chosen=sum(1<<(g['variable']-1) for g in selected);assert all(mask&chosen for mask in unique)
  pinset=set(pins);firstdiff=next(((lo,hi) for lo,hi in pair_pins if (lo in pinset)!=(hi in pinset)),None);assert firstdiff is not None and firstdiff[0] in pinset
  cover=0
  for v in pins:cover|=balls[rowindex[v]]
  assert cover==(1<<n)-1
  graph,degrees=export(spec,pins)
  hit={'status':'PRODUCTION_FULL_CURRENT_CACHE_COVER_AND_ACTUAL_DEGREE','source_n':n,'source_m':spec['m'],'source_D':D,'new_vertex':n,'new_n':n+1,'new_m':spec['m']+len(pins),'max_degree':15,'full_neighbor_set':pins,'old_pin_degrees':[degrees[v] for v in pins],'new_vertex_degree':len(pins),'inversion_asymmetric':True,'first_differing_inversion_pair':firstdiff,'lex_representative_valid':True,'complete_cached_radius':D-1,'complete_cached_targets':n,'all_old_edges_retained':True,'graph_file':graph,'source_allroot_BFS':0,'new_graph_BFS':0,'SAT_validity_depends_on_prior_UNSAT':False,'parent_pending':True}
  save('FIRST_HIT.json',hit);save('candidate/accepted_step.json',hit);status='SAT_FULL_CACHE_DEGREE_EDGE_EXPORT_FIRST_HIT'
 row={**dims,'status':status,'solver_return_code':code,'solver_CPU_seconds':childcpu()-before,'solver_wall_seconds':time.monotonic()-sw,'CaDiCaL_requested_seconds':limit,'selected_pins':pins,'solver_calls':1,'candidate_graphs':int(hit is not None)}
 results.append(row);save('CHECKPOINT.json',{'status':'FIRST_HIT' if hit else 'SOURCE_TERMINAL','sources':results,'aggregate_CPU_seconds':used()});print('SOURCE_DONE '+json.dumps(row),flush=True)
 if hit:break
 del structural,table,unique,balls
r={'status':'FIRST_HIT_STOP' if hit else 'TERMINAL_TWO_FULL_INDEPENDENT_MODELS' if len(results)==2 else 'UNKNOWN_AGGREGATE_BUDGET','sources':results,'first_hit':hit,'source_models_planned':2,'source_models_not_attempted':2-len(results),'solver_calls':calls,'carried_directions_CPU_seconds':carry,'children_CPU_seconds':childcpu(),'parent_CPU_seconds':time.process_time()-START,'aggregate_CPU_seconds':used(),'wall_seconds':time.monotonic()-WALL,'new_balls':0,'source_allroot_BFS':0,'candidate_graphs':int(hit is not None),'pending':[]}
save('RESULT.json',r);save('TERMINAL.json',{k:r[k] for k in ['status','solver_calls','aggregate_CPU_seconds','wall_seconds','candidate_graphs','source_models_not_attempted','pending']});save('LIVE_HANDLE.json',{'status':'TERMINAL','pending':[]});print('FINAL '+json.dumps({k:r[k] for k in ['status','solver_calls','aggregate_CPU_seconds','candidate_graphs','source_models_not_attempted']}),flush=True)
