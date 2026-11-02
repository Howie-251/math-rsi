#!/usr/bin/env python3
"""Run the two new-seed bounded unrestricted neighborhoods, saving resources."""
import json,os,resource,subprocess,time
from pathlib import Path
HERE=Path(__file__).resolve().parent
OUT=HERE/'twin_seed_unrestricted_switch_run'

def limits():
    resource.setrlimit(resource.RLIMIT_CPU,(11,12))
    resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))

def main():
    OUT.mkdir(exist_ok=True);reports=[]
    jobs=[('deflated59',HERE/'twin60_deflate59_run/candidate.best.edges',10),
          ('twin60',HERE/'petersen_all_matchings_run/candidate.best.edges',1)]
    for name,source,maxsteps in jobs:
        prefix=OUT/name;began=time.monotonic()
        with prefix.with_suffix('.log').open('w') as out:
            command=[str(HERE/'twin_seed_unrestricted_switch.bin'),str(source),str(prefix),str(maxsteps),'10']
            p=subprocess.Popen(command,stdout=out,stderr=subprocess.STDOUT,preexec_fn=limits)
            _,status,usage=os.wait4(p.pid,0);p.returncode=os.waitstatus_to_exitcode(status)
        record={'command':command,'exit_code':p.returncode,'wall_seconds':time.monotonic()-began,
                'user_cpu_seconds':usage.ru_utime,'system_cpu_seconds':usage.ru_stime,
                'max_rss_kib':usage.ru_maxrss,'threads':1,'internal_cpu_budget_seconds':10,
                'rlimit_cpu_soft_seconds':11,'rlimit_cpu_hard_seconds':12}
        prefix.with_suffix('.resources.json').write_text(json.dumps(record,indent=2)+'\n')
        assert p.returncode==0
        result=json.loads(prefix.with_suffix('.json').read_text());reports.append(result)
    print(json.dumps([{k:v for k,v in r.items() if k!='neighborhoods'}|{'neighborhood_summary':[{k:v for k,v in q.items() if k!='bad_pair_histogram'} for q in r['neighborhoods']]} for r in reports],indent=2))
if __name__=='__main__':main()
