"""Single bounded production call; never retries."""
import json
from pathlib import Path
import resource
import subprocess
import time

root = Path(__file__).resolve().parent
assert not (root/'result.json').exists(), 'Production output already exists; do not rerun.'


def limits():
    resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
    resource.setrlimit(resource.RLIMIT_AS, (4*1024**3, 4*1024**3))
    resource.setrlimit(resource.RLIMIT_FSIZE, (256*1024**2, 256*1024**2))


before = resource.getrusage(resource.RUSAGE_CHILDREN)
start = time.monotonic()
with (root/'production.stdout').open('w') as stdout, (root/'production.stderr').open('w') as stderr:
    try:
        result = subprocess.run([str(root/'enumerate'), str(root)], stdout=stdout,
                                stderr=stderr, timeout=45, preexec_fn=limits)
        exit_code, termination = result.returncode, 'process_exit'
    except subprocess.TimeoutExpired:
        exit_code, termination = None, 'wall_limit'
after = resource.getrusage(resource.RUSAGE_CHILDREN)
record = dict(exit_code=exit_code, termination=termination,
              child_cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
              wall_seconds=time.monotonic()-start,
              cpu_limit_seconds=30, wall_limit_seconds=45)
(root/'timing.json').write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps(record))
