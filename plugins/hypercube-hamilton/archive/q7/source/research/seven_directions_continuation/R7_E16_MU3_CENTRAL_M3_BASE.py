"""Materialize the counted central m=3 completions and quotient the last group."""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
from time import process_time

from E16_MU3_CENTRAL_LOCAL_HIGH_M_BASE import minority_sets
from R7_E16_MU3_CENTRAL_M3_SOURCE_PREFLIGHT import move, pre, root_stabilizer, verify_transport


SOURCE = Path(__file__).with_name("R7_E16_MU3_CENTRAL_M3_SOURCE_PREFLIGHT.json")
SOURCE_SHA256 = "3f5087ad8276fcac2c4d906ba72a64fc295c43edce1d046112bd1e112649c2ac"
EXPECTED = 50_859
CPU_LIMIT = 20


def physical_colors(s, w, y, u):
    return tuple(sorted((*u, *(p | 64 for p in w)))), tuple(sorted((*y, *(p | 64 for p in s))))


def run(start):
    def check_time():
        if process_time() - start >= CPU_LIMIT:
            raise TimeoutError("completion basis exceeded CPU limit")

    raw = SOURCE.read_bytes()
    assert sha256(raw).hexdigest() == SOURCE_SHA256
    data = json.loads(raw)
    assert data["status"] == "complete" and len(data["representatives"]) == 4163
    assert sum(r["U_coefficients"] for r in data["representatives"]) == EXPECTED
    groups = {h: tuple(root_stabilizer(h)) for h in (2, 4, 6)}
    records, transports = [], []
    raw_counts, counts, stabilizer_sizes, no_gap_six_counts = Counter(), Counter(), Counter(), Counter()
    status = "complete"
    source_index = None
    try:
        for entry in data["representatives"]:
            check_time()
            expected = entry["U_coefficients"]
            if not expected:
                continue
            source_index = entry["source_index"]
            row = dict(data["sources"][source_index])
            for field in ("S", "W", "Y", "U_pool_raw", "U_pool", "b_loads"):
                row[field] = tuple(row[field])
            for field in ("allowed_a", "allowed_a_no_gap_six"):
                row[field] = tuple(map(tuple, row[field]))
            assert row["representative_index"] == source_index
            h = row["h"]
            s, w, y = (tuple(row[key]) for key in ("S", "W", "Y"))
            allowed = tuple(set(values) for values in row["allowed_a"])
            allowed5 = tuple(set(values) for values in row["allowed_a_no_gap_six"])
            stabilizer = tuple((order, shift, action) for order, shift, action in groups[h]
                               if move(w, action) == w and move(y, action) == y)
            assert stabilizer
            for order, shift, action in stabilizer:
                verify_transport(row, row, order, shift, action)
            stabilizer_sizes[len(stabilizer)] += 1
            canonicals = {}
            generated = no_gap_six = 0
            for u in minority_sets(row["U_pool"], allowed):
                check_time()
                assert len(transports) < EXPECTED and generated < expected
                generated += 1
                a = tuple(sum(bool(p & bit) for p in u) for bit in pre.AXES)
                gap5 = all(load in values for load, values in zip(a, allowed5))
                no_gap_six += gap5
                canonical, order, shift, action = min((move(u, action), order, shift, action)
                                                      for order, shift, action in stabilizer)
                if canonical not in canonicals:
                    colors = physical_colors(s, w, y, canonical)
                    gaps = tuple(sum((p >> i) & 1 for p in colors[0]) - sum((p >> i) & 1 for p in colors[1])
                                 for i in range(7))
                    assert gaps[6] == 3 and all(3 <= abs(gap) <= 6 for gap in gaps)
                    assert gap5 == (max(map(abs, gaps)) <= 5)
                    assert all(len(set(group)) == 8 and all(p.bit_count() % 2 == parity for p in group)
                               for parity, group in enumerate(colors))
                    assert all((p ^ q).bit_count() != 1 for p in colors[0] for q in colors[1])
                    canonicals[canonical] = len(records)
                    records.append(dict(source_index=source_index, h=h, S=s, W=w, Y=y, U=canonical,
                                        signed_gaps=gaps))
                    no_gap_six_counts[h] += gap5
                transports.append(dict(source_index=source_index, U=u, representative=canonicals[canonical],
                                       axis_destination=order, xor_after_permutation=shift))
            assert generated == expected and no_gap_six == entry["U_coefficients_no_gap_six"]
            raw_counts[h] += generated
            counts[h] += len(canonicals)
        check_time()
        assert len(transports) == EXPECTED
    except TimeoutError:
        status = "cpu_limit"
    return dict(status=status, source_sha256=SOURCE_SHA256, qualified_completions=len(transports),
                expected_completions=EXPECTED, record_count=len(records), raw_counts_by_h=raw_counts,
                counts_by_h=counts, no_gap_six_by_h=no_gap_six_counts, stabilizer_sizes=stabilizer_sizes,
                first_unfinished_source=source_index if status != "complete" else None,
                records=records, completion_transports=transports, cpu_seconds=process_time()-start,
                cpu_limit_seconds=CPU_LIMIT, plan_searches=0, original_matchings_enumerated=0,
                solver_calls=0, rank_runs=0)


if __name__ == "__main__":
    result = run(process_time())
    with Path(__file__).with_suffix(".json").open("x", encoding="utf-8", newline="\n") as file:
        json.dump(result, file, separators=(",", ":"))
        file.write("\n")
    print(json.dumps({key: value for key, value in result.items()
                      if key not in ("records", "completion_transports")}, indent=2))
