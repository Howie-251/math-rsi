"""Apply both outer-coordinate orientations to the frozen scalar alphabet."""

from collections import Counter
import json

from E16_MU3_ROUTE_SCALAR import remaining_columns


def transposed_hits(r, s, row):
    a, b, c, d = row
    bit_one = ((a, b), (c, d))
    bit_zero = ((r - a, r + 3 - b), (s + 3 - c, s - d))
    hits = set()
    for donor, receiver in ((bit_one, bit_zero), (bit_zero, bit_one)):
        donor_counts = tuple(map(sum, zip(*donor)))
        beta = int(donor_counts[1] > donor_counts[0])
        alpha = 1 - beta
        donor_minority = donor_counts[alpha]
        gap = donor_counts[beta] - donor_minority
        receiver_minority = sum(block[beta] for block in receiver)
        if gap == 3 and donor_minority == 5 and receiver_minority == 0:
            hits.add("E16_mono_three")
        if donor_minority <= 5 and all(
            (q := recv[alpha] - recv[beta]) in (1, 2)
            and send[beta] >= q
            and (q == 1 or recv[beta] <= 1)
            for send, recv in zip(donor, receiver)
        ):
            hits.add("controlled_count")
    return hits


def summarize(r, s):
    totals = (r, r + 3, s + 3, s)
    rows = list(remaining_columns(r, s))
    hits = Counter()
    residual = []
    for row in rows:
        reasons = transposed_hits(r, s, row)
        if reasons:
            hits.update(reasons)
        else:
            residual.append(row)
    positive = [row for row in residual if row[0] + row[2] - row[1] - row[3] >= 3]
    assert set(residual) == {tuple(t - x for t, x in zip(totals, row)) for row in residual}
    projections = {
        name: sorted({(row[i], row[j]) for row in positive})
        for name, (i, j) in {
            "A": (0, 1),
            "B": (2, 3),
            "minority": (0, 3),
            "majority": (1, 2),
        }.items()
    }
    return {
        "totals": totals,
        "before_transpose": len(rows),
        "hits": dict(hits),
        "removed": len(rows) - len(residual),
        "remaining": len(residual),
        "positive_gap_counts": dict(sorted(Counter(a + c - b - d for a, b, c, d in positive).items())),
        "positive_projections": projections,
    }


if __name__ == "__main__":
    print(json.dumps([summarize(4, 1), summarize(3, 2)], separators=(",", ":")))
