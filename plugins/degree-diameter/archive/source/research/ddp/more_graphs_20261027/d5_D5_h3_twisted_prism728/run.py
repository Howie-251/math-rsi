import json
import pathlib
import resource
import subprocess
import time

D = pathlib.Path(__file__).resolve().parent
SOURCE = D.parent / 'd4_D5_polarity_extensions/source_and_single/source364.edges'
def cpu():
    a = resource.getrusage(resource.RUSAGE_SELF)
    b = resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start = cpu()
wall = time.monotonic()
reflection = json.loads((D/'geometry_selector/REFLECTION.json').read_text())
assert reflection['status'] == 'READY_SINGLE_CANONICAL_GEOMETRIC_MATCHING'
pi = reflection['pi364']
assert len(pi) == 364
(D/'pi.txt').write_text('\n'.join(map(str,pi))+'\n')
(D/'checkpoint.json').write_text(json.dumps({'status':'COMPILING_SINGLE_FROZEN_REFLECTION','normal7':reflection['normal7'],'actual_matching_selected':True},indent=2)+'\n')
compile_run = subprocess.run(['g++','-O3','-std=c++17',str(D/'probe.cpp'),'-o',str(D/'probe')],text=True,capture_output=True)
(D/'compile.log').write_text(compile_run.stdout+compile_run.stderr)
compile_run.check_returncode()
compile_cpu = cpu()-start
(D/'checkpoint.json').write_text(json.dumps({'status':'NATIVE_RUNNING','native_CPU_hard_limit_seconds':3,'normal7':reflection['normal7']},indent=2)+'\n')
run = subprocess.run([str(D/'probe'),str(D),str(SOURCE)],text=True,capture_output=True)
(D/'native.log').write_text(run.stdout+run.stderr)
if run.returncode:
    result = dict(status='UNKNOWN_NATIVE_PROCESS_EXIT',returncode=run.returncode,actual_D=None)
else:
    result = json.loads((D/'NATIVE_RESULT.json').read_text())
result.update(
    target_Delta=5,target_D=5,savedL=650,
    source_file=str(SOURCE.relative_to(D.parents[3])),
    source_n=364,source_m=714,source_reported_D=5,
    normal7=reflection['normal7'],normal_Q=reflection['Q'],
    source_free_image_intersection=reflection['ports_image_intersection'],
    fixed_B2_ports=reflection['fixed_B2_ports'],
    candidate_reflections_graph_tested=1,
    compile_and_setup_CPU_seconds=compile_cpu,
    total_parent_children_CPU_seconds=cpu()-start,
    wall_seconds=time.monotonic()-wall,
    new_lower_bounds=int(result['status']=='COMPLETE_D5_REQUIRES_PARENT_CHECK')
)
(D/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(D/'checkpoint.json').write_text(json.dumps({'status':result['status'],'result':'RESULT.json','running':False},indent=2)+'\n')
(D/'terminal.json').write_text(json.dumps({'status':result['status'],'pending':[],'running':False,'new_lower_bounds':result['new_lower_bounds']},indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','n','m','actual_D','modified_graph_roots_R5_checked','failed_root','first_missing_cross_target','failed_root_cross_R5_missing','native_CPU_seconds','total_parent_children_CPU_seconds'] if k in result}))
