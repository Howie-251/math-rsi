"""Append verified local at-most-three counters; one bounded graph-model call."""
import itertools
import json
import os
from pathlib import Path
import resource
import subprocess
import time
from datetime import datetime,timezone
from counter_encoding import atmost_three
from counter_calibration import calibrate

cpu0,wall0=time.process_time(),time.perf_counter()
resource.setrlimit(resource.RLIMIT_CPU,(35,35))
HERE=Path(__file__).resolve().parent
GIRTH=HERE.parent/'girth5_cnf_20261028'
DDP=HERE.parents[2]
ROOT=DDP.parents[1]
OLD=DDP/'breadth_20261027_wave11/gq80_paired_matchings'
CADICAL=ROOT/'.tools/lean-4.24.0-linux/bin/cadical'


def save(name,value):
    (HERE/name).write_text(json.dumps(value,indent=2)+'\n')


try:
    calibration=calibrate()
except Exception as exc:
    out={'status':'COUNTER_CALIBRATION_FAILED_NO_SOLVER_CALL','error':f'{type(exc).__name__}: {exc}',
         'solver_calls':0,'candidate_graphs':0,'graph_BFS_calls':0}
    for name in ('COUNTER_CALIBRATION.json','RESULT.json','terminal.json','RUN_HANDLE.json'):
        save(name,out)
    print(json.dumps(out,indent=2),flush=True)
    raise SystemExit(0)
save('COUNTER_CALIBRATION.json',calibration)
base_map=json.loads((GIRTH/'VARIABLE_MAP.json').read_text())
mapping=base_map['variables']
assert len(mapping)==1080
assert [row['DIMACS_variable'] for row in mapping]==list(range(1,1081))
overlap=json.loads((HERE.parent/'overlap_cuts.json').read_text())['cuts']
closed={}
for row in overlap:
    key=(row['side'],row['root'])
    value=tuple(row['closed_root'])
    if key in closed:
        assert closed[key]==value
    else:
        closed[key]=value
assert len(closed)==80
base_clauses=[]
for line in (GIRTH/'model.cnf').read_text().splitlines():
    if not line or line[0] in 'cp':
        continue
    values=list(map(int,line.split()))
    assert values[-1]==0
    base_clauses.append(values[:-1])
assert len(base_clauses)==35720
counter_records=[]
next_aux=1081
next_clause=len(base_clauses)+1
for side in (0,1):
    name='point' if side==0 else 'line'
    for root in range(40):
        near=set(closed[side,root])-{root}
        selected=[edge for edge in mapping if edge['side']==name and edge['u'] in near and edge['v'] in near]
        inputs=[edge['DIMACS_variable'] for edge in selected]
        assert len(inputs)==len(set(inputs))==54
        clauses,meta=atmost_three(inputs,next_aux)
        assert meta['aux_count']==162 and meta['clause_count']==375
        counter_records.append(dict(side=side,root_local=root,root_global=root+40*side,
             near12_old_vertex_ids=sorted(near),input_DIMACS_edge_variables=inputs,
             input_original_edge_variable_ids=[edge['original_variable_id'] for edge in selected],
             **meta,first_CNF_clause1based=next_clause,
             last_CNF_clause1based=next_clause+len(clauses)-1,clauses=clauses))
        next_aux=meta['last_aux']+1
        next_clause+=len(clauses)
total_variables=next_aux-1
total_clauses=next_clause-1
assert len(counter_records)==80 and total_variables==14040 and total_clauses==65720
save('COUNTERS.json',{'inherited_edge_DIMACS_range':[1,1080],
     'new_auxiliary_DIMACS_range':[1081,14040],'counter_count':80,
     'auxiliary_count':12960,'counter_clause_count':30000,
     'inherited_map':str(GIRTH/'VARIABLE_MAP.json'),
     'records':[{k:v for k,v in record.items() if k!='clauses'} for record in counter_records]})
save('COUNTER_CLAUSES.json',{'count':30000,'records':[{'side':row['side'],'root_local':row['root_local'],
     'first_CNF_clause1based':row['first_CNF_clause1based'],
     'last_CNF_clause1based':row['last_CNF_clause1based'],'clauses':row['clauses']} for row in counter_records]})
cnf=HERE/'model.cnf'
with cnf.open('w') as f:
    f.write('c Existing girth5 CNF plus80 valid local route-budget at-most3 counters.\n')
    f.write(f'p cnf {total_variables} {total_clauses}\n')
    for clause in base_clauses:
        f.write(' '.join(map(str,clause))+' 0\n')
    for row in counter_records:
        for clause in row['clauses']:
            f.write(' '.join(map(str,clause))+' 0\n')
prep_cpu,prep_wall=time.process_time()-cpu0,time.perf_counter()-wall0
stats=dict(edge_variables=1080,auxiliary_variables=12960,total_variables=total_variables,
           inherited_clauses=35720,added_counter_clauses=30000,total_clauses=total_clauses,
           counters=80,inputs_per_counter=54,auxiliaries_per_counter=162,
           clauses_per_counter=375,counter_bound=3,first_auxiliary_ID=1081,last_auxiliary_ID=14040,
           inherited_girth_CNF=str(GIRTH/'model.cnf'),inherited_variable_map=str(GIRTH/'VARIABLE_MAP.json'),
           integer_graph_family='unchanged complete girth>=5 GQ80 paired-matching family',
           calibration_pass=True,preparation_CPU_seconds=prep_cpu,preparation_wall_seconds=prep_wall,
           stdlib_only=True,geometry_reconstruction=False,old_solver_repeated=False,
           fixed_edges=[],symmetry_conditions=[],solver_calls=0,graph_BFS_calls=0)
save('MODEL_STATS.json',stats)
print(json.dumps({'status':'COUNTER_CALIBRATION_PASS_MODEL_READY','variables':total_variables,
                  'clauses':total_clauses,'preparation_CPU_seconds':prep_cpu}),flush=True)
child_hard=max(1,int(35-prep_cpu))


def child_limits():
    resource.setrlimit(resource.RLIMIT_CPU,(child_hard,child_hard))


before=resource.getrusage(resource.RUSAGE_CHILDREN)
solver_wall0=time.perf_counter()
with (HERE/'cadical.log').open('w') as log:
    process=subprocess.Popen([str(CADICAL),'-t','30',str(cnf)],stdout=log,stderr=subprocess.STDOUT,
                             preexec_fn=child_limits)
    save('RUN_HANDLE.json',dict(status='RUNNING_SINGLE_GIRTH5_LOCAL_BUDGET_CADICAL',worker_pid=os.getpid(),
         solver_pid=process.pid,started_at_utc=datetime.now(timezone.utc).isoformat(),
         command=[str(CADICAL),'-t','30',str(cnf)],solver_calls_started=1,
         configured_solver_wall_seconds=30,configured_worker_CPU_hard_seconds=35,
         configured_child_CPU_hard_seconds=child_hard,configured_parent_wall_seconds=45,
         preparation_CPU_seconds=prep_cpu,calibration='COUNTER_CALIBRATION.json'))
    rc=process.wait()
after=resource.getrusage(resource.RUSAGE_CHILDREN)
child_cpu=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
solver_wall=time.perf_counter()-solver_wall0
text=(HERE/'cadical.log').read_text()
out=dict(solver='CaDiCaL',solver_exit_code=rc,solver_calls=1,
         configured_solver_wall_seconds=30,configured_worker_CPU_hard_seconds=35,
         configured_child_CPU_hard_seconds=child_hard,configured_parent_wall_seconds=45,
         preparation_CPU_seconds=prep_cpu,preparation_wall_seconds=prep_wall,
         measured_solver_CPU_seconds=child_cpu,measured_solver_wall_seconds=solver_wall,
         calibration_pass=True,candidate_graphs=0,graph_BFS_calls=0,actual_D=None,
         ordinary_bad_unordered_pairs=None,UNSAT_proof_requested=False,UNSAT_proof_checked=False,
         scope='Same complete girth>=5 GQ80 subfamily with valid local-budget consequences; not unrestricted GQ80.')
if rc==10:
    assert 's SATISFIABLE' in text
    bits={}
    for line in text.splitlines():
        if line.startswith('v '):
            for value in map(int,line.split()[1:]):
                if value:
                    assert 1<=abs(value)<=total_variables
                    assert abs(value) not in bits or bits[abs(value)]==(value>0)
                    bits[abs(value)]=value>0
    assert len(bits)==total_variables
    checked=0
    for line in cnf.read_text().splitlines():
        if not line or line[0] in 'cp':
            continue
        values=list(map(int,line.split()));assert values[-1]==0
        assert any(bits[abs(value)]==(value>0) for value in values[:-1]);checked+=1
    assert checked==65720
    chosen={edge['original_variable_id'] for edge in mapping if bits[edge['DIMACS_variable']]}
    assert len(chosen)==40
    model=json.loads((OLD/'model.json').read_text())
    assert all(sum(i in chosen for i in row['vars'])==1 for row in model['degree_equations'])
    assert all(any(i in chosen for i in row['vars']) for row in model['far_pair_covers'])
    assert all(sum(i in chosen for i in row['positive_variable_ids'])>=6*(row['selected_variable_id'] in chosen) for row in overlap)
    local_counts=[sum(bits[i] for i in row['input_DIMACS_edge_variables']) for row in counter_records]
    assert max(local_counts)<=3
    rectangles=json.loads((GIRTH/'RECTANGLE_CLAUSES.json').read_text())['clauses']
    assert all(any(bits[abs(v)]==(v>0) for v in clause) for clause in rectangles)
    matchings=[[],[]]
    for edge in mapping:
        if bits[edge['DIMACS_variable']]:
            matchings[0 if edge['side']=='point' else 1].append([edge['u'],edge['v']])
    source=(OLD/'incidence.edges').read_text().splitlines()
    assert source[0].split()==['80','160']
    edges=[tuple(map(int,row.split())) for row in source[1:] if row.strip()]
    for side in (0,1):
        assert len(matchings[side])==20
        assert sorted(v for row in matchings[side] for v in row)==list(range(40))
        edges.extend((u+40*side,v+40*side) for u,v in matchings[side])
    edges=sorted(tuple(sorted(edge)) for edge in edges)
    assert len(edges)==len(set(edges))==200
    adjacency=[set() for _ in range(80)]
    for u,v in edges:
        assert u!=v;adjacency[u].add(v);adjacency[v].add(u)
    assert all(len(n)==5 for n in adjacency)
    assert all(not(adjacency[u]&adjacency[v]) for u,v in edges)
    assert all(len(adjacency[u]&adjacency[v])<=1 for u,v in itertools.combinations(range(80),2))
    (HERE/'candidate.edges').write_text('80 200\n'+''.join(f'{u} {v}\n' for u,v in edges))
    save('candidate.matchings.json',dict(point_matching=matchings[0],line_matching=matchings[1],
         selected_original_edge_variable_ids=sorted(chosen),
         selected_edge_DIMACS_variables=[row['DIMACS_variable'] for row in mapping if bits[row['DIMACS_variable']]],
         auxiliary_variables_never_decoded_as_edges=True,n=80,m=200,degree=5,
         all_65720_CNF_clauses_pass=True,all_original_degrees_and_covers_pass=True,
         all_3120_overlap_cuts_pass=True,all_girth_constraints_pass=True,
         local_a_counts=local_counts,all_80_a_counts_atmost3=True,
         graph_BFS_calls=0,pending='Parent independent all80-source D3 and girth check.'))
    out.update(status='SAT_LOCAL_BUDGET_EXACT_GIRTH5_MODEL_AWAITS_ROOT_BFS',incumbent_exported=True,
               candidate_graphs=1,prediction_status='CANDIDATE_AWAITS_ROOT_VERIFICATION')
elif rc==20:
    assert 's UNSATISFIABLE' in text
    out.update(status='RAW_UNSAT_GIRTH5_LOCAL_BUDGET_NO_PROOF',incumbent_exported=False,
               prediction_status='RAW_GIRTH5_UNSAT_UNCERTIFIED')
else:
    out.update(status='UNKNOWN_GIRTH5_LOCAL_BUDGET_WINDOW_CLOSED',incumbent_exported=False,
               prediction_status='UNKNOWN_NOT_REFUTED')
out.update(worker_self_CPU_seconds=time.process_time()-cpu0,
           aggregate_worker_children_CPU_seconds=time.process_time()-cpu0+child_cpu,
           worker_wall_seconds=time.perf_counter()-wall0)
for name in ('RESULT.json','terminal.json','RUN_HANDLE.json'):
    save(name,out)
print(json.dumps(out,indent=2),flush=True)
