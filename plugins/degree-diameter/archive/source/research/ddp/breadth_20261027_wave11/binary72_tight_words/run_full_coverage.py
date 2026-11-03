from pathlib import Path
import json
import resource
import subprocess
import time

P=Path(__file__).resolve().parent
ROOT=P.parents[3]
def childcpu():
    r=resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime+r.ru_stime

def main():
    assert not (P/'coverage_terminal.json').exists(),'Completed fixed batch must not automatically rerun.'
    src=ROOT/'research/ddp/breadth_20261027_wave5/mizuno_d4_source/controller72.labels.json'
    adj=json.loads(src.read_text())['out']
    (P/'controller.txt').write_text(''.join(' '.join(map(str,row))+'\n' for row in adj))
    started=time.process_time();c0=childcpu();wall=time.monotonic()
    subprocess.run(['g++','-O3','-march=native','-std=c++17',str(P/'full_coverage.cpp'),'-o',str(P/'full_coverage')],check=True)
    compiled=childcpu()
    def limit():resource.setrlimit(resource.RLIMIT_CPU,(20,20))
    with (P/'coverage_production.log').open('w') as log:
        p=subprocess.Popen([str(P/'full_coverage'),str(P),'18'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,
                           text=True,bufsize=1,preexec_fn=limit)
        for line in p.stdout:log.write(line);log.flush();print(line,end='',flush=True)
        code=p.wait()
    r=P/'coverage_result.json'
    x=json.loads(r.read_text()) if r.exists() else dict(status='NATIVE_TERMINATED_WITHOUT_FINAL_RESULT')
    x.update(process_returncode=code,compile_CPU_seconds=compiled-c0,native_process_CPU_seconds=childcpu()-compiled,
             driver_CPU_seconds=time.process_time()-started,total_CPU_seconds_compile_and_full_step=childcpu()-c0+time.process_time()-started,
             wall_seconds_compile_and_full_step=time.monotonic()-wall,native_hard_seconds=20,workers=1,
             new_lower_bounds=0,producer_BFS_performed=False,pending=['root_unique_final_best_all1152_source_BFS'])
    (P/'coverage_terminal.json').write_text(json.dumps(x,indent=2)+'\n');print(json.dumps(x,indent=2))

if __name__=='__main__':main()
