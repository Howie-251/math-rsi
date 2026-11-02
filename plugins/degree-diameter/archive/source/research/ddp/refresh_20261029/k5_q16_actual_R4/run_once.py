#!/usr/bin/env python3
"""Explicit, single-call actual voltage enumeration. Not run by prepare.py."""
import argparse, datetime, json, math, os, resource, subprocess, time
from pathlib import Path
HERE=Path(__file__).resolve().parent

def write(name,obj):
    (HERE/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--run',action='store_true',required=True);parser.parse_args()
    assert not (HERE/'RUN_HANDLE.json').exists(), 'This is a single batch; do not restart an existing handle.'
    wall=time.monotonic()
    prep=json.loads((HERE/'PREPARE_RESULT.json').read_text())
    calibration=json.loads((HERE/'CALIBRATION.json').read_text())
    gate=json.loads((HERE.parent/'k5_actual_route_provider_gate'/'RESULT.json').read_text())
    assert prep['status']=='PREPARED_NOT_SEARCHED' and calibration['status']=='PASS'
    assert gate['passed']==30 and gate['remaining_Q16_full_assignments']==122880
    prior=prep['total_CPU_seconds']+gate['CPU_seconds']
    # Charge the root's existing provider computation too, conservatively.
    native_limit=90-prior-time.process_time()-2
    assert native_limit>0
    hard=math.ceil(native_limit)+1
    def child_limit():resource.setrlimit(resource.RLIMIT_CPU,(hard,hard))
    command=[str(HERE/'search'),str(HERE/'search_input.txt'),str(native_limit)]
    handle=dict(driver_pid=os.getpid(),command=command,whole_CPU_budget=90,
        prior_prepare_and_provider_CPU=prior,native_soft_budget_seconds=native_limit,
        native_RLIMIT_CPU_seconds=hard,reserved_driver_finish_CPU=2,
        started_UTC=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        scope=122880,automatic_restart=False)
    write('RUN_HANDLE.json',handle)
    with (HERE/'search.log').open('w')as log:
        p=subprocess.Popen(command,cwd=HERE,stdout=log,stderr=subprocess.STDOUT,preexec_fn=child_limit)
        handle['native_pid']=p.pid;write('RUN_HANDLE.json',handle)
        observations=0
        while True:
            try:code=p.wait(timeout=5);break
            except subprocess.TimeoutExpired:
                observations+=1
                write('RUN_OBSERVATION.json',dict(pid=p.pid,observation_timeouts=observations,
                    action='continue_waiting_same_PID',wall_seconds=time.monotonic()-wall))
    child=resource.getrusage(resource.RUSAGE_CHILDREN)
    native_cpu=child.ru_utime+child.ru_stime
    own=time.process_time()
    terminal_path=HERE/'NATIVE_TERMINAL.json'
    terminal=json.loads(terminal_path.read_text())if terminal_path.exists()else {}
    status=terminal.get('status','ABNORMAL_STOP_NO_NATIVE_TERMINAL')if code==0 else 'ABNORMAL_STOP'
    write('TERMINAL.json',dict(status=status,driver_pid=os.getpid(),native_pid=p.pid,returncode=code,
        prior_prepare_and_provider_CPU=prior,driver_CPU_seconds=own,native_CPU_seconds=native_cpu,
        charged_whole_CPU_seconds=prior+own+native_cpu,whole_CPU_budget=90,
        wall_seconds=time.monotonic()-wall,observation_timeouts=observations,
        numeric_calls=1,automatic_restart=False,native_terminal=terminal,
        full_graph_claimed=status=='COMPLETE_GRAPH_PASS',
        full_fixed_family_excluded=status=='COMPLETE_NO_FULL_GRAPH',
        scope='fixed K5 ports and stored F3^4 chart, ordinary Q16 voltages, actual D4 requirement'))
    print(json.dumps(json.loads((HERE/'TERMINAL.json').read_text())))

if __name__=='__main__':main()
