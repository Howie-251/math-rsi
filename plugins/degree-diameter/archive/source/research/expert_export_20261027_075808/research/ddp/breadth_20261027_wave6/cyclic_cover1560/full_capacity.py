"""Full120x120 voltage-form capacity and sparse input for the one fixed profile."""

import json
from pathlib import Path
import resource
import time


HERE = Path(__file__).resolve().parent


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (16, 16))
    started = time.process_time()
    prior = json.loads((HERE / "terminal.json").read_text())
    (HERE / "self_capacity.json").write_text(json.dumps(prior, indent=2) + "\n")
    gauge = json.loads((HERE / "tree_gauge.json").read_text())
    edges, free = gauge["edges"], gauge["free_edge_ids"]
    free_set = set(free)
    adjacency = [[] for _ in range(120)]
    for e, (u, v) in enumerate(edges):
        adjacency[u].append((v, e, 1))
        adjacency[v].append((u, e, -1))
    records, total_walks, total_forms, witness = [], 0, 0, None
    cache = HERE / "forms.txt"
    with cache.open("w") as output:
        output.write("120 360 13\n")
        output.write(str(len(free)) + " " + " ".join(map(str, free)) + "\n")
        for root in range(120):
            functions = [dict() for _ in range(120)]
            coefficients, walk = {}, [root]
            walks = 0

            def visit(u, depth):
                nonlocal walks
                walks += 1
                key = tuple(sorted((e, c % 13) for e, c in coefficients.items()))
                if key not in functions[u] or len(walk) < len(functions[u][key]):
                    functions[u][key] = list(walk)
                if depth == 5:
                    return
                for v, e, sign in adjacency[u]:
                    if e in free_set:
                        coefficients[e] = coefficients.get(e, 0) + sign
                        if not coefficients[e]:
                            del coefficients[e]
                    walk.append(v)
                    visit(v, depth + 1)
                    walk.pop()
                    if e in free_set:
                        coefficients[e] = coefficients.get(e, 0) - sign
                        if not coefficients[e]:
                            del coefficients[e]

            visit(root, 0)
            assert walks == 9331
            total_walks += walks
            for target, ff in enumerate(functions):
                count = len(ff)
                records.append({"source": root, "target": target, "mod13_forms": count})
                if count < 13:
                    witness = {"source": root, "target": target, "mod13_forms": count, "required13": 13,
                        "complete_walk_length_range": [0, 5], "root_walks_enumerated": walks,
                        "forms": [{"terms_mod13": terms, "representative_walk": path}
                                  for terms, path in sorted(ff.items())]}
                    break
            if witness:
                break
            for ff in functions:
                output.write(str(len(ff)) + "\n")
                for terms in sorted(ff):
                    output.write(str(len(terms)) + (" " + " ".join(f"{e} {c}" for e, c in terms) if terms else "") + "\n")
                total_forms += len(ff)
            if time.process_time() - started > 14:
                break
    passed = len(records) == 14400 and witness is None
    if witness:
        (HERE / "capacity_witness.json").write_text(json.dumps(witness, indent=2) + "\n")
    if not passed:
        cache.unlink(missing_ok=True)
    result = {"status": "ALL14400_FORM_CAPACITIES_PASS" if passed else
              "FORM_CAPACITY_OBSTRUCTION_STOP" if witness else "CAPACITY_TIME_LIMIT_INCOMPLETE",
              "base_vertices": 120, "base_edges": 360, "sheets": 13,
              "roots_enumerated": total_walks // 9331, "slots_checked": len(records),
              "raw_walks_enumerated": total_walks, "minimum_mod13_forms": min(r["mod13_forms"] for r in records),
              "maximum_mod13_forms": max(r["mod13_forms"] for r in records),
              "total_sparse_forms_for_scoring": total_forms if passed else None,
              "records": records, "witness": witness,
              "CPU_seconds": time.process_time() - started,
              "earlier_self_capacity_CPU_seconds": prior["CPU_seconds"],
              "sparse_cache_complete": passed, "voltage_search_started": False,
              "single_edge_proposals": 0, "BFS_performed": False}
    (HERE / "capacity.json").write_text(json.dumps(result, separators=(",", ":")) + "\n")
    if not passed:
        prior.update({"status": "CAPACITY_FAIL_NO_SEARCH" if witness else "CAPACITY_PREPARATION_INCOMPLETE_NO_SEARCH",
                      "full_capacity": {k: v for k, v in result.items() if k not in ("records", "witness")},
                      "pending": [], "CPU_seconds": prior["CPU_seconds"] + result["CPU_seconds"]})
        (HERE / "terminal.json").write_text(json.dumps(prior, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k not in ("records", "witness")}, indent=2))


if __name__ == "__main__":
    main()
