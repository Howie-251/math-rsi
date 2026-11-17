"""Verify the odd covered-vertex class in every residual Q6 A8 orbit."""

from collections import defaultdict
from itertools import combinations
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def certificate(geometry):
    minority = set(geometry["minority"])
    majority = {0, *geometry["other_majority"]}
    covered = set(range(64)) - minority - majority
    axes = geometry["delta_0_k_2_axes"]
    mirrors = {}
    for axis in axes:
        bit = 1 << axis
        minority_in_a = {hole for hole in minority if not hole & bit}
        majority_in_a = {hole for hole in majority if not hole & bit}
        assert len(minority_in_a) == len(majority_in_a) == 2
        mirrors[axis] = {hole ^ bit for hole in minority_in_a}
        assert mirrors[axis] <= covered

    def signature(vertex):
        return tuple(
            axis for axis in axes
            if vertex & (1 << axis) and vertex not in mirrors[axis]
        )

    def passes_edge_restriction(u, v, axis):
        bit = 1 << axis
        w = mirrors[axis]
        if (u ^ v) & bit:
            return (u if u & bit else v) in w
        if u & bit:
            return (u in w) == (v in w)
        return True

    buckets = defaultdict(list)
    for vertex in sorted(covered):
        buckets[signature(vertex)].append(vertex)
    bucket_sizes = sorted(map(len, buckets.values()))
    assert sum(bucket_sizes) == 56
    odd_signature, odd_bucket = min(
        ((key, bucket) for key, bucket in buckets.items() if len(bucket) % 2),
        key=lambda item: (len(item[1]), item[1]),
    )
    for u, v in combinations(sorted(covered), 2):
        assert (signature(u) == signature(v)) == all(
            passes_edge_restriction(u, v, axis) for axis in axes
        )
    return {
        "minority": geometry["minority"],
        "other_majority": geometry["other_majority"],
        "mirrors_by_axis": {
            axis: sorted(vertices) for axis, vertices in mirrors.items()
        },
        "clique_sizes": bucket_sizes,
        "maximum_matching_size": sum(size // 2 for size in bucket_sizes),
        "odd_signature": odd_signature,
        "odd_covered_vertices": odd_bucket,
    }


if __name__ == "__main__":
    report = json.loads((HERE / "geometry.json").read_text(encoding="utf-8-sig"))
    assert report["residual_list_complete"]
    residual = report["residual_geometries"]
    assert len(residual) == report["domains"]["after_all_gates"]["full_s6_orbits"]
    print(json.dumps([certificate(geometry) for geometry in residual],
                     separators=(",", ":"), sort_keys=True))
