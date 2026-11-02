"""Recover six affine-line relations from the public Dhar 810 adjacency list.

The reconstruction is derived from the edge data, not an author-supplied chart.
Coordinates use little-endian ternary labels x0 + 3*x1 + 9*x2.
No graph search or hashing is performed.
"""
from pathlib import Path
from itertools import product
import json

HERE = Path(__file__).resolve().parent


def vec(n):
    return tuple((n // 3**i) % 3 for i in range(3))


def code(v):
    return sum(int(x) * 3**i for i, x in enumerate(v))


def add(x, y):
    return tuple((a + b) % 3 for a, b in zip(x, y))


def scale(k, x):
    return tuple((k * a) % 3 for a in x)


def mv(M, x):
    return tuple(sum(a * b for a, b in zip(row, x)) % 3 for row in M)


def det(M):
    a, b, c = M
    return (a[0]*(b[1]*c[2]-b[2]*c[1]) - a[1]*(b[0]*c[2]-b[2]*c[0])
            + a[2]*(b[0]*c[1]-b[1]*c[0])) % 3


def main():
    rows = [list(map(int, line.split())) for line in (HERE / 'dhar810.txt').read_text().splitlines()
            if line and not line.startswith('#')]
    adj = {row[0]: set(row[1:]) for row in rows}
    assert set(adj) == set(range(810))
    assert all(len(ns) == 12 and u not in ns and all(u in adj[v] for v in ns)
               for u, ns in adj.items())
    chart = []
    for i in range(3):
        controls = sorted({(v//270, (v//27)%10) for v in adj[i*270] if v//270 > i})
        for j, a in controls:
            lines = [{v % 27 for v in adj[i*270+x] if (v//270, (v//27)%10) == (j, a)}
                     for x in range(27)]
            assert all(len(line) == 3 for line in lines)
            zline = sorted(lines[0])
            u = vec(zline[0])
            b = add(vec(zline[1]), scale(-1, u))
            assert {code(add(u, scale(t,b))) for t in range(3)} == lines[0]
            columns0 = [add(vec(min(lines[3**k])), scale(-1,u)) for k in range(3)]
            found = None
            for shifts in product(range(3), repeat=3):
                cols = [add(v, scale(t,b)) for v,t in zip(columns0,shifts)]
                M = tuple(tuple(cols[c][r] for c in range(3)) for r in range(3))
                if det(M) and all({code(add(add(mv(M,vec(x)),u),scale(t,b))) for t in range(3)}
                                  == lines[x] for x in range(27)):
                    found=M; break
            assert found is not None, (i,j,a)
            chart.append(dict(i=i,j=j,a=a,M=found,u=u,b=b))
    rebuilt = [set() for _ in range(810)]
    for e in chart:
        for z in range(10):
            for x in range(27):
                source=e['i']*270+z*27+x
                for t in range(3):
                    y=code(add(add(mv(e['M'],vec(x)),e['u']),scale(t,e['b'])))
                    target=e['j']*270+((z+e['a'])%10)*27+y
                    rebuilt[source].add(target);rebuilt[target].add(source)
    assert all(rebuilt[u] == ns for u,ns in adj.items())
    result=dict(status='exact_reconstruction_of_public_edge_data',q=3,s=3,m=10,
                vertex_label='i*(27*m)+z*27+x0+3*x1+9*x2',
                relation='(i,z,x) -- (j,z+a mod m,M*x+u+lambda*b), lambda in F3',
                author_chart=False,darts=chart,edge_count=sum(map(len,rebuilt))//2)
    (HERE/'dhar810_recovered_chart.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
