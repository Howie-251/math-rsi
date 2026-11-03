import csv
import json
import resource
import subprocess
import time
from pathlib import Path

D = Path(__file__).resolve().parent
start = time.process_time()
initial = resource.getrusage(resource.RUSAGE_CHILDREN)
wall = time.time()

def cpu():
    r = resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-start+r.ru_utime+r.ru_stime-initial.ru_utime-initial.ru_stime

P = json.loads((D.parents[1]/'ACTUAL_POINTS.json').read_text())['point_ids']
S = json.loads((D.parents[2]/'PARAMETERS.json').read_text())['spread_line_labels']
assert len(P) == 33 and len(S) == 50
C = [400*p+l for p in P for l in S]
assert len(set(C)) == 1650
lower = D.parents[1]/'multiplicity65_72_family/independent_acceptance/SOURCE_R2_ONLY_PREDICTIONS.csv'
with lower.open() as f:
    rows = list(csv.DictReader(f))
by_center = {int(row['center']): row for row in rows}
assert len(rows) == len(by_center) == 1650 and set(by_center) == set(C)
R, R3 = [], []
for h, c in enumerate(C):
    row = by_center[c]
    assert int(row['base']) == h
    r, r3, b2 = (int(row[k]) for k in ['source_R2', 'inherited_D3_source_R3', 'source_B2'])
    assert b2 == 65+r and r3 == 160050-b2
    R.append(r)
    R3.append(r3)
(D/'center_input.h').write_text(
    'constexpr int center_labels[1650]={'+','.join(map(str, C))+'};\n'
    'constexpr int inherited_R2[1650]={'+','.join(map(str, R))+'};\n'
    'constexpr int inherited_R3[1650]={'+','.join(map(str, R3))+'};\n')
inheritance = dict(status='PASS_CENTER_ID_BINDING_OF_PRIOR_ACCEPTED_PREDICTIONS',
                   file=str(lower), inherited_rows=1650, center_ID_set_exact=True,
                   base_index_and_center_recipe_exact=True, new_source_R2_enumerations=0,
                   new_source_R3_BFS=0, CPU_seconds=cpu())
(D/'INHERITED_PREDICTION_BINDING.json').write_text(json.dumps(inheritance, indent=2)+'\n')

phases = []
def call(args, name, limit):
    before = cpu()
    def cap():
        resource.setrlimit(resource.RLIMIT_CPU, (limit, limit+1))
    with (D/(name+'.stdout')).open('w') as out, (D/(name+'.stderr')).open('w') as err:
        p = subprocess.Popen(args, cwd=D, stdout=out, stderr=err, preexec_fn=cap)
        (D/'HANDLE.json').write_text(json.dumps(dict(pid=p.pid, phase=name,
             single_worker=True, CPU_budget_seconds=180, k_min=9, k_max=15), indent=2)+'\n')
        rc = p.wait()
    phases.append(dict(phase=name, returncode=rc, CPU_seconds_including_driver=cpu()-before))
    return rc

rc = call(['g++', '-std=c++17', '-O2', 'verify.cpp', '-o', 'verify'], 'compile', 15)
if rc == 0:
    remaining = 180-cpu()
    rc = call(['./verify', '../../../graph_d64_D3_n160050.edges', '../graphs',
               str(min(170, remaining-3))], 'validate', min(175, int(remaining-1)))

result = json.loads((D/'RESULT.json').read_text()) if (D/'RESULT.json').exists() else None
if rc == 0:
    assert result['source_literal_parses'] == 1
    assert result['source_R2_only_centers'] == result['source_R2_prediction_batches'] == 0
    assert result['inherited_source_R2_prediction_centers'] == 1650
    assert result['all_new_literal_N_bindings'] == 138600
    assert result['actual_new_literal_R3_BFS_roots'] == 24750
    assert result['BFS_graph_k'] == 15 and len(result['cases']) == 7
    lines = ['# Seven P33 endpoint graphs: fresh mathematical acceptance', '',
             'All seven complete literal files pass. Each endpoint has its own old-source-only-interior proof; only k15 has actual new-root BFS. Source R2 counts are inherited by exact centerID binding, with no new source-radius enumeration.', '',
             '|k|Degree|Order|Edges|Literal new-N bindings|Actual new-root BFS|',
             '|---:|---:|---:|---:|---:|---:|']
    for c in result['cases']:
        case = D/'cases'/c['case']
        (case/'SUMMARY.json').write_text(json.dumps(c, indent=2)+'\n')
        text = (f"# {c['case']}: independent acceptance PASS\n\n"
                f"k={c['k']}, n={c['n']}, m={c['m']}, degree cap={c['degree_cap']}. "
                f"Complete source5121600edge body retained exactly; every {c['new_vertices']} new vertex has its entire immutable source N64 bound. No new-new edges. "
                f"Actual new-root ordinary R3 BFS count={c['actual_new_literal_R3_BFS_roots']}; source R2/R3 enumerations=0. "
                "Predicted histograms use the prior accepted centerID-matched source data. "
                "Complete current-prefix/all-pairs proof and nonD2 follow from the independently bound old-only-interior construction; this does not infer a smaller graph's diameter from maximal BFS.\n\n"
                f"Proof-derived histogram distribution: {json.dumps(c['proof_derived_histogram_distribution'])}.\n\n"
                f"Actually measured BFS distribution: {json.dumps(c['actual_BFS_histogram_distribution'])}.\n")
        (case/'RESULT.md').write_text(text)
        (case/'PROOF.md').write_text(text+'\nSee ../../PROOF.md for the explicit genuine-Walk routes and collapse map. This endpoint has its own complete literal binding.\n')
        lines.append(f"|{c['k']}|{c['degree_cap']}|{c['n']}|{c['m']}|{c['new_vertices']}|{c['actual_new_literal_R3_BFS_roots']}|")
    (D/'RESULT.md').write_text('\n'.join(lines)+'\n')
    (D/'SUMMARY.json').write_text(json.dumps(result, indent=2)+'\n')

terminal = dict(status='PASS' if rc == 0 else 'PARTIAL_OR_FAILED', returncode=rc,
    total_CPU_seconds_including_preparation_compile_inherited_prediction_binding_seven_files_max_BFS_and_aggregation=cpu(),
    wall_seconds=time.time()-wall, CPU_budget_seconds=180, single_worker=True,
    k_min=9, k_max=15, all_children_terminal=True, phases=phases,
    inherited_prediction_binding=inheritance, result=result,
    measurement_boundary='One recipe/prediction-header preparation and compiler/validator/aggregation batch. One accepted-source parse, zero new sourceR2/R3 enumeration, seven complete file bindings, only maxk15 all24750newroot ordinary BFS. Interactive authoring and initial read-only inspection excluded.')
(D/'TERMINAL.json').write_text(json.dumps(terminal, indent=2)+'\n')
(D/'HANDLE.json').write_text(json.dumps(dict(status='TERMINAL', returncode=rc,
    single_worker=True, all_children_terminal=True, k_min=9, k_max=15), indent=2)+'\n')
print(json.dumps(terminal, indent=2))
raise SystemExit(rc)
