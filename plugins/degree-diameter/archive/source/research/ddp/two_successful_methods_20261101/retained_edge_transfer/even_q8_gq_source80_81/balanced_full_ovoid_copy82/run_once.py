"""One explicitly authorized producer; compile+prep+one sourceparse under30CPU."""
import csv,json,os,resource,subprocess,time
from pathlib import Path
D=Path(__file__).resolve().parent;START=time.process_time();WALL=time.monotonic();BUDGET=30
assert not (D/'RESULT.json').exists(),'Existing terminal result: no automatic rerun.'
S=D.parent;G=S.parent/'even_q8_gq_geometry_pilot';gate=S.parent.parent/'public_baseline_audit/DEGREE82_BALANCED_FULL_OVOID_COPY_TARGET_GATE_20261101.json'
assert json.loads(gate.read_text())['candidate_gain']==65
(D/'INPUT_TABLES.txt').write_bytes((S/'balanced/TABLES_INPUT.txt').read_bytes())
ovoid=list(csv.DictReader((G/'OVOID65.tsv').open(),delimiter='\t'));assert len(ovoid)==65
(D/'OVOID_INPUT.txt').write_text(''.join(f"{r['i']} {r['point']} {r['spreadowner']}\n" for r in ovoid))
params={'degree_cap':82,'D_target':3,'source_file':'../balanced/graph_d81_D3_n342290.edges','source_n':342290,'source_m':13862745,'source_is_Payne':False,'accepted_source_parameters':'../balanced/PARAMETERS.json','accepted_tables':'../balanced/TABLES_INPUT.txt','ovoid_input':'../../even_q8_gq_geometry_pilot/OVOID65.tsv','spread_input':'../../even_q8_gq_geometry_pilot/SPREAD65.tsv','point_label_order':'Inherited actual balanced source PG3_POINTS.tsv','line_label_order':'Inherited actual source original_isotropic_line ID order','ovoid_point_ids':[int(r['point']) for r in ovoid],'ovoid_spread_owners':[int(r['spreadowner']) for r in ovoid],'center_label':'o_i*585+S_j','index':'65*i+j','new_label':'342290+index','immutable_N81':'linePoints[S_j] x pointLines[o_i],remove self; if j=owner(o_i) add old-source fill342225+j','n':346515,'m':14204970,'copies_each_center':1,'center_count':4225,'new_old_edges':342225,'new_new_edges':0,'predicted_pin_union':'source minus D65','predicted_old_load_histogram':{'0':65,'1':342225},'predicted_degree_histogram':{'81':4290,'82':342225},'predicted_newroot_histograms':[{'class':'diagonal','roots':65,'histogram':[1,81,5249,341184]},{'class':'offdiagonal','roots':4160,'histogram':[1,81,5329,341104]}],'newroot_predictions_verified_by_producer_BFS':False,'centers_independent_assumed':False,'predicted_center_induced_graph':'2080K2 +65isolates','output_graph':'graph_d82_D3_n346515.edges','format':'n m header; strictlex a b body,a<b; each edge once','public_gate':str(gate.resolve()),'best_located_published_guarantee':346450,'scoped_candidate_gain':65,'exactsourcefill_priority':'UNKNOWN','global_record_claim':False,'producer_budget_CPU':30,'workers':1}
(D/'PARAMETERS.json').write_text(json.dumps(params,ensure_ascii=False,indent=2)+'\n')
receipts=[]
def used():return time.process_time()-START+sum(r['CPU_seconds'] for r in receipts)
def child(name,cmd):
 remaining=BUDGET-used();assert remaining>1
 limit=max(1,int(remaining));before=resource.getrusage(resource.RUSAGE_CHILDREN);began=time.monotonic()
 def cap():resource.setrlimit(resource.RLIMIT_CPU,(limit,limit))
 with (D/(name+'.stdout')).open('w') as out,(D/(name+'.stderr')).open('w') as err:
  p=subprocess.Popen(cmd,cwd=D,stdout=out,stderr=err,preexec_fn=cap)
  (D/'HANDLE.json').write_text(json.dumps({'driver_PID':os.getpid(),'child_PID':p.pid,'stage':name,'running':True,'CPU_limit_seconds':limit,'command':cmd},indent=2)+'\n')
  try:code=p.wait(timeout=180)
  except subprocess.TimeoutExpired:p.kill();p.wait();code='wall_timeout'
 after=resource.getrusage(resource.RUSAGE_CHILDREN);cpu=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
 receipts.append({'stage':name,'command':cmd,'exit_code':code,'CPU_seconds':cpu,'wall_seconds':time.monotonic()-began})
 return code
code=child('compile',['g++','-O3','-std=c++17','produce.cpp','-o','produce'])
prod=None
if code==0:
 remaining=BUDGET-used();code=child('produce',['./produce','../balanced/graph_d81_D3_n342290.edges',str(remaining-.5)])
 if code==0:prod=json.loads((D/'produce.stdout').read_text())
result={'status':'PRODUCTION_PASS_ONE_COMPLETE_DEGREE82_GRAPH_PENDING_FRESH_ACCEPTANCE' if code==0 else 'UNKNOWN_ONE_FIXED_PRODUCTION_BATCH_STOP','producer_result':prod,'receipts':receipts,'wrapper_CPU_seconds':time.process_time()-START,'accounted_CPU_seconds':used(),'CPU_budget_seconds':30,'wall_seconds':time.monotonic()-WALL,'single_worker':True,'source_parse_count':1 if prod else None,'new_accepted_graphs':0,'new_concrete_Lean':0,'BFS_runs':0,'old_field_geometry_projection_rechecks':0,'source80_used':False,'graph83plus_generated':False,'root_counts_modified':False,'parent_source_or_Lean_modules_modified':False,'sourcefill_priority':'UNKNOWN','global_record_claim':False,'running':False,'active_processes':[]}
for f in ['RESULT.json','TERMINAL.json']:(D/f).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
(D/'HANDLE.json').write_text(json.dumps({'driver_PID':os.getpid(),'running':False,'status':result['status'],'active_processes':[]},indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False),flush=True)
if code!=0:raise SystemExit(1)
