import json
from pathlib import Path
import resource
import subprocess
import time
HERE=Path(__file__).resolve().parent
start=time.process_time()
capacity=json.loads((HERE/'controller_capacity/RESULT.json').read_text())
assert capacity['minimum_raw_count']==78 and capacity['first_minimum_slot']==110
assert capacity['prefix_count']==22409
(HERE/'EXECUTION_MODEL.json').write_text(json.dumps({'source_directory':'../d9_D5_current9020_source','normalization_and_connectivity_paper_VALID_before_run':True,'source_scalar61_not_executed':True,'fixed_case_counts_per_lambda':[625,125,25],'lambdas':[2,3],'objects':1550,'selected_thin_slot':{'id':110,'phase':10,'normal11':0,'raw_routes':78},'module_image_size':25,'native_CPU_hard_limit_seconds':20,'source_BFS':0,'negative_distance_scope':'closed identity R5 only;globalDnull'},indent=2)+'\n')
before=resource.getrusage(resource.RUSAGE_CHILDREN)
cc=subprocess.run(['g++','-O3','-std=c++17',str(HERE/'probe.cpp'),'-o',str(HERE/'probe')],capture_output=True,text=True)
(HERE/'compile.log').write_text(cc.stdout+cc.stderr)
assert cc.returncode==0
compiled=resource.getrusage(resource.RUSAGE_CHILDREN)
(HERE/'RUN_HANDLE.json').write_text(json.dumps({'status':'RUNNING_NATIVE_ALL1550','hard_CPU_seconds':20},indent=2)+'\n')
run=subprocess.run([str(HERE/'probe'),'110','78',str(HERE)],capture_output=True,text=True)
(HERE/'run.log').write_text(run.stdout+run.stderr)
after=resource.getrusage(resource.RUSAGE_CHILDREN)
def cpu(r):return r.ru_utime+r.ru_stime
receipt={'native_exit_code':run.returncode,'compile_CPU_seconds':cpu(compiled)-cpu(before),'native_process_CPU_seconds':cpu(after)-cpu(compiled),'driver_CPU_seconds':time.process_time()-start}
if run.returncode==0:
 result=json.loads((HERE/'NATIVE_RESULT.json').read_text())
else:
 rows=[json.loads(s) for s in (HERE/'CASES.jsonl').read_text().splitlines()] if (HERE/'CASES.jsonl').exists() else []
 result={'status':'UNKNOWN_CPU_LIMIT_OR_EXECUTION_ERROR','objects_total':1550,'objects_processed':len(rows),'actual_implicit_graphs':sum(r['actual_graph'] for r in rows),'hits':0,'untested':1550-len(rows),'actual_global_D':None,'ordinary_unordered_bad_pairs':None}
result['receipt']=receipt
result['prediction']='SUPPORTED_COMPLETE_HIT' if result.get('hits') else 'REFUTED_COMPLETE_ALL1550' if result.get('objects_processed')==1550 else 'UNKNOWN_UNTESTED_REMAIN'
(HERE/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(HERE/'RUN_HANDLE.json').write_text(json.dumps({'status':result['status'],'execution_finished':True,**receipt},indent=2)+'\n')
(HERE/'terminal.json').write_text(json.dumps({'status':result['status'],'execution_finished':True,'pending':[],'untested':result['untested'],'receipt':receipt},indent=2)+'\n')
(HERE/'THIN_IMAGE_SCHEMA.json').write_text(json.dumps({'file':'THIN_IMAGES.u32le.bin','encoding':'one little-endianuint32bitmask perprocessedobject;bit5*x+y iff modulepoint(x,y) occurs','row_order':'CASES.jsonl candidateordinal','rows_written':result['objects_processed'],'thin_controller':110,'thin_phase':10,'thin_normal11':0,'coefficient_format':'perlambda6coeffs[a2,b2,a3,b3,a4,b4];endpoint=sum(aiI+biN)vi'},indent=2)+'\n')
print(json.dumps(result,indent=2))
