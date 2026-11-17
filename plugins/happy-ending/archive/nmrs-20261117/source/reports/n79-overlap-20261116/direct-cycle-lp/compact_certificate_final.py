#!/usr/bin/env python3
"""Pack and independently check a self-contained native trace certificate.

Linux scientific execution only; standard library, no optimizer needed.
"""
import argparse
import hashlib
import itertools as it
import json
from pathlib import Path
import platform


def pack(folder):
    raw = (folder / "rows.json").read_bytes()
    cert_raw = (folder / "certificate.json").read_bytes()
    data, cert = json.loads(raw), json.loads(cert_raw)
    generic = "parameters" in data
    exact = cert["exact"]
    compact = {"schema": "self-contained-native-trace-integer-v1",
               "parameters": data["parameters"] if generic else [6, 6, 9, False],
               "case": data.get("case", "988-native-v2"),
               "states": data["states"], "selected": [], "exact": exact,
               "all_state_loads": cert["all_state_loads"] if generic else exact["all_state_loads"],
               "original_rows_sha256": hashlib.sha256(raw).hexdigest(),
               "original_certificate_sha256": hashlib.sha256(cert_raw).hexdigest()}
    compact["exact"] = {k: v for k, v in exact.items() if k != "all_state_loads"}
    for rid, weight in cert["weights"]:
        meta = data["metadata"][rid]
        assert generic or meta["kind"] == "trace", "This packer only proves native trace rows"
        compact["selected"].append({"original_row_id": rid, "weight": weight,
                                    "support": data["rows"][rid], "rhs": data["rhs"][rid],
                                    "metadata": meta})
    output = folder / "compact-certificate.json"
    output.write_text(json.dumps(compact, separators=(",", ":")))
    return output


def check(path):
    raw = path.read_bytes()
    data = json.loads(raw)
    assert data["schema"] == "self-contained-native-trace-integer-v1"
    a0, b0, m, restricted = data["parameters"]
    parameters = {"d9": [5, 7, 9, True], "d8": [4, 6, 8, True],
                  "988": [6, 6, 9, False], "988-native-v2": [6, 6, 9, False],
                  "757": [3, 5, 7, False]}
    assert data["parameters"] == parameters[data["case"]]
    assert type(restricted) is bool and 2 <= a0 <= 7 and 2 <= b0 <= 7
    n = a0 + b0
    states = [tuple(w) for w in data["states"]]
    assert states == [w for w in it.combinations(range(1, n + 1), a0)
                      if not restricted or n not in w or n - 1 in w]
    state_set = set(states)
    loads, total, fixed_credit = [0] * len(states), 0, 0
    depth_counts = {}
    for item in data["selected"]:
        weight, meta = item["weight"], item["metadata"]
        assert type(weight) is int and weight > 0
        inc, exc = tuple(meta["inc"]), tuple(meta["exc"])
        assert set(inc + exc) <= set(range(1, n + 1))
        assert len(set(inc + exc)) == len(inc + exc)
        a, b = a0 - len(inc), b0 - len(exc)
        assert (a, b) == (meta["a"], meta["b"]) and min(a, b) >= 2
        rem = [v for v in range(1, n + 1) if v not in inc + exc]
        p, q = meta["p"], meta["q"]
        assert len(p) == len(q) == a - 1
        s, e = tuple(v - 1 for v in p) + (0,), (b,) + tuple(q)
        cells = [(i, h) for i in range(a) for h in range(s[i] + 1, e[i] + 1)]
        assert all(any(j == i for j, h in cells) for i in range(a))
        assert all(any(y == h for i, y in cells) for h in range(1, b + 1))
        assert all(h >= k for i, h in cells for j, k in cells if i < j)
        ideals = [e[:i] + s[i:] for i in range(a + 1)]
        ideals += [tuple(v + sum(j == i and h <= level for j, h in cells)
                         for i, v in enumerate(s)) for level in range(b + 1)]
        original = set()
        for lam in ideals:
            assert all(0 <= v <= b for v in lam)
            assert all(lam[i] >= lam[i + 1] for i in range(a - 1))
            word = [v + i + 1 for i, v in enumerate(lam[::-1])]
            original.add(tuple(sorted(tuple(rem[v - 1] for v in word) + inc)))
        assert len(original) == a + b
        forbidden = len(original - state_set)
        assert forbidden == meta.get("fixed_forbidden", 0)
        assert item["rhs"] == a + b - m + 1 - forbidden > 0
        support = item["support"]
        assert len(support) == len(set(support))
        assert {states[v] for v in support} == original & state_set
        total += weight * item["rhs"]
        fixed_credit += weight * forbidden
        for v in support:
            loads[v] += weight
        depth = len(inc + exc)
        depth_counts[depth] = depth_counts.get(depth, 0) + 1
    cap = data["exact"]["lambda"]
    assert type(cap) is int and cap > 0
    penalty = sum(max(0, v - cap) for v in loads)
    numerator = total - penalty
    exact = {"weighted_rhs": total, "lambda": cap, "overload_penalty": penalty,
             "numerator": numerator, "max_load": max(loads),
             "holes_lower_bound": (numerator + cap - 1) // cap,
             "nonzero_weights": len(data["selected"])}
    assert exact == data["exact"] and loads == data["all_state_loads"]
    result = {"status": "PASS", "case": data["case"], "states": len(states),
              "exact": exact, "population_upper_bound": len(states) - exact["holes_lower_bound"],
              "selected_fixed_depths": depth_counts, "weighted_fixed_forbidden_credit": fixed_credit,
              "compact_sha256": hashlib.sha256(raw).hexdigest(),
              "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "original_rows_sha256": data["original_rows_sha256"]}
    print(json.dumps(result, sort_keys=True), flush=True)


def main():
    assert platform.system() == "Linux", "Scientific execution must be on Linux"
    ap = argparse.ArgumentParser()
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument("--pack", type=Path)
    group.add_argument("--check", type=Path)
    args = ap.parse_args()
    check(pack(args.pack) if args.pack else args.check)


if __name__ == "__main__":
    main()
