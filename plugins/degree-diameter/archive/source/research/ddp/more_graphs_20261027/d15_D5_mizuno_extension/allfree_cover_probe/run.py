from pathlib import Path
import json,resource,subprocess,time
P=Path(__file__).resolve().parent
start=time.process_time()
before=resource.getrusage(resource.RUSAGE_CHILDREN)
def cpu():
 r=resource.getrusage(resource.RUSAGE_CHILDREN)
 return time.process_time()-start+r.ru_utime+r.ru_stime-before.ru_utime-before.ru_stime
assert json.loads((P/'PREDICTION.json').read_text())['status']=='FROZEN_BEFORE_ALLFREE_CACHE_AND_CONSTRUCTION'
assert not(P/'terminal.json').exists()
subprocess.run(['g++','-O3','-march=native','-std=c++17',str(P/'probe.cpp'),'-o',str(P/'probe')],check=True)
compiled=cpu()
remaining=19.5-compiled
assert remaining>1
with(P/'native.log').open('w')as log:
 answer=subprocess.run([str(P/'probe'),str(P.parent),str(P),str(remaining)],stdout=log,stderr=subprocess.STDOUT,timeout=40)
r=json.loads((P/'NATIVE_RESULT.json').read_text())if(P/'NATIVE_RESULT.json').exists()else{'status':'INCOMPLETE_NATIVE_OUTPUT'}
r.update(compile_CPU_seconds=compiled,total_process_and_children_CPU_seconds=cpu(),CPU_budget_seconds=20,returncode=answer.returncode)
hit=bool(r.get('hit_pins'))
r.update(target_Delta=15,target_D=5,public_savedL=100132,hypothetical_n=100133,actual_n=100133 if hit else None,actual_D=5 if hit else None,ordinary_bad_unordered_pairs=None,graphs_generated=int(hit),source_D5_scope='Inherited published source; no old allsource repeat.',prediction_exists_verdict='SUPPORTED'if hit else'REFUTED'if r.get('unsupported_targets')else'UNRESOLVED',operational_prediction_verdict='SUPPORTED'if hit else'REFUTED'if r.get('status')in['EXACT_ALLFREE_UNSUPPORTED_TARGET','COMPLETE_FIXED64_CONSTRUCTIVE_PROBE_NO_HIT']else'UNRESOLVED',pending=[])
(P/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n')
(P/'terminal.json').write_text(json.dumps({**r,'running':False},indent=2)+'\n')
print(json.dumps({k:v for k,v in r.items()if k not in['attempts','support_histogram']},indent=2))
