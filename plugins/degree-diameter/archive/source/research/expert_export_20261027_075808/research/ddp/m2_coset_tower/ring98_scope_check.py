"""Tiny arithmetic check for RING98_SCOPE; does not enumerate graph candidates."""
import json
from collections import Counter, defaultdict
from math import gcd
from pathlib import Path
from time import process_time

start = process_time()
q, k = 98, 42
powers = [pow(3, i, q) for i in range(k)]
assert len(set(powers)) == 42 and pow(3, 42, q) == 1


def inverse(g):
    x, i = g
    return (-pow(3, (-i) % k, q) * x % q, (-i) % k)


involutions = []
pair_classes = Counter()
for x in range(q):
    for i in range(k):
        g = x, i
        if g == (0, 0):
            continue
        gi = inverse(g)
        assert inverse(gi) == g
        if gi == g:
            involutions.append(g)
        elif g < gi:
            pair_classes[gcd(x, q)] += 1

assert set(involutions) == {(x, 21) for x in range(98)} | {(49, 0)}
assert pair_classes == {1: 861, 2: 861, 7: 123, 14: 123, 49: 20, 98: 20}
orbit_sizes = {d: sum(gcd(x, q) == d for x in range(1, q)) for d in (1, 2, 7, 14, 49)}
assert orbit_sizes == {1: 42, 2: 42, 7: 6, 14: 6, 49: 1}
normalization_counts = {
    "pair_gcd1": 41 * 42 * 6 * 6 * 2,
    "pair_gcd2": pair_classes[2] * 6 * 6 * 2,
    "pair_gcd7": pair_classes[7] * 42 * 6 * 2,
    "pair_gcd14": pair_classes[14] * 42 * 6 * 2,
    "pair_gcd49": pair_classes[49] * 42 * 6 * 6,
}
assert sum(normalization_counts.values()) == 340200

labels = (1, -1, 0, 0, 0, 0)
letter_inverse = (1, 0, 2, 3, 4, 5)
states = {(0, -1): 1}
counts = []
for length in range(6):
    counts.append(sum(n for (r, last), n in states.items() if r == 3))
    if length == 5:
        break
    following = defaultdict(int)
    for (r, last), n in states.items():
        for j, t in enumerate(labels):
            if last < 0 or j != letter_inverse[last]:
                following[((r + t) % 7, j)] += n
    states = following
assert counts == [0, 0, 0, 1, 17, 164]
route_capacities = {"pure_S": sum(counts), "one_H": 4 * 5, "two_H": 0, "one_K": 6 + 6 * 6 + 6 * 6}
assert sum(route_capacities.values()) == 280 < 98 * 6

result = {
    "status": "ARITHMETIC_CHECK_COMPLETE_NO_GRAPH_SEARCH",
    "q": q, "quotient_order": k, "r": 3,
    "selected_powers": {i: pow(3, i, q) for i in (6, 7, 14, 21, 42)},
    "nonzero_gcd_orbit_sizes": orbit_sizes,
    "involution_count": len(involutions),
    "inverse_pairs_by_gcd_zero_is_98": dict(sorted(pair_classes.items())),
    "normalized_inputs_not_executed": normalization_counts,
    "normalized_total_not_executed": sum(normalization_counts.values()),
    "index3_nonbacktracking_word_counts_length0_to5": counts,
    "index3_route_upper_bounds": route_capacities,
    "index3_total_upper_bound": sum(route_capacities.values()),
    "target_layer_size": 98 * 6,
    "zero_index_generators_other_layer_upper_bound": 78,
    "cpu_seconds": process_time() - start,
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
