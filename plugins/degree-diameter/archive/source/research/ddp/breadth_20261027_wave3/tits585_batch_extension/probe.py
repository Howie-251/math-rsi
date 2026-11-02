"""Small deterministic radius-two probe; no full-source BFS or graph search."""

from collections import Counter
import json
from pathlib import Path
import time


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE = ROOT / "research/ddp/polarity585_replication/source585.implicit_adj.txt"


def bits(vertices):
    return sum(1 << v for v in vertices)


def main():
    start = time.process_time()
    adj = [set(map(int, line.split())) for line in SOURCE.read_text().splitlines() if line.strip()]
    n = len(adj)
    absolute = [v for v in range(n) if len(adj[v]) == 8]
    nonabsolute = [v for v in range(n) if len(adj[v]) == 9]
    absolute_mask = bits(absolute)
    full = (1 << n) - 1
    radius_two = []
    for v in range(n):
        ball = {v} | adj[v]
        for u in adj[v]:
            ball.update(adj[u])
        radius_two.append(bits(ball))

    def covered(spokes):
        result = 0
        for v in spokes:
            result |= radius_two[v]
        return result

    # These are the actual neighborhoods giving the known twin construction.
    known_twin_groups = [sorted(adj[a]) for a in absolute]
    known_twin_histogram = Counter(covered(group).bit_count() for group in known_twin_groups)

    # Twelve fixed, deterministic starts, at most ten spokes each.  There is no
    # random restart, no backtracking, and no attempted simultaneous packing.
    samples = []
    for seed in absolute[:4] + nonabsolute[:8]:
        spokes = [seed]
        mask = radius_two[seed]
        sample = {"seed": seed, "seed_type": "A" if seed in absolute else "B", "coverage": {}}
        while len(spokes) < 10:
            candidates = [v for v in range(n) if v not in spokes]
            v = max(candidates, key=lambda u: ((radius_two[u] & ~mask).bit_count(), -u))
            spokes.append(v)
            mask |= radius_two[v]
            if len(spokes) in (8, 9, 10):
                sample["coverage"][str(len(spokes))] = {
                    "spokes": list(spokes),
                    "covered_old": mask.bit_count(),
                    "uncovered_old": [u for u in range(n) if not (mask >> u) & 1],
                    "covered_absolute": (mask & absolute_mask).bit_count(),
                    "equals_old_open_neighborhood_of": [u for u in range(n) if adj[u] == set(spokes)],
                }
        samples.append(sample)

    result = {
        "scope": "Radius-two unions and 12 deterministic greedy starts; not a batch construction or nonexistence test.",
        "source": "research/ddp/polarity585_replication/source585.implicit_adj.txt",
        "source_primary_url": "https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD3/n585d9k3.txt",
        "n": n,
        "degree_histogram": dict(sorted(Counter(map(len, adj)).items())),
        "edge_count": sum(map(len, adj)) // 2,
        "radius_two_size_histogram_A": dict(sorted(Counter(radius_two[v].bit_count() for v in absolute).items())),
        "radius_two_size_histogram_B": dict(sorted(Counter(radius_two[v].bit_count() for v in nonabsolute).items())),
        "radius_two_absolute_count_histogram_A": dict(sorted(Counter((radius_two[v] & absolute_mask).bit_count() for v in absolute).items())),
        "radius_two_absolute_count_histogram_B": dict(sorted(Counter((radius_two[v] & absolute_mask).bit_count() for v in nonabsolute).items())),
        "known_twin_groups": {
            "group_count": len(known_twin_groups),
            "size": 8,
            "coverage_histogram": dict(sorted(known_twin_histogram.items())),
            "first_group": known_twin_groups[0],
        },
        "greedy_samples": samples,
        "best_greedy_coverage_by_size": {
            str(size): max(s["coverage"][str(size)]["covered_old"] for s in samples) for size in (8, 9, 10)
        },
        "old_spoke_capacity_by_delta": {
            str(delta): {"A": 65 * (delta - 8), "B": 520 * (delta - 9), "total": 65 * (delta - 8) + 520 * (delta - 9)}
            for delta in (10, 11, 12)
        },
        "full_source_BFS_performed": False,
        "new_graph_constructed": False,
        "cpu_seconds": time.process_time() - start,
    }
    (HERE / "RESULT.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: result[key] for key in (
        "degree_histogram", "radius_two_size_histogram_A", "radius_two_size_histogram_B",
        "radius_two_absolute_count_histogram_A", "radius_two_absolute_count_histogram_B",
        "known_twin_groups", "best_greedy_coverage_by_size", "cpu_seconds"
    )}, indent=2))


if __name__ == "__main__":
    main()
