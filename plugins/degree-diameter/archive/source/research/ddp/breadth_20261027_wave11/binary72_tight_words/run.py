from pathlib import Path
import json
import resource
import subprocess
import time

P=Path(__file__).resolve().parent
def childcpu():
    r=resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime+r.ru_stime

def main():
    started=time.process_time();c0=childcpu();wall=time.monotonic()
    subprocess.run(['g++','-O3','-march=native','-std=c++17',str(P/'search.cpp'),'-o',str(P/'search')],check=True)
    compiled=childcpu()
    def limit():resource.setrlimit(resource.RLIMIT_CPU,(20,20))
    with (P/'production.log').open('w') as log:
        p=subprocess.run([str(P/'search'),str(P),'18'],stdout=log,stderr=subprocess.STDOUT,preexec_fn=limit)
    result=P/'search_result.json'
    x=json.loads(result.read_text()) if result.exists() else dict(status='NATIVE_TERMINATED_WITHOUT_RESULT')
    x.update(process_returncode=p.returncode,compile_CPU_seconds=compiled-c0,
             native_process_CPU_seconds=childcpu()-compiled,driver_CPU_seconds=time.process_time()-started,
             total_CPU_seconds_compile_and_enumeration=childcpu()-c0+time.process_time()-started,
             wall_seconds_compile_and_enumeration=time.monotonic()-wall,workers=1,restarts=0,
             native_hard_limit_seconds=20,new_lower_bounds=0,
             pending=['root_independent_required_words_and_one_candidate_rank_check'])
    if x.get('complete'):
        assert x['examined']==2419200
        assert sum(a['count'] for a in x['first_failure_words'])+x['survivors']==x['examined']
    (P/'terminal.json').write_text(json.dumps(x,indent=2)+'\n');print(json.dumps(x,indent=2))

if __name__=='__main__':main()
