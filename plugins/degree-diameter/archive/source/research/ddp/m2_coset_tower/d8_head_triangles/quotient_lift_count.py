"""Count actual normalized inputs passing the saved quotient filter; no BB/BFS evaluation."""
import json
from collections import Counter
from pathlib import Path
from time import process_time

started = process_time()
HERE = Path(__file__).parent
check = json.loads((HERE / "QUOTIENT_BB_CHECK.json").read_text())
internal = json.loads((HERE / "internal_options.json").read_text())
metadata = json.loads((HERE / "profile_metadata.json").read_text())
assert list(map(len, internal)) == [5166, 5166, 630, 5166, 252]
assert sum(map(len, internal)) == 16380


def qenc(v, w, j):
    return v % 7 + 7 * (w % 3) + 21 * (j % 6)


def qinv(g):
    v, w, j = g % 7, g // 7 % 3, g // 21
    return qenc(-pow(3, (-j) % 6, 7) * v, -w, -j)


def project(g):
    x, k = g % 147, g // 147
    return qenc(x // 7 % 7, x // 49, k // 7)


allowed = sorted({tuple(sorted(qenc(*coordinate) for coordinate in row))
                  for row in check["allowed_projected_generator_sets"]})
assert len(allowed) == 16
lookup = {row: index for index, row in enumerate(allowed)}
cross = []
for ja in range(6):
    for jb in range(6):
        a, b = qenc(0, 1, ja), qenc(1, 1, jb)
        cross.append((ja, jb, {a, qinv(a), b, qinv(b)}))

completed = 0
matches = []
branches = []
all_internal = set()
per_allowed = Counter()
for branch_id, options in enumerate(internal):
    passed = 0
    cross_counts = Counter()
    for internal_index, generators in enumerate(options):
        actual_key = tuple(sorted(generators))
        assert len(set(generators)) == 3 and actual_key not in all_internal
        assert all(g % 147 // 49 == 0 for g in generators)
        all_internal.add(actual_key)
        projected = {project(g) for g in generators}
        for ja, jb, cross_set in cross:
            completed += 1
            key = tuple(sorted(projected | cross_set))
            if key in lookup:
                allowed_id = lookup[key]
                passed += 1
                cross_counts[f"{ja},{jb}"] += 1
                per_allowed[allowed_id] += 1
                matches.append({"branch": branch_id, "internal_index": internal_index,
                                "cross_a_index": ja, "cross_b_index": jb,
                                "allowed_projected_S_id": allowed_id})
    branches.append({"branch": branch_id, "name": metadata["branches"][branch_id]["name"],
                     "internal_options": len(options), "completed_quotient_keys": len(options) * 36,
                     "passing_quotient_keys": passed, "cross_b_choices_per_key": 49,
                     "passing_full_normalized_inputs": passed * 49,
                     "passing_keys_by_cross_indices": dict(sorted(cross_counts.items()))})

assert completed == 589680 and len(all_internal) == 16380
result = {
    "status": "COMPLETE_ACTUAL_INPUT_LIFT_COUNT_ONLY",
    "Q_encoding": "v+7*w+21*j; v in 0..6, w in 0..2, j in 0..5",
    "original_group_encoding": "u+7*v+49*w+147*(b+7*j)",
    "allowed_unique_projected_S": allowed,
    "allowed_unique_projected_S_count": len(allowed),
    "canonical_key": "sort the distinct Q codes of the seven projected original generators",
    "source_internal_options": "internal_options.json",
    "source_internal_options_count": len(all_internal),
    "completed_quotient_keys": completed,
    "passing_quotient_keys": len(matches),
    "cross_b_choices_per_key": 49,
    "passing_full_normalized_inputs": len(matches) * 49,
    "full_normalized_inputs_before_filter": 28894320,
    "branches": branches,
    "passing_keys_by_allowed_projected_S_id": dict(sorted(per_allowed.items())),
    "passing_key_file": "quotient_lift_allowed_keys.jsonl",
    "full_BB_evaluations": 0,
    "full_tower_graphs_generated": 0,
    "full_tower_BFS_runs": 0,
    "cpu_seconds": process_time() - started,
}
(HERE / "QUOTIENT_BB_ALLOWED.json").write_text(json.dumps(result, indent=2) + "\n")
(HERE / "quotient_lift_allowed_keys.jsonl").write_text("".join(json.dumps(row) + "\n" for row in matches))
print(json.dumps({key: value for key, value in result.items()
                  if key not in ("allowed_unique_projected_S", "passing_keys_by_allowed_projected_S_id")}, indent=2))
