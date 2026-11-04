"""Independently verify reported nonhalf Q4 obstructions via all short completions.

For a perfect required matching on the 14 allowed vertices, every new-edge
set is a short perfect matching. Enumerate those by a bipartite recursion,
which is independent of the producer's Hamilton-path search.
"""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def analyze(required, hole):
    f = {frozenset(e) for e in required}
    vertices = set(range(16)) - {0, hole}
    flattened = [x for e in f for x in e]
    assert len(f) == 7 and len(flattened) == len(set(flattened)) == 14
    assert set(flattened) == vertices
    for i in range(4):
        for parity in range(2):
            half = {frozenset((x, x ^ (1 << i))) for x in range(16)
                    if not (x >> i & 1) and x.bit_count() % 2 == parity}
            assert len(half) == 4 and not half <= f
    even = sorted(x for x in vertices if x.bit_count() % 2 == 0)
    odd = {x for x in vertices if x.bit_count() % 2}
    assert len(even) == len(odd) == 7
    neighbors = {x: sorted(y for y in odd if (x ^ y).bit_count() == 1
                           and frozenset((x, y)) not in f) for x in even}
    histogram = Counter()

    def recurse(index, available, chosen):
        if index == len(even):
            h = {frozenset(e) for e in chosen}
            graph = {x: set() for x in vertices}
            for e in f | h:
                x, y = e
                graph[x].add(y)
                graph[y].add(x)
            assert len(h) == 7 and not f & h and all(len(ns) == 2 for ns in graph.values())
            unseen = set(vertices)
            components = 0
            while unseen:
                components += 1
                stack = [unseen.pop()]
                while stack:
                    x = stack.pop()
                    new = graph[x] & unseen
                    unseen.difference_update(new)
                    stack.extend(new)
            histogram[components] += 1
            return
        x = even[index]
        for y in neighbors[x]:
            if y in available:
                recurse(index + 1, available - {y}, chosen + [(x, y)])

    recurse(0, odd, [])
    assert histogram and histogram[1] == 0
    return {'required_matching': required, 'avoided': [0, hole],
            'short_perfect_completions': sum(histogram.values()),
            'component_histogram': dict(sorted(histogram.items())),
            'contains_half_layer': False, 'hamilton_14_cycle_exists': False}


def main():
    source = json.loads((ROOT / 'q4_opposite_avoided_probe_results.json').read_text(encoding='utf-8-sig'))
    items = [analyze(f, entry['other_hole']) for entry in source['orbits']
             for f in entry['nonhalf_examples']]
    result = {'status': 'PASS', 'examples_checked': len(items),
              'scope': 'each listed nonhalf obstruction individually; not a completeness proof of the exception lists',
              'examples': items, 'q5_a4_counterexample': False, 'full_p6_proved': False}
    (ROOT / 'q4_opposite_avoided_obstruction_verification.json').write_text(
        json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'status': result['status'], 'examples_checked': len(items),
                      'distance_three_examples': sum(i['avoided'][1] == 7 for i in items)}))


if __name__ == '__main__':
    main()
