import json
import pathlib
import resource
import subprocess
import time

ROOT = pathlib.Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math')
HERE = pathlib.Path(__file__).resolve().parent
def cpu():
    a = resource.getrusage(resource.RUSAGE_SELF)
    b = resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime + a.ru_stime + b.ru_utime + b.ru_stime

start_cpu, start_wall = cpu(), time.monotonic()
subprocess.run(['g++', '-std=c++17', '-O2', str(HERE / 'check.cpp'), '-o', str(HERE / 'check')], check=True)
compile_cpu = cpu() - start_cpu
with (HERE / 'RESULT.json').open('w') as output:
    subprocess.run([str(HERE / 'check')], cwd=ROOT, stdout=output, check=True)
result = json.loads((HERE / 'RESULT.json').read_text())
result['compile_cpu_seconds'] = compile_cpu
result['aggregate_cpu_seconds'] = cpu() - start_cpu
result['wall_seconds'] = time.monotonic() - start_wall
assert result['aggregate_cpu_seconds'] < 10
(HERE / 'RESULT.json').write_text(json.dumps(result, indent=2) + '\n')
terminal = {'status': 'COMPLETE_BOUNDED_NECESSARY_GATE', 'pending': [], 'roots_checked': sum(len(s['roots']) for s in result['sources']), 'aggregate_cpu_seconds': result['aggregate_cpu_seconds'], 'source_bfs_runs': 0, 'cover_graphs': 0, 'restarts': 0}
(HERE / 'TERMINAL.json').write_text(json.dumps(terminal, indent=2) + '\n')
print(json.dumps(result, indent=2))
