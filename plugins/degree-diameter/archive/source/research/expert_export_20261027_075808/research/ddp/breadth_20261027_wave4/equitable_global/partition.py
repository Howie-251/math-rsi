"""One anchored 1-WL partition of the entire H(9) fold, independent of witnesses."""

from collections import Counter
import json
from pathlib import Path
import time


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE = ROOT / "research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/Q_data.json"


def main():
    started = time.process_time()
    data = json.loads(SOURCE.read_text())
    nq, nh = len(data["Q"]), len(data["H3_graph"])
    adjacency = [list(a) for a in data["Q"]]
    for f, h in enumerate(data["H3_neighbors"]):
        if h is not None and h >= 0:
            adjacency[f].append(nq + h)
    adjacency.extend([
        list(data["H3_generic_neighbors"][h]) + [nq + j for j in data["H3_graph"][h]]
        for h in range(nh)
    ])
    absolute = [h for h, a in enumerate(data["H3_absolute"]) if a]
    anchor_h = min(absolute, key=lambda h: data["H3_fold_ids"][h])
    colours = [0] * nq + [2 if a else 1 for a in data["H3_absolute"]]
    colours[nq + anchor_h] = 3
    rounds = [{"round": 0, "cells": 4}]
    round_number = 0
    while True:
        signatures = [
            (colours[v], tuple(sorted(Counter(colours[u] for u in adjacency[v]).items())))
            for v in range(nq + nh)
        ]
        order = {sig: i for i, sig in enumerate(sorted(set(signatures)))}
        refined = [order[sig] for sig in signatures]
        round_number += 1
        cell_count = len(order)
        rounds.append({"round": round_number, "cells": cell_count})
        stable = cell_count == len(set(colours))
        colours = refined
        if stable:
            break
    members = [[] for _ in range(max(colours) + 1)]
    for v, c in enumerate(colours):
        members[c].append(v)
    cells = []
    for i, vertices in enumerate(members):
        v = vertices[0]
        counts = Counter(colours[u] for u in adjacency[v])
        assert all(Counter(colours[u] for u in adjacency[w]) == counts for w in vertices)
        is_generic = v < nq
        assert all((w < nq) == is_generic for w in vertices)
        kind = "generic" if is_generic else "H3_absolute" if data["H3_absolute"][v - nq] else "H3_nonabsolute"
        cells.append({
            "id": i, "kind": kind, "size": len(vertices), "members": vertices,
            "neighbor_counts": dict(sorted(counts.items())),
        })
    generic_cells = [c for c in cells if c["kind"] == "generic"]
    h3_cells = [c for c in cells if c["kind"] != "generic"]
    result = {
        "status": "STABLE_EQUITABLE_PARTITION",
        "source": str(SOURCE.relative_to(ROOT)),
        "node_encoding": "0..33032 are Q indices; 33033+h is H3 index h",
        "initial_colours": "generic / H3 nonabsolute / H3 absolute / one anchored H3 absolute",
        "author_split_state_used": False,
        "anchor_H3_index": anchor_h,
        "anchor_fold_id": data["H3_fold_ids"][anchor_h],
        "anchor_point_representative": data["H3_point_representatives"][anchor_h],
        "fold_nodes": nq + nh,
        "rounds": rounds,
        "cell_count": len(cells),
        "generic_cell_count": len(generic_cells),
        "H3_cell_count": len(h3_cells),
        "generic_cell_size_histogram": dict(sorted(Counter(c["size"] for c in generic_cells).items())),
        "H3_cell_size_histogram": dict(sorted(Counter(c["size"] for c in h3_cells).items())),
        "equitable_counts_checked_for_all_vertices": True,
        "cell_of_vertex": colours,
        "cells": cells,
        "CPU_seconds": time.process_time() - started,
    }
    (HERE / "partition.json").write_text(json.dumps(result, separators=(",", ":")) + "\n")
    summary = {k: v for k, v in result.items() if k not in ("cells", "cell_of_vertex")}
    (HERE / "partition_summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
