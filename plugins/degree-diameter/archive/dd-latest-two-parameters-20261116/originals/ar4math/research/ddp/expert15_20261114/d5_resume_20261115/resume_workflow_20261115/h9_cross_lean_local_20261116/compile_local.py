from pathlib import Path
import json, math, os, resource, signal, subprocess, time

OUT = Path(__file__).resolve().parent
AR = OUT.parents[5]
LOCAL = Path('/tmp/mathrsi-lean-runtime-20261116-9_yv1yqz/lean-4.24.0-linux')
ORIGIN = 1794800635.0  # 2026-11-16 03:43:55 UTC, first preflight observation
old = json.loads((AR / 'research/ddp/expert15_20261114/d5_resume_20261115/d12_n42403/formal/BUILD_ATTEMPT_2.json').read_text())['LEAN_PATH']
paths = [str(LOCAL / 'lib/lean')]
for p in old.split(':'):
    if '/.tools/lean-' not in p and p not in paths:
        paths.append(p)
env = dict(os.environ)
env.pop('LEAN_SRC_PATH', None)
env.update(LEAN_PATH=':'.join(paths), LEAN_SYSROOT=str(LOCAL), OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1')
cmd = [str(LOCAL / 'bin/lean'), '-j1', '-M2048', 'DegreeDiameter/Portfolio/H9CrossRouting.lean', '-o', str(OUT / 'H9CrossRouting.olean')]
def usage():
    r = resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time() + r.ru_utime + r.ru_stime
start_cpu = usage()
start_wall = time.monotonic()
task = dict(command=cmd, cwd=str(AR / 'formal'), LEAN_PATH=env['LEAN_PATH'], LEAN_SYSROOT=env['LEAN_SYSROOT'], CPU_cap=20, wall_cap=120, first_observation_UTC='2026-11-16 03:43:55 UTC', previous_runtime_test_separate=True, H9_source=str(AR / 'formal/DegreeDiameter/Portfolio/H9CrossRouting.lean'))
(OUT / 'TASK.json').write_text(json.dumps(task, indent=2) + '\n')
result = dict(task)
proc = None
try:
    remaining = 120 - (time.time() - ORIGIN)
    if remaining <= 0:
        raise TimeoutError('whole-task wall exhausted before compile')
    def limits():
        resource.setrlimit(resource.RLIMIT_CPU, (19, 19))
        resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
    with (OUT / 'BUILD.log').open('w') as log:
        proc = subprocess.Popen(cmd, cwd=AR / 'formal', env=env, stdout=log, stderr=subprocess.STDOUT, preexec_fn=limits, start_new_session=True)
        (OUT / 'RUN_HANDLE.json').write_text(json.dumps(dict(running=True, pid=proc.pid, driver_pid=os.getpid(), command=cmd)) + '\n')
        try:
            rc = proc.wait(timeout=remaining)
            result.update(status='COMPILED_KERNEL_MODULE' if rc == 0 else 'BUILD_FAILED', exit_code=rc)
        except subprocess.TimeoutExpired:
            os.killpg(proc.pid, signal.SIGKILL)
            proc.wait()
            result.update(status='UNKNOWN_WALL_LIMIT', exit_code=proc.returncode)
except Exception as exc:
    if proc is not None and proc.poll() is None:
        os.killpg(proc.pid, signal.SIGKILL)
        proc.wait()
    result.update(status='UNKNOWN_OR_TOOL_ERROR', error=str(exc))
finally:
    text = (OUT / 'BUILD.log').read_text() if (OUT / 'BUILD.log').exists() else ''
    axioms = [x for x in text.splitlines() if 'depends on axioms' in x or 'does not depend on any axioms' in x]
    result.update(measured_driver_and_children_CPU=usage()-start_cpu, conservative_prior_inspection_CPU=0.5,
                  conservative_task_CPU_charge=usage()-start_cpu+0.5, compile_wall=time.monotonic()-start_wall,
                  whole_task_wall=time.time()-ORIGIN, axiom_output_lines=axioms,
                  concrete_graph_Lean_closed=False, full_geometry_Lean_closed=False,
                  mathlib_copied=False, old_diameter_wrapper_run=False, running=False)
    if result['status'] == 'COMPILED_KERNEL_MODULE':
        result['axiom_checks_complete'] = len(axioms) == 5
        result['sorryAx_absent'] = 'sorryAx' not in text
    (OUT / 'BUILD_RESULT.json').write_text(json.dumps(result, indent=2) + '\n')
    (OUT / 'RUN_HANDLE.json').write_text(json.dumps(dict(running=False,status=result['status'])) + '\n')
    print(json.dumps(result), flush=True)
