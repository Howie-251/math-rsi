import time
START=time.process_time();WALL=time.time()
import json,math,os,resource,subprocess
from pathlib import Path
D=Path(__file__).resolve().parent
ROOT=next(p for p in D.parents if (p/'formal/DegreeDiameter/Portfolio').is_dir())
assert not (D/'TERMINAL.json').exists(), 'One-shot acceptance already terminal; no restart.'
BUDGET=120;PREP=0.0
INITIAL=resource.getrusage(resource.RUSAGE_CHILDREN)
def cpu():
 r=resource.getrusage(resource.RUSAGE_CHILDREN)
 return PREP+time.process_time()-START+r.ru_utime+r.ru_stime-INITIAL.ru_utime-INITIAL.ru_stime
def save(name,v):(D/name).write_text(json.dumps(v,indent=2)+'\n')
prep=read_prep=json.loads((D/'PREPARATION.json').read_text());PREP=prep['CPU_seconds']
source=ROOT/'research/ddp/more_graphs_20261027/d15_D4_current15552/source15552.author.adjlist.txt'
candidate=D.parent/'graph_d16_D4_n16389.edges'
steps=[];phase='preflight'
try:
 assert source.is_file() and candidate.is_file()
 assert json.loads((D.parent/'TERMINAL.json').read_text())['graph_closed']
 for phase,command in [('compile',['g++','-O3','-std=c++17','verify.cpp','-o','verify']),('validate',['./verify',str(source),str(candidate)])]:
  remaining=max(1,math.floor(BUDGET-cpu()-1))
  if phase=='validate':command.append(str(remaining-1))
  def limit():resource.setrlimit(resource.RLIMIT_CPU,(remaining,remaining+1))
  before=cpu()
  with (D/(phase+'.stdout')).open('w') as out,(D/(phase+'.stderr')).open('w') as err:
   p=subprocess.Popen(command,cwd=D,stdout=out,stderr=err,preexec_fn=limit)
   save('HANDLE.json',dict(status='RUNNING',pid=p.pid,phase=phase,total_CPU_budget=120,single_worker=True,one_all_final_root_batch=True))
   code=p.wait()
  steps.append(dict(phase=phase,exit_code=code,CPU_seconds=cpu()-before))
  assert code==0,(phase,code)
  assert cpu()<BUDGET
 result=json.loads((D/'RESULT.json').read_text())
 assert result['status']=='PASS_COMPLETE_LITERAL_AND_ALL16389_FINAL_ROOTS_EXACT_D4'
 assert result['ordinary_final_graph_BFS_roots']==16389 and result['source_only_BFS_roots']==0
 result['total_suite_CPU_seconds']=cpu();result['CPU_budget_seconds']=120
 save('RESULT.json',result)
 terminal=dict(status=result['status'],all_processes_terminal=True,single_worker=True,CPU_seconds=cpu(),CPU_budget_seconds=120,wall_seconds=time.time()-WALL,
  steps=steps,source_raw_parses=1,candidate_parses=1,final_graph_BFS_roots=16389,final_old_labelled_roots=15552,final_new_labelled_roots=837,
  separate_source_BFS_roots=0,preliminary_newroot_BFS=0,root_prediction_mismatches=0,no_automatic_continuation=True,
  measurement_boundary='Recorded localpreparation, onecompile, oneauthorrawstream, onecandidate stream, fullN/projection binding, one complete finalallroot ordinaryBFS, aggregation; source text authoring/read-only metadata inspection not separately timed.')
 save('TERMINAL.json',terminal);save('HANDLE.json',dict(status='TERMINAL',running=False,all_processes_terminal=True))
 print(json.dumps(terminal,indent=2))
except Exception as e:
 save('TERMINAL.json',dict(status='FAIL_OR_BUDGET_UNKNOWN',phase=phase,error=str(e),CPU_seconds=cpu(),steps=steps,all_processes_terminal=True,no_automatic_continuation=True))
 raise
