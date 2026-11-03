import json,resource,subprocess,time
from pathlib import Path
HERE=Path(__file__).resolve().parent
start=time.process_time()
(HERE/'SOURCE_BASELINE.json').write_text(json.dumps({'target_Delta':9,'target_D':8,'savedL':1961496,'source_n':4522590,'source_directory':'../d10_D8_current4522590_source','source_BFS_repeated':False,'field811_action_order':45,'not_order90':True,'target_n':2262690,'target_m':10182105,'no_extra_coarse_DP_required':True},indent=2)+'\n')
before=resource.getrusage(resource.RUSAGE_CHILDREN)
cc=subprocess.run(['g++','-O3','-std=c++17',str(HERE/'probe.cpp'),'-o',str(HERE/'probe')],capture_output=True,text=True)
(HERE/'compile.log').write_text(cc.stdout+cc.stderr);assert cc.returncode==0
compiled=resource.getrusage(resource.RUSAGE_CHILDREN)
(HERE/'RUN_HANDLE.json').write_text(json.dumps({'status':'STARTING_NATIVE_ALL120','hard_native_CPU_seconds':90},indent=2)+'\n')
with (HERE/'native.log').open('w') as log:
    worker=subprocess.Popen([str(HERE/'probe'),str(HERE)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    for line in worker.stdout:log.write(line);log.flush();print(line,end='',flush=True)
    code=worker.wait()
after=resource.getrusage(resource.RUSAGE_CHILDREN)
def cpu(r):return r.ru_utime+r.ru_stime
receipt={'native_exit_code':code,'compile_CPU_seconds':cpu(compiled)-cpu(before),'native_process_CPU_seconds':cpu(after)-cpu(compiled),'driver_CPU_seconds':time.process_time()-start}
if code==0:
    result=json.loads((HERE/'NATIVE_RESULT.json').read_text())
else:
    rows=[json.loads(s) for s in (HERE/'CASES.jsonl').read_text().splitlines()] if (HERE/'CASES.jsonl').exists() else []
    cp=json.loads((HERE/'checkpoint.json').read_text()) if (HERE/'checkpoint.json').exists() else {}
    incomplete=int(cp.get('status') in ['CHECKING_CONNECTEDNESS','IN_PROGRESS_R8'] and cp.get('object_ordinal') not in {r['object_ordinal'] for r in rows})
    result={'status':'UNKNOWN_HARD_LIMIT_OR_EXECUTION_ERROR','objects_total':120,'objects_processed':len(rows),'algebraic_disconnection_rejections':sum(not r['actual_R8_graph'] for r in rows),'completed_R8_cases':sum(r['actual_R8_graph'] for r in rows),'started_incomplete_cases':incomplete,'untested':120-len(rows)-incomplete,'hits':0,'actual_global_D':None,'ordinary_unordered_bad_pairs':None,'checkpoint':cp}
result['receipt']=receipt;result['prediction']='SUPPORTED_COMPLETE_HIT' if result.get('hits') else 'REFUTED_COMPLETE_ALL120' if result.get('objects_processed')==120 else 'UNKNOWN_UNFINISHED_OBJECTS'
(HERE/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
for name in ['RUN_HANDLE.json','terminal.json']:(HERE/name).write_text(json.dumps({'status':result['status'],'execution_finished':True,'objects_processed':result['objects_processed'],'started_incomplete_cases':result['started_incomplete_cases'],'untested':result['untested'],'receipt':receipt},indent=2)+'\n')
print(json.dumps(result,indent=2),flush=True)
