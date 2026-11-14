"""Bounded geometry replay for E16 even oriented groups and mu=4."""

from collections import Counter, defaultdict
from functools import cache
from hashlib import sha256
from itertools import combinations, permutations, product
import json
from pathlib import Path
import re
from time import process_time

from R7_CONTROLLED_CYCLE_DONOR_PROBE import BITS, PERMUTATIONS, project
from R7_DELTA2_DISTANCE2_BROAD_CONTROLLED_CHECK import marked_ranks, new_ranks, t63


HERE = Path(__file__).resolve().parent
Q5 = Path("E:/新问题/research/six_directions")
EDGES = tuple(a | b for a, b in combinations(BITS, 2))
EDGE_INDEX = {edge: i for i, edge in enumerate(EDGES)}
REP_LIMIT = 1000
CPU_LIMIT = 60


def check_time(start):
    if process_time() - start >= CPU_LIMIT:
        raise TimeoutError


def edge_masks(graph):
    return [edge for i, edge in enumerate(EDGES) if graph & (1 << i)]


def edge_map(coordinates):
    return tuple(1 << EDGE_INDEX[sum(BITS[coordinates[i]] for i in range(7) if edge & BITS[i])]
                 for edge in EDGES)


def image(graph, mapping):
    result = 0
    while graph:
        bit = graph & -graph
        result |= mapping[bit.bit_length() - 1]
        graph ^= bit
    return result


def representatives(start):
    buckets = defaultdict(set)
    for index, indices in enumerate(combinations(range(len(EDGES)), 7)):
        if index % 1024 == 0:
            check_time(start)
        degrees = [0] * 7
        for edge_index in indices:
            edge = EDGES[edge_index]
            while edge:
                bit = edge & -edge
                degrees[bit.bit_length() - 1] += 1
                edge ^= bit
        if degrees[-1] <= 4 and all(a <= b for a, b in zip(degrees, degrees[1:])):
            buckets[tuple(degrees)].add(sum(1 << i for i in indices))

    reverse = edge_map(tuple(reversed(range(7))))
    for degrees in sorted(buckets, key=lambda ds: (ds != (2,) * 7, ds)):
        check_time(start)
        complement = tuple(4 - d for d in reversed(degrees))
        partners = {image(k, reverse) for k in buckets.get(complement, ())}
        if not partners:
            continue
        degree_blocks = tuple(tuple(i for i, d in enumerate(degrees) if d == degree)
                              for degree in sorted(set(degrees)))
        maps = tuple(edge_map(sum(blocks, ()))
                     for blocks in product(*(permutations(block) for block in degree_blocks)))
        remaining_g = set(buckets[degrees])
        while remaining_g:
            check_time(start)
            g = min(remaining_g)
            images_g = [(image(g, mapping), mapping) for mapping in maps]
            remaining_g.difference_update(h for h, _ in images_g)
            stabilizer = [mapping for h, mapping in images_g if h == g]
            remaining_k = set(partners)
            while remaining_k:
                check_time(start)
                k = min(remaining_k)
                remaining_k.difference_update(image(k, mapping) for mapping in stabilizer)
                yield g, k


def t26_key(minority, majority, marks):
    return min(tuple(tuple(sorted(p[x ^ root] for x in group))
                     for group in (minority, majority, marks))
               for root in minority for p in PERMUTATIONS)


def t26_registry():
    proof = (Q5 / "Q5_T26_RANK_BATCH_PROOF.md").read_bytes()
    assert sha256(proof).hexdigest() == "3908f60e884dda47570e652b6448b5ca2c519d8dadb8ba878879201be819cfc4"
    rows = re.findall(r"^\|\s*(\d+)\s*\|\s*([0-9, ]+)\s*\|\s*([0-9, ]+)\s*\|\s*([0-9, ]+)\s*\|\s*\d+\s*\|\s*2048\s*\|",
                      proof.decode("utf-8"), re.M)
    assert [int(row[0]) for row in rows] == list(range(55))
    ranks = {t26_key(*(tuple(map(int, group.split(","))) for group in groups)): int(index)
             for index, *groups in rows}
    assert len(ranks) == 55
    return ranks


def make_receiver_lookup():
    ranks = t26_registry()
    old_t63, _ = marked_ranks()
    new_t63 = new_ranks()

    @cache
    def lookup(minority, majority, marks):
        q, m = len(marks), len(minority)
        if q == 1:
            return dict(kind="Q5_A_ALL")
        if (q, m) == (2, 0):
            return dict(kind="Q5_T44")
        if (q, m) == (2, 1):
            return dict(kind="Q5_T15_FULL")
        if (q, m) == (2, 2):
            key = t26_key(minority, majority, marks)
            if key in ranks:
                return dict(kind="Q5_T26_RANK", rank=ranks[key], canonical=key)
        if (q, m) == (3, 0):
            return t63(dict(majority=majority, marks=marks), old_t63, new_t63)
        return None

    return lookup


def donor_interface(outer, minority, retained, marks):
    holes = minority | retained | marks
    r = len(minority)
    s1 = []
    for inner, bit in enumerate(BITS):
        if inner == outer:
            continue
        for side in (0, 1):
            face = {p for p in holes if bool(p & bit) == side}
            if r <= 1 and face == holes:
                return dict(kind="Q6_T44_same_face" if r == 0 else "Q6_T15_same_face",
                            inner=inner, side=side)
            if r <= 1 and len(face) == 1 and face <= marks:
                return dict(kind="Q6_T44_isolated_mark" if r == 0 else "Q6_T15_isolated_mark",
                            inner=inner, side=side)
            if r == 2 and marks <= face:
                n_minor, n_major = len(face & minority), len(face - minority)
                if (n_minor, n_major) == (2, 5):
                    return dict(kind="Q6_T26_ODD_S2", inner=inner, side=side)
                if (n_minor, n_major) == (1, 4):
                    s1.append((inner, side, next(iter(face & minority)), (holes - face) - minority))
    for a, b in combinations(s1, 2):
        if a[0] != b[0] and a[2] == b[2] and len(a[3] & b[3]) in (0, 2):
            return dict(kind="Q6_T26_ODD_PAIRED_S1", inner_sides=[a[:2], b[:2]], minority_root=a[2])
    return None


def receiver_plan(outer, minority, retained, marks, lookup, counts, gate):
    for inner, bit in enumerate(BITS):
        if inner == outer:
            continue
        axes = tuple(b for b in BITS if b not in (BITS[outer], bit))
        faces = []
        for side in (0, 1):
            groups = tuple(tuple(sorted(project(p, axes) for p in group if bool(p & bit) == side))
                           for group in (minority, retained | marks, marks))
            small, large, marked = groups
            if not marked or len(large) - len(small) != 2 * len(marked):
                break
            faces.append(groups)
        if len(faces) != 2:
            continue
        counts[gate + "_balanced_receiver_geometry"] += 1
        plans = []
        for small, large, marked in faces:
            interface = lookup(small, large, marked)
            if interface is None:
                counts[f"{gate}_unsupported_q{len(marked)}_m{len(small)}"] += 1
            plans.append(dict(minority=small, majority=large, marks=marked, interface=interface))
        if all(face["interface"] for face in plans):
            return dict(inner=inner, projected_axes=[b.bit_length() - 1 for b in axes], faces=plans)
    return None


def find_plan(even, odd, lookup, counts, start):
    colors = (even, odd)
    orientations = []
    for outer, bit in enumerate(BITS):
        for side, beta in ((0, 0), (1, 1)):
            donor_min = {p for p in colors[1 - beta] if bool(p & bit) == side}
            donor_maj = {p for p in colors[beta] if bool(p & bit) == side}
            receiver_min = colors[beta] - donor_maj
            receiver_maj = colors[1 - beta] - donor_min
            r, s = len(donor_min), len(receiver_min)
            assert r + s == 4 and len(donor_maj) == r + 4 and len(receiver_maj) == s + 4
            orientations.append((outer, bit, side, beta, donor_min, donor_maj, receiver_min, receiver_maj))

    for gate, n_source in (("controlled_C", 4), ("controlled_double_return", 2)):
        for outer, bit, side, beta, donor_min, donor_maj, receiver_min, receiver_maj in orientations:
            check_time(start)
            r, s = len(donor_min), len(receiver_min)
            counts[f"{gate}_orientation_r{r}"] += 1
            if n_source == 2 and r > 2:
                continue
            for x in combinations(sorted(donor_maj), n_source):
                check_time(start)
                y = {p ^ bit for p in x}
                returns = [()] if n_source == 4 else combinations(sorted(receiver_maj), 2)
                for u in returns:
                    v = {p ^ bit for p in u}
                    kept_a = donor_maj - set(x)
                    donor = (dict(kind=f"C_{r}") if not u
                             else donor_interface(outer, donor_min, kept_a, v))
                    if donor is None:
                        continue
                    counts[gate + "_certified_donor_choices"] += 1
                    kept_b = receiver_maj - set(u)
                    receiver = receiver_plan(outer, receiver_min, kept_b, y, lookup, counts, gate)
                    if receiver:
                        return dict(gate=gate, outer=outer, side=side, beta=beta, r=r, s=s,
                                    x=x, u=u, donor=donor, donor_minor=sorted(donor_min),
                                    donor_kept_major=sorted(kept_a), donor_marks=sorted(v),
                                    receiver=receiver, receiver_marks=sorted(y))
    return None


def main():
    start = process_time()
    counts = Counter()
    rows = []
    status = "all_representatives_covered"
    try:
        lookup = make_receiver_lookup()
        for g, k in representatives(start):
            if len(rows) == REP_LIMIT:
                status = "representative_limit"
                break
            g_edges, k_edges = edge_masks(g), edge_masks(k)
            even, odd = {0, *g_edges}, {127 ^ p for p in (0, *k_edges)}
            assert all((e ^ o) not in BITS for e in even for o in odd)
            local_counts = Counter()
            plan = find_plan(even, odd, lookup, local_counts, start)
            rows.append(dict(G=g_edges, K=k_edges, even=sorted(even), odd=sorted(odd), plan=plan))
            counts.update(local_counts)
            if plan is None:
                rows[-1]["gap_counts"] = local_counts
                status = "first_uncovered_representative"
                break
    except TimeoutError:
        status = "cpu_limit"
    result = dict(status=status, cpu_seconds=round(process_time() - start, 3),
                  limits=dict(cpu_seconds=CPU_LIMIT, representatives=REP_LIMIT),
                  counts=counts, checked=len(rows),
                  covered=sum(row["plan"] is not None for row in rows), rows=rows,
                  matching_calls=0, matching_enumerations=0, hamilton_calls=0, solver_calls=0, rank_runs=0)
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in ("status", "checked", "covered", "cpu_seconds", "counts")}))


if __name__ == "__main__":
    main()
