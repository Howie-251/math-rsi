"""Independent set-based check of saved edges and colors; no encoder import."""
from collections import Counter
from itertools import combinations
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def inspect(data, q=5):
    n = data['n']
    assert n == q*(q+2)
    raw = data['edges']
    assert all(len(ab) == 2 and 0 <= ab[0] < ab[1] < n for ab in raw)
    edges = set(map(tuple, raw))
    assert len(edges) == len(raw)
    adj = [set() for _ in range(n)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    f, g, A, P = data['f'], data['g'], set(data['A']), set(data['P'])
    assert len(f) == len(g) == n and all(0 <= x < q for x in f+g)
    balls = [adj[a] | {a} for a in A]
    packing = (len(A) == q+1 and sum(map(len, balls)) == len(set().union(*balls))
               and set(range(n))-set().union(*balls) == P
               and all(not adj[p].intersection(P) for p in P))
    stars = [range(q*s, q*(s+1)) for s in range(q+1)]
    target_colors = list(range(q))
    center_counts = Counter(g[a] for a in A)
    groups = dict(
        second_color_onehot=True,
        stars_P_and_center_colors=(all(sorted(g[v] for v in block) == target_colors
                                      for block in stars+[sorted(P)])
                                  and sorted(center_counts.values()) == [1]*(q-1)+[2]),
        all_permutation_intersection_grid=all(
            sum(f[v] == a and g[v] == b for v in range(n)) >= 1+int(a == b)
            for a in range(q) for b in range(q)),
        first_color_closed_neighborhoods=all(
            sorted(f[x] for x in adj[v] | {v}) == target_colors for v in range(n)),
        second_color_closed_neighborhoods=all(
            sorted(g[x] for x in adj[v] | {v}) == target_colors for v in range(n)),
        exact_actual_coverage_gates=True)
    cov = {}
    rho = [0]*n
    covered_counts = [0]*n
    for a, b in combinations(range(n), 2):
        routes = (int(b in adj[a]) + len(adj[a] & adj[b])
                  + int(f[a] == f[b]) + int(g[a] == g[b]))
        cov[a, b] = routes > 0
        covered_counts[a] += int(routes > 0)
        covered_counts[b] += int(routes > 0)
        rho[a] += max(0, routes-1)
        rho[b] += max(0, routes-1)

    def covered(a, b):
        return cov[min(a, b), max(a, b)]

    holes = {}
    if q == 5:
        groups['rho_capacities'] = (all(covered_counts[v] >= (25 if v in P else 24)
                                        for v in range(n)) and sum(cov.values()) >= 425)
        father_pass = all(covered(a, p) for a in A for p in P)
        for block in (A, P):
            for v in block:
                missing = {w for w in range(n) if w not in block and not covered(v, w)}
                holes[str(v)] = sorted(missing)
                father_pass &= len(missing) <= 5 and all(not (adj[w] & missing) for w in missing)
        groups['known_A_P_and_remaining_father_holes'] = father_pass
    matrix = [[sum(f[v] == a and g[v] == b for v in range(n))
               for b in range(q)] for a in range(q)]
    valid = (packing and all(groups.values()) and len(edges) == n*(q-1)//2
             and sorted(Counter(f[a] for a in A).values()) == [1]*(q-1)+[2]
             and all(len(row) == q-1 for row in adj))
    if valid and q == 5:
        assert rho == [28-c for c in covered_counts]
        assert max(rho) <= 4 and sum(rho) <= 130 and all(rho[p] <= 3 for p in P)
    return dict(valid_necessary_object=valid, target61_verified=False,
                n=n, edges=len(edges), degrees=list(map(len, adj)), packing=packing,
                groups=groups, intersection_matrix=matrix, rho=rho,
                max_rho=max(rho), sum_rho=sum(rho), covered_counts=covered_counts,
                unordered_covered=sum(cov.values()), remaining_father_holes=holes,
                covered=cov)


def main():
    data = json.loads((HERE/'candidate.json').read_text())
    lines = (HERE/'candidate.edges').read_text().splitlines()
    n, count = map(int, lines[0].split())
    edges = [list(map(int, line.split())) for line in lines[1:] if line.strip()]
    assert n == data['n'] and count == len(edges) and edges == data['edges']
    data['edges'] = edges
    result = inspect(data)
    del result['covered']
    (HERE/'candidate_check.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
    if not result['valid_necessary_object']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
