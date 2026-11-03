import json
from pathlib import Path
import resource
import subprocess
import time
P=Path(__file__).resolve().parent
start=time.process_time();r0=resource.getrusage(resource.RUSAGE_CHILDREN)
def cpu():
    r=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-start+r.ru_utime+r.ru_stime-r0.ru_utime-r0.ru_stime
assert (P/'source102060.author.adjlist.txt').stat().st_size==9648601
c=subprocess.run(['g++','-O3','-std=c++17',str(P/'profile.cpp'),'-o',str(P/'profile')],capture_output=True,text=True)
(P/'compile.log').write_text(c.stdout+c.stderr);c.check_returncode();compile_cpu=cpu()
assert compile_cpu<3
r=subprocess.run([str(P/'profile'),str(P/'source102060.author.adjlist.txt'),str(P/'SOURCE_PROFILE.json')],capture_output=True,text=True)
(P/'native.log').write_text(r.stdout+r.stderr);r.check_returncode()
j=json.loads((P/'SOURCE_PROFILE.json').read_text());j.update(compile_and_driver_before_native_CPU_seconds=compile_cpu,total_parent_and_children_CPU_seconds=cpu(),source_file='source102060.author.adjlist.txt',source_file_bytes=9648601)
(P/'SOURCE_PROFILE.json').write_text(json.dumps(j,indent=2)+'\n')
assert j['total_parent_and_children_CPU_seconds']<3
print(r.stdout,end='');print('total_parent_and_children_CPU_seconds',j['total_parent_and_children_CPU_seconds'])
