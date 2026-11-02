from pathlib import Path
import json,time,subprocess,resource
B=Path(__file__).resolve().parent;A=B.parent;R=B.parents[6];t0=time.process_time()
def load(p):return json.loads(p.read_text())
def save(n,o):(B/n).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
assert not (B/'RESULT.json').exists();source=A/'orbit0';model=load(source/'MODEL.json');lines=(source/'MODEL.cnf').read_text().splitlines();nvars=int(lines[0].split()[2]);clauses=[list(map(int,l.split()[:-1])) for l in lines[1:]];assert len(clauses)==model['clauses'];prefix=clauses[:-6916];blocks=[clauses[-6916+i*364:-6916+(i+1)*364] if i<18 else clauses[-364:] for i in range(19)];assert all(len(z)==364 for z in blocks)
solver=R/'.tools/lean-4.24.0-linux/bin/cadical';assert solver.exists();cases=[];cpus=[]
def solve(helpers):
 ordinal=len(cases);cnf=B/f'subset{ordinal}.cnf';cls=prefix+[c for h in helpers for c in blocks[h]]
 with cnf.open('w') as out:
  out.write(f'p cnf {nvars} {len(cls)}\n')
  for c in cls:out.write(' '.join(map(str,c))+' 0\n')
 before=resource.getrusage(resource.RUSAGE_CHILDREN)
 def limit():resource.setrlimit(resource.RLIMIT_CPU,(3,3))
 with (B/f'subset{ordinal}.log').open('w') as out:
  p=subprocess.Popen([str(solver),'-t','2',str(cnf)],stdout=out,stderr=subprocess.STDOUT,preexec_fn=limit);save('LIVE_HANDLE.json',{'pid':p.pid,'helpers':helpers,'terminal':False})
  killed=False
  try:rc=p.wait(timeout=6)
  except subprocess.TimeoutExpired:p.kill();rc=p.wait();killed=True
 after=resource.getrusage(resource.RUSAGE_CHILDREN);cpu=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime;cpus.append(cpu);text=(B/f'subset{ordinal}.log').read_text();status='SAT' if rc==10 and 's SATISFIABLE' in text else 'RAW_UNSAT' if rc==20 and 's UNSATISFIABLE' in text else 'UNKNOWN';r={'case':ordinal,'helpers':helpers,'status':status,'returncode':rc,'CPU':cpu,'killed':killed}
 if status=='SAT':
  vals=[int(z) for line in text.splitlines() if line.startswith('v ') for z in line[2:].split() if int(z)];pos={z for z in vals if z>0};assert all(any((l in pos if l>0 else -l not in pos) for l in c) for c in cls)
  owners=[]
  for pi in range(28):
   js=[j for j in range(19) if pi*19+j+1 in pos];assert len(js)==1;owners.append(js[0])
  assert [owners.count(j) for j in range(19)]==model['spokes'];save(f'subset{ordinal}_SAT_ASSIGNMENT.json',{'helpers_covered':helpers,'portowners':owners,'ports':model['ports'],'all_submodel_clauses_checked':True,'full383_status':'NOT_CLAIMED'})
 cases.append(r);print(json.dumps(r),flush=True);return r
current=list(range(19));reason=None;split=None
while len(current)>1 and len(cases)<=8:
 cut=len(current)//2;left,right=current[:cut],current[cut:];a=solve(left)
 if a['status']=='UNKNOWN':reason='UNKNOWN_SUBMODEL_STOP';break
 if a['status']=='RAW_UNSAT':current=left;continue
 b=solve(right)
 if b['status']=='UNKNOWN':reason='UNKNOWN_SUBMODEL_STOP';break
 if b['status']=='RAW_UNSAT':current=right;continue
 reason='TWO_SAT_SIDES_SHARED_ASSIGNMENT_INCOMPATIBLE_BY_PARENT_RAW_UNSAT';split=[left,right];break
if len(current)==1:reason='SINGLE_HELPER_COVERAGE_RAW_UNSAT'
if reason is None:reason='CALL_BUDGET_STOP'
prior=load(A/'remaining_orbit5/RESULT.json')['case_CPU'];parentcpu=time.process_time()-t0;r={'status':reason,'orbit':0,'original_pattern':model['pattern'],'remaining_raw_UNSAT_helper_set':current,'incompatible_split':split,'cases':cases,'new_solver_calls':len(cases),'solver_CPU':sum(cpus),'parent_CPU':parentcpu,'prior_CPU':prior,'read_prepare_CPU_charge':.35,'case_CPU':prior+.35+parentcpu+sum(cpus),'casecap':40,'proof_checked':False,'source_BFS_oldball_newtarget_Lean_ARIS':0,'new_accepted_graph_parameter_Lean':[0,0,0],'terminal':True,'scope':'onlyorbit0CNFhelpercoverageconstraintlocalization;rawUNSATnotformal/generalNo','next':'useidentifiedlocalorjointobstacletochangehelperconnectionrules;noresumingoldsolverwindows'};assert r['case_CPU']<40;save('RESULT.json',r);save('TERMINAL.json',{'terminal':True,'result':'RESULT.json'});save('LIVE_HANDLE.json',{'terminal':True,'pid':None});print(json.dumps(r,ensure_ascii=False),flush=True)
