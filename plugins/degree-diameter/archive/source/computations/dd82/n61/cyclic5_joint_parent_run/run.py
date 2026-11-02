"""One production process, explicit limits, no automatic retry or old-file writes."""
import json
import os
from pathlib import Path
import resource
import subprocess
import time
from check import check_result, inherited_prefix

ROOT = Path(__file__).resolve().parent


def limits():
    os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
    resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
    resource.setrlimit(resource.RLIMIT_AS, (4*1024**3, 4*1024**3))
    resource.setrlimit(resource.RLIMIT_FSIZE, (256*1024**2, 256*1024**2))


def main():
    for name in ('result.json', 'timing.json', 'production.stdout', 'production.stderr'):
        assert not (ROOT/name).exists(), 'Production already started; this runner never retries.'
    inheritance = inherited_prefix()
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    start = time.monotonic()
    with (ROOT/'production.stdout').open('x') as stdout, (ROOT/'production.stderr').open('x') as stderr:
        try:
            process = subprocess.run([str(ROOT/'enumerate'), str(ROOT)], stdout=stdout, stderr=stderr,
                                     timeout=45, preexec_fn=limits)
            exit_code, termination = process.returncode, 'process_exit'
        except subprocess.TimeoutExpired:
            exit_code, termination = None, 'wall_limit'
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    timing = dict(exit_code=exit_code, termination=termination,
                  child_cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
                  wall_seconds=time.monotonic()-start, cpu_limit_seconds=30, wall_limit_seconds=45,
                  soft_cpu_seconds=27, soft_wall_seconds=40, cpu_count=1,
                  memory_bytes=4*1024**3, output_file_bytes=256*1024**2,
                  inherited_prefix=inheritance)
    (ROOT/'timing.json').write_text(json.dumps(timing, indent=2)+'\n')
    if not (ROOT/'result.json').exists():
        fallback = dict(status='INCOMPLETE_RESOURCE_LIMIT' if termination == 'wall_limit' or exit_code in (-9, -24, -25)
                        else 'PROCESS_ERROR', complete=False, partial_counters_unavailable=True,
                        exit_code=exit_code, termination=termination)
        (ROOT/'result.json').write_text(json.dumps(fallback, indent=2)+'\n')
    validation_cpu, validation_wall = time.process_time(), time.monotonic()
    checked = check_result()
    (ROOT/'candidate_check.json').write_text(json.dumps(checked, indent=2)+'\n')
    validation = dict(cpu_seconds=time.process_time()-validation_cpu,
                      wall_seconds=time.monotonic()-validation_wall)
    (ROOT/'validation_timing.json').write_text(json.dumps(validation, indent=2)+'\n')
    print(json.dumps(dict(timing=timing, verification_status=checked['status'])))


if __name__ == '__main__':
    main()
