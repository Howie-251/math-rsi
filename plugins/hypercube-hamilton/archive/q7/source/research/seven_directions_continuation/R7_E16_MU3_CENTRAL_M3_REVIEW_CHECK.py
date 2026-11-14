"""Independent finite check of the frozen E16 central m=3 submission."""

from collections import Counter, defaultdict
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, permutations, product
import json
from pathlib import Path
from time import process_time


HERE = Path(__file__).resolve().parent
RESEARCH = Path("E:/\u65b0\u95ee\u9898/research")
STEM = "R7_E16_MU3_CENTRAL_M3_"
OLD = "R7_E16_MU3_R32_M_GE4_CLOSURE_INPUTS.json"
RECEIVERS = "E16_MU3_CENTRAL_LOCAL_RECEIVER.json"
PREFLIGHT = "R7_E16_MU3_CENTRAL_LOWM_PREFLIGHT_COUNT.json"
PROOF_HASH = "181f307d7d4380ce133210b31e4386b28da6fa6b400f992659e034a01862ea77"
MANIFEST_HASH = "0bdf9440c651dc2021cfb6b89a849951e1c3fc531159359058d793261aa40dbb"
AXES = tuple(range(6))
BITS = tuple(1 << i for i in AXES)
EVEN = tuple(v for v in range(64) if v.bit_count() % 2 == 0)
ODD = tuple(v for v in range(64) if v.bit_count() % 2 == 1)
ADJ = tuple(frozenset(v ^ bit for bit in BITS) for v in range(64))
USEFUL = {(2, 0), (2, 1), (3, 1), (3, 2)}
START = process_time()


def guard():
    if process_time() - START >= 90:
        raise TimeoutError("central m=3 audit reached 90 CPU seconds")


def read(path):
    return json.loads((HERE / path).read_bytes())


def digest(path):
    return sha256((HERE / path).read_bytes()).hexdigest()


def loads(points):
    return tuple(sum((v >> i) & 1 for v in points) for i in AXES)


def scalar_table():
    def count_gate(donor, receiver):
        d = [a - b for a, b in receiver]
        return (sum(a for a, _ in donor) <= 5
                and all(x in (1, 2) and b >= x and (x == 1 or q <= 1)
                        for x, (_, b), (_, q) in zip(d, donor, receiver)))

    def covered(first, second, transposed):
        for source, target in ((first, second), (second, first)):
            for source, target in ((source, target),
                                   (tuple(p[::-1] for p in source), tuple(p[::-1] for p in target))):
                if count_gate(source, target):
                    return True
                if transposed and (sum(a for a, _ in source), sum(b for _, b in source),
                                   sum(b for _, b in target)) == (5, 8, 0):
                    return True
        return False

    relation = defaultdict(list)
    counter = Counter()
    for a, b, c, d in product(range(4), range(7), range(6), range(3)):
        gap = abs(a + c - b - d)
        counter["raw"] += 1
        if gap < 3:
            continue
        counter["gap"] += 1
        A, B = ((3 - a, 6 - b), (a, b)), ((5 - c, 2 - d), (c, d))
        if covered(A, B, False):
            continue
        counter["original"] += 1
        if covered((A[0], B[0]), (A[1], B[1]), True):
            continue
        counter["residual"] += 1
        if gap <= 6:
            counter["limited"] += 1
            relation[c, d].append((a, b, gap))
    assert counter == dict(raw=504, gap=212, original=204, residual=166, limited=156)
    return {k: set(v) for k, v in relation.items()}, counter


def map_point(point, destination, shift):
    return shift ^ sum(1 << j for i, j in enumerate(destination) if (point >> i) & 1)


def action(destination, shift):
    assert sorted(destination) == list(AXES) and 0 <= shift < 64
    return tuple(map_point(v, destination, shift) for v in range(64))


def move(points, mapping):
    return tuple(sorted(mapping[v] for v in points))


def root_group(h):
    return tuple(action(left + right, shift)
                 for left in permutations(range(h)) for right in permutations(range(h, 6))
                 for shift in (0, (1 << h) - 1))


POINT_KEY = tuple(sum(((v >> i) & 1) << (2 * i) for i in AXES) for v in range(64))
KEY_LOADS = tuple(tuple((key >> (2 * i)) & 3 for i in AXES) for key in range(4096))


@lru_cache(maxsize=2048)
def third_coefficients(pool):
    degree = [Counter({0: 1}), Counter(), Counter(), Counter()]
    for v in pool:
        shift = POINT_KEY[v]
        for k in (3, 2, 1):
            for key, count in degree[k - 1].items():
                degree[k][key + shift] += count
    return degree[3]


def coefficient(pool, allowed):
    if len(pool) < 3 or not all(allowed):
        return 0
    coeffs = third_coefficients(pool)
    return sum(count for key, count in coeffs.items()
               if all(value in column for value, column in zip(KEY_LOADS[key], allowed)))


def partitions(items):
    """All unordered partitions of the at most three active sparse columns."""
    if not items:
        yield ()
        return
    first, rest = items[0], items[1:]
    for partition in partitions(rest):
        yield (first,) + partition
        for i, part in enumerate(partition):
            yield partition[:i] + (first | part,) + partition[i + 1:]


def source_fiber(fibers, active):
    for partition in partitions(active):
        z = 6 - len(partition)
        if z > len(fibers[0]):
            continue
        for nonzero in product(*(fibers[p] for p in partition)):
            for zero in combinations(fibers[0], z):
                yield tuple(sorted(zero + nonzero))


def verify_pool(h, s, w, y, b, allowed, allowed5, record, raw_pool, pair_count, no_six):
    assert (record["h"], tuple(record["S"]), tuple(record["W"]), tuple(record["Y"])) == (h, s, w, y)
    assert tuple(record["b_loads"]) == b
    assert tuple(record["U_pool_raw"]) == raw_pool
    assert tuple(map(set, record["allowed_a"])) == allowed
    assert tuple(map(set, record["allowed_a_no_gap_six"])) == allowed5
    pool = tuple(record["U_pool"])
    assert tuple(sorted(set(pool))) == pool and set(pool) <= set(raw_pool)
    assert coefficient(pool, allowed) == pair_count
    assert coefficient(pool, allowed5) == no_six


def verify_source():
    rel, scalar = scalar_table()
    old = read(OLD)["input_sha256"]
    assert old[(HERE / RECEIVERS).as_posix()].removeprefix("sha256:") == digest(RECEIVERS)
    templates = read(RECEIVERS)["receivers"]
    assert len(templates) == 704
    broad = read(PREFLIGHT)
    assert broad["receiver_template_sha256"] == digest(RECEIVERS)
    assert broad["scalar_rows_after"] == 156
    assert {(row["c"], row["d"]): set(map(tuple, row["rows"]))
            for row in broad["allowed_a_b_gap"]} == rel
    old_rows = {(r["h"], tuple(r["W"])): r for r in broad["rows"] if r["m"] == 3}
    d = read(STEM + "SOURCE_PREFLIGHT.json")
    assert d["frozen_sha256"] == digest(PREFLIGHT) and d["status"] == "complete"
    source_rows = d["sources"]
    source_ids = {(r["h"], tuple(r["W"]), tuple(r["Y"])): i for i, r in enumerate(source_rows)}
    assert len(source_ids) == len(source_rows)
    reps = {r["source_index"]: r for r in d["representatives"]}
    assert len(reps) == len(d["representatives"])
    groups = {h: root_group(h) for h in (2, 4, 6)}
    seen = set()
    rep_groups = {}
    orbit_sizes = Counter()
    stats = defaultdict(Counter)
    extras = Counter()
    for template in templates:
        h, w = template["h"], tuple(template["W"])
        s = (0, (1 << h) - 1)
        cd = tuple(zip(loads(w), loads(s)))
        axes = tuple(i for i, pair in enumerate(cd) if pair in USEFUL)
        assert len(axes) == template["m"] and cd == tuple(map(tuple, template["loads_c_d"]))
        if len(axes) != 3:
            continue
        guard()
        count = stats[h]
        count["templates"] += 1
        row = old_rows.pop((h, w))
        options = tuple({b for _, b, _ in rel[c, d]} for c, d in cd)
        assert axes == tuple(row["sparse_axes"]) and options == tuple(map(set, row["b_projection"]))
        assert all(options[i] <= {0, 1, 5, 6} for i in axes)
        allowed_by_b = tuple({b: ({a for a, b1, _ in rel[pair] if b == b1},
                                  {a for a, b1, gap in rel[pair] if b == b1 and gap <= 5})
                              for b in options[i]} for i, pair in enumerate(cd))
        cases = {tuple(case["b"]): case for case in row["sparse_cases"]}
        assert len(cases) == len(row["sparse_cases"])
        receiver_group = tuple(g for g in groups[h] if move(w, g) == w)
        sparse_mask = sum(BITS[i] for i in axes)
        accepted_total = pair_total = projected_total = 0
        for sparse in product(*(sorted(options[i]) for i in axes)):
            case = cases.pop(sparse, None)
            count_case = Counter()
            shift = sum(BITS[i] for i, b in zip(axes, sparse) if b > 3)
            active = tuple(BITS[i] for i, b in zip(axes, sparse) if b in (1, 5))
            fibers = defaultdict(list)
            for point in ODD:
                if point not in w:
                    fibers[(point ^ shift) & sparse_mask].append(point)
            assert len(fibers[0]) <= 4
            min_zero = 6 - len(active)
            broad_pool = tuple(v for v in EVEN if v not in s and len(set(fibers[0]) - ADJ[v]) >= min_zero)
            weights = {}
            for y in source_fiber(fibers, active):
                count_case["raw"] += 1
                b = loads(y)
                assert tuple(b[i] for i in axes) == sparse
                if not all(x in allowed for x, allowed in zip(b, options)):
                    continue
                projected_total += 1
                allowed, allowed5 = tuple(zip(*(t[x] for x, t in zip(b, allowed_by_b))))
                if b not in weights:
                    weights[b] = coefficient(broad_pool, allowed), coefficient(broad_pool, allowed5)
                weight, weight5 = weights[b]
                raw_pool = tuple(v for v in EVEN if v not in s and not ADJ[v].intersection(y))
                assert set(raw_pool) <= set(broad_pool)
                real = coefficient(raw_pool, allowed)
                assert real <= weight
                ident = source_ids.get((h, w, y))
                if not weight:
                    assert ident is None and real == 0
                    continue
                assert case is not None and ident is not None and ident not in seen
                seen.add(ident)
                no_six = coefficient(raw_pool, allowed5)
                count_case["sources"] += 1
                count_case["pairs"] += weight
                count_case["pairs5"] += weight5
                record = source_rows[ident]
                verify_pool(h, s, w, y, b, allowed, allowed5, record, raw_pool, real, no_six)
                y_rep = min(move(y, g) for g in receiver_group)
                rep = source_ids[h, w, y_rep]
                assert record["representative_index"] == rep
                mapping = action(record["axis_destination"], record["xor_after_permutation"])
                target = source_rows[rep]
                assert mapping in receiver_group and move(y, mapping) == y_rep
                for key in ("U_pool_raw", "U_pool"):
                    assert move(record[key], mapping) == tuple(target[key])
                for i, j in enumerate(record["axis_destination"]):
                    flipped = (record["xor_after_permutation"] >> j) & 1
                    assert target["b_loads"][j] == (6 - b[i] if flipped else b[i])
                    for key in ("allowed_a", "allowed_a_no_gap_six"):
                        assert set(target[key][j]) == {3 - a if flipped else a for a in record[key][i]}
                count["pair_count_before_source_quotient"] += real
                orbit_sizes[rep] += 1
                if ident == rep:
                    witness = reps[rep]
                    assert (witness["U_coefficients"], witness["U_coefficients_no_gap_six"]) == (real, no_six)
                    rep_groups[rep] = tuple(g for g in receiver_group if move(y, g) == y)
                    count["representative_sources"] += 1
                    count["representatives_with_U"] += int(real > 0)
                    count["quotient_pair_count"] += real
                    count["quotient_pair_count_no_gap_six"] += no_six
            if case is None:
                assert count_case["sources"] == count_case["pairs"] == 0
                extras["omitted_sparse_cases"] += 1
                extras["raw_choices_outside_positive_cases"] += count_case["raw"]
            else:
                assert (count_case["sources"], count_case["pairs"], count_case["pairs5"]) == (
                    case["source_upper_bound"], case["pair_upper_bound"], case["pair_upper_bound_no_gap_six"])
                extras["positive_sparse_cases"] += 1
                count["raw_choices"] += count_case["raw"]
                accepted_total += count_case["sources"]
                pair_total += count_case["pairs"]
        assert not cases
        assert (projected_total, accepted_total, pair_total) == (
            row["source_projection_count"], row["source_upper_bound"], row["pair_upper_bound"])
        count["admitted_sources"] += accepted_total
        extras["relaxed_pairs"] += pair_total
    assert not old_rows and len(seen) == len(source_rows) == 5259
    assert {h: count["templates"] for h, count in stats.items()} == {2: 111, 4: 79, 6: 4}
    assert {str(h): c for h, c in stats.items()} == d["by_h"]
    assert {rep: r["source_orbit_size"] for rep, r in reps.items()} == dict(orbit_sizes)
    assert len(rep_groups) == len(reps) == 4163
    summary = sum(stats.values(), Counter())
    assert (summary["raw_choices"], summary["quotient_pair_count"], summary["pair_count_before_source_quotient"],
            extras["relaxed_pairs"]) == (13754, 50859, 59392, 150138)
    assert extras["positive_sparse_cases"] == 438
    return source_rows, reps, rep_groups, dict(scalar=scalar, by_h=stats, additional_checks=extras)


def physical_colors(row):
    return (set(row["U"]) | {v ^ 64 for v in row["W"]},
            set(row["Y"]) | {v ^ 64 for v in row["S"]})


def verify_base(sources, representatives, rep_groups):
    base = read(STEM + "BASE.json")
    assert base["status"] == "complete" and base["first_unfinished_source"] is None
    assert base["source_sha256"] == digest(STEM + "SOURCE_PREFLIGHT.json")
    raw = base["completion_transports"]
    rows = base["records"]
    assert len(raw) == base["qualified_completions"] == base["expected_completions"] == 50859
    assert len(rows) == base["record_count"]
    seen, hit = defaultdict(set), set()
    gap5_seen, raw_h, reps_h, gap5_h, group_sizes = (Counter() for _ in range(5))
    info = {}
    for rep, source in enumerate(sources):
        if rep not in representatives or not representatives[rep]["U_coefficients"]:
            continue
        group = rep_groups[rep]
        assert group
        group_sizes[len(group)] += 1
        info[rep] = (set(source["U_pool"]), tuple(map(set, source["allowed_a"])),
                     tuple(map(set, source["allowed_a_no_gap_six"])), group)
    for transport in raw:
        guard()
        i, u = transport["source_index"], tuple(transport["U"])
        pool, allowed, allowed5, group = info[i]
        assert len(u) == 3 and tuple(sorted(set(u))) == u and set(u) <= pool and u not in seen[i]
        seen[i].add(u)
        values = loads(u)
        assert all(a in column for a, column in zip(values, allowed))
        gap5_seen[i] += all(a in column for a, column in zip(values, allowed5))
        mapping = action(transport["axis_destination"], transport["xor_after_permutation"])
        assert mapping in group
        j = transport["representative"]
        assert 0 <= j < len(rows)
        row = rows[j]
        assert row["source_index"] == i
        assert move(u, mapping) == tuple(row["U"]) == min(move(u, g) for g in group)
        hit.add(j)
    assert len(hit) == len(rows)
    for i, expected in representatives.items():
        assert len(seen.get(i, ())) == expected["U_coefficients"]
        assert gap5_seen[i] == expected["U_coefficients_no_gap_six"]
        if expected["U_coefficients"]:
            raw_h[sources[i]["h"]] += expected["U_coefficients"]
    unique = set()
    for row in rows:
        guard()
        source = sources[row["source_index"]]
        assert all(row[k] == source[k] for k in ("h", "S", "W", "Y"))
        key = (row["source_index"], tuple(row["U"]))
        assert key not in unique
        unique.add(key)
        even, odd = physical_colors(row)
        assert len(even) == len(odd) == 8
        assert all(v.bit_count() % 2 == 0 for v in even) and all(v.bit_count() % 2 == 1 for v in odd)
        assert all((u ^ v).bit_count() != 1 for u, v in product(even, odd))
        gaps = tuple(sum((v >> i) & 1 for v in even) - sum((v >> i) & 1 for v in odd) for i in range(7))
        assert gaps[6] == 3 and all(3 <= abs(v) <= 6 for v in gaps)
        assert tuple(row["signed_gaps"]) == gaps
        reps_h[row["h"]] += 1
        gap5_h[row["h"]] += max(map(abs, gaps)) <= 5
    for key, counts in (("raw_counts_by_h", raw_h), ("counts_by_h", reps_h),
                        ("no_gap_six_by_h", gap5_h), ("stabilizer_sizes", group_sizes)):
        assert base[key] == {str(k): v for k, v in counts.items()}
    return rows, dict(representatives_by_h=reps_h, completions_by_h=raw_h,
                      representatives_no_gap_six=gap5_h, stabilizer_sizes=group_sizes)


def exact_registry():
    seven = RESEARCH / "seven_directions"
    profile = seven / "Q6_T15_ACTUAL_PROFILE.json"
    good = read(seven / "Q6_T15_GOOD_ROOT_COMPONENTS_REVIEW.json")
    s2 = read(seven / "Q6_T15_S2_COMBINED_EXTENSION_REVIEW.json")
    for receipt in (good, s2):
        assert receipt["verdict"] == "PASS"
        assert receipt["audited_input_hashes"][profile.name] == "sha256:" + digest(profile)
    accepted = set(good["union_closed_core_indices"])
    assert len(accepted) == 1017
    assert accepted == set(good["closed_core_indices"]) | set(s2["union_closed_core_indices"])
    for index in (85, 1054):
        stem = f"Q6_T15_CORE{index}_MARKED"
        receipt = read(seven / (stem + "_REVIEW.json"))
        assert receipt["verdict"] == "PASS" and receipt[f"core{index}_universal_proved"]
        for name in (stem + "_CLOSURE.md", profile.name):
            assert receipt["audited_input_hashes"][name] == "sha256:" + digest(seven / name)
        assert index not in accepted
        accepted.add(index)
    return {r["index"]: [r["included"], r["omitted"]] for r in read(profile)["orbits"]
            if r["index"] in accepted}


def forbid_edge_assumption(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if "edge" in key:
                assert key == "required_forced_edge" and value is None
            forbid_edge_assumption(value)
    elif isinstance(obj, list):
        for value in obj:
            forbid_edge_assumption(value)


def verify_plans(rows):
    # Reuse the prior independent checkers' local interface predicates only.
    # The earlier producers, large bases, main functions and rank code are not called.
    from R7_E16_MU3_GAP7_EVEN_MINIMAL_REVIEW_CHECK import directed_cut, face, one_send, shape
    from R7_E16_MU3_GAP7_EVEN_D30_REVIEW_CHECK import high_m
    from R7_E16_MU3_GAP7_ODD_REVIEW_CHECK import k4, whole_receiver_k3

    d = read(STEM + "FIXED_PLANS.json")
    assert d["base_sha256"] == digest(STEM + "BASE.json")
    assert d["status"] == "complete" and d["first_failure"] is None and d["unvisited"] == 0
    assert len(d["positives"]) == d["input_representatives"] == d["visited"] == len(rows) == 45924
    assert all(d[k] == 0 for k in ("new_geometries", "original_matchings_enumerated", "solver_calls", "rank_runs"))
    registry = exact_registry()
    seen, excluded_indices = set(), []
    gates, donors, cores, counts, params, high, modes, fallback, balanced, excluded = (
        Counter() for _ in range(10))
    for entry in d["positives"]:
        guard()
        index, plan = entry["index"], entry["plan"]
        assert 0 <= index < len(rows) and index not in seen
        seen.add(index)
        colors = physical_colors(rows[index])
        holes = colors[0] | colors[1]
        forbid_edge_assumption(plan)
        gate = plan["gate"]
        gates[gate] += 1
        try:
            if gate == "accepted_high_m":
                high_m(colors, plan["witnesses"])
                high["+".join(sorted(plan["witnesses"]))] += 1
                continue
            if gate == "impossible_geometry":
                exclusion = plan["exclusion"]
                assert exclusion["gate"] == "impossible_isolated_covered_vertex"
                v = exclusion["vertex"]
                assert 0 <= v < 128 and v not in holes and {v ^ (1 << i) for i in range(7)} <= holes
                excluded[v] += 1
                excluded_indices.append(index)
                continue
            j, a, b = directed_cut(colors, plan, "donor_side" if gate == "four_mono_capacity" else "A_side")
            if gate == "controlled_cycle_count":
                one_send(plan, j, a, b, counts)
                params[f"{plan['r']},{plan['k']}"] += 1
            elif gate == "k3_whole_receiver":
                whole_receiver_k3(plan, j, a, b, registry, cores)
                kind = plan["donor"]["kind"]
                donors[kind] += 1
                if kind == "Q6_balanced_complement_avoid_two":
                    balanced[str(plan["donor"]["face_counts"])] += 1
            elif gate == "four_mono_capacity":
                assert shape(a, b) == plan["shape"] == [[4, 8], [4, 0]]
                assert list(map(sorted, a)) == plan["original_A_by_alpha_beta"]
                assert list(map(sorted, b)) == plan["original_B_by_alpha_beta"]
                axes = [i for i in range(7) if i != j and len(face(b[0], i, 1)) == 2]
                assert plan["split_axes"] == axes and len(axes) in (3, 4, 5, 6)
                assert len(a[1]) > {3: 7, 4: 6, 5: 6, 6: 7}[len(axes)]
            else:
                assert gate == "k4_two_return"
                _, mode, kind = k4(plan, j, a, b, registry, fallback)
                if mode == "controlled_single_root":
                    receiver = plan["receiver"]
                    assert receiver["a"] in b[1] and receiver["w"] not in holes | set(plan["Y"])
                modes[f"{mode}:{kind}"] += 1
        except (AssertionError, KeyError, ValueError) as exc:
            raise AssertionError((index, gate)) from exc
    assert seen == set(range(len(rows))) and gates == d["plan_counts"] and donors == d["k3_donor_counts"]
    return dict(plan_counts=gates, k3_donors=donors, k3_cores=cores, controlled_local=counts,
                controlled_parameters=params, high_m=high, k4_receivers=modes,
                k4_suppliers={f"{k}:{v}": c for (k, v), c in sorted(fallback.items())},
                balanced_donor_shapes=balanced, excluded_vertices=excluded,
                impossible_geometry_indices=sorted(excluded_indices))


def main():
    assert __debug__
    manifest_name = STEM + "CLOSURE_INPUTS.json"
    assert digest(STEM + "CLOSURE.md") == PROOF_HASH and digest(manifest_name) == MANIFEST_HASH
    manifest = read(manifest_name)
    assert len(manifest["sha256"]) == 113
    for name, expected in manifest["sha256"].items():
        guard()
        assert digest(name) == expected, name
    print("Frozen inputs verified", flush=True)
    sources, reps, groups, source_check = verify_source()
    print("Source modes, coefficients and orbit transports verified", flush=True)
    rows, base_check = verify_base(sources, reps, groups)
    print("Full U coverage and orbit transports verified", flush=True)
    plan_check = verify_plans(rows)
    assert manifest["representatives"] == len(rows)
    assert manifest["representatives_by_h"] == {str(k): v for k, v in base_check["representatives_by_h"].items()}
    assert manifest["no_gap_six_by_h"] == {str(k): v for k, v in base_check["representatives_no_gap_six"].items()}
    assert manifest["plan_counts"] == plan_check["plan_counts"]
    assert manifest["k3_donor_counts"] == plan_check["k3_donors"]
    assert manifest["exact_T15_targets"] == {str(k): v for k, v in plan_check["k3_cores"].items()}
    assert manifest["impossible_geometry_indices"] == plan_check["impossible_geometry_indices"]
    guard()
    elapsed = process_time() - START
    result = dict(status="complete", proof_sha256=PROOF_HASH, manifest_sha256=MANIFEST_HASH,
                  bindings=len(manifest["sha256"]), sources=source_check, basis=base_check,
                  plans=plan_check, cpu_seconds=elapsed, cpu_budget=90, producer_runs=0,
                  plan_searches=0, matching_enumerations=0, solver_calls=0, rank_runs=0,
                  old_certificate_replays=0)
    with (HERE / (STEM + "REVIEW_CHECK.json")).open("x", encoding="utf-8", newline="\n") as f:
        json.dump(result, f, indent=2)
        f.write("\n")
    print(f"Fixed plans verified in {elapsed:.6f} CPU seconds total", flush=True)


if __name__ == "__main__":
    main()
