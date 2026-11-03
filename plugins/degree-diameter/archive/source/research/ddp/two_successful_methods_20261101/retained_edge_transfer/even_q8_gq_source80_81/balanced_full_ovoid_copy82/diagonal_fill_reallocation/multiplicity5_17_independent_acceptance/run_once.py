import time
START=time.process_time();WALL=time.time()
import json,math,resource,subprocess
from pathlib import Path
D=Path(__file__).resolve().parent;BASE=D.parent;BUDGET=60
INIT=resource.getrusage(resource.RUSAGE_CHILDREN)
def cpu():
 r=resource.getrusage(resource.RUSAGE_CHILDREN)
 return time.process_time()-START+r.ru_utime+r.ru_stime-INIT.ru_utime-INIT.ru_stime
cases=[(86,BASE/'multiplicity5_degree86','graph_d86_D3_n363420.edges'),(98,BASE/'multiplicity17_degree98','graph_d98_D3_n414132.edges')]
steps=[];phase='prepare_unique_suite'
try:
 for cap,p,name in cases:
  assert (p/name).is_file()
  (p/'independent_acceptance').mkdir(exist_ok=True)
 commands=[('compile',['g++','-O2','-std=c++17','verify.cpp','-o','verify']),
  ('validate',['./verify',str(BASE/'graph_d82_D3_n346516.edges'),str(cases[0][1]/cases[0][2]),str(cases[0][1]/'independent_acceptance'),str(cases[1][1]/cases[1][2]),str(cases[1][1]/'independent_acceptance')])]
 for phase,cmd in commands:
  remaining=max(1,math.floor(BUDGET-cpu()-1))
  if phase=='validate':cmd.append(str(remaining-1))
  def limit():resource.setrlimit(resource.RLIMIT_CPU,(remaining,remaining+1))
  before=cpu()
  with (D/(phase+'.stdout')).open('w') as out,(D/(phase+'.stderr')).open('w') as err:
   p=subprocess.Popen(cmd,cwd=D,stdout=out,stderr=err,preexec_fn=limit)
   (D/'HANDLE.json').write_text(json.dumps(dict(pid=p.pid,phase=phase,CPU_budget_seconds=60,single_worker=True),indent=2)+'\n')
   rc=p.wait()
  steps.append(dict(phase=phase,exit_code=rc,CPU_seconds_including_driver=cpu()-before))
  assert rc==0,(phase,rc)
  assert cpu()<BUDGET
 summary=json.loads((D/'VALIDATOR_SUMMARY.json').read_text());assert summary['parent_parse_count']==1
 total=cpu();case_statuses={}
 for cap,p,name in cases:
  result=json.loads((p/'independent_acceptance/RESULT.json').read_text())
  assert result['status'] in ['PASS','PASS_WITH_HIST_PREDICTION_MISMATCH'] and result['actual_lastblock_new_BFS_roots']==68
  case_statuses[str(cap)]=result['status']
  terminal=dict(status=result['status'],all_children_terminal=True,single_worker=True,
   case_validator_CPU_seconds=result['case_validator_CPU_seconds'],shared_parent_parse_CPU_seconds=summary['shared_parent_parse_CPU_seconds'],
   joint_two_target_total_CPU_seconds=total,joint_CPU_budget_seconds=60,case_candidate_parses=1,
   source_G1_parsed_once_for_both=True,actual_case_BFS_roots=68,old_BFS_roots=0,
   common_TERMINAL='../../multiplicity5_17_independent_acceptance/TERMINAL.json',no_automatic_continuation=True)
  (p/'independent_acceptance/TERMINAL.json').write_text(json.dumps(terminal,indent=2)+'\n')
 suite_status='PASS_BOTH_INDEPENDENT_G1_TARGETS' if all(s=='PASS' for s in case_statuses.values()) else 'MATH_PASS_WITH_REPORTED_HIST_PREDICTION_MISMATCH'
 summary['case_statuses']=case_statuses;summary['status']=suite_status
 terminal=dict(status=suite_status,total_CPU_seconds=cpu(),wall_seconds=time.time()-WALL,
  CPU_budget_seconds=60,single_worker=True,steps=steps,parent_parse_count=1,candidate_parses=2,
  actual_new_BFS_roots=136,old_BFS_roots=0,all_children_terminal=True,no_automatic_continuation=True,
  measurement_boundary='One compile, one literal G1 read reused in memory, two candidate streams, every newrole complete N binding, onlylastblock68roots each, aggregation; authoring excluded.')
 (D/'RESULT.json').write_text(json.dumps(summary,indent=2)+'\n')
 (D/'TERMINAL.json').write_text(json.dumps(terminal,indent=2)+'\n')
 (D/'HANDLE.json').write_text(json.dumps(dict(status='TERMINAL',all_children_terminal=True),indent=2)+'\n')
 print(json.dumps(terminal,indent=2))
except Exception as e:
 fail=dict(status='FAILED_OR_UNKNOWN_NO_CONTINUATION',phase=phase,error=str(e),steps=steps,total_CPU_seconds=cpu(),all_children_terminal=True)
 (D/'TERMINAL.json').write_text(json.dumps(fail,indent=2)+'\n')
 raise
