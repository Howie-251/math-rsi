from pathlib import Path
import json
import resource
import subprocess
import time

HERE = Path(__file__).resolve().parent
started = resource.getrusage(resource.RUSAGE_CHILDREN)
subprocess.run(['g++', '-O2', '-std=c++17', 'construct.cpp', '-o', 'construct'], cwd=HERE, check=True, stdout=(HERE/'compile.log').open('w'), stderr=subprocess.STDOUT)
compiled = resource.getrusage(resource.RUSAGE_CHILDREN)
def limit():
    resource.setrlimit(resource.RLIMIT_CPU, (10, 11))
with (HERE/'native.json').open('w') as output:
    result = subprocess.run(['./construct'], cwd=HERE, preexec_fn=limit, stdout=output, stderr=(HERE/'native.stderr').open('w'))
ended = resource.getrusage(resource.RUSAGE_CHILDREN)
if result.returncode:
    terminal = {'status':'EXECUTION_ERROR_OR_RESOURCE_LIMIT', 'returncode':result.returncode, 'new_lower_bound':False}
else:
    terminal = json.loads((HERE/'native.json').read_text())
    terminal.update(status='VALID_NEW_PARAMETER_HIT' if terminal['global_diameter']==4 else 'SOLE_CANDIDATE_EXACT_D5_NO_NEW_BOUND', new_lower_bound=terminal['global_diameter']==4)
terminal['compilation_CPU_seconds'] = compiled.ru_utime+compiled.ru_stime-started.ru_utime-started.ru_stime
terminal['tracked_batch_CPU_seconds'] = ended.ru_utime+ended.ru_stime-started.ru_utime-started.ru_stime
terminal['all_requested_candidate_count'] = 1
terminal['published_source_BFS_roots'] = 0
(HERE/'RESULT.json').write_text(json.dumps(terminal,indent=2)+'\n')
(HERE/'terminal.json').write_text(json.dumps({'status':terminal['status'],'running':False})+'\n')
print(json.dumps(terminal))
