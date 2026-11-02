import json
import pathlib
import resource
import subprocess
import time

D=pathlib.Path(__file__).resolve().parent
def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF)
    b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start=cpu()
wall=time.monotonic()
literal=D/'source1428361.author.adjlist.txt'
assert literal.exists()
(D/'checkpoint.json').write_text(json.dumps({'status':'COMPILING_EXACTSOURCE_PROFILE','actual_source_file':literal.name,'source_BFS':0},indent=2)+'\n')
compiled=subprocess.run(['g++','-O3','-std=c++17',str(D/'profile.cpp'),'-o',str(D/'profile')],text=True,capture_output=True)
(D/'compile.log').write_text(compiled.stdout+compiled.stderr)
compiled.check_returncode()
compile_cpu=cpu()-start
(D/'checkpoint.json').write_text(json.dumps({'status':'ACTUAL1428361_NATIVE_PROFILE_RUNNING','native_CPU_hard_limit':10,'source_BFS':0},indent=2)+'\n')
run=subprocess.run([str(D/'profile'),str(literal),str(D)],text=True,capture_output=True)
(D/'profile.log').write_text(run.stdout+run.stderr)
if run.returncode:
    result={'status':'UNKNOWN_PROFILE_PROCESS_EXIT','returncode':run.returncode,'source_n_expected':1428361,'actual_D':None,'source_BFS_roots':0}
else:
    result=json.loads((D/'SOURCE_PROFILE.json').read_text())
result.update(compile_CPU_seconds=compile_cpu,total_profile_parent_children_CPU_seconds=cpu()-start,profile_wall_seconds=time.monotonic()-wall)
receipt=json.loads((D/'SOURCE_RECEIPT.json').read_text())
result['source_decompression_CPU_seconds']=receipt['decompression_CPU_seconds']
result['profile_setup_plus_decompression_CPU_seconds']=result['total_profile_parent_children_CPU_seconds']+receipt['decompression_CPU_seconds']
(D/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(D/'checkpoint.json').write_text(json.dumps({'status':result['status'],'running':False,'result':'RESULT.json','candidate_exported':result.get('whole_neighborhood_candidate_exported',False)},indent=2)+'\n')
(D/'terminal.json').write_text(json.dumps({'status':result['status'],'running':False,'pending':[],'candidate_exported':result.get('whole_neighborhood_candidate_exported',False)},indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','n','m','Delta','free_vertex_count','free_slots','minSatN','minSatN_count','zeroSatN_count','onefault_count','whole_neighborhood_candidate_exported','native_CPU_seconds','profile_setup_plus_decompression_CPU_seconds'] if k in result}))
