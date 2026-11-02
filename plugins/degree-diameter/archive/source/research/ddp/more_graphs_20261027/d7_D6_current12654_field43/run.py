import json
from pathlib import Path
import resource
import subprocess
import time

HERE=Path(__file__).resolve().parent
start=time.process_time()
capacity=json.loads((HERE/'controller_capacity/RESULT.json').read_text())
assert capacity['status']=='RAW_CAPACITY_PASSES' and capacity['minimum_raw_count']>=43
assert capacity['first_minimum_slot']==126 and capacity['minimum_raw_count']==152
(HERE/'EXECUTION_MODEL.json').write_text(json.dumps({
 'source_paper_status':'VALID from parent and expert before target numeric execution; source/gauge proof supplemented when written',
 'operation':'RIGHT law(j,u,v)(k,s,t)=(j+k,u*9^k+s,v*r^k+t)',
 'controller':{'phase_modulus':18,'normal_modulus':19,'action':9,'positive_phases':[17,13,10],'positive_normals':[17,11,17],'inverse_phases':[1,5,8],'inverse_normals':[18,14,15],'involution':[9,0]},
 'target_field':43,'actions':[7,37],
 'all_projective_representatives':'(1,b,c) for all b,c; (0,1,c) for all c; (0,0,1)',
 'objects':3786,'inherited_control_first':[1,18,39],
 'selected_thin_controller':{'id':126,'phase':6,'normal19':12,'raw_routes':152},
 'capacity_reused':str(HERE/'controller_capacity/RESULT.json'),
 'source_BFS':0,'compile_separate':True,'native_CPU_hard_limit_seconds':20
},indent=2)+'\n')
before=resource.getrusage(resource.RUSAGE_CHILDREN)
cc=subprocess.run(['g++','-O3','-std=c++17',str(HERE/'probe.cpp'),'-o',str(HERE/'probe')],capture_output=True,text=True)
(HERE/'compile.log').write_text(cc.stdout+cc.stderr)
assert cc.returncode==0
compiled=resource.getrusage(resource.RUSAGE_CHILDREN)
(HERE/'RUN_HANDLE.json').write_text(json.dumps({'status':'RUNNING_NATIVE_FIXED3786','hard_CPU_seconds':20,'gate':'raw152>=43 and paperVALID'},indent=2)+'\n')
run=subprocess.run([str(HERE/'probe'),'126','152',str(HERE)],capture_output=True,text=True)
(HERE/'run.log').write_text(run.stdout+run.stderr)
after=resource.getrusage(resource.RUSAGE_CHILDREN)
def cpu(r):return r.ru_utime+r.ru_stime
receipt={'exit_code':run.returncode,'compile_CPU_seconds':cpu(compiled)-cpu(before),'native_process_CPU_seconds':cpu(after)-cpu(compiled),'driver_CPU_seconds':time.process_time()-start}
if run.returncode==0:
 result=json.loads((HERE/'NATIVE_RESULT.json').read_text());result['receipt']=receipt
else:
 rows=[json.loads(s) for s in (HERE/'CASES.jsonl').read_text().splitlines()] if (HERE/'CASES.jsonl').exists() else []
 result={'status':'UNKNOWN_CPU_LIMIT_OR_EXECUTION_ERROR','exit_code':run.returncode,'objects_total':3786,'objects_processed':len(rows),'untested':3786-len(rows),'actual_implicit_graphs':sum(r['actual_graph'] for r in rows),'hits':0,'receipt':receipt,'actual_global_D':None,'ordinary_bad_unordered_pairs':None}
result['prediction']='SUPPORTED_FULL_D6_HIT' if result.get('hits') else 'REFUTED_COMPLETE_FIXED_FAMILY' if result.get('objects_processed')==3786 else 'UNKNOWN_UNTESTED_REMAIN'
(HERE/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(HERE/'RUN_HANDLE.json').write_text(json.dumps({'status':result['status'],'execution_finished':True,**receipt},indent=2)+'\n')
(HERE/'terminal.json').write_text(json.dumps({'status':result['status'],'execution_finished':True,'pending':[],'objects_processed':result.get('objects_processed'),'untested':result.get('untested'),'receipt':receipt},indent=2)+'\n')
print(json.dumps(result,indent=2))
