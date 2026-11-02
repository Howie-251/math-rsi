#!/usr/bin/env python3
"""Run the four necessary H domains under one total ten-CPU-second cap."""
from pathlib import Path
import json,os,resource,subprocess,time
HERE=Path(__file__).resolve().parent
OUT=HERE/'hs58_one_delete_auxiliary_run'
def limits():
    resource.setrlimit(resource.RLIMIT_CPU,(11,12))
    resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def main():
    OUT.mkdir(exist_ok=True)
    command=[str(HERE/'hs58_one_delete_auxiliary.bin'),str(OUT/'enumeration.json')]
    start=time.monotonic()
    with (OUT/'enumeration.log').open('w') as out:
        p=subprocess.Popen(command,stdout=out,stderr=subprocess.STDOUT,preexec_fn=limits)
        _,status,usage=os.wait4(p.pid,0);p.returncode=os.waitstatus_to_exitcode(status)
    result={'command':command,'exit_code':p.returncode,'wall_seconds':time.monotonic()-start,
      'user_cpu_seconds':usage.ru_utime,'system_cpu_seconds':usage.ru_stime,'max_rss_kib':usage.ru_maxrss,
      'threads':1,'shared_internal_cpu_budget_seconds':10}
    (OUT/'resources.json').write_text(json.dumps(result,indent=2)+'\n')
    assert p.returncode==0
    print((OUT/'enumeration.log').read_text().strip());print(json.dumps(result,indent=2))
if __name__=='__main__':main()
