"""Enumerate HH color-count cells and coarse short-word capacities, not generating sets."""
import json
import math
from collections import Counter
from pathlib import Path
from time import process_time

started = process_time()
HERE = Path(__file__).parent


def compositions3(n):
    for z in range(n + 1):
        for a in range(n - z + 1):
            yield (z, a, n - z - a)


cells = []
summary = []
for t in (2, 3, 4):
    internal_size = 11 - 2 * t
    cross_colors = [(z, a, b) for z, a, b in compositions3(t) if a >= 1 and b >= 1]
    count = 0
    component_patterns = []
    for p in range(internal_size // 2 + 1):
        i = internal_size - 2 * p
        allocations = []
        for pc in compositions3(p):
            for ic in compositions3(i):
                if ic[0] > 1 or pc[1] + ic[1] == 0 or pc[2] + ic[2] == 0:
                    continue
                allocations.append((pc, ic))
        expected = math.comb(p + 2, 2) * (2 * i + 1) - 4 * (p + 1) + (i == 1)
        assert len(allocations) == expected
        component_patterns.append({"internal_pairs": p, "internal_involutions": i,
                                   "legal_internal_color_allocations": len(allocations),
                                   "sample_cells": len(cross_colors) * len(allocations)})
        for cc in cross_colors:
            for pc, ic in allocations:
                cells.append({"cell_id": len(cells), "cross_inverse_pairs": t,
                              "cross_colors_zero_axis_offaxis": cc,
                              "extra_cross_colors_after_anchors": (cc[0], cc[1] - 1, cc[2] - 1),
                              "internal_pairs": p, "internal_involutions": i,
                              "internal_pair_colors_zero_axis_offaxis": pc,
                              "internal_involution_colors_zero_axis_offaxis": ic,
                              "planned_representatives": 1})
                count += 1
    summary.append({"cross_inverse_pairs": t, "internal_elements": internal_size,
                    "cross_color_allocations": len(cross_colors),
                    "internal_patterns": component_patterns, "sample_cells": count})
assert [s["sample_cells"] for s in summary] == [81, 81, 30]
assert len(cells) == 192


def word_counts(t):
    # 2t cross letters are paired inverses. Internal letters are taken as
    # involutions here: the aggregate w counts are independent of their inverse pairing.
    labels = [value for _ in range(t) for value in (1, 2)] + [0] * (11 - 2 * t)
    inv = [j ^ 1 for j in range(2 * t)] + list(range(2 * t, 11))
    states = {(labels[j], j): 1 for j in range(11)}
    by_length = [[1, 0, 0]]
    for length in range(1, 6):
        counts = [0, 0, 0]
        for (w, _), count in states.items():
            counts[w] += count
        by_length.append(counts)
        assert sum(counts) == 11 * 10 ** (length - 1)
        next_states = Counter()
        if length < 5:
            for (w, last), count in states.items():
                for letter, value in enumerate(labels):
                    if letter != inv[last]:
                        next_states[((w + value) % 3, letter)] += count
        states = next_states
    w3 = [sum(row[w] for row in by_length[:4]) for w in range(3)]
    w5 = [sum(row[w] for row in by_length) for w in range(3)]
    m = 11 - 2 * t
    bb_raw_upper = [w3[0] + 20 * (m + 1), w3[1] + 20 * t + 10, w3[2] + 20 * t + 10]
    assert min(bb_raw_upper) > 110 and min(w5) > 13310
    return {"cross_inverse_pairs": t, "nonbacktracking_words_by_length_and_w": by_length,
            "W3_word_count_upper_by_w": w3,
            "quotient_BB_coarse_uncapped_upper_by_w": bb_raw_upper,
            "quotient_targets_per_w": 110,
            "W5_word_count_upper_by_w": w5, "original_leaf_targets_per_w": 13310}


output = {
    "status": "COMPLETE_PROFILE_DESIGN_SMALL_TABLE_ONLY",
    "q": 11, "r": 3, "c": 2, "degree": 12, "n": 43923,
    "HH_color_cell_count": len(cells),
    "planned_representatives_per_cell": 1,
    "planned_total_representatives_if_authorized": 192,
    "summary_by_t": summary,
    "cells": cells,
    "coarse_capacities": [word_counts(t) for t in (2, 3, 4)],
    "BB_index_mask_count": 10,
    "quotient_points_per_mask": 33,
    "original_points_per_mask": 363,
    "remaining_axis_block_targets_after_quotient_pass": 330,
    "actual_generator_sets_sampled": 0,
    "graphs_generated": 0,
    "BFS_runs": 0,
    "cpu_seconds": process_time() - started,
}
(HERE / "HEAD_TRIANGLE_Q11_PROFILE_DESIGN.json").write_text(json.dumps(output, indent=2) + "\n")
print(json.dumps({k: v for k, v in output.items() if k != "cells"}, indent=2))
