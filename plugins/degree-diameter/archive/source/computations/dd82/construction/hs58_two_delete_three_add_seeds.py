"""Two complete degree-correct HS58 seeds; no solver or graph search.

The planned attachment SAT calls were cancelled before launch because of
the deletion-endpoint coverage obstruction.  The seeds retain the exact
authorized old core and both remaining auxiliary representatives.
"""
from pathlib import Path
import json
import resource
import time

from hs_augmentation import base, dump, verify

OUT = Path(__file__).with_name("hs58_two_delete_three_add_seeds_run")
D = {(0, 1), (10, 11)}
A = {(25, 26), (35, 41), (2, 4)}
H = {
    2: [(0, 1), (0, 2), (0, 4), (0, 5), (0, 6), (0, 7), (1, 2), (1, 3)],
    3: [(0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 2), (1, 3)],
}
CENTERS = {2: 3, 3: 1}


def neighbors(n, edges):
    ns = [set() for _ in range(n)]
    for x, y in edges:
        ns[x].add(y)
        ns[y].add(x)
    return ns


def main():
    wall = time.monotonic()
    cpu = time.process_time()
    child = resource.getrusage(resource.RUSAGE_CHILDREN)
    OUT.mkdir(exist_ok=True)
    assert not (OUT / "result.json").exists(), "No unchanged rerun"
    old_base, _ = base()
    old_base = set(old_base)
    assert D <= old_base and A.isdisjoint(old_base)
    deleted_endpoints = {v for e in D for v in e}
    zero_ports = {v for e in A for v in e}
    assert len(deleted_endpoints) == 4 and len(zero_ports) == 6
    assert deleted_endpoints.isdisjoint(zero_ports)
    old_edges = sorted((old_base - D) | A)
    old_ns = neighbors(50, old_edges)
    free = sorted(set(range(50)) - deleted_endpoints - zero_ports)
    assert len(free) == 40
    results = []
    for kind in (2, 3):
        target = OUT / f"type{kind}"
        target.mkdir(exist_ok=True)
        h = H[kind]
        hn = neighbors(8, h)
        u = CENTERS[kind]
        ports = {0: {u, 4}, 1: {u, 5}, 10: {u, 6}, 11: {u, 7}}
        fixed_incidence = [sum(a in b for b in ports.values()) for a in range(8)]
        capacities = [8 - len(hn[a]) - fixed_incidence[a] for a in range(8)]
        assert sum(capacities) == 40 and min(capacities) >= 0
        slots = [a for a, capacity in enumerate(capacities) for _ in range(capacity)]
        # A deterministic capacity bijection, with no distance optimization.
        for x, a in zip(free, slots):
            ports[x] = {a}
        for x in zero_ports:
            ports[x] = set()
        assert all(len(old_ns[x]) + len(ports[x]) == 8 for x in range(50))
        edges = sorted(old_edges + [(50 + a, 50 + b) for a, b in h]
                       + [(x, 50 + a) for x in range(50) for a in sorted(ports[x])])
        assert len(edges) == len(set(edges)) == 232
        graph_ns = neighbors(58, edges)
        assert all(len(v) == 8 for v in graph_ns)
        seed = dict(n=58, edges=edges, source="hs_augmentation.base()",
                    old_deletions=sorted(D), old_additions=sorted(A),
                    auxiliary_type=kind, auxiliary_edges=h, bad_star_center=u,
                    fixed_double_ports={str(x): sorted(ports[x]) for x in sorted(deleted_endpoints)},
                    zero_port_old_vertices=sorted(zero_ports),
                    singleton_old_vertices=free, residual_column_capacities=capacities,
                    attachments=[sorted(ports[x]) for x in range(50)],
                    seed_rule="Pair sorted singleton old vertices with sorted repeated capacity slots; no optimization.")
        path = target / "seed.json"
        dump(path, seed)
        (target / "seed.edges").write_text("".join(f"{x} {y}\n" for x, y in edges))
        independent = json.loads(verify(path))
        full_check = json.loads(path.with_suffix(".verification.json").read_text())
        assert full_check["n"] == 58 and full_check["edges"] == 232
        assert full_check["degrees"] == [8] * 58

        # Actual-label version of the conditional deletion-endpoint obstruction.
        # For a completion, each ordinary old neighbor t of x=0 must repair
        # the lost old pair (t,y=1) via a shared new neighbor.  Both t and y
        # are untouched by A, so there is no replacement old length-two path.
        x, y = 0, 1
        ordinary_neighbors = sorted(old_ns[x] & set(free))
        zero_neighbors = sorted(old_ns[x] & zero_ports)
        other_deleted_neighbors = sorted(old_ns[x] & (deleted_endpoints - {x, y}))
        assert ordinary_neighbors == [30, 40, 45]
        assert zero_neighbors == [4, 25, 35]
        assert not other_deleted_neighbors
        lost_pairs = []
        for t in ordinary_neighbors:
            assert y not in old_ns[t] and not (old_ns[y] & old_ns[t])
            actual_common = sorted(graph_ns[t] & graph_ns[y])
            match = next((b for b in full_check["bad_pairs"] if b["pair"] == sorted((y, t))), None)
            lost_pairs.append(dict(pair=sorted((y, t)), old_common_neighbors=[],
                                   necessary_singleton_colors=sorted(ports[y]),
                                   actual_singleton_color=next(iter(ports[t])),
                                   actual_common_neighbors=actual_common,
                                   actual_bad_pair=match))
        allowed_bad_leaf_reach = ({4} | (ports[y] & {4, 5, 6, 7})
                                 | ((hn[u] | hn[4]) & {4, 5, 6, 7}))
        missing_bad_leaves = sorted({4, 5, 6, 7} - allowed_bad_leaf_reach)
        assert missing_bad_leaves == [6, 7]
        witness = dict(old_vertex=x, deleted_partner=y, old_neighbors=sorted(old_ns[x]),
                       ordinary_old_neighbors=ordinary_neighbors,
                       zero_port_old_neighbors=zero_neighbors,
                       other_deleted_endpoint_neighbors=other_deleted_neighbors,
                       direct_new_neighbors=sorted(ports[x]),
                       h_one_step_from_ports=sorted(hn[u] | hn[4]),
                       necessary_lost_old_pair_repairs=lost_pairs,
                       conditional_reachable_bad_leaves=sorted(allowed_bad_leaf_reach),
                       forced_missing_new_vertices_if_all_old_pairs_covered=[50 + a for a in missing_bad_leaves],
                       statement="If every old-old pair is covered, colors at 30,40,45 must lie in B_1. Then old vertex 0 cannot reach new vertices 56 or 57 within two steps.",
                       seed_violation="The deterministic seed uses forbidden colors at old vertices 40 and 45, so the old-old pairs (1,40),(1,45) already fail.")
        assert all(row["actual_bad_pair"] is not None for row in lost_pairs if row["pair"][1] in (40, 45))
        dump(target / "failure_witness.json", witness)
        results.append(dict(auxiliary_type=kind, residual_column_capacities=capacities,
                            independent_graph_check=independent,
                            solver_started=False, solver_cpu_seconds=0,
                            stop_reason="Cancelled before launch: analytic deletion-endpoint coverage obstruction",
                            scope="Fixed D/A, fixed H representative, and assigned double ports; no attachment domain was enumerated."))
    child_after = resource.getrusage(resource.RUSAGE_CHILDREN)
    report = dict(results=results, seeds_completed=2, solver_runs=0,
                  graph_search_runs=0, cnf_generated=False,
                  parent_cpu_seconds=time.process_time() - cpu,
                  independent_bfs_child_cpu_seconds=(child_after.ru_utime + child_after.ru_stime - child.ru_utime - child.ru_stime),
                  wall_seconds=time.monotonic() - wall)
    dump(OUT / "result.json", report)
    print(json.dumps(report))


if __name__ == "__main__":
    main()
