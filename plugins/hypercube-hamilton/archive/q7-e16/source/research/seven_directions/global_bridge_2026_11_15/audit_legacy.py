"""Certify the extent of the frozen legacy menu certificates without rediscovery."""
from collections import Counter, defaultdict
from hashlib import sha256
import json
from pathlib import Path
import sys
from time import process_time

from audit_geometry import HERE, fixed_basis, loads, proof_geometry

sys.path.append(str(HERE.parent))
from R7_E16_MU3_CENTRAL_M3_REVIEW_CHECK import exact_registry, forbid_edge_assumption
from R7_E16_MU3_GAP6_EVEN_02_REVIEW_CHECK import whole_receiver_k3
from R7_E16_MU3_GAP7_EVEN_MINIMAL_REVIEW_CHECK import directed_cut, face, one_send, shape
from R7_E16_MU3_GAP7_ODD_REVIEW_CHECK import actual_returns, double_omit, k4, project, permuted, split_shape
from R41_M1_REVIEW_CHECK import registered


def accepted_t63():
    root = HERE.parent
    receipt = json.loads((root / "R7_MU3_CONTROLLED_AND_T63_REVIEW.json").read_bytes())
    assert receipt["verdict"] == "PASS"
    paths = ("R7_MU3_T63_NEW_RANK_INPUTS.json", "R7_MU3_T63_NEW_RANK_REVIEW_CHECK.json")
    for path, field in zip(paths, ("audited_input_hashes", "evidence_hashes")):
        assert receipt[field][path] == "sha256:" + sha256((root / path).read_bytes()).hexdigest()
    inputs, evidence = (json.loads((root / path).read_bytes()) for path in paths)
    def targets(rows):
        return {row["target_class"]: (set(row["H"]), set(row["U"])) for row in rows}
    by_rank = targets(inputs["targets"])
    assert by_rank == targets(evidence["verified"])
    assert set(by_rank) == set(range(1, 7))
    return by_rank


def broad_receiver(spec, outer, minority, majority, marks, new63, stats):
    inner = spec["inner"]
    assert inner in range(7) and inner != outer
    axes = [i for i in range(7) if i not in (outer, inner)]
    assert spec["projected_axes"] == axes and len(spec["faces"]) == 2
    for side, row in enumerate(spec["faces"]):
        n, m, z = (project(face(g, inner, side), axes) for g in (minority, majority, marks))
        assert (n, m, z) == tuple(row[k] for k in ("minority", "majority", "marks"))
        n, m, z = set(n), set(m), set(z)
        assert n.isdisjoint(m) and z <= m and z and len(m)-len(n) == 2*len(z)
        iface = row["interface"]
        if iface["kind"] != "T63_new":
            split_shape(n, m, z, len(z), iface["kind"])
            continue
        assert not n and len(m) == 6 and len(z) == 3
        rank, shift, perm = (iface[k] for k in ("rank", "local_to_rank_xor", "local_to_rank_permutation"))
        assert shift in range(32) and sorted(perm) == list(range(5))
        assert tuple({permuted(v ^ shift, perm) for v in group} for group in (m, z)) == new63[rank]
        stats["broad_t63"][rank] += 1


def replay(colors, plan, registry, new63, stats):
    forbid_edge_assumption(plan)
    gate = plan["gate"]
    holes = set.union(*colors)
    if gate == "impossible_geometry":
        data = plan["exclusion"]
        v = data["vertex"]
        assert data["gate"] == "impossible_isolated_covered_vertex" and 0 <= v < 128
        assert v not in holes and {v ^ (1 << i) for i in range(7)} <= holes
        return
    if gate == "registry_two_return":
        j, a, b = directed_cut(colors, dict(plan, alpha_parity=1-plan["donor_majority_parity"]), "donor_side")
        k = plan["k"]
        assert 4 <= k <= 8 and plan["required_forced_edge"] is None
        retained, v, rb, y = actual_returns(plan, j, a, b, k)
        groups = (a[0], retained, v, b[1], rb, y)
        names = ("donor_minority", "donor_retained", "donor_marks",
                 "receiver_minority", "receiver_retained", "receiver_marks")
        for group, name in zip(groups, names):
            assert sorted(group) == plan[name]
        double_omit(plan["donor"], a[0], retained | v, v, j, registry, stats["registry_cores"])
        receiver = plan["receiver"]
        assert receiver["kind"] == "positive_split_Q5"
        broad_receiver(receiver, j, b[1], rb | y, y, new63, stats)
        assert all(row["marks"] for row in receiver["faces"])
        stats["broad"][(k, plan["donor"]["kind"], tuple(row["interface"]["kind"]
                                                     for row in receiver["faces"]))] += 1
        return
    if gate in ("k3_whole_receiver", "k4_two_return", "controlled_cycle_count"):
        j, a, b = directed_cut(colors, plan, "A_side")
        if gate == "k3_whole_receiver":
            whole_receiver_k3(plan, j, a, b, registry, stats["k3_cores"])
            stats["k3_donors"][plan["donor"]["kind"]] += 1
        elif gate == "k4_two_return":
            _, mode, kind = k4(plan, j, a, b, registry, stats["k4_suppliers"])
            if mode == "controlled_single_root":
                receiver = plan["receiver"]
                assert receiver["a"] in b[1] and receiver["w"] not in holes | set(plan["Y"])
            stats["k4_receivers"][(mode, kind)] += 1
        else:
            one_send(plan, j, a, b, stats["controlled"])
        return
    if gate == "controlled_cycle_registered_split":
        j, a, b = directed_cut(colors, plan, "donor_side")
        assert len(b[1]) <= 5
        registered(plan, j, a, b, {}, new63, stats["registered"], stats["registered_ranks"])
        return
    if gate == "four_mono_capacity":
        j, a, b = directed_cut(colors, plan, "donor_side")
        assert shape(a, b) == plan["shape"] == [[4, 8], [4, 0]]
        assert list(map(sorted, a)) == plan["original_A_by_alpha_beta"]
        assert list(map(sorted, b)) == plan["original_B_by_alpha_beta"]
        axes = [i for i in range(7) if i != j and len(face(b[0], i, 1)) == 2]
        assert axes == plan["split_axes"] and len(a[1]) > {3: 7, 4: 6, 5: 6, 6: 7}[len(axes)]
        return
    # Geometry gates require no separate bridge witnesses.
    if gate in ("gap7", "gap8"):
        i = plan["axis"]
        gap = loads(colors[0], 7)[i] - loads(colors[1], 7)[i]
        assert gap == plan["delta"] and abs(gap) == int(gate[-1])
        return
    if gate in ("monochromatic_three", "R41", "central_h6", "central_s3", "central_s2_strong"):
        axis, side = plan["axis"], plan["B_side"]
        face_colors = tuple(face(g, axis, side) for g in colors)
        counts = tuple(map(len, face_colors))
        if gate in ("monochromatic_three", "R41"):
            assert counts == tuple(plan["B_counts_even_odd"])
            assert sorted(counts) == ([0, 3] if gate == "monochromatic_three" else [1, 4])
            return
        alpha = plan["alpha"]
        majority, minority = face_colors[alpha], face_colors[1-alpha]
        assert (len(majority), len(minority)) == (5, 2)
        assert (set(plan["W"]), set(plan["S"])) == (majority, minority)
        u, v = minority
        assert (u ^ v).bit_count() == plan["h"]
        cd = {i: (len(face(majority, i, 1)), len(face(minority, i, 1)))
              for i in range(7) if i != axis}
        assert cd == {int(i): tuple(pair) for i, pair in plan["B_bit_one_loads"].items()}
        s = sum(c-d in (1, 2) for c, d in cd.values())
        assert s == plan["s"]
        if gate == "central_h6":
            assert plan["h"] == 6
        elif gate == "central_s3":
            assert s >= 3
        else:
            assert s >= 2 and set(cd.values()) & {(2, 0), (3, 2)}
        return
    raise ValueError(f"Unaudited gate in this checker: {gate}")


def run(filename):
    start = process_time()
    scalar, _, first, _, _ = fixed_basis()
    certificate = HERE / filename
    raw = certificate.read_bytes()
    data = json.loads(raw)
    registry = exact_registry()
    new63 = accepted_t63()
    assert registry[117] == [[31, 61, 62], [1, 2]]
    seen = set()
    actual_by_source = Counter()
    actual_by_b = Counter()
    gates, axes, controlled_parameters = Counter(), Counter(), Counter()
    stats = {name: Counter() for name in ("registry_cores", "broad", "k3_cores", "k3_donors",
                                          "k4_suppliers", "k4_receivers", "controlled", "broad_t63", "registered")}
    stats["registered_ranks"] = defaultdict(Counter)
    for entry in data["positives"]:
        u, y = tuple(entry["Z"]), tuple(entry["Y"])
        try:
            assert (y, u) not in seen and first[y] > 0
            seen.add((y, u))
            actual_by_source[y] += 1
            assert tuple(entry["a"]) == loads(u) and tuple(entry["b"]) == loads(y)
            actual_by_b[loads(y)] += 1
            colors = proof_geometry(scalar, y, u)
            assert colors == tuple(map(set, (entry["even"], entry["odd"])))
            assert [x-y for x, y in zip(loads(colors[0], 7), loads(colors[1], 7))] == entry["deltas"]
            replay(colors, entry["plan"], registry, new63, stats)
            plan = entry["plan"]
            gate = plan["gate"]
            axes[plan.get("outer", plan.get("axis"))] += 1
            if plan.get("outer", plan.get("axis")) == 6:
                assert gate == "k3_whole_receiver"
                assert (plan["A_side"], plan["alpha_parity"]) == (1, 1)
            if gate == "controlled_cycle_count":
                controlled_parameters[(plan["r"], plan["k"])] += 1
            gates[gate] += 1
        except (AssertionError, KeyError, ValueError) as error:
            raise AssertionError(f"certificate {y}, {u}, {entry['plan']['gate']}") from error
        assert process_time()-start < 30
    assert all(n <= first[y] for y, n in actual_by_source.items())
    full = data["failure"] is None and len(seen) == data["candidate_limit"] == sum(first.values())
    if full:
        assert actual_by_source == Counter({y: n for y, n in first.items() if n})
        assert actual_by_b == Counter({tuple(b): n for b, n in data["checked_by_b"]})
        assert data["candidate_count"] == len(seen)
        assert gates == data["plan_counts"] and axes[6] == 452
        assert controlled_parameters == {(3,3): 52, (3,4): 356, (4,4): 6}
        for relative_path, digest in data["input_SHA256"].items():
            assert sha256((HERE.parent / relative_path).read_bytes()).hexdigest() == digest
        assert data["inherited_prefix_SHA256"] == sha256((HERE / "EXCEPTION_LEGACY_FULL.json").read_bytes()).hexdigest()
    assert not data["original_matchings_enumerated"] and not data["solver_calls"]
    return {
        "certificate_file": filename,
        "certificate_sha256": sha256(raw).hexdigest(),
        "basis_certified": full,
        "certificates_replayed": len(seen),
        "expected_basis_count": sum(first.values()),
        "gates_certified": gates,
        "witness_outer_axes": axes,
        "controlled_parameters": {repr(k): n for k, n in controlled_parameters.items()},
        "full_registry_kinds": {repr(k): n for k, n in stats["broad"].items()},
        "registry_cores": stats["registry_cores"],
        "registry_t63": stats["broad_t63"],
        "controlled_t63": stats["registered_ranks"],
        "non_registry_k3_donors": stats["k3_donors"],
        "k4_supplier_receiver": {repr(k): n for k, n in stats["k4_suppliers"].items()},
        "k4_receivers": {repr(k): n for k, n in stats["k4_receivers"].items()},
        "elapsed_CPU_seconds": process_time()-start,
    }


if __name__ == "__main__":
    print(json.dumps(run(sys.argv[1]), indent=2))
