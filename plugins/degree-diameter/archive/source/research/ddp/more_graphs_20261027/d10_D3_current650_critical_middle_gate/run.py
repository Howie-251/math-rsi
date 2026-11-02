import json
from pathlib import Path
import resource
import subprocess
import time

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
started = time.process_time()
children_start = resource.getrusage(resource.RUSAGE_CHILDREN)
structure = json.loads((HERE / 'STRUCTURE_ROOT.json').read_text())
assert structure['status'] == 'STRUCTURE_VERIFIED' and structure['structure_confirmed']
assert len(structure['P_vertices']) == 130 and len(structure['F_vertices']) == 520
(HERE / 'P_LABELS.txt').write_text('\n'.join(map(str, structure['P_vertices'])) + '\n')
source = ROOT / structure['source_path']
compile_result = subprocess.run(['g++', '-O3', '-std=c++17', str(HERE / 'critical.cpp'), '-o', str(HERE / 'critical')], capture_output=True, text=True)
(HERE / 'compile.log').write_text(compile_result.stdout + compile_result.stderr)
assert compile_result.returncode == 0
compile_children = resource.getrusage(resource.RUSAGE_CHILDREN)
run = subprocess.run([str(HERE / 'critical'), str(source), str(HERE / 'P_LABELS.txt'), str(HERE)], capture_output=True, text=True)
(HERE / 'run.log').write_text(run.stdout + run.stderr)
ended = resource.getrusage(resource.RUSAGE_CHILDREN)
def childcpu(r):
    return r.ru_utime + r.ru_stime
receipt = {
    'native_exit_code': run.returncode,
    'compile_CPU_seconds': childcpu(compile_children) - childcpu(children_start),
    'native_process_CPU_seconds': childcpu(ended) - childcpu(compile_children),
    'driver_CPU_seconds': time.process_time() - started,
    'native_hard_CPU_seconds': 10,
    'root_structure_CPU_seconds_inherited_separately': structure['CPU_seconds'],
}
(HERE / 'RUN_RECEIPT.json').write_text(json.dumps(receipt, indent=2) + '\n')
if run.returncode != 0:
    (HERE / 'terminal.json').write_text(json.dumps({'status': 'UNKNOWN_OR_EXECUTION_ERROR', **receipt}, indent=2) + '\n')
    raise SystemExit(run.returncode)
native = json.loads((HERE / 'NATIVE_RESULT.json').read_text())
assert native['status'] == 'COMPLETE'
ff_forbidden = native['all_FF_have_matching9']
bound = max(structure['max_endpoint_R2_union_port_count'][t] for t in ['FP', 'PP'])
closed = ff_forbidden and 5 * bound < len(structure['P_vertices'])
result = {
    'status': 'FIXED_HUB_FAMILY_STRICTLY_EXCLUDED' if closed else 'NECESSARY_GATE_INCONCLUSIVE',
    'target_Delta': 10, 'target_D': 3, 'savedL': 650,
    'actual_graph_n': None, 'hypothetical_n': 651, 'actual_D': None,
    'ordinary_unordered_bad_pairs': None,
    'all_FF_cuts_forbidden': ff_forbidden,
    'remaining_cut_endpoint_R2_port_union_upper_bound': bound,
    'maximum_cuts': 5,
    'maximum_reachable_P_from_hub_bound': 5 * bound if ff_forbidden else None,
    'P_vertices_to_cover': len(structure['P_vertices']),
    'native': native, 'receipt': receipt,
    'scope': 'One hub adjacent to ALL distinct endpoints of 1..5 deleted old edges; all other old edges retained; no other added edges. No exclusion of arbitrary 651-vertex graphs.',
    'source_distance_BFS': 0, 'modified_graphs': 0, 'solver_calls': 0,
}
(HERE / 'RESULT.json').write_text(json.dumps(result, indent=2) + '\n')
(HERE / 'terminal.json').write_text(json.dumps({'status': result['status'], 'complete': True, 'pending': [], 'unattempted_source_edges': 0, **receipt}, indent=2) + '\n')
(HERE / 'WALK_COUNT_SCHEMA.json').write_text(json.dumps({
    'files': ['A2.u16le.bin', 'A3.u16le.bin'],
    'encoding': 'row-major 650 by 650 little-endian unsigned uint16',
    'row_and_column_labels': 'source vertex IDs 0..649',
    'meaning': 'Exact ordinary old-graph walks of length 2 or 3. Not distances or nonbacktracking counts.',
    'row_sums': {'A2': 100, 'A3': 1000}, 'source_path': structure['source_path'],
}, indent=2) + '\n')
print(json.dumps(result, indent=2))
