"""Verify the stored 19 first plans directly from the independently checked physical hole sets."""

from collections import Counter
from hashlib import file_digest
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
PLAN_SHA = "09b43f1b44a64ca87a4d965606bc31f927a4d8f381e665b196d4a38c92b96615"
GEOMETRY_SHA = "db2f7a47c191a4d6b7c39584d08071f3b8f1bb2d60b87dd6252b0f6a29cb26ab"


def digest(path):
    with path.open("rb") as handle:
        return file_digest(handle, "sha256").hexdigest()


def load(path):
    return json.loads(path.read_bytes())


def select(points, axis, val):
    return {v for v in points if (v >> axis) & 1 == val}


def two_counts(alpha, beta, axis, side):
    return [[len(select(alpha, axis, k)), len(select(beta, axis, k))] for k in (side, 1-side)]


def ordered_unique(values):
    assert len(values) == len(set(values))
    return set(values)


def plan_check(data, normalized):
    even, odd = (ordered_unique(data[name]) for name in ("H_even", "H_odd"))
    assert even == set(normalized["beta"]) and odd == set(normalized["alpha"])
    H = even | odd
    assert not even & odd and len(H) == 16 and min(H) >= 64
    assert all((u ^ v).bit_count() > 1 for u in even for v in odd)
    signs = [len(select(odd, j, 1)) - len(select(even, j, 1)) for j in range(7)]
    assert data["global_odd_minus_even"] == signs and signs[6] == 0
    assert all(x <= -2 for x in signs[:6])

    plan = data["first_plan"]
    gate, axis, inner, side = (plan[k] for k in ("gate", "outer_axis", "inner_axis", "receiver_bit"))
    assert axis in range(7) and inner in range(7) and inner != axis and side in (0, 1)
    # Determine receiver majority from the real physical hole set.
    receiver = select(H, axis, side)
    donor = H - receiver
    alpha = (odd if len(receiver & odd) > len(receiver & even) else even)
    beta = H - alpha
    aa, ab, ba, bb = donor & alpha, donor & beta, receiver & alpha, receiver & beta
    assert len(ba) > len(bb)
    r, s, k = len(aa), len(bb), len(ba)-len(bb)
    assert len(ab) == r+k and r+s+k == 8
    result = {
        "index": data["index"], "gate": gate, "outer_axis": axis, "receiver_bit": side,
        "inner_axis": inner, "alpha_parity": int(alpha == odd), "r": r, "s": s, "k": k,
        "original_outer_counts": [[len(aa), len(ab)], [len(ba), len(bb)]],
    }

    if gate == "same_side":
        assert (r, s, k) == (plan["r"], plan["s"], plan["k"]) == (3, 2, 3)
        x, U = plan["x"], ordered_unique(plan["U"])
        assert x in ab and len(U) == 2 and U <= ba
        y, V = x ^ (1 << axis), {u ^ (1 << axis) for u in U}
        assert plan["y"] == y and V == set(plan["V"]) and not ({y} | V) & H
        donor_side = plan["donor_half_bit"]
        assert donor_side in (0, 1) and select(V, inner, donor_side) == V
        modified_A = two_counts(aa, (ab-{x}) | V, inner, donor_side)
        assert modified_A == plan["modified_donor_halves"] == [[1, 5], [2, 2]]
        assert plan["marks"] == [2, 0]
        assert plan["modified_receiver_counts"] == [len((ba-U) | {y}), len(bb)] == [4, 2]
        result.update(X=[x], U=sorted(U), Y=[y], V=sorted(V),
                      modified_donor=modified_A, donor_minor_major="T15 plus positive-balanced complement",
                      receiver_tool="A6 with y omitted")
        return result

    assert result["alpha_parity"] == plan["alpha_parity"]
    assert result["original_outer_counts"] == plan["original_outer_halves_alpha_beta"]
    assert r <= 5 and k > 0
    X, Y = ordered_unique(plan["X"]), ordered_unique(plan["Y"])
    assert len(X) == k and X <= ab
    assert Y == {x ^ (1 << axis) for x in X} and Y.isdisjoint(H)
    assert all((v >> axis) & 1 == side for v in Y)
    side_flag = plan["inner_side"]
    assert side_flag in (0, 1)
    receiver_counts = two_counts(ba, bb, inner, side_flag)
    new_counts = two_counts(ba | Y, bb, inner, side_flag)
    marks = [len(select(Y, inner, z)) for z in (side_flag, 1-side_flag)]
    assert new_counts == plan["modified_receiver_halves_alpha_beta"] and marks == plan["marks_by_half"]
    col = plan["original_seen_column"]
    candidates = {x ^ (1 << axis) for x in ab}
    assert col == dict(minor=receiver_counts[0][1], majority=receiver_counts[0][0],
                       sources=len(select(candidates, inner, side_flag)))
    assert Y <= candidates

    if gate == "controlled_positive_split":
        assert plan["root"] is None
        assert all(q in (1, 2) and pairs[0]-pairs[1] == 2*q and (q == 1 or pairs[1] <= 1)
                   for pairs, q in zip(new_counts, marks))
        result["receiver_tool"] = ["A_ALL" if q == 1 else "T44" if ns == 0 else "T15"
                                   for (_, ns), q in zip(new_counts, marks)]
    elif gate == "central_single_root_split":
        assert (r,s,k) == (3,3,2) and marks == [1, 1]
        assert receiver_counts[1][0] == receiver_counts[1][1] >= 1
        assert receiver_counts[0][0] - receiver_counts[0][1] == 2
        assert receiver_counts[0][1] <= 1
        root = plan["root"]
        assert root in select(bb, inner, 1-side_flag)
        w = root ^ (1 << inner)
        assert w not in H and w not in Y
        result.update(root=root, root_mirror=w, receiver_tool="separated controlled single root")
    elif gate == "central_balanced_complement":
        assert (r,s,k) == (3,3,2) and marks == [2, 0]
        assert plan["root"] is None
        assert new_counts[0][0] - new_counts[0][1] == 4 and new_counts[0][1] <= 1
        assert new_counts[1][0] == new_counts[1][1] >= 1
        assert Y <= select(Y, inner, side_flag)
        result["receiver_tool"] = "T44/T15 plus nonempty balanced complement"
    else:
        raise ValueError(gate)
    result.update(X=sorted(X), Y=sorted(Y), receiver_original=receiver_counts,
                  receiver_modified=new_counts, receiver_marks=marks)
    return result


def main():
    plans_path = HERE / "MU0_A0_BASIS_PLANS.json"
    basis_path = HERE / "MU0_A0_BASIS_REVIEW_check.json"
    assert digest(plans_path) == PLAN_SHA
    basis_census = load(basis_path)
    assert basis_census["producer_basis_sha256"] == GEOMETRY_SHA and basis_census["verdict"] == "PASS"
    basis = basis_census["physical_hole_sets"]
    plans = load(plans_path)
    assert plans["basis_sha256"] == GEOMETRY_SHA
    assert digest(HERE / "MU0_A0_BASIS_PLANS.py") == plans["source_sha256"]
    rows = plans["results"]
    assert len(rows) == len(basis) == 19
    assert [x["index"] for x in rows] == [x["basis_index"] for x in basis] == list(range(19))
    checked = [plan_check(row, normalized) for row, normalized in zip(rows, basis)]
    counts = Counter(record["gate"] for record in checked)
    assert dict(counts) == {
        "controlled_positive_split": 7, "central_single_root_split": 4,
        "central_balanced_complement": 7, "same_side": 1,
    } == plans["first_gate_counts"]
    result = {
        "verdict": "PASS",
        "scope": "Verify the nineteen specified first plans directly; no search for new plans or prescribed matchings.",
        "basis_census_sha256": digest(basis_path),
        "plans_sha256": digest(plans_path),
        "checker_sha256": digest(Path(__file__)),
        "checked_plan_counts": dict(counts),
        "checked": checked,
    }
    target = HERE / "MU0_A0_PLANS_REVIEW_check.json"
    with target.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps({k: v for k,v in result.items() if k != "checked"}))


if __name__ == "__main__":
    main()

