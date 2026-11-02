#!/usr/bin/env python3
"""Reproduce the 100-state / 5-CPU-second deterministic neutral-component task."""
from pathlib import Path
import json,os,resource,subprocess,time
HERE=Path(__file__).resolve().parent
OUT=HERE/'twin59_neutral_component_run'
def limits():
    resource.setrlimit(resource.RLIMIT_CPU,(6,7))
    resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def main():
    OUT.mkdir(exist_ok=True);prefix=OUT/'component';began=time.monotonic()
    command=[str(HERE/'twin59_neutral_component.bin'),str(HERE/'twin_seed_unrestricted_switch_run/deflated59.step1.edges'),str(prefix)]
    with prefix.with_suffix('.log').open('w') as out:
        p=subprocess.Popen(command,stdout=out,stderr=subprocess.STDOUT,preexec_fn=limits)
        _,status,usage=os.wait4(p.pid,0);p.returncode=os.waitstatus_to_exitcode(status)
    resources={'command':command,'exit_code':p.returncode,'wall_seconds':time.monotonic()-began,
      'user_cpu_seconds':usage.ru_utime,'system_cpu_seconds':usage.ru_stime,'max_rss_kib':usage.ru_maxrss,
      'threads':1,'internal_cpu_budget_seconds':5,'state_cap':100,'rlimit_cpu_soft_seconds':6,'rlimit_cpu_hard_seconds':7}
    prefix.with_suffix('.resources.json').write_text(json.dumps(resources,indent=2)+'\n')
    assert p.returncode==0
    result=json.loads(prefix.with_suffix('.json').read_text())
    print(json.dumps({k:v for k,v in result.items() if k not in ('stored_states','expansions')},indent=2))
    print(json.dumps(resources,indent=2))
if __name__=='__main__':main()
