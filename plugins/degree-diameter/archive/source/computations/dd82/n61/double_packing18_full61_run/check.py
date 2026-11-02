"""Independent set/count/BFS checks; does not import the CNF encoder."""
from collections import Counter, deque
from itertools import combinations
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def adjacency(n, raw):
    assert all(len(ab) == 2 and 0 <= ab[0] < ab[1] < n for ab in raw)
    edges = set(map(tuple, raw))
    assert len(edges) == len(raw)
    adj = [set() for _ in range(n)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    return edges, adj


def original_edges(data):
    """Reconstruct by vertex neighborhoods, independently of CNF literals."""
    edges = set()
    def add(v, neighbors):
        for w in neighbors:
            assert v != w
            edges.add((min(v, w), max(v, w)))
    add(0, [1, 2, 3]+list(range(4, 9)))
    add(1, [2, 3]+list(range(9, 14)))
    add(2, range(14, 20))
    add(3, range(20, 26))
    s_to_t = [[0], [0], [4, 5], [1], [2], [3]]
    for x, row in enumerate(s_to_t):
        add(14+x, [20+y for y in row])
    for z in range(35):
        add(26+z, [4+data['f'][z], 9+data['g'][z],
                   14+data['S'][z], 20+data['T'][z]])
    for a, b in data['edges']:
        add(26+a, [26+b])
    return edges


def inspect(data, include_bfs=False):
    assert data['n'] == 35
    edges, adj = adjacency(35, data['edges'])
    f, g, s, t = [data[name] for name in ('f', 'g', 'S', 'T')]
    assert all(len(row) == 35 for row in (f, g, s, t))
    assert all(0 <= x < 5 for x in f+g) and all(0 <= x < 6 for x in s+t)
    A, AP, P, R = set(range(6)), set(range(6, 12)), set(range(12, 17)), set(range(17, 35))
    k = [[int(y in row) for y in range(6)] for row in ([0], [0], [4, 5], [1], [2], [3])]
    forced = {(a, 6+a) for a in A} | {(a, 17+3*a+j) for a in A for j in range(3)}
    allowed = forced | {(a, r) for a in AP|P for r in R} | set(combinations(sorted(R), 2))
    groups = {'onehot_incidence_maps': True}
    groups['double_packing_degree_split'] = (
        forced <= edges <= allowed and all(len(row) == 4 for row in adj)
        and all(len(adj[r] & AP) == 1 and len(adj[r] & (R|P)) == 2 for r in R)
        and all(len(adj[a] & R) == 3 for a in AP)
        and all(len(adj[p] & R) == 4 for p in P))
    ca, cb = Counter(g[v] for v in A), Counter(g[v] for v in AP)
    groups['legal_color_normalization'] = (
        f[:6] == [0, 0, 1, 2, 3, 4]
        and f[12:17] == g[12:17] == list(range(5))
        and Counter(f[v] for v in AP) == Counter([0, 1, 1, 2, 3, 4])
        and all(1 <= ca[b] <= 2 and 1 <= cb[b] <= 2 and ca[b]+cb[b] <= 3 for b in range(5))
        and all(f[17+3*a] < f[18+3*a] < f[19+3*a] for a in A))
    matrix = [[sum(f[v] == a and g[v] == b for v in range(35)) for b in range(5)]
              for a in range(5)]
    groups['color_sizes_and_M_ge_J'] = (
        all(Counter(row) == Counter({b: 7 for b in range(5)}) for row in (f, g))
        and all(value >= 1 for row in matrix for value in row))
    closed = [adj[z] | {z} for z in range(35)]
    groups['dual_local_bijections'] = all(
        sorted(colors[v] for v in closed[z]) == list(range(5))
        for colors in (f, g) for z in range(35))
    groups['full_parent_class_sizes'] = (
        all(s[v] == 0 for v in A) and all(s[v] == 1 for v in AP)
        and all(s[v] in range(2, 6) for v in R|P)
        and all(t[v] == 0 for v in P) and all(t[v] in range(1, 6) for v in set(range(35))-P)
        and [s.count(x) for x in range(6)] == [6, 6, 5, 6, 6, 6]
        and [t.count(y) for y in range(6)] == [5, 6, 6, 6, 6, 6])
    groups['full_S_T_independence'] = all(s[a] != s[b] and t[a] != t[b] for a, b in edges)
    color_marginals = True
    for parent, special in ((s, 2), (t, 0)):
        for colors in (f, g):
            for x in range(6):
                counts = Counter(colors[z] for z in range(35) if parent[z] == x)
                color_marginals &= all(1 <= counts[b] <= (1 if x == special else 2) for b in range(5))
    groups['full_parent_color_marginals'] = color_marginals

    def port_check(parent, other, transpose, support, row_sums):
        counts = [[sum(parent[v] == x for v in closed[z]) for z in range(35)] for x in range(6)]
        repeat = [[int(value >= 2) for value in row] for row in counts]
        valid = True
        for x in range(6):
            for z in range(35):
                blocked = k[other[z]][x] if transpose else k[x][other[z]]
                value = counts[x][z]
                valid &= (value == 0 if blocked else value in (1, 2))
                if repeat[x][z]:
                    valid &= support[z] and parent[z] != x
        valid &= [sum(row) for row in repeat] == row_sums
        valid &= all(sum(repeat[x][z] for x in range(6)) == int(support[z]) for z in range(35))
        return bool(valid), repeat

    groups['exact_S_closed_counts_and_beta'], beta = port_check(
        s, t, False, [z in P for z in range(35)], [0, 0, 2, 1, 1, 1])
    groups['exact_T_closed_counts_and_gamma'], gamma = port_check(
        t, s, True, [s[z] == 2 for z in range(35)], [2, 1, 1, 1, 0, 0])
    cross = [[sum(s[z] == x and t[z] == y for z in range(35)) for y in range(6)] for x in range(6)]
    groups['actual_ST_intersection_permutation'] = all(
        cross[x][y] == 0 if k[x][y] else cross[x][y] >= 1 for x in range(6) for y in range(6))
    original = original_edges(data)
    _, fulladj = adjacency(61, sorted(original))
    covered = {(a, b): b in fulladj[a] or bool(fulladj[a] & fulladj[b])
               for a, b in combinations(range(61), 2)}
    groups['all_1830_original_pairs_covered'] = all(covered.values())
    result = dict(groups=groups, valid_encoded_object=all(groups.values()),
                  n=61, edges=len(original), degrees=list(map(len, fulladj)),
                  H_edges=len(edges), H_degrees=list(map(len, adj)), intersection_matrix=matrix,
                  ST_intersection=cross, beta_row_sums=list(map(sum, beta)),
                  gamma_row_sums=list(map(sum, gamma)), uncovered_pairs=[list(ab) for ab, ok in covered.items() if not ok],
                  covered=covered, original_edges=original, target61_verified=False)
    if include_bfs:
        unreachable, far, diameter = [], [], 0
        for root in range(61):
            distance = {root: 0}
            queue = deque([root])
            while queue:
                v = queue.popleft()
                for w in fulladj[v]:
                    if w not in distance:
                        distance[w] = distance[v]+1
                        queue.append(w)
            for v in range(root+1, 61):
                if v not in distance:
                    unreachable.append([root, v])
                elif distance[v] > 2:
                    far.append([root, v, distance[v]])
            diameter = max(diameter, max(distance.values()))
        uv_defect = len(fulladj[0] & fulladj[1])+int(1 in fulladj[0])-1
        epsilon = int(20 in fulladj[16])  # q=S2, p=T0
        eta = len(fulladj[16] & fulladj[20])+epsilon-1
        graph_valid = (len(original) == 244 and all(len(row) == 8 for row in fulladj)
                       and not unreachable and not far and diameter <= 2)
        result.update(bfs_diameter=None if unreachable else diameter,
                      unreachable_pairs=unreachable, pairs_beyond_two=far,
                      uv_adjacent_double=(1 in fulladj[0] and uv_defect == 2),
                      epsilon=epsilon, eta=eta,
                      target61_verified=(graph_valid and all(groups.values()) and uv_defect == 2
                                         and epsilon == 0 and eta in (0, 1)))
    return result


def main():
    data = json.loads((HERE/'candidate_h35.json').read_text())
    result = inspect(data, include_bfs=True)
    reported = json.loads((HERE/'candidate.json').read_text())
    lines = (HERE/'candidate.edges').read_text().splitlines()
    n, count = map(int, lines[0].split())
    raw = [list(map(int, line.split())) for line in lines[1:] if line.strip()]
    actual_edges, _ = adjacency(61, raw)
    assert n == reported['n'] == 61 and count == len(raw)
    assert raw == reported['edges'] and actual_edges == result['original_edges']
    del result['covered'], result['original_edges']
    (HERE/'candidate_check.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
    if not result['target61_verified']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
