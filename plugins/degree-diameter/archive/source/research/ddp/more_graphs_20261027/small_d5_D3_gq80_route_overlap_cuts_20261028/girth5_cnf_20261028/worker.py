"""Single direct-CNF test of the GQ80 girth>=5 matching subfamily."""
import itertools
import json
import os
from pathlib import Path
import resource
import subprocess
import time
from datetime import datetime,timezone

cpu0,wall0=time.process_time(),time.perf_counter()
resource.setrlimit(resource.RLIMIT_CPU,(35,35))
HERE=Path(__file__).resolve().parent
DDP=HERE.parents[2]
ROOT=DDP.parents[1]
OLD=DDP/'breadth_20261027_wave11/gq80_paired_matchings'
CADICAL=ROOT/'.tools/lean-4.24.0-linux/bin/cadical'


def save(name,value):
    (HERE/name).write_text(json.dumps(value,indent=2)+'\n')


model=json.loads((OLD/'model.json').read_text())
geometry=json.loads((OLD/'geometry.json').read_text())
lines=[set(row) for row in geometry['lines']]
incident=[set(row) for row in geometry['point_incident_lines']]
closed=[
    [{p}|set().union(*(lines[l] for l in incident[p])) for p in range(40)],
    [{l}|set().union(*(incident[p] for p in lines[l])) for l in range(40)],
]
variables=model['variables']
old_to_new={}
mapping=[]
for old_id,edge in enumerate(variables):
    side=0 if edge['side']=='point' else 1
    if edge['v'] not in closed[side][edge['u']]:
        new_id=len(mapping)+1
        old_to_new[old_id]=new_id
        mapping.append(dict(original_variable_id=old_id,DIMACS_variable=new_id,**edge))
eid={(0 if row['side']=='point' else 1,row['u'],row['v']):i for i,row in enumerate(variables)}


def old_eid(side,u,v):
    return eid[side,min(u,v),max(u,v)]


degree_rows=[[old_to_new[i] for i in row['vars'] if i in old_to_new]
             for row in model['degree_equations']]
cover_rows=[[old_to_new[i] for i in row['vars'] if i in old_to_new]
            for row in model['far_pair_covers']]
own_sizes=[sum(i in old_to_new for i in row['own_vars']) for row in model['far_pair_covers']]
relay_sizes=[sum(i in old_to_new for i in row['relay_vars']) for row in model['far_pair_covers']]
rectangles=[]
for l,m in itertools.combinations(range(40),2):
    q_old=old_eid(1,l,m)
    if q_old not in old_to_new:
        continue
    row_rect=[]
    for p in sorted(lines[l]):
        for q in sorted(lines[m]):
            p_old=old_eid(0,p,q)
            if p_old in old_to_new:
                pair=(old_to_new[p_old],old_to_new[q_old])
                rectangles.append(pair)
                row_rect.append(pair)
    assert len(row_rect)==12
actual=dict(variables=len(mapping),point_variables=sum(row['side']=='point' for row in mapping),
            line_variables=sum(row['side']=='line' for row in mapping),degree_rows=len(degree_rows),
            degree_choice_sizes=sorted(set(map(len,degree_rows))),cover_rows=len(cover_rows),
            cover_literal_sizes=sorted(set(map(len,cover_rows))),own_literal_sizes=sorted(set(own_sizes)),
            relay_literal_sizes=sorted(set(relay_sizes)),mixed_rectangle_rows=len(rectangles),
            unique_mixed_rectangle_rows=len(set(rectangles)))
expected=(actual['variables']==1080 and actual['point_variables']==540 and actual['line_variables']==540
          and len(degree_rows)==80 and set(map(len,degree_rows))=={27}
          and len(cover_rows)==1080 and set(map(len,cover_rows))=={29}
          and set(own_sizes)=={17} and set(relay_sizes)=={12}
          and len(rectangles)==len(set(rectangles))==6480)
save('ACTUAL_COUNTS.json',actual|{'expected_counts_match':expected,'solver_calls':0})
if not expected:
    out={'status':'MODEL_COUNT_MISMATCH_NO_SOLVER_CALL','actual_counts':actual,
         'solver_calls':0,'candidate_graphs':0,'graph_BFS_calls':0}
    for name in ('RESULT.json','terminal.json','RUN_HANDLE.json'):
        save(name,out)
    print(json.dumps(out,indent=2),flush=True)
    raise SystemExit(0)
save('VARIABLE_MAP.json',{'original_model':str(OLD/'model.json'),
     'old_to_DIMACS':{str(k):v for k,v in old_to_new.items()},
     'DIMACS_to_old':[row['original_variable_id'] for row in mapping],
     'variables':mapping,'excluded_collinear_old_variable_ids':[i for i in range(1560) if i not in old_to_new]})
save('RECTANGLE_CLAUSES.json',{'clauses':[[-p,-q] for p,q in rectangles],
                             'count':6480,'semantics':'Forbid simultaneously selecting the two internal edges of a mixed4cycle.'})
cnf=HERE/'model.cnf'
clause_count=0
with cnf.open('w') as f:
    f.write('c GQ80 girth>=5 matching subfamily; explicit original-variable map saved.\n')
    f.write('p cnf 1080 35720\n')
    for vs in degree_rows:
        f.write(' '.join(map(str,vs))+' 0\n');clause_count+=1
        for a,b in itertools.combinations(vs,2):
            f.write(f'-{a} -{b} 0\n');clause_count+=1
    for vs in cover_rows:
        f.write(' '.join(map(str,vs))+' 0\n');clause_count+=1
    for a,b in rectangles:
        f.write(f'-{a} -{b} 0\n');clause_count+=1
assert clause_count==35720
prep_cpu,prep_wall=time.process_time()-cpu0,time.perf_counter()-wall0
save('MODEL_STATS.json',actual|dict(clauses=35720,degree_ALO=80,degree_pairwise_AMO=28080,
     original_far_cover_filtered=1080,mixed_rectangles=6480,original_inputs_modified=False,
     geometry_reconstruction=False,preparation_CPU_seconds=prep_cpu,
     preparation_wall_seconds=prep_wall,stdlib_only=True,solver_calls=0,
     fixed_edges=[],symmetry_conditions=[],graph_BFS_calls=0))
child_hard=max(1,int(35-prep_cpu))


def child_limits():
    resource.setrlimit(resource.RLIMIT_CPU,(child_hard,child_hard))


before=resource.getrusage(resource.RUSAGE_CHILDREN)
solver_wall0=time.perf_counter()
with (HERE/'cadical.log').open('w') as log:
    process=subprocess.Popen([str(CADICAL),'-t','30',str(cnf)],stdout=log,stderr=subprocess.STDOUT,
                             preexec_fn=child_limits)
    save('RUN_HANDLE.json',dict(status='RUNNING_SINGLE_GIRTH5_CADICAL',worker_pid=os.getpid(),
         solver_pid=process.pid,started_at_utc=datetime.now(timezone.utc).isoformat(),
         command=[str(CADICAL),'-t','30',str(cnf)],solver_calls_started=1,
         configured_solver_wall_seconds=30,worker_CPU_hard_seconds=35,
         inherited_child_CPU_hard_seconds=child_hard,configured_parent_wall_seconds=45,
         preparation_CPU_seconds=prep_cpu,preparation_wall_seconds=prep_wall))
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
         candidate_graphs=0,graph_BFS_calls=0,actual_D=None,ordinary_bad_unordered_pairs=None,
         UNSAT_proof_requested=False,UNSAT_proof_checked=False,
         scope='Only the fixed girth>=5 paired-matching subfamily; not all GQ80 or all(5,3)graphs.')
if rc==10:
    assert 's SATISFIABLE' in text
    bits={}
    for line in text.splitlines():
        if line.startswith('v '):
            for value in map(int,line.split()[1:]):
                if value:
                    assert 1<=abs(value)<=1080
                    assert abs(value) not in bits or bits[abs(value)]==(value>0)
                    bits[abs(value)]=value>0
    assert len(bits)==1080
    checked=0
    for line in cnf.read_text().splitlines():
        if not line or line[0] in 'cp':
            continue
        vs=list(map(int,line.split()));assert vs[-1]==0
        assert any(bits[abs(v)]==(v>0) for v in vs[:-1]);checked+=1
    assert checked==35720
    chosen={row['original_variable_id'] for row in mapping if bits[row['DIMACS_variable']]}
    assert len(chosen)==40
    assert all(sum(i in chosen for i in row['vars'])==1 for row in model['degree_equations'])
    assert all(any(i in chosen for i in row['vars']) for row in model['far_pair_covers'])
    assert all((old_to_new[i] in bits and bits[old_to_new[i]]) for i in chosen)
    assert all(not(bits[p] and bits[q]) for p,q in rectangles)
    cuts=json.loads((HERE.parent/'overlap_cuts.json').read_text())['cuts']
    assert all(sum(i in chosen for i in row['positive_variable_ids'])>=6*(row['selected_variable_id'] in chosen) for row in cuts)
    matchings=[[],[]]
    for i in sorted(chosen):
        edge=variables[i];side=0 if edge['side']=='point' else 1
        assert edge['v'] not in closed[side][edge['u']]
        matchings[side].append([edge['u'],edge['v']])
    source=(OLD/'incidence.edges').read_text().splitlines()
    assert source[0].split()==['80','160']
    edges=[tuple(map(int,row.split())) for row in source[1:] if row.strip()]
    for side in (0,1):
        assert len(matchings[side])==20
        assert sorted(v for pair in matchings[side] for v in pair)==list(range(40))
        edges.extend((u+40*side,v+40*side) for u,v in matchings[side])
    edges=sorted(tuple(sorted(e)) for e in edges)
    assert len(edges)==len(set(edges))==200
    adjacency=[set() for _ in range(80)]
    for u,v in edges:
        assert u!=v;adjacency[u].add(v);adjacency[v].add(u)
    assert all(len(n)==5 for n in adjacency)
    assert all(not(adjacency[u]&adjacency[v]) for u,v in edges)
    assert all(len(adjacency[u]&adjacency[v])<=1 for u,v in itertools.combinations(range(80),2))
    assert all(len({u}|adjacency[u]|set().union(*(adjacency[v] for v in adjacency[u])))==26 for u in range(80))
    (HERE/'candidate.edges').write_text('80 200\n'+''.join(f'{u} {v}\n' for u,v in edges))
    save('candidate.matchings.json',dict(point_matching=matchings[0],line_matching=matchings[1],
         selected_original_variable_ids=sorted(chosen),selected_DIMACS_variables=sorted(v for v,b in bits.items() if b),
         n=80,m=200,degree=5,all_35720_clauses_pass=True,
         original_80_degrees_and1080_cover_rows_pass=True,all_3120_derived_integer_cuts_pass=True,
         local_triangle_and4cycle_absent=True,all_80_closed_B2_sizes=26,
         graph_BFS_calls=0,pending='Parent independent all80-root D3 check.'))
    out.update(status='SAT_GIRTH5_EXACT_MODEL_AWAITS_ROOT_BFS',incumbent_exported=True,
               candidate_graphs=1,checked_CNF_clauses=35720,
               prediction_status='CANDIDATE_AWAITS_ROOT_VERIFICATION')
elif rc==20:
    assert 's UNSATISFIABLE' in text
    out.update(status='RAW_UNSAT_GIRTH5_SUBFAMILY_NO_PROOF',incumbent_exported=False,
               prediction_status='RAW_SUBFAMILY_UNSAT_UNCERTIFIED')
else:
    out.update(status='UNKNOWN_GIRTH5_SINGLE_CADICAL_WINDOW_CLOSED',incumbent_exported=False,
               prediction_status='UNKNOWN_NOT_REFUTED')
out.update(worker_self_CPU_seconds=time.process_time()-cpu0,
           aggregate_worker_children_CPU_seconds=time.process_time()-cpu0+child_cpu,
           worker_wall_seconds=time.perf_counter()-wall0)
for name in ('RESULT.json','terminal.json','RUN_HANDLE.json'):
    save(name,out)
print(json.dumps(out,indent=2),flush=True)
