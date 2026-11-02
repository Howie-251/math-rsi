"""One worker; two fixed1000-proposal S36 profiles; total20 CPU incl compile."""
from pathlib import Path
import json
import math
import resource
import subprocess
import time

HERE=Path(__file__).resolve().parent
def child_cpu():
    r=resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime+r.ru_stime

def main():
    started=time.process_time();wall=time.monotonic();children=child_cpu()
    subprocess.run(['g++','-O3','-march=native','-std=c++17',str(HERE/'search.cpp'),'-o',str(HERE/'search')],check=True)
    after_compile=child_cpu()
    remaining=20-(after_compile-children)-(time.process_time()-started)
    hard=max(1,math.floor(remaining-0.1));internal=max(0.05,hard-1.0)
    def limit():
        resource.setrlimit(resource.RLIMIT_CPU,(hard,hard))
    with (HERE/'production.log').open('w') as log:
        proc=subprocess.Popen([str(HERE/'search'),str(HERE),str(internal)],stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT,text=True,bufsize=1,preexec_fn=limit)
        for line in proc.stdout:
            log.write(line);log.flush();print(line,end='',flush=True)
        code=proc.wait()
    result=HERE/'search_result.json'
    d=json.loads(result.read_text()) if result.exists() else dict(status='TERMINATED_WITHOUT_FINAL_RESULT')
    d.update(process_returncode=code,compile_CPU_seconds=after_compile-children,
             search_process_CPU_seconds=child_cpu()-after_compile,
             driver_CPU_seconds=time.process_time()-started,
             total_CPU_seconds_including_compile=child_cpu()-children+time.process_time()-started,
             wall_seconds=time.monotonic()-wall,total_CPU_budget_seconds=20,
             search_process_CPU_hard_limit_seconds=hard,workers=1,restarts=0,
             all96_incidence_permutations_independent_S36=True,
             preserved_guarantees=['simple8regular','connected','samepoint A-C distance<=3','samepoint C-C distance<=4'],
             all_crosspoint_AC_coverage_guaranteed=False,old_a_constraints_used=False,
             ordinary_final_BFS_performed=False,new_lower_bounds=0,
             pending=['root_unique_final_all1296_source_BFS'])
    (HERE/'terminal.json').write_text(json.dumps(d,indent=2)+'\n')
    print(json.dumps(d,indent=2))

if __name__=='__main__':
    main()
