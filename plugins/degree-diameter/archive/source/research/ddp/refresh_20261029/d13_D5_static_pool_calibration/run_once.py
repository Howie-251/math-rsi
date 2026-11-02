import json
import pathlib
import resource
import subprocess
import time

ROOT=pathlib.Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math')
HERE=pathlib.Path(__file__).resolve().parent
def cpu():
    own=resource.getrusage(resource.RUSAGE_SELF)
    child=resource.getrusage(resource.RUSAGE_CHILDREN)
    return own.ru_utime+own.ru_stime+child.ru_utime+child.ru_stime
start,wall=cpu(),time.monotonic()
subprocess.run(['g++','-std=c++17','-O2',str(HERE/'check.cpp'),'-o',str(HERE/'check')],check=True)
compile_cpu=cpu()-start
with (HERE/'RESULT.json').open('w') as out:
    subprocess.run([str(HERE/'check')],cwd=ROOT,stdout=out,check=True)
x=json.loads((HERE/'RESULT.json').read_text())
x['compile_cpu_seconds']=compile_cpu
x['aggregate_cpu_seconds']=cpu()-start
x['wall_seconds']=time.monotonic()-wall
assert x['aggregate_cpu_seconds']<5
x['prediction_status']='SUPPORTED' if x['failed_sets']==0 and x['incompatible_pairs']==0 and x['port_overloads']==0 else 'REFUTED'
(HERE/'RESULT.json').write_text(json.dumps(x,indent=2)+'\n')
(HERE/'TERMINAL.json').write_text(json.dumps({'status':'COMPLETE_40_STATIC_SETS','prediction_status':x['prediction_status'],'pending':[],'aggregate_cpu_seconds':x['aggregate_cpu_seconds'],'new_graphs':0,'optimizers':0},indent=2)+'\n')
print(json.dumps({k:v for k,v in x.items() if k not in ['sets','used_ports']},indent=2))
