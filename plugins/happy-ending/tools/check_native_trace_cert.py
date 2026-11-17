#!/usr/bin/env python3
"""Cross-platform standard-library checker for self-contained native trace dual certificates.

Verifies `self-contained-native-trace-integer-v1` compact dual certificates (such as
`run-988-d2/compact-certificate.json` for N(9,8,8) <= 688 and `run-d9-d3/compact-certificate.json`
for junction-restricted D_9 <= 458) without SciPy or giant LP matrices, and optionally checks
an exact rational relaxation-ceiling witness (`--fractional-witness`) against all generated
native trace rows up to `--max-depth`.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools as it
import json
from pathlib import Path
import platform


PARAMETERS = {
    "d9": [5, 7, 9, True],
    "d8": [4, 6, 8, True],
    "988": [6, 6, 9, False],
    "988-native-v2": [6, 6, 9, False],
    "757": [3, 5, 7, False],
}


def enumerate_qp(a: int, b: int):
    for q in it.combinations_with_replacement(range(b, 0, -1), a - 1):
        choices = []
        for i in range(a - 1):
            prev_q = b if i == 0 else q[i - 1]
            opts = [q[i]]
            if q[i] + 1 <= prev_q:
                opts.append(q[i] + 1)
            choices.append(opts)
        for p in it.product(*choices):
            yield q, p


def build_trace_states(a: int, b: int, rem: list[int], inc: tuple[int, ...], p: list[int] | tuple[int, ...], q: list[int] | tuple[int, ...]) -> set[tuple[int, ...]]:
    assert len(p) == len(q) == a - 1
    s = tuple(v - 1 for v in p) + (0,)
    e = (b,) + tuple(q)
    cells = [(i, h) for i in range(a) for h in range(s[i] + 1, e[i] + 1)]
    assert all(any(j == i for j, _ in cells) for i in range(a))
    assert all(any(y == h for _, y in cells) for h in range(1, b + 1))
    assert all(h >= k for i, h in cells for j, k in cells if i < j)
    ideals = [e[:i] + s[i:] for i in range(a + 1)]
    ideals += [
        tuple(v + sum(j == i and h <= level for j, h in cells) for i, v in enumerate(s))
        for level in range(b + 1)
    ]
    original = set()
    for lam in ideals:
        assert all(0 <= v <= b for v in lam)
        assert all(lam[i] >= lam[i + 1] for i in range(a - 1))
        word = [v + i + 1 for i, v in enumerate(lam[::-1])]
        original.add(tuple(sorted(tuple(rem[v - 1] for v in word) + inc)))
    assert len(original) == a + b
    return original


def check_compact(path: Path) -> dict:
    raw = path.read_bytes()
    data = json.loads(raw)
    assert data["schema"] == "self-contained-native-trace-integer-v1"
    a0, b0, m, restricted = data["parameters"]
    assert data["parameters"] == PARAMETERS[data["case"]]
    assert type(restricted) is bool and 2 <= a0 <= 7 and 2 <= b0 <= 7
    n = a0 + b0
    states = [tuple(w) for w in data["states"]]
    expected_states = [
        w for w in it.combinations(range(1, n + 1), a0)
        if not restricted or n not in w or n - 1 in w
    ]
    assert states == expected_states
    state_set = set(states)
    loads = [0] * len(states)
    total = 0
    fixed_credit = 0
    depth_counts: dict[str, int] = {}

    for item in data["selected"]:
        weight, meta = item["weight"], item["metadata"]
        assert type(weight) is int and weight > 0
        inc, exc = tuple(meta["inc"]), tuple(meta["exc"])
        assert set(inc + exc) <= set(range(1, n + 1))
        assert len(set(inc + exc)) == len(inc + exc)
        a, b = a0 - len(inc), b0 - len(exc)
        assert (a, b) == (meta["a"], meta["b"]) and min(a, b) >= 2
        rem = [v for v in range(1, n + 1) if v not in inc + exc]
        original = build_trace_states(a, b, rem, inc, meta["p"], meta["q"])
        forbidden = len(original - state_set)
        assert forbidden == meta.get("fixed_forbidden", 0)
        assert item["rhs"] == a + b - m + 1 - forbidden > 0
        support = item["support"]
        assert len(support) == len(set(support))
        assert {states[v] for v in support} == (original & state_set)
        total += weight * item["rhs"]
        fixed_credit += weight * forbidden
        for v in support:
            loads[v] += weight
        d_key = str(len(inc + exc))
        depth_counts[d_key] = depth_counts.get(d_key, 0) + 1

    cap = data["exact"]["lambda"]
    assert type(cap) is int and cap > 0
    penalty = sum(max(0, v - cap) for v in loads)
    numerator = total - penalty
    exact = {
        "weighted_rhs": total,
        "lambda": cap,
        "overload_penalty": penalty,
        "numerator": numerator,
        "max_load": max(loads),
        "holes_lower_bound": (numerator + cap - 1) // cap,
        "nonzero_weights": len(data["selected"]),
    }
    assert exact == data["exact"] and loads == data["all_state_loads"]
    return {
        "status": "PASS",
        "platform": platform.platform(),
        "case": data["case"],
        "parameters": data["parameters"],
        "states": len(states),
        "exact": exact,
        "population_upper_bound": len(states) - exact["holes_lower_bound"],
        "selected_fixed_depths": depth_counts,
        "weighted_fixed_forbidden_credit": fixed_credit,
        "compact_sha256": hashlib.sha256(raw).hexdigest(),
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "original_rows_sha256": data["original_rows_sha256"],
    }


def check_fractional_ceiling(parameters: list, witness_path: Path, max_depth: int) -> dict:
    raw = witness_path.read_bytes()
    fg = json.loads(raw)
    scale = fg["scale"]
    values = fg["values"]
    assert type(scale) is int and scale > 0
    a0, b0, m, restricted = parameters
    n = a0 + b0
    states = [
        w for w in it.combinations(range(1, n + 1), a0)
        if not restricted or n not in w or n - 1 in w
    ]
    state_idx = {w: idx for idx, w in enumerate(states)}
    assert len(values) == len(states)
    assert all(type(v) is int and 0 <= v <= scale for v in values)

    distinct_rows: dict[tuple[int, ...], int] = {}
    for depth in range(max_depth + 1):
        for chosen in it.combinations(range(1, n + 1), depth):
            for r_inc in range(depth + 1):
                for inc in it.combinations(chosen, r_inc):
                    exc = tuple(v for v in chosen if v not in inc)
                    a, b = a0 - len(inc), b0 - len(exc)
                    if min(a, b) < 2:
                        continue
                    rem = [v for v in range(1, n + 1) if v not in chosen]
                    for q, p in enumerate_qp(a, b):
                        s = tuple(v - 1 for v in p) + (0,)
                        e = (b,) + tuple(q)
                        cells = [(i, h) for i in range(a) for h in range(s[i] + 1, e[i] + 1)]
                        ideals = [e[:i] + s[i:] for i in range(a + 1)] + [
                            tuple(v + sum(j == i and h <= level for j, h in cells) for i, v in enumerate(s))
                            for level in range(b + 1)
                        ]
                        original = {
                            tuple(sorted(tuple(rem[v - 1] for v in [vv + i + 1 for i, vv in enumerate(lam[::-1])]) + inc))
                            for lam in ideals
                        }
                        forbidden = sum(1 for w in original if w not in state_idx)
                        rhs = a + b - m + 1 - forbidden
                        if rhs <= 0:
                            continue
                        supp = tuple(sorted(state_idx[w] for w in original if w in state_idx))
                        if supp not in distinct_rows or rhs > distinct_rows[supp]:
                            distinct_rows[supp] = rhs

    min_slack = None
    for supp, rhs in distinct_rows.items():
        slack = sum(values[u] for u in supp) - rhs * scale
        assert slack >= 0, f"Row violated with slack {slack}"
        if min_slack is None or slack < min_slack:
            min_slack = slack

    total = sum(values)
    target = fg.get("integer_hole_target")
    if target is not None:
        assert total <= target * scale
    return {
        "status": "PASS",
        "max_depth": max_depth,
        "checked_distinct_rows": len(distinct_rows),
        "scale": scale,
        "integer_total": total,
        "integer_hole_target": target,
        "minimum_row_slack": min_slack,
        "witness_sha256": hashlib.sha256(raw).hexdigest(),
        "scope_note": "Feasible fractional LP hole vector certifying relaxation ceiling; not an integral state occupancy or point set.",
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", type=Path, required=True, help="Path to compact-certificate.json")
    ap.add_argument("--fractional-witness", type=Path, default=None, help="Optional fractional-grid.json")
    ap.add_argument("--max-depth", type=int, default=3, help="Max (inc+exc) depth for fractional witness check")
    ap.add_argument("--output", type=Path, default=None, help="Optional JSON receipt output path")
    args = ap.parse_args()

    result = check_compact(args.check)
    if args.fractional_witness is not None:
        result["fractional_ceiling"] = check_fractional_ceiling(
            result["parameters"], args.fractional_witness, args.max_depth
        )
        assert (
            result["fractional_ceiling"]["integer_hole_target"]
            == result["exact"]["holes_lower_bound"]
        ), "Relaxation ceiling target does not match dual holes lower bound"

    payload = json.dumps(result, indent=2, sort_keys=True)
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload + "\n", encoding="utf-8")
    print(json.dumps({
        "status": result["status"],
        "case": result["case"],
        "states": result["states"],
        "holes_lower_bound": result["exact"]["holes_lower_bound"],
        "population_upper_bound": result["population_upper_bound"],
        "fractional_ceiling_checked": "fractional_ceiling" in result,
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
