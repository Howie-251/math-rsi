from datetime import datetime, timezone
import json
from pathlib import Path
import resource
import subprocess
import time

HERE=Path(__file__).resolve().parent
start=time.process_time()
before=resource.getrusage(resource.RUSAGE_CHILDREN)
(HERE/'CURRENT_MAIN_RECEIPT.json').write_text(json.dumps({
 'URL':'https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html',
 'read_UTC':datetime.now(timezone.utc).isoformat(),
 'Delta':14,'D':3,'current_value':1141,
 'evidence':'Fresh browser read: degree14 row, D3 cell * 1 141, primary href desc_g3. Asterisk does not prove actual current graph Cayley.',
 'existing_source_node':'ddp-current-d14d3-1141-source-profile-20261027',
 'exact_ledger_scope':'Existing source profile/no-spare result only; no prior balanced vertex split or critical-middle matching cache.'
},indent=2)+'\n')
cc=subprocess.run(['g++','-O3','-std=c++17',str(HERE/'analyze.cpp'),'-o',str(HERE/'analyze')],capture_output=True,text=True)
(HERE/'compile.log').write_text(cc.stdout+cc.stderr)
assert cc.returncode==0
compiled=resource.getrusage(resource.RUSAGE_CHILDREN)
(HERE/'RUN_HANDLE.json').write_text(json.dumps({'status':'RUNNING_NATIVE','hard_native_CPU_seconds':10},indent=2)+'\n')
run=subprocess.run([str(HERE/'analyze'),str(HERE.parent/'source1141.header.edges'),str(HERE)],capture_output=True,text=True)
(HERE/'run.log').write_text(run.stdout+run.stderr)
after=resource.getrusage(resource.RUSAGE_CHILDREN)
def cpu(r):return r.ru_utime+r.ru_stime
receipt={'exit_code':run.returncode,'compile_CPU_seconds':cpu(compiled)-cpu(before),'native_process_CPU_seconds':cpu(after)-cpu(compiled),'driver_CPU_seconds':time.process_time()-start}
if run.returncode==0:
 r=json.loads((HERE/'NATIVE_RESULT.json').read_text())
 r['receipt']=receipt
 r['actual_modified_n']=None;r['hypothetical_n']=1142;r['actual_modified_D']=None;r['ordinary_bad_unordered_pairs']=None
 r['split_prediction']='SUPPORTED_NECESSARY_ONLY' if r['eligible_vertices_without_singleton'] else 'REFUTED'
else:
 r={'status':'UNKNOWN_OR_EXECUTION_ERROR','receipt':receipt,'actual_modified_n':None,'actual_modified_D':None,'ordinary_bad_unordered_pairs':None}
(HERE/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n')
(HERE/'terminal.json').write_text(json.dumps({'status':r['status'],'complete':run.returncode==0,'pending':[] if run.returncode==0 else ['unfinished necessary cache'],'receipt':receipt},indent=2)+'\n')
(HERE/'RUN_HANDLE.json').write_text(json.dumps({'status':r['status'],**receipt},indent=2)+'\n')
(HERE/'CACHE_SCHEMA.json').write_text(json.dumps({
 'n':1141,'vertex_order':'actual source labels0..1140',
 'binary_files':{'A2.u16le.bin':'ordinary source length2 walk counts','A3.u16le.bin':'ordinary source length3 walk counts','FIRST_SUPPORTS.u16le.bin':'distance3 first-neighbor14-bit support;0 if not distance3'},
 'binary_encoding':'1141 by1141 row-major little-endian uint16',
 'H_bit_order':'sorted source adjacency; recorded per vertex in VERTEX_FIRST_SUPPORTS.jsonl',
 'ELIGIBLE_SPLIT_HYPEREDGES.jsonl':'one row for each v without a singleton far-first support; complete [target,mask] list',
 'EDGE_CRITICAL_MATCHINGS.jsonl':'7987lex source edges;13-bit row masks,physical L/R labels and maximum matching pairs',
 'source_distance_BFS':0,'modified_graphs':0
},indent=2)+'\n')
print(json.dumps(r,indent=2))
