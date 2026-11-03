"""Compile and run one finite364plane Baer pool, no coverage search."""
from pathlib import Path
import subprocess,resource,time,json
H=Path(__file__).resolve().parent;ROOT=H.parents[3];start=time.perf_counter();before=resource.getrusage(resource.RUSAGE_CHILDREN)
assert not(H/'terminal.json').exists(),'Finite Baer pool already terminal'
subprocess.run(['g++','-O3','-std=c++17',str(H/'enumerate.cpp'),'-o',str(H/'enumerate')],check=True)
compiled=resource.getrusage(resource.RUSAGE_CHILDREN);compileCPU=compiled.ru_utime+compiled.ru_stime-before.ru_utime-before.ru_stime
s=json.loads((H/'sources.json').read_text());limit=min(9.,max(.1,13.-compileCPU))
with (H/'native.log').open('w') as out:
 answer=subprocess.run([str(H/'enumerate'),str(ROOT/s['coords']),str(ROOT/s['fold11']),str(ROOT/s['fold12']),str(H/'degree11.u8.bin'),str(H/'degree12.u8.bin'),str(H),str(limit),'scope364'],stdout=out,stderr=subprocess.STDOUT,timeout=14)
end=resource.getrusage(resource.RUSAGE_CHILDREN);r=json.loads((H/'native_result.json').read_text()) if (H/'native_result.json').exists() else dict(status='NATIVE_EXIT_WITH_PARTIAL_FILES')
r.update(process_returncode=answer.returncode,compile_CPU_seconds=compileCPU,total_children_CPU_seconds=end.ru_utime+end.ru_stime-before.ru_utime-before.ru_stime,wall_seconds=time.perf_counter()-start,coverage_search=False)
(H/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n');(H/'terminal.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
