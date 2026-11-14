"""Count scalar column loads after the E16 |delta| and controlled-C gates."""

from collections import Counter
from itertools import product
import json


def controlled(source_total, source, receiver_major, receiver_minor, minor):
    """A split 1+2 with enough sources and minority <= 1 on the 2-side."""
    for sources, majority, minority in (
        (source, receiver_major, receiver_minor),
        (source_total - source, minor + 3 - receiver_major, minor - receiver_minor),
    ):
        gap = majority - minority
        if gap not in (1, 2) or sources < gap or (gap == 2 and minority > 1):
            return False
    return True


def remaining_columns(r, s):
    """Yield the oriented bit-one loads (A_alpha, A_beta, B_alpha, B_beta)."""
    totals = (r, r + 3, s + 3, s)
    for a, b, c, d in product(*(range(total + 1) for total in totals)):
        if abs(a + c - b - d) < 3:
            continue
        if controlled(r + 3, b, c, d, s) or controlled(s + 3, c, b, a, r):
            continue
        yield a, b, c, d


def summarize(r, s):
    totals = (r, r + 3, s + 3, s)
    raw = absolute_gate = forward = reverse = both = 0
    for a, b, c, d in product(*(range(total + 1) for total in totals)):
        raw += 1
        if abs(a + c - b - d) < 3:
            continue
        absolute_gate += 1
        a_to_b = controlled(r + 3, b, c, d, s)
        b_to_a = controlled(s + 3, c, b, a, r)
        forward += a_to_b
        reverse += b_to_a
        both += a_to_b and b_to_a

    rows = list(remaining_columns(r, s))
    positive = [row for row in rows if row[0] + row[2] - row[1] - row[3] >= 3]
    assert len(rows) == absolute_gate - forward - reverse + both
    assert set(rows) == {tuple(t - x for t, x in zip(totals, row)) for row in rows}
    assert 2 * len(positive) == len(rows)
    projections = {}
    for name, indices in (
        ("A", (0, 1)),
        ("B", (2, 3)),
        ("minority", (0, 3)),
        ("majority", (1, 2)),
    ):
        projection = sorted({tuple(row[i] for i in indices) for row in positive})
        projections[name] = {"size": len(projection), "loads": projection}
    return {
        "totals": totals,
        "raw_rows": raw,
        "absolute_gate": absolute_gate,
        "controlled_A_to_B": forward,
        "controlled_B_to_A": reverse,
        "controlled_overlap": both,
        "remaining": len(rows),
        "positive_gap_counts": dict(sorted(Counter(a + c - b - d for a, b, c, d in positive).items())),
        "positive_load_values": [sorted({row[i] for row in positive}) for i in range(4)],
        "positive_projections": projections,
    }


if __name__ == "__main__":
    print(json.dumps([summarize(4, 1), summarize(3, 2)], separators=(",", ":")))
