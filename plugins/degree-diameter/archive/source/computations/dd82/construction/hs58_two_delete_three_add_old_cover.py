"""Deterministic capacity matching to cover all old-old pairs; no SAT.

One bounded refinement of the two already saved degree-correct seeds.
Each actual M-bad pair is checked before deriving singleton color domains.
"""
from pathlib import Path
from itertools import combinations
import json
import resource
import time

from hs_augmentation import dump, verify
from hs58_two_delete_three_add_seeds import OUT, neighbors


def run():
    resource.setrlimit(resource.RLIMIT_CPU, (1, 1))
    start = time.monotonic()
    cpu = time.process_time()
    children = resource.getrusage(resource.RUSAGE_CHILDREN)
    target = OUT / "old_cover"
    target.mkdir(exist_ok=True)
    assert not (target / "result.json").exists(), "No unchanged rerun"
    results = []
    for kind in (2, 3):
        seed = json.loads((OUT / f"type{kind}" / "seed.json").read_text())
        old_edges = [tuple(e) for e in seed["edges"] if e[1] < 50]
        ns = neighbors(50, old_edges)
        free = seed["singleton_old_vertices"]
        free_set = set(free)
        fixed = {int(x): set(b) for x, b in seed["fixed_double_ports"].items()}
        zero = set(seed["zero_port_old_vertices"])
        bad = [(x, y) for x, y in combinations(range(50), 2)
               if y not in ns[x] and not (ns[x] & ns[y])]
        domains = {x: set(range(8)) for x in free}
        bad_kinds = {"fixed_fixed": [], "singleton_fixed": [], "unhandled": []}
        impossible = []
        for x, y in bad:
            if x in fixed and y in fixed:
                bad_kinds["fixed_fixed"].append([x, y])
                if not (fixed[x] & fixed[y]):
                    impossible.append([x, y])
            elif x in free_set and y in fixed:
                domains[x] &= fixed[y]
                bad_kinds["singleton_fixed"].append([x, y])
            elif y in free_set and x in fixed:
                domains[y] &= fixed[x]
                bad_kinds["singleton_fixed"].append([x, y])
            else:
                bad_kinds["unhandled"].append([x, y])
        result = dict(auxiliary_type=kind, actual_old_bad_pairs=bad,
                      old_bad_pair_types=bad_kinds,
                      impossible_fixed_pairs=impossible,
                      allowed_domains={str(x): sorted(domains[x]) for x in free},
                      residual_column_capacities=seed["residual_column_capacities"])
        if impossible or bad_kinds["unhandled"]:
            result["status"] = "STOP_FIXED_OR_UNHANDLED_OLD_PAIR"
            results.append(result)
            continue

        slots = [a for a, cap in enumerate(seed["residual_column_capacities"])
                 for _ in range(cap)]
        # Each capacity unit is a right-hand vertex. Standard deterministic
        # alternating-path bipartite matching, with old vertices and slots
        # visited in increasing order; at most forty augmentations.
        owner = [None] * len(slots)

        def augment(x, seen):
            for j, color in enumerate(slots):
                if j in seen or color not in domains[x]:
                    continue
                seen.add(j)
                if owner[j] is None or augment(owner[j], seen):
                    owner[j] = x
                    return True
            return False

        matched = 0
        for x in free:
            if augment(x, set()):
                matched += 1
        result["matched_singletons"] = matched
        if matched < len(free):
            # Alternating reachability from all unmatched left vertices
            # yields an explicit capacitated Hall deficit.
            owned = {x for x in owner if x is not None}
            left = set(free) - owned
            right = set()
            queue = sorted(left)
            for x in queue:
                for j, color in enumerate(slots):
                    if color in domains[x] and j not in right:
                        right.add(j)
                        if owner[j] is not None and owner[j] not in left:
                            left.add(owner[j])
                            queue.append(owner[j])
            colors = sorted(set().union(*(domains[x] for x in left)))
            capacity = sum(seed["residual_column_capacities"][a] for a in colors)
            assert len(left) > capacity == len(right)
            result.update(status="INFEASIBLE_CAPACITY_MATCHING",
                          hall_deficit=dict(old_vertices=sorted(left), colors=colors,
                                            old_count=len(left), available_capacity=capacity,
                                            deficit=len(left)-capacity))
            results.append(result)
            continue

        ports = {x: set(b) for x, b in fixed.items()}
        for j, x in enumerate(owner):
            ports[x] = {slots[j]}
        for x in zero:
            ports[x] = set()
        assert all(ports[x] & ports[y] for x, y in bad)
        graph_edges = sorted(old_edges + [(50+a, 50+b) for a,b in seed["auxiliary_edges"]]
                             + [(x,50+a) for x in range(50) for a in sorted(ports[x])])
        assert len(graph_edges) == len(set(graph_edges)) == 232
        assert all(len(s) == 8 for s in neighbors(58, graph_edges))
        data = dict(seed)
        data.update(edges=graph_edges, attachments=[sorted(ports[x]) for x in range(50)],
                    seed_rule="Deterministic maximum bipartite matching of singleton allowed domains to exact capacity slots; all old-old pairs covered.",
                    source_seed=f"../type{kind}/seed.json")
        path = target / f"type{kind}.seed.json"
        dump(path, data)
        path.with_suffix(".edges").write_text("".join(f"{x} {y}\n" for x,y in graph_edges))
        checked = json.loads(verify(path))
        full = json.loads(path.with_suffix(".verification.json").read_text())
        assert all(b["pair"][0] < 50 <= b["pair"][1] for b in full["bad_pairs"])
        forced = [b for b in full["bad_pairs"] if b["pair"] in ([0,56],[0,57])]
        assert len(forced) == 2
        result.update(status="COMPLETE_OLD_COVER_SEED", independent_graph_check=checked,
                      forced_failure_witnesses=forced,
                      all_remaining_bad_pairs_are_old_new=True,
                      assignment={str(x): next(iter(ports[x])) for x in free})
        results.append(result)
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    report = dict(results=results, solver_runs=0, graph_search_runs=0,
                  algorithm="Deterministic bipartite capacity matching; no optimization or SAT",
                  cpu_budget_seconds=1, parent_cpu_seconds=time.process_time()-cpu,
                  independent_bfs_child_cpu_seconds=after.ru_utime+after.ru_stime-children.ru_utime-children.ru_stime,
                  wall_seconds=time.monotonic()-start)
    dump(target / "result.json", report)
    print(json.dumps(report))


if __name__ == "__main__":
    run()
