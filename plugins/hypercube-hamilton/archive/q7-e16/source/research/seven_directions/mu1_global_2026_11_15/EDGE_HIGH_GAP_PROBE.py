"""Two capped physical-coordinate probes adding the audited high-gap constructions."""

import json
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
from time import perf_counter

import ortools
from ortools.sat.python import cp_model

from EDGE_LOW_GAP_PROBE import (
    ALPHA, AXES, BETA, COLORS, HERE, LIMIT_SECONDS, SEED, VERTICES, WORKERS,
    add_menu, add_old_coverage, bit_is_one, build_hole_model, check_matching,
    short_maximum_matching, validate_sat,
)
from GLOBAL_PROBE import indicator_at_least, indicator_equal
from JOINT_GAP_PROBE import old_phi
from ODD_WHOLE_PAIR_PROBE import every_whole_pair
from PROBE import oriented_cut

INNER_AXES = AXES[:-1]
Q_PAIRS = tuple(product((1, 2), repeat=2))


def add_high_gaps(model, holes):
    """Forbid exactly the four-Phi two-return plans under review."""
    existing = {v.name: i for i, v in enumerate(model.proto.variables)}
    counts = {}
    minima = {}

    def variable(name):
        return model.get_int_var_from_proto_index(existing[name])

    def count(color, *positions):
        pattern = tuple(sorted(set(positions)))
        if len({axis for axis, _ in pattern}) != len(pattern):
            return 0
        key = (color, pattern)
        if key not in counts:
            old_name = f"gate_count_{key}"
            if old_name in existing:
                counts[key] = variable(old_name)
            else:
                points = [v for v in COLORS[color]
                          if all(bit_is_one(v, axis) == side for axis, side in pattern)]
                val = model.new_int_var(0, min(8, len(points)), f"high_count_{key}")
                model.add(val == sum(holes[v] for v in points))
                counts[key] = val
        return counts[key]

    def at_least(color, minimum, *positions):
        key = (color, minimum, tuple(sorted(set(positions))))
        if key not in minima:
            amount = count(color, *positions)
            if isinstance(amount, int):
                minima[key] = model.new_constant(int(amount >= minimum))
            else:
                minima[key] = indicator_at_least(model, amount, minimum, f"high_min_{key}")
        return minima[key]

    # Common permutations of the internal axes preserve the outer cut and vertex 0.
    signatures = [variable(f"global_alpha_{j}") - variable(f"global_beta_{j}")
                  for j in INNER_AXES]
    for left, right in zip(signatures, signatures[1:]):
        model.add(left <= right)

    orientations = {}
    phi = {}
    table = [(r, a, b, *(int(old_phi(r, a, b - eps + 2 - a)) for eps in range(5)))
             for r in range(5) for a in range(r + 1) for b in range(9)]
    for j, b_side, alpha in product(AXES, (0, 1), (0, 1)):
        direction = (j, b_side, alpha)
        beta = 1 - alpha
        A, B = (j, 1 - b_side), (j, b_side)
        actual_gap = count(alpha, B) - count(beta, B)
        gap = {k: indicator_equal(model, actual_gap, k, f"high_gap_{direction}_{k}")
               for k in (4, 5, 6)}
        active = model.new_bool_var(f"high_active_{direction}")
        model.add(sum(gap.values()) == active)
        orientations[direction] = gap
        for h, t in product(AXES, (0, 1)):
            if h == j:
                continue
            T = (h, t)
            flags = [model.new_bool_var(f"high_phi_{direction}_{T}_{eps}") for eps in range(5)]
            r = count(alpha, A)
            a, b = count(alpha, A, T), count(beta, A, T)
            model.add_allowed_assignments([r, a, b, *flags], table).only_enforce_if(active)
            phi[direction, T] = flags

    positive_clauses = 0
    whole_pairs = 0
    for direction, gap in orientations.items():
        j, b_side, alpha = direction
        beta = 1 - alpha
        A, B = (j, 1 - b_side), (j, b_side)
        reverse = (j, 1 - b_side, beta)
        inner = tuple(i for i in AXES if i != j)
        halves = tuple(product(inner, (0, 1)))

        for i, (h, t) in product(inner, halves):
            S, Sc, T, Tc = (i, 0), (i, 1), (h, t), (h, 1 - t)
            g = count(alpha, B, S) - count(beta, B, S)
            inside, outside = count(alpha, B, S, T), count(alpha, B, Sc, T)
            for q0 in (1, 2):
                tag = f"{direction}_{S}_{T}_{q0}"
                receiving = [
                    indicator_at_least(model, g, q0, f"high_lower_{tag}"),
                    ~indicator_at_least(model, g, q0 + 3, f"high_upper_{tag}"),
                    indicator_at_least(model, inside - g, -q0, f"high_in_{tag}"),
                    indicator_at_least(model, outside + g, 2 + q0, f"high_out_{tag}"),
                ]
                for q1 in (1, 2):
                    k = q0 + q1 + 2
                    common = [gap[k], *receiving, at_least(beta, q0, A, S), at_least(beta, q1, A, Sc)]
                    if q0 == 2:
                        common.append(~at_least(beta, 2, B, S))
                    if q1 == 2:
                        common.append(~at_least(beta, 2, B, Sc))
                    for eps in range(q0 + q1 + 1):
                        capacities = (
                            (q0 - eps, (A, S, Tc)), (q1 - eps, (A, Sc, Tc)),
                            (q0 + q1 - eps, (A, Tc)), (eps - q1, (A, S, T)),
                            (eps - q0, (A, Sc, T)), (eps, (A, T)),
                        )
                        allowed_sources = [
                            at_least(beta, minimum, *pattern)
                            for minimum, pattern in capacities if minimum > 0
                        ]
                        # All six bounds hold for the SAME allocation with |X ∩ T| = eps.
                        terms = [*common, *allowed_sources, phi[direction, T][eps]]
                        model.add_bool_or([~term for term in terms])
                        positive_clauses += 1

        for S, T in product(halves, repeat=2):
            i, s = S
            h, t = T
            Sc, Tc = (i, 1 - s), (h, 1 - t)
            tag = f"{direction}_{S}_{T}"
            donor = model.new_bool_var(f"whole_donor_{tag}")
            receiver = model.new_bool_var(f"whole_receiver_{tag}")
            for n in range(3):
                # X is in A∩S*, U is in B∩T*. Choices use disjoint raw pools.
                X = [phi[direction, T][n], at_least(beta, n, A, S, T),
                     at_least(beta, 2 - n, A, S, Tc)]
                U = [phi[reverse, S][n], at_least(alpha, n, B, T, S),
                     at_least(alpha, 2 - n, B, T, Sc)]
                model.add_bool_or([~lit for lit in X] + [donor])
                model.add_bool_or([~lit for lit in U] + [receiver])
            model.add_bool_or([~gap[4], ~donor, ~receiver])
            whole_pairs += 1

    assert positive_clauses == 32256 and whole_pairs == 4032
    return dict(oriented_outer_cuts=len(orientations), positive_split_clauses=positive_clauses,
                whole_pair_choices=whole_pairs, internal_signed_delta_order=len(INNER_AXES) - 1)


def validate_high_geometry(holes):
    """Independently check actual X and U on fixed data, rather than table flags."""
    colors = tuple(tuple(v for v in color if v in holes) for color in COLORS)
    delta = [sum(bit_is_one(v, j) for v in colors[1]) - sum(bit_is_one(v, j) for v in colors[0])
             for j in AXES]
    positives = []
    for j, side in product(AXES, (0, 1)):
        k = abs(delta[j])
        if k not in (4, 5, 6):
            continue
        aa, ab, ba, bb = map(set, oriented_cut(colors, j, side))
        inner = tuple(i for i in AXES if i != j)
        for X, U in product(combinations(sorted(ab), k - 2), combinations(sorted(ba), 2)):
            Y, V = ({v ^ (1 << j) for v in src} for src in (X, U))
            assert not (Y | V) & holes
            new_a, new_b = (ab - set(X)) | V, (ba - set(U)) | Y
            receiver_ok = False
            for i in inner:
                q = sum(bit_is_one(y, i) for y in Y)
                qq = len(Y) - q
                small = sum(bit_is_one(v, i) for v in bb)
                net = sum(bit_is_one(v, i) for v in new_b) - small
                if (q, qq) in Q_PAIRS and net == 2 * q:
                    if (q == 1 or small <= 1) and (qq == 1 or len(bb) - small <= 1):
                        receiver_ok = True
                        break
            if not receiver_ok:
                continue
            for h in inner:
                t = bit_is_one(next(iter(V)), h)
                if any(bit_is_one(v, h) != t for v in V):
                    continue
                a = sum(bit_is_one(v, h) == t for v in aa)
                ell = sum(bit_is_one(v, h) == t for v in new_a) - a
                if old_phi(len(aa), a, ell):
                    positives.append(dict(outer=j, side=side, gap=k, X=X, U=U))
                    break
            else:
                continue
            break
    whole_pairs = every_whole_pair(colors, delta)
    return dict(positive_split=positives, whole_pair=[row for row in whole_pairs if row["first_plan"]])


def build(a):
    model, holes = build_hole_model(a)
    for vertex in VERTICES:
        model.add_bool_or([holes[vertex], *[~holes[vertex ^ (1 << j)] for j in AXES]])
    stats = dict(low_menu=add_menu(model, holes), previous_additions=add_old_coverage(model, holes),
                 high_gap=add_high_gaps(model, holes), no_isolated_nonhole=len(VERTICES))
    msg = model.validate()
    if msg:
        raise ValueError(msg)
    return model, holes, stats


def run(a):
    start = perf_counter()
    model, holes, stats = build(a)
    print(f"a={a}: model validated after {perf_counter()-start:.3f}s", flush=True)
    cp = cp_model.CpSolver()
    cp.parameters.max_time_in_seconds = LIMIT_SECONDS
    cp.parameters.num_search_workers = WORKERS
    cp.parameters.random_seed = SEED
    status = cp.solve(model)
    result = dict(a=a, b=7-a, status=cp.status_name(status), wall_seconds=cp.wall_time,
                  conflicts=cp.num_conflicts, branches=cp.num_branches,
                  gate_stats=stats, model_stats=model.model_stats(), response_stats=cp.response_stats(),
                  matching_calls=0)
    print(f"a={a}: {result['status']} in {result['wall_seconds']:.3f}s", flush=True)
    if status == cp_model.INFEASIBLE:
        # OR-Tools native export on Windows takes an ASCII relative filename.
        assert Path.cwd() == HERE
        filename = f"EDGE_HIGH_GAP_A{a}.pb"
        assert model.export_to_file(filename)
        result.update(model_file=filename, model_sha256=sha256((HERE / filename).read_bytes()).hexdigest())
    elif status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        H = {v for v in VERTICES if cp.value(holes[v])}
        axes = validate_sat(a, H)
        assert [row["delta"] for row in axes[:6]] == sorted(row["delta"] for row in axes[:6])
        assert not any(validate_high_geometry(H).values())
        assert all(any(v ^ (1 << j) not in H for j in AXES) for v in VERTICES if v not in H)
        matching = short_maximum_matching(H)
        realized = check_matching(H, matching)
        result.update(axes=axes, holes_alpha_odd=sorted(H.intersection(ALPHA)),
                      holes_beta_even=sorted(H.intersection(BETA)), matching_calls=1,
                      matching_size=len(matching), realized_by_short_matching=realized,
                      short_matching=matching)
        print(f"a={a}: short matching size {len(matching)}", flush=True)
    return result


def main():
    upstream = (HERE / "EDGE_LOW_GAP_PROBE.json").read_bytes()
    case = next(r for r in json.loads(upstream)["results"] if r["a"] == 1)
    control = validate_high_geometry(set(case["holes_alpha_odd"] + case["holes_beta_even"]))
    assert len(control["positive_split"]) == 8 and len(control["whole_pair"]) == 6
    output = dict(
        scope="EDGE_LOW_GAP_PROBE plus the four audited Phi suppliers, k=4..6 positive split and k=4 double whole",
        conditional_assumption="Q6 A8 input for the central gap-one exclusion and previous s=3 menus.",
        geometry_review="../mu3_hard_first_2026_11_15/ODD_HIGH_GAP_WHOLE_PAIR_REVIEW.md",
        sorting="Signed odd-minus-even differences on the six internal axes in nondecreasing order, by a common axis permutation fixing outer 6 and vertex 0.",
        code_sha256={name: sha256((HERE / name).read_bytes()).hexdigest()
                     for name in ("EDGE_PROBE.py", "EDGE_MENU_PROBE.py", "EDGE_LOW_GAP_PROBE.py", Path(__file__).name)},
        input_sha256=sha256(upstream).hexdigest(),
        matching_necessity="Every nonhole has some nonhole short neighbor.",
        cp_model_calls=0, max_seconds_per_call=LIMIT_SECONDS, num_search_workers=WORKERS,
        ortools_version=ortools.__version__, seed=SEED, results=[],
    )
    for a in (0, 1):
        output["results"].append(run(a))
        output["cp_model_calls"] += 1
        Path(__file__).with_suffix(".json").write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
