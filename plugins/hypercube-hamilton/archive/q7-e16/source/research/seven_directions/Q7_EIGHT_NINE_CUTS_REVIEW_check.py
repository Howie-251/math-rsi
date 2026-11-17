"""Independent audit checks; no producer imports and no eight-hole census.

Finite checks supplement the universal forest argument in the review. Abstract
path orders are deliberately allowed to violate cube adjacency: the forest
bookkeeping must hold even on this larger domain.
"""
import hashlib
import itertools
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent


def digest(p):
    return 'sha256:' + hashlib.sha256(p.read_bytes()).hexdigest()


def run():
    imports = {}
    for name in ('A6_FULL_REVIEW.json', 'A4_FULL_REVIEW.json',
                 'Q7_SIX_HOLE_REVIEW.json', 'ZERO_CROSSING_REVIEW.json'):
        obj = json.loads((BASE / name).read_text(encoding='utf-8-sig'))
        assert obj['verdict'] == 'PASS', name
        n = 0
        for field in ('audited_input_hashes', 'imported_dependency_hashes',
                      'reviewed_source_and_dependency_hashes'):
            for rel, expected in obj.get(field, {}).items():
                p = Path(rel) if Path(rel).is_absolute() else BASE / rel
                assert digest(p) == expected, (name, field, rel)
                n += 1
        imports[name] = {'sha256': digest(BASE / name), 'declared_hashes_verified': n}

    # Local endpoint lemma, including arbitrary same-parity prescribed edges.
    endpoint_cases = 0
    for t in range(1, 4):
        for h in (-2, 0, 2):
            ne, no = t + h // 2, t - h // 2
            for er, ey in itertools.product((-1, 1), repeat=2):
                if er + ey != h or (ne if er == 1 else no) == 0:
                    continue
                assert h - er - ey == 0  # free-target insertion
                assert h - er + ey == 2 * ey  # covered-target replacement
                assert (2*t - 2) in (0, 2, 4)
                endpoint_cases += 1

    G = {(0, 1), (0, 2), (1, 1), (1, 2), (1, 3),
         (2, 2), (2, 3), (2, 4), (3, 3)}
    B = {(0, 0), (0, 3), (0, 4), (1, 0), (1, 4),
         (2, 0), (2, 1), (3, 0), (3, 1), (3, 2), (3, 4)}
    assert G.isdisjoint(B) and G | B == set(itertools.product(range(4), range(5)))
    rows = []
    for a, b in sorted(G):
        for delta in (0, 1):
            port_diff = b-a-delta
            bridge = b-a-1  # -1 consumes even, +1 consumes odd
            minimum_c = None
            count = 0
            for c in range(1, 65):
                if c < abs(port_diff) or (c-port_diff) % 2:
                    continue
                pe, po = (c+port_diff)//2, (c-port_diff)//2
                # Each face has 32 vertices in each parity class.
                if a+delta+pe > 32 or b+po > 32:
                    continue
                if minimum_c is None:
                    minimum_c = c
                if delta == 0:
                    assert pe >= 1
                Dsize = (c - (1-delta) + abs(bridge))//2
                assert Dsize >= 0
                if delta or bridge:
                    assert Dsize >= 1
                local_A = (a+delta + (1-delta) - (bridge == -1),
                           b - (bridge == 1))
                assert local_A[0] == local_A[1]
                assert 2 <= sum(local_A) <= 6
                orig_B = (4-a-delta, 4-b)
                if not bridge:
                    holes = (orig_B[0]-(1-delta), orig_B[1])
                    assert holes == (3-a, 3-a) and 2 <= sum(holes) <= 6
                else:
                    ey = bridge  # even x -> odd y; odd x -> even y
                    nonterminal = (orig_B[0]-(1-delta)+(ey == 1),
                                   orig_B[1]+(ey == -1))
                    assert nonterminal[0]-nonterminal[1] == 2*ey
                    assert sum(nonterminal) in (2, 4, 6)
                    if delta:
                        for eq in (-1, 1):
                            terminal = (orig_B[0]+(eq == 1), orig_B[1]+(eq == -1))
                            assert terminal[0]-terminal[1] == eq+ey
                            assert sum(terminal) in (2, 4, 6)
                    else:
                        assert orig_B[0]-orig_B[1] == 1+ey
                        assert sum(orig_B) in (2, 4, 6)
                count += 1
            rows.append({'a': a, 'b': b, 'delta': delta,
                         'minimum_positive_c': minimum_c, 'feasible_c_counts': count})

    # All disjoint deleted-edge subsets of abstract paths on 3..14 vertices.
    # Root 0 is never on D; target n-1 is allowed on D and may be isolated.
    # A bridge x may be any nonterminal endpoint exposed by deletion.
    forest_cases = 0
    isolated_target_cases = 0
    for n in range(3, 15):
        for mask in range(1, 1 << (n-2)):
            deleted = {i+1 for i in range(n-2) if mask >> i & 1}
            if any(i+1 in deleted for i in deleted):
                continue
            edges = {(i, i+1) for i in range(n-1) if i not in deleted}
            exposed = {j for i in deleted for j in (i, i+1)}
            for bridge_x in [None] + sorted(exposed - {0, n-1}):
                graph = {i: set() for i in range(n)}
                for a, b in edges:
                    graph[a].add(b)
                    graph[b].add(a)
                for j in exposed:
                    new = n+j
                    graph[new] = {j}
                    graph[j].add(new)
                # Distinct attached B vertices preclude merging components.
                unseen = set(graph)
                terminal_components = []
                nonterminal = 0
                while unseen:
                    root = next(iter(unseen))
                    stack, comp = [root], set()
                    while stack:
                        q = stack.pop()
                        if q in comp:
                            continue
                        comp.add(q)
                        stack.extend(graph[q] - comp)
                    unseen -= comp
                    assert sum(len(graph[q]) for q in comp)//2 == len(comp)-1
                    assert all(1 <= len(graph[q]) <= 2 for q in comp)
                    ends = {q for q in comp if len(graph[q]) == 1}
                    assert len(ends) == 2
                    if comp & {0, n-1}:
                        terminal_components.append(comp)
                    else:
                        nonterminal += 1
                assert len(terminal_components) == 2
                assert nonterminal == len(deleted)-1
                if n-2 in deleted:
                    isolated_target_cases += 1
                forest_cases += 1

    result = {'verdict': 'PASS', 'import_hash_checks': imports,
              'local_endpoint_parity_cases': endpoint_cases, 'cut_rows': rows,
              'abstract_forest_cases': forest_cases,
              'covered_target_isolation_cases': isolated_target_cases,
              'full_eight_hole_geometry_enumerated': False,
              'arbitrary_matching_instances_enumerated': False,
              'universal_forest_proof_required': True}
    (BASE / 'Q7_EIGHT_NINE_CUTS_REVIEW_check.json').write_text(
        json.dumps(result, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False))


if __name__ == '__main__':
    run()
