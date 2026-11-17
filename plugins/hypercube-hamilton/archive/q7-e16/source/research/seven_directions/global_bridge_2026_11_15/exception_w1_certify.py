"""Check the frozen seven-axis menu on the sorted-load W1 exception."""

from collections import Counter
import json
from hashlib import sha256
from time import process_time

from exception_preflight import AXES, HERE, column_load, donor_pool, load_inputs, sources


CPU_LIMIT = 60
COMPLETION_LIMIT = 5000
AXES7 = tuple(range(7))


def timer(started):
    if process_time() - started >= CPU_LIMIT:
        raise TimeoutError("CPU cap reached")


def completions(pool, permitted, started):
    """Yield exactly the degree-three terms permitted by all six columns."""
    suffix = [column_load(pool[i:]) for i in range(len(pool) + 1)]

    def visit(start, chosen, loads):
        timer(started)
        need = 3 - len(chosen)
        remaining = len(pool) - start
        if remaining < need:
            return
        for have, ones, valid in zip(loads, suffix[start], permitted):
            low = have + max(0, need - (remaining - ones))
            high = have + min(need, ones)
            if not any(low <= a <= high for a in valid):
                return
        if need == 0:
            yield chosen, loads
            return
        for i in range(start, len(pool) - need + 1):
            p = pool[i]
            updated = tuple(have + bool(p & bit) for have, bit in zip(loads, AXES))
            yield from visit(i + 1, chosen + (p,), updated)

    yield from visit(0, (), (0,) * 6)


def points_on(points, axis, side):
    return tuple(p for p in points if ((p >> axis) & 1) == side)


def baseline_or_central(even, odd):
    """Test the accepted baseline and retain every central cut for the next test."""
    colors = (even, odd)
    central = []
    deltas = tuple(len(points_on(even, i, 1)) - len(points_on(odd, i, 1)) for i in AXES7)
    assert min(map(abs, deltas)) == 3
    for axis, gap in enumerate(map(abs, deltas)):
        if gap in (7, 8):
            return {"gate": f"gap{gap}", "axis": axis, "delta": deltas[axis]}, central
        if gap != 3:
            continue
        for side in (0, 1):
            restricted = tuple(points_on(group, axis, side) for group in colors)
            shape = tuple(map(len, restricted))
            if shape in ((3, 0), (0, 3), (4, 1), (1, 4)):
                gate = "monochromatic_three" if max(shape) == 3 else "R41"
                return {"gate": gate, "axis": axis, "B_side": side, "B_counts_even_odd": shape}, central
            if shape not in ((5, 2), (2, 5)):
                continue
            alpha = shape.index(5)
            w, roots = restricted[alpha], restricted[1 - alpha]
            a_minor = points_on(colors[alpha], axis, 1 - side)
            a_major = points_on(colors[1 - alpha], axis, 1 - side)
            assert (len(a_minor), len(a_major)) == (3, 6)
            loads = {
                i: (len(points_on(w, i, 1)), len(points_on(roots, i, 1)))
                for i in AXES7 if i != axis
            }
            s = sum(c - d in (1, 2) for c, d in loads.values())
            h = (roots[0] ^ roots[1]).bit_count()
            strong = [i for i, cd in loads.items() if cd in ((2, 0), (3, 2))]
            gate = None
            if h == 6:
                gate = "central_h6"
            elif s >= 3:
                gate = "central_s3"
            elif s >= 2 and strong:
                gate = "central_s2_strong"
            if gate:
                return {
                    "gate": gate, "axis": axis, "B_side": side, "alpha": alpha,
                    "W": w, "S": roots, "h": h, "s": s, "strong_axes": strong,
                    "B_bit_one_loads": loads,
                }, central
            central.append((axis, side, alpha, w, a_minor, a_major, loads))
    return None, central


def joint_witness(central):
    for axis, side, alpha, w, a_minor, a_major, loads in central:
        for x in a_major:
            y = x ^ (1 << axis)
            for d_axis, (c, d) in loads.items():
                d_side = (y >> d_axis) & 1
                g = c - d if d_side else 3 - c + d
                if g not in (1, 2, 3):
                    continue
                for t_axis in loads:
                    if t_axis == d_axis:
                        continue
                    for t_side in (0, 1):
                        a = len(points_on(a_minor, t_axis, t_side))
                        b = len(points_on(a_major, t_axis, t_side))
                        epsilon = int(((x >> t_axis) & 1) == t_side)
                        q = b - epsilon + 2 - a
                        if a in (0, 1) and q in (4, 5, 6):
                            gate = {4: "balanced_complement_avoid_two", 5: "two_majority_odd",
                                    6: "two_majority_even"}[q]
                        elif a == 2 and q == 3:
                            gate = "two_minority_odd"
                        else:
                            continue
                        w_in_t = points_on(w, t_axis, t_side)
                        in_d = points_on(w_in_t, d_axis, d_side)
                        out_d = points_on(w_in_t, d_axis, 1 - d_side)
                        if len(in_d) < g - 1 or len(out_d) < 3 - g:
                            continue
                        returns = in_d[:g - 1] + out_d[:3 - g]
                        assert len(returns) == len(set(returns)) == 2
                        return {
                            "gate": gate, "axis": axis, "B_side": side, "alpha": alpha,
                            "x": x, "y": y, "return_sources": returns,
                            "T": (t_axis, t_side), "D": (d_axis, d_side),
                            "a": a, "b": b, "epsilon": epsilon, "q": q, "g": g,
                            "W_in_T_D": in_d, "W_in_T_not_D": out_d,
                        }
    return None


def main():
    started = process_time()
    exceptions, allowed, input_hashes = load_inputs()
    preflight_raw = (HERE / "EXCEPTION_PREFLIGHT.json").read_bytes()
    preflight = json.loads(preflight_raw)
    assert preflight["input_SHA256"] == input_hashes
    expected_by_b = {
        tuple(b): count for b, count in preflight["exceptions"][0]["completions_by_b"]
        if b[2:] == sorted(b[2:])
    }
    assert sum(expected_by_b.values()) == 2757 < COMPLETION_LIMIT
    row = exceptions[0]
    w = tuple(row["W"])
    roots = tuple(row["receiver_minority_roots"])
    pool = tuple(row["available_odd_vertices"])
    assert w == (28, 44, 52, 56, 61) and roots == (0, 3)
    cd = tuple(zip(column_load(w), column_load(roots)))
    projected = tuple(tuple(b for b in range(7) if (c, d, b) in allowed) for c, d in cd)
    count_by_b = Counter()
    witness_counts = Counter()
    accepted = []
    unsupported = None
    budget_error = None
    candidate_count = 0
    try:
        for y, b in sources(pool, projected, started):
            if b[2:] != tuple(sorted(b[2:])) or b[1] == 6:
                continue
            permitted = tuple(allowed[c, d, value] for value, (c, d) in zip(b, cd))
            for u, a in completions(donor_pool(y, roots), permitted, started):
                timer(started)
                if candidate_count >= COMPLETION_LIMIT:
                    raise RuntimeError("Full geometry cap reached")
                candidate_count += 1
                count_by_b[b] += 1
                even = u + tuple(64 + p for p in w)
                odd = y + tuple(64 + p for p in roots)
                baseline, central = baseline_or_central(even, odd)
                witness = baseline or joint_witness(central)
                result = {"Y": y, "U": u, "a": a, "b": b, "even": even, "odd": odd}
                if witness is None:
                    unsupported = result
                    unsupported["central_cuts"] = central
                    break
                result["witness"] = witness
                accepted.append(result)
                witness_counts[witness["gate"]] += 1
            if unsupported:
                break
    except (TimeoutError, RuntimeError) as error:
        budget_error = str(error)
    if unsupported is None and budget_error is None:
        assert count_by_b == expected_by_b
    output = {
        "scope": "Sorted high-four b loads for the fixed W1 exception with b1 below six.",
        "input_SHA256": input_hashes,
        "preflight_SHA256": sha256(preflight_raw).hexdigest(),
        "expected_full_range": 2757,
        "canonicalization": "Sort b[2:] by the S4 stabilizer of S,W,F; keep all ties.",
        "candidate_count": candidate_count,
        "checked_by_b": sorted(count_by_b.items()),
        "matched_by_gate": sorted(witness_counts.items()),
        "unsupported_first": unsupported,
        "budget_error": budget_error,
        "CPU_limit_seconds": CPU_LIMIT, "CPU_seconds": process_time() - started,
        "full_geometry_limit": COMPLETION_LIMIT,
        "original_matchings_enumerated": 0, "solver_calls": 0,
        "accepted": accepted,
    }
    (HERE / "EXCEPTION_W1_CERTIFICATES.json").write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in output.items() if k != "accepted"}, indent=2))


if __name__ == "__main__":
    main()
