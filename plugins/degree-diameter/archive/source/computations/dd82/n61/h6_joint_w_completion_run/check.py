"""Independent actual-edge set/count/BFS validation; no encoder imports."""
from collections import deque
from itertools import combinations
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def inspect(data, include_bfs=False):
    assert data['n'] == 61
    raw = data['edges']
    assert all(len(ab) == 2 and 0 <= ab[0] < ab[1] < 61 for ab in raw)
    edges = set(map(tuple, raw))
    assert len(edges) == len(raw)
    adj = [set() for _ in range(61)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    common = {(a, b): len(adj[a] & adj[b]) for a, b in combinations(range(61), 2)}
    covered = {ab: ab in edges or c >= 1 for ab, c in common.items()}
    s, u, v, r = set(range(2, 5)), set(range(5, 10)), set(range(10, 15)), set(range(15, 61))
    root_neighbors_exact = adj[0] == s|u and adj[1] == s|v
    root_triangles = [sum(b in adj[a] for a, b in combinations(sorted(adj[x]), 2)) for x in (0, 1)]
    branch_structure = root_neighbors_exact and root_triangles == [0, 0]
    wgroups=[set(range(15+6*i,21+6*i)) for i in range(3)]
    wall=set.union(*wgroups); cc=set(range(33,61))
    uv={(5,11),(5,12),(6,10),(7,10),(8,13),(9,14)}
    fixed=({(0,x) for x in s|u}|{(1,x) for x in s|v}|uv
           |{(parent,w) for parent,group in zip(sorted(s),wgroups) for w in group}
           |{(15+i,15+6*j+i) for i in range(6) for j in (1,2)})
    allowed=({(p,r) for p in u|v for r in wall|cc}
             |{(a,b) for a in wgroups[1] for b in wgroups[2]}
             |{(w,c) for w in wall for c in cc}|set(combinations(sorted(cc),2)))
    branch_structure=branch_structure and fixed <= edges <= fixed|allowed
    front=(all(len(adj[a]&wgroups[2])==1 for a in wgroups[1])
           and all(len(adj[b]&wgroups[1])==1 for b in wgroups[2])
           and all(sum(len(adj[p]&wall) for p in parents)==1 for parents in (u,v))
           and all(len(adj[c]&parents)==1 for c in cc for parents in (u,v))
           and all(len(adj[w]&(u|v))<=1 for w in wall)
           and all(all(adj[c]&group for group in wgroups) and len(adj[c]&wall)<=5 for c in cc))
    vectors = [tuple(int(p in adj[x]) for p in range(5, 15)) for x in range(33,61)]
    groups = dict(
        complete_h6_frontend=front,
        all_original_degrees_8=all(len(row) == 8 for row in adj),
        exact_common_and_coverage_definitions=True,
        all_1830_original_pairs_covered=all(covered.values()),
        global_common_at_most_3=all(c <= 3 for c in common.values()),
        adjacent_common_at_most_1=all(common[ab] <= 1 for ab in edges),
        selected_roots_no_other_double=all(c <= 2 for ab, c in common.items()
                                         if (0 in ab or 1 in ab) and ab != (0, 1)),
        C_parent_vectors_nonincreasing_lex=all(a >= b for a, b in zip(vectors, vectors[1:])))
    result = dict(groups=groups, fixed_branch_structure=branch_structure,
                  valid_encoded_object=branch_structure and all(groups.values()),
                  n=61, edges=len(edges), degrees=list(map(len, adj)),
                  root_common_neighbors=sorted(adj[0] & adj[1]),
                  root_triangle_counts=root_triangles,
                  uv_nonadjacent_double=((0, 1) not in edges and common[0, 1] == 3),
                  selected_root_other_double_pairs=[list(ab) for ab, c in common.items()
                      if (0 in ab or 1 in ab) and ab != (0, 1) and c >= 3],
                  h=sum(b in adj[a] for a in u for b in v),
                  W_sizes=[len(adj[x] & r) for x in sorted(s)],
                  common=common, covered=covered, original_edges=edges,
                  target61_verified=False)
    if include_bfs:
        unreachable, far, diameter = [], [], 0
        for root in range(61):
            distance = {root: 0}
            queue = deque([root])
            while queue:
                x = queue.popleft()
                for y in adj[x]:
                    if y not in distance:
                        distance[y] = distance[x]+1
                        queue.append(y)
            for y in range(root+1, 61):
                if y not in distance:
                    unreachable.append([root, y])
                elif distance[y] > 2:
                    far.append([root, y, distance[y]])
            diameter = max(diameter, max(distance.values()))
        graph_valid = (len(edges) == 244 and all(len(row) == 8 for row in adj)
                       and not unreachable and not far and diameter <= 2)
        result.update(bfs_diameter=None if unreachable else diameter,
                      unreachable_pairs=unreachable, pairs_beyond_two=far,
                      target61_verified=graph_valid and result['valid_encoded_object']
                                        and result['uv_nonadjacent_double'])
    return result


def main():
    data = json.loads((HERE/'candidate.json').read_text())
    result = inspect(data, include_bfs=True)
    lines = (HERE/'candidate.edges').read_text().splitlines()
    n, count = map(int, lines[0].split())
    raw = [list(map(int, line.split())) for line in lines[1:] if line.strip()]
    assert n == 61 and count == len(raw) and raw == data['edges']
    assert set(map(tuple, raw)) == result['original_edges']
    for name in ('common', 'covered', 'original_edges'):
        del result[name]
    (HERE/'candidate_check.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
    if not result['target61_verified']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
