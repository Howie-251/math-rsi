"""Apply the fixed S3/M3 menu to the stopped geometry or the whole W1 basis."""

from collections import Counter
from contextlib import contextmanager
from hashlib import sha256
import json
import sys
from itertools import combinations
from time import process_time
from unittest.mock import patch

from exception_preflight import HERE, column_load, donor_pool, load_inputs, sources
from exception_w1_certify import AXES7, baseline_or_central, completions, points_on
from exception_first_hole import accepted_cut_witness, previous_pass


CPU_LIMIT = 90
FULL_CAP = 2757
DEPENDENCIES = {
    "gap7": "R7_E16_MU3_GAP7_ODD_CLOSURE.md",
    "gap8": "R7_E16_MU3_GAP8_FULL_CLOSURE.md",
    "monochromatic_three": "R7_E16_THREE_MONOCHROMATIC_CLOSURE.md",
    "R41": "R7_E16_MU3_R41_M0_CLOSURE.md",
    "central_h6": "R7_E16_MU3_CENTRAL_ANTIPODAL_CLOSURE.md",
    "central_s3": "R7_E16_MU3_CENTRAL_S3_CLOSURE.md",
    "central_s2_strong": "R7_E16_MU3_CENTRAL_S2_STRONG_CLOSURE.md",
    "accepted_high_m": "R7_E16_MU3_CENTRAL_S3_FIXED_PLANS.py",
    "four_mono_capacity": "R7_FOUR_MONO_BALANCED_COORDINATES_REVIEW.md",
    "controlled_cycle_count": "R7_MU3_CONTROLLED_AND_T63_REVIEW.md",
    "controlled_cycle_registered_split": "R7_E16_MU3_CENTRAL_S3_REVIEW_CHECK.py",
    "k3_whole_receiver": "R7_MU3_THREE_BRIDGE_REVIEW.md",
    "k4_two_return": "R7_E16_ODD_22_COMPLETE_COVERAGE_REVIEW.md",
    "registry_two_return": "R7_E16_DISTANCE2_TWO_RETURN_PLAN_REVIEW.md",
    "impossible_geometry": "R7_E16_MU3_CENTRAL_M3_CLOSURE.md",
}
K3_DEPENDENCIES = {
    "Q6_balanced_complement_avoid_two": "R7_E14_NEXT_REVIEW.md",
    "Q6_same_side_majority_root": "R7_DELTA2_ODD_SAME_SIDE_RECEIVERS_REVIEW.md",
    "Q6_same_side_two_minority_roots": "R7_DELTA2_ODD_SAME_SIDE_RECEIVERS_REVIEW.md",
    "T26_separated_two_root_choice": "R7_MU3_THREE_BRIDGE_FULL_REVIEW.md",
    "Q6_T26_paired_S1": "R7_E14_ODD_RECEIVER_CLOSURE_REVIEW.md",
    "T26_two_majority_roots": "R7_TWO_MAJORITY_ROOTS_AVOID_TWO_REVIEW.md",
    "T15_same_face": "Q6_T15_GOOD_ROOT_COMPONENTS_REVIEW.json",
    "T15_isolated_mark": "Q6_TWO_AVOIDED_EASY_REVIEW.md",
    "Q6_T15_D4": "Q6_T15_D45_D3_REVIEW.json",
    "T15_exact_core": "R7_E16_MU3_CENTRAL_M3_CLOSURE.md",
}


@contextmanager
def legacy_menu(started):
    gates = previous_pass.gates
    accepted = gates.accepted
    broad = accepted.joint.broad_returns
    old_surviving = broad.surviving
    old_supplier = gates.supplier
    lookup = gates.make_t15_lookup()
    search = dict(lookup=None, broad=None)
    assert set(K3_DEPENDENCIES) == previous_pass.K3_AUDITED_DONORS

    def surviving_optional(edge, outer, side, omitted):
        return None if edge is None else old_surviving(edge, outer, side, omitted)

    def audited_supplier(outer, minor, retained, marks, lookup_t15, t26):
        plan = old_supplier(outer, minor, retained, marks, lookup_t15, t26)
        return plan if plan and plan["kind"] in previous_pass.K3_AUDITED_DONORS else None

    def find(colors, gaps, counters):
        accepted.check_time(started)
        baseline, _ = baseline_or_central(*colors)
        if baseline is not None:
            return baseline
        high = accepted_cut_witness(colors)
        plan = dict(gate="accepted_high_m", witnesses=high) if high else None
        found = (
            plan or accepted.joint.counts_orbits(colors) or gates.previous.four_mono(colors)
            or accepted.controlled_count(colors)
            or gates.k3_whole(colors, lookup, {}, counters, started)
            or gates.previous.first_plan(colors, gaps, search, counters, started)
        )
        accepted.check_time(started)
        return found

    with (
        patch.object(gates.previous, "directed_cuts", gates.directed_cuts),
        patch.object(gates, "supplier", audited_supplier),
        patch.object(accepted, "CPU_LIMIT", CPU_LIMIT),
        patch.object(gates.previous.four_limits, "CPU_LIMIT", CPU_LIMIT),
        patch.object(broad, "CPU_LIMIT", CPU_LIMIT),
        patch.object(broad, "surviving", surviving_optional),
        patch.object(broad, "whole_interface", accepted.balanced_whole_wrapper(broad.whole_interface)),
    ):
        yield find


def requires_edge(data):
    if isinstance(data, dict):
        return data.get("required_forced_edge") is not None or any(requires_edge(v) for v in data.values())
    if isinstance(data, (list, tuple)):
        return any(requires_edge(v) for v in data)
    return False


def signed_gaps(colors):
    return tuple(len(points_on(colors[0], i, 1)) - len(points_on(colors[1], i, 1)) for i in AXES7)


def completions_after(pool, permitted, previous):
    """List only triples strictly after the stored stop triple."""
    for i in (2, 1, 0):
        prefix = previous[:i]
        tail = tuple(p for p in pool if p > previous[i])
        if i == 0:
            yield from completions(tail, permitted, process_time())
            continue
        for rest in combinations(tail, 3 - i):
            z = prefix + rest
            a = column_load(z)
            if all(value in valid for value, valid in zip(a, permitted)):
                yield z, a


def all_candidates(started, after=None):
    exceptions, allowed, input_hashes = load_inputs()
    preflight_raw = (HERE / "EXCEPTION_PREFLIGHT.json").read_bytes()
    preflight = json.loads(preflight_raw)
    assert preflight["input_SHA256"] == input_hashes
    expected = {
        tuple(b): count for b, count in preflight["exceptions"][0]["completions_by_b"]
        if b[2:] == sorted(b[2:])
    }
    assert sum(expected.values()) == FULL_CAP
    row = exceptions[0]
    w, roots, pool = (tuple(row[key]) for key in ("W", "receiver_minority_roots", "available_odd_vertices"))
    assert w == (28, 44, 52, 56, 61) and roots == (0, 3)
    cd = tuple(zip(column_load(w), column_load(roots)))
    projected = tuple(tuple(b for b in range(7) if (c, d, b) in allowed) for c, d in cd)
    ordered = [
        (y, b) for y, b in sources(pool, projected, started)
        if b[2:] == tuple(sorted(b[2:])) and b[1] != 6
    ]

    def candidates():
        for y, b in ordered:
            if after is not None and y < tuple(after["Y"]):
                continue
            permitted = tuple(allowed[c, d, value] for value, (c, d) in zip(b, cd))
            available = donor_pool(y, roots)
            if after is not None and y == tuple(after["Y"]):
                supplies = completions_after(available, permitted, tuple(after["Z"]))
            else:
                # The outer loop applies the overall 90-second limit.
                supplies = completions(available, permitted, process_time())
            for z, a in supplies:
                even = z + tuple(64 + p for p in w)
                odd = y + tuple(64 + p for p in roots)
                yield {"Y": y, "Z": z, "a": a, "b": b, "even": even, "odd": odd}

    return candidates(), expected, input_hashes


def main(mode):
    started = process_time()
    prior_cpu = 0
    prefix_sha = None
    done_by_b = Counter()
    gate_counts = Counter()
    k3_donors = Counter()
    positives = []
    spot_file = HERE / "EXCEPTION_W1_BIDIRECTIONAL_CERTIFICATES.json"
    spot_raw = spot_file.read_bytes()
    spot_hash = sha256(spot_raw).hexdigest()
    if mode == "spot":
        case = json.loads(spot_raw)["unsupported_first"]
        assert tuple(case["Z"]) == (12, 54, 58)
        candidates = iter((case,))
        expected = {tuple(case["b"]): 1}
        input_hashes = {spot_file.name: spot_hash}
    else:
        spot = json.loads((HERE / "EXCEPTION_LEGACY_SPOT.json").read_bytes())
        assert spot["input_SHA256"][spot_file.name] == spot_hash
        assert spot["candidate_count"] == 1 and len(spot["positives"]) == 1 and not spot["failure"]
        if mode == "resume":
            original = (HERE / "EXCEPTION_LEGACY_FULL.json").read_bytes()
            prefix_sha = sha256(original).hexdigest()
            prefix = json.loads(original)
            failure = prefix["failure"]
            candidate = failure["candidate"]
            plan = failure["attempted_plan"]
            assert prefix["candidate_count"] == 251 and len(prefix["positives"]) == 250
            assert plan["gate"] == "registry_two_return" and not requires_edge(plan)
            assert plan["donor"]["kind"] == "T15_exact_core" and plan["donor"]["index"] == 117
            positives = prefix["positives"]
            positives.append(dict(
                candidate, deltas=signed_gaps((candidate["even"], candidate["odd"])), plan=plan,
                dependencies=[
                    DEPENDENCIES[plan["gate"]], "R7_E16_MU2_FULL_REVIEW.md",
                    "Q6_T15_GOOD_ROOT_COMPONENTS_REVIEW.json",
                ],
            ))
            done_by_b.update({tuple(b): n for b, n in prefix["checked_by_b"]})
            gate_counts.update(prefix["plan_counts"])
            gate_counts[plan["gate"]] += 1
            k3_donors.update(prefix["k3_donor_counts"])
            prior_cpu = prefix["CPU_seconds"]
            candidates, expected, input_hashes = all_candidates(started, after=candidate)
            assert prefix["input_SHA256"] == input_hashes
        else:
            candidates, expected, input_hashes = all_candidates(started)

    deadline_origin = started - prior_cpu
    failure = None
    try:
        with legacy_menu(deadline_origin) as find:
            for case in candidates:
                if process_time() - deadline_origin >= CPU_LIMIT:
                    raise TimeoutError("CPU cap reached")
                if sum(done_by_b.values()) >= sum(expected.values()):
                    raise RuntimeError("Candidate cap reached")
                colors = tuple(case["even"]), tuple(case["odd"])
                gaps = signed_gaps(colors)
                assert min(map(abs, gaps)) == 3
                counters = Counter()
                plan = find(colors, gaps, counters)
                done_by_b[tuple(case["b"])] += 1
                if plan is None or requires_edge(plan) or plan["gate"] not in DEPENDENCIES:
                    failure = {"candidate": case, "attempted_plan": plan, "counters": counters}
                    break
                gate = plan["gate"]
                dependency = [DEPENDENCIES[gate]]
                gate_counts[gate] += 1
                if gate == "k3_whole_receiver":
                    kind = plan["donor"]["kind"]
                    dependency.append(K3_DEPENDENCIES[kind])
                    k3_donors[kind] += 1
                elif gate == "registry_two_return":
                    dependency.append("R7_E16_MU2_FULL_REVIEW.md")
                    if plan["donor"]["kind"] == "T15_exact_core":
                        dependency.append("Q6_T15_GOOD_ROOT_COMPONENTS_REVIEW.json")
                positives.append(dict(case, deltas=gaps, plan=plan, dependencies=dependency))
    except (TimeoutError, RuntimeError, FileNotFoundError, ImportError) as error:
        failure = {"error": str(error)}

    if not failure:
        assert done_by_b == expected
    output = {
        "mode": mode,
        "scope": "Fixed S3/M3 menu plus the latest accepted geometric gates. First unsupported stops the run.",
        "input_SHA256": input_hashes,
        "inherited_prefix_SHA256": prefix_sha,
        "candidate_limit": sum(expected.values()),
        "candidate_count": sum(done_by_b.values()),
        "checked_by_b": sorted(done_by_b.items()),
        "failure": failure,
        "plan_counts": gate_counts,
        "k3_donor_counts": k3_donors,
        "CPU_limit_seconds": CPU_LIMIT,
        "CPU_seconds": process_time() - deadline_origin,
        "original_matchings_enumerated": 0, "solver_calls": 0,
        "positives": positives,
    }
    (HERE / f"EXCEPTION_LEGACY_{mode.upper()}.json").write_text(
        json.dumps(output, separators=(",", ":")) + "\n", encoding="utf-8",
    )
    print(json.dumps({k: v for k, v in output.items() if k != "positives"}, indent=2))
    if mode == "spot" and positives:
        print(json.dumps(positives[0]["plan"], indent=2))


if __name__ == "__main__":
    assert sys.argv[1:] in (["spot"], ["full"], ["resume"])
    main(sys.argv[1])
