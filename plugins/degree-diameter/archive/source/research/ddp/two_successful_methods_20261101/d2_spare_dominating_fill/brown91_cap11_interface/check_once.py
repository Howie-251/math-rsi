#!/usr/bin/env python3
"""One scalar type-count relaxation, using inherited finite profiles only."""
import json
from pathlib import Path
import resource
import subprocess
import time

root=Path(__file__).resolve().parent
start_cpu=time.process_time()
start_wall=time.monotonic()
options={}
profiles=json.loads((root/'pin_profiles/PROFILES.json').read_text())

def add(i,e,a,c,kind,profile=None):
    s=i+e+a
    if not 1<=s<=8 or (i and s>6):
        return
    c=min(c,91)
    # All helper sizes are at most8, proved independently in PROOF.md.
    if c+8*(11-s)<91:
        return
    key=(i,e,a)
    value={'I':i,'E':e,'A':a,'s':s,'closed_upper':c,
           'degree_H_upper':11-s,'geometry':kind}
    if profile is not None:
        value['profile_representative_pole']=profile['representative_pole']
        value['profile_representative_pins']=profile['representative_pins']
    if key not in options or options[key]['closed_upper']<c:
        options[key]=value

for p in profiles:
    add(p['I'],p['E'],p['A'],p['closed_coverage'],p['line_type'],p)
for s in range(3,9):
    for a in range(s+1):
        for i in range(s-a+1):
            e=s-a-i
            # First union the a absolute-point tangent lines; their pairwise
            # intersections are distinct external points (no three concurrent).
            tangent_bound=10*a-a*(a-1)//2+(s-a)*(11-(a+1)//2)
            add(i,e,a,min(9*s+3-a,tangent_bound),
                'noncollinear_optimistic_bound')
options=sorted(options.values(),key=lambda p:(p['s'],p['A'],p['I'],p['E']))
(root/'DP_OPTIONS.json').write_text(json.dumps(options,indent=2)+'\n')
(root/'DP_OPTIONS.txt').write_text(''.join(
    f"{p['I']} {p['E']} {p['A']} {p['s']} {p['closed_upper']}\n"
    for p in options))

child_before=resource.getrusage(resource.RUSAGE_CHILDREN)
compile_run=subprocess.run(['g++','-O2','-std=c++17',str(root/'check_dp.cpp'),
                            '-o',str(root/'check_dp')],capture_output=True,text=True)
assert compile_run.returncode==0,compile_run.stderr
compile_usage=resource.getrusage(resource.RUSAGE_CHILDREN)
run=subprocess.run([str(root/'check_dp'),str(root/'DP_OPTIONS.txt')],
                   capture_output=True,text=True,timeout=18)
assert run.returncode==0,run.stderr
end_usage=resource.getrusage(resource.RUSAGE_CHILDREN)
(root/'DP_RAW.txt').write_text(run.stdout)
lines=iter(run.stdout.splitlines())
cases=[]
for line in lines:
    _,a,score=line.split()
    a,score=int(a),int(score)
    ids=list(map(int,next(lines).split()))
    pattern=[dict(options[t]) for t in ids]
    assert len(pattern)==16
    assert sum(p['I'] for p in pattern)==36
    assert sum(p['E'] for p in pattern)==45
    assert sum(p['A'] for p in pattern)==a
    assert sum(p['A'] for p in pattern if p['s']<=5)>=20-a
    # Necessary row capacities under this pattern. Failure rejects this witness,
    # not every other type pattern. No helper edges are enumerated.
    row_pass=True
    for j,p in enumerate(pattern):
        best_neighbors=sorted((q['s'] for k,q in enumerate(pattern) if k!=j),
                              reverse=True)[:p['degree_H_upper']]
        p['best_row_capacity']=p['closed_upper']+sum(best_neighbors)
        row_pass &= p['best_row_capacity']>=91
    excess_demand=sum(max(0,91-p['closed_upper']-6*p['degree_H_upper'])
                      for p in pattern)
    excess_supply=sum(max(0,p['s']-6)*p['degree_H_upper'] for p in pattern)
    cases.append({'absolute_pin_load':a,'B':81+a,
                  'single_absolute_points':20-a,'double_absolute_points':a-10,
                  'max_scalar_capacity':score,'capacity_minus_1456':score-1456,
                  'witness_degree_upper_sum':sum(p['degree_H_upper'] for p in pattern),
                  'witness_individual_best_row_pass':row_pass,
                  'witness_excess_demand_at_base6':excess_demand,
                  'witness_excess_supply_at_base6':excess_supply,
                  'witness_excess_cut_pass':excess_demand<=excess_supply,
                  'pattern':pattern})

P=lambda h:90*h*h-2121*h+10201
assert P(17)==154
assert P(18)-P(17)==1029
assert 88*16*16-2020*16+10201==409
no_big_tangent=[0,21,39,55,69,81,89,95,99,102,101,91]
assert all(v<=6*s+53 for s,v in enumerate(no_big_tangent))
result={
    'status':'PASS_FINITE_TYPE_COUNT_RELAXATION',
    'scope':'16 helper slots; fixed I36/E45 old unique owners; A load15..20; single A owners in s<=5 groups; inherited exact collinear capacities and optimistic noncollinear capacities',
    'options':len(options),'cases':cases,
    'relaxation_limit':'Ignores actual simultaneous pin sets, old-vertex identity overlaps, helper graph realization, exact helper-old coverage and helper-helper D2. A scalar pass is not a graph.',
    'compile_CPU_seconds':(compile_usage.ru_utime+compile_usage.ru_stime
                           -child_before.ru_utime-child_before.ru_stime),
    'DP_process_CPU_seconds':(end_usage.ru_utime+end_usage.ru_stime
                              -compile_usage.ru_utime-compile_usage.ru_stime),
    'driver_CPU_seconds_through_analysis':time.process_time()-start_cpu,
    'wall_seconds_through_analysis':time.monotonic()-start_wall,
    'workers':1,'graph_generation':0,'BFS':0,'SAT':0,'MIP':0,'Lean':0,
    'helper_graphs_enumerated':0,'new_primary_search':0}
(root/'INTEGER_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='cases'},indent=2))
print(json.dumps([{k:v for k,v in p.items() if k!='pattern'} for p in cases],indent=2))
