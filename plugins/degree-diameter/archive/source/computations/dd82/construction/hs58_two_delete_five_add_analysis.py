"""Concrete port-capacity and route witnesses for the saved a5 seeds."""
from itertools import combinations
from pathlib import Path
import json
import time

from hs_augmentation import dump

HERE = Path(__file__).parent / "hs58_two_delete_five_add_switch_run"


def analyze(name):
    data = json.loads((HERE / name).read_text())
    adj = [set() for _ in range(58)]
    for x, y in data["edges"]:
        adj[x].add(y)
        adj[y].add(x)
    old = [s & set(range(50)) for s in adj[:50]]
    ports = [sorted(y-50 for y in adj[x] if y >= 50) for x in range(50)]
    h = [{y-50 for y in adj[50+a] if y >= 50} for a in range(8)]
    rows = []
    zero_bounds = []
    for x in range(50):
        direct = set(ports[x])
        old_route = set().union(*(set(ports[y]) for y in old[x]))
        new_route = set().union(*(h[a] for a in ports[x]))
        missing = set(range(8)) - direct - old_route - new_route
        rows.append(dict(old_vertex=x, ports=ports[x], old_neighbors=sorted(old[x]),
                         direct_labels=sorted(direct), old_intermediate_labels=sorted(old_route),
                         new_intermediate_labels=sorted(new_route), missing_labels=sorted(missing)))
        if not ports[x]:
            cap = sum(len(ports[y]) for y in old[x])
            zero_bounds.append(dict(old_vertex=x, old_neighbors=sorted(old[x]),
                                   neighbor_port_counts=[len(ports[y]) for y in sorted(old[x])],
                                   summed_port_capacity=cap,
                                   obstruction_to_any_reattachment=(cap < 8)))
    broken = [dict(pair=[x,y], current_common_new=sorted(set(ports[x]) & set(ports[y])))
              for x,y in combinations(range(50),2) if y not in old[x] and not old[x]&old[y]]
    assert all(row["current_common_new"] for row in broken)
    report = dict(source=name, auxiliary_catalog_type=data["auxiliary_catalog_type"],
                  old_deletions=data["old_deletions"], old_additions=data["old_additions"],
                  ports=ports, rows=rows, zero_port_capacity_bounds=zero_bounds,
                  zero_port_obstructions=[r for r in zero_bounds if r["obstruction_to_any_reattachment"]],
                  old_pairs_repaired_through_new=broken,
                  explained_old_new_bad_pairs=sum(len(row["missing_labels"]) for row in rows),
                  scope="Exact witnesses for this saved full graph. Zero-row degree-sum obstructions additionally exclude all reattachments with this fixed old core.")
    dump(HERE / name.replace(".json", ".analysis.json"), report)
    return dict(path=name, old_new_bad_pairs=report["explained_old_new_bad_pairs"],
                zero_port_obstructions=report["zero_port_obstructions"])


if __name__ == "__main__":
    cpu, wall = time.process_time(), time.monotonic()
    result = [analyze(name) for name in ("type54.best.json", "type14.old_covered.json")]
    dump(HERE / "failure_analysis.json", dict(results=result,
         cpu_seconds=time.process_time()-cpu, wall_seconds=time.monotonic()-wall))
    print(json.dumps(result))
