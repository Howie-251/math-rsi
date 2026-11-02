from pathlib import Path
import subprocess,resource,time,json
H=Path(__file__).resolve().parent;b=resource.getrusage(resource.RUSAGE_CHILDREN);start=time.perf_counter();assert not(H/'terminal.json').exists(),'Rootcover finite scope already terminal'
subprocess.run(['g++','-O3','-std=c++17',str(H/'enumerate.cpp'),'-o',str(H/'enumerate')],check=True)
c=resource.getrusage(resource.RUSAGE_CHILDREN);compileCPU=c.ru_utime+c.ru_stime-b.ru_utime-b.ru_stime
with (H/'native.log').open('w') as out:p=subprocess.run([str(H/'enumerate'),str(H)],stdout=out,stderr=subprocess.STDOUT,timeout=26)
e=resource.getrusage(resource.RUSAGE_CHILDREN);r=json.loads((H/'RESULT.json').read_text()) if (H/'RESULT.json').exists() else dict(status='PARTIAL_NATIVE_EXIT')
r.update(process_returncode=p.returncode,compile_CPU_seconds=compileCPU,total_children_CPU_seconds=e.ru_utime+e.ru_stime-b.ru_utime-b.ru_stime,wall_seconds=time.perf_counter()-start)
(H/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n');(H/'terminal.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items() if k not in ['necessary_by_omittedvertex','exact_by_omittedvertex','orphanedge_counts']},indent=2))
