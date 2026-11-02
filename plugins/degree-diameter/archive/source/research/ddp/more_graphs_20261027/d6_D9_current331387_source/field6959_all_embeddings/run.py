import json
from pathlib import Path
import resource
import subprocess
import time
HERE=Path(__file__).resolve().parent
start=time.process_time()
capacity=json.loads((HERE.parent/'controller_capacity/RESULT.json').read_text())
assert capacity['minimum_raw_count']==58581 and capacity['first_minimum_phase']==23
assert capacity['exact_prefix_count']==2929687
(HERE/'EXECUTION_MODEL.json').write_text(json.dumps({'source_gauge':'../ANALYSIS_GAUGE.json','source_paper_VALID_before_run':True,'phase_modulus':49,'target_field':6959,'positive_generators':[[1,0],[36,1],[45,1512]],'action_set':'all42 exactorder49 fieldroots','selected_thin_phase':23,'inherited_minraw':58581,'source_BFS':0,'target_graph_upper_n':340991,'target_graph_m':1022973,'native_CPU_hard_limit_seconds':20,'negative_distance_scope':'closed identity R9 only;globalDnull','first_hit_scope':'full identity distances from actualhistogram;Cayley gives globalD'},indent=2)+'\n')
before=resource.getrusage(resource.RUSAGE_CHILDREN)
cc=subprocess.run(['g++','-O3','-std=c++17',str(HERE/'probe.cpp'),'-o',str(HERE/'probe')],capture_output=True,text=True)
(HERE/'compile.log').write_text(cc.stdout+cc.stderr)
assert cc.returncode==0
compiled=resource.getrusage(resource.RUSAGE_CHILDREN)
(HERE/'RUN_HANDLE.json').write_text(json.dumps({'status':'RUNNING_NATIVE_ALL42','hard_CPU_seconds':20},indent=2)+'\n')
run=subprocess.run([str(HERE/'probe'),'23','58581',str(HERE)],capture_output=True,text=True)
(HERE/'run.log').write_text(run.stdout+run.stderr)
after=resource.getrusage(resource.RUSAGE_CHILDREN)
def cpu(r):return r.ru_utime+r.ru_stime
receipt={'native_exit_code':run.returncode,'compile_CPU_seconds':cpu(compiled)-cpu(before),'native_process_CPU_seconds':cpu(after)-cpu(compiled),'driver_CPU_seconds':time.process_time()-start}
if run.returncode==0:
 result=json.loads((HERE/'NATIVE_RESULT.json').read_text())
else:
 rows=[json.loads(s) for s in (HERE/'CASES.jsonl').read_text().splitlines()] if (HERE/'CASES.jsonl').exists() else []
 result={'status':'UNKNOWN_CPU_LIMIT_OR_EXECUTION_ERROR','embeddings_total':42,'embeddings_processed':len(rows),'actual_implicit_graphs':sum(r['actual_graph'] for r in rows),'hits':0,'untested':42-len(rows),'actual_global_D':None,'ordinary_unordered_bad_pairs':None}
result['receipt']=receipt
result['prediction']='SUPPORTED_COMPLETE_HIT' if result.get('hits') else 'REFUTED_COMPLETE_ALL42' if result.get('embeddings_processed')==42 else 'UNKNOWN_UNTESTED_REMAIN'
(HERE/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(HERE/'RUN_HANDLE.json').write_text(json.dumps({'status':result['status'],'execution_finished':True,**receipt},indent=2)+'\n')
(HERE/'terminal.json').write_text(json.dumps({'status':result['status'],'execution_finished':True,'pending':[],'untested':result['untested'],'receipt':receipt},indent=2)+'\n')
(HERE/'THIN_IMAGE_SCHEMA.json').write_text(json.dumps({'file':'THIN_IMAGES.u8.bin','encoding':'consecutive6959byte rows;value1 iff residue occurs','row_order':'processedprefixofROOTS.json roots','rows_written':result['embeddings_processed'],'thin_phase':23,'equivalent_readable_encoding':'CASES.jsonl thin_missing_residues is the exact complement'},indent=2)+'\n')
print(json.dumps(result,indent=2))
