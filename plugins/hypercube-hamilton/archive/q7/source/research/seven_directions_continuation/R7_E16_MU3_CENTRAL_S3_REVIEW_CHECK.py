"""Independent check of the frozen central s>=3 proof and local witnesses."""

from collections import Counter, defaultdict
from hashlib import sha256
from itertools import combinations, product
import json
from math import comb, prod
from pathlib import Path
import sys
from time import process_time

from R7_E16_MU3_CENTRAL_M3_REVIEW_CHECK import (
    ADJ, AXES, EVEN, ODD, USEFUL, action, coefficient, forbid_edge_assumption,
    loads, move, partitions, root_group, scalar_table,
)
from R7_E16_MU3_GAP6_EVEN_02_REVIEW_CHECK import whole_receiver_k3
from R7_E16_MU3_GAP7_EVEN_MINIMAL_REVIEW_CHECK import directed_cut, face, one_send, shape
from R7_E16_MU3_GAP7_ODD_REVIEW_CHECK import k4
from R41_M1_REVIEW_CHECK import registered, verify_original_cut


HERE = Path(__file__).resolve().parent
SIX = Path("E:/\u65b0\u95ee\u9898/research/six_directions")
STEM = "R7_E16_MU3_CENTRAL_S3_"
RECEIVERS = "E16_MU3_CENTRAL_LOCAL_RECEIVER.json"
OLD_ROWS = "R7_E16_MU3_CENTRAL_LOWM_PREFLIGHT_COUNT.json"
R41_CUTS = {(1, 4), (4, 1), (4, 7), (7, 4)}
CPU_LIMIT = 60


def digest(path):
    return sha256((HERE / path).read_bytes()).hexdigest()


def read(path):
    return json.loads((HERE / path).read_bytes())


def guard(start):
    if process_time() - start >= CPU_LIMIT:
        raise TimeoutError("central s>=3 independent CPU budget")


def bound_receipt(receipt, key, path):
    assert receipt[key][Path(path).name].removeprefix("sha256:") == digest(path), path


def check_scalar():
    previous, history = scalar_table()
    old = {(a, b, c, d) for (c, d), rows in previous.items() for a, b, _ in rows}
    frozen = read(OLD_ROWS)
    assert len(old) == 156
    saved = set()
    for row in frozen["allowed_a_b_gap"]:
        c, d = row["c"], row["d"]
        for a, b, gap in row["rows"]:
            assert gap == abs(a+c-b-d) and (a, b, c, d) not in saved
            saved.add((a, b, c, d))
    assert old == saved
    scalar = read("R7_E16_MU3_CENTRAL_AFTER_R41_SCALAR_NOTE.json")
    assert scalar["rows_before_sha256"] == sha256(
        json.dumps(sorted(old), separators=(",", ":")).encode()).hexdigest()
    removed = {row for row in old if (row[1] + row[3], row[0] + row[2]) in R41_CUTS}
    assert len(removed) == 16 and removed == set(map(tuple, scalar["removed_columns_abcd"]))
    assert Counter((b+d, a+c) for a, b, c, d in removed) == {
        (1, 4): 5, (4, 1): 3, (4, 7): 3, (7, 4): 5}
    allowed = old - removed
    assert len(allowed) == 140
    assert allowed == {(3-a, 6-b, 5-c, 2-d) for a, b, c, d in allowed}
    relation = defaultdict(set)
    projection = defaultdict(set)
    for a, b, c, d in allowed:
        relation[c, d, b].add(a)
        projection[c, d].add(b)
    assert projection == {(r["c"], r["d"]): set(r["b_after"]) for r in scalar["b_projections_by_cd"]}
    assert {cd: bs for cd, bs in projection.items() if cd[0]-cd[1] in (1, 2)} == {
        (1, 0): {0, 5, 6}, (2, 0): {0, 6}, (2, 1): {0, 5, 6},
        (3, 1): {0, 1, 6}, (3, 2): {0, 6}, (4, 2): {0, 1, 6}}
    return relation, projection, dict(history, after_R41=len(allowed))


def check_templates():
    stem = "R7_E16_MU3_R32_M_GE4_CLOSURE"
    old = read("R7_E16_MU3_R32_M_GE4_REVIEW.json")
    assert old["verdict"] == "PASS" and old["verification"]["basis"]["receiver_orbits"] == 704
    manifest = stem + "_INPUTS.json"
    for path in (stem + ".md", manifest):
        bound_receipt(old, "audited_input_hashes", path)
    assert read(manifest)["input_sha256"][HERE.joinpath(RECEIVERS).as_posix()] == digest(RECEIVERS)
    r41 = read("R41_FULL_REVIEW.json")
    assert r41["verdict"] == "PASS" and r41["full_R41_proved"]
    for name in ("R7_E16_MU3_CENTRAL_ANTIPODAL_REVIEW.json", "R7_E16_MU3_CENTRAL_M3_REVIEW.json"):
        assert read(name)["verdict"] == "PASS"

    templates, partition, seen = set(), Counter(), set()
    for row in read(RECEIVERS)["receivers"]:
        h, w = row["h"], tuple(row["W"])
        assert h in (2, 4, 6) and (h, w) not in seen
        seen.add((h, w))
        assert len(set(w)) == 5 and set(w) <= set(ODD) - (ADJ[0] | ADJ[(1 << h) - 1])
        cd = tuple(zip(loads(w), loads((0, (1 << h)-1))))
        m = sum(col in USEFUL for col in cd)
        s = sum(c-d in (1, 2) for c, d in cd)
        assert cd == tuple(map(tuple, row["loads_c_d"])) and m == row["m"] and m <= s
        if s < 3:
            partition["s_below_3"] += 1
        elif h == 6:
            partition["antipodal"] += 1
        elif m >= 3:
            partition["old_m_ge3"] += 1
        else:
            assert m == 2 and s == 3
            templates.add((h, w))
            partition[f"new_h{h}"] += 1
    assert len(seen) == 704
    assert partition == dict(s_below_3=334, antipodal=25, old_m_ge3=311, new_h2=32, new_h4=2)
    return templates, partition


def sources_from_fibers(w, choices, sparse):
    stats, modes, valid = Counter(), Counter(), set()
    mask = sum(1 << i for i in sparse)
    for column in product(*(sorted(choices[i]) for i in sparse)):
        flip = sum(1 << i for i, n in zip(sparse, column) if n > 3)
        active = tuple(1 << i for i, n in zip(sparse, column) if n in (1, 5))
        fibers = defaultdict(list)
        for v in set(ODD) - set(w):
            fibers[(v ^ flip) & mask].append(v)
        for parts in partitions(active):
            zeros = 6 - len(parts)
            if zeros > 4:
                continue
            if zeros == 3:
                mode = "three_zero_three_units"
            elif all(part.bit_count() == 1 for part in parts):
                mode = "four_zero_two_units"
            else:
                mode = "four_zero_unit_pair"
            bound = comb(len(fibers[0]), zeros) * prod(len(fibers[part]) for part in parts)
            modes[mode] += bound
            stats["positive_modes" if bound else "zero_modes"] += 1
            generated = 0
            for zero, others in product(combinations(fibers[0], zeros),
                                        product(*(fibers[part] for part in parts))):
                y = tuple(sorted(zero + others))
                b = loads(y)
                assert len(set(y)) == 6 and tuple(b[i] for i in sparse) == column
                generated += 1
                if all(value in opts for value, opts in zip(b, choices)):
                    assert y not in valid
                    valid.add(y)
            assert generated == bound
    return valid, modes, stats


def source_info(s, y, cd, relation):
    b = loads(y)
    pool = tuple(sorted(set(EVEN) - set(s) - set().union(*(ADJ[v] for v in y))))
    allowed = tuple(frozenset(relation[c, d, value]) for (c, d), value in zip(cd, b))
    return b, pool, allowed


def check_sources(templates, relation, projection, start):
    preflight = read(STEM + "PREFLIGHT.json")
    assert preflight["status"] == "complete" and preflight["first_missing_mode"] is None
    for path, expected in preflight["inputs_sha256"].items():
        assert digest(path) == expected, path
    group = {h: root_group(h) for h in (2, 4)}
    all_sources, totals, hist, shape_totals, mode_totals = {}, Counter(), defaultdict(Counter), Counter(), Counter()
    rooted = exchanged = 0
    for ti, row in enumerate(preflight["rows"]):
        guard(start)
        h, s, w = row["h"], tuple(row["S"]), tuple(row["W"])
        templates.remove((h, w))
        assert s == (0, (1 << h) - 1)
        cd = tuple(zip(loads(w), loads(s)))
        sparse = tuple(i for i, (c, d) in enumerate(cd) if c-d in (1, 2))
        assert len(sparse) == row["s"] == 3 and sum(col in USEFUL for col in cd) == row["m"] == 2
        assert row["complete"] and cd == tuple(map(tuple, row["loads_c_d"]))
        choices = tuple(projection[col] for col in cd)
        assert sparse == tuple(row["sparse_axes"]) and [sorted(choices[i]) for i in sparse] == row["sparse_allowed_b"]
        valid, modes, mode_counts = sources_from_fibers(w, choices, sparse)
        assert modes == row["fiber_bounds_by_mode"] and sum(modes.values()) == row["fiber_bound"]
        assert (mode_counts["zero_modes"], mode_counts["positive_modes"]) == (
            row["zero_bound_modes"], row["positive_bound_modes"])
        shape_totals.update(modes)
        mode_totals.update(mode_counts)
        subgroup = tuple(a for a in group[h] if move(w, a) == w)
        assert all(move(s, a) == s for a in subgroup)
        swap = sum(a[0] == s[1] for a in subgroup)
        assert (len(subgroup), swap) == (row["receiver_stabilizer_size"], row["receiver_stabilizer_root_exchange_count"])
        rooted += bool(swap)
        stats = Counter(raw_choices=sum(modes.values()), labeled_Y=len(valid))
        cache = {y: source_info(s, y, cd, relation) for y in valid}
        for si, record in enumerate(row["source_representatives"]):
            y = tuple(record["Y"])
            orbit = {move(y, a) for a in subgroup}
            assert y == min(orbit) and orbit <= valid
            valid.difference_update(orbit)
            b, pool, allowed = cache[y]
            assert list(b) == record["b_loads"] and list(pool) == record["U_pool"]
            assert [sorted(a) for a in allowed] == record["allowed_a"]
            n = coefficient(pool, allowed)
            assert n == record["exact_U"] and len(orbit) == record["source_orbit_size"]
            for tr in record["source_transport"]:
                member = tuple(tr["Y"])
                orbit.remove(member)
                perm, shift = tr["axis_destination"], tr["xor_after_permutation"]
                a = action(perm, shift)
                assert a in subgroup and move(member, a) == y
                old_b, old_pool, old_allowed = cache[member]
                assert move(old_pool, a) == pool
                for src, dst in enumerate(perm):
                    flipped = (shift >> dst) & 1
                    c, d = cd[src]
                    assert ((5-c, 2-d) if flipped else (c, d)) == cd[dst]
                    assert (6-old_b[src] if flipped else old_b[src]) == b[dst]
                    assert ({3-x for x in old_allowed[src]} if flipped else old_allowed[src]) == allowed[dst]
                exchanged += shift != 0
            assert not orbit
            common = tuple(a for a in subgroup if move(y, a) == y)
            all_sources[ti, si] = (h, s, w, y, pool, allowed, common, n, record["source_orbit_size"])
            stats.update(dict(source_orbits=1, source_orbits_with_U=bool(n),
                              labeled_Y_with_U=bool(n)*record["source_orbit_size"],
                              exact_U_on_source_reps=n, exact_labeled_Y_U=n*record["source_orbit_size"]))
        assert not valid and stats == Counter(row["counts"])
        hist[h].update(stats)
        totals.update(stats)
    assert not templates and totals == preflight["totals"]
    assert hist == {int(h): r for h, r in preflight["counts_by_h"].items()}
    assert totals == dict(raw_choices=7309, labeled_Y=2815, source_orbits=1842,
                          source_orbits_with_U=1178, labeled_Y_with_U=1785,
                          exact_U_on_source_reps=22233, exact_labeled_Y_U=30591)
    assert shape_totals == dict(four_zero_two_units=1626, four_zero_unit_pair=851, three_zero_three_units=4832)
    assert mode_totals == dict(positive_modes=248, zero_modes=60)
    assert (rooted, exchanged) == (15, 513)
    return all_sources, dict(totals=totals, by_h=hist, fiber_shapes=shape_totals, modes=mode_totals,
                             root_exchange_templates=rooted, root_exchange_transports=exchanged)


def check_base(sources, start):
    base = read(STEM + "BASE.json")
    assert base["status"] == "complete" and base["first_unfinished_source"] is None
    assert base["source_sha256"] == digest(STEM + "PREFLIGHT.json")
    records, colors, keys, seen = base["records"], [], set(), set()
    per_source, per_template, per_h = Counter(), defaultdict(Counter), defaultdict(Counter)
    assert len(records) == base["record_count"] == 18049
    for index, record in enumerate(records):
        if index % 512 == 0:
            guard(start)
        ti, si = key = record["template_index"], record["source_index"]
        h, s, w, y, pool, allowed, common, n, _ = sources[key]
        u = tuple(record["U"])
        assert n > 0 and (key, u) not in keys and len(set(u)) == 3 and set(u) <= set(pool)
        keys.add((key, u))
        assert u == min(move(u, a) for a in common)
        assert record["common_stabilizer_size"] == len(common)
        assert (h, s, w, y, 2, 3) == (record["h"], tuple(record["S"]), tuple(record["W"]),
                                      tuple(record["Y"]), record["m"], record["s"])
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
        h, s, w, y, pool, allowed, common, _, orbit_size = sources[key]
        a = action(tr["axis_destination"], tr["xor_after_permutation"])
        assert a in common and move(u, a) == tuple(row["U"])
        assert move(pool, a) == pool and len(u) == 3 and set(u) <= set(pool)
        assert all(value in opts for value, opts in zip(loads(u), allowed))
        assert all(value in opts for value, opts in zip(loads(row["U"]), allowed))
        per_source[key] += 1
        per_template[key[0]].update(completions=1, labeled_Y_U=orbit_size)
    assert len(seen) == base["qualified_completions"] == 22233 and keys <= seen
    for (ti, si), (_, _, _, _, _, _, _, n, _) in sources.items():
        assert per_source[ti, si] == n
        per_template[ti]["positive_sources"] += bool(n)
    assert len(base["summaries"]) == len(per_template) == 34
    preflight_rows = read(STEM + "PREFLIGHT.json")["rows"]
    for ti, summary in enumerate(base["summaries"]):
        assert (summary["h"], summary["W"]) == (preflight_rows[ti]["h"], preflight_rows[ti]["W"])
        assert per_template[ti] == Counter(summary["counts"])
        per_h[summary["h"]].update(per_template[ti])
    assert per_h == {int(h): row for h, row in base["counts_by_h"].items()}
    assert {h: stat["representatives"] for h, stat in per_h.items()} == {2: 17460, 4: 589}
    assert sum(stat["labeled_Y_U"] for stat in per_h.values()) == base["labeled_Y_U"] == 30591
    assert all(base[k] == 0 for k in ("plans", "original_matchings_enumerated", "solver_calls", "rank_runs"))
    return colors, dict(representatives=len(records), transports=len(seen), by_h=per_h)


def check_t63_import():
    stem = "R7_MU3_T63_NEW_RANK"
    inputs, proof, evidence = stem + "_INPUTS.json", stem + ".md", stem + "_REVIEW_CHECK.json"
    receipt = read("R7_MU3_CONTROLLED_AND_T63_REVIEW.json")
    assert receipt["verdict"] == "PASS" and receipt["proof_status"] == "sound-modulo-imports"
    for path in (inputs, proof, "R7_CONTROLLED_CYCLE_DONOR_TRANSFER.md",
                 "R7_CONTROLLED_CYCLE_DONOR_TRANSFER_INPUTS.json"):
        bound_receipt(receipt, "audited_input_hashes", path)
    bound_receipt(receipt, "evidence_hashes", evidence)
    check = read(evidence)
    assert (check["inputs_sha256"], check["proof_sha256"]) == (digest(inputs), digest(proof))
    imported = read(inputs)
    batch = stem + "_MANIFEST.json"
    assert imported["bindings_sha256"][batch] == digest(batch)
    target, = (r for r in imported["targets"] if r["target_class"] == 4)
    batch_record, = (r for r in read(batch)["targets"] if r["target_class"] == 4)
    verified, = (r for r in check["verified"] if r["target_class"] == 4)
    manifest = Path(target["manifest_path"])
    cert = read(manifest)
    assert digest(manifest) == target["manifest_sha256"] == batch_record["manifest_sha256"]
    assert batch_record["manifest_path"] == target["manifest_path"]
    assert cert["rank_GF2"] == batch_record["rank_GF2"] == 4096 and cert["target_class"] == 4
    assert verified["verifier"] == "PASS forests=4096 columns=4096 bits=16777216 rank=4096"
    geometry = (target["H"], target["U"])
    assert geometry == (cert["H"], cert["U"]) == (verified["H"], verified["U"]) == (
        [0, 3, 5, 10, 15, 20], [0, 5, 20])
    assert "0,3,5,10,15,20 | 0,5,20" in (HERE / proof).read_text(encoding="utf8")
    for entry in cert["artifacts"]:
        artifact = HERE / manifest.parent / entry["name"]
        assert artifact.stat().st_size == entry["bytes"] and digest(artifact) == entry["sha256"]
    q5 = SIX / "Q5_A10_FULL_REVIEW.json"
    assert read(q5)["verdict"] == "PASS"
    return {4: tuple(map(set, geometry))}, dict(
        target_class=4, H=geometry[0], U=geometry[1], imported_rank=4096,
        proof_sha256=digest(proof), inputs_sha256=digest(inputs),
        independent_result_sha256=digest(evidence), rank_manifest_sha256=digest(manifest),
        audited_receipt_sha256=digest("R7_MU3_CONTROLLED_AND_T63_REVIEW.json"), q5_a_all_receipt_sha256=digest(q5))


def check_plans(colors, new63, start):
    data = read(STEM + "FIXED_PLANS.json")
    assert data["base_sha256"] == digest(STEM + "BASE.json")
    assert data["status"] == "complete" and data["first_failure"] is None
    assert len(data["positives"]) == data["visited"] == data["input_representatives"] == len(colors)
    assert all(data[k] == 0 for k in ("unvisited", "new_geometries", "original_matchings_enumerated",
                                     "solver_calls", "rank_runs"))
    for path, expected in data["accepted_receipts_sha256"].items():
        assert digest(path) == expected and read(path)["verdict"] == "PASS"
    seen, exact = set(), {}
    gates, donors, cores, controlled, parameters, k4_suppliers, k4_receivers, reg_counts = (Counter() for _ in range(8))
    ranks = defaultdict(Counter)
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
            if gate in ("accepted_central_m_ge3", "accepted_central_antipodal_h6"):
                witness = p["witness"] if gate == "accepted_central_m_ge3" else p
                j, a, b = directed_cut(colors[index], witness, "donor_side")
                verify_original_cut(a, b, witness, [[3, 6], [5, 2]])
                if gate == "accepted_central_m_ge3":
                    cd = [[i, [len(face(g, i, 1)) for g in b]] for i in range(7) if i != j]
                    usable = [i for i, counts in cd if tuple(counts) in USEFUL]
                    assert cd == witness["inner_loads"] and usable == witness["usable"] and len(usable) >= 3
                else:
                    u, v = b[1]
                    assert (u ^ v).bit_count() == witness["h"] == 6
                continue
            j, a, b = directed_cut(colors[index], p, "donor_side" if gate in {
                "four_mono_capacity", "controlled_cycle_registered_split"} else "A_side")
            if gate == "controlled_cycle_count":
                one_send(p, j, a, b, controlled)
                parameters[f"{p['r']},{p['k']}"] += 1
            elif gate == "controlled_cycle_registered_split":
                registered(p, j, a, b, {}, new63, reg_counts, ranks)
                assert (p["r"], p["k"], j, p["donor_side"], p["alpha_parity"]) == (3, 4, 4, 0, 0)
                assert p["sources"] == [2, 32, 64, 67] and p["marks"] == [18, 48, 80, 83]
                spec = p["receiver"]
                assert spec["inner"] == 5 and spec["projected_axes"] == [0, 1, 2, 3, 6]
                first, second = spec["faces"]
                assert (first["minority"], first["majority"], first["marks"]) == (
                    [], [2, 16, 19, 21, 28, 31], [2, 16, 19])
                assert first["interface"] == dict(kind="T63_new", rank=4, local_to_rank_xor=16,
                                                   local_to_rank_permutation=[0, 2, 1, 3, 4])
                assert second["minority"] == [2] and second["marks"] == [0] and second["interface"]["kind"] == "Q5_A_ALL"
                exact[index] = second["majority"]
            elif gate == "k3_whole_receiver":
                whole_receiver_k3(p, j, a, b, {}, cores)
                donors[p["donor"]["kind"]] += 1
            elif gate == "four_mono_capacity":
                verify_original_cut(a, b, p, [[4, 8], [4, 0]])
                split = [i for i in range(7) if i != j and len(face(b[0], i, 1)) == 2]
                assert split == p["split_axes"] and len(a[1]) > {3: 7, 4: 6, 5: 6, 6: 7}[len(split)]
            else:
                assert gate == "k4_two_return"
                supplier, mode, kind = k4(p, j, a, b, {}, k4_suppliers)
                assert supplier in ("majority_root", "two_minority_roots")
                if mode == "controlled_single_root":
                    assert p["receiver"]["a"] in b[1] and p["receiver"]["w"] not in set.union(*a, *b) | set(p["Y"])
                k4_receivers[f"{mode}:{kind}" if kind is not None else mode] += 1
        except (AssertionError, KeyError, ValueError) as exc:
            raise AssertionError((index, gate)) from exc
    assert seen == set(range(18049))
    assert gates == data["plan_counts"] == dict(
        accepted_central_m_ge3=6279, accepted_central_antipodal_h6=137, four_mono_capacity=3,
        controlled_cycle_count=7714, controlled_cycle_registered_split=2, k3_whole_receiver=3862,
        k4_two_return=52)
    assert donors == data["k3_donor_counts"] == dict(
        Q6_same_side_majority_root=2412, Q6_balanced_complement_avoid_two=931,
        T26_separated_two_root_choice=375, T26_two_majority_roots=139, Q6_T26_paired_S1=5)
    assert not cores and exact == {11961: [0, 5, 30], 11962: [0, 9, 30]}
    assert reg_counts == {"Q5_A_ALL": 2, "T63_new": 2} and ranks == {"T63_new": {4: 2}}
    return dict(gates=gates, controlled_modes=controlled, controlled_parameters=parameters,
                registered_modes=reg_counts, registered_other_majority=exact, k3_donors=donors, k3_cores=cores,
                k4_suppliers={":".join(k): v for k, v in k4_suppliers.items()}, k4_receivers=k4_receivers)


def main(start, manifest_hash):
    assert __debug__
    manifest = STEM + "CLOSURE_INPUTS.json"
    assert digest(manifest) == manifest_hash
    frozen = read(manifest)
    hashes = frozen["sha256"]
    for path, expected in hashes.items():
        assert digest(path) == expected.removeprefix("sha256:"), path
    required = {STEM + name for name in ("CLOSURE.md", "PREFLIGHT.json", "BASE.json", "FIXED_PLANS.json")}
    assert required <= {Path(path).name for path in hashes}
    templates, partition = check_templates()
    relation, projection, scalar = check_scalar()
    sources, source_check = check_sources(templates, relation, projection, start)
    colors, base_check = check_base(sources, start)
    t63, rank4 = check_t63_import()
    plan_check = check_plans(colors, t63, start)
    assert plan_check["gates"] == frozen["plan_counts"] and plan_check["k3_donors"] == frozen["k3_donor_counts"]
    assert plan_check["controlled_modes"] == frozen["controlled_count_receiver_interfaces"]
    assert plan_check["controlled_parameters"] == frozen["controlled_count_rk"]
    assert plan_check["k4_receivers"] == frozen["k4_receiver_counts"]
    suppliers = Counter()
    for label, n in plan_check["k4_suppliers"].items():
        suppliers[label.split(":")[0]] += n
    assert suppliers == frozen["k4_supplier_counts"]
    assert not any(frozen[k] for k in ("full_mu3_proved", "full_E16_proved", "full_R7_proved"))
    guard(start)
    return dict(verdict="PASS", manifest_sha256=manifest_hash, manifest_entries=len(hashes),
                proof_sha256=digest(STEM + "CLOSURE.md"), scalar=scalar, receivers=partition, sources=source_check,
                base=base_check, plans=plan_check, T63_import=rank4, cpu_seconds=process_time()-start,
                cpu_limit=CPU_LIMIT, producers_run=0, searches_run=0, original_matchings_enumerated=0,
                solver_calls=0, rank_runs=0)


if __name__ == "__main__":
    start = process_time()
    try:
        result = main(start, sys.argv[1])
    except Exception:
        print(f"Independent check failed after {process_time()-start:.6f} CPU seconds.", file=sys.stderr)
        raise
    print(json.dumps(result, indent=2, ensure_ascii=True, sort_keys=True))
