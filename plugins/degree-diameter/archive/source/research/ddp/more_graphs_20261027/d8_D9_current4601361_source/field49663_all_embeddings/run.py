import json,resource,subprocess,time
from pathlib import Path
HERE=Path(__file__).resolve().parent
start=time.process_time()
capacity=json.loads((HERE.parent/'controller_capacity/RESULT.json').read_text())
assert capacity['minimum_raw_count']==575896
(HERE/'SOURCE_BASELINE.json').write_text(json.dumps({'Delta':8,'D':9,'savedL':4601361,'primary_source':'../PROVENANCE.json','source_gauge':'../ANALYSIS_GAUGE.json','source_BFS_repeated':False,'target_field':49663,'target_n':4618659,'target_m':18474636,'shared_capacity_only_not_per_case_gate':575896,'target_word_enumeration':0,'int64_modular_products':True},indent=2)+'\n')
before=resource.getrusage(resource.RUSAGE_CHILDREN)
cc=subprocess.run(['g++','-O3','-std=c++17',str(HERE/'probe.cpp'),'-o',str(HERE/'probe')],capture_output=True,text=True)
(HERE/'compile.log').write_text(cc.stdout+cc.stderr);assert cc.returncode==0
compiled=resource.getrusage(resource.RUSAGE_CHILDREN)
(HERE/'RUN_HANDLE.json').write_text(json.dumps({'status':'STARTING_NATIVE_ALL60','hard_native_CPU_seconds':120},indent=2)+'\n')
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
    incomplete=int(cp.get('status')=='IN_PROGRESS' and cp.get('embedding_ordinal') not in {r['embedding_ordinal'] for r in rows})
    result={'status':'UNKNOWN_HARD_LIMIT_OR_EXECUTION_ERROR','embeddings_total':60,'completed_R9_cases':len(rows),'actual_graphs_started':len(rows)+incomplete,'started_incomplete_cases':incomplete,'untested':60-len(rows)-incomplete,'hits':0,'actual_global_D':None,'ordinary_unordered_bad_pairs':None,'checkpoint':cp}
result['receipt']=receipt
result['prediction']='SUPPORTED_COMPLETE_HIT' if result.get('hits') else 'REFUTED_COMPLETE_ALL60' if result.get('completed_R9_cases')==60 else 'UNKNOWN_UNFINISHED_EMBEDDINGS'
(HERE/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
for name in ['RUN_HANDLE.json','terminal.json']:(HERE/name).write_text(json.dumps({'status':result['status'],'execution_finished':True,'completed_R9_cases':result['completed_R9_cases'],'started_incomplete_cases':result['started_incomplete_cases'],'untested':result['untested'],'receipt':receipt},indent=2)+'\n')
print(json.dumps(result,indent=2),flush=True)
