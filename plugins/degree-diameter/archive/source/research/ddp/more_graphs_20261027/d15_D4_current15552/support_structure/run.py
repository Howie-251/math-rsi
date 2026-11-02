from pathlib import Path
import resource,subprocess,time,json
resource.setrlimit(resource.RLIMIT_CPU,(3,3))
P=Path(__file__).resolve().parent
assert not(P/'RESULT.json').exists()
START=time.process_time();c0=resource.getrusage(resource.RUSAGE_CHILDREN)
def cpu():
 c=resource.getrusage(resource.RUSAGE_CHILDREN)
 return time.process_time()-START+c.ru_utime+c.ru_stime-c0.ru_utime-c0.ru_stime
assert json.loads((P/'PREDICTION.json').read_text())['hard_CPU_seconds']==3
subprocess.run(['g++','-O3','-std=c++17',str(P/'counter.cpp'),'-o',str(P/'counter')],check=True)
compiled=cpu()
with(P/'counter.log').open('w')as log:
 subprocess.run([str(P/'counter'),str(P.parent),str(P)],check=True,stdout=log,stderr=log,timeout=8)
r=json.loads((P/'NATIVE_RESULT.json').read_text())
r.update(compile_CPU_seconds=compiled,total_batch_CPU_seconds=cpu(),
 prediction='SUPPORTED'if r['duplicate_excess_rows']else'REFUTED',actual_new_n=None,actual_new_D=None,ordinary_bad_unordered_pairs=None,
 source_label_repartition_trials=0,pending=[])
assert r['total_batch_CPU_seconds']<3
for fn in['RESULT.json','terminal.json']:(P/fn).write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
