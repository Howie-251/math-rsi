#!/usr/bin/env python3
"""Reproduce complete <=2 matching-transposition enumeration with a 20-CPU-second cap.
Compilation (once): g++ -O3 -march=native -std=c++17 petersen_route_cap_neighborhood.cpp -o petersen_route_cap_neighborhood.bin
Run this wrapper from any directory; no root-only inline script is required.
"""
import json,os,resource,subprocess,time
from pathlib import Path
HERE=Path(__file__).resolve().parent

def limits():
    resource.setrlimit(resource.RLIMIT_CPU,(19,20))
    resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))

def main():
    binary=HERE/'petersen_route_cap_neighborhood.bin'
    seed=HERE/'petersen_six_fibers.best.edges'
    prefix=HERE/'petersen_route_cap_two_switches'
    began=time.monotonic()
    with prefix.with_suffix('.log').open('w') as out:
        r=subprocess.Popen([str(binary),str(seed),str(prefix)],stdout=out,stderr=subprocess.STDOUT,preexec_fn=limits)
        _,status,usage=os.wait4(r.pid,0)
        r.returncode=os.waitstatus_to_exitcode(status)
    data={'exit_code':r.returncode,'wall_seconds':time.monotonic()-began,'user_cpu_seconds':usage.ru_utime,
          'system_cpu_seconds':usage.ru_stime,'max_rss_kib':usage.ru_maxrss,'threads':1,
          'rlimit_cpu_soft_seconds':19,'rlimit_cpu_hard_seconds':20,'address_space_limit_bytes':4*1024**3}
    prefix.with_suffix('.resources.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))
    if r.returncode:raise SystemExit(r.returncode)
    result=json.loads(prefix.with_suffix('.json').read_text())
    print(json.dumps({k:v for k,v in result.items() if k!='single_feasible_moves'},indent=2))
if __name__=='__main__':main()
