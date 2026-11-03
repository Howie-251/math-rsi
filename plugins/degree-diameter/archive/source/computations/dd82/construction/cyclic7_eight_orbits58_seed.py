"""One bounded colored-HS automorphism diagnosis and one complete C7 seed.

No optimization, SAT or search in the already excluded induced-HS family.
"""
from pathlib import Path
from math import lcm
import json
import os
import resource
import signal
import subprocess
import time

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'computations/dd82/construction'
OUT = BASE / 'cyclic7_eight_orbits58_seed_run'
SOURCE = BASE / 'hs58_edge_k26_structure_run/hs50.edges'


def dump(path, value):
    path.write_text(json.dumps(value, indent=2) + '\n')


def cycles(p):
    unseen = set(range(len(p)))
    result = []
    while unseen:
        v = min(unseen)
        orbit = []
        while v in unseen:
            unseen.remove(v)
            orbit.append(v)
            v = p[v]
        assert v == orbit[0]
        result.append(orbit)
    return result


def power(p, exponent):
    q = list(range(len(p)))
    for _ in range(exponent):
        q = [p[v] for v in q]
    return q


class CpuBudget(Exception):
    pass


def main():
    start_cpu, start_wall = time.process_time(), time.monotonic()
    os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
    resource.setrlimit(resource.RLIMIT_CPU, (10, 11))
    OUT.mkdir(exist_ok=True)
    assert not (OUT / 'launch.json').exists(), 'One bounded diagnosis only'
    dump(OUT / 'launch.json', dict(source=str(SOURCE.relative_to(ROOT)),
        total_cpu_budget_seconds=10, graphmatcher_cpu_stop=8.5,
        graphmatcher_attempts=1, optimization=False, sat=False))
    result = dict(status='started', found_order7=False, seed_exported=False)
    signal.signal(signal.SIGPROF, lambda *args: (_ for _ in ()).throw(CpuBudget()))
    signal.setitimer(signal.ITIMER_PROF, max(.1, 8.5-time.process_time()))
    try:
        import networkx as nx
        lines = SOURCE.read_text().splitlines()
        assert tuple(map(int, lines[0].split())) == (50, 175)
        edges = {tuple(sorted(map(int, line.split()))) for line in lines[1:]}
        assert len(edges) == 175
        graph = nx.Graph()
        graph.add_nodes_from(range(50))
        graph.add_edges_from(edges)
        assert all(graph.degree(v) == 7 for v in graph)
        c = 0
        neighbors = sorted(graph[c])
        source_graph, target_graph = graph.copy(), graph.copy()
        nx.set_node_attributes(source_graph, -1, 'color')
        nx.set_node_attributes(target_graph, -1, 'color')
        source_graph.nodes[c]['color'] = target_graph.nodes[c]['color'] = 7
        for i, u in enumerate(neighbors):
            source_graph.nodes[u]['color'] = i
            target_graph.nodes[neighbors[(i+1) % 7]]['color'] = i
        dump(OUT / 'constraints.json', dict(fixed_vertex=c, neighbors=neighbors,
            prescribed_neighbor_images=neighbors[1:]+neighbors[:1]))
        matcher = nx.algorithms.isomorphism.GraphMatcher(source_graph, target_graph,
            node_match=nx.algorithms.isomorphism.categorical_node_match('color', -1))
        lookup_cpu = time.process_time()
        mapping = next(matcher.isomorphisms_iter(), None)
        result['graphmatcher_cpu_seconds'] = time.process_time()-lookup_cpu
        signal.setitimer(signal.ITIMER_PROF, 0)
        if mapping is None:
            result['status'] = 'prescribed_local_cycle_has_no_extension'
        else:
            p = [mapping[v] for v in range(50)]
            assert sorted(p) == list(range(50)) and p[c] == c
            assert {tuple(sorted((p[u], p[v]))) for u, v in edges} == edges
            original_cycles = cycles(p)
            original_order = lcm(*(len(cycle) for cycle in original_cycles))
            assert original_order % 7 == 0 and original_order % 49 != 0
            exponent = original_order // 7
            q = power(p, exponent)
            q_cycles = cycles(q)
            dump(OUT / 'hs.automorphism.json', dict(first_permutation=p,
                first_cycle_type=sorted(map(len, original_cycles)),
                first_order=original_order, power_taken=exponent,
                order7_permutation=q, order7_cycles=q_cycles,
                checked_original_edge_images=175))
            assert {tuple(sorted((q[u], q[v]))) for u, v in edges} == edges
            if sorted(map(len, q_cycles)) != [1]+[7]*7:
                result['status'] = 'extension_found_but_required_cycle_type_failed'
            else:
                result['found_order7'] = True
                old_orbits = [cycle for cycle in q_cycles if len(cycle) == 7]
                new_orbit, fixed_new = list(range(50, 57)), 57
                full_edges = edges | {(c, fixed_new)}
                full_edges |= {(v, fixed_new) for v in new_orbit}
                full_edges |= {tuple(sorted((orbit[t], new_orbit[t])))
                    for orbit in old_orbits for t in range(7)}
                assert len(full_edges) == 232
                q58 = q + [50+(t+1) % 7 for t in range(7)] + [fixed_new]
                assert {tuple(sorted((q58[u], q58[v]))) for u, v in full_edges} == full_edges
                fixed = [c, fixed_new]
                orbits = old_orbits+[new_orbit]
                new_to_old = fixed+[v for orbit in orbits for v in orbit]
                old_to_new = [new_to_old.index(v) for v in range(58)]
                reindexed = {tuple(sorted((old_to_new[u], old_to_new[v]))) for u, v in full_edges}
                degree = [0]*58
                for u, v in reindexed:
                    degree[u] += 1
                    degree[v] += 1
                assert degree == [8]*58
                seed = dict(n=58, edges=sorted(reindexed), original_source=str(SOURCE.relative_to(ROOT)),
                    coordinates='fixed vertices 0,1; orbit a vertex 2+7*a+t',
                    induced_hs_preserved=True, target_claim=False)
                dump(OUT / 'seed.json', seed)
                dump(OUT / 'seed.original.json', dict(n=58, edges=sorted(full_edges)))
                (OUT / 'seed.edges').write_text('58 232\n'+''.join(f'{u} {v}\n' for u, v in sorted(reindexed)))
                dump(OUT / 'coordinates.json', dict(fixed_vertices_original=fixed,
                    orbits_original=orbits, old_to_new=old_to_new, new_to_old=new_to_old,
                    original_permutation=q58, cycle_type=sorted(map(len, cycles(q58))),
                    checked_full_edge_images=232))
                palette = []
                def add(kind, parameters, expanded):
                    expanded = {tuple(sorted(e)) for e in expanded}
                    overlap = expanded & reindexed
                    assert len(overlap) in (0, len(expanded))
                    palette.append(dict(index=len(palette), kind=kind, **parameters,
                        selected=bool(overlap), edges=sorted(expanded)))
                add('fixed_fixed', dict(fixed=[0, 1]), [(0, 1)])
                for f in range(2):
                    for a in range(8):
                        add('fixed_orbit', dict(fixed=f, orbit=a), [(f, 2+7*a+t) for t in range(7)])
                shifts = [[[] for _ in range(8)] for _ in range(8)]
                for a in range(8):
                    for d in range(1, 4):
                        add('internal', dict(a=a, b=a, shift=d),
                            [(2+7*a+t, 2+7*a+(t+d) % 7) for t in range(7)])
                        if palette[-1]['selected']:
                            shifts[a][a] += [d, (-d) % 7]
                    for b in range(a+1, 8):
                        for d in range(7):
                            add('cross', dict(a=a, b=b, shift=d),
                                [(2+7*a+t, 2+7*b+(t+d) % 7) for t in range(7)])
                            if palette[-1]['selected']:
                                shifts[a][b].append(d)
                                shifts[b][a].append((-d) % 7)
                assert len(palette) == 237 and sum(len(o['edges']) for o in palette) == 58*57//2
                reconstructed = {tuple(e) for o in palette if o['selected'] for e in o['edges']}
                assert reconstructed == reindexed
                dump(OUT / 'palette.json', dict(orbit_count=237, orbits=palette))
                dump(OUT / 'parameters.json', dict(fixed_edge=True,
                    fixed_orbit_incidence=[[int(all((min(f, 2+7*a+t), max(f, 2+7*a+t)) in reindexed
                        for t in range(7))) for a in range(8)] for f in range(2)],
                    shifts=[[sorted(cell) for cell in row] for row in shifts],
                    selected_orbit_indices=[o['index'] for o in palette if o['selected']],
                    quotient_diagonal=[len(shifts[a][a]) for a in range(8)]))
                before = resource.getrusage(resource.RUSAGE_CHILDREN)
                verified = subprocess.run(['python', str(BASE/'verify_hs_candidate.py'), str(OUT/'seed.json')],
                    capture_output=True, text=True)
                (OUT/'verification.log').write_text(verified.stdout+verified.stderr)
                after = resource.getrusage(resource.RUSAGE_CHILDREN)
                result['independent_bfs_cpu_seconds'] = after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
                assert verified.returncode == 0
                verification = json.loads((OUT/'seed.verification.json').read_text())
                assert verification['n'] == 58 and verification['edges'] == 232 and verification['degrees'] == [8]*58
                result.update(status='verified_order7_and_expanded_seed', seed_exported=True,
                    original_hs_cycle_type=sorted(map(len, q_cycles)),
                    seed_cycle_type=sorted(map(len, cycles(q58))),
                    selected_orbit_count=sum(o['selected'] for o in palette),
                    verification={k: verification[k] for k in ['n', 'edges', 'max_degree', 'bad_pair_count', 'diameter', 'valid_target']})
    except CpuBudget:
        result['status'] = 'graphmatcher_cpu_limit_no_decision'
    finally:
        signal.setitimer(signal.ITIMER_PROF, 0)
        child = resource.getrusage(resource.RUSAGE_CHILDREN)
        result.update(parent_cpu_seconds=time.process_time()-start_cpu,
            total_cpu_seconds=time.process_time()+child.ru_utime+child.ru_stime,
            elapsed_task_cpu_seconds=time.process_time()-start_cpu+child.ru_utime+child.ru_stime,
            wall_seconds=time.monotonic()-start_wall, total_cpu_budget_seconds=10)
        dump(OUT/'result.json', result)
        print(json.dumps(result), flush=True)


if __name__ == '__main__':
    main()
