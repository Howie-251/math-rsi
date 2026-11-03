"""Direct full adjacency-matrix checker, independent of bitsets/signature joins."""
import argparse
import json
from pathlib import Path


def check(c, edge_path=None):
    d, p, q = c['d'], c['p'], c['q']
    expected = set()
    for r in range(7):
        for i in range(5):
            for perm, step in ((p, 1), (q, 2)):
                expected.add(tuple(sorted((5*r+i, 5*perm[r]+(i+step)%5))))
    if edge_path:
        edges = [tuple(map(int, x.split())) for x in edge_path.read_text().splitlines()]
        assert len(edges) == len(set(edges)) and set(edges) == expected
    else:
        edges = expected
    a = [[0]*35 for _ in range(35)]
    for x, y in edges:
        assert x != y
        a[x][y] = a[y][x] = 1
    assert len(edges) == 70 and all(sum(row) == 4 for row in a)
    f = [z % 5 for z in range(35)]
    g = [(z % 5 + d[z//5]) % 5 for z in range(35)]
    colors_ok = all({colors[v] for v in range(35) if a[z][v] or v == z} == set(range(5))
                    for colors in (f, g) for z in range(35))
    matrix = [[sum(f[z] == i and g[z] == j for z in range(35)) for j in range(5)] for i in range(5)]
    rho, geometric = [], []
    for z in range(35):
        routes = [a[z][v] + sum(a[z][h]*a[h][v] for h in range(35)) for v in range(35)]
        rho.append(sum(max(routes[v] + (f[z] == f[v]) + (g[z] == g[v]) - 1, 0)
                       for v in range(35) if v != z))
        geometric.append(16-sum(routes[v] > 0 for v in range(35) if v != z)+matrix[f[z]][g[z]]-1)
    assert geometric == [r for r in c['rho_orbit'] for _ in range(5)]
    assert max(geometric) == c['max_rho'] and sum(geometric) == c['sum_rho']
    if colors_ok:
        assert rho == geometric
    return dict(edges=len(edges), degrees=[sum(row) for row in a], f=f, g=g,
                two_local_colorings=colors_ok, intersection=matrix, rho=rho,
                max_rho=max(rho), sum_rho=sum(rho),
                frontend_pass=colors_ok and max(rho) <= 4 and sum(rho) <= 130)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['sanity', 'result'])
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    if args.mode == 'sanity':
        cases = json.loads((root/'sanity_cpp.json').read_text())['cases']
        checked = [check(x['candidate']) for x in cases]
        assert all(c['two_local_colorings'] == x['signature_accept'] for c, x in zip(checked, cases))
        assert checked[0]['max_rho'] == 14
        print(json.dumps({'status': 'PASS', 'cases': checked}, indent=2))
    else:
        result = json.loads((root/'result.json').read_text())
        checked = check(result['candidate'], root/'candidate.edges')
        assert checked['two_local_colorings']
        assert checked['frontend_pass'] == (result['status'] == 'FRONTEND_FOUND')
        print(json.dumps(checked, indent=2))
