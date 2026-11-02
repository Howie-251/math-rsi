import json
from pathlib import Path
import resource
import subprocess
HERE=Path(__file__).resolve().parent
before=resource.getrusage(resource.RUSAGE_CHILDREN)
cc=subprocess.run(['g++','-O3','-std=c++17',str(HERE/'verify.cpp'),'-o',str(HERE/'verify')],capture_output=True,text=True)
(HERE/'compile.log').write_text(cc.stdout+cc.stderr)
assert cc.returncode==0
compiled=resource.getrusage(resource.RUSAGE_CHILDREN)
(HERE/'COMPILE_RECEIPT.json').write_text(json.dumps({'CPU_seconds':compiled.ru_utime+compiled.ru_stime-before.ru_utime-before.ru_stime},indent=2)+'\n')
run=subprocess.run(['python',str(HERE/'worker.py')],capture_output=True,text=True)
(HERE/'worker.log').write_text(run.stdout+run.stderr)
ended=resource.getrusage(resource.RUSAGE_CHILDREN)
(HERE/'PROCESS_RECEIPT.json').write_text(json.dumps({'worker_exit_code':run.returncode,'worker_and_all_descendants_CPU_seconds':ended.ru_utime+ended.ru_stime-compiled.ru_utime-compiled.ru_stime},indent=2)+'\n')
if run.returncode and not (HERE/'RESULT.json').exists():
    (HERE/'RESULT.json').write_text(json.dumps({'status':'UNKNOWN_HARD_LIMIT_OR_EXECUTION_ERROR','worker_exit_code':run.returncode,'actual_D':None,'ordinary_bad_unordered_pairs':None,'checkpoint':'RUN_HANDLE.json'},indent=2)+'\n')
print(run.stdout)
print('worker_exit_code',run.returncode)
