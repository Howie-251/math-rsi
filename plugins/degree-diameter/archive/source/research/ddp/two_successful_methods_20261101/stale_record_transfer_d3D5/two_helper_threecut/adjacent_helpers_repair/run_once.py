#!/usr/bin/env python3
import json,os,resource,subprocess
from pathlib import Path
P=Path(__file__).resolve().parent;R=P.parents[5]
prior=json.loads((P.parent/'RESULT.json').read_text())['CPU_seconds_measured_runner_and_children']
S=R/'research/ddp/more_graphs_20261027/cubic_D6_twofold70/source70.edges';attempts=[]
def run(cmd,name,limit):
 with (P/(name+'.log')).open('w') as f:
  def caps():resource.setrlimit(resource.RLIMIT_CPU,(limit,limit+1))
  proc=subprocess.Popen(cmd,stdout=f,stderr=subprocess.STDOUT,preexec_fn=caps)
  pid,st,u=os.wait4(proc.pid,0);proc.returncode=os.waitstatus_to_exitcode(st)
 attempts.append(dict(name=name,pid=pid,exit_code=proc.returncode,CPU_seconds=u.ru_utime+u.ru_stime));return proc.returncode
assert run(['g++','-O3','-std=c++17',str(P/'gate.cpp'),'-o',str(P/'gate')],'compile',5)==0
u=resource.getrusage(resource.RUSAGE_SELF);remaining=20-prior-sum(x['CPU_seconds'] for x in attempts)-u.ru_utime-u.ru_stime-1.0
limit=min(15.5,remaining);assert limit>0
assert run([str(P/'gate'),str(S),str(P),str(limit)],'gate',int(limit)+1)==0
j=json.loads((P/'gate.log').read_text());u=resource.getrusage(resource.RUSAGE_SELF);cost=sum(x['CPU_seconds'] for x in attempts)+u.ru_utime+u.ru_stime
j.update(date='2026-11-01',source=str(S.relative_to(R)),source_legality='inherited; no validation/D5 BFS or R4 recomputation',rule='three matching cuts; choose nondouble old-old endpoint repair; split remaining4 pins2+2 between adjacent helpers',partition_symmetry='minimum remaining endpoint assigned helper70; three partitions per valid repair',inherited_case_CPU_seconds=prior,new_batch_measured_CPU_seconds=cost,cumulative_case_measured_CPU_seconds=prior+cost,cumulative_CPU_budget=20,preparation_note='one CPU second reserved for preceding brief code/PRED preparation and final receipts; these operations not individually metered',attempts=attempts,new_graphs=int(j['hit']),new_Lean_instances=0)
(P/'RESULT.json').write_text(json.dumps(j,indent=2)+'\n');(P/'TERMINAL.json').write_text(json.dumps(dict(date=j['date'],status=j['status'],active_processes=0,complete_fixed_rule=j['complete'],cumulative_case_measured_CPU_seconds=prior+cost,cumulative_CPU_budget=20,new_graphs=int(j['hit']),attempts=attempts),indent=2)+'\n');print(json.dumps(j,indent=2))
