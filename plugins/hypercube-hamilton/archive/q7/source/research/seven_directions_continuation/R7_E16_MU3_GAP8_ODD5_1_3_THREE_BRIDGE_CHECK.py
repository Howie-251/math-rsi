"""One fixed-class check of the three-bridge whole-receiver gate."""

from collections import Counter
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
from time import process_time

from R7_DELTA2_DISTANCE2_BROAD_CHECK import core_transport
from R7_DOUBLE_RETURN_BRIDGE_GEOMETRY import donor_interface
from R7_E16_D35_B14_ZERO_SOURCE_CHECK import balanced_whole_wrapper
from R7_E16_DISTANCE2_TWO_RETURN_PLAN import whole_interface
from R7_E16_EVEN_HIGH_GAP_CHECK import t26_key, t26_registry
from R7_E16_MU3_GAP8_FIXED_PLANS import BASE, BASE_HASH, directed_cuts, physical_colors
from R7_MU3_BROAD_T15_DONOR_PROBE import RESEARCH, accepted_cores, marked_signature


def face(group, axis, side):
    return frozenset(v for v in group if (v >> axis) & 1 == side)


def project(point, axes):
    return sum(((point >> axis) & 1) << i for i, axis in enumerate(axes))


def supplier(outer, minor, retained, marks, lookup_t15, t26):
    if len(minor) == 1:
        exact = donor_interface(outer, minor, retained, marks, lookup_t15)
        if exact:
            return exact
    whole = balanced_whole_wrapper(whole_interface)(
        outer, minor, retained, marks, allow_t15_odd=True
    )
    if whole:
        return whole
    if len(minor) != 2:
        return None

    majority = retained | marks
    for inner in range(7):
        if inner == outer:
            continue
        for side in (0, 1):
            left = tuple(face(group, inner, side) for group in (minor, majority, marks))
            right = tuple(group - block for group, block in zip((minor, majority, marks), left))
            if tuple(map(len, left)) == (0, 6, 2) and tuple(map(len, right)) == (2, 0, 0):
                return dict(kind="T26_two_majority_roots", inner=inner, side=side)
            if tuple(map(len, left)) == (2, 3, 1) and tuple(map(len, right)) == (0, 3, 1):
                mirrors = {a ^ (1 << inner) for a in left[0]}
                if not mirrors & right[2] or mirrors & (right[1] - right[2]):
                    return dict(kind="T26_separated_two_root_choice", inner=inner, side=side)
            if left == (minor, majority, marks):
                axes = [i for i in range(7) if i not in (outer, inner)]
                projected = tuple(tuple(sorted(project(v, axes) for v in group)) for group in left)
                key = t26_key(*projected)
                if key in t26:
                    return dict(kind="T26_same_face", inner=inner, side=side,
                                rank=t26[key], projected=projected, canonical=key)
    return None


def run(start):
    def check_time():
        if process_time() - start >= 5:
            raise TimeoutError("fixed-class five CPU seconds")

    payload = BASE.read_bytes()
    assert sha256(payload).hexdigest() == BASE_HASH
    rows = json.loads(payload)["records"]
    indices = list(range(4546, 4560))
    assert all(rows[i]["family"] == "odd5_1_3" for i in indices)
    t15 = accepted_cores()
    t26 = t26_registry()
    profile = json.loads((RESEARCH / "Q6_T15_ACTUAL_PROFILE.json").read_bytes())
    targets = {row["index"]: row for row in profile["orbits"]}

    def lookup_t15(retained, marks):
        index = t15.get(marked_signature(retained, marks))
        if index is not None:
            groups = retained, marks
            return dict(kind="T15_exact_core", index=index, normalized_groups=groups,
                        coordinate_transport=core_transport(groups, targets[index]))
        return None

    def plan(row, counts):
        colors = physical_colors(row)
        for outer, b_side, alpha, donor, receiver in directed_cuts(colors):
            a_minor, a_major = map(frozenset, donor)
            b_major, b_minor = map(frozenset, receiver)
            if len(a_major) - len(a_minor) != 3 or len(a_minor) not in (1, 2):
                continue
            counts["oriented_outer_cuts"] += 1
            bit = 1 << outer
            for x in sorted(a_major):
                y = x ^ bit
                for u in combinations(sorted(b_major), 2):
                    check_time()
                    counts["source_choices"] += 1
                    b_new = (b_major - set(u)) | {y}
                    for inner in range(7):
                        if inner == outer:
                            continue
                        marked_side = (y >> inner) & 1
                        d = tuple(len(face(b_new, inner, side)) - len(face(b_minor, inner, side))
                                  for side in (0, 1))
                        if d[marked_side] == 2 and d[1 - marked_side] == 0:
                            break
                    else:
                        continue
                    counts["receiver_A6_choices"] += 1
                    v = frozenset(p ^ bit for p in u)
                    a_kept = a_major - {x}
                    assert not ({y} | v) & set(colors[0] + colors[1])
                    tool = supplier(outer, a_minor, a_kept, v, lookup_t15, t26)
                    if tool:
                        return dict(outer=outer, A_side=1 - b_side, alpha_parity=alpha,
                                    X=[x], U=u, Y=[y], V=sorted(v),
                                    A_minor=sorted(a_minor), A_retained=sorted(a_kept),
                                    B_minor=sorted(b_minor), B_new_major=sorted(b_new),
                                    B_inner=inner, B_marked_side=marked_side,
                                    B_deltas=d, donor=tool)
        return None

    positive = []
    failure = None
    for index in indices:
        counts = Counter()
        try:
            witness = plan(rows[index], counts)
        except TimeoutError:
            failure = dict(index=index, status="cpu_limit", counters=counts)
            break
        if witness is None:
            failure = dict(index=index, status="first_unsupported", counters=counts,
                           representative=rows[index])
            break
        positive.append(dict(index=index, plan=witness, counters=counts))
    return dict(base_sha256=BASE_HASH, indices=indices, positive=positive, failure=failure,
                cpu_seconds=process_time()-start, cpu_limit_seconds=5,
                solver_calls=0, original_matching_enumerations=0, rank_runs=0)


if __name__ == "__main__":
    result = run(process_time())
    with Path(__file__).with_suffix(".json").open("x", encoding="utf-8") as file:
        json.dump(result, file, indent=2)
        file.write("\n")
    print(json.dumps(result, separators=(",", ":")))
