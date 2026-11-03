"""One fixed two-start production batch, one native worker, no graph BFS."""
from pathlib import Path
import json
import resource
import subprocess
import sys
import time
import generate

HERE = Path(__file__).resolve().parent
started = time.perf_counter()
driver0 = time.process_time()
children0 = resource.getrusage(resource.RUSAGE_CHILDREN)
geometry = generate.generate()
before = resource.getrusage(resource.RUSAGE_CHILDREN)
build = subprocess.run(['g++','-O3','-std=c++17',str(HERE/'search.cpp'),'-o',str(HERE/'search')],capture_output=True,text=True)
(HERE/'compile.log').write_text(build.stdout+build.stderr)
assert build.returncode==0
compiled = resource.getrusage(resource.RUSAGE_CHILDREN)
compile_cpu = compiled.ru_utime+compiled.ru_stime-before.ru_utime-before.ru_stime
with (HERE/'production.log').open('w') as log:
    p = subprocess.Popen([str(HERE/'search'),str(HERE),'17'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    for line in p.stdout:
        log.write(line);log.flush();print(line,end='',flush=True)
    rc=p.wait()
after = resource.getrusage(resource.RUSAGE_CHILDREN)
assert rc==0,rc
d=json.loads((HERE/'search_result.json').read_text())
d.update(native_process_returncode=rc,
         compile_CPU_seconds=compile_cpu,
         geometry_preparation_CPU_seconds=geometry['CPU_seconds'],
         native_CPU_seconds=after.ru_utime+after.ru_stime-compiled.ru_utime-compiled.ru_stime,
         total_CPU_seconds_including_prep_compile=time.process_time()-driver0+after.ru_utime+after.ru_stime-children0.ru_utime-children0.ru_stime,
         wall_seconds=time.perf_counter()-started,
         new_lower_bounds=0,
         mechanism='W(3,5) incidence plus independent unrestricted simple2factors within point and line sides',
         source_geometry_generated_locally=True,
         initial_rule='Independent seeded shuffled Hamilton cycles on each156-vertex side; subsequent switches may split/merge cycles.',
         proposal_rule='Uniform side and two disjoint factor edges; random cross reconnection; reject existing factor edge; full graph exact radius3 objective.',
         acceptance_rule='Metropolis temperature30 to1 geometrically over1000 legal proposals per start; all best candidates retained.',
         scope='Exactly two fixed starts, at most1000 legal two-edge switches per start; no source/field/q/degree changes or further rounds.',
         pending=['root_unique_all312_ordinary_BFS_from_best.edges'])
(HERE/'terminal.json').write_text(json.dumps(d,indent=2)+'\n')
print(json.dumps({k:d[k] for k in ['status','best_bad_unordered_pairs_predicted','native_CPU_seconds','total_CPU_seconds_including_prep_compile']}))
