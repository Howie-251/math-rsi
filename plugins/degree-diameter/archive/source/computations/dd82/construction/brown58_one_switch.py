"""Exhaust the single-switch neighborhood of the explicit Brown+hub seed.

The result is a local-search diagnostic, not a nonexistence certificate.
"""
from collections import Counter
from pathlib import Path
import json
import time


def main():
    base = Path(__file__).parent
    lines = (base / 'brown57.edges').read_text().splitlines()
    n, m = map(int, lines[0].split())
    assert (n, m) == (57, 224)
    edges = [tuple(map(int, row.split())) for row in lines[1:]]
    g = [0] * 58
    for a, b in edges:
        g[a] |= 1 << b
        g[b] |= 1 << a
    for v in range(57):
        if g[v].bit_count() == 7:
            edges.append((v, 57))
            g[v] |= 1 << 57
            g[57] |= 1 << v
    assert len(edges) == 232 and all(row.bit_count() == 8 for row in g)
    full = (1 << 58) - 1

    def score():
        total = 0
        for u, row in enumerate(g):
            cover = row | (1 << u)
            todo = row
            while todo:
                bit = todo & -todo
                todo -= bit
                cover |= g[bit.bit_length() - 1]
            total += (full & ~cover).bit_count()
        return total // 2

    def toggle(a, b):
        g[a] ^= 1 << b
        g[b] ^= 1 << a

    start = time.process_time()
    initial = score()
    histogram = Counter()
    best = 10**9
    best_move = None
    for i, (a, b) in enumerate(edges):
        for c, d in edges[i + 1:]:
            if len({a, b, c, d}) != 4:
                continue
            for x, y in ((c, d), (d, c)):
                if g[a] >> x & 1 or g[b] >> y & 1:
                    continue
                toggle(a, b); toggle(x, y); toggle(a, x); toggle(b, y)
                energy = score()
                histogram[energy] += 1
                if energy < best:
                    best = energy
                    best_move = dict(removed=[[a, b], [x, y]], added=[[a, x], [b, y]])
                toggle(a, b); toggle(x, y); toggle(a, x); toggle(b, y)
    result = dict(
        scope='Every single simple degree-preserving two-edge switch from the Brown57 plus absolute-point hub seed, not arbitrary order58 graphs',
        initial_uncovered_pairs=initial, legal_switches=sum(histogram.values()),
        minimum_after_one_switch=best, score_histogram=dict(sorted(histogram.items())),
        example_minimum_switch=best_move, cpu_seconds=time.process_time() - start,
    )
    (base / 'brown58_one_switch.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
