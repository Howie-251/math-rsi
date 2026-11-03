from pathlib import Path
import json,resource,subprocess,time
P=Path(__file__).resolve().parent
assert(P/'source100132.edges').exists()
assert not(P/'terminal.json').exists()
start=time.process_time()
before=resource.getrusage(resource.RUSAGE_CHILDREN)
def cpu():
 r=resource.getrusage(resource.RUSAGE_CHILDREN)
 return time.process_time()-start+r.ru_utime+r.ru_stime-before.ru_utime-before.ru_stime
subprocess.run(['g++','-O3','-std=c++17',str(P/'profile.cpp'),'-o',str(P/'profile')],check=True)
compiled=cpu()
with(P/'native.log').open('w')as log:
 answer=subprocess.run([str(P/'profile'),str(P/'source100132.edges'),str(P)],stdout=log,stderr=subprocess.STDOUT,timeout=8)
r=json.loads((P/'PROFILE.json').read_text())
star=json.loads((P/'SPARE_STAR_RESULT.json').read_text())
hit=bool(star['passing_prototypes'])
r.update(compile_CPU_seconds=compiled,total_process_and_children_CPU_seconds=cpu(),CPU_budget_seconds=5,returncode=answer.returncode,target_Delta=15,target_D=5,public_savedL=100132,hypothetical_n=100133,actual_n=100133 if hit else None,actual_D=5 if hit else None,ordinary_bad_unordered_pairs=None,sphere_prediction_verdict='SUPPORTED'if r['sphere_prediction_supported']else'REFUTED'if r['sample_has20_roots']else'UNRESOLVED',cover_existence_prediction_verdict='SUPPORTED'if hit else'UNRESOLVED',allfree_constructive_search_started=False,spare_star_prototypes_checked=star['prototypes_checked'],spare_star_hits=len(star['passing_prototypes']),spare_star_extra_CPU_seconds=star['extra_CPU_seconds'],source_D5_scope='Inherited published source diameter5; no old allsource BFS repeated.',pending=[])
(P/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n')
(P/'terminal.json').write_text(json.dumps({**r,'running':False},indent=2)+'\n')
print(json.dumps(r,indent=2))
