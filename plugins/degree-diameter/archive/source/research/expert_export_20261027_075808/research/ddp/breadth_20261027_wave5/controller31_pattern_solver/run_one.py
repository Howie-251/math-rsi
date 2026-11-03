from pathlib import Path
import sys,json,time,subprocess,resource
from core import read_graph,make_problem,production
P=Path(__file__).resolve().parent;started=time.process_time()
budgetfile=P/'batch.json';batch=json.loads(budgetfile.read_text()) if budgetfile.exists() else dict(max_inputs=8,max_total_CPU_seconds=60,items=[],CPU_seconds=0.0)
if len(batch['items'])>=8 or batch['CPU_seconds']>=52:raise SystemExit('Fixed batch limit reached; no further input accepted.')
if any(x.get('status')=='HIT837' for x in batch['items']):raise SystemExit('A hit already ended this batch.')
source=Path(sys.argv[1]).resolve();idx=len(batch['items']);out=P/f'item_{idx:02d}';out.mkdir()
n,edges=read_graph(source);problem,pre=make_problem(n,edges);(out/'precheck.json').write_text(json.dumps(pre,indent=2)+'\n');(out/'ports.json').write_text(json.dumps(problem['graph'],separators=(',',':'))+'\n')
record=dict(index=idx,source=str(source),status=pre['status'],precheck=pre,solver_started=False)
childcpu=0.0
if pre['status']=='READY_FOR_PATTERN_MILP':
 (out/'problem.json').write_text(json.dumps(problem,separators=(',',':'))+'\n');r0=resource.getrusage(resource.RUSAGE_CHILDREN)
 with (out/'solver_stdout.txt').open('w') as stdout,(out/'solver_stderr.txt').open('w') as stderr:
  try:run=subprocess.run([sys.executable,str(P/'worker.py'),str(out)],stdout=stdout,stderr=stderr,timeout=9);code=run.returncode
  except subprocess.TimeoutExpired:code='WALL_LIMIT'
 r1=resource.getrusage(resource.RUSAGE_CHILDREN);childcpu=r1.ru_utime+r1.ru_stime-r0.ru_utime-r0.ru_stime
 f=out/'solver_result.json';result=json.loads(f.read_text()) if f.exists() else dict(status='UNKNOWN_PROCESS_LIMIT',incumbent=False)
 record.update(solver_started=True,solver_result=result,process_returncode=code,status='UNKNOWN' if not result.get('choice') else 'CHOICE_RETURNED')
 if result.get('choice'):
  check=production(problem,result['choice'],out);record.update(status='HIT837',production=check)
 elif result.get('status')==2:record['status']='FIXED_CONTROLLER_PATTERN_INFEASIBLE'
record['CPU_seconds']=time.process_time()-started+childcpu;record['child_CPU_seconds']=childcpu;batch['CPU_seconds']+=record['CPU_seconds'];batch['items'].append(record)
batch['status']='HIT837' if record['status']=='HIT837' else 'FIXED_BATCH_LIMIT_REACHED' if len(batch['items'])>=8 else 'WAITING_EXPLICIT_INPUT'
batch['solver_calls']=sum(x.get('solver_started',False) for x in batch['items']);batch['new_graphs']=sum(x.get('status')=='HIT837' for x in batch['items'])
(out/'terminal.json').write_text(json.dumps(record,indent=2)+'\n');budgetfile.write_text(json.dumps(batch,indent=2)+'\n');print(json.dumps(record,indent=2),flush=True)
