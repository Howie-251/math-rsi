"""Exhaust two supplied finite fixtures on Linux; corroboration, not proof."""
from collections import defaultdict
from itertools import combinations, product
from pathlib import Path
import datetime
import hashlib
import heapq
import json
import platform
import resource
import time

HERE = Path(__file__).resolve().parent


def check_fixture(names, blue):
    n = len(names)
    vertices = tuple(range(n))
    triples = {t: ('B' if blue(t) else 'R') for t in combinations(vertices, 3)}

    def labels(seq):
        return [names[v] for v in seq]

    def mono(seq, color):
        return all(triples[t] == color for t in combinations(seq, 3))

    paths = {c: [s for k in range(1, n + 1) for s in combinations(vertices, k)
                 if mono(s, c)] for c in 'RB'}
    # The independent local-chain predicate checks closure for every subset.
    closure = all(mono(s, c) == all(triples[tuple(s[j:j + 3])] == c
                                   for j in range(len(s) - 2))
                  for c in 'RB' for k in range(1, n + 1)
                  for s in combinations(vertices, k))
    packet_rows = []
    for q in combinations(vertices, 4):
        a, b, c, d = q
        word = ''.join(triples[t] for t in [(a, b, c), (a, b, d), (a, c, d), (b, c, d)])
        changes = sum(x != y for x, y in zip(word, word[1:]))
        packet_rows.append({'vertices': labels(q), 'word': word, 'switches': changes})
    endpoint_rows = []
    for s, t in combinations(vertices, 2):
        maxima = {c: max(len(p) for p in paths[c] if p[0] == s and p[-1] == t)
                  for c in 'RB'}
        endpoint_rows.append({'endpoints': labels((s, t)), **maxima, 'sum': sum(maxima.values())})

    def family(color, k, inside=None):
        return [p for p in paths[color] if len(p) == k and
                (inside is None or set(p) <= set(inside))]

    r6, b5 = family('R', 6), family('B', 5)
    sources_r6 = {p[0] for p in r6}
    sources_b5 = {p[0] for p in b5}
    lock_rows = []
    for s in sorted(sources_r6 & sources_b5):
        ends = {p[-1] for p in r6 if p[0] == s}
        seconds = {p[1] for p in b5 if p[0] == s}
        lock_rows.append({'source': names[s], 'T': labels(sorted(ends)),
                          'Q': labels(sorted(seconds)), 'union': labels(sorted(ends | seconds)),
                          'union_size': len(ends | seconds), 'locked': len(ends | seconds) == 1})

    pairs = list(combinations(vertices, 2))
    edges = {p: set() for p in pairs}
    comparison_rows = []
    for (a, b, c), color in triples.items():
        order = [(a, b), (a, c), (b, c)]
        if color == 'B':
            order.reverse()
        for p, q in combinations(order, 2):
            edges[p].add(q)
        comparison_rows.append({'triple': labels((a, b, c)), 'color': color,
                                'increasing_pair_order': [labels(p) for p in order]})
    indegree = {p: 0 for p in pairs}
    for targets in edges.values():
        for q in targets:
            indegree[q] += 1
    queue = [p for p in pairs if indegree[p] == 0]
    heapq.heapify(queue)
    order = []
    while queue:
        p = heapq.heappop(queue)
        order.append(p)
        for q in sorted(edges[p]):
            indegree[q] -= 1
            if not indegree[q]:
                heapq.heappush(queue, q)
    assert len(order) == len(pairs), 'pair comparison cycle'
    rank = {p: i for i, p in enumerate(order)}
    minimum_neighbor = {}
    incident_rows = []
    for u in vertices:
        incident = sorted((p for p in pairs if u in p), key=rank.__getitem__)
        first = incident[0]
        assert all(q in edges[first] for q in incident[1:]), 'non-intrinsic incident minimum'
        minimum_neighbor[u] = first[0] if first[1] == u else first[1]
        incident_rows.append({'vertex': names[u], 'p': names[minimum_neighbor[u]],
                              'incident_pair_order': [labels(p) for p in incident],
                              'minimum_beats_all_other_incident_pairs': True})
    plus = {u for u in vertices if u < minimum_neighbor[u]}
    minus = set(vertices) - plus
    g = {p[-1] for p in family('R', 5, plus)} & {p[0] for p in family('B', 4, plus)}
    h, r = minus | g, plus - g

    # All R6 witnesses participate: zero-based consecutive-pair positions.
    pair_witnesses = defaultdict(list)
    for path in r6:
        for i in range(5):
            pair_witnesses[path[i:i + 2]].append((i, path))
    position_rows = []
    recombinations = []
    level_edges = defaultdict(set)
    for pair, occurrences in sorted(pair_witnesses.items()):
        positions = sorted({i for i, _ in occurrences})
        assert len(positions) == 1, 'pair has multiple R6 positions'
        i = positions[0]
        level_edges[i].add(pair)
        prefixes = sorted({p[:i + 2] for _, p in occurrences})
        suffixes = sorted({p[i + 2:] for _, p in occurrences})
        joined = sorted({p + q for p, q in product(prefixes, suffixes)})
        assert all(len(p) == 6 and mono(p, 'R') for p in joined)
        position_rows.append({'pair': labels(pair), 'positions': positions,
                              'witnesses': [labels(p) for _, p in occurrences]})
        recombinations.append({'pair': labels(pair), 'position': i,
                               'sources': labels(sorted({p[0] for _, p in occurrences})),
                               'ends': labels(sorted({p[-1] for _, p in occurrences})),
                               'prefix_count': len(prefixes), 'suffix_count': len(suffixes),
                               'all_prefix_suffix_R6': [labels(p) for p in joined]})
    walks = []
    for i, graph in sorted(level_edges.items()):
        for u, v, w in combinations(vertices, 3):
            if (u, v) in graph and (v, w) in graph:
                color = triples[u, v, w]
                walks.append({'position': i, 'vertices': labels((u, v, w)), 'color': color})
                assert color == 'B', 'red directed level two-edge walk'
    checks = {'all_packets_at_most_one_switch': all(row['switches'] <= 1 for row in packet_rows),
              'chain_predicate_equals_all_triples_predicate': closure,
              'no_weak7_same_endpoint_max_sum_le8': all(row['sum'] <= 8 for row in endpoint_rows),
              'no_R7': not family('R', 7), 'no_B6': not family('B', 6),
              'no_B5': not b5, 'unique_R6_pair_positions': True,
              'all_same_pair_prefix_suffix_combinations_R6': True,
              'all_level_two_edge_walks_blue': True}
    assert all(checks.values()), checks
    return {'vertices': list(names), 'checks': checks,
            'all_triples': [{'vertices': labels(t), 'color': c} for t, c in triples.items()],
            'all_four_packets': packet_rows,
            'all_subset_paths': {c: [labels(p) for p in ps] for c, ps in paths.items()},
            'longest_paths_same_endpoints': endpoint_rows,
            'max_same_endpoint_sum': max(row['sum'] for row in endpoint_rows),
            'longest_red': max(map(len, paths['R'])), 'longest_blue': max(map(len, paths['B'])),
            'SrcR6': labels(sorted(sources_r6)), 'SrcB5': labels(sorted(sources_b5)),
            'SrcR6_intersect_SrcB5': labels(sorted(sources_r6 & sources_b5)),
            'locked_source_candidates': lock_rows, 'F': [row['source'] for row in lock_rows if row['locked']],
            'complete_R6_list': [labels(p) for p in r6],
            'pair_comparisons': comparison_rows, 'global_pair_linear_extension': [labels(p) for p in order],
            'intrinsic_minimum_neighbors': incident_rows,
            'canonical': {'Pplus': labels(sorted(plus)), 'Pminus': labels(sorted(minus)),
                          'G': labels(sorted(g)), 'H': labels(sorted(h)), 'R': labels(sorted(r)),
                          'internal_Pplus_R5': [labels(p) for p in family('R', 5, plus)],
                          'internal_Pplus_B4': [labels(p) for p in family('B', 4, plus)]},
            'R6_pair_positions': position_rows, 'R6_pair_recombinations': recombinations,
            'rank_level_edges': {i: [labels(p) for p in sorted(es)] for i, es in level_edges.items()},
            'rank_level_two_edge_walks': walks}


def main():
    assert platform.system() == 'Linux', 'scientific execution is Linux-only'
    resource.setrlimit(resource.RLIMIT_CPU, (20, 20))
    resource.setrlimit(resource.RLIMIT_AS, (512 * 1024 ** 2, 512 * 1024 ** 2))
    started = time.monotonic()
    names7 = ('u', 'a', 'b', 'z', 'c', 'd', 'e')
    blue7 = {(0, 1, 3), (0, 2, 3), (1, 2, 3)}
    names8 = ('a1', 'a2', 'm1', 'm2', 'm3', 'm4', 'b1', 'b2')
    report = {'scope': 'Two main-supplied complete fixtures; deterministic exhaustive corroboration only, not general proof or acceptance',
              'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'platform': platform.platform(), 'cpu_seconds_limit': 20,
              'fixtures': {'fixture7': check_fixture(names7, blue7.__contains__),
                           'fixture8': check_fixture(names8, lambda t: (t[0] < 2 and t[1] < 2 and 2 <= t[2] < 6)
                                                     or (2 <= t[0] < 6 and t[1] >= 6 and t[2] >= 6))}}
    report['seconds'] = time.monotonic() - started
    destination = HERE / 'explicit_fixtures_result.json'
    with destination.open('x') as output:
        json.dump(report, output, indent=2)
    summary = {name: {k: data[k] for k in ['checks', 'max_same_endpoint_sum', 'longest_red', 'longest_blue',
                                         'SrcR6', 'SrcB5', 'F', 'complete_R6_list', 'canonical',
                                         'rank_level_two_edge_walks']} for name, data in report['fixtures'].items()}
    print(json.dumps({'status': 'PASS', 'result': str(destination), 'seconds': report['seconds'],
                      'fixtures': summary}, indent=2))


if __name__ == '__main__':
    main()
