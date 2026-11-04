"""Independent exhaustive audit of the Q5 degree-completion Hall bound.

Uses Gray-code updates of odd neighborhood degrees, rather than the main
checker's subset-by-subset incidence construction. Standard library only.
"""
import hashlib
import json
from pathlib import Path


def run():
    evens = [x for x in range(32) if x.bit_count() % 2 == 0]
    odds = [x for x in range(32) if x.bit_count() % 2 == 1]
    odd_index = {x: j for j, x in enumerate(odds)}
    adj = [[odd_index[x ^ (1 << d)] for d in range(5)] for x in evens]
    degree = [0] * 16
    owners_xor = [0] * 16  # XOR of original vertex labels of selected neighbors
    minima = [999] * 17
    witnesses = [None] * 17
    histogram = {}
    previous = 0
    negative = 0
    for counter in range(1 << 16):
        selected = counter ^ (counter >> 1)
        if counter:
            changed = selected ^ previous
            i = changed.bit_length() - 1
            delta = 1 if selected & changed else -1
            for j in adj[i]:
                degree[j] += delta
                owners_xor[j] ^= evens[i]
        previous = selected
        k = selected.bit_count()
        n = sum(d != 0 for d in degree)
        leaf_owners = {owners_xor[j] for j, d in enumerate(degree) if d == 1}
        leaf_owners.discard(0)
        r = len(leaf_owners)
        slack = 0 if not k else n - 1 + max(0, n - 14) - r - k - bool(selected & 1)
        negative += slack < 0
        if slack < minima[k]:
            minima[k] = slack
            witnesses[k] = {
                "S": [evens[i] for i in range(16) if selected >> i & 1],
                "N": n, "R_all": r, "slack": slack,
            }
        histogram[slack] = histogram.get(slack, 0) + 1
    expected = [0, 2, 3, 3, 2, 2, 1, 1, 1, 3, 4, 3, 3, 3, 2, 1, 0]
    assert minima == expected, (minima, expected)
    assert negative == 0
    assert sum(histogram.values()) == 65536
    return {
        "method": "Gray-code degree updates; original vertex XOR unique-owner tracking",
        "subsets_tested": 65536,
        "nonempty_subsets_tested": 65535,
        "negative_bounds": negative,
        "minimum_slack_by_subset_size": minima,
        "slack_histogram": histogram,
        "minimizing_witness_by_subset_size": witnesses,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


if __name__ == "__main__":
    result = run()
    output = Path(__file__).with_name("a4_factor_gray_audit_results.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if not k.startswith("minimizing")}))
