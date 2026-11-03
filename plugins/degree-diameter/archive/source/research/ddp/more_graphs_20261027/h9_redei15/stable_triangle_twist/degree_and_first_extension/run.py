from array import array
from collections import Counter
from pathlib import Path
import json,resource,subprocess,time
P=Path(__file__).resolve().parent;ROOT=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');BASE=ROOT/'research/ddp/more_graphs_20261027';START=time.process_time();WALL=time.monotonic();r0=resource.getrusage(resource.RUSAGE_CHILDREN);C0=r0.ru_utime+r0.ru_stime
assert not(P/'RESULT.json').exists();pred=json.loads((P/'PREDICTION.json').read_text());carry=pred['budget']['orbit_process_CPU_seconds']
def used():
 c=resource.getrusage(resource.RUSAGE_CHILDREN);return carry+time.process_time()-START+c.ru_utime+c.ru_stime-C0
def save(name,r):(P/name).write_text(json.dumps(r,indent=2)+'\n')
orbit=json.loads((P.parent/'orbit.json').read_text());assert orbit['orbit_size']==702
ids15=orbit['point_indices15'];masks=[int(a)+(int(b)<<64) for a,b in orbit['mask_words_u64_decimal']]
coeff=orbit['coefficient_points_PG2F9'];word=list(map(int,(BASE/'h9_baer_nonflat_F3_pool/coefficient_points91.txt').read_text().split()));assert word[0]==91 and [word[1+3*j:4+3*j] for j in range(91)]==coeff
flats=json.loads((BASE/'h9_baer_plane_pool/planes.json').read_text())['records'];nonflats=json.loads((BASE/'h9_baer_nonflat_F3_pool/nonflat_planes.json').read_text())['records']
planes=[{'index':i,'kind':'flat','basis':r['basis_y_x_z'],'raw':r['point_ids91']} for i,r in enumerate(flats)]
planes +=[{'index':364+i,'kind':'nonflat','basis':r['RREF_basis'],'raw':r['Q9_point_ids91']} for i,r in enumerate(nonflats)];assert len(planes)==1120
info={11:dict(n=37631,m=205329,source=BASE/'h9_d11_followups/graph_d11_D5_n37631.edges',fold=BASE/'h9_other_degrees/point_to_core11.u16.bin'),12:dict(n=42402,m=245937,source=BASE/'h9_redei15/production/continuation/graphs/graph_d12_D5_n42402.edges',fold=ROOT/'research/ddp/global_coverage_20261027/h9_quadric_line_signature/point_to_core.u16.bin')}
fold={};degree={}
for d,x in info.items():
 f=array('H');f.frombytes(x['fold'].read_bytes());fold[d]=f;assert len(f)==66430
 degree[d]=(BASE/f'accepted_d11_d12_full_neighborhood_clones/source_degrees_d{d}.u8.bin').read_bytes();assert len(degree[d])==x['n']
 with x['source'].open()as stream:assert tuple(map(int,next(stream).split()))==(x['n'],x['m'])
classes={11:{},12:{}};counts={d:Counter() for d in info}
for plane in planes:
 for d in info:
  actual=[fold[d][r] for r in plane['raw']];allowed=sum(1<<i for i,v in enumerate(actual) if degree[d][v]<d)
  counts[d]['raw_parameters']+=702
  if allowed.bit_count()<15:counts[d]['planes_below15_available']+=1;continue
  for oi,mask in enumerate(masks):
   if mask&~allowed:continue
   counts[d]['degree_allowed']+=1;pins=tuple(sorted({actual[i] for i in ids15[oi]}))
   if len(pins)>d:continue
   counts[d]['cardinality_allowed']+=1
   if pins in classes[d]:classes[d][pins]['witness_multiplicity']+=1;continue
   classes[d][pins]={'pins':list(pins),'anchor_cap':d-len(pins),'mandatory_pin_count':len(pins),'current_pin_degrees':[degree[d][v] for v in pins],'witness_multiplicity':1,'plane_index':plane['index'],'plane_kind':plane['kind'],'plane_basis':plane['basis'],'orbit_index':oi,'coefficient_indices15':ids15[oi],'raw_point_ids15':[plane['raw'][i] for i in ids15[oi]],'whole_Frobenius_classes':True}
pools={}
for d in info:
 rows=[classes[d][pins] for pins in sorted(classes[d])]
 for i,row in enumerate(rows):row['pool_index']=i
 pools[d]=rows;pool={'status':'COMPLETE_NEW702_DEGREE_POOL','degree':d,'source_n':info[d]['n'],'source_m':info[d]['m'],'raw_parameters':786240,'raw_degree_allowed':counts[d]['degree_allowed'],'cardinality_allowed_occurrences':counts[d]['cardinality_allowed'],'distinct_pinsets':len(rows),'pin_count_histogram':dict(sorted(Counter(len(r['pins']) for r in rows).items())),'records':rows}
 save(f'pool{d}.json',pool);print(json.dumps({k:v for k,v in pool.items() if k!='records'}),flush=True)
save('POOL_RESULT.json',{'status':'COMPLETE_TWO_NEW702_DEGREE_POOLS','source_counts':{str(d):{'distinct_pinsets':len(pools[d]),'counts':dict(counts[d])} for d in info},'CPU_before_R4':used()})
native=BASE/'h9_redei15/production/cover';schedule=[]
for i in range(max(map(len,pools.values()),default=0)):
 for d in [11,12]:
  if i<len(pools[d]):schedule.append((d,pools[d][i]))
(P/'items').mkdir(exist_ok=True);cases=[];calls=0;hit=None;status='COMPLETE_FIXED_POOLS_NO_HIT'
for d,item in schedule:
 if 30-used()<7.5:status='UNKNOWN_COVERAGE_BUDGET';break
 n,m=info[d]['n'],info[d]['m'];source=info[d]['source'];pins=item['pins'];prefix=P/'items'/f'd{d}_pool{item["pool_index"]:05d}';pinfile=Path(str(prefix)+'.pins.txt');pinfile.write_text(' '.join(map(str,pins))+'\n')
 with Path(str(prefix)+'.log').open('w') as log:
  proc=subprocess.Popen([str(native),'prepare',str(source),str(pinfile),str(prefix),str(d)],stdout=log,stderr=log)
  save('LIVE_HANDLE.json',{'status':'RUNNING_COMPLETE_CURRENT_R4_AND_EXACT_GUARDS','pid':proc.pid,'degree':d,'pool_index':item['pool_index']})
  try:code=proc.wait(timeout=15)
  except subprocess.TimeoutExpired:proc.kill();code=proc.wait()
 calls+=1
 if code:cases.append({'degree':d,'pool_index':item['pool_index'],'status':'UNKNOWN_NATIVE_PROCESS','returncode':code});status='UNKNOWN_NATIVE_PROCESS';break
 check=json.loads(Path(str(prefix)+'.json').read_text());assert (check['source_n'],check['source_m'],check['pins'])==(n,m,pins);assert check['pin_current_degrees']==item['current_pin_degrees']
 missing=check['missing'];core=37471 if d==11 else 41356
 case={'degree':d,'pool_index':item['pool_index'],'mandatory_missing':len(missing),'core_missing':sum(t<core for t in missing),'first_missing':missing[0] if missing else None}
 if case['core_missing']:case['status']='CORE_BINDING_COUNTEREXAMPLE';cases.append(case);status='CORE_BINDING_COUNTEREXAMPLE';break
 if item['anchor_cap']==0 and missing:
  case['status']='EXACT_MANDATORY_MISSING_NO_ANCHOR_BUDGET';cases.append(case);continue
 guards=[] if not missing else check.get('exact_anchors') if check.get('exact_one_or_two_found') else None
 if guards is None:
  case['status']='EXACT_NO_ALLOWED_GUARDS' if item['anchor_cap']<2 or check.get('exact_two_complete') else 'UNKNOWN_EXACT_TWO_LIMIT';cases.append(case);continue
 assert len(guards)<=item['anchor_cap'];selected=sorted(pins+guards);assert len(set(selected))==len(selected)<=d and all(degree[d][v]<d for v in selected)
 verified=check;vp=prefix
 if guards:
  if 30-used()<1:case['status']='MASK_HIT_VERIFY_UNATTEMPTED_BUDGET';case['guards']=guards;cases.append(case);status='UNKNOWN_VERIFY_BUDGET';break
  vp=Path(str(prefix)+'_selected');pinfile.write_text(' '.join(map(str,selected))+'\n')
  with Path(str(vp)+'.log').open('w')as log:ret=subprocess.run([str(native),'verify',str(source),str(pinfile),str(vp),str(d)],stdout=log,stderr=log,timeout=15)
  calls+=1;assert ret.returncode==0;verified=json.loads(Path(str(vp)+'.json').read_text())
 assert verified['missing_count']==0 and verified['covered_count']==n
 (P/'candidate').mkdir(exist_ok=True);graph=P/'candidate'/f'graph_d{d}_D5_n{n+1}.edges'
 with source.open()as old,graph.open('w')as new:
  assert tuple(map(int,next(old).split()))==(n,m);new.write(f'{n+1} {m+len(selected)}\n')
  for line in old:new.write(line)
  for v in selected:new.write(f'{v} {n}\n')
 hit={**item,'status':'PRODUCTION_COMPLETE_CURRENT_R4_AND_DEGREE','degree':d,'source_n':n,'source_m':m,'new_vertex':n,'new_n':n+1,'new_m':m+len(selected),'source_file':str(source.relative_to(ROOT)),'mandatory_pins':pins,'anchors':guards,'full_neighbor_set':selected,'selected_old_degrees':verified['pin_current_degrees'],'new_vertex_degree':len(selected),'max_degree':d,'actual_complete_current_R4_covered':n,'actual_complete_current_R4_missing':0,'all_old_edges_retained':True,'graph_file':str(graph.relative_to(ROOT)),'native_evidence':str(Path(str(vp)+'.json').relative_to(ROOT)),'parent_pending':True}
 save('FIRST_HIT.json',hit);save('candidate/accepted_step.json',hit);case['status']='ACCEPTED_PRODUCTION_FIRST_HIT';cases.append(case);status='FIRST_HIT_STOP_FOR_PARENT';print(json.dumps({'status':status,'degree':d,'new_n':n+1,'new_m':hit['new_m'],'pins':selected,'graph':str(graph)}),flush=True);break
result={'status':status,'pools':{str(d):len(pools[d]) for d in pools},'coverage_schedule_size':len(schedule),'coverage_items_visited':len(cases),'coverage_items_unvisited':len(schedule)-len(cases),'native_calls':calls,'cases':cases,'first_hit':hit,'new_graphs':int(hit is not None),'old_source_D5_BFS':0,'solver_calls':0,'aggregate_CPU_seconds':used(),'wall_seconds':time.monotonic()-WALL,'orbit_carried_CPU_seconds':carry,'pending':[]}
save('RESULT.json',result);save('TERMINAL.json',{k:result[k] for k in ['status','aggregate_CPU_seconds','native_calls','coverage_items_visited','coverage_items_unvisited','new_graphs','pending']});save('LIVE_HANDLE.json',{'status':'TERMINAL','last_pid':proc.pid if calls else None})
print(json.dumps({k:result[k] for k in ['status','aggregate_CPU_seconds','pools','native_calls','coverage_items_visited','coverage_items_unvisited','new_graphs']}),flush=True)
