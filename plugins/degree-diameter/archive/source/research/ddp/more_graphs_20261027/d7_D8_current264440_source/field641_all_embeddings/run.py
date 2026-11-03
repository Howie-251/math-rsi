import json
from pathlib import Path
import resource
import subprocess
import time
HERE=Path(__file__).resolve().parent
start=time.process_time()
capacity=json.loads((HERE.parent/'controller_capacity/RESULT.json').read_text())
assert capacity['minimum_raw_count']==4964 and capacity['first_minimum_slot']==2
assert capacity['prefix_count']==2351462
(HERE/'EXECUTION_MODEL.json').write_text(json.dumps({
 'source_files_owned_by':'debruijn source parentdirectory;producer does not overwrite',
 'paper_VALID_before_run':True,'operation':'AUTHOR LEFT law(n,I)(m,J)=(n+rho^I*m,I+J)',
 'phase_modulus':40,'normal_moduli':[11,641],'action11':6,
 'positive_phases':[4,9,6],'positive_normal11':[1,3,9],'positive_field_integer':[1,-53,234],
 'involution':[20,0,0],'target_field_actions':'all16 exactorder40 beta,beta40=1,beta20!=1,beta8!=1',
 'predeclared_thin_slot':{'id':2,'phase':0,'normal11':2,'raw_routes':4964},
 'inherited_capacity':str(HERE.parent/'controller_capacity/RESULT.json'),
 'source_BFS':0,'target_n':282040,'target_m':987140,'native_CPU_hard_limit_seconds':20,
 'negative_distance_scope':'closed identity R8 only;exactglobalDnull',
 'positive_distance_scope':'complete identity distances fromactualhistogram;Cayley givesglobalD'
},indent=2)+'\n')
before=resource.getrusage(resource.RUSAGE_CHILDREN)
cc=subprocess.run(['g++','-O3','-std=c++17',str(HERE/'probe.cpp'),'-o',str(HERE/'probe')],capture_output=True,text=True)
(HERE/'compile.log').write_text(cc.stdout+cc.stderr)
assert cc.returncode==0
compiled=resource.getrusage(resource.RUSAGE_CHILDREN)
(HERE/'RUN_HANDLE.json').write_text(json.dumps({'status':'RUNNING_NATIVE_ALL16','hard_CPU_seconds':20},indent=2)+'\n')
run=subprocess.run([str(HERE/'probe'),'2','4964',str(HERE)],capture_output=True,text=True)
(HERE/'run.log').write_text(run.stdout+run.stderr)
after=resource.getrusage(resource.RUSAGE_CHILDREN)
def cpu(r):return r.ru_utime+r.ru_stime
receipt={'native_exit_code':run.returncode,'compile_CPU_seconds':cpu(compiled)-cpu(before),'native_process_CPU_seconds':cpu(after)-cpu(compiled),'driver_CPU_seconds':time.process_time()-start}
if run.returncode==0:
 result=json.loads((HERE/'NATIVE_RESULT.json').read_text())
else:
 rows=[json.loads(s) for s in (HERE/'CASES.jsonl').read_text().splitlines()] if (HERE/'CASES.jsonl').exists() else []
 result={'status':'UNKNOWN_CPU_LIMIT_OR_EXECUTION_ERROR','embeddings_total':16,'embeddings_processed':len(rows),'actual_implicit_graphs':sum(r['actual_graph'] for r in rows),'hits':0,'untested':16-len(rows),'actual_global_D':None,'ordinary_unordered_bad_pairs':None}
result['receipt']=receipt
result['prediction']='SUPPORTED_COMPLETE_HIT' if result.get('hits') else 'REFUTED_COMPLETE_ALL16' if result.get('embeddings_processed')==16 else 'UNKNOWN_UNTESTED_REMAIN'
(HERE/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(HERE/'RUN_HANDLE.json').write_text(json.dumps({'status':result['status'],'execution_finished':True,**receipt},indent=2)+'\n')
(HERE/'terminal.json').write_text(json.dumps({'status':result['status'],'execution_finished':True,'pending':[],'untested':result['untested'],'receipt':receipt},indent=2)+'\n')
(HERE/'THIN_IMAGE_SCHEMA.json').write_text(json.dumps({'file':'THIN_IMAGES.u8.bin','encoding':'consecutive641byte rows;value1 iff residue occurs','row_order':'processedprefixofROOTS.json roots','rows_written':result['embeddings_processed'],'thin_controller':2,'thin_phase':0,'thin_normal11':2,'equivalent_readable_encoding':'CASES.jsonl thin_missing_residues is exactcomplement'},indent=2)+'\n')
print(json.dumps(result,indent=2))
