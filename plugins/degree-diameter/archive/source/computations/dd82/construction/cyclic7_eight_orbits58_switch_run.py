"""One strict descent with all 220 nonfixed C7 edge orbits available."""
from collections import Counter
from pathlib import Path
import json
import os
import resource
import subprocess
import time

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT/'computations/dd82/construction'
SEED = BASE/'cyclic7_eight_orbits58_seed_run'
OUT = BASE/'cyclic7_eight_orbits58_switch_run'


def dump(path, obj):
    path.write_text(json.dumps(obj, indent=2)+'\n')


def children_cpu():
    r = resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime+r.ru_stime


def main():
    start, parent_cpu, child_start = time.monotonic(), time.process_time(), children_cpu()
    os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
    OUT.mkdir(exist_ok=True)
    assert not (OUT/'launch.json').exists(), 'Exactly one strict descent episode'
    all_orbits = json.loads((SEED/'palette.json').read_text())['orbits']
    fixed_edges = sorted(tuple(e) for o in all_orbits if o['selected'] and o['kind'].startswith('fixed') for e in o['edges'])
    assert len(fixed_edges) == 15
    core = [dict(o, index=i, source_orbit_index=o['index'])
        for i, o in enumerate(o for o in all_orbits if o['kind'] in ['internal', 'cross'])]
    assert len(core) == 220 and sum(o['selected'] for o in core) == 31
    initial_score = json.loads((SEED/'seed.verification.json').read_text())['bad_pair_count']
    assert initial_score == 105
    input_file = OUT/'input.txt'
    input_file.write_text(f'220 31 {initial_score}\n15\n'
        + ''.join(f'{u} {v}\n' for u, v in fixed_edges)
        + ''.join(f"{o['index']} {o['a']} {o['b']} {o['shift']} {int(o['selected'])}\n" for o in core))
    dump(OUT/'domain.json', dict(fixed_edges=fixed_edges, core_orbits=core,
        source=str(SEED.relative_to(ROOT)), full_graph_vertices=58,
        preserved_core_degrees=[7,8,8,8,8,8,8,7], independent_special_orbits_hard_filter=False))
    dump(OUT/'launch.json', dict(total_cpu_budget_seconds=30, initial_bad_pairs=initial_score,
        episodes=1, neutral_moves=False, random_restarts=0,
        quotient_hard_filter=False, independent_special_orbits_hard_filter=False,
        source=str(SEED.relative_to(ROOT))))
    before = children_cpu()
    compiled = subprocess.run(['g++','-O3','-std=c++17',str(BASE/'cyclic7_eight_orbits58_switch.cpp'),
        '-o',str(BASE/'cyclic7_eight_orbits58_switch.bin')],capture_output=True,text=True)
    compile_cpu = children_cpu()-before
    (OUT/'compile.log').write_text(compiled.stdout+compiled.stderr)
    assert compiled.returncode == 0
    search_budget = max(.1, 29.0-compile_cpu-(time.process_time()-parent_cpu))
    def limits():
        resource.setrlimit(resource.RLIMIT_CPU, (max(1,int(search_budget)+1),max(2,int(search_budget)+2)))
        resource.setrlimit(resource.RLIMIT_AS, (1024**3,1024**3))
    before = children_cpu()
    with (OUT/'search.log').open('w') as log:
        run = subprocess.run([str(BASE/'cyclic7_eight_orbits58_switch.bin'),str(input_file),str(OUT),str(search_budget)],
            stdout=log,stderr=subprocess.STDOUT,preexec_fn=limits)
    search_process_cpu = children_cpu()-before
    assert run.returncode == 0
    search = json.loads((OUT/'search.json').read_text())
    assert search['initial_bad_pairs'] == initial_score
    final = json.loads((OUT/'candidate.best.json').read_text())
    before = children_cpu()
    checked = subprocess.run(['python',str(BASE/'verify_hs_candidate.py'),str(OUT/'candidate.best.json')],
        capture_output=True,text=True)
    bfs_cpu = children_cpu()-before
    (OUT/'verification.log').write_text(checked.stdout+checked.stderr)
    assert checked.returncode == 0
    verification = json.loads((OUT/'candidate.best.verification.json').read_text())
    assert verification['bad_pair_count'] == final['bad_pairs_exact'] == search['best_bad_pairs']
    assert verification['n'] == 58 and verification['edges'] == 232 and verification['degrees'] == [8]*58
    coordinates = json.loads((SEED/'coordinates.json').read_text())
    new_to_old = coordinates['new_to_old']
    original_source = json.loads((SEED/'seed.json').read_text())['original_source']
    old_hs_edges = {tuple(map(int,line.split())) for line in (ROOT/original_source).read_text().splitlines()[1:]}
    state_trace = []
    for path in sorted(OUT.glob('state[0-9][0-9][0-9].json')):
        state = json.loads(path.read_text())
        old_labeled = {tuple(sorted((new_to_old[u],new_to_old[v]))) for u,v in state['edges']}
        core_matrix = [[0]*8 for _ in range(8)]
        for p in state['selected_parameters']:
            a,b = p['a'],p['b']
            if a == b: core_matrix[a][a] += 2
            else: core_matrix[a][b] += 1;core_matrix[b][a] += 1
        assert [sum(row) for row in core_matrix] == [7,8,8,8,8,8,8,7]
        state_trace.append(dict(state=path.name, bad_pair_count=state['bad_pairs_exact'],
            original_hs_edges_deleted=sorted(old_hs_edges-old_labeled),
            original_hs_deleted_count=len(old_hs_edges-old_labeled),
            added_old_old_edges=sorted(e for e in old_labeled if e[1]<50 and e not in old_hs_edges),
            core_quotient=core_matrix, core_internal_degrees=[core_matrix[a][a] for a in range(8)],
            move=state['move']))
    def label(v):
        return f'fixed{v}' if v<2 else f'orbit{(v-2)//7}'
    failure = dict(original_hs_source=original_source, state_trace=state_trace,
        left_original_induced_hs=state_trace[-1]['original_hs_deleted_count']>0,
        bad_pairs_by_orbits=dict(Counter(','.join(sorted(label(v) for v in item['pair']))
            for item in verification['bad_pairs'])))
    dump(OUT/'failure_structure.json', failure)
    result = dict(compile_cpu_seconds=compile_cpu, search_process_cpu_seconds=search_process_cpu,
        independent_bfs_cpu_seconds=bfs_cpu, parent_cpu_seconds=time.process_time()-parent_cpu,
        total_cpu_seconds=children_cpu()-child_start+time.process_time()-parent_cpu,
        wall_seconds=time.monotonic()-start, total_cpu_budget_seconds=30, search=search,
        original_hs_deleted_count=state_trace[-1]['original_hs_deleted_count'],
        left_original_induced_hs=failure['left_original_induced_hs'],
        verification={k:verification[k] for k in ['n','edges','max_degree','bad_pair_count','diameter','valid_target']})
    dump(OUT/'resources.json', result)
    print(json.dumps(result), flush=True)


if __name__ == '__main__':
    main()
