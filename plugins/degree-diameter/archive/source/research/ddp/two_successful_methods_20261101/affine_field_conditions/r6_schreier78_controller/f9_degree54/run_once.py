import json
import os
from pathlib import Path
import resource
import subprocess
import time

SCOPE=Path(__file__).resolve().parent
os.chdir(SCOPE)
started=time.process_time()
children_start=resource.getrusage(resource.RUSAGE_CHILDREN)
wall=time.time()
def spent():
    child=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-started+child.ru_utime+child.ru_stime-children_start.ru_utime-children_start.ru_stime
record={'budget_total_cpu_seconds':30,'single_worker':True,'steps':[]}
for name,command in [('prepare',['python3','prepare.py']),
                     ('compile',['g++','-O3','-std=c++17','-Wall','-Wextra','-o','generate','generate.cpp']),
                     ('generate',['./generate'])]:
    before=spent()
    with open(name+'.log','w') as log:
        result=subprocess.run(command,stdout=log,stderr=subprocess.STDOUT)
    record['steps'].append({'name':name,'returncode':result.returncode,'cpu_seconds':spent()-before})
    if result.returncode or spent()>=30: break
record['total_cpu_seconds']=spent()
record['wall_seconds']=time.time()-wall
record['all_children_terminal']=True
record['production_result']=json.loads(Path('GENERATION_RESULT.json').read_text()) if Path('GENERATION_RESULT.json').exists() else None
record['under_budget']=record['total_cpu_seconds']<30
record['status']='PRODUCTION_PASS' if record['under_budget'] and record['production_result'] and record['production_result']['status']=='PRODUCTION_PASS' else 'STOP'
Path('TERMINAL.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(record,ensure_ascii=False,indent=2))
