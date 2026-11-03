#!/usr/bin/env python3
import json,os,resource,subprocess,time
from pathlib import Path
P=Path(__file__).resolve().parent;R=P.parents[4]
S=R/'research/ddp/more_graphs_20261027/cubic_D6_twofold70/source70.edges'
children=[]
def run(cmd,name,cpu_limit):
 with (P/(name+'.log')).open('w') as log:
  def limits():resource.setrlimit(resource.RLIMIT_CPU,(cpu_limit,cpu_limit+1))
  proc=subprocess.Popen(cmd,stdout=log,stderr=subprocess.STDOUT,preexec_fn=limits)
  pid,status,usage=os.wait4(proc.pid,0);proc.returncode=os.waitstatus_to_exitcode(status)
 c=usage.ru_utime+usage.ru_stime
 children.append(dict(name=name,pid=pid,exit_code=proc.returncode,CPU_seconds=c));return proc.returncode
assert run(['g++','-O3','-std=c++17',str(P/'gate.cpp'),'-o',str(P/'gate')],'compile',5)==0
usage=resource.getrusage(resource.RUSAGE_SELF);available=20-sum(c['CPU_seconds'] for c in children)-usage.ru_utime-usage.ru_stime-1.0
run_limit=min(17.0,available)
assert run_limit>0
exit_code=run([str(P/'gate'),str(S),str(P),str(run_limit)],'gate',int(run_limit)+1)
assert exit_code==0
j=json.loads((P/'gate.log').read_text())
j.update(date='2026-11-01',source=str(S.relative_to(R)),source_acceptance='inherited published cubic70/D5; no source-validity or D5 BFS repeated',rule='delete3 vertex-disjoint old edges; add2 nonadjacent helpers; split6pins3+3',partition_symmetry='minimum endpoint assigned helper70; ten partitions per matching',new_graphs=int(j['hit']),new_Lean_instances=0,old_R4_union_is_diagnostic_not_necessary_filter=True,source_radius4_new_mechanism_only=True,attempts=children)
u=resource.getrusage(resource.RUSAGE_SELF);j['CPU_seconds_measured_runner_and_children']=sum(c['CPU_seconds'] for c in children)+u.ru_utime+u.ru_stime
j['CPU_seconds_budget']=20;j['preparation_note']='Earlier brief PRED/code preparation and read-only reports were not individually metered; one CPU second reserved from the numerical run budget for those operations and final receipts.'
(P/'RESULT.json').write_text(json.dumps(j,indent=2)+'\n')
(P/'TERMINAL.json').write_text(json.dumps(dict(date=j['date'],status=j['status'],active_processes=0,complete_fixed_rule=j['complete'],new_graphs=j['new_graphs'],CPU_seconds_measured=j['CPU_seconds_measured_runner_and_children'],CPU_seconds_budget=20,attempts=children),indent=2)+'\n')
print(json.dumps(j,indent=2))
