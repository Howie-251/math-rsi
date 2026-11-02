import collections,json,pathlib,resource,struct,subprocess,time
P=pathlib.Path(__file__).resolve().parent;ROOT=pathlib.Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');BASE=P.parents[1];G=P.parent/'nonstable_longside_gate'
START=time.process_time();WALL=time.monotonic();cr=resource.getrusage(resource.RUSAGE_CHILDREN);C0=cr.ru_utime+cr.ru_stime
pred=json.loads((P/'PREDICTION.json').read_text());assert pred['status']=='FROZEN_BEFORE_NONSTABLE_REDEI_DEGREE_POOL_AND_CURRENT_R4';assert not(P/'RESULT.json').exists()
carry=sum(pred['budget'][k] for k in ['carried_plane_CPU_seconds','carried_affine_CPU_seconds','carried_line_gate_CPU_seconds'])
def used():
 r=resource.getrusage(resource.RUSAGE_CHILDREN);return carry+time.process_time()-START+r.ru_utime+r.ru_stime-C0
planes=json.loads((G/'NONSTABLE_PLANES64.json').read_text())['records'];patterns=json.loads((G/'AFFINE_PATTERNS.json').read_text())['records'];assert len(planes)==384 and len(patterns)==486
fold=struct.unpack('<66430H',(ROOT/'research/ddp/global_coverage_20261027/h9_quadric_line_signature/point_to_core.u16.bin').read_bytes());degree=(BASE/'accepted_d11_d12_full_neighborhood_clones/source_degrees_d12.u8.bin').read_bytes();assert len(degree)==42402
counts=collections.Counter(fold);preimage=collections.defaultdict(list)
for raw,c in enumerate(fold):preimage[c].append(raw)
allowed=[counts[c]==2 and degree[c]<12 for c in fold]
maskrows=[(int(r['mask_words_u64_decimal'][0])+(int(r['mask_words_u64_decimal'][1])<<64),r) for r in patterns]
pool={};subsetchecks=0;accepted_patterns=rawlegal=0
for plane in planes:
 grid=plane['offgrid_point_ids81'];linepins=plane['longside_whole_class_pins'];assert len(linepins)==3 and all(degree[c]<12 for c in linepins)
 available=sum(1<<i for i,p in enumerate(grid) if allowed[p])
 for mask,pattern in maskrows:
  subsetchecks+=1
  if mask&~available:continue
  accepted_patterns+=1;rawlegal+=pattern['multiplicity']
  raw15=sorted(plane['longside_nonF3_point_ids6']+[grid[i] for i in pattern['grid_indices9']]);assert len(set(raw15))==15
  pins=tuple(sorted({fold[p] for p in raw15}));assert len(pins)==12 and all(counts[c]==2 and degree[c]<12 for c in pins)
  if pins in pool:pool[pins]['raw_projectivities_merged']+=pattern['multiplicity'];continue
  raw24=sorted(x for c in pins for x in preimage[c]);assert len(raw24)==24 and set(raw15)<=set(raw24)
  pool[pins]={'mandatory_pins':list(pins),'anchor_cap':0,'pin_current_degrees':[degree[c] for c in pins],'line_index':plane['line_index'],'plane_index':plane['plane_index'],'local_plane_index':plane['local_plane_index'],'line_basis_e0_e1':plane['line_basis_e0_e1'],'complement_w':plane['complement_w'],'affine_pattern_index':pattern['pattern_index'],'projectivity_witness_Aidx_r_a_b':pattern['witness'],'raw_points15':raw15,'wholeclass_raw_preimage24':raw24,'raw_projectivities_merged':pattern['multiplicity']}
records=[]
for i,k in enumerate(sorted(pool)):
 row=pool[k];row['pool_index']=i;records.append(row)
poolmeta={'status':'COMPLETE_NONSTABLE_REDEI_CURRENT_DEGREE_POOL','source_n':42402,'source_m':245937,'planes':384,'raw_projectivities_covered':5971968,'unique_affine_pattern_subset_checks':subsetchecks,'degree_legal_pattern_placements':accepted_patterns,'degree_legal_raw_projectivities':rawlegal,'distinct_current_degree_legal_C12':len(records),'CPU_cumulative_seconds_before_R4':used()}
(P/'POOL12.json').write_text(json.dumps({**poolmeta,'records':records},indent=2)+'\n');(P/'POOL_RESULT.json').write_text(json.dumps(poolmeta,indent=2)+'\n');print(json.dumps(poolmeta),flush=True)
source=BASE/'h9_redei15/production/continuation/graphs/graph_d12_D5_n42402.edges';native=P.parent/'production/cover';assert native.exists()
(P/'items').mkdir(exist_ok=True);cases=[];calls=0;hit=None;status='COMPLETE_POOL_ALL_CURRENT_R4_FAILED' if records else 'COMPLETE_DEGREE_POOL_EMPTY'
for item in records:
 if 60-used()<7.5:status='UNKNOWN_R4_BUDGET_REMAINDER';break
 idx=item['pool_index'];prefix=P/'items'/f'pool{idx:05d}';pins=item['mandatory_pins'];pinfile=pathlib.Path(str(prefix)+'.pins.txt');pinfile.write_text(' '.join(map(str,pins))+'\n')
 with pathlib.Path(str(prefix)+'.log').open('w') as log:
  proc=subprocess.Popen([str(native),'verify',str(source),str(pinfile),str(prefix),'12'],stdout=log,stderr=log)
  (P/'LIVE_HANDLE.json').write_text(json.dumps({'status':'RUNNING_CURRENT_R4','pool_index':idx,'pid':proc.pid},indent=2)+'\n')
  try:code=proc.wait(timeout=15)
  except subprocess.TimeoutExpired:proc.kill();code=proc.wait()
 calls+=1
 if code:cases.append({'pool_index':idx,'status':'UNKNOWN_NATIVE_PROCESS','returncode':code});status='UNKNOWN_NATIVE_PROCESS';break
 check=json.loads(pathlib.Path(str(prefix)+'.json').read_text());assert check['source_n']==42402 and check['source_m']==245937 and check['pins']==pins
 assert check['status']=='FULL_SELECTED_R4_CHECK_COMPLETE' and check['pin_current_degrees']==item['pin_current_degrees']
 missing=check['missing'];core_missing=[t for t in missing if t<41356]
 row={'pool_index':idx,'status':'COMPLETE_SELECTED_R4' if not missing else 'R4_FAIL_EXTRAS','missing_count':len(missing),'core_missing_count':len(core_missing),'extra_missing_count':sum(t>=41356 for t in missing),'first_missing':missing[0] if missing else None,'native_CPU_seconds':check['CPU_seconds']}
 cases.append(row)
 if core_missing:status='CORE_COVER_COUNTEREXAMPLE_BINDING_FAILURE';break
 if missing:continue
 candidate=P/'candidate';candidate.mkdir(exist_ok=True);graph=candidate/'graph_d12_D5_n42403.edges'
 with source.open() as old,graph.open('w') as new:
  assert tuple(map(int,next(old).split()))==(42402,245937);new.write('42403 245949\n')
  for line in old:new.write(line)
  for pin in pins:new.write(f'{pin} 42402\n')
 hit={**item,'status':'PRODUCTION_COMPLETE_CURRENT_R4_AND_DEGREE','source_n':42402,'source_m':245937,'source_graph':str(source.relative_to(ROOT)),'new_vertex':42402,'new_n':42403,'new_m':245949,'anchors':[],'full_neighbor_set':pins,'complete_current_R4_covered':42402,'complete_current_R4_missing':0,'all_old_edges_retained':True,'new_vertex_degree':12,'max_degree':12,'raw_geometry':'nonstablePlane Redei15 whole-Frobenius-class block','graph_file':str(graph.relative_to(ROOT)),'native_evidence':str(pathlib.Path(str(prefix)+'.json').relative_to(ROOT)),'parent_pending':True,'source_allroot_BFS':0}
 (candidate/'accepted_step.json').write_text(json.dumps(hit,indent=2)+'\n');(P/'FIRST_HIT.json').write_text(json.dumps(hit,indent=2)+'\n');status='FIRST_HIT42403_STOP_FOR_PARENT';print(json.dumps({'status':status,'pool_index':idx,'pins':pins,'graph':str(graph)}),flush=True);break
result={'status':status,'source_n':42402,'source_m':245937,'pool_meta':poolmeta,'R4_native_calls':calls,'R4_cases':cases,'pool_items_unvisited':len(records)-len(cases),'candidate_graphs':int(hit is not None),'first_hit':hit,'solver_calls':0,'source_allroot_BFS':0,'core_BFS':0,'carried_preparation_CPU_seconds':carry,'aggregate_CPU_seconds':used(),'wall_seconds':time.monotonic()-WALL,'pending':[]}
(P/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');(P/'TERMINAL.json').write_text(json.dumps({k:result[k] for k in ['status','aggregate_CPU_seconds','wall_seconds','R4_native_calls','pool_items_unvisited','candidate_graphs','pending']},indent=2)+'\n');(P/'LIVE_HANDLE.json').write_text(json.dumps({'status':'TERMINAL','last_native_pid':proc.pid if calls else None},indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','aggregate_CPU_seconds','R4_native_calls','pool_items_unvisited','candidate_graphs']}),flush=True)
