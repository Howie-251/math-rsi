"""Short word/count arithmetic only; no generator-set or graph enumeration."""
import json
from collections import defaultdict
from math import comb
from pathlib import Path
from time import process_time

started = process_time()


def meeting(total, sizes, number):
    result = 0
    for bits in range(1 << len(sizes)):
        removed = sum(size for j, size in enumerate(sizes) if bits >> j & 1)
        result += (-1 if bits.bit_count() % 2 else 1) * comb(total - removed, number)
    return result


involutions = [14, 14, 42, 42]
pairs = [140, 287, 420, 420]
all_involution_hh = meeting(119, involutions, 6)
one_pair_hh_by_color = {}
for j, name in enumerate(["O7", "O14", "O21a", "O21b"]):
    one_pair_hh_by_color[name] = pairs[j] * meeting(119, involutions[:j] + involutions[j + 1:], 4)
one_pair_hh_by_color["zero"] = 17 * meeting(119, involutions, 4)
assert all_involution_hh == 689125416
assert list(one_pair_hh_by_color.values()) == [236834640, 485511012, 285238800, 285238800, 5877648]
assert sum(one_pair_hh_by_color.values()) == 1298700900

commuting_translation_bounds = []
for t in range(1, 7):
    r = 6 - t
    c2 = comb(t, 2) + 2 * t * r + r * (r - 1)
    c3 = comb(t, 3) + 2 * r * comb(t, 2) + r * t * t + 2 * t * r * (r - 1) + t * r * r + r * (r - 1) ** 2
    c = [1, 6, c2, c3]
    one_H = 2 * sum(c[i] * c[j] for i in range(4) for j in range(4 - i))
    commuting_translation_bounds.append({
        "pure_A_involutions": t,
        "reflection_involutions": r,
        "reduced_leaf_word_bounds_length0_to3": c,
        "one_H_capacity": one_H,
        "two_H_extra_capacity": 48,
        "K_capacity": 182,
        "nonzero_C3_layer_capacity_bound": one_H + 48 + 182,
    })

labels = (1, -1, 0, 0, 0, 0)
inverses = (1, 0, 2, 3, 4, 5)
states = {(0, -1): 1}
word_counts = []
for length in range(6):
    word_counts.append([sum(count for (residue, last), count in states.items() if residue == target) for target in range(3)])
    if length == 5:
        break
    following = defaultdict(int)
    for (residue, last), count in states.items():
        for letter, label in enumerate(labels):
            if last == -1 or letter != inverses[last]:
                following[((residue + label) % 3, letter)] += count
    states = following
result = {
    "status": "SMALL_CAPACITY_ARITHMETIC_COMPLETE_NO_CANDIDATE_SEARCH",
    "all_involution_raw_HH_sets": all_involution_hh,
    "one_pair_raw_HH_sets_by_pair_color": one_pair_hh_by_color,
    "one_pair_raw_HH_total": sum(one_pair_hh_by_color.values()),
    "nonzero_C3_layer_size": 896,
    "all_involution_translation_commutation_capacity_bounds": commuting_translation_bounds,
    "one_pair_nonzero_C3_projection_NB_words_by_length_and_residue": word_counts,
    "one_pair_nonzero_C3_projection_pure_leaf_word_bounds": [sum(row[j] for row in word_counts) for j in range(3)],
    "all_generators_K_part_in_H_other_block_layer_capacity": 78,
    "other_block_layer_size": 384,
    "cpu_seconds": process_time() - started,
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
