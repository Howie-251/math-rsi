"""Independent finite regressions for N10/E1 and Z6 boundary bookkeeping.

No finite outcome is used as a proof of an unbounded statement.
"""
import itertools
import json
from pathlib import Path


def parity(x):
    return x.bit_count() & 1


def edge_bit(a, b, n=32):
    return 1 << (min(a, b) * n + max(a, b))


def half_layers(m):
    n = 1 << m
    return [(j, b, tuple((x, x ^ (1 << j)) for x in range(n)
                        if not (x & (1 << j)) and parity(x) == b))
            for j in range(m) for b in range(2)]


def check_hole_geometry():
    checks = 0
    dimensions = {}
    for m in range(2, 11):
        count = 0
        for j, b, edges in half_layers(m):
            covered = {v for edge in edges for v in edge}
            for q in range(2):
                holes = [x for x in range(1 << m)
                         if x not in covered and parity(x) == q]
                for y, s in itertools.combinations(holes, 2):
                    assert ((y ^ s) & (1 << j)) == 0
                    count += 1
        dimensions[m] = count
        checks += count
    return {"checks": checks, "dimensions": dimensions}


def check_e1_anchored_first_half():
    # Normalize c=0, j=0 and the half-layer missing c. Enumerate the entire
    # m=5 family where the newly compressed partner edge completes that half,
    # and the two removed endpoint matching edges are short. Its remaining
    # seven even/odd pairs range over all 7! complete-bipartite permutations.
    m, n, c, j = 5, 32, 0, 0
    halves = half_layers(m)
    masks = [sum(edge_bit(a, b) for a, b in edges) for _, _, edges in halves]
    h_edges = next(edges for k, b, edges in halves if k == j and b == 1)
    s_set = {v for edge in h_edges for v in edge}
    t_set = set(range(n)) - s_set
    counts = {"perfect_matchings": 0, "third_endpoint_applications": 0,
              "simultaneous_half_obstructions": 0}
    for k in range(1, m):
        pc = 1 << k
        pd = pc ^ 1
        for ell in range(1, m):
            d = pd ^ (1 << ell)
            rest_even = sorted(x for x in t_set - {c, d} if parity(x) == 0)
            rest_odd = sorted(x for x in t_set - {c, d} if parity(x) == 1)
            fixed = [(a, b) for a, b in h_edges if {a, b} != {pc, pd}]
            fixed += [(c, pc), (d, pd)]
            fixed_mask = sum(edge_bit(a, b) for a, b in fixed)
            for perm in itertools.permutations(rest_odd):
                edges = fixed + list(zip(rest_even, perm))
                p = {a: b for a, b in edges} | {b: a for a, b in edges}
                pmask = fixed_mask | sum(edge_bit(a, b) for a, b in zip(rest_even, perm))
                assert len(p) == n
                first = (pmask ^ edge_bit(c, pc) ^ edge_bit(d, pd)) | edge_bit(pc, pd)
                assert any(first & h == h for h in masks)
                counts["perfect_matchings"] += 1
                for e in range(n):
                    if parity(e) != 1 or e in (d, pc):
                        continue
                    if (e ^ p[e]).bit_count() != 1:
                        continue
                    counts["third_endpoint_applications"] += 1
                    second = (pmask ^ edge_bit(c, pc) ^ edge_bit(e, p[e])) | edge_bit(pc, p[e])
                    if any(second & h == h for h in masks):
                        counts["simultaneous_half_obstructions"] += 1
                        allowed = [a for a in range(m)
                                   if ((d >> a) & 1) == ((e >> a) & 1) != ((c >> a) & 1)]
                        assert k in allowed, (edges, c, d, e, allowed)
    return counts


def check_z6_abstract_cut():
    # Oriented path begins at odd c=0 and ends at even d=2h-1;
    # alternating matching edges have positions (2j,2j+1).
    count = 0
    degenerate = 0
    q_port = 0
    q_t = 0
    for h in range(2, 11):
        for mask in range(1, 1 << (h - 1)):
            deleted = [j for j in range(1, h) if mask & (1 << (j - 1))]
            for u_index in deleted:
                # If the final PA edge belongs to D, d must be u.
                if h - 1 in deleted and u_index != h - 1:
                    continue
                u = 2 * u_index + 1
                starts = [0] + [2 * j + 1 for j in deleted]
                ends = [2 * j for j in deleted] + [2 * h - 1]
                pieces = [list(range(a, b + 1)) for a, b in zip(starts, ends)]
                assert sorted(x for piece in pieces for x in piece) == list(range(2 * h))
                containing = [piece for piece in pieces if u in piece]
                assert len(containing) == 1
                piece = containing[0]
                assert piece[0] == u and 0 not in piece
                if piece[-1] == 2 * h - 1:
                    # End d moves to t; singleton {u=d} moves to edge u--t.
                    q_t += 1
                    if u == 2 * h - 1:
                        assert piece == [u]
                        degenerate += 1
                else:
                    # Position even means original parity odd, hence its
                    # cross-layer mate has even parity and differs from v.
                    assert piece[-1] % 2 == 0
                    q_port += 1
                count += 1
    return {"cases": count, "u_equals_d_cases": degenerate,
            "q_is_even_port_cases": q_port, "q_equals_t_cases": q_t}


def verify_original_z6_boundary_witness():
    gray = [(k ^ (k >> 1)) << 1 for k in range(32)]
    path = gray[1:] + [0]
    norm = lambda a, b: tuple(sorted((a, b)))
    pa = {norm(path[k], path[k + 1]) for k in range(0, 32, 2)}
    de = {(0, 32)}
    ma = pa - de
    cross = {(32, 33)}
    mb = {norm(x, x ^ 2) for x in range(1, 64, 2)} - {(1, 3), (33, 35)}
    matching = ma | cross | mb
    covered = [x for edge in matching for x in edge]
    assert len(covered) == len(set(covered)) == 60
    assert set(range(64)) - set(covered) == {0, 3, 35, 1}
    assert all((a ^ b).bit_count() == 1 for a, b in matching)
    assert path[0] == 2 and path[-1] == 0
    assert len(set(path)) == 32 and set(path) == set(range(0, 64, 2))
    assert pa <= {norm(a, b) for a, b in zip(path, path[1:])}
    assert all((a ^ b).bit_count() == 1 for a, b in zip(path, path[1:]))
    assert de <= pa and path[-2:] == [32, 0]
    assert 7 in covered and parity(7) == 1
    remainder = path[:-1]
    transferred = [3] + remainder + [33]
    assert len(set(transferred)) == len(transferred)
    assert {norm(a, b) for a, b in zip(transferred, transferred[1:])} >= ma | cross
    lb = mb | {(3, 33)}
    assert set(range(1, 64, 2)) - {x for e in lb for x in e} == {1, 35}
    return {"meaning": "Counterexample to original no-isolate proof assertion, not to Z6 theorem",
            "n": 6, "split_coordinate": 0, "u": 0, "z": 3, "w": 35,
            "t": 1, "c": 2, "d": 0, "v": 7, "K_A": path,
            "P_A": sorted(pa), "D": sorted(de), "M": sorted(matching),
            "repaired_J": [0, 1], "R": [[3, 33]], "L_B_holes": [1, 35]}


if __name__ == "__main__":
    result = {"scope": "Finite independent regressions, not general proofs",
              "N10_half_layer_hole_geometry": check_hole_geometry(),
              "E1_dimension5_anchored_family": check_e1_anchored_first_half(),
              "Z6_abstract_fragment_bookkeeping": check_z6_abstract_cut(),
              "Z6_original_assertion_counterexample": verify_original_z6_boundary_witness()}
    target = Path(__file__).with_suffix(".json")
    target.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
