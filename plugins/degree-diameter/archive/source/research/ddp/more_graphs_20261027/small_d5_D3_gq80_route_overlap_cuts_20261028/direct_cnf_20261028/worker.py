"""One direct-CNF call; pure stdlib preparation and SAT-witness export."""
import itertools
import json
import os
from pathlib import Path
import resource
import subprocess
import time
from datetime import datetime, timezone

cpu0, wall0 = time.process_time(), time.perf_counter()
resource.setrlimit(resource.RLIMIT_CPU, (35, 35))
HERE = Path(__file__).resolve().parent
DDP = HERE.parents[2]
ROOT = DDP.parents[1]
OLD = DDP / 'breadth_20261027_wave11/gq80_paired_matchings'
CADICAL = ROOT / '.tools/lean-4.24.0-linux/bin/cadical'


def save(name, value):
    (HERE / name).write_text(json.dumps(value, indent=2) + '\n')


model = json.loads((OLD / 'model.json').read_text())
assert model['variable_count'] == len(model['variables']) == 1560
degree = model['degree_equations']
cover = model['far_pair_covers']
assert len(degree) == 80 and all(len(row['vars']) == 39 for row in degree)
assert len(cover) == 1080 and all(len(row['vars']) == 41 for row in cover)
assert model['preassigned_edges'] == model['symmetry_constraints'] == []
cnf = HERE / 'model.cnf'
count = 0
with cnf.open('w') as f:
    f.write('c Direct complete GQ80 paired-matchings model; old IDs plus one.\n')
    f.write('p cnf 1560 60440\n')
    for row in degree:
        vs = [v+1 for v in row['vars']]
        f.write(' '.join(map(str, vs)) + ' 0\n')
        count += 1
        for a, b in itertools.combinations(vs, 2):
            f.write(f'-{a} -{b} 0\n')
            count += 1
    for row in cover:
        f.write(' '.join(str(v+1) for v in row['vars']) + ' 0\n')
        count += 1
assert count == 60440
prep_cpu, prep_wall = time.process_time()-cpu0, time.perf_counter()-wall0
save('MODEL_STATS.json', dict(variables=1560, clauses=60440, degree_ALO=80,
     degree_pairwise_AMO=59280, original_far_cover=1080,
     derived_integer_cuts_encoded=0, derived_integer_cuts_checked_on_SAT=3120,
     clause_deduplication=False, variable_map='DIMACS ID = original edge variable ID + 1',
     input_model=str(OLD/'model.json'), input_incidence=str(OLD/'incidence.edges'),
     matrix_or_geometry_reconstruction=False, BLAS_or_numpy_imports=False,
     preparation_CPU_seconds=prep_cpu, preparation_wall_seconds=prep_wall,
     solver_calls=0, graph_BFS_calls=0, candidate_graphs=0))
child_hard = max(1, int(35-prep_cpu))


def child_limits():
    resource.setrlimit(resource.RLIMIT_CPU, (child_hard, child_hard))


before = resource.getrusage(resource.RUSAGE_CHILDREN)
solver_wall0 = time.perf_counter()
with (HERE/'cadical.log').open('w') as log:
    process = subprocess.Popen([str(CADICAL), '-t', '30', str(cnf)],
                               stdout=log, stderr=subprocess.STDOUT,
                               preexec_fn=child_limits)
    save('RUN_HANDLE.json', dict(status='RUNNING_SINGLE_CADICAL', worker_pid=os.getpid(),
         solver_pid=process.pid, started_at_utc=datetime.now(timezone.utc).isoformat(),
         command=[str(CADICAL), '-t', '30', str(cnf)], solver_calls_started=1,
         configured_solver_wall_seconds=30, worker_CPU_hard_seconds=35,
         inherited_child_CPU_hard_seconds=child_hard, parent_wall_seconds=45,
         preparation_CPU_seconds=prep_cpu, preparation_wall_seconds=prep_wall))
    rc = process.wait()
after = resource.getrusage(resource.RUSAGE_CHILDREN)
child_cpu = after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
solver_wall = time.perf_counter()-solver_wall0
log_text = (HERE/'cadical.log').read_text()
incumbent = False
out = dict(solver='CaDiCaL', solver_exit_code=rc, solver_calls=1,
           configured_solver_wall_seconds=30, worker_CPU_hard_seconds=35,
           inherited_child_CPU_hard_seconds=child_hard, configured_parent_wall_seconds=45,
           preparation_CPU_seconds=prep_cpu, preparation_wall_seconds=prep_wall,
           measured_solver_CPU_seconds=child_cpu, measured_solver_wall_seconds=solver_wall,
           graph_BFS_calls=0, candidate_graphs=0, actual_D=None,
           ordinary_bad_unordered_pairs=None, UNSAT_proof_requested=False,
           UNSAT_proof_checked=False)
if rc == 10:
    assert 's SATISFIABLE' in log_text
    bits = {}
    for line in log_text.splitlines():
        if line.startswith('v '):
            for token in line.split()[1:]:
                literal = int(token)
                if not literal:
                    continue
                assert 1 <= abs(literal) <= 1560
                value = literal > 0
                assert abs(literal) not in bits or bits[abs(literal)] == value
                bits[abs(literal)] = value
    assert len(bits) == 1560
    checked = 0
    for line in cnf.read_text().splitlines():
        if not line or line[0] in 'cp':
            continue
        literals = [int(x) for x in line.split()]
        assert literals[-1] == 0
        assert any(bits[abs(x)] == (x > 0) for x in literals[:-1])
        checked += 1
    assert checked == 60440
    chosen = {i for i in range(1560) if bits[i+1]}
    assert all(sum(i in chosen for i in row['vars']) == 1 for row in degree)
    assert all(any(i in chosen for i in row['vars']) for row in cover)
    cuts = json.loads((HERE.parent/'overlap_cuts.json').read_text())['cuts']
    assert len(cuts) == 3120
    cut_slacks = []
    for row in cuts:
        slack = sum(i in chosen for i in row['positive_variable_ids']) - 6*(row['selected_variable_id'] in chosen)
        assert slack >= 0
        cut_slacks.append(slack)
    assert len(chosen) == 40
    matchings = [[], []]
    for i in sorted(chosen):
        edge = model['variables'][i]
        matchings[0 if edge['side'] == 'point' else 1].append([edge['u'], edge['v']])
    source_rows = (OLD/'incidence.edges').read_text().splitlines()
    assert source_rows[0].split() == ['80', '160']
    edges = [tuple(map(int, row.split())) for row in source_rows[1:] if row.strip()]
    for side in (0, 1):
        assert len(matchings[side]) == 20
        assert sorted(v for edge in matchings[side] for v in edge) == list(range(40))
        edges.extend((u+40*side, v+40*side) for u,v in matchings[side])
    edges = sorted(tuple(sorted(edge)) for edge in edges)
    assert len(edges) == len(set(edges)) == 200
    degrees = [0]*80
    for u,v in edges:
        assert u != v
        degrees[u] += 1
        degrees[v] += 1
    assert set(degrees) == {5}
    (HERE/'candidate.edges').write_text('80 200\n'+''.join(f'{u} {v}\n' for u,v in edges))
    save('candidate.matchings.json', dict(point_matching=matchings[0], line_matching=matchings[1],
         selected_variable_ids=sorted(chosen), DIMACS_true_variables=sorted(i+1 for i in chosen),
         n=80,m=200,degree=5,all_60440_clauses_pass=True,
         all_80_original_degree_equations_pass=True, all_1080_original_cover_rows_pass=True,
         all_3120_derived_integer_cuts_pass=True, minimum_derived_cut_slack=min(cut_slacks),
         graph_BFS_calls=0,pending='Parent independent all-80-root BFS.'))
    incumbent = True
    out.update(status='SAT_VERIFIED_EXACT_MODEL_AWAITS_ROOT_BFS',candidate_graphs=1,
               checked_CNF_clauses=checked,checked_original_degree_rows=80,
               checked_original_cover_rows=1080,checked_derived_integer_cuts=3120,
               selected_matching_edges=40,prediction_status='CANDIDATE_AWAITS_ROOT_VERIFICATION')
elif rc == 20:
    assert 's UNSATISFIABLE' in log_text
    out.update(status='RAW_UNSAT_NO_PROOF_NOT_CERTIFIED',prediction_status='RAW_SOLVER_UNSAT_UNCERTIFIED')
else:
    out.update(status='UNKNOWN_SINGLE_CADICAL_WINDOW_CLOSED',prediction_status='UNKNOWN_NOT_REFUTED')
out.update(incumbent_exported=incumbent,worker_self_CPU_seconds=time.process_time()-cpu0,
           aggregate_worker_children_CPU_seconds=time.process_time()-cpu0+child_cpu,
           worker_wall_seconds=time.perf_counter()-wall0)
for name in ('RESULT.json','terminal.json','RUN_HANDLE.json'):
    save(name,out)
print(json.dumps(out,indent=2),flush=True)
