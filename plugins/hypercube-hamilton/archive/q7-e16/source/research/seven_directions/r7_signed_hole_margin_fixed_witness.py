"""Arithmetic check of one prescribed 54-edge input; no matching-family search."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent


def edge(x, y):
    return tuple(sorted((x, y)))


def face(base, ds, e, g, directions):
    indices = [v for v in range(64) if not v & base]
    removed = {0, 3}
    for v in ds:
        removed.update((v, v ^ e, v ^ e ^ g))
    assert len(removed) == 14
    matching = {edge(v, v ^ base) for v in indices if v not in removed}
    for v in ds:
        matching.update((edge(v, v ^ e), edge((v ^ e) ^ base, (v ^ e ^ g) ^ base)))
    swaps = []
    for q in directions:
        candidates = [(v, v ^ q) for v in indices if v < (v ^ q)
                      and edge(v, v ^ base) in matching
                      and edge(v ^ q, v ^ q ^ base) in matching]
        v, u = min(candidates)
        matching.difference_update((edge(v, v ^ base), edge(u, u ^ base)))
        matching.update((edge(v, u), edge(v ^ base, u ^ base)))
        swaps.append({'direction_bit': q, 'index_pair': [v, u]})
    assert len(matching) == 26
    assert len({v for pair in matching for v in pair}) == 52
    return matching, swaps


def main():
    a, sa = face(32, (12, 24, 5, 18), 1, 2, (4, 8, 16))
    b, sb = face(16, (6, 33, 34, 5), 8, 2, (1, 4, 32))
    m = a | {edge(v + 64, u + 64) for v, u in b} | {(0, 64), (3, 67)}
    endpoints = [v for pair in m for v in pair]
    assert len(m) == 54 and len(endpoints) == len(set(endpoints))
    assert all((v ^ u).bit_count() == 1 for v, u in m)
    holes = sorted(set(range(128)) - set(endpoints))
    eh = [v for v in holes if v.bit_count() % 2 == 0]
    oh = [v for v in holes if v.bit_count() % 2]
    ha = sorted(v for v in holes if v < 64)
    hb = sorted(v - 64 for v in holes if v >= 64)
    assert ha == sorted((15, 27, 6, 17, 32, 35, 44, 56, 37, 50))
    assert hb == sorted((12, 43, 40, 15, 16, 19, 22, 49, 50, 21))
    induced = sorted(edge(v, u) for v in holes for u in holes
                     if v < u and (v ^ u).bit_count() == 1)
    assert induced == [(15, 79), (50, 114)]
    counts = [sum(v ^ u == 1 << j for v, u in m) for j in range(7)]
    side_counts = [[sum(v ^ u == 1 << j for v, u in side) for side in (a, b)]
                   for j in range(6)]
    assert counts[6] == 2 and all(x > 2 for x in counts[:6])
    assert all(min(pair) >= 2 for pair in side_counts)
    # Relative O in B is local odd, relative E local even, since b=0,d=3 are even.
    ox = [v for v in hb if v % 2 == 0 and v.bit_count() % 2]
    ex = [v for v in hb if v % 2 == 0 and not v.bit_count() % 2]
    assert ox == [16, 22, 50] and ex == [12, 40]
    assert len(ox) - len(ex) == 1
    out = {
        'scope': 'one fixed 54-edge signed-hole-margin input only',
        'matching': sorted(m), 'size': len(m), 'holes': holes,
        'even_holes_global': eh, 'odd_holes_global': oh,
        'A_holes_local': ha, 'B_holes_local': hb,
        'direction_counts': counts, 'face_internal_direction_counts': side_counts,
        'swaps_A': sa, 'swaps_B': sb,
        'free_induced_edges': induced,
        'maximum_supermatching_size': 56,
        'new_theorem': {'j': 6, 'k': 0, 'd_local': 3, 'X_bit': 0,
                        'O_in_X_local': ox, 'E_in_X_local': ex, 'delta_X': 1,
                        'f_A': 6, 'f_B': 6},
        'excluded_old_rules': ['T/U/V/W: every allowed cut, side and naming',
                               'F7 and all f<=5 four-free supplements: both f=6',
                               'B: 20 original holes exceeds maximum 12',
                               'E8 augmentation: supermatching size at most56'],
        'not_claimed': ['universal margin gate', 'complete R7/P7',
                        'universal matching-family enumeration']}
    path = ROOT / 'R7_SIGNED_HOLE_MARGIN_WITNESS.json'
    path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: out[k] for k in ('size', 'direction_counts',
          'face_internal_direction_counts', 'A_holes_local', 'B_holes_local',
          'swaps_A', 'swaps_B', 'free_induced_edges')}, ensure_ascii=False))
    print('witness_sha256=' + hashlib.sha256(path.read_bytes()).hexdigest())


if __name__ == '__main__':
    main()
