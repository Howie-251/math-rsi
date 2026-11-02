import time
START=time.process_time();WALL=time.time()
import csv,json,resource,subprocess,math
from pathlib import Path
D=Path(__file__).resolve().parent;BASE=D.parents[3];GEOM=D.parents[4]/'even_q8_gq_geometry_pilot'
INIT=resource.getrusage(resource.RUSAGE_CHILDREN);BUDGET=40
def cpu():
 r=resource.getrusage(resource.RUSAGE_CHILDREN)
 return time.process_time()-START+r.ru_utime+r.ru_stime-INIT.ru_utime-INIT.ru_stime
phase='small_accepted_recipe_and_preselect_BFS';steps=[]
try:
 with (GEOM/'OVOID65.tsv').open() as f:O=sorted(csv.DictReader(f,delimiter='\t'),key=lambda r:int(r['i']))
 with (GEOM/'SPREAD65.tsv').open() as f:S=sorted(csv.DictReader(f,delimiter='\t'),key=lambda r:int(r['spread']))
 assert len(O)==len(S)==65
 o=[int(r['point']) for r in O];owner=[int(r['spreadowner']) for r in O];s=[int(r['original_line']) for r in S]
 assert len(set(o))==len(set(owner))==len(set(s))==65
 diagonal=[65*i+owner[i] for i in range(65)]
 off=[h for h in range(4225) if h not in set(diagonal)][:2]
 roots=[346516+h for h in diagonal]+[346516+h for h in off]+[350741]
 (D/'PRESELECTED_BFS_ROOTS.json').write_text(json.dumps(dict(new_diagonal_indices=diagonal,new_off_indices=off,
  new_root_labels=roots,root_count=68,chosen_before_reading_candidate=True,
  oldroot_BFS=0,unmeasured_new_off_roots=4158),indent=2)+'\n')
 (D/'center_input.h').write_text('constexpr int ovoid[65]={'+','.join(map(str,o))+'};\nconstexpr int ovoid_owner[65]={'+','.join(map(str,owner))+'};\nconstexpr int spread[65]={'+','.join(map(str,s))+'};\nconstexpr int off_indices[2]={'+','.join(map(str,off))+'};\n')
 (D/'INPUT_BINDING.json').write_text(json.dumps(dict(ovoid_points=o,spread_lines=s,ovoid_owner=owner,
  center='585*o_i+S_j',oldclone='342290+h',newclone='346516+h',oldhub=346515,newhub=350741,
  field_or_geometry_revalidation=False),indent=2)+'\n')
 commands=[('compile',['g++','-std=c++17','-O2','verify.cpp','-o','verify']),
  ('validate',['./verify',str(BASE/'balanced/graph_d81_D3_n342290.edges'),str(D.parents[1]/'graph_d82_D3_n346516.edges'),str(D.parent/'graph_d83_D3_n350742.edges')])]
 for phase,cmd in commands:
  remaining=max(1,math.floor(BUDGET-cpu()-1))
  if phase=='validate':cmd.append(str(remaining-1))
  def limit():resource.setrlimit(resource.RLIMIT_CPU,(remaining,remaining+1))
  before=cpu()
  with (D/(phase+'.stdout')).open('w') as out,(D/(phase+'.stderr')).open('w') as err:
   p=subprocess.Popen(cmd,cwd=D,stdout=out,stderr=err,preexec_fn=limit)
   (D/'HANDLE.json').write_text(json.dumps(dict(pid=p.pid,phase=phase,CPU_budget_seconds=40,single_worker=True),indent=2)+'\n')
   rc=p.wait()
  steps.append(dict(phase=phase,exit_code=rc,CPU_seconds_including_driver=cpu()-before))
  assert rc==0,(phase,rc)
  assert cpu()<BUDGET
 r=json.loads((D/'RESULT.json').read_text())
 r.update(copy_block_count=2,clones_per_block=4225,total_clone_bindings=8450,
  structural_nonD2='hub N subset F, clone N subset U, F intersect U empty; actual hub BFS Walk saved',
  structural_nonD2_witness='HUB_CLONE_STRUCTURE_WITNESS.json',plain_allpair_and_two_prefix_proof='NOTE.md')
 (D/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n')
 assert (r['actual_BFS_new_diagonal_roots'],r['actual_BFS_new_off_roots'],r['actual_BFS_new_hubs'])==(65,2,1)
 terminal=dict(status=r['status'],total_CPU_seconds=cpu(),wall_seconds=time.time()-WALL,CPU_budget_seconds=40,
  single_worker=True,phases=steps,all_children_terminal=True,no_automatic_continuation=True,
  literal_streams={'H':1,'accepted346516':1,'new350742':1},both_clone_blocks_bound=8450,
  new_BFS_roots=68,old_BFS_roots=0,new_off_unmeasured=4158,
  measurement_boundary='Small accepted recipe/preselectedroots, one compile, three literal streams once each, all8450N_U bindings/degree/oldbody, only68 newroot BFS, aggregation. Interactive authoring excluded.')
 (D/'TERMINAL.json').write_text(json.dumps(terminal,indent=2)+'\n')
 (D/'HANDLE.json').write_text(json.dumps(dict(status='TERMINAL',all_children_terminal=True),indent=2)+'\n')
 print(json.dumps(terminal,indent=2))
except Exception as e:
 fail=dict(status='FAILED_OR_UNKNOWN_NO_CONTINUATION',phase=phase,error=str(e),phases=steps,total_CPU_seconds=cpu(),all_children_terminal=True)
 (D/'TERMINAL.json').write_text(json.dumps(fail,indent=2)+'\n')
 if not (D/'RESULT.json').exists():(D/'RESULT.json').write_text(json.dumps(fail,indent=2)+'\n')
 raise
