"""Exact root-endpoint census by inverse images of certified Q4 negatives.

Reads binary certificates directly. No existing producer/checker is imported.
Does not enumerate all 15!! perfect matchings on the sixteen vertices.
"""
from pathlib import Path
from itertools import permutations, combinations
from collections import defaultdict, Counter
import hashlib
import json

ROOT = Path(__file__).resolve().parent
V = frozenset(range(16))
ODD = frozenset(x for x in V if x.bit_count() % 2)
PERMS = tuple(permutations(range(4)))


def require(condition, label):
    if not condition:
        raise ValueError(label)


def dfact(n):
    value = 1
    for k in range(1, n, 2):
        value *= k
    return value


def edge(x, y):
    return (min(x, y), max(x, y))


def transform(x, perm):
    return sum(((x >> i) & 1) << perm[i] for i in range(4))


def negative_short_completions(matching, vertices):
    """All complementary short perfect matchings; no Hamilton DFS."""
    adjacency = {x: {y for y in vertices if (x ^ y).bit_count() == 1
                     and edge(x, y) not in matching} for x in vertices}
    counts = Counter()

    def visit(left, chosen):
        if not left:
            graph = {x: set() for x in vertices}
            for x, y in matching | chosen:
                graph[x].add(y)
                graph[y].add(x)
            require(all(len(ns) == 2 for ns in graph.values()), 'two-factor degrees')
            unseen = set(vertices)
            components = 0
            while unseen:
                components += 1
                stack = [unseen.pop()]
                while stack:
                    fresh = graph[stack.pop()] & unseen
                    unseen -= fresh
                    stack.extend(fresh)
            require(components > 1, 'negative admits Hamilton cycle')
            counts[components] += 1
            return
        x = min(left, key=lambda z: (len(adjacency[z] & left), z))
        for y in sorted(adjacency[x] & left):
            visit(left - {x, y}, chosen | {edge(x, y)})

    visit(set(vertices), frozenset())
    return dict(sorted(counts.items()))


def load_table(hole):
    name = f'q4_distance{hole.bit_count()}_avoided_table.bin'
    data = (ROOT / name).read_bytes()
    require(len(data) == 135135 * 30, 'complete table byte length')
    vertices = V - {0, hole}
    seen = bytearray(135135)
    negatives = []
    negative_proofs = []
    positive = 0
    for offset in range(0, len(data), 30):
        mate = data[offset:offset + 16]
        cycle = data[offset + 16:offset + 30]
        require({x for x, y in enumerate(mate) if y == 255} == {0, hole}, 'holes')
        require(all(mate[x] in vertices and mate[x] != x and mate[mate[x]] == x
                    for x in vertices), 'matching involution')
        matching = frozenset(edge(x, mate[x]) for x in vertices)
        remaining = sorted(vertices)
        rank = 0
        while remaining:
            x = remaining.pop(0)
            partner_index = remaining.index(mate[x])
            rank += partner_index * dfact(len(remaining) - 1)
            remaining.pop(partner_index)
        require(0 <= rank < len(seen) and not seen[rank], 'unique valid matching rank')
        seen[rank] = 1
        if cycle == bytes([255]) * 14:
            proof = negative_short_completions(matching, vertices)
            negatives.append(matching)
            negative_proofs.append({'matching': sorted(matching),
                                    'short_completion_component_histogram': proof})
        else:
            require(len(set(cycle)) == 14 and set(cycle) == vertices, 'cycle support')
            edges = frozenset(edge(cycle[i], cycle[(i + 1) % 14]) for i in range(14))
            require(len(edges) == 14 and matching <= edges, 'cycle required edges')
            require(all((x ^ y).bit_count() == 1 for x, y in edges - matching),
                    'new cycle edges short')
            positive += 1
    require(all(seen), 'full table coverage')
    require(len(negatives) == (51 if hole == 1 else 53), 'negative count')
    return negatives, {'file': name, 'sha256': hashlib.sha256(data).hexdigest(),
                       'records': len(seen), 'positive': positive,
                       'negative': len(negatives), 'negative_proofs': negative_proofs}


def main():
    loaded = {hole: load_table(hole) for hole in (1, 7)}
    bad_tables = {}
    transport = {}
    for y in sorted(ODD):
        source = 1 if y.bit_count() == 1 else 7
        perm = next(p for p in PERMS if transform(source, p) == y)
        bad_tables[y] = {frozenset(edge(transform(a, perm), transform(b, perm))
                                    for a, b in matching) for matching in loaded[source][0]}
        require(len(bad_tables[y]) == len(loaded[source][0]), 'bijective transport')
        transport[y] = {'source_hole': source, 'coordinate_permutation': perm}

    exception_endpoints = defaultdict(set)
    inverse_instances = 0
    for y, negatives in bad_tables.items():
        for matching in negatives:
            for a, b in matching:
                for root_partner, endpoint_partner in ((a, b), (b, a)):
                    perfect = matching - {edge(a, b)} | {
                        edge(0, root_partner), edge(y, endpoint_partner)}
                    require(len(perfect) == 8
                            and sorted(x for e in perfect for x in e) == list(range(16)),
                            'inverse-generated perfect matching')
                    exception_endpoints[perfect].add(y)
                    inverse_instances += 1

    histogram = Counter()
    examples = {}
    records = []
    good_set_counts = Counter()
    weight_three_histogram = Counter()
    exceptional_root_partner_odd = 0
    for perfect in sorted(exception_endpoints, key=lambda p: tuple(sorted(p))):
        mate = {}
        for x, y in perfect:
            mate[x], mate[y] = y, x
        inverse_bad = exception_endpoints[perfect]
        forward_bad = set()
        for y in ODD:
            if mate[0] == y:
                forward_bad.add(y)
            else:
                a, b = mate[0], mate[y]
                reduced = perfect - {edge(0, a), edge(y, b)} | {edge(a, b)}
                require(len(reduced) == 7, 'forward reduction size')
                if reduced in bad_tables[y]:
                    forward_bad.add(y)
        expected = inverse_bad | ({mate[0]} if mate[0] in ODD else set())
        require(forward_bad == expected, 'forward/inverse endpoint agreement')
        histogram[len(forward_bad)] += 1
        good_set_counts[tuple(sorted(ODD - forward_bad))] += 1
        weight_three_histogram[len({7, 11, 13, 14} - forward_bad)] += 1
        exceptional_root_partner_odd += mate[0] in ODD
        examples.setdefault(len(forward_bad), {'matching': sorted(perfect),
                                              'bad_odd_endpoints': sorted(forward_bad),
                                              'good_odd_endpoints': sorted(ODD - forward_bad)})
        records.append({'matching': sorted(perfect), 'bad_odd_endpoints': sorted(forward_bad)})

    max_bad = max(histogram)
    minimum_sets = {frozenset(s) for s in good_set_counts}
    inclusion_minimal = sorted((sorted(s) for s in minimum_sets
                                if not any(t < s for t in minimum_sets)),
                               key=lambda s: (len(s), s))
    require(all(any(set(t) <= set(s) for t in inclusion_minimal)
                for k in (7, 8) for s in combinations(sorted(ODD), k)),
            'nonexceptional sets do not change inclusion-minimal list')
    full_bad_histogram = Counter(histogram)
    full_bad_histogram[1] += 8 * dfact(14) - exceptional_root_partner_odd
    full_bad_histogram[0] += 7 * dfact(14) - (len(records) - exceptional_root_partner_odd)
    require(sum(full_bad_histogram.values()) == dfact(16), 'whole-universe count')
    result = {'status': 'PASS' if max_bad <= 4 else 'COUNTEREXAMPLE',
              'claim_at_least_four_odd_endpoints': max_bad <= 4,
              'root': 0, 'odd_endpoints': sorted(ODD),
              'inverse_instances': inverse_instances,
              'distinct_exceptional_perfect_matchings': len(exception_endpoints),
              'bad_endpoint_count_histogram_on_exceptions': dict(sorted(histogram.items())),
              'max_bad_odd_endpoints': max_bad, 'minimum_good_odd_endpoints': 8 - max_bad,
              'minimum_good_distance_three_endpoints': min(3, min(weight_three_histogram)),
              'good_distance_three_histogram_on_exceptions': dict(sorted(weight_three_histogram.items())),
              'minimum_cardinality_good_endpoint_sets': [
                  {'good_odd_endpoints': s, 'perfect_matching_count': good_set_counts[s]}
                  for s in sorted(good_set_counts) if len(s) == 8 - max_bad],
              'all_inclusion_minimal_good_endpoint_sets': inclusion_minimal,
              'full_perfect_matching_bad_endpoint_count_histogram': dict(sorted(full_bad_histogram.items())),
              'nonexceptional_perfect_matchings_good_lower_bound': 7,
              'examples_by_bad_count': examples,
              'transport': transport, 'tables': [loaded[h][1] for h in (1, 7)],
              'all_exceptional_matchings': records,
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'prior_review_sha256': hashlib.sha256((ROOT / 'CANONICAL_COMPLETION_REVIEW.md').read_bytes()).hexdigest(),
              'full_q5_t15_proved': False, 'full_p6_proved': False}
    (ROOT / 'q4_perfect_endpoint_abundance_check.json').write_text(
        json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('status', 'inverse_instances',
          'distinct_exceptional_perfect_matchings', 'bad_endpoint_count_histogram_on_exceptions',
          'max_bad_odd_endpoints', 'minimum_good_odd_endpoints', 'examples_by_bad_count')}, indent=2))


if __name__ == '__main__':
    main()
