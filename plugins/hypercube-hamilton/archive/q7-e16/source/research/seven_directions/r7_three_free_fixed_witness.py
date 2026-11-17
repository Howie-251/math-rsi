"""One prescribed 58-edge witness; no matching-family or hole enumeration."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent


def edge(x, y):
    return tuple(sorted((x, y)))


def face(b, ds, e, g, swap_directions):
    indices = [x for x in range(64) if not x & b]
    removed = {0, 3}
    for d in ds:
        removed.update((d, d ^ e, d ^ e ^ g))
    assert len(removed) == 8
    matching = {edge(x, x ^ b) for x in indices if x not in removed}
    for d in ds:
        matching.update((edge(d, d ^ e), edge((d ^ e) ^ b, (d ^ e ^ g) ^ b)))
    swaps = []
    for q in swap_directions:
        # Exactly one deterministic local choice per prescribed direction.
        # The 16 disjoint index-pairs lose at most 8+4 available pairs.
        candidates = [(x, x ^ q) for x in indices if x < (x ^ q)
                      and edge(x, x ^ b) in matching
                      and edge(x ^ q, x ^ q ^ b) in matching]
        x, y = min(candidates)
        matching.remove(edge(x, x ^ b))
        matching.remove(edge(y, y ^ b))
        matching.update((edge(x, y), edge(x ^ b, y ^ b)))
        swaps.append({'direction_bit': q, 'index_pair': [x, y]})
    assert len(matching) == 28
    return matching, swaps


def run():
    a, swaps_a = face(32, (12, 24), 1, 2, (4, 8, 16))
    b, swaps_b = face(16, (6, 33), 8, 2, (1, 4, 32))
    matching = a | {edge(x + 64, y + 64) for x, y in b} | {(0, 64), (3, 67)}
    vertices = [v for pair in matching for v in pair]
    assert len(matching) == 58 and len(vertices) == len(set(vertices))
    assert all((x ^ y).bit_count() == 1 for x, y in matching)
    holes = sorted(set(range(128)) - set(vertices))
    even = [x for x in holes if x.bit_count() % 2 == 0]
    odd = [x for x in holes if x.bit_count() % 2 == 1]
    counts = [sum(x ^ y == 1 << j for x, y in matching) for j in range(7)]
    assert counts == [4, 4, 4, 4, 20, 20, 2]
    assert even == [15, 27, 80, 83, 86, 113]
    assert odd == [32, 35, 44, 56, 76, 107]
    assert not any((x ^ y).bit_count() == 1 for x in even for y in odd)
    marginals = [[sum((x >> j) & 1 for x in even),
                  sum((x >> j) & 1 for x in odd)] for j in range(7)]
    assert marginals == [[4, 2], [4, 2], [2, 2], [2, 4], [5, 1], [1, 5], [4, 2]]
    assert all(pair != [3, 3] for pair in marginals)
    side_counts = [[sum(x < 64 and x ^ y == 1 << j for x, y in matching),
                    sum(x >= 64 and x ^ y == 1 << j for x, y in matching)]
                   for j in range(6)]
    assert all(min(pair) >= 2 for pair in side_counts)
    out = {'scope': 'one fixed 58-edge maximal m=2 witness only',
           'matching': sorted(matching), 'size': len(matching), 'holes': holes,
           'even_holes': even, 'odd_holes': odd, 'direction_counts': counts,
           'face_internal_direction_counts': side_counts,
           'bit1_even_odd_hole_marginals': marginals,
           'swaps_A': swaps_a, 'swaps_B': swaps_b,
           'new_theorem': {'j': 6, 'internal_edges_A': 28, 'internal_edges_B': 28,
                           'f_A': 4, 'f_B': 4},
           'old_coverage_excluded': ['T/U/V/W every allowed direction and side',
                                     'B every coordinate (needs 3:3 at 12 holes)',
                                     'E8 augmentation (maximal size 58)']}
    path = ROOT / 'R7_THREE_FREE_PAIRINGS_WITNESS.json'
    path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: out[k] for k in ('size', 'holes', 'direction_counts',
                                         'bit1_even_odd_hole_marginals', 'swaps_A', 'swaps_B')},
                     ensure_ascii=False))
    print('witness_sha256=' + hashlib.sha256(path.read_bytes()).hexdigest())


if __name__ == '__main__':
    run()
