#!/usr/bin/env python3
"""One fixed-seed genuine three-edge neighborhood, under a ten-CPU-second cap."""
from pathlib import Path
import json,os,resource,subprocess,time
HERE=Path(__file__).resolve().parent
OUT=HERE/'twin58_three_switch_two_hs_deletions_run'
def limits():
    resource.setrlimit(resource.RLIMIT_CPU,(11,12))
    resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def main():
    OUT.mkdir(exist_ok=True)
    command=[str(HERE/'twin58_three_switch_two_hs_deletions.bin'),
      str(HERE/'twin59_to_58_deflation_run/component.path1.edges'),
      str(HERE/'petersen_all_matchings_run/candidate.best.edges'),str(OUT/'neighborhood')]
    start=time.monotonic()
    with (OUT/'neighborhood.log').open('w') as out:
        p=subprocess.Popen(command,stdout=out,stderr=subprocess.STDOUT,preexec_fn=limits)
        _,status,usage=os.wait4(p.pid,0);p.returncode=os.waitstatus_to_exitcode(status)
    result={'command':command,'exit_code':p.returncode,'wall_seconds':time.monotonic()-start,
      'user_cpu_seconds':usage.ru_utime,'system_cpu_seconds':usage.ru_stime,'max_rss_kib':usage.ru_maxrss,
      'threads':1,'internal_cpu_budget_seconds':10}
    (OUT/'resources.json').write_text(json.dumps(result,indent=2)+'\n')
    assert p.returncode==0;print((OUT/'neighborhood.log').read_text().strip())
if __name__=='__main__':main()
