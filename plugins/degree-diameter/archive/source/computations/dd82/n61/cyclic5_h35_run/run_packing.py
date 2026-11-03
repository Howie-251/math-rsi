"""One bounded fixed-object diagnostic; no retries."""
import json
from pathlib import Path
import resource
import subprocess
import time

root = Path(__file__).resolve().parent
assert not (root/'packing_result.json').exists(), 'Already ran fixed-H diagnostic.'


def limits():
    resource.setrlimit(resource.RLIMIT_CPU, (10, 10))
    resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
    resource.setrlimit(resource.RLIMIT_FSIZE, (16*1024**2, 16*1024**2))


before = resource.getrusage(resource.RUSAGE_CHILDREN)
start = time.monotonic()
with (root/'packing.stdout').open('w') as out, (root/'packing.stderr').open('w') as err:
    try:
        r = subprocess.run(['python', str(root/'packing.py')], stdout=out, stderr=err,
                           timeout=15, preexec_fn=limits)
        code, reason = r.returncode, 'process_exit'
    except subprocess.TimeoutExpired:
        code, reason = None, 'wall_limit'
after = resource.getrusage(resource.RUSAGE_CHILDREN)
record = dict(exit_code=code, termination=reason,
              child_cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
              wall_seconds=time.monotonic()-start, cpu_limit_seconds=10, wall_limit_seconds=15)
(root/'packing_timing.json').write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps(record))
