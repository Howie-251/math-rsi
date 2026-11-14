"""Freeze the strong-column central basis and every common completion transport."""

from collections import Counter, defaultdict
from hashlib import sha256
import json
from pathlib import Path
from time import process_time

from E16_MU3_CENTRAL_LOCAL_HIGH_M_BASE import minority_sets
from R7_E16_MU3_CENTRAL_M3_BASE import physical_colors
from R7_E16_MU3_CENTRAL_S3_PREFLIGHT import move, root_stabilizer, verify_transport


SOURCE = Path(__file__).with_name("R7_E16_MU3_CENTRAL_S2_STRONG_PREFLIGHT.json")
SOURCE_SHA256 = "2755033cbc410a6fe5bbe9d043afe0cc5b4e06941a850275eb43f6c30c9ad2b8"
EXPECTED = 20_760
EXPECTED_LABELED = 23_949
CPU_LIMIT = 15
COMPUTE_LIMIT = 14


def run(start):
    raw = SOURCE.read_bytes()
    assert sha256(raw).hexdigest() == SOURCE_SHA256
    source = json.loads(raw)
    assert source["status"] == "complete" and source["template_count"] == len(source["rows"]) == 76
    assert source["totals"]["exact_U_on_source_reps"] == EXPECTED
    assert source["totals"]["exact_labeled_Y_U"] == EXPECTED_LABELED
    groups = {h: tuple(root_stabilizer(h)) for h in (2, 4)}
    records, transports, summaries = [], [], []
    counts_by_h = defaultdict(Counter)
    status = "complete"
    unfinished = None
    try:
        for ti, row in enumerate(source["rows"]):
            h, s, w = row["h"], tuple(row["S"]), tuple(row["W"])
            assert row["s"] == 2 and row["m"] in (1, 2) and 1 <= row["strong_columns"] <= row["m"]
            stabilizer = tuple((order, shift, action) for order, shift, action in groups[h]
                               if move(w, action) == w and move(s, action) == s)
            assert len(stabilizer) == row["receiver_stabilizer_size"]
            stats = Counter()
            summaries.append(dict(h=h, W=w, counts=stats))
            for yi, entry in enumerate(row["source_representatives"]):
                if process_time() - start >= COMPUTE_LIMIT:
                    unfinished = ti, yi
                    raise TimeoutError("central strong-column base CPU limit")
                expected = entry["exact_U"]
                if not expected:
                    continue
                y, pool = tuple(entry["Y"]), tuple(entry["U_pool"])
                allowed = tuple(map(tuple, entry["allowed_a"]))
                data = tuple(entry["b_loads"]), pool, allowed
                common = tuple((order, shift, action) for order, shift, action in stabilizer
                               if move(y, action) == y)
                assert common
                for order, shift, action in common:
                    verify_transport(data, data, order, shift, action)
                canonicals, generated = {}, 0
                for u in minority_sets(pool, tuple(map(set, allowed))):
                    generated += 1
                    assert generated <= expected
                    canonical, order, shift = min((move(u, action), order, shift) for order, shift, action in common)
                    if canonical not in canonicals:
                        assert canonical == u
                        even, odd = physical_colors(s, w, y, u)
                        assert len(set(even)) == len(set(odd)) == 8
                        assert all(v.bit_count() % 2 == parity for parity, points in enumerate((even, odd)) for v in points)
                        assert all((p ^ q).bit_count() != 1 for p in even for q in odd)
                        gaps = tuple(sum(v >> i & 1 for v in even) - sum(v >> i & 1 for v in odd) for i in range(7))
                        assert gaps[-1] == 3 and all(3 <= abs(g) <= 6 for g in gaps)
                        canonicals[canonical] = len(records)
                        records.append(dict(h=h, m=row["m"], s=2, strong_columns=row["strong_columns"],
                                            S=s, W=w, Y=y, U=u, template_index=ti, source_index=yi,
                                            common_stabilizer_size=len(common), signed_gaps=gaps))
                    transports.append(dict(representative=canonicals[canonical], U=u,
                                           axis_destination=order, xor_after_permutation=shift))
                assert generated == expected
                stats["completions"] += generated
                stats["labeled_Y_U"] += generated * entry["source_orbit_size"]
                stats["representatives"] += len(canonicals)
                stats["positive_sources"] += 1
            assert stats["completions"] == row["counts"]["exact_U_on_source_reps"]
            counts_by_h[h].update(stats)
    except TimeoutError:
        status = "stopped_cpu_limit"

    assert len(records) == len({(r["S"], r["W"], r["Y"], r["U"]) for r in records})
    labeled = sum(r["counts"]["labeled_Y_U"] for r in summaries)
    if status == "complete":
        assert len(transports) == EXPECTED and labeled == EXPECTED_LABELED
    return dict(status=status, source_sha256=SOURCE_SHA256, record_count=len(records), qualified_completions=len(transports),
                labeled_Y_U=labeled, summaries=summaries, counts_by_h=counts_by_h, first_unfinished_source=unfinished,
                records=records, completion_transports=transports, cpu_seconds=process_time() - start,
                cpu_limit_seconds=CPU_LIMIT, compute_cutoff_cpu_seconds=COMPUTE_LIMIT, plans=0,
                original_matchings_enumerated=0, solver_calls=0, rank_runs=0)


if __name__ == "__main__":
    result = run(process_time())
    with Path(__file__).with_suffix(".json").open("x", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(result, separators=(",", ":")) + "\n")
    print(json.dumps({key: value for key, value in result.items()
                      if key not in ("records", "completion_transports", "summaries")}))
