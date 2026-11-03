"""One native full-geometry degree-only single-fault enumeration; no cover search."""
from pathlib import Path
import json,subprocess,resource,time
H=Path(__file__).resolve().parent;ROOT=H.parents[3];start=time.perf_counter();before=resource.getrusage(resource.RUSAGE_CHILDREN)
assert not(H/'terminal.json').exists(),'This degree-only pool task is already terminal'
subprocess.run(['g++','-O3','-std=c++17',str(H/'enumerate.cpp'),'-o',str(H/'enumerate')],check=True)
after=resource.getrusage(resource.RUSAGE_CHILDREN);compileCPU=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
meta=json.loads((H/'source_mapping.json').read_text());limit=min(5.5,max(.1,9.2-compileCPU))
with (H/'native.log').open('w') as out:
 p=subprocess.run([str(H/'enumerate'),str(ROOT/meta['point_coordinates']),str(ROOT/meta['point_to_core']),str(H/'current_degree.u8.bin'),str(H),str(limit)],stdout=out,stderr=subprocess.STDOUT,timeout=12)
end=resource.getrusage(resource.RUSAGE_CHILDREN);r=json.loads((H/'native_result.json').read_text()) if (H/'native_result.json').exists() else dict(status='NATIVE_EXIT_PARTIAL_NO_COMPLETE_JSON')
r.update(process_returncode=p.returncode,compile_CPU_seconds=compileCPU,measured_children_CPU_seconds=end.ru_utime+end.ru_stime-before.ru_utime-before.ru_stime,wall_seconds=time.perf_counter()-start,old_incidence_WL_rebuilt=False)
(H/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n');(H/'terminal.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
