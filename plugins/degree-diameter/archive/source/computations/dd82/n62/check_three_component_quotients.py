"""Independently enumerate all positive-even three-component quotients.

The domain is nonnegative integer 3-by-3 R with row sums eight, trace
seven, and R^2 + R - 10I = 1 n^T, where every n_i is positive and even.
Balanced edge counts are also required. Component size two is allowed;
neither B <= 2 nor any D1 minimum-size bound is used.

This checks integer quotient possibilities only, not graph realizability.
The original minimum-four discovery script and its output are not changed.
"""

import itertools
import json
import os
from pathlib import Path
import time


ROOT = Path(__file__).resolve().parents[3]
REFERENCE = ROOT / "computations/dd82/n62/three_component_quotients.json"
OUTPUT = ROOT / "computations/dd82/n62/three_component_quotients_check.json"


def canonical_key(sizes, matrix):
    """Relabel sizes and both matrix axes by the same permutation."""
    return min(
        (
            tuple(sizes[i] for i in permutation),
            tuple(tuple(matrix[i][j] for j in permutation) for i in permutation),
        )
        for permutation in itertools.permutations(range(3))
    )


def enumerate_quotients():
    # Enumerate complete rows first, independently of the discovery script's
    # diagonal-first loops. Every nonnegative row summing to eight occurs once.
    rows = [(a, b, 8 - a - b) for a in range(9) for b in range(9 - a)]
    tested = 0
    raw_survivors = 0
    orbits = {}
    for matrix in itertools.product(rows, repeat=3):
        if sum(matrix[i][i] for i in range(3)) != 7:
            continue
        tested += 1
        q = tuple(
            tuple(
                sum(matrix[i][k] * matrix[k][j] for k in range(3))
                + matrix[i][j]
                - (10 if i == j else 0)
                for j in range(3)
            )
            for i in range(3)
        )
        if len(set(q)) != 1:
            continue
        sizes = q[0]
        if not all(size >= 2 and size % 2 == 0 for size in sizes):
            continue
        if not all(
            sizes[i] * matrix[i][j] == sizes[j] * matrix[j][i]
            for i in range(3)
            for j in range(3)
        ):
            continue
        # This follows from (R^2 + R - 10I)1 = (64 + 8 - 10)1.
        assert sum(sizes) == 62
        raw_survivors += 1
        key = canonical_key(sizes, matrix)
        orbits[key] = orbits.get(key, 0) + 1
    return len(rows), tested, raw_survivors, orbits


def main():
    os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
    start = time.monotonic()
    row_count, tested, raw_survivors, orbits = enumerate_quotients()

    reference = json.loads(REFERENCE.read_text())
    # D1 annotations are deliberately outside this check's mathematical core.
    reference_keys = {
        canonical_key(entry["sizes"], entry["R"])
        for entry in reference["canonical_quotients"]
    }
    assert len(reference_keys) == len(reference["canonical_quotients"])
    assert set(orbits) == reference_keys
    assert tested == reference["tested_matrices"] == 9108
    assert row_count == 45
    assert raw_survivors == 18
    assert len(orbits) == 3

    report = {
        "status": "VERIFIED_EXHAUSTIVE_INTEGER_QUOTIENT_CHECK",
        "minimum_component_size": 2,
        "candidate_rows": row_count,
        "row_triples_before_trace_filter": row_count ** 3,
        "tested_matrices": tested,
        "raw_survivors": raw_survivors,
        "canonical_count": len(orbits),
        "canonical_quotients": [
            {"sizes": sizes, "R": matrix, "labelled_count": count}
            for (sizes, matrix), count in sorted(orbits.items())
        ],
        "size_two_canonical_quotients": sum(
            2 in sizes for sizes, _matrix in orbits
        ),
        "matches_original_quotient_list": True,
        "reference_json": str(REFERENCE.relative_to(ROOT)),
        "D1_marks_checked": False,
        "cpu_count": len(os.sched_getaffinity(0)),
        "wall_seconds": time.monotonic() - start,
        "scope": (
            "All nonnegative integer 3x3 matrices with row sums 8, trace 7, "
            "R^2+R-10I having identical positive even rows, and balance. "
            "Component sizes 2 are included."
        ),
        "nonclaims": [
            "No retained quotient is asserted graph-realizable",
            "No B<=2 or D1 minimum-size assumption is used",
            "D1 annotations and actual-graph exclusions are outside this check",
            "Other numbers of repeat-support components are outside this check",
        ],
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
