#!/usr/bin/env python3
import json
from pathlib import Path
import resource
import subprocess
import time
root=Path(__file__).resolve().parent
start=time.process_time()
u0=resource.getrusage(resource.RUSAGE_CHILDREN)
c=subprocess.run(['g++','-O2','-std=c++17',str(root/'check_dp.cpp'),'-o',str(root/'check_dp')],capture_output=True,text=True)
assert c.returncode==0,c.stderr
u1=resource.getrusage(resource.RUSAGE_CHILDREN)
r=subprocess.run([str(root/'check_dp'),str(root/'DP_OPTIONS.txt'),'excess'],capture_output=True,text=True,timeout=15)
assert r.returncode==0,r.stderr
u2=resource.getrusage(resource.RUSAGE_CHILDREN)
options=json.loads((root/'DP_OPTIONS.json').read_text())
lines=iter(r.stdout.splitlines())
cases=[]
for line in lines:
    _,a,score=line.split()
    a,score=int(a),int(score)
    pattern=[dict(options[t]) for t in map(int,next(lines).split())]
    assert len(pattern)==16
    assert sum(p['I'] for p in pattern)==36
    assert sum(p['E'] for p in pattern)==45
    assert sum(p['A'] for p in pattern)==a
    demand=sum(max(0,91-p['closed_upper']-6*p['degree_H_upper']) for p in pattern)
    supply=sum(max(0,p['s']-6)*p['degree_H_upper'] for p in pattern)
    assert supply-demand==score
    cases.append({'B':81+a,'absolute_pin_load':a,
                  'max_excess_supply_minus_demand':score,
                  'witness_excess_supply':supply,'witness_excess_demand':demand,
                  'all_profiles_excluded_by_cut':score<0,'pattern':pattern})
result={'status':'PASS_BOUNDED_COHORT_CUT_OPTIMIZATION',
        'cases':cases,'recurrence_source':'check_dp.cpp excess objective',
        'options_source':'DP_OPTIONS.json:87 complete geometric-type upper options',
        'compile_CPU_seconds':u1.ru_utime+u1.ru_stime-u0.ru_utime-u0.ru_stime,
        'DP_process_CPU_seconds':u2.ru_utime+u2.ru_stime-u1.ru_utime-u1.ru_stime,
        'driver_CPU_seconds_through_analysis':time.process_time()-start,
        'workers':1,'graph_generation':0,'helper_graphs_enumerated':0,
        'BFS':0,'SAT':0,'MIP':0,'Lean':0,'new_primary_search':0}
(root/'COHORT_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='cases'},indent=2))
print(json.dumps([{k:v for k,v in p.items() if k!='pattern'} for p in cases],indent=2))
