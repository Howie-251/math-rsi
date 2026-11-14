"""Check frozen central s>=2 strong-column coverage independently of production."""

from collections import Counter, defaultdict
from itertools import combinations, product
import json
from math import comb
from pathlib import Path
import sys
from time import process_time

from R7_E16_MU3_CENTRAL_S3_REVIEW_CHECK import (
    ADJ, AXES, EVEN, ODD, RECEIVERS, USEFUL, action, check_scalar, coefficient,
    digest, directed_cut, face, forbid_edge_assumption, guard, k4, loads, move,
    one_send, read, root_group, source_info, verify_original_cut, whole_receiver_k3,
)


STEM = "R7_E16_MU3_CENTRAL_S2_STRONG_"
COARSE = "R7_E16_MU3_CENTRAL_S2_PREFLIGHT.json"
STRONG = {(2, 0), (3, 2)}
CPU_LIMIT = 60
S3_RECEIPT = "R7_E16_MU3_CENTRAL_S3_REVIEW.json"
H6_RECEIPT = "R7_E16_MU3_CENTRAL_ANTIPODAL_REVIEW.json"
EXPECTED_S3_RECEIPT = "bbbad5bdd633a02a105d8e9c598cb66d89811a0f27bb069d55e5eb01ec6b4750"


def check_imports():
    s3, antipodal = read(S3_RECEIPT), read(H6_RECEIPT)
    assert digest(S3_RECEIPT) == EXPECTED_S3_RECEIPT
    assert s3["verdict"] == "PASS" and s3["central_s_ge3_proved"]
    assert antipodal["verdict"] == "PASS" and antipodal["central_antipodal_all_m_proved"]
    imports = dict(s3=s3["audited_input_hashes"], antipodal={k: v for k, v in
        antipodal["audited_input_hashes"].items() if Path(k).name in (
            "R7_E16_MU3_CENTRAL_ANTIPODAL_CLOSURE.md",
            "R7_E16_MU3_CENTRAL_ANTIPODAL_CLOSURE_INPUTS.json")})
    assert all(len(paths) == 2 for paths in imports.values())
    for label, receipt in (("s3", s3), ("antipodal", antipodal)):
        report, = (path for path in receipt["evidence_hashes"] if path.endswith("_REVIEW.md"))
        imports[label] = dict(imports[label], **{report: receipt["evidence_hashes"][report]})
        for path, expected in imports[label].items():
            assert digest(path) == expected.removeprefix("sha256:"), path

    r32 = read("R7_E16_MU3_R32_M_GE4_REVIEW.json")
    assert r32["verdict"] == "PASS" and r32["verification"]["basis"]["receiver_orbits"] == 704
    manifest = "R7_E16_MU3_R32_M_GE4_CLOSURE_INPUTS.json"
    for path in (manifest, "R7_E16_MU3_R32_M_GE4_CLOSURE.md"):
        assert r32["audited_input_hashes"][path].removeprefix("sha256:") == digest(path)
    receiver_hash, = (value for path, value in read(manifest)["input_sha256"].items()
                      if Path(path).name == RECEIVERS)
    assert receiver_hash == digest(RECEIVERS)
    r41 = read("R41_FULL_REVIEW.json")
    assert r41["verdict"] == "PASS" and r41["full_R41_proved"]
    return imports


def check_receivers():
    partition, hist, all_s2_h_m, all_s2_h_strong = (Counter() for _ in range(4))
    templates, seen = {}, set()
    all_s2 = set()
    for row in read(RECEIVERS)["receivers"]:
        h, w = row["h"], tuple(row["W"])
        key = (h, w)
        assert h in (2, 4, 6) and key not in seen and len(w) == 5 and w == tuple(sorted(set(w)))
        seen.add(key)
        s = (0, (1 << h) - 1)
        assert set(w) <= set(ODD) - ADJ[s[0]] - ADJ[s[1]]
        cd = tuple(zip(loads(w), loads(s)))
        m = sum(col in USEFUL for col in cd)
        assert cd == tuple(map(tuple, row["loads_c_d"])) and m == row["m"]
        sparse = tuple(i for i, (c, d) in enumerate(cd) if c-d in (1, 2))
        strong = sum(col in STRONG for col in cd)
        assert strong <= m <= len(sparse)
        if h != 6 and len(sparse) == 2:
            all_s2.add(key)
            all_s2_h_m[h, m] += 1
            all_s2_h_strong[h, strong] += 1
        if len(sparse) < 2 or strong == 0:
            partition["outside_scope"] += 1
        elif len(sparse) >= 3:
            partition["accepted_s_ge3"] += 1
        elif h == 6:
            partition["accepted_h6_s2"] += 1
        else:
            templates[key] = s, cd, sparse, strong, m
            partition[f"new_h{h}"] += 1
            hist[h, m, strong] += 1
    assert len(seen) == 704 and len(all_s2) == 207
    assert partition["new_h2"] == 72 and partition["new_h4"] == 4
    assert all_s2_h_m == {(2, 1): 16, (2, 2): 139, (4, 2): 52}
    assert all_s2_h_strong == {(2, 0): 83, (2, 1): 61, (2, 2): 11, (4, 0): 48, (4, 1): 4}
    return templates, all_s2, dict(partition=partition,
        all_s2_by_h_m={",".join(map(str, k)): n for k, n in all_s2_h_m.items()},
        all_s2_by_h_strong={",".join(map(str, k)): n for k, n in all_s2_h_strong.items()},
        by_h_m_strong={",".join(map(str, k)): n for k, n in hist.items()})


def fiber_sources(w, s, sparse, cd, relation, projection):
    """Derive fibers from rare-bit counts. Account for the zero-capacity modes."""
    shapes = ("zero6", "zero5_unit", "zero4_two_units", "zero5_pair")
    measures = ("fiber_choices", "projected_Y", "relaxed_pairs", "modes", "positive_modes")
    counts = {shape: Counter({k: 0 for k in measures}) for shape in shapes}
    mask = sum(1 << i for i in sparse)
    valid = set()
    choices = tuple(projection[col] for col in cd)
    for rare in product(*(sorted(choices[i]) for i in sparse)):
        assert all(v in (0, 1, 5, 6) for v in rare)
        active = [i for i, b in zip(sparse, rare) if b in (1, 5)]
        assert len(active) <= 1
        flip = sum(1 << i for i, b in zip(sparse, rare) if b in (5, 6))
        fibers = {k: tuple(v for v in ODD if (v ^ flip) & mask == k and v not in w)
                  for k in (0, *(1 << i for i in sparse), mask)}
        assert sum(map(len, fibers.values())) == 27 and all(len(f) <= 8 for f in fibers.values())
        name = "zero5_unit" if active else "zero6"
        count = counts[name]
        exceptions = fibers[1 << active[0]] if active else (None,)
        nzero = 6 - len(active)
        bound = comb(len(fibers[0]), nzero) * len(exceptions)
        count.update(modes=1, positive_modes=bool(bound), fiber_choices=bound)
        relaxed_pool = tuple(u for u in EVEN if u not in s
                             and len(set(fibers[0]) - ADJ[u]) >= nzero
                             and any(v not in ADJ[u] for v in exceptions))
        generated = 0
        for zero, exceptional in product(combinations(fibers[0], nzero), exceptions):
            generated += 1
            y = tuple(sorted(zero if exceptional is None else zero + (exceptional,)))
            b = loads(y)
            assert len(set(y)) == 6 and tuple(b[i] for i in sparse) == rare
            if all(value in opts for value, opts in zip(b, choices)):
                assert y not in valid
                valid.add(y)
                count["projected_Y"] += 1
                allowed = tuple(frozenset(relation[c, d, value]) for (c, d), value in zip(cd, b))
                count["relaxed_pairs"] += coefficient(relaxed_pool, allowed)
        assert generated == bound
    return valid, counts


def check_sources(templates, all_s2, relation, projection, start):
    coarse, exact = read(COARSE), read(STEM + "PREFLIGHT.json")
    assert exact["coarse_preflight_sha256"] == digest(COARSE)
    assert coarse["status"] == exact["status"] == "complete"
    assert coarse["necessary_scalar_rows"] == 140
    coarse_rows = {(r["h"], tuple(r["W"])): r for r in coarse["templates"]}
    assert coarse_rows.keys() == all_s2 and len(coarse["templates"]) == coarse["expected_templates"] == 207
    assert templates.keys() == {k for k, r in coarse_rows.items() if r["strong_columns"]}
    assert exact["template_count"] == exact["expected_templates"] == len(exact["rows"]) == 76
    groups = {h: root_group(h) for h in (2, 4)}
    sources, totals, hist = {}, Counter(), defaultdict(Counter)
    shape_totals = defaultdict(Counter)
    seen = set()
    for ti, row in enumerate(exact["rows"]):
        guard(start)
        h, w = key = row["h"], tuple(row["W"])
        assert key not in seen
        seen.add(key)
        s, cd, sparse, strong, m = templates[key]
        assert list(s) == row["S"] and list(sparse) == row["sparse_axes"]
        assert cd == tuple(map(tuple, row["loads_c_d"])) and (2, strong, m) == (
            row["s"], row["strong_columns"], row["m"])
        assert all(row[k] == coarse_rows[key][k] for k in
                   ("h", "m", "s", "S", "W", "loads_c_d", "sparse_axes", "strong_columns"))
        valid, shapes = fiber_sources(w, s, sparse, cd, relation, projection)
        assert shapes == coarse_rows[key]["by_shape"]
        for name, stat in shapes.items():
            shape_totals[name].update(stat)
        metrics = {k: sum(stat[k] for stat in shapes.values()) for k in shapes["zero6"]}
        assert all(value == coarse_rows[key][k] for k, value in metrics.items())
        assert len(valid) == metrics["projected_Y"]
        subgroup = tuple(a for a in groups[h] if move(w, a) == w)
        assert all(move(s, a) == s for a in subgroup) and len(subgroup) == row["receiver_stabilizer_size"]
        data = {y: source_info(s, y, cd, relation) for y in valid}
        counts = Counter({key: 0 for key in exact["totals"]})
        counts.update(raw_choices=metrics["fiber_choices"], labeled_Y=len(valid))
        for si, record in enumerate(row["source_representatives"]):
            y = tuple(record["Y"])
            orbit = {move(y, a) for a in subgroup}
            assert y == min(orbit) and orbit <= valid
            valid.difference_update(orbit)
            b, pool, allowed = data[y]
            assert list(b) == record["b_loads"] and list(pool) == record["U_pool"]
            assert [sorted(v) for v in allowed] == record["allowed_a"]
            n, orbit_size = coefficient(pool, allowed), len(orbit)
            assert n == record["exact_U"] and orbit_size == record["source_orbit_size"]
            for tr in record["source_transport"]:
                member = tuple(tr["Y"])
                orbit.remove(member)
                perm, shift = tr["axis_destination"], tr["xor_after_permutation"]
                a = action(perm, shift)
                assert a in subgroup and move(member, a) == y
                old_b, old_pool, old_allowed = data[member]
                assert move(old_pool, a) == pool
                for src, dst in enumerate(perm):
                    flipped = (shift >> dst) & 1
                    c, d = cd[src]
                    assert ((5-c, 2-d) if flipped else (c, d)) == cd[dst]
                    assert (6-old_b[src] if flipped else old_b[src]) == b[dst]
                    assert ({3-x for x in old_allowed[src]} if flipped else old_allowed[src]) == allowed[dst]
                counts["root_exchange_transports"] += bool(shift)
            assert not orbit
            common = tuple(a for a in subgroup if move(y, a) == y)
            assert common and all(move(pool, a) == pool for a in common)
            sources[ti, si] = (h, s, w, y, pool, allowed, common, n, orbit_size, strong, m)
            counts.update(source_orbits=1, source_orbits_with_U=bool(n), exact_U_on_source_reps=n,
                          exact_labeled_Y_U=n*orbit_size)
        assert not valid and counts == row["counts"]
        totals.update(counts)
        hist[h].update(counts)
    assert seen == templates.keys() and totals == exact["totals"]
    assert hist == {int(h): r for h, r in exact["counts_by_h"].items()}
    assert totals == dict(raw_choices=22336, labeled_Y=4491, source_orbits=3822,
                          source_orbits_with_U=2269, root_exchange_transports=15,
                          exact_U_on_source_reps=20760, exact_labeled_Y_U=23949)
    assert shape_totals == coarse["cohorts"]["at_least_one_strong"]["by_shape"]
    assert sum(stat["relaxed_pairs"] for stat in shape_totals.values()) == 64438
    return sources, exact["rows"], dict(totals=totals, by_h=hist, fiber_shapes=shape_totals)


def check_base(sources, preflight_rows, start):
    base = read(STEM + "BASE.json")
    assert base["status"] == "complete" and base["first_unfinished_source"] is None
    assert base["source_sha256"] == digest(STEM + "PREFLIGHT.json")
    records, colors, keys, seen = base["records"], [], set(), set()
    per_source, per_template, per_h = Counter(), defaultdict(Counter), defaultdict(Counter)
    assert len(records) == base["record_count"] == 19718
    for index, record in enumerate(records):
        if index % 512 == 0:
            guard(start)
        ti, si = key = record["template_index"], record["source_index"]
        h, s, w, y, pool, allowed, common, n, _, strong, m = sources[key]
        u = tuple(record["U"])
        assert n > 0 and (key, u) not in keys and len(set(u)) == 3 and set(u) <= set(pool)
        keys.add((key, u))
        assert u == min(move(u, a) for a in common)
        assert record["common_stabilizer_size"] == len(common)
        assert (h, s, w, y, m, 2, strong) == (record["h"], tuple(record["S"]), tuple(record["W"]),
            tuple(record["Y"]), record["m"], record["s"], record["strong_columns"])
        assert all(v in opts for v, opts in zip(loads(u), allowed))
        even, odd = set(u) | {64 ^ v for v in w}, set(y) | {64 ^ v for v in s}
        assert all(len(g) == 8 and all(v.bit_count() % 2 == p for v in g)
                   for p, g in enumerate((even, odd)))
        assert all((a ^ b).bit_count() != 1 for a, b in product(even, odd))
        gap = tuple(sum((v >> j) & 1 for v in even) - sum((v >> j) & 1 for v in odd) for j in range(7))
        assert gap == tuple(record["signed_gaps"]) and gap[6] == 3 and all(3 <= abs(g) <= 6 for g in gap)
        colors.append((even, odd))
        per_template[ti]["representatives"] += 1
    assert len({(frozenset(a), frozenset(b)) for a, b in colors}) == len(records)
    for i, tr in enumerate(base["completion_transports"]):
        if i % 512 == 0:
            guard(start)
        index = tr["representative"]
        assert 0 <= index < len(records)
        row = records[index]
        key = row["template_index"], row["source_index"]
        u = tuple(tr["U"])
        assert u == tuple(sorted(set(u))) and (key, u) not in seen
        seen.add((key, u))
        _, _, _, _, pool, allowed, common, _, orbit_size, _, _ = sources[key]
        a = action(tr["axis_destination"], tr["xor_after_permutation"])
        assert a in common and move(u, a) == tuple(row["U"])
        assert move(pool, a) == pool and len(u) == 3 and set(u) <= set(pool)
        assert all(value in opts for value, opts in zip(loads(u), allowed))
        per_source[key] += 1
        per_template[key[0]].update(completions=1, labeled_Y_U=orbit_size)
    assert len(seen) == base["qualified_completions"] == 20760 and keys <= seen
    for (ti, si), (_, _, _, _, _, _, _, n, _, _, _) in sources.items():
        assert per_source[ti, si] == n
        per_template[ti]["positive_sources"] += bool(n)
    assert len(base["summaries"]) == len(per_template) == 76
    for ti, summary in enumerate(base["summaries"]):
        h = summary["h"]
        assert (h, summary["W"]) == (preflight_rows[ti]["h"], preflight_rows[ti]["W"])
        assert per_template[ti] == Counter(summary["counts"])
        per_h[h].update(per_template[ti])
    assert per_h == {int(h): row for h, row in base["counts_by_h"].items()}
    assert {h: stat["representatives"] for h, stat in per_h.items()} == {2: 19215, 4: 503}
    assert sum(stat["labeled_Y_U"] for stat in per_h.values()) == base["labeled_Y_U"] == 23949
    assert all(base[k] == 0 for k in ("plans", "original_matchings_enumerated", "solver_calls", "rank_runs"))
    return colors, dict(representatives=len(records), transports=len(seen), by_h=per_h)


def check_plans(colors, start):
    data = read(STEM + "FIXED_PLANS.json")
    assert data["base_sha256"] == digest(STEM + "BASE.json")
    assert data["status"] == "complete" and data["first_failure"] is None
    assert len(data["positives"]) == data["visited"] == data["input_representatives"] == len(colors)
    assert all(data[k] == 0 for k in ("unvisited", "new_geometries", "original_matchings_enumerated",
                                     "solver_calls", "rank_runs"))
    assert data["accepted_receipts_sha256"].keys() == {
        "R41_FULL_REVIEW.json", S3_RECEIPT, H6_RECEIPT}
    for path, expected in data["accepted_receipts_sha256"].items():
        assert digest(path) == expected and read(path)["verdict"] == "PASS"
    seen, gates, donors, cores, controlled, parameters, suppliers, receivers = set(), *(Counter() for _ in range(7))
    for entry in data["positives"]:
        index, p = entry["index"], entry["plan"]
        if index % 256 == 0:
            guard(start)
        assert index not in seen and 0 <= index < len(colors)
        seen.add(index)
        gate = p["gate"]
        gates[gate] += 1
        forbid_edge_assumption(p)
        try:
            if gate in ("accepted_central_s_ge3", "accepted_central_antipodal_h6"):
                witness = p["witness"] if gate == "accepted_central_s_ge3" else p
                j, a, b = directed_cut(colors[index], witness, "donor_side")
                verify_original_cut(a, b, witness, [[3, 6], [5, 2]])
                if gate == "accepted_central_s_ge3":
                    cd = [[i, [len(face(g, i, 1)) for g in b]] for i in range(7) if i != j]
                    sparse = [i for i, (c, d) in cd if c-d in (1, 2)]
                    assert cd == witness["inner_loads"] and sparse == witness["sparse_axes"] and len(sparse) >= 3
                else:
                    u, v = b[1]
                    assert (u ^ v).bit_count() == witness["h"] == 6
                continue
            j, a, b = directed_cut(colors[index], p, "donor_side" if gate == "four_mono_capacity" else "A_side")
            if gate == "controlled_cycle_count":
                one_send(p, j, a, b, controlled)
                parameters[f"{p['r']},{p['k']}"] += 1
            elif gate == "k3_whole_receiver":
                whole_receiver_k3(p, j, a, b, {}, cores)
                donors[p["donor"]["kind"]] += 1
            elif gate == "four_mono_capacity":
                verify_original_cut(a, b, p, [[4, 8], [4, 0]])
                split = [i for i in range(7) if i != j and len(face(b[0], i, 1)) == 2]
                assert split == p["split_axes"] and len(a[1]) > {3: 7, 4: 6, 5: 6, 6: 7}[len(split)]
            else:
                assert gate == "k4_two_return"
                supplier, mode, kind = k4(p, j, a, b, {}, suppliers)
                assert supplier in ("majority_root", "two_minority_roots")
                if mode == "controlled_single_root":
                    assert p["receiver"]["a"] in b[1] and p["receiver"]["w"] not in set.union(*a, *b) | set(p["Y"])
                receivers[f"{mode}:{kind}" if kind is not None else mode] += 1
        except (AssertionError, KeyError, ValueError) as exc:
            raise AssertionError((index, gate)) from exc
    assert seen == set(range(19718))
    assert gates == data["plan_counts"] == dict(accepted_central_s_ge3=6328, accepted_central_antipodal_h6=2,
        four_mono_capacity=12, controlled_cycle_count=8443, k3_whole_receiver=4928, k4_two_return=5)
    assert donors == data["k3_donor_counts"] == dict(Q6_same_side_majority_root=2533,
        T26_separated_two_root_choice=544, Q6_balanced_complement_avoid_two=1243,
        T26_two_majority_roots=511, Q6_T26_paired_S1=20, Q6_same_side_two_minority_roots=77)
    assert not cores
    supplier_totals = Counter()
    for (kind, _), n in suppliers.items():
        supplier_totals[kind] += n
    return dict(gates=gates, controlled_modes=controlled, controlled_parameters=parameters,
                k3_donors=donors, k3_cores=cores, k4_suppliers=supplier_totals, k4_receivers=receivers)


def main(start, manifest_hash):
    assert __debug__
    manifest = STEM + "CLOSURE_INPUTS.json"
    assert digest(manifest) == manifest_hash
    frozen = read(manifest)
    hashes = frozen["sha256"]
    for path, expected in hashes.items():
        guard(start)
        assert digest(path) == expected.removeprefix("sha256:"), path
    names = {Path(path).name for path in hashes}
    required = {STEM + name for name in ("CLOSURE.md", "PREFLIGHT.json", "BASE.json", "FIXED_PLANS.json")}
    assert required | {COARSE, S3_RECEIPT, H6_RECEIPT, RECEIVERS} <= names
    imports = check_imports()
    templates, all_s2, partition = check_receivers()
    relation, projection, scalar = check_scalar()
    sources, rows, source_check = check_sources(templates, all_s2, relation, projection, start)
    colors, base_check = check_base(sources, rows, start)
    plan_check = check_plans(colors, start)
    declared = frozen["selected_cut_receiver_templates"]
    assert declared["complete"] == sum(partition["partition"].values())
    assert declared["h2_or_h4_s2"] == len(all_s2) and declared["finite_branch_at_least_one_strong"] == len(templates)
    assert declared["finite_branch_by_h"] == {str(h): partition["partition"][f"new_h{h}"] for h in (2, 4)}
    assert declared["finite_branch_by_h_m"] == {f"{h},{m}": n for (h, m), n in
        Counter((h, value[4]) for (h, _), value in templates.items()).items()}
    assert frozen["necessary_column_rows"] == dict(old=scalar["limited"], removed_by_complete_R41=16,
                                                    remaining=scalar["after_R41"])
    shapes = source_check["fiber_shapes"]
    assert frozen["fiber_bound"] == sum(row["fiber_choices"] for row in shapes.values())
    for field, metric in (("fiber_bounds_by_shape", "fiber_choices"), ("projected_Y_by_shape", "projected_Y")):
        assert frozen[field] == {name: row[metric] for name, row in shapes.items() if row[metric]}
    assert frozen["relaxed_labeled_pairs_upper_bound"] == sum(row["relaxed_pairs"] for row in shapes.values())
    assert frozen["source_counts"] == source_check["totals"]
    assert frozen["source_counts_by_h"] == {str(h): row for h, row in source_check["by_h"].items()}
    assert frozen["base_counts_by_h"] == {str(h): row for h, row in base_check["by_h"].items()}
    assert frozen["representatives"] == frozen["positive_plans"] == len(colors)
    assert frozen["first_failure"] is None and not frozen["exact_registered_targets"]
    assert frozen["accepted_R41_plan_count"] == 0
    assert plan_check["gates"] == frozen["plan_counts"] and plan_check["k3_donors"] == frozen["k3_donor_counts"]
    assert plan_check["controlled_modes"] == frozen["controlled_count_receiver_interfaces"]
    assert plan_check["controlled_parameters"] == frozen["controlled_count_rk"]
    assert plan_check["k4_receivers"] == frozen["k4_receiver_counts"]
    assert plan_check["k4_suppliers"] == frozen["k4_supplier_counts"]
    assert not any(frozen[k] for k in ("full_s2_proved", "full_mu3_proved", "full_E16_proved", "full_R7_proved"))
    guard(start)
    return dict(verdict="PASS", manifest_sha256=manifest_hash, manifest_entries=len(hashes),
                proof_sha256=digest(STEM + "CLOSURE.md"), direct_theorem_imports=imports, scalar=scalar,
                receivers=partition, sources=source_check, base=base_check, plans=plan_check,
                cpu_seconds=process_time()-start, cpu_limit=CPU_LIMIT, producers_run=0,
                searches_run=0, original_matchings_enumerated=0, solver_calls=0, rank_runs=0,
                old_rank_certificate_replays=0)


if __name__ == "__main__":
    start = process_time()
    try:
        result = main(start, sys.argv[1])
    except Exception:
        print(f"Independent check failed after {process_time()-start:.6f} CPU seconds.", file=sys.stderr)
        raise
    print(json.dumps(result, indent=2, ensure_ascii=True, sort_keys=True))
