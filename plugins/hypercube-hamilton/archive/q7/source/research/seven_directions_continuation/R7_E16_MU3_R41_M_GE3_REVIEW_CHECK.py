"""Independent bounded checker of the frozen reduction and fixed certificates."""

from collections import Counter
from hashlib import sha256
from itertools import combinations, permutations, product
from math import comb
from pathlib import Path
from time import process_time
import json
import re


ROOT = Path(__file__).resolve().parent
SUBMISSION = "R7_E16_MU3_R41_M_GE3_CLOSURE"
BASIS = "E16_MU3_ROUTE_R41_M3_"
SIX = Path("E:/\u65b0\u95ee\u9898/research/six_directions")
AXES = tuple(range(6))
ODD = {v for v in range(64) if v.bit_count() % 2}
EVEN = set(range(64)) - ODD
START = process_time()


def budget():
    if process_time() - START >= 30:
        raise TimeoutError("30 CPU second audit limit")


def read(path):
    return json.loads((ROOT / path).read_bytes())


def bit(v, i):
    return (v >> i) & 1


def project(v, axes):
    return sum(bit(v, i) << j for j, i in enumerate(axes))


def permute(v, permutation):
    return sum(bit(v, i) << j for i, j in enumerate(permutation))


def loads(points, axes=AXES):
    return tuple(sum(bit(v, i) for v in points) for i in axes)


def scalar_table():
    def covered(blocks, mono):
        for direction, beta in product(range(2), repeat=2):
            donor, receiver = blocks[direction], blocks[1 - direction]
            alpha = 1 - beta
            r, major = (sum(piece[c] for piece in donor) for c in (alpha, beta))
            if major - r not in (3, 4):
                continue
            if mono and (r, major) == (5, 8) and sum(piece[beta] for piece in receiver) == 0:
                return True
            if r <= 5 and all(
                (gap := target[alpha] - target[beta]) in (1, 2)
                and source[beta] >= gap
                and (gap == 1 or target[beta] <= 1)
                for source, target in zip(donor, receiver)
            ):
                return True
        return False

    def table(totals):
        sizes = Counter()
        accepted = set()
        for row in product(*(range(t + 1) for t in totals)):
            sizes["raw"] += 1
            a, b, c, d = row
            if abs(a + c - b - d) < 3:
                continue
            sizes["gap"] += 1
            e, f, g, h = (t - x for t, x in zip(totals, row))
            if covered((((e, f), (a, b)), ((g, h), (c, d))), False):
                continue
            sizes["original"] += 1
            if covered((((e, f), (g, h)), ((a, b), (c, d))), True):
                continue
            accepted.add(row)
        return sizes, accepted

    counts, allowed = table((4, 7, 4, 1))
    other, other_allowed = table((3, 6, 5, 2))
    assert (counts, len(allowed)) == (dict(raw=400, gap=178, original=154), 140)
    assert (other, len(other_allowed)) == (dict(raw=504, gap=212, original=204), 166)
    return allowed


def check_basis():
    allowed = scalar_table()
    actions = tuple(tuple(permute(v, p) for v in range(64)) for p in permutations(AXES))

    def image(points, action):
        return tuple(sorted(action[v] for v in points))

    def canonical_frame(points):
        # Construct the author's frame for comparison, independently of orbit generation.
        signature = min(tuple(sorted(sum(bit(v, i) << row for row, v in enumerate(ordered))
                                     for i in AXES))
                        for ordered in permutations(points))
        return tuple(sorted(sum(bit(c, row) << i for i, c in enumerate(signature))
                            for row in range(4)))

    unseen = set(combinations(sorted(ODD - {1 << i for i in AXES}), 4))
    assert len(unseen) == 14950
    hist, frames = Counter(), {}
    while unseen:
        w = min(unseen)
        orbit = {image(w, action) for action in actions}
        assert orbit <= unseen
        unseen.difference_update(orbit)
        frame = canonical_frame(w)
        assert frame in orbit
        count = sum(c in (1, 2) for c in loads(frame))
        hist[count] += 1
        if count == 3:
            assert frame not in frames
            frames[frame] = tuple(a for a in actions if image(frame, a) == frame)
    assert hist == dict(enumerate((3, 4, 12, 18, 18, 6, 2)))

    sources = read(BASIS + "SOURCE_BASE.json")["source_rows"]
    by_geometry = {(tuple(row["receiver_majority"]), tuple(row["source_mirrors"])): index
                   for index, row in enumerate(sources)}
    assert len(by_geometry) == len(sources) == 317
    source_counts, reduced_sizes, totals = Counter(), Counter(), Counter()
    expected = {}
    for w, stabilizer in frames.items():
        budget()
        c = loads(w)
        use = tuple(i for i in AXES if c[i] in (1, 2))
        flip = sum(1 << n for n, i in enumerate(use) if c[i] == 1)
        fibers = [tuple(v for v in ODD if project(v, use) ^ flip == k) for k in (0, 1, 2, 4)]
        assert [len(f) for f in fibers] == [4] * 4
        for selected in product(*fibers[1:]):
            source_counts["raw"] += 1
            y = tuple(sorted((*fibers[0], *selected)))
            if set(w) & set(y):
                source_counts["overlap"] += 1
                continue
            b = loads(y)
            column = tuple({a for a in range(5) if (a, u, v, 0) in allowed} for u, v in zip(b, c))
            if not all(column):
                source_counts["column"] += 1
                continue
            index = by_geometry.pop((w, y))
            row = sources[index]
            pool = {v for v in EVEN - {0} if all((v ^ p).bit_count() != 1 for p in y)}
            assert list(b) == row["source_loads"] and list(c) == row["receiver_loads"]
            assert [sorted(g) for g in column] == row["allowed_donor_minority_loads"]
            assert sorted(pool) == row["donor_minority_pool"]
            totals["initial_bound"] += comb(len(pool), 4)

            def feasible_loads():
                return tuple({n for n in g if n <= ones and 4 - n <= len(pool) - ones}
                             for g, ones in zip(column, loads(pool)))

            feasible = feasible_loads()
            assert row["pool_compatible_loads"] == [sorted(g) for g in feasible]
            assert row["pool_compatible"] == all(feasible)
            while all(feasible):
                reduced = {v for v in pool if all(g != {0} or not bit(v, i)
                                                 for i, g in enumerate(feasible))
                           and all(g != {4} or bit(v, i) for i, g in enumerate(feasible))}
                if reduced == pool:
                    break
                pool = reduced
                feasible = feasible_loads()
            if not all(feasible):
                pool = set()
            reduced_sizes[len(pool)] += 1
            totals["reduced_bound"] += comb(len(pool), 4)
            good = {u for u in combinations(sorted(pool), 4)
                    if all(n in g for n, g in zip(loads(u), column))}
            totals["valid_U"] += len(good)
            group = tuple(a for a in stabilizer if image(y, a) == y)
            while good:
                u = min(good)
                orbit = {image(u, a) for a in group}
                assert orbit <= good
                good.difference_update(orbit)
                colors = ((0, *(v ^ 64 for v in y)), (*w, *(v ^ 64 for v in u)))
                assert all(len(set(g)) == 8 and all(v.bit_count() % 2 == n for v in g)
                           for n, g in enumerate(colors))
                assert all((v ^ p).bit_count() != 1 for v, p in product(*colors))
                gaps = tuple(a - b for a, b in zip(*(loads(g, range(7)) for g in colors)))
                assert gaps[6] == min(map(abs, gaps)) == 3
                expected[index, u] = len(group), colors, gaps
    assert not by_geometry
    assert source_counts == dict(raw=1152, overlap=710, column=125)
    assert reduced_sizes == {0: 110, 5: 138, 9: 6, 10: 46, 11: 15, 13: 2}
    assert totals == dict(initial_bound=82292, reduced_bound=17486, valid_U=4468)
    assert len(expected) == 3785
    completion = read(BASIS + "COMPLETION_BASE.json")
    assert completion["summary"]["status"] == "complete"
    rows = []
    for row in completion["representatives"]:
        group, colors, gaps = expected.pop((row["source_row"], tuple(row["donor_minority"])))
        assert group == row["common_stabilizer_size"]
        assert colors == (tuple(row["even_holes"]), tuple(row["odd_holes"]))
        assert gaps == tuple(row["bit_one_even_minus_odd"])
        rows.append(colors)
    assert not expected and len(set(rows)) == 3785
    return rows, dict(orbits_by_m=hist, source_counts=source_counts, source_rows=317,
                      refined_sizes=reduced_sizes, **totals, representatives=len(rows))


def ranked_targets(path, pattern):
    return {int(k): tuple(set(map(int, g.split(","))) for g in groups)
            for k, *groups in re.findall(pattern, path.read_text(encoding="utf8"), re.M)}


def check_plans(rows, bound):
    plans = read(BASIS + "FIXED_PLANS.json")
    assert plans["base_sha256"] == bound[str(ROOT / (BASIS + "COMPLETION_BASE.json")).replace("\\", "/")]
    assert plans["status"] == "complete" and not plans["unvisited"] and plans["first_failure"] is None
    assert plans["visited"] == plans["input_representatives"] == len(rows)
    assert all(not plans[k] for k in ("original_matchings_enumerated", "solver_calls", "rank_runs",
                                     "new_geometries", "nested_T63_separate_gate"))
    t26 = ranked_targets(SIX / "Q5_T26_RANK_BATCH_PROOF.md",
                         r"^\| (\d+) \| ([\d,]+) \| ([\d,]+) \| ([\d,]+) \|")
    old63 = ranked_targets(SIX / "Q5_T63_RANK_PROOF.md", r"^\|(\d+)\|([\d,]+)\|([\d,]+)\|$")
    new63 = ranked_targets(ROOT / "R7_MU3_T63_NEW_RANK.md",
                           r"^\| (\d+) \| ([\d,]+) \| ([\d,]+) \| [\d,]+ \|")
    assert set(t26) == set(range(55)) and set(old63) == set(range(7)) and set(new63) == set(range(1, 7))
    gate_counts, count_tools, registered_tools, return_tools = (Counter() for _ in range(4))
    ranks = {"Q5_T26_RANK": set(), "T63_old": set(), "T63_new": set()}
    witnesses = []

    def side(points, i, b):
        assert i in range(7) and b in (0, 1)
        return {v for v in points if bit(v, i) == b}

    def split(groups, i, b):
        return tuple(side(g, i, b) for g in groups)

    def arrays(*groups):
        return [sorted(g) for g in groups]

    def sizes(groups):
        return list(map(len, groups))

    def marked_local(old, marks, kind):
        small, large = sizes(old)
        q = len(marks)
        assert not marks & (old[0] | old[1])
        assert large - small == q
        if kind == "Q5_A_ALL":
            assert q == 1 and 0 <= small <= 14
        elif kind == "Q5_T44":
            assert q == 2 and small == 0
        else:
            assert kind == "Q5_T15_FULL" and q == 2 and small == 1

    def recorded_edges(value):
        if isinstance(value, dict):
            for key, item in value.items():
                assert "edge" not in key, key
                recorded_edges(item)
        elif isinstance(value, list):
            for item in value:
                recorded_edges(item)

    def majority_root(groups, marks, spec, outer):
        axis, b = spec["inner"], spec["mark_side"]
        assert spec["kind"] == "majority_root" and axis != outer
        assert len(marks) == 2 and marks <= side(groups[1], axis, b)
        actual = [sizes(split(groups, axis, t)) for t in (b, 1 - b)]
        assert actual == spec["hole_counts"]
        (a, c), (d, e) = actual
        assert a in (0, 1) and c == a + 5 and 1 <= d <= 16 and e == d - 1

    seen = set()
    for entry in plans["positives"]:
        budget()
        index, p = entry["index"], entry["plan"]
        assert index in range(len(rows)) and index not in seen
        seen.add(index)
        g = p["gate"]
        recorded_edges(p)
        gate_counts[g] += 1
        colors = tuple(map(set, rows[index]))
        holes = colors[0] | colors[1]
        if g == "impossible_geometry":
            assert p["exclusion"] == {"gate": "impossible_isolated_covered_vertex", "vertex": 64}
            assert 64 not in holes and all((64 ^ (1 << i)) in holes for i in range(7))
            continue
        j, alpha = p["outer"], p["alpha_parity"]
        assert alpha in (0, 1)
        donor_side = p.get("A_side", p.get("donor_side"))
        A = split((colors[alpha], colors[1 - alpha]), j, donor_side)
        B = split((colors[1 - alpha], colors[alpha]), j, 1 - donor_side)
        x = p.get("X", p.get("sources"))
        X = set(x)
        assert X <= A[1] and len(X) == len(x)
        Y = {v ^ (1 << j) for v in X}
        assert not Y & holes
        if g == "k4_two_return":
            assert p["B_side"] == 1 - donor_side and p["beta_parity"] == 1 - alpha
            assert sizes(A)[1] - sizes(A)[0] == sizes(B)[1] - sizes(B)[0] == 4
            U = set(p["U"])
            assert len(X) == len(U) == len(p["U"]) == 2 and U <= B[1]
            V = {v ^ (1 << j) for v in U}
            assert sorted(Y) == p["Y"] and sorted(V) == p["V"] and not V & (holes | Y)
            AA, BB = (A[0], (A[1] - X) | V), (B[0], (B[1] - U) | Y)
            assert arrays(*AA) == p["H_prime_A_by_alpha_beta"]
            assert arrays(*BB[::-1]) == p["H_prime_B_by_alpha_beta"]
            assert sorted(AA[0] | AA[1]) == p["H_prime_A"]
            assert sorted(BB[0] | BB[1]) == p["H_prime_B"]
            majority_root(AA, V, p["supplier"], j)
            spec = p["receiver"]
            i, mode = spec["inner"], spec["mode"]
            assert i != j
            if mode == "whole_face":
                majority_root(BB, Y, spec, j)
            elif mode == "positive_split":
                assert [f["side"] for f in spec["sides"]] == [0, 1]
                for s, f in enumerate(spec["sides"]):
                    part, marks = split(BB, i, s), side(Y, i, s)
                    assert arrays(*part, marks) == [f["minority"], f["majority"], f["marks"]]
                    assert sizes(part) == f["hole_counts"] and f["interface"] == "Q5_A_ALL"
                    marked_local((part[0], part[1] - marks), marks, f["interface"])
            else:
                assert mode == "controlled_single_root"
                z, t = spec["Z_side"], spec["T_side"]
                assert t == 1 - z
                counts = [sizes(split(BB, i, s)) for s in (z, t)]
                mark_counts = [len(side(Y, i, s)) for s in (z, t)]
                assert counts == spec["hole_counts"] and mark_counts == spec["mark_counts"]
                (a, b), (c, d) = counts
                assert (a, c) == (spec["p"], spec["q"])
                kind = spec["kind"]
                if kind == "same_side":
                    assert a in (1, 2) and b == a + 3 and d == c + 1 and mark_counts == [2, 0]
                else:
                    assert kind == "separated" and a >= 1 and c in (0, 1)
                    assert b == a + 1 and d == c + 3 and mark_counts == [1, 1]
                root, w = spec["a"], spec["w"]
                assert root in side(B[0], i, z) and w == root ^ (1 << i) and w not in holes | Y
                mode = kind
            return_tools[mode] += 1
            continue

        r, k = p["r"], p["k"]
        assert r in (3, 4) and k in (3, 4) and sizes(A) == [r, r + k]
        assert sizes(B)[1] - sizes(B)[0] == len(X) == k
        if g == "controlled_cycle_count":
            assert sorted(Y) == p["Y"] and arrays(*A) == [p["donor_original_minority"], p["donor_original_majority"]]
            i = p["inner"]
            assert i != j and [f["side"] for f in p["receiver_sides"]] == [0, 1]
            for s, f in enumerate(p["receiver_sides"]):
                old, marks = split(B, i, s), side(Y, i, s)
                assert arrays(*old, marks) == [f["original_minority"], f["original_majority"], f["marks"]]
                marked_local(old, marks, f["interface"])
                count_tools[f["interface"]] += 1
            continue
        assert sorted(Y) == p["marks"] and arrays(*B) == [p["receiver_minority"], p["receiver_majority"]]
        if g == "universal_delta3":
            i, root, w = p["inner"], p["root"], p["mirror"]
            assert i != j and (r, k) == (4, 3) and sizes(B) == [1, 4]
            assert B[0] == {root} and w == root ^ (1 << i) and w not in holes | Y
            z = bit(root, i)
            assert [sizes(split(B, i, s)) for s in (z, 1 - z)] == [[1, 2], [0, 2]]
            assert [len(side(Y, i, s)) for s in (z, 1 - z)] == [2, 1]
            continue
        assert g == "controlled_cycle_registered_split"
        spec = p["receiver"]
        i = spec["inner"]
        assert i != j and i in range(7)
        axes = [a for a in range(7) if a not in (i, j)]
        assert axes == spec["projected_axes"] and len(spec["faces"]) == 2
        used = []
        for s, f in enumerate(spec["faces"]):
            old, marks = split(B, i, s), side(Y, i, s)
            small, large, marked = ({project(v, axes) for v in points}
                                     for points in (*old[:1], old[1] | marks, marks))
            assert arrays(small, large, marked) == [f["minority"], f["majority"], f["marks"]]
            iface = f["interface"]
            kind = iface["kind"]
            used.append(kind)
            registered_tools[kind] += 1
            assert len(large) - len(small) == 2 * len(marked)
            if kind == "Q5_A_ALL":
                marked_local(old, marks, kind)
                continue
            if kind == "Q5_T26_RANK":
                assert sizes((small, large, marked)) == [2, 6, 2]
                rank = iface["rank"]
                target = t26[rank]
                assert arrays(*target) == iface["canonical"]
                # Derive all possible shifts from the image of one minority anchor.
                anchor = min(small)
                witness = next(((p, shift) for p in permutations(range(5)) for dest in target[0]
                                if (shift := permute(anchor, p) ^ dest) in range(32)
                                and tuple({permute(v, p) ^ shift for v in g}
                                          for g in (small, large, marked)) == target), None)
                assert witness is not None
                witnesses.append(dict(index=index, side=s, rank=rank, permutation=witness[0], xor=witness[1]))
            else:
                assert sizes((small, large, marked)) == [0, 6, 3]
                if kind == "T63_split":
                    axis = iface["local_inner"]
                    assert axis in range(5)
                    retained = large - marked
                    assert sum(bit(v, axis) for v in retained) == sum(bit(v, axis) for v in marked) in (1, 2)
                    continue
                rank = iface["rank"]
                if kind == "T63_old":
                    perm, shift = iface["rank_to_local_permutation"], iface["rank_to_local_xor"]
                    source, target = old63[rank], (large, marked)
                else:
                    assert kind == "T63_new"
                    perm, pre_shift = iface["local_to_rank_permutation"], iface["local_to_rank_xor"]
                    assert pre_shift in range(32)
                    shift = permute(pre_shift, perm)
                    source, target = (large, marked), new63[rank]
                assert sorted(perm) == list(range(5)) and shift in range(32)
                assert tuple({permute(v, perm) ^ shift for v in g} for g in source) == target
            ranks[kind].add(rank)
        assert used.count("Q5_A_ALL") == 1

    assert len(seen) == len(rows)
    assert gate_counts == plans["plan_counts"] == dict(
        controlled_cycle_count=2640, controlled_cycle_registered_split=398,
        universal_delta3=604, k4_two_return=50, impossible_geometry=93)
    assert count_tools == dict(Q5_A_ALL=1578, Q5_T44=2050, Q5_T15_FULL=1652)
    assert registered_tools == dict(Q5_A_ALL=398, Q5_T26_RANK=101, T63_split=137, T63_old=152, T63_new=8)
    assert return_tools == dict(whole_face=3, positive_split=9, same_side=1, separated=37)
    assert ranks == dict(Q5_T26_RANK={0,2,3,7,8,10,12,13,14,17,32,46}, T63_old={0,4,5,6}, T63_new={1,4})
    return dict(gates=gate_counts, count_tools=count_tools, registered_tools=registered_tools,
                return_receivers=return_tools, targets={k: sorted(v) for k, v in ranks.items()},
                T26_transports=witnesses)


def main():
    assert __debug__
    manifest_path = ROOT / (SUBMISSION + "_INPUTS.json")
    payload = manifest_path.read_bytes()
    assert sha256(payload).hexdigest() == "c8e308626e237d0e446b03079dd1895cbcf60b7cd43c72a355c8f310e5170590"
    hashes = json.loads(payload)["input_sha256"]
    for file, expected in hashes.items():
        assert sha256(Path(file).read_bytes()).hexdigest() == expected, file
    rows, reduction = check_basis()
    plans = check_plans(rows, hashes)
    budget()
    print(json.dumps(dict(reduction=reduction, plans=plans, manifest_entries=len(hashes),
                          cpu_seconds=process_time() - START), ensure_ascii=True))


if __name__ == "__main__":
    main()
