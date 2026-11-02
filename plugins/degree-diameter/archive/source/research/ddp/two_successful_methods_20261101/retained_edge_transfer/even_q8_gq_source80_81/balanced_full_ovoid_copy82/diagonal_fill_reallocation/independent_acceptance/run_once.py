import time
START=time.process_time();WALL=time.time()
import csv,json,resource,subprocess,math
from pathlib import Path
D=Path(__file__).resolve().parent;BASE=D.parents[2];GEOM=D.parents[3]/'even_q8_gq_geometry_pilot'
INIT=resource.getrusage(resource.RUSAGE_CHILDREN);BUDGET=40
def cpu():
 r=resource.getrusage(resource.RUSAGE_CHILDREN)
 return time.process_time()-START+r.ru_utime+r.ru_stime-INIT.ru_utime-INIT.ru_stime
phase='small_ordered_input_binding';steps=[]
try:
 with (GEOM/'OVOID65.tsv').open() as f:O=sorted(csv.DictReader(f,delimiter='\t'),key=lambda r:int(r['i']))
 with (GEOM/'SPREAD65.tsv').open() as f:S=sorted(csv.DictReader(f,delimiter='\t'),key=lambda r:int(r['spread']))
 assert len(O)==len(S)==65
 o=[int(r['point']) for r in O];owner=[int(r['spreadowner']) for r in O];s=[int(r['original_line']) for r in S]
 assert len(set(o))==len(set(owner))==len(set(s))==65
 (D/'center_input.h').write_text('constexpr int ovoid[65]={'+','.join(map(str,o))+'};\nconstexpr int ovoid_owner[65]={'+','.join(map(str,owner))+'};\nconstexpr int spread[65]={'+','.join(map(str,s))+'};\n')
 (D/'INPUT_BINDING.json').write_text(json.dumps(dict(ovoid_points=o,spread_lines=s,ovoid_owner=owner,
  recipe='center585*o_i+S_j,clone342290+65i+j,diagonal iff j=actualowner[i]',
  accepted_geometry_input_only=True,field_or_geometry_revalidation=False),indent=2)+'\n')
 commands=[('compile',['g++','-std=c++17','-O2','verify.cpp','-o','verify']),
  ('validate',['./verify',str(BASE/'balanced/graph_d81_D3_n342290.edges'),str(D.parents[1]/'graph_d82_D3_n346515.edges'),str(D.parent/'graph_d82_D3_n346516.edges')])]
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
 result=json.loads((D/'RESULT.json').read_text())
 assert result['changed_diag_roots_BFS']==65 and result['hub_roots_BFS']==1 and result['off4160_roots_BFS']==0
 terminal=dict(status=result['status'],total_CPU_seconds=cpu(),wall_seconds=time.time()-WALL,
  CPU_budget_seconds=40,single_worker=True,phases=steps,all_children_terminal=True,no_automatic_continuation=True,
  literal_parse_counts={'source_H':1,'old346515_delta':1,'new346516':1},changed_BFS_roots=66,off_BFS_roots=0,old_BFS_roots=0,
  measurement_boundary='Small accepted recipe binding, one compile, three literal streams once each, full4225N_U binding/degree/delta and only66 changed-root BFS, aggregation. Interactive authoring excluded.')
 (D/'TERMINAL.json').write_text(json.dumps(terminal,indent=2)+'\n')
 (D/'HANDLE.json').write_text(json.dumps(dict(status='TERMINAL',all_children_terminal=True),indent=2)+'\n')
 print(json.dumps(terminal,indent=2))
except Exception as e:
 fail=dict(status='FAILED_OR_UNKNOWN_NO_CONTINUATION',phase=phase,error=str(e),phases=steps,total_CPU_seconds=cpu(),all_children_terminal=True)
 (D/'TERMINAL.json').write_text(json.dumps(fail,indent=2)+'\n')
 if not (D/'RESULT.json').exists():(D/'RESULT.json').write_text(json.dumps(fail,indent=2)+'\n')
 raise
