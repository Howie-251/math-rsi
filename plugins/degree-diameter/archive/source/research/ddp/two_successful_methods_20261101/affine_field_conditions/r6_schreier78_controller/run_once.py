import json
import os
from pathlib import Path
import resource
import subprocess
import time

SCOPE = Path(__file__).resolve().parent
os.chdir(SCOPE)
started_cpu = time.process_time()
started_child = resource.getrusage(resource.RUSAGE_CHILDREN)
started_wall = time.time()
def spent():
    child = resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time() - started_cpu + child.ru_utime + child.ru_stime - started_child.ru_utime - started_child.ru_stime

with open('compile.log', 'w') as log:
    compile_result = subprocess.run(['g++', '-O3', '-std=c++17', '-Wall', '-Wextra', '-o', 'search', 'search.cpp'], stdout=log, stderr=subprocess.STDOUT)
after_compile = spent()
record = {'budget_total_cpu_seconds': 10, 'single_worker': True, 'compile_returncode': compile_result.returncode,
          'compile_and_driver_cpu_seconds': after_compile}
if compile_result.returncode == 0 and after_compile < 9.8:
    with open('search.log', 'w') as log:
        run_result = subprocess.run(['./search', str(10-after_compile-0.15)], stdout=log, stderr=subprocess.STDOUT)
    record['search_returncode'] = run_result.returncode
    if Path('SEARCH_RESULT.json').exists():
        record['result'] = json.loads(Path('SEARCH_RESULT.json').read_text())
else:
    record['status'] = 'COMPILE_FAIL_OR_BUDGET'
record['total_cpu_seconds'] = spent()
record['wall_seconds'] = time.time() - started_wall
record['all_children_terminal'] = True
Path('TERMINAL.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(record, ensure_ascii=False, indent=2))
