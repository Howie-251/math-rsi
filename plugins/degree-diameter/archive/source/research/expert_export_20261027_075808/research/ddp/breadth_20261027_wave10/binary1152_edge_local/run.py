"""Exactly two fixed finite native profiles; no producer BFS."""
from pathlib import Path
import json
import resource
import subprocess
import time

HERE=Path(__file__).resolve().parent
def child_cpu():
    r=resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime+r.ru_stime

def main():
    started=time.process_time();children=child_cpu();wall=time.monotonic()
    cap=json.loads((HERE/'capacity_screen.json').read_text())
    assert cap['status']=='PASS_NECESSARY_ONLY'
    subprocess.run(['g++','-O3','-march=native','-std=c++17',str(HERE/'search.cpp'),'-o',str(HERE/'search')],check=True)
    compiled=child_cpu()
    def hard_limit():resource.setrlimit(resource.RLIMIT_CPU,(20,20))
    with (HERE/'production.log').open('w') as log:
        p=subprocess.Popen([str(HERE/'search'),str(HERE),'18'],stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT,text=True,bufsize=1,preexec_fn=hard_limit)
        for line in p.stdout:
            log.write(line);log.flush();print(line,end='',flush=True)
        code=p.wait()
    path=HERE/'search_result.json'
    result=json.loads(path.read_text()) if path.exists() else dict(status='NATIVE_TERMINATED_WITHOUT_FINAL_RESULT')
    plan=json.loads((HERE/'encoding_and_plan.json').read_text())
    result.update(process_returncode=code,compile_CPU_seconds=compiled-children,
                  native_process_CPU_seconds=child_cpu()-compiled,driver_CPU_seconds=time.process_time()-started,
                  preparation_CPU_seconds=plan['preparation_CPU_seconds'],
                  total_measured_CPU_seconds=child_cpu()-children+time.process_time()-started+plan['preparation_CPU_seconds'],
                  wall_seconds_compile_and_search=time.monotonic()-wall,native_CPU_hard_seconds=20,
                  workers=1,restarts=0,new_lower_bounds=0,producer_BFS_performed=False,
                  pending=['root_unique_final_all1152_source_BFS'])
    (HERE/'terminal.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

if __name__=='__main__':main()
