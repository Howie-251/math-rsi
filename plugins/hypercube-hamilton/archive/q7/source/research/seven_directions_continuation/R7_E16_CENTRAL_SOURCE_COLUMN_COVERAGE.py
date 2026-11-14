"""Check count-only whole-cut gates on the frozen complete 222/224 source rows."""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
from time import process_time


HERE = Path(__file__).resolve().parent
SOURCE = "R7_E16_CENTRAL_TWO_ROOT_SOURCE_PROBE.json"
SOURCE_HASH = "14646c2424b1580a0df9ae2e626219cba4d0d868050502f5995fdbeefcd9875a"
EXPECTED = {"222": (245, 1117), "224": (170, 843)}
CPU_LIMIT = 5
BITS = (1, 2, 4, 8, 16, 32)
EVENS = frozenset(v for v in range(64) if v.bit_count() % 2 == 0)
ODDS = frozenset(range(64)) - EVENS
GATES = {
    (3, 3): "B",
    (4, 4): "B",
    (2, 3): "D",
    (6, 8): "delta2_2hole",
    (5, 7): "delta2_edge",
    (4, 6): "delta2_middle",
    (5, 8): "mono3",
}


def gate(e, o):
    for pair in ((e, o), (o, e), (8 - e, 8 - o), (8 - o, 8 - e)):
        if pair in GATES:
            return GATES[pair]
    return None


def columns(S, T, Y, pool):
    for bit_index, bit in enumerate(BITS):
        e = sum(bool(v & bit) for v in S | Y)
        t = sum(bool(v & bit) for v in T)
        pool1 = sum(bool(v & bit) for v in pool)
        pool0 = len(pool) - pool1
        low, high = max(0, 3 - pool0), min(3, pool1)
        assert low <= high
        yield dict(bit=bit_index, e=e, t=t, pool0=pool0, pool1=pool1,
                   u_min=low, u_max=high, gates=[gate(e, t + u) for u in range(low, high + 1)])


def run():
    start = process_time()
    input_bytes = (HERE / SOURCE).read_bytes()
    assert sha256(input_bytes).hexdigest() == SOURCE_HASH
    source = json.loads(input_bytes)
    assert source["conditional_on_new_two_root_lemma"]
    summaries = {}
    first_residual = None
    certificates = []
    for kind, (expected_rows, expected_reps) in EXPECTED.items():
        rows = [row for row in source["rows"] if row["distance_type"] == kind]
        assert [row["local_index"] for row in rows] == list(range(expected_rows))
        counts = Counter({"source_representatives": 0, "pool_lt_3": 0,
                          "column_closed": 0, "residual": 0})
        for row in rows:
            assert row["status"] == "completed"
            S, T = map(frozenset, (row["S"], row["T"]))
            assert len(S) == 3 and S <= EVENS and len(T) == 5 and T <= ODDS
            assert all((s ^ t).bit_count() != 1 for s in S for t in T)
            seen = set()
            reps = sorted(row["representatives"], key=lambda rep: rep["Y"])
            for rep in reps:
                if process_time() - start >= CPU_LIMIT:
                    raise TimeoutError("source column coverage exceeded CPU budget")
                Y = frozenset(rep["Y"])
                assert len(Y) == 5 and Y <= ODDS and not (T & Y) and Y not in seen
                seen.add(Y)
                pool = EVENS - S - {y ^ bit for y in Y for bit in BITS}
                record = dict(distance_type=kind, local_index=row["local_index"],
                              Y=rep["Y"], pool_size=len(pool))
                if len(pool) < 3:
                    result = "pool_lt_3"
                else:
                    profiles = list(columns(S, T, Y, pool))
                    winner = next((col for col in profiles if all(col["gates"])), None)
                    if winner is not None:
                        result = "column_closed"
                        record["witness"] = winner
                    else:
                        result = "residual"
                        if first_residual is None:
                            first_residual = dict(**record, S=row["S"], T=row["T"],
                                                  pool=sorted(pool), columns=profiles)
                record["result"] = result
                certificates.append(record)
                counts["source_representatives"] += 1
                counts[result] += 1
        assert counts["source_representatives"] == expected_reps
        summaries[kind] = counts
    elapsed = process_time() - start
    if elapsed >= CPU_LIMIT:
        raise TimeoutError("source column coverage exceeded CPU budget")
    return dict(status="complete", source=SOURCE, source_sha256=SOURCE_HASH,
                conditional_on_two_root_source_reduction=True, cpu_seconds=elapsed,
                cpu_limit_seconds=CPU_LIMIT, summaries=summaries,
                first_residual=first_residual, certificates=certificates,
                opposite_minority_completions=0, original_matching_enumerations=0)


if __name__ == "__main__":
    result = run()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "certificates"}, indent=2))
