import collections,json,pathlib,resource,struct,sys,time
from datetime import datetime,timezone
START=time.process_time();WALL=time.monotonic();resource.setrlimit(resource.RLIMIT_CPU,(10,10))
P=pathlib.Path(__file__).resolve().parent;ROOT=pathlib.Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');BASE=P.parents[1]
p=json.loads((P/'PREDICTION.json').read_text());assert p['status']=='FROZEN_BEFORE_LONGSIDE_LINE_DEGREE_GATE'
L=ROOT/'research/ddp/more_graphs_20261027/h9_baer_nonstable_global_pool/F3_lines.json';lines=json.loads(L.read_text())['records'];assert len(lines)==3640
profiles=[];allrows={};eligiblepools={}
for target in p['targets']:
 delta=target['Delta'];n=target['source_n'];cap=target['line_closure_cap']
 fold=struct.unpack('<66430H',(ROOT/target['map']).read_bytes());degree=(ROOT/target['degree']).read_bytes();assert len(degree)==n
 # Maps bind old core representatives. Appends alter currentdegrees, nottheseclasslabels.
 assert max(fold)<n
 sizehist=collections.Counter();blockhist=collections.Counter();combined=collections.Counter();elig=[];rows=[];cardinality_pass=degree_only_pass=0
 for line in lines:
  pairs=line['taupairs'];assert len(pairs)==3
  rawpairs=[x['point_ids'] for x in pairs];raw=sorted(x for pair in rawpairs for x in pair)
  assert len(set(raw))==6 and all(len(pair)==2 for pair in rawpairs) and set(raw)<=set(line['Q9point_ids10'])
  pairpins=[sorted({fold[x] for x in pair}) for pair in rawpairs]
  pins=sorted({x for pair in pairpins for x in pair});assert len(pins)==sum(map(len,pairpins))
  blocked=[x for x in pins if degree[x]>=delta];fits=len(pins)<=cap
  sizehist[len(pins)]+=1;blockhist[len(blocked)]+=1;combined[(len(pins),len(blocked))]+=1
  cardinality_pass+=fits;degree_only_pass+=not blocked
  row={'line_index':line['line_index'],'RREF_basis':line['RREF_basis'],'raw_nonF3_points6':raw,'raw_pairs3':rawpairs,'pair_actual_core_ids':pairpins,'whole_class_pins':pins,'closure_size':len(pins),'split_pairs':len(pins)-3,'pin_current_degrees':[degree[x] for x in pins],'saturated_pins':blocked,'cardinality_fits':fits,'eligible':fits and not blocked,'minimum_offline_classes':9,'remaining_slots_after_line_and_minimum9':delta-len(pins)-9}
  rows.append(row)
  if row['eligible']:elig.append(row)
 profile={'Delta':delta,'source_n':n,'source_m':target['source_m'],'degree_cache':target['degree'],'map':target['map'],'line_records':3640,'line_closure_cap':cap,'cardinality_pass':cardinality_pass,'degree_only_free_lines':degree_only_pass,'eligible_lines':len(elig),'closure_size_histogram':dict(sorted(sizehist.items())),'saturated_pin_count_histogram':dict(sorted(blockhist.items())),'size_and_blocked_histogram':[{'closure_size':s,'blocked_pins':b,'lines':c} for (s,b),c in sorted(combined.items())]}
 profiles.append(profile);allrows[str(delta)]=rows;eligiblepools[str(delta)]=elig
 (P/f'eligible_lines_d{delta}.json').write_text(json.dumps({'source_n':n,'source_m':target['source_m'],'degree_cap':delta,'records':elig},indent=2)+'\n')
 print(json.dumps(profile),flush=True)
r={'status':'COMPLETE3640_LONGSIDE_NECESSARY_GATE','timestamp_UTC':datetime.now(timezone.utc).isoformat(),'profiles':profiles,'eligible_lines_total':sum(q['eligible_lines'] for q in profiles),'prediction_disposition':'SUPPORTED_NECESSARY_GATE_ONLY' if any(q['eligible_lines'] for q in profiles) else 'REFUTED_FIXED_LONGSIDE_FOOTPRINT','new_graphs':0,'BFS':0,'R4':0,'solver_calls':0,'geometry_rebuilt':False,'nonstable_planes_enumerated':0,'projectivities_enumerated':0,'CPU_seconds':time.process_time()-START,'wall_seconds':time.monotonic()-WALL,'scope':p['scope'],'capture_screen':'clean'}
sys.path.insert(0,str(ROOT/'aris_repo/tools'));from capture_filter import screen
for name,obj in [('RESULT.json',r),('LINE_DIAGNOSTICS.json',allrows)]:
 text=json.dumps(obj,indent=2)+'\n';(P/name).write_text(text)
(P/'TERMINAL.json').write_text(json.dumps({**r,'pending':[]},indent=2)+'\n')
print(json.dumps({k:r[k] for k in ['status','eligible_lines_total','prediction_disposition','CPU_seconds','wall_seconds']}),flush=True)
